"""Uncertainty Evaluation & Confidence Scoring Service."""

from typing import List, Optional
from backend.models.schemas import ConfidenceType, UncertaintyInfo, EvidenceCitation


def compute_uncertainty(
    evidence: List[EvidenceCitation],
    room_penalty_applied: bool = False,
    is_non_network: bool = False,
    age_ambiguity: bool = False,
    modelled_bill: bool = True
) -> UncertaintyInfo:
    """Computes confidence tier and compiles missing information checklist."""
    # 1. Base confidence from top retrieval score
    top_score = evidence[0].score if evidence else 0.0

    if top_score >= 8.0:
        base_conf: ConfidenceType = "high"
    elif top_score >= 4.0:
        base_conf: ConfidenceType = "medium"
    elif top_score >= 1.5:
        base_conf: ConfidenceType = "low"
    else:
        base_conf: ConfidenceType = "insufficient"

    missing_info: List[str] = []

    # 2. Engine downgrades
    downgrade_steps = 0
    if room_penalty_applied:
        missing_info.append("Choice of exact room tier (Single Standard vs Deluxe / Suite).")
        downgrade_steps += 1

    if is_non_network:
        missing_info.append("Hospital non-network tariff tariff schedule benchmarks.")
        downgrade_steps += 1

    if age_ambiguity:
        missing_info.append("Exact insured date of birth for senior citizen co-payment tier.")
        downgrade_steps += 1

    if modelled_bill:
        missing_info.append("Itemized hospital estimate separating surgeon, pharmacy, and consumables.")

    # Apply downgrades
    conf_ladder = ["high", "medium", "low", "insufficient"]
    curr_idx = conf_ladder.index(base_conf)
    new_idx = min(len(conf_ladder) - 1, curr_idx + downgrade_steps)
    final_conf: ConfidenceType = conf_ladder[new_idx]

    # Templated recommendation
    if is_non_network:
        recommendation = "Seek treatment at an empanelled Network Provider to prevent non-network tariff deductions and ensure cashless pre-authorization."
    elif room_penalty_applied:
        recommendation = "Select a Single Standard A/C Room or stay strictly within your entitled room rent limit to prevent proportionate billing deductions."
    elif final_conf == "insufficient":
        recommendation = "Provide your complete policy wording document or endorsement schedule to verify specific clause terms."
    else:
        recommendation = "Obtain cashless pre-authorization from the hospital TPA desk at least 48 hours prior to planned admission."

    return UncertaintyInfo(
        confidence=final_conf,
        missing_info=missing_info,
        recommendation=recommendation
    )
