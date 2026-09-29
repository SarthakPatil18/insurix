"""Initial schema for policies, policy_chunks, query_log, and treatments.

Revision ID: 001_initial_schema
Revises: None
Create Date: 2026-09-29
"""

from alembic import op
import sqlalchemy as sa

revision = '001_initial_schema'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # 1. Policies table
    op.create_table(
        'policies',
        sa.Column('id', sa.String(length=36), primary_key=True),
        sa.Column('session_id', sa.String(length=64), index=True, nullable=True),
        sa.Column('insurer', sa.String(length=255), nullable=False),
        sa.Column('name', sa.String(length=255), nullable=False),
        sa.Column('file_name', sa.String(length=255), nullable=True),
        sa.Column('pages', sa.Integer(), nullable=True, default=1),
        sa.Column('sum_insured', sa.Integer(), nullable=False, default=500000),
        sa.Column('policy_period', sa.String(length=64), nullable=True),
        sa.Column('tenure_months', sa.Integer(), nullable=True, default=36),
        sa.Column('room_rent', sa.JSON(), nullable=True),
        sa.Column('icu_rent', sa.JSON(), nullable=True),
        sa.Column('proportionality', sa.Boolean(), nullable=True, default=True),
        sa.Column('deductible', sa.Integer(), nullable=True, default=0),
        sa.Column('copay', sa.JSON(), nullable=True),
        sa.Column('non_network_copay_pct', sa.Integer(), nullable=True, default=0),
        sa.Column('waiting', sa.JSON(), nullable=True),
        sa.Column('sub_limits', sa.JSON(), nullable=True),
        sa.Column('implant_caps', sa.JSON(), nullable=True),
        sa.Column('created_at', sa.DateTime(timezone=True), nullable=True)
    )

    # 2. Policy chunks table
    op.create_table(
        'policy_chunks',
        sa.Column('id', sa.String(length=36), primary_key=True),
        sa.Column('policy_id', sa.String(length=36), sa.ForeignKey('policies.id', ondelete='CASCADE'), nullable=False, index=True),
        sa.Column('ord', sa.Integer(), nullable=True, default=0),
        sa.Column('section', sa.String(length=64), nullable=True),
        sa.Column('heading', sa.String(length=255), nullable=True),
        sa.Column('page', sa.Integer(), nullable=True, default=1),
        sa.Column('text', sa.Text(), nullable=False),
        sa.Column('tokens', sa.Integer(), nullable=True, default=0),
        sa.Column('embedding', sa.JSON(), nullable=True),
        sa.Column('tsv', sa.Text(), nullable=True)
    )

    # 3. Query log table
    op.create_table(
        'query_log',
        sa.Column('id', sa.String(length=36), primary_key=True),
        sa.Column('session_id', sa.String(length=64), index=True, nullable=True),
        sa.Column('policy_id', sa.String(length=36), sa.ForeignKey('policies.id', ondelete='SET NULL'), nullable=True),
        sa.Column('question', sa.Text(), nullable=False),
        sa.Column('verdict', sa.String(length=64), nullable=True),
        sa.Column('confidence', sa.String(length=64), nullable=True),
        sa.Column('payable', sa.Integer(), nullable=True, default=0),
        sa.Column('created_at', sa.DateTime(timezone=True), nullable=True)
    )

    # 4. Treatments table
    op.create_table(
        'treatments',
        sa.Column('id', sa.String(length=64), primary_key=True),
        sa.Column('name', sa.String(length=255), nullable=False),
        sa.Column('category', sa.String(length=128), nullable=False),
        sa.Column('icd', sa.String(length=32), nullable=True),
        sa.Column('specific_waiting', sa.Boolean(), nullable=True, default=False),
        sa.Column('excluded', sa.Boolean(), nullable=True, default=False),
        sa.Column('exclusion_code', sa.String(length=32), nullable=True),
        sa.Column('day_care', sa.Boolean(), nullable=True, default=False),
        sa.Column('cost_range', sa.JSON(), nullable=True),
        sa.Column('average', sa.Integer(), nullable=True, default=0),
        sa.Column('room_rate', sa.Integer(), nullable=True, default=0),
        sa.Column('icu_rate', sa.Integer(), nullable=True, default=0),
        sa.Column('icu_days', sa.Integer(), nullable=True, default=0),
        sa.Column('default_days', sa.Integer(), nullable=True, default=1),
        sa.Column('heads', sa.JSON(), nullable=True)
    )


def downgrade() -> None:
    op.drop_table('treatments')
    op.drop_table('query_log')
    op.drop_table('policy_chunks')
    op.drop_table('policies')
