"""Tests for Dense + BM25 Hybrid Retrieval and Exclusion Guarantee."""

import pytest
from backend.services.vector_service import hybrid_search, register_in_memory_chunks


@pytest.fixture(autouse=True)
def setup_policy_chunks():
    chunks = [
        {
            "ord": 1,
            "section": "4.2",
            "heading": "Joint Replacement",
            "page": 18,
            "text": "Total Knee Replacement surgery is covered as a medically necessary procedure under Section 4.2."
        },
        {
            "ord": 2,
            "section": "5.1",
            "heading": "Exclusions: Pre-Existing Diseases",
            "page": 12,
            "text": "Pre-existing conditions and joint replacement waiting period applies for 36 continuous months."
        },
        {
            "ord": 3,
            "section": "6.3",
            "heading": "Cataract Capping",
            "page": 22,
            "text": "Cataract surgery with intraocular lens is limited to ₹25,000 per eye."
        }
    ]
    register_in_memory_chunks("test_policy", chunks)


def test_hybrid_search_retrieves_relevant_clause():
    results = hybrid_search("knee replacement surgery", policy_id="test_policy", top_k=2)
    assert len(results) >= 1
    assert any("Knee Replacement" in r.text for r in results)
    assert results[0].page in [12, 18]


def test_exclusion_guarantee_appends_exclusion():
    results = hybrid_search("knee replacement", policy_id="test_policy", top_k=5)
    # The exclusion guarantee ensures that when joint replacement is granted, the waiting/exclusion clause is surfaced
    has_exclusion_clause = any("waiting period" in r.text.lower() or "exclusion" in r.text.lower() for r in results)
    assert has_exclusion_clause is True
