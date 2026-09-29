"""API Contract Tests against RESEARCH §7 and UI Response Schema."""

import io
import pytest


def test_health_endpoint(client):
    res = client.get("/health")
    assert res.status_code == 200
    data = res.json()
    assert "status" in data
    assert "db" in data
    assert "vector_store" in data
    assert "embedding" in data
    assert "llm" in data
    assert "degraded" in data
    assert isinstance(data["degraded"], list)


def test_root_endpoint(client):
    res = client.get("/")
    assert res.status_code == 200
    data = res.json()
    assert data["status"] == "operational"
    assert "disclaimer" in data


def test_policy_endpoints(client):
    # 1. Summary
    res = client.get("/api/policy/star/summary")
    assert res.status_code == 200
    data = res.json()
    assert data["id"] == "star"
    assert data["sum_insured"] == 500000

    # 2. Coverage
    cov_res = client.get("/api/policy/star/coverage")
    assert cov_res.status_code == 200
    cov_data = cov_res.json()
    assert cov_data["policy_id"] == "star"
    assert len(cov_data["inclusions"]) > 0

    # 3. Exclusions
    excl_res = client.get("/api/policy/star/exclusions")
    assert excl_res.status_code == 200
    excl_data = excl_res.json()
    assert len(excl_data["exclusions"]) > 0


def test_treatments_endpoints(client):
    # 1. List
    res = client.get("/api/treatments")
    assert res.status_code == 200
    items = res.json()
    assert isinstance(items, list)
    assert len(items) >= 5

    # 2. Detail
    det_res = client.get("/api/treatments/cataract")
    assert det_res.status_code == 200
    detail = det_res.json()
    assert detail["id"] == "cataract"
    assert "heads" in detail


def test_query_endpoint(client):
    payload = {
        "question": "Is cataract surgery covered under Star Health?",
        "policy_id": "star"
    }
    res = client.post("/api/query", json=payload)
    assert res.status_code == 200
    data = res.json()

    # Assert exact UI contract schema
    assert "answer" in data
    assert "verdict" in data
    assert "verdict_label" in data
    assert "confidence" in data
    assert "evidence" in data
    assert "cost_estimate" in data
    assert "uncertainty" in data
    assert "trace" in data
    assert "disclaimer" in data

    # Assert evidence citations have required fields
    if data["evidence"]:
        ev = data["evidence"][0]
        assert "text" in ev
        assert "page" in ev
        assert "section" in ev
        assert "score" in ev


def test_estimate_endpoint(client):
    payload = {
        "policy_id": "star",
        "treatment_id": "knee_replacement",
        "cost": 280000,
        "days": 4,
        "hospital": "network",
        "room": "within_limit",
        "age_band": 45,
        "tenure_months": 36,
        "ped": False
    }
    res = client.post("/api/estimate", json=payload)
    assert res.status_code == 200
    data = res.json()
    assert "cost_estimate" in data
    assert "trace" in data
    assert "uncertainty" in data
    est = data["cost_estimate"]
    assert est["total_cost"] == 280000
    assert est["total_cost"] - est["deduction_total"] == est["payable"]


def test_document_upload_and_delete(client):
    # Minimal valid PDF file with %PDF magic header
    pdf_bytes = b"%PDF-1.4\n1 0 obj\n<< /Type /Catalog >>\nendobj\ntrailer\n<< /Root 1 0 R >>\n%%EOF"
    files = {"file": ("test_policy.pdf", io.BytesIO(pdf_bytes), "application/pdf")}

    # 1. Upload
    up_res = client.post("/api/documents/upload", files=files)
    assert up_res.status_code == 201
    up_data = up_res.json()
    doc_id = up_data["document_id"]
    assert up_data["file_name"] == "test_policy.pdf"

    # 2. Get
    get_res = client.get(f"/api/documents/{doc_id}")
    assert get_res.status_code == 200
    assert get_res.json()["document_id"] == doc_id

    # 3. Delete
    del_res = client.delete(f"/api/documents/{doc_id}")
    assert del_res.status_code == 204

    # 4. Confirm 404 after delete
    get_after = client.get(f"/api/documents/{doc_id}")
    assert get_after.status_code == 404
