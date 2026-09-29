"""Policy Specifications, Coverage Inclusions, and Exclusions API Endpoints."""

import json
from pathlib import Path
from typing import Dict, Any, Optional, List
from fastapi import APIRouter
from backend.models.schemas import (
    PolicySummaryResponse,
    PolicyCoverageResponse,
    PolicyExclusionsResponse,
    ExclusionCluster,
    EvidenceCitation
)
from backend.core.errors import NotFoundError
from backend.services.vector_service import register_in_memory_chunks

router = APIRouter(prefix="/api/policy", tags=["policy"])

_policies_cache: Optional[Dict[str, Any]] = None


def load_sample_policies() -> Dict[str, Any]:
    global _policies_cache
    if _policies_cache is not None:
        return _policies_cache

    data_path = Path(__file__).resolve().parent.parent / "data" / "sample_policies.json"
    if data_path.exists():
        with open(data_path, "r", encoding="utf-8") as f:
            _policies_cache = json.load(f)
            # Register in-memory chunks for preloaded policies
            for p_id, p_data in _policies_cache.items():
                clauses = p_data.get("clauses", [])
                chunks = []
                for idx, c in enumerate(clauses):
                    chunks.append({
                        "ord": idx + 1,
                        "section": c.get("section", "1.0"),
                        "heading": c.get("heading", "Clause"),
                        "page": c.get("page", 1),
                        "text": c.get("text", ""),
                        "tokens": len(c.get("text", "")) // 4
                    })
                register_in_memory_chunks(p_id, chunks)
    else:
        _policies_cache = {}

    return _policies_cache


def get_policy_dict(policy_id: str) -> Optional[Dict[str, Any]]:
    policies = load_sample_policies()
    return policies.get(policy_id)


@router.get("/{id}/summary", response_model=PolicySummaryResponse, summary="Get policy schedule, limits, and clocks")
async def get_policy_summary(id: str):
    p = get_policy_dict(id)
    if not p:
        raise NotFoundError(f"Policy '{id}' not found.")

    return PolicySummaryResponse(
        id=p["id"],
        insurer=p["insurer"],
        policy_name=p["policy_name"],
        sum_insured=p["sum_insured"],
        policy_period=p["policy_period"],
        waiting_periods=p["waiting_periods"],
        room_rent_limit=p["room_rent_limit"],
        icu_limit=p["icu_limit"],
        co_payment=p["co_payment"],
        sub_limits=p["sub_limits"],
        proportionality=p.get("proportionality", True),
        deductible=p.get("deductible", 0)
    )


@router.get("/{id}/coverage", response_model=PolicyCoverageResponse, summary="Get inclusions and covered benefits")
async def get_policy_coverage(id: str):
    p = get_policy_dict(id)
    if not p:
        raise NotFoundError(f"Policy '{id}' not found.")

    clauses = p.get("clauses", [])
    inclusions = [
        EvidenceCitation(
            text=c["text"],
            page=c.get("page", 1),
            section=c.get("section", "1.0"),
            score=10.0,
            policy_id=id
        )
        for c in clauses if "exclu" not in c.get("heading", "").lower()
    ]

    return PolicyCoverageResponse(
        policy_id=id,
        inclusions=inclusions
    )


@router.get("/{id}/exclusions", response_model=PolicyExclusionsResponse, summary="Get exclusion clusters and statutory exclusions")
async def get_policy_exclusions(id: str):
    p = get_policy_dict(id)
    if not p:
        raise NotFoundError(f"Policy '{id}' not found.")

    clauses = p.get("clauses", [])
    excl_clauses = [
        EvidenceCitation(
            text=c["text"],
            page=c.get("page", 1),
            section=c.get("section", "Excl"),
            score=10.0,
            policy_id=id
        )
        for c in clauses if "exclu" in c.get("heading", "").lower() or "waiting" in c.get("heading", "").lower()
    ]

    cluster = ExclusionCluster(
        irdai_code="IRDAI-HLT-EXCL",
        title="Statutory and Specific Policy Exclusions",
        description="Non-medical consumables, pre-existing conditions during waiting period, and cosmetic treatments.",
        clauses=excl_clauses
    )

    return PolicyExclusionsResponse(
        policy_id=id,
        exclusions=[cluster]
    )
