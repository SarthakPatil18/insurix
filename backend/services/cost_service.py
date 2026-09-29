"""Cost Service: Treatment Catalogue Management and Head-Wise Bill Reconstruction."""

import json
from pathlib import Path
from typing import Dict, Any, List, Optional
from backend.utils.money import scale_heads_with_drift_absorption, to_rupees

_treatments_cache: Optional[Dict[str, Any]] = None


def load_treatments() -> Dict[str, Any]:
    """Loads treatments catalog from data/treatments.json."""
    global _treatments_cache
    if _treatments_cache is not None:
        return _treatments_cache

    data_path = Path(__file__).resolve().parent.parent / "data" / "treatments.json"
    if data_path.exists():
        with open(data_path, "r", encoding="utf-8") as f:
            _treatments_cache = json.load(f)
    else:
        _treatments_cache = {}

    return _treatments_cache


def get_treatment_by_id(treatment_id: str) -> Optional[Dict[str, Any]]:
    treatments = load_treatments()
    return treatments.get(treatment_id)


def reconstruct_bill(
    treatment_id: str,
    quoted_cost: int,
    days: int = 1,
    is_network: bool = True
) -> Dict[str, int]:
    """Reconstructs head-wise itemized hospital bill reconciled to the quoted amount.
    
    Absorbs any scaling and rounding drift into the largest financial head (typically surgeon or implant).
    """
    treatment = get_treatment_by_id(treatment_id)
    if not treatment:
        # Default distribution for generic treatment
        default_heads = {
            "surgeon": to_rupees(quoted_cost * 0.35),
            "ot": to_rupees(quoted_cost * 0.15),
            "anaesthesia": to_rupees(quoted_cost * 0.10),
            "implant": to_rupees(quoted_cost * 0.15),
            "medicines": to_rupees(quoted_cost * 0.12),
            "diagnostics": to_rupees(quoted_cost * 0.08),
            "room": to_rupees(quoted_cost * 0.05),
            "icu": 0
        }
        return scale_heads_with_drift_absorption(default_heads, quoted_cost)

    base_heads = treatment.get("heads", {})
    return scale_heads_with_drift_absorption(base_heads, quoted_cost)
