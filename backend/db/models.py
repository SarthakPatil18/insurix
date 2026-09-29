"""SQLAlchemy Data Models for Insurix (Policies, Chunks, Query Logs, Treatments)."""

import uuid
from datetime import datetime, timezone
from sqlalchemy import (
    Column,
    String,
    Integer,
    Boolean,
    Text,
    DateTime,
    ForeignKey,
    JSON
)
from sqlalchemy.dialects.postgresql import UUID as PG_UUID, JSONB
from sqlalchemy.orm import relationship
from backend.db.database import Base, is_postgres

try:
    from pgvector.sqlalchemy import Vector
    has_vector = True
except ImportError:
    has_vector = False


def utc_now():
    return datetime.now(timezone.utc)


class Policy(Base):
    __tablename__ = "policies"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    session_id = Column(String(64), index=True, nullable=True)
    insurer = Column(String(255), nullable=False)
    name = Column(String(255), nullable=False)
    file_name = Column(String(255), nullable=True)
    pages = Column(Integer, default=1)
    sum_insured = Column(Integer, nullable=False, default=500000)
    policy_period = Column(String(64), default="1 year")
    tenure_months = Column(Integer, default=36)
    
    # Coverage configurations stored as JSON/JSONB
    room_rent = Column(JSON, nullable=True)
    icu_rent = Column(JSON, nullable=True)
    proportionality = Column(Boolean, default=True)
    deductible = Column(Integer, default=0)
    copay = Column(JSON, nullable=True)
    non_network_copay_pct = Column(Integer, default=0)
    waiting = Column(JSON, nullable=True)
    sub_limits = Column(JSON, nullable=True)
    implant_caps = Column(JSON, nullable=True)
    created_at = Column(DateTime(timezone=True), default=utc_now)

    chunks = relationship("PolicyChunk", back_populates="policy", cascade="all, delete-orphan")


class PolicyChunk(Base):
    __tablename__ = "policy_chunks"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    policy_id = Column(String(36), ForeignKey("policies.id", ondelete="CASCADE"), nullable=False, index=True)
    ord = Column(Integer, default=0)
    section = Column(String(64), nullable=True)
    heading = Column(String(255), nullable=True)
    page = Column(Integer, default=1)
    text = Column(Text, nullable=False)
    tokens = Column(Integer, default=0)
    
    # Store embedding as pgvector Vector(384) in PostgreSQL or JSON list in SQLite
    if is_postgres and has_vector:
        embedding = Column(Vector(384), nullable=True)
    else:
        embedding = Column(JSON, nullable=True)
        
    tsv = Column(Text, nullable=True)

    policy = relationship("Policy", back_populates="chunks")


class QueryLog(Base):
    __tablename__ = "query_log"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    session_id = Column(String(64), index=True, nullable=True)
    policy_id = Column(String(36), ForeignKey("policies.id", ondelete="SET NULL"), nullable=True)
    question = Column(Text, nullable=False)
    verdict = Column(String(64), nullable=True)
    confidence = Column(String(64), nullable=True)
    payable = Column(Integer, default=0)
    created_at = Column(DateTime(timezone=True), default=utc_now)


class Treatment(Base):
    __tablename__ = "treatments"

    id = Column(String(64), primary_key=True)
    name = Column(String(255), nullable=False)
    category = Column(String(128), nullable=False)
    icd = Column(String(32), nullable=True)
    specific_waiting = Column(Boolean, default=False)
    excluded = Column(Boolean, default=False)
    exclusion_code = Column(String(32), nullable=True)
    day_care = Column(Boolean, default=False)
    cost_range = Column(JSON, nullable=True)
    average = Column(Integer, default=0)
    room_rate = Column(Integer, default=0)
    icu_rate = Column(Integer, default=0)
    icu_days = Column(Integer, default=0)
    default_days = Column(Integer, default=1)
    heads = Column(JSON, nullable=True)
