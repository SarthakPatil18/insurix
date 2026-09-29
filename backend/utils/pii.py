"""PII Scrubbing Utilities.

Strips personally identifiable information (patient names, policy numbers, phone numbers,
email addresses, Aadhaar / PAN numbers) before document embedding and retrieval indexing.
"""

import re

# Regex patterns for common Indian and general PII identifiers
EMAIL_PATTERN = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b')
PHONE_PATTERN = re.compile(r'\b(?:\+91[-\s]?)?[6-9]\d{9}\b')
PAN_PATTERN = re.compile(r'\b[A-Z]{5}[0-9]{4}[A-Z]\b')
AADHAAR_PATTERN = re.compile(r'\b\d{4}[-\s]?\d{4}[-\s]?\d{4}\b')
POLICY_NUM_PATTERN = re.compile(r'\b(?:Policy\s*(?:No|Number|#)?[:\s]*)([A-Z0-9\/-]{7,25})\b', re.IGNORECASE)
NAME_HEADER_PATTERN = re.compile(r'\b(?:Insured|Patient|Proposer|Beneficiary)\s*(?:Name)?[:\s]+([A-Z][a-z]+(?:\s+[A-Z][a-z]+){1,3})\b', re.IGNORECASE)


def redact_pii(text: str) -> str:
    """Scrubs all sensitive personal identifiers from extracted text."""
    if not text:
        return ""

    sanitized = text
    # 1. Emails
    sanitized = EMAIL_PATTERN.sub("[REDACTED_EMAIL]", sanitized)
    # 2. Phone numbers
    sanitized = PHONE_PATTERN.sub("[REDACTED_PHONE]", sanitized)
    # 3. PAN card numbers
    sanitized = PAN_PATTERN.sub("[REDACTED_PAN]", sanitized)
    # 4. Aadhaar numbers
    sanitized = AADHAAR_PATTERN.sub("[REDACTED_AADHAAR]", sanitized)
    # 5. Policy numbers
    sanitized = POLICY_NUM_PATTERN.sub("Policy No: [REDACTED_POLICY_ID]", sanitized)
    # 6. Patient/Proposer names
    sanitized = NAME_HEADER_PATTERN.sub("Insured: [REDACTED_NAME]", sanitized)

    return sanitized
