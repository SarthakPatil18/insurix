"""Query and Streaming Reasoning API Endpoints."""

import json
import uuid
from datetime import datetime, timezone
from typing import List, Optional
from fastapi import APIRouter, Depends, Query
from fastapi.responses import StreamingResponse

from backend.models.schemas import (
    QueryRequest,
    QueryResponse,
    QueryHistoryItem,
    DISCLAIMER_TEXT,
    CostEstimate
)
from backend.services.vector_service import hybrid_search
from backend.services.rule_engine import evaluate_scenario
from backend.services.llm_service import generate_grounded_answer
from backend.services.uncertainty_service import compute_uncertainty
from backend.services.cost_service import load_treatments, get_treatment_by_id
from backend.api.policy import get_policy_dict
from backend.api.deps import get_session_id
from backend.core.errors import NotFoundError

router = APIRouter(prefix="/api/query", tags=["query"])

_query_history_store: List[dict] = []


def _resolve_query(req: QueryRequest) -> QueryResponse:
    policy_id = req.policy_id or "star"
    policy = get_policy_dict(policy_id)
    if not policy:
        raise NotFoundError(f"Policy '{policy_id}' not found.")

    # 1. Retrieve evidence clauses using hybrid search
    evidence = hybrid_search(req.question, policy_id=policy_id, top_k=5)

    # 2. Evaluate financial scenario if treatment specified or question is procedural
    cost_estimate = None
    trace = []
    verdict = "conditional"
    verdict_label = "COVERED — WITH DEDUCTIONS"

    t_in = req.treatment
    treatment_id = t_in.id if (t_in and t_in.id) else None
    
    # Keyword inference if treatment not explicitly provided
    if not treatment_id:
        q_low = req.question.lower()
        if "knee" in q_low or "arthroplasty" in q_low:
            treatment_id = "knee_replacement"
        elif "cataract" in q_low or "eye" in q_low or "lens" in q_low:
            treatment_id = "cataract"
        elif "append" in q_low:
            treatment_id = "appendectomy"
        elif "cabg" in q_low or "bypass" in q_low or "heart" in q_low:
            treatment_id = "cabg"
        elif "dialysis" in q_low:
            treatment_id = "dialysis"

    treatment_data = get_treatment_by_id(treatment_id) if treatment_id else None

    if treatment_data:
        cost = t_in.cost if (t_in and t_in.cost) else treatment_data.get("average", 50000)
        hosp = t_in.hospital if (t_in and t_in.hospital) else "network"
        room = t_in.room if (t_in and t_in.room) else "within_limit"
        age = t_in.age_band if (t_in and t_in.age_band) else 45
        tenure = t_in.tenure_months if (t_in and t_in.tenure_months is not None) else 36
        ped = t_in.ped if (t_in and t_in.ped is not None) else False
        wait = "partial" if (tenure < 24) else "completed"

        verdict, verdict_label, cost_estimate, trace = evaluate_scenario(
            policy=policy,
            treatment=treatment_data,
            cost=cost,
            hospital=hosp,
            room=room,
            age=age,
            tenure_months=tenure,
            waiting_status=wait,
            ped=ped
        )

    # 3. Uncertainty evaluation
    uncertainty = compute_uncertainty(
        evidence=evidence,
        room_penalty_applied=any(l.label.startswith("Room Rent") for l in (cost_estimate.lines if cost_estimate else [])),
        is_non_network=(t_in.hospital == "non_network") if t_in else False
    )

    # 4. Synthesize answer with citations
    from backend.services.llm_service import deterministic_synthesize_answer
    answer_text = deterministic_synthesize_answer(
        question=req.question,
        policy_name=policy.get("policy_name", "Policy"),
        verdict=verdict,
        evidence=evidence,
        cost_estimate=cost_estimate.model_dump() if cost_estimate else None
    )

    response = QueryResponse(
        answer=answer_text,
        verdict=verdict,
        verdict_label=verdict_label,
        confidence=uncertainty.confidence,
        evidence=evidence,
        cost_estimate=cost_estimate,
        uncertainty=uncertainty,
        trace=trace,
        disclaimer=DISCLAIMER_TEXT
    )

    # Record in query history
    _query_history_store.append({
        "id": str(uuid.uuid4()),
        "policy_id": policy_id,
        "question": req.question,
        "verdict": verdict,
        "confidence": uncertainty.confidence,
        "payable": cost_estimate.payable if cost_estimate else 0,
        "created_at": datetime.now(timezone.utc).isoformat()
    })

    return response


@router.post("", response_model=QueryResponse, summary="Query policy with grounded evidence citations")
async def query_policy(req: QueryRequest):
    return _resolve_query(req)


@router.post("/stream", summary="Stream query evaluation reasoning traces via Server-Sent Events")
async def query_stream(req: QueryRequest):
    response = _resolve_query(req)

    async def event_generator():
        # Stream trace events
        for step in response.trace:
            event_payload = json.dumps({"event": "trace", "rule": step.rule, "detail": step.detail})
            yield f"data: {event_payload}\n\n"
        
        # Stream final response
        final_payload = json.dumps({"event": "complete", "response": response.model_dump()})
        yield f"data: {final_payload}\n\n"

    return StreamingResponse(event_generator(), media_type="text/event-stream")


@router.get("/history", response_model=List[QueryHistoryItem], summary="Get past query evaluations")
async def get_query_history(policy_id: Optional[str] = Query(default=None)):
    if policy_id:
        items = [q for q in _query_history_store if q.get("policy_id") == policy_id]
    else:
        items = _query_history_store

    return [
        QueryHistoryItem(
            id=item["id"],
            question=item["question"],
            verdict=item["verdict"],
            confidence=item["confidence"],
            payable=item["payable"],
            created_at=item["created_at"]
        )
        for item in reversed(items[-50:])
    ]
