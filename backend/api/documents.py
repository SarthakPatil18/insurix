"""Document Ingestion and Management API Endpoints."""

import uuid
from typing import Dict, Any
from fastapi import APIRouter, UploadFile, File, status, Response, Depends
from backend.core.config import settings
from backend.core.errors import (
    UnsupportedMediaError,
    PayloadTooLargeError,
    NotFoundError,
    ValidationError
)
from backend.models.schemas import DocumentUploadResponse, DocumentDetailResponse
from backend.services.pipeline import ingest_policy_pdf
from backend.services.vector_service import get_in_memory_chunks, register_in_memory_chunks
from backend.api.deps import get_session_id

router = APIRouter(prefix="/api/documents", tags=["documents"])

# In-memory document registry for session documents
_documents_db: Dict[str, Dict[str, Any]] = {}


@router.post(
    "/upload",
    response_model=DocumentUploadResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Upload and index policy PDF"
)
async def upload_document(
    file: UploadFile = File(...),
    session_id: str = Depends(get_session_id)
):
    # 1. Validate file extension
    filename = file.filename or "policy.pdf"
    if not filename.lower().endswith(".pdf"):
        raise UnsupportedMediaError(f"File '{filename}' must be a PDF document.")

    # 2. Read bytes and check size
    contents = await file.read()
    if len(contents) > settings.MAX_UPLOAD_BYTES:
        raise PayloadTooLargeError(f"File size ({len(contents)} bytes) exceeds maximum limit of 10 MB.")

    if len(contents) < 5:
        raise ValidationError("Uploaded file is empty or corrupted.")

    # 3. Validate magic bytes (%PDF)
    if not contents.startswith(b"%PDF-"):
        raise UnsupportedMediaError("Invalid document: missing %PDF- header magic bytes.")

    # 4. Ingest via pipeline
    doc_id = str(uuid.uuid4())
    result = ingest_policy_pdf(contents, filename, policy_id=doc_id)

    # 5. Store record
    _documents_db[doc_id] = {
        "document_id": doc_id,
        "session_id": session_id,
        "file_name": filename,
        "pages": result.pages,
        "chunks": result.chunks_count,
        "status": result.status
    }

    return DocumentUploadResponse(
        document_id=result.document_id,
        file_name=result.file_name,
        pages=result.pages,
        chunks=result.chunks_count,
        status=result.status,
        degraded=result.degraded
    )


@router.get(
    "/{id}",
    response_model=DocumentDetailResponse,
    summary="Get document details"
)
async def get_document(id: str):
    doc = _documents_db.get(id)
    if not doc:
        chunks = get_in_memory_chunks(id)
        if chunks:
            return DocumentDetailResponse(
                document_id=id,
                status="indexed",
                pages=max(c.get("page", 1) for c in chunks),
                chunks=len(chunks),
                summary={"source": "preloaded_sample"}
            )
        raise NotFoundError(f"Document with ID '{id}' not found.")

    return DocumentDetailResponse(
        document_id=doc["document_id"],
        status=doc["status"],
        pages=doc["pages"],
        chunks=doc["chunks"],
        summary={"file_name": doc["file_name"]}
    )


@router.delete(
    "/{id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete uploaded document"
)
async def delete_document(id: str):
    if id in _documents_db:
        del _documents_db[id]
        register_in_memory_chunks(id, [])
        return Response(status_code=status.HTTP_204_NO_CONTENT)

    chunks = get_in_memory_chunks(id)
    if chunks:
        register_in_memory_chunks(id, [])
        return Response(status_code=status.HTTP_204_NO_CONTENT)

    raise NotFoundError(f"Document with ID '{id}' not found.")
