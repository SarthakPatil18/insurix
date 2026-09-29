"""API Dependencies: Session Scoping, Database, and Settings."""

from typing import Optional
from fastapi import Header, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from backend.db.database import get_db
from backend.core.config import settings, Settings


def get_settings() -> Settings:
    return settings


def get_session_id(x_session_id: Optional[str] = Header(default="default-session")) -> str:
    """Extracts or assigns a session ID for data scoping."""
    return x_session_id or "default-session"
