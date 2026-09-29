"""Tests for PII Anonymization and Scrubbing."""

import pytest
from backend.utils.pii import redact_pii


def test_redact_email():
    text = "Send claim pre-authorization to patient.sarthak@example.com immediately."
    clean = redact_pii(text)
    assert "patient.sarthak@example.com" not in clean
    assert "[REDACTED_EMAIL]" in clean


def test_redact_phone():
    text = "Emergency contact: +91 9876543210 or 8765432109 for TPA queries."
    clean = redact_pii(text)
    assert "9876543210" not in clean
    assert "[REDACTED_PHONE]" in clean


def test_redact_pan_and_aadhaar():
    text = "Beneficiary PAN: ABCDE1234F and Aadhaar: 1234 5678 9012."
    clean = redact_pii(text)
    assert "ABCDE1234F" not in clean
    assert "[REDACTED_PAN]" in clean
    assert "1234 5678 9012" not in clean
    assert "[REDACTED_AADHAAR]" in clean


def test_redact_policy_number():
    text = "Policy Number: P/123456/01/2026/000123 has been registered."
    clean = redact_pii(text)
    assert "P/123456/01/2026/000123" not in clean
    assert "[REDACTED_POLICY_ID]" in clean
