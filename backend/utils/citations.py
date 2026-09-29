"""Citations Normalization and Clause Formatting Utilities."""

import re
from typing import Dict, Any, Optional


def normalize_section(section_str: Optional[str]) -> str:
    """Normalizes various section formatting styles into clean identifiers.
    
    Examples:
        "Section 4.2" -> "4.2"
        "§ 4.2" -> "4.2"
        "clause 5.1(a)" -> "5.1"
    """
    if not section_str:
        return "1.0"
    cleaned = re.sub(r'^(Section|Clause|§)\s*', '', str(section_str).strip(), flags=re.IGNORECASE)
    match = re.search(r'\d+(\.\d+)*', cleaned)
    return match.group(0) if match else cleaned


def trim_quote(text: str, max_words: int = 40) -> str:
    """Trims long clause excerpts to concise, punchy quotes without breaking words."""
    if not text:
        return ""
    words = text.split()
    if len(words) <= max_words:
        return text.strip()
    return " ".join(words[:max_words]).strip() + "..."
