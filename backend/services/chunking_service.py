"""Section-Aware Policy Chunking Service."""

import re
from typing import List, Dict, Any
from backend.services.pdf_service import PDFPageBlock
from backend.utils.citations import normalize_section

SECTION_HEADER_REGEX = re.compile(
    r'(?:^(?:SECTION|Section)\s+\d[A-Za-z0-9.]*)|'
    r'(?:^\d+(\.\d+)+\s+[A-Z])|'
    r'(?:^[A-Z\s]{4,40}$)|'
    r'(?:Excl0\d)',
    re.MULTILINE
)


class ChunkResult:
    def __init__(
        self,
        ord: int,
        section: str,
        heading: str,
        page: int,
        text: str,
        tokens: int,
        is_table: bool = False
    ):
        self.ord = ord
        self.section = section
        self.heading = heading
        self.page = page
        self.text = text
        self.tokens = tokens
        self.is_table = is_table


def chunk_policy_blocks(blocks: List[PDFPageBlock], target_tokens: int = 500, overlap_pct: float = 0.15) -> List[ChunkResult]:
    """Chunks policy page blocks into section-aware, citation-ready units."""
    chunks: List[ChunkResult] = []
    ord_counter = 0

    for block in blocks:
        # Table blocks remain atomic
        if block.kind == "table":
            ord_counter += 1
            tokens = len(block.text) // 4
            chunks.append(
                ChunkResult(
                    ord=ord_counter,
                    section="Table",
                    heading="Policy Schedule / Sub-limit Table",
                    page=block.page,
                    text=block.text,
                    tokens=tokens,
                    is_table=True
                )
            )
            continue

        # Split prose by paragraph or sections
        paragraphs = block.text.split("\n\n")
        current_section = "1.0"
        current_heading = "General Terms & Coverage"
        buffer_paragraphs = []
        buffer_tokens = 0

        for para in paragraphs:
            para = para.strip()
            if not para:
                continue

            # Detect section header
            first_line = para.split("\n")[0].strip()
            if SECTION_HEADER_REGEX.search(first_line):
                # If buffer has accumulated tokens, flush previous chunk
                if buffer_paragraphs:
                    ord_counter += 1
                    chunk_text = "\n\n".join(buffer_paragraphs)
                    chunks.append(
                        ChunkResult(
                            ord=ord_counter,
                            section=normalize_section(current_section),
                            heading=current_heading[:200],
                            page=block.page,
                            text=chunk_text,
                            tokens=buffer_tokens,
                            is_table=False
                        )
                    )
                    buffer_paragraphs = []
                    buffer_tokens = 0

                current_heading = first_line
                sec_match = re.search(r'\d+(\.\d+)*', first_line)
                if sec_match:
                    current_section = sec_match.group(0)

            para_tokens = len(para) // 4
            # If adding this para exceeds target_tokens, flush
            if buffer_tokens + para_tokens > target_tokens and buffer_paragraphs:
                ord_counter += 1
                chunk_text = "\n\n".join(buffer_paragraphs)
                chunks.append(
                    ChunkResult(
                        ord=ord_counter,
                        section=normalize_section(current_section),
                        heading=current_heading[:200],
                        page=block.page,
                        text=chunk_text,
                        tokens=buffer_tokens,
                        is_table=False
                    )
                )
                # Keep overlap if configured
                if overlap_pct > 0 and buffer_paragraphs:
                    overlap_para = buffer_paragraphs[-1]
                    buffer_paragraphs = [overlap_para, para]
                    buffer_tokens = (len(overlap_para) + len(para)) // 4
                else:
                    buffer_paragraphs = [para]
                    buffer_tokens = para_tokens
            else:
                buffer_paragraphs.append(para)
                buffer_tokens += para_tokens

        # Flush remaining buffer
        if buffer_paragraphs:
            ord_counter += 1
            chunk_text = "\n\n".join(buffer_paragraphs)
            chunks.append(
                ChunkResult(
                    ord=ord_counter,
                    section=normalize_section(current_section),
                    heading=current_heading[:200],
                    page=block.page,
                    text=chunk_text,
                    tokens=buffer_tokens,
                    is_table=False
                )
            )

    return chunks
