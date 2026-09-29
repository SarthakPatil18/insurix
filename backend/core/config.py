"""Insurix Application Configuration via Pydantic-Settings."""

from typing import List, Optional
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )

    # Database
    DATABASE_URL: str = Field(
        default="sqlite+aiosqlite:///:memory:",
        description="Async database connection string. Uses in-memory SQLite when Postgres not specified."
    )

    # LLM & Reasoning
    GROQ_API_KEY: Optional[str] = Field(default=None, description="Groq API key")
    GROQ_MODEL: str = Field(default="llama-3.3-70b-versatile", description="Model name on Groq")

    # Embeddings & Vector Search
    EMBEDDING_MODEL: str = Field(default="BAAI/bge-small-en-v1.5", description="Embedding model name")
    EMBEDDING_DIM: int = Field(default=384, description="Embedding vector dimensions")
    SIMILARITY_THRESHOLD: float = Field(default=0.45, description="Minimum cosine similarity cutoff")
    TOP_K: int = Field(default=5, description="Top-k retrieval count")
    RRF_K: int = Field(default=60, description="Reciprocal Rank Fusion smoothing parameter")

    # Chunking
    CHUNK_TOKENS: int = Field(default=500, description="Approx target token count per chunk")
    CHUNK_OVERLAP: float = Field(default=0.15, description="Overlap percentage between sequential chunks")

    # Security & Limits
    MAX_UPLOAD_BYTES: int = Field(default=10485760, description="10 MB max file upload size")
    SESSION_TTL: int = Field(default=86400, description="Session time to live in seconds")
    CORS_ORIGINS: List[str] = Field(
        default=[
            "http://localhost:3000",
            "http://127.0.0.1:3000",
            "https://sarthakpatil18.github.io"
        ],
        description="Allowed CORS origins"
    )

    # Logging & Environment
    APP_ENV: str = Field(default="development", description="development | staging | production")
    LOG_LEVEL: str = Field(default="INFO", description="Log level")
    PORT: int = Field(default=8123, description="HTTP listening port")


settings = Settings()
