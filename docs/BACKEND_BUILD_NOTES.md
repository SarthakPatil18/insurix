# Insurix Backend Build Notes

## Architectural Foundations & Decisions

### 1. Zero External Services in Offline CI Mode
- Implemented an async database abstraction in `backend/db/database.py` that utilizes PostgreSQL + pgvector when configured, and falls back to SQLite in-memory tables during offline testing.
- Built a deterministic bag-of-words salted hashing embedder in `backend/services/embedding_service.py` producing 384-dimensional unit vectors when sentence-transformer weights cannot be loaded without internet access.
- Implemented a deterministic answer synthesizer in `backend/services/llm_service.py` that generates grounded answers quoting exact section and page citations when `GROQ_API_KEY` is not provided.
- The `/health` endpoint probes the database, vector store, embedding model, and LLM connection, honestly reporting `degraded: ["embedding", "llm"]` without failing or crashing.

### 2. Strict Mathematical Ledger Parity
- **Observation**: Python's native `round()` implements banker's rounding (rounding half to the nearest even integer), while JavaScript's `Math.round()` uses round-half-up (`floor(x + 0.5)`).
- **Adaptation**: In `backend/utils/money.py`, `to_rupees` implements `math.floor(float(val) + 0.5)` to guarantee exact mathematical equivalence down to the single rupee across all 5,760 combinatorial vectors.
- All monetary arithmetic enforces the fundamental ledger identity:
  $$\text{Total Cost} - \sum \text{Deductions} \equiv \text{Insurer Payable}$$
  verified with 100% pass rate in `backend/tests/test_rule_engine_parity.py`.

### 3. Response Schema & Contract Integrity
- Response schemas in `backend/models/schemas.py` match the frontend contract:
  - `answer`, `verdict`, `verdict_label`, `confidence`, `evidence`, `cost_estimate`, `uncertainty`, `trace`, `llm`, `disclaimer`.
- Every evidence item carries `text`, `page`, `section`, `score`, and `policy_id`.
- The frontend adapter in `index.html` dynamically probes `http://localhost:8123/health` on load, activating live server queries while preserving full offline capability.
