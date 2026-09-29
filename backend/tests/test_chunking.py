"""Tests for Hierarchical Section-Aware Chunking Service."""

import pytest
from backend.services.pdf_service import PDFPageBlock
from backend.services.chunking_service import chunk_policy_blocks


def test_chunking_preserves_tables_atomically():
    blocks = [
        PDFPageBlock(
            page=1,
            text="Col1 | Col2 | Col3\nData1 | Data2 | Data3",
            kind="table"
        )
    ]
    chunks = chunk_policy_blocks(blocks)
    assert len(chunks) == 1
    assert chunks[0].is_table is True
    assert chunks[0].page == 1
    assert "Data2" in chunks[0].text


def test_chunking_detects_sections():
    prose = (
        "SECTION 4.0 COVERED BENEFITS\n"
        "Hospitalization expenses incurred for medically necessary treatment.\n\n"
        "4.1 Room Rent Charges\n"
        "Room rent charges covered up to specified limits per day.\n\n"
        "EXCLUSIONS\n"
        "Cosmetic surgery and aesthetic treatments are strictly excluded under Excl01."
    )
    blocks = [PDFPageBlock(page=2, text=prose, kind="prose")]
    chunks = chunk_policy_blocks(blocks, target_tokens=30)
    assert len(chunks) >= 2
    assert any("EXCLUSIONS" in c.heading or "Excl" in c.section for c in chunks)
