"""Insurix Pydantic v2 Models and HTTP Contract Schemas."""

from typing import List, Optional, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict


DISCLAIMER_TEXT = "Estimate only — not a settlement promise. Confirm with your insurer or TPA before admission."

VerdictType = Literal["covered", "conditional", "no", "unknown"]
ConfidenceType = Literal["high", "medium", "low", "insufficient"]
LineKindType = Literal["info", "sub", "total"]


class EvidenceCitation(BaseModel):
    model_config = ConfigDict(extra="ignore")
    text: str = Field(description="Verbatim text from policy clause")
    page: int = Field(description="1-based page number")
    section: str = Field(description="Clause or section identifier e.g. 4.2")
    score: float = Field(default=1.0, description="Relevance retrieval score")
    policy_id: Optional[str] = Field(default=None, description="Policy identifier")


class CostEstimateLine(BaseModel):
    model_config = ConfigDict(extra="ignore")
    label: str
    amount: int
    kind: LineKindType = "info"


class CostEstimate(BaseModel):
    model_config = ConfigDict(extra="ignore")
    total_cost: int
    payable: int
    out_of_pocket: int
    admissible: Optional[int] = None
    deduction_total: int
    pct: int
    lines: List[CostEstimateLine] = Field(default_factory=list)


class UncertaintyInfo(BaseModel):
    model_config = ConfigDict(extra="ignore")
    confidence: ConfidenceType = "medium"
    missing_info: List[str] = Field(default_factory=list)
    recommendation: Optional[str] = None


class TraceStep(BaseModel):
    model_config = ConfigDict(extra="ignore")
    rule: str
    detail: str


class LLMInfo(BaseModel):
    model_config = ConfigDict(extra="ignore")
    used: bool = False
    model: Optional[str] = None


# Query schemas
class TreatmentScenarioInput(BaseModel):
    model_config = ConfigDict(extra="ignore")
    id: Optional[str] = None
    cost: Optional[int] = None
    days: Optional[int] = 1
    hospital: Optional[Literal["network", "non_network"]] = "network"
    room: Optional[Literal["within_limit", "exceeds_deluxe", "suite"]] = "within_limit"
    age_band: Optional[int] = 45
    ped: Optional[bool] = False
    tenure_months: Optional[int] = 36


class QueryRequest(BaseModel):
    model_config = ConfigDict(extra="ignore")
    question: str
    policy_id: Optional[str] = "star"
    treatment: Optional[TreatmentScenarioInput] = None


class QueryResponse(BaseModel):
    model_config = ConfigDict(extra="ignore")
    answer: str
    verdict: VerdictType
    verdict_label: str
    confidence: ConfidenceType
    evidence: List[EvidenceCitation] = Field(default_factory=list)
    cost_estimate: Optional[CostEstimate] = None
    uncertainty: UncertaintyInfo
    trace: List[TraceStep] = Field(default_factory=list)
    llm: LLMInfo = Field(default_factory=LLMInfo)
    disclaimer: str = DISCLAIMER_TEXT


class QueryHistoryItem(BaseModel):
    model_config = ConfigDict(extra="ignore")
    id: str
    question: str
    verdict: str
    confidence: str
    payable: int
    created_at: str


# Document schemas
class DocumentUploadResponse(BaseModel):
    model_config = ConfigDict(extra="ignore")
    document_id: str
    file_name: str
    pages: int
    chunks: int
    status: str = "indexed"
    degraded: List[str] = Field(default_factory=list)


class DocumentDetailResponse(BaseModel):
    model_config = ConfigDict(extra="ignore")
    document_id: str
    status: str
    pages: int
    chunks: int
    summary: Dict[str, Any] = Field(default_factory=dict)


# Estimate schemas
class EstimateRequest(BaseModel):
    model_config = ConfigDict(extra="ignore")
    policy_id: str = "star"
    treatment_id: str
    cost: Optional[int] = None
    days: Optional[int] = 1
    hospital: Optional[Literal["network", "non_network"]] = "network"
    room: Optional[Literal["within_limit", "exceeds_deluxe", "suite"]] = "within_limit"
    age_band: Optional[int] = 45
    ped: Optional[bool] = False
    tenure_months: Optional[int] = 36


class EstimateResponse(BaseModel):
    model_config = ConfigDict(extra="ignore")
    cost_estimate: CostEstimate
    trace: List[TraceStep] = Field(default_factory=list)
    confidence: ConfidenceType
    uncertainty: UncertaintyInfo
    evidence: List[EvidenceCitation] = Field(default_factory=list)
    disclaimer: str = DISCLAIMER_TEXT


# Treatment catalogue schemas
class TreatmentListItem(BaseModel):
    model_config = ConfigDict(extra="ignore")
    id: str
    name: str
    category: str
    icd: Optional[str] = None
    cost_range: Optional[Dict[str, int]] = None
    average: int


class TreatmentDetail(BaseModel):
    model_config = ConfigDict(extra="ignore")
    id: str
    name: str
    category: str
    icd: Optional[str] = None
    specific_waiting: bool = False
    excluded: bool = False
    exclusion_code: Optional[str] = None
    day_care: bool = False
    cost_range: Optional[Dict[str, int]] = None
    average: int
    room_rate: int = 0
    icu_rate: int = 0
    icu_days: int = 0
    default_days: int = 1
    heads: Dict[str, int] = Field(default_factory=dict)


# Policy schemas
class PolicySummaryResponse(BaseModel):
    model_config = ConfigDict(extra="ignore")
    id: str
    insurer: str
    policy_name: str
    sum_insured: int
    policy_period: str
    waiting_periods: Dict[str, Any]
    room_rent_limit: str
    icu_limit: str
    co_payment: str
    sub_limits: Dict[str, Any]
    proportionality: bool
    deductible: int


class PolicyCoverageResponse(BaseModel):
    model_config = ConfigDict(extra="ignore")
    policy_id: str
    inclusions: List[EvidenceCitation] = Field(default_factory=list)


class ExclusionCluster(BaseModel):
    model_config = ConfigDict(extra="ignore")
    irdai_code: str
    title: str
    description: str
    clauses: List[EvidenceCitation] = Field(default_factory=list)


class PolicyExclusionsResponse(BaseModel):
    model_config = ConfigDict(extra="ignore")
    policy_id: str
    exclusions: List[ExclusionCluster] = Field(default_factory=list)


# Health schema
class HealthResponse(BaseModel):
    model_config = ConfigDict(extra="ignore")
    status: Literal["healthy", "degraded", "unhealthy"]
    db: str
    vector_store: str
    embedding: str
    llm: str
    degraded: List[str] = Field(default_factory=list)
