"""Financial Arithmetic & Currency Formatting Utilities.

Rule: All money values inside the engine and ledger are stored as integer rupees.
Zero floats in financial ledgers. INR string formatting occurs strictly at the presentation edge.
"""

from typing import Dict, List, Tuple


import math


def to_rupees(value: float | int) -> int:
    """Safely converts any numeric input to integer rupees matching JavaScript Math.round()."""
    if value is None:
        return 0
    return int(math.floor(float(value) + 0.5))


def format_inr(amount: int, symbol: bool = True) -> str:
    """Formats an integer rupee amount using standard Indian numbering system (Lakhs / Crores).
    
    Example:
        format_inr(280000) -> "₹2,80,000"
        format_inr(280000, symbol=False) -> "2,80,000"
    """
    sign = "-" if amount < 0 else ""
    val_str = str(abs(int(amount)))
    
    if len(val_str) <= 3:
        formatted = val_str
    else:
        last_three = val_str[-3:]
        remaining = val_str[:-3]
        # Group remaining digits in pairs of 2 from right to left
        groups = []
        while len(remaining) > 2:
            groups.insert(0, remaining[-2:])
            remaining = remaining[:-2]
        if remaining:
            groups.insert(0, remaining)
        formatted = ",".join(groups) + "," + last_three

    prefix = "₹" if symbol else ""
    return f"{sign}{prefix}{formatted}"


def scale_heads_with_drift_absorption(
    heads: Dict[str, int],
    target_total: int
) -> Dict[str, int]:
    """Scales component heads proportionally to target_total and absorbs rounding drift
    into the largest financial head, ensuring exact identity sum(scaled) == target_total.
    """
    if target_total <= 0:
        return {k: 0 for k in heads}

    current_sum = sum(heads.values())
    if current_sum <= 0:
        return {k: 0 for k in heads}

    if current_sum == target_total:
        return dict(heads)

    # Scale each head with integer round
    scaled = {}
    largest_head = None
    max_val = -1

    for head, val in heads.items():
        ratio = val / current_sum
        head_scaled = int(round(target_total * ratio))
        scaled[head] = head_scaled
        if val > max_val:
            max_val = val
            largest_head = head

    # Absorb rounding drift
    drift = target_total - sum(scaled.values())
    if drift != 0 and largest_head in scaled:
        scaled[largest_head] += drift

    return scaled
