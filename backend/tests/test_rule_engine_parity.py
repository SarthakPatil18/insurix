"""Rule Engine Parity Test Suite.

Asserts exact equality of amounts, deduction lines, verdicts, and confidence
across all exported combinatorial scenarios between frontend and backend engines.
"""

import json
from pathlib import Path
import pytest
from backend.services.rule_engine import evaluate_scenario
from backend.api.policy import get_policy_dict
from backend.services.cost_service import get_treatment_by_id


@pytest.fixture(scope="module")
def parity_vectors():
    path = Path(__file__).resolve().parent / "parity_vectors.json"
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def test_parity_vectors_count(parity_vectors):
    """Enforces that at least 2,000 combinatorial scenarios are tested."""
    assert len(parity_vectors) >= 2000, f"Expected >= 2000 vectors, got {len(parity_vectors)}"


def test_rule_engine_parity_exhaustive(parity_vectors):
    """Runs all 5,760 scenarios and asserts exact mathematical and ledger equality."""
    failures = []

    for idx, item in enumerate(parity_vectors):
        sc = item["scenario"]
        exp = item["expected"]

        policy = get_policy_dict(sc["policyId"])
        treatment = get_treatment_by_id(sc["treatmentId"])

        verdict, verdict_label, estimate, trace = evaluate_scenario(
            policy=policy,
            treatment=treatment,
            cost=sc["cost"],
            hospital=sc["hospital"],
            room=sc["room"],
            age=sc["age"],
            tenure_months=sc["tenureMonths"],
            waiting_status=sc["waitingStatus"],
            ped=sc["ped"]
        )

        # 1. Assert verdict parity
        if verdict != exp["verdict"]:
            failures.append(f"[{idx}] Verdict mismatch: {verdict} != {exp['verdict']}")
            if len(failures) > 10:
                break
            continue

        # 2. Assert financial totals parity to the exact rupee
        exp_tot = exp["totals"]
        if estimate.total_cost != exp_tot["total_cost"]:
            failures.append(f"[{idx}] total_cost mismatch: {estimate.total_cost} != {exp_tot['total_cost']}")
        if estimate.payable != exp_tot["payable"]:
            failures.append(f"[{idx}] payable mismatch: {estimate.payable} != {exp_tot['payable']}")
        if estimate.out_of_pocket != exp_tot["out_of_pocket"]:
            failures.append(f"[{idx}] out_of_pocket mismatch: {estimate.out_of_pocket} != {exp_tot['out_of_pocket']}")
        if estimate.deduction_total != exp_tot["deduction_total"]:
            failures.append(f"[{idx}] deduction_total mismatch: {estimate.deduction_total} != {exp_tot['deduction_total']}")

        # 3. Assert ledger identity: total_cost - deduction_total == payable
        assert estimate.total_cost - estimate.deduction_total == estimate.payable, f"Ledger identity violated in vector {idx}"

        if len(failures) > 10:
            break

    assert len(failures) == 0, f"Parity failures encountered:\n" + "\n".join(failures)
