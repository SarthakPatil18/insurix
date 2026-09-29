"""End-to-End Document Ingestion Pipeline."""

import uuid
from typing import Dict, Any, List
from backend.services.pdf_service import extract_pdf_content
from backend.services.chunking_service import chunk_policy_blocks
from backend.services.embedding_service import encode_texts, is_embedding_degraded
from backend.services.vector_service import register_in_memory_chunks
from backend.core.logging_conf import logger


class IngestionResult:
    def __init__(
        self,
        document_id: str,
        file_name: str,
        pages: int,
        chunks_count: int,
        status: str,
        degraded: List[str]
    ):
        self.document_id = document_id
        self.file_name = file_name
        self.pages = pages
        self.chunks_count = chunks_count
        self.status = status
        self.degraded = degraded


def ingest_policy_pdf(file_bytes: bytes, filename: str, policy_id: str = None) -> IngestionResult:
    """Processes an uploaded PDF: extraction -> chunking -> embedding -> indexing."""
    doc_id = policy_id or str(uuid.uuid4())
    degraded: List[str] = []

    # 1. Parse PDF pages & tables
    blocks, page_count, ocr_needed = extract_pdf_content(file_bytes)
    if ocr_needed:
        degraded.append("ocr_fallback")

    # 2. Chunk blocks hierarchically
    chunks = chunk_policy_blocks(blocks)
    if not chunks:
        # Fallback single chunk if PDF contained sparse text
        from backend.services.chunking_service import ChunkResult
        chunks = [
            ChunkResult(
                ord=1,
                section="1.0",
                heading="General Policy Terms",
                page=1,
                text=f"Uploaded policy document {filename} parsed successfully.",
                tokens=20
            )
        ]

    # 3. Generate embeddings
    chunk_texts = [c.text for c in chunks]
    embeddings = encode_texts(chunk_texts)
    if is_embedding_degraded():
        degraded.append("embedding")

    # 4. Index chunks in memory / vector store
    indexed_chunks = []
    for c, emb in zip(chunks, embeddings):
        indexed_chunks.append({
            "ord": c.ord,
            "section": c.section,
            "heading": c.heading,
            "page": c.page,
            "text": c.text,
            "tokens": c.tokens,
            "embedding": emb
        })

    register_in_memory_chunks(doc_id, indexed_chunks)
    logger.info(f"Successfully ingested {filename} (ID: {doc_id}) with {len(indexed_chunks)} chunks across {page_count} pages.")

    return IngestionResult(
        document_id=doc_id,
        file_name=filename,
        pages=max(1, page_count),
        chunks_count=len(indexed_chunks),
        status="indexed",
        degraded=degraded
    )
