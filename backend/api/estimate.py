"""Out-of-Pocket Cost Estimation and Treatment Catalogue API Endpoints."""

from typing import List
from fastapi import APIRouter
from backend.models.schemas import (
    EstimateRequest,
    EstimateResponse,
    TreatmentListItem,
    TreatmentDetail,
    DISCLAIMER_TEXT
)
from backend.services.cost_service import load_treatments, get_treatment_by_id
from backend.services.rule_engine import evaluate_scenario
from backend.services.vector_service import hybrid_search
from backend.services.uncertainty_service import compute_uncertainty
from backend.api.policy import get_policy_dict
from backend.core.errors import NotFoundError

router = APIRouter(prefix="/api", tags=["estimate"])


@router.post("/estimate", response_model=EstimateResponse, summary="Calculate exact out-of-pocket medical estimate")
async def calculate_estimate(req: EstimateRequest):
    policy = get_policy_dict(req.policy_id)
    if not policy:
        raise NotFoundError(f"Policy '{req.policy_id}' not found.")

    treatment = get_treatment_by_id(req.treatment_id)
    if not treatment:
        raise NotFoundError(f"Treatment '{req.treatment_id}' not found in medical catalogue.")

    cost = req.cost if (req.cost and req.cost > 0) else treatment.get("average", 50000)
    wait_status = "partial" if (req.tenure_months < 24) else "completed"

    verdict, verdict_label, estimate, trace = evaluate_scenario(
        policy=policy,
        treatment=treatment,
        cost=cost,
        hospital=req.hospital,
        room=req.room,
        age=req.age_band or 45,
        tenure_months=req.tenure_months or 36,
        waiting_status=wait_status,
        ped=req.ped or False
    )

    evidence = hybrid_search(treatment["name"], policy_id=req.policy_id, top_k=3)

    uncertainty = compute_uncertainty(
        evidence=evidence,
        room_penalty_applied=any(l.label.startswith("Room Rent") for l in estimate.lines),
        is_non_network=(req.hospital == "non_network")
    )

    return EstimateResponse(
        cost_estimate=estimate,
        trace=trace,
        confidence=uncertainty.confidence,
        uncertainty=uncertainty,
        evidence=evidence,
        disclaimer=DISCLAIMER_TEXT
    )


@router.get("/treatments", response_model=List[TreatmentListItem], summary="List all indexed procedures")
async def list_treatments():
    treatments = load_treatments()
    return [
        TreatmentListItem(
            id=t["id"],
            name=t["name"],
            category=t["category"],
            icd=t.get("icd"),
            cost_range=t.get("cost_range"),
            average=t.get("average", 0)
        )
        for t in treatments.values()
    ]


@router.get("/treatments/{id}", response_model=TreatmentDetail, summary="Get full treatment details with head-wise cost breakdown")
async def get_treatment_detail(id: str):
    treatment = get_treatment_by_id(id)
    if not treatment:
        raise NotFoundError(f"Treatment '{id}' not found in medical catalogue.")
    return TreatmentDetail(**treatment)
