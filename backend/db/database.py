"""Database Connection Engine, Sessionmaker, and Schema Initialization."""

import os
from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import declarative_base
from sqlalchemy import text
from backend.core.config import settings
from backend.core.logging_conf import logger

Base = declarative_base()

# Determine database driver & capabilities
is_postgres = settings.DATABASE_URL.startswith("postgresql")

engine = create_async_engine(
    settings.DATABASE_URL,
    echo=False,
    future=True,
    **({} if not is_postgres else {"pool_size": 10, "max_overflow": 20})
)

async_session_factory = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autocommit=False,
    autoflush=False
)


async def init_db() -> bool:
    """Initialize database tables and pgvector extension if PostgreSQL."""
    try:
        async with engine.begin() as conn:
            if is_postgres:
                logger.info("Enabling pgvector extension on PostgreSQL...")
                await conn.execute(text("CREATE EXTENSION IF NOT EXISTS vector;"))
            
            # Import models to register tables
            from backend.db import models  # noqa: F401
            await conn.run_sync(Base.metadata.create_all)
            logger.info("Database schema initialized successfully.")
        return True
    except Exception as e:
        logger.error(f"Database initialization error: {e}")
        return False


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    """Dependency for providing database sessions."""
    async with async_session_factory() as session:
        try:
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()
