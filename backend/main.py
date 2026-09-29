"""Insurix FastAPI Application Factory, Lifespan, and Health Probes."""

import time
import uuid
from contextlib import asynccontextmanager
from typing import Dict, Any
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from sqlalchemy import text

from backend.core.config import settings
from backend.core.logging_conf import logger
from backend.core.errors import InsurixError, insurix_exception_handler
from backend.db.database import init_db, engine, is_postgres
from backend.services.embedding_service import is_embedding_degraded, get_embedding_model
from backend.services.llm_service import is_llm_available
from backend.api.policy import load_sample_policies
from backend.api.documents import router as documents_router
from backend.api.query import router as query_router
from backend.api.estimate import router as estimate_router
from backend.api.policy import router as policy_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Lifecycle manager: initializes database and preloads reference policies."""
    logger.info("Booting Insurix Backend Engine...")
    await init_db()
    load_sample_policies()
    logger.info("Insurix Backend Engine ready to serve traffic.")
    yield
    logger.info("Shutting down Insurix Backend Engine...")
    await engine.dispose()


def create_app() -> FastAPI:
    app = FastAPI(
        title="Insurix Health Insurance Intelligence API",
        version="2.0.0",
        description="Deterministic policy clause retrieval, deduction calculation, and evidence grounding engine.",
        lifespan=lifespan
    )

    # 1. CORS Middleware
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.CORS_ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # 2. Structured Request ID & Timing Middleware
    @app.middleware("http")
    async def request_id_middleware(request: Request, call_next):
        req_id = request.headers.get("x-request-id", str(uuid.uuid4())[:8])
        start_time = time.time()
        response = await call_next(request)
        duration_ms = round((time.time() - start_time) * 1000, 2)
        response.headers["x-request-id"] = req_id
        response.headers["x-response-time"] = f"{duration_ms}ms"
        return response

    # 3. Global Exception Handlers
    app.add_exception_handler(InsurixError, insurix_exception_handler)

    # 4. Register All 4 Contract Routers
    app.include_router(documents_router)
    app.include_router(query_router)
    app.include_router(estimate_router)
    app.include_router(policy_router)

    # 5. Core Root & Probed Health Endpoints
    @app.get("/", summary="Root health and API status")
    async def root():
        return {
            "name": "Insurix API",
            "version": "2.0.0",
            "status": "operational",
            "disclaimer": "Estimate only — not a settlement promise. Confirm with your insurer or TPA before admission."
        }

    @app.get("/health", summary="Probed service health and honest degradation reporting")
    async def health():
        degraded = []

        # Probe Database (SELECT 1)
        db_status = "disconnected"
        try:
            async with engine.connect() as conn:
                await conn.execute(text("SELECT 1"))
            db_status = "connected"
        except Exception as e:
            logger.warning(f"DB health probe failed: {e}")
            degraded.append("db")

        # Probe Vector Store
        vector_store_status = "pgvector" if is_postgres else "in_memory_sqlite"

        # Probe Embedding Model
        emb_model = get_embedding_model()
        if emb_model is not None:
            embedding_status = "connected"
        else:
            embedding_status = "deterministic_hash_fallback"
            degraded.append("embedding")

        # Probe LLM
        if is_llm_available():
            llm_status = "connected"
        else:
            llm_status = "offline_deterministic_synthesizer"
            degraded.append("llm")

        status_code = "healthy" if not degraded else "degraded"

        return {
            "status": status_code,
            "db": db_status,
            "vector_store": vector_store_status,
            "embedding": embedding_status,
            "llm": llm_status,
            "degraded": degraded
        }

    return app


app = create_app()
