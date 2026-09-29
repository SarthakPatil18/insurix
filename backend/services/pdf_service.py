"""PDF Extraction Service with PyMuPDF text and pdfplumber table extraction."""

import io
from typing import List, Dict, Any, Tuple
import pymupdf as fitz
import pdfplumber

from backend.core.logging_conf import logger


class PDFPageBlock:
    def __init__(self, page: int, text: str, kind: str = "prose", metadata: Dict[str, Any] = None):
        self.page = page
        self.text = text
        self.kind = kind  # "prose" | "table"
        self.metadata = metadata or {}


def extract_pdf_content(file_bytes: bytes) -> Tuple[List[PDFPageBlock], int, bool]:
    """Extracts text and structured tables per page.
    
    Returns:
        (blocks, page_count, ocr_needed_flag)
    """
    blocks: List[PDFPageBlock] = []
    total_text_chars = 0
    page_count = 0

    # 1. First pass: extract tables via pdfplumber
    table_ranges_per_page = {}
    try:
        with pdfplumber.open(io.BytesIO(file_bytes)) as pdf:
            page_count = len(pdf.pages)
            for page_idx, page in enumerate(pdf.pages):
                page_num = page_idx + 1
                tables = page.extract_tables() or []
                for table in tables:
                    if not table or len(table) < 2:
                        continue
                    # Convert table to row-per-line markdown format
                    rows_text = []
                    for row in table:
                        clean_row = [str(cell).strip() if cell is not None else "" for cell in row]
                        if any(clean_row):
                            rows_text.append(" | ".join(clean_row))
                    if rows_text:
                        table_str = "\n".join(rows_text)
                        blocks.append(
                            PDFPageBlock(
                                page=page_num,
                                text=table_str,
                                kind="table",
                                metadata={"rows": len(rows_text)}
                            )
                        )
                        total_text_chars += len(table_str)
    except Exception as e:
        logger.warning(f"pdfplumber table extraction note: {e}")

    # 2. Second pass: extract prose text via PyMuPDF
    doc = fitz.open(stream=file_bytes, filetype="pdf")
    page_count = max(page_count, len(doc))
    for page_idx, page in enumerate(doc):
        page_num = page_idx + 1
        page_text = page.get_text("text").strip()
        if page_text:
            blocks.append(
                PDFPageBlock(
                    page=page_num,
                    text=page_text,
                    kind="prose"
                )
            )
            total_text_chars += len(page_text)
    doc.close()

    # Determine if document is scanned (less than 100 characters per page average)
    avg_chars = total_text_chars / max(1, page_count)
    ocr_needed = avg_chars < 100

    return blocks, page_count, ocr_needed
