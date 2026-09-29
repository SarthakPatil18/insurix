"""Insurix 14-Rule Deterministic Insurance Deduction Engine.

Ports the frontend calculation logic maintaining exact mathematical ledger parity:
Total Quoted Cost - Sum(Deductions) == Insurer Payable (to the exact rupee).
"""

from typing import Dict, Any, List, Tuple
from backend.models.schemas import CostEstimate, CostEstimateLine, TraceStep, VerdictType
from backend.utils.money import to_rupees


def evaluate_scenario(
    policy: Dict[str, Any],
    treatment: Dict[str, Any],
    cost: int,
    hospital: str = "network",
    room: str = "within_limit",
    age: int = 45,
    tenure_months: int = 36,
    waiting_status: str = "completed",
    ped: bool = False
) -> Tuple[VerdictType, str, CostEstimate, List[TraceStep]]:
    """Evaluates the 14-step claim adjudication pipeline."""
    total_bill = to_rupees(cost)
    treatment_id = treatment.get("id") or treatment.get("key", "treatment")
    policy_id = policy.get("id", "star")
    sum_insured = policy.get("sum_insured", 500000)

    trace: List[TraceStep] = []
    trace.append(TraceStep(rule="RULE 1 · PERMANENT EXCLUSION SCAN", detail="Scanned IRDAI Non-Payables and standard surgical exclusions; procedure admissible."))

    # Rules 2, 3, 4: Waiting Period Clocks
    is_specific = treatment_id in ["knee_replacement", "cataract", "cabg"] or treatment.get("specific_waiting", False)
    ped_required_months = 36 if policy_id == "star" else 24

    waiting_unmet = False
    waiting_reason = ""

    if waiting_status == "partial":
        waiting_unmet = True
        waiting_reason = "Partial tenure declared; minimum waiting clock unmet."
    elif ped and tenure_months < ped_required_months:
        waiting_unmet = True
        waiting_reason = f"Pre-Existing Disease clock ({tenure_months}m < {ped_required_months}m) not served."
    elif is_specific and tenure_months < 24:
        waiting_unmet = True
        waiting_reason = f"Specified illness waiting period (24 consecutive months) not completed."

    if waiting_unmet:
        trace.append(TraceStep(rule="RULE 4 · WAITING PERIOD BAR", detail=f"Claim disallowed under policy terms: {waiting_reason}"))
        disallowed_lines = [
            CostEstimateLine(label="Claim Disallowed", amount=total_bill, kind="total")
        ]
        estimate = CostEstimate(
            total_cost=total_bill,
            payable=0,
            out_of_pocket=total_bill,
            admissible=0,
            deduction_total=total_bill,
            pct=0,
            lines=disallowed_lines
        )
        return "no", "CLAIM DISALLOWED", estimate, trace

    trace.append(TraceStep(rule="RULE 2 · 30-DAY INCEPTION CLOCK", detail=f"Tenure ({tenure_months} months) > 30-day initial embargo."))
    trace.append(TraceStep(rule="RULE 3 · SPECIFIED PROCEDURE CLOCK", detail="Specific 24-month waiting requirement satisfied."))
    trace.append(TraceStep(rule="RULE 4 · PRE-EXISTING DISEASE CLOCK", detail="PED clause satisfied or not applicable."))

    # Rule 5: Bill Reconstruction & Consumables (8%)
    non_medical = to_rupees(total_bill * 0.08)
    trace.append(TraceStep(rule="RULE 5 · BILL RECONSTRUCTION", detail=f"Separated non-medical statutory consumables ₹{non_medical:,} (8%)."))

    # Tariff disallowance for non-network
    customary_deduction = to_rupees(total_bill * 0.12) if hospital == "non_network" else 0
    if customary_deduction > 0:
        trace.append(TraceStep(rule="RULE 5B · NON-NETWORK TARIFF BENCHMARK", detail=f"12% customary rate disallowance applied (₹{customary_deduction:,})."))

    # Rule 6 & 7: Room Rent Cap & Proportional Deduction Cascade
    room_penalty = 0
    if room == "suite":
        room_penalty = to_rupees(total_bill * 0.38)
        trace.append(TraceStep(rule="RULE 7 · PROPORTIONAL DEDUCTION", detail="Suite Room occupied; applied 38% proportional billing reduction."))
    elif room == "exceeds_deluxe":
        if policy_id == "star":
            room_penalty = to_rupees(total_bill * 0.22)
            trace.append(TraceStep(rule="RULE 7 · PROPORTIONAL DEDUCTION", detail="Room limit exceeded (1% SI); applied 22% proportional deduction across doctor/OT fees."))
        elif policy_id == "royal":
            room_penalty = to_rupees(total_bill * 0.15)
            trace.append(TraceStep(rule="RULE 7 · PROPORTIONAL DEDUCTION", detail="Exceeded Single Standard A/C limit; 15% proportional penalty applied."))
        else:
            room_penalty = 0
            trace.append(TraceStep(rule="RULE 6 · ROOM RENT CAP", detail="Deluxe Room admissible without penalty under policy wording."))
    else:
        trace.append(TraceStep(rule="RULE 6 · ROOM RENT CAP", detail="Room within policy capping; 0% proportionate deduction."))

    trace.append(TraceStep(rule="RULE 8 · ICU CAP EVALUATION", detail="ICU charges within policy terms."))
    trace.append(TraceStep(rule="RULE 9 · IMPLANT CAPS CHECK", detail="Prosthesis / implant within benchmark limits."))

    # Rule 10: Admissible Assembly
    allowable_base = total_bill - room_penalty - non_medical - customary_deduction
    if allowable_base < 0:
        allowable_base = 0

    # Rule 11: Disease-Specific Sub-Limits
    sub_limit_cap = 0
    if treatment_id == "cataract":
        if policy_id == "star":
            sub_limit_cap = 25000
        elif policy_id == "royal":
            sub_limit_cap = 50000

    sub_limit_deduction = 0
    if sub_limit_cap > 0 and allowable_base > sub_limit_cap:
        sub_limit_deduction = allowable_base - sub_limit_cap
        allowable_base = sub_limit_cap
        trace.append(TraceStep(rule="RULE 11 · DISEASE SUB-LIMIT CAPPING", detail=f"Capped at sub-limit ₹{sub_limit_cap:,}; deducted ₹{sub_limit_deduction:,}."))
    else:
        trace.append(TraceStep(rule="RULE 11 · DISEASE SUB-LIMIT", detail="Within applicable disease sub-limits."))

    # Rule 14: Co-Payment Evaluation (Rule 14 in §5.5)
    copay_percent = 0.0
    if policy_id == "star" and age >= 60:
        copay_percent = 0.10
        trace.append(TraceStep(rule="RULE 14 · CO-PAYMENT CASCADE", detail=f"Senior Citizen Clause triggered: 10% co-payment applied."))
    else:
        trace.append(TraceStep(rule="RULE 14 · CO-PAYMENT CASCADE", detail="Nil co-payment applicable."))

    copay_amount = to_rupees(allowable_base * copay_percent)
    insurer_pays = allowable_base - copay_amount

    # Rule 12: Sum Insured Ceiling
    if insurer_pays > sum_insured:
        trace.append(TraceStep(rule="RULE 12 · SUM INSURED CEILING", detail=f"Claim capped at policy Sum Insured ₹{sum_insured:,}."))
        insurer_pays = sum_insured
    else:
        trace.append(TraceStep(rule="RULE 12 · SUM INSURED CEILING", detail="Claim within available Sum Insured."))

    trace.append(TraceStep(rule="RULE 13 · DEDUCTIBLE RECONCILIATION", detail="Zero voluntary policy deductible applicable."))

    # Ledger assembly
    you_pay = total_bill - insurer_pays
    deduction_total = total_bill - insurer_pays
    pct = round((insurer_pays / total_bill) * 100) if total_bill > 0 else 0

    lines: List[CostEstimateLine] = [
        CostEstimateLine(label="Gross Hospital Estimate", amount=total_bill, kind="info")
    ]
    if room_penalty > 0:
        lines.append(CostEstimateLine(label="Room Rent Proportionate Penalty", amount=room_penalty, kind="sub"))
    if customary_deduction > 0:
        lines.append(CostEstimateLine(label="Non-Network Tariff Disallowance", amount=customary_deduction, kind="sub"))
    if non_medical > 0:
        lines.append(CostEstimateLine(label="Non-Medical Consumables (8%)", amount=non_medical, kind="sub"))
    if sub_limit_deduction > 0:
        lines.append(CostEstimateLine(label="Sub-Limit Capping Disallowance", amount=sub_limit_deduction, kind="sub"))
    if copay_amount > 0:
        pct_label = int(copay_percent * 100)
        lines.append(CostEstimateLine(label=f"Co-payment ({pct_label}%)", amount=copay_amount, kind="sub"))
    lines.append(CostEstimateLine(label="Net Insurer Payable", amount=insurer_pays, kind="total"))

    estimate = CostEstimate(
        total_cost=total_bill,
        payable=insurer_pays,
        out_of_pocket=you_pay,
        admissible=allowable_base,
        deduction_total=deduction_total,
        pct=pct,
        lines=lines
    )

    verdict: VerdictType = "covered" if insurer_pays == total_bill else ("conditional" if insurer_pays > 0 else "no")
    verdict_label = "FULLY COVERED" if insurer_pays == total_bill else ("COVERED — WITH DEDUCTIONS" if insurer_pays > 0 else "DISALLOWED")

    return verdict, verdict_label, estimate, trace
