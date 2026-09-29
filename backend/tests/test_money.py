"""Tests for Money Arithmetic, INR String Formatting, and Drift Absorption."""

import pytest
from backend.utils.money import to_rupees, format_inr, scale_heads_with_drift_absorption


def test_to_rupees():
    assert to_rupees(100.4) == 100
    assert to_rupees(100.6) == 101
    assert to_rupees(None) == 0
    assert to_rupees(0) == 0


def test_format_inr():
    assert format_inr(0) == "₹0"
    assert format_inr(500) == "₹500"
    assert format_inr(5000) == "₹5,000"
    assert format_inr(25000) == "₹25,000"
    assert format_inr(280000) == "₹2,80,000"
    assert format_inr(1000000) == "₹10,00,000"
    assert format_inr(10000000) == "₹1,00,00,000"
    assert format_inr(280000, symbol=False) == "2,80,000"
    assert format_inr(-45000) == "-₹45,000"


def test_scale_heads_with_drift_absorption():
    heads = {
        "surgeon": 75000,
        "ot": 35000,
        "anaesthesia": 20000,
        "implant": 85000,
        "medicines": 30000,
        "diagnostics": 15000,
        "room": 20000
    }
    target = 250000
    scaled = scale_heads_with_drift_absorption(heads, target)
    assert sum(scaled.values()) == target
    assert isinstance(scaled["surgeon"], int)
    assert isinstance(scaled["implant"], int)


def test_scale_heads_zero_target():
    heads = {"surgeon": 1000, "room": 500}
    scaled = scale_heads_with_drift_absorption(heads, 0)
    assert sum(scaled.values()) == 0
