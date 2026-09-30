# INSURIXX — mainidea.md

## The Big Idea

**Insurixx is not a chatbot. It is a policy-dissection workbench.**

A customer holds a 60-page health insurance policy they cannot read. Insurixx takes that policy (physical on-screen, as a stack of paper), pins down each clause as evidence, runs the treatment through a deterministic 14-rule financial cascade, and prints an auditable receipt showing — to the exact rupee — what the insurer must pay, what the patient pays, which clause says so, which page it is on, and what is still uncertain.

**Core Journey (the value chain):**
```
Policy (PDF / sample)
  → Evidence (verbatim clause retrieval: Page 18 · §4.2)
    → Treatment scenario (knee replacement, deluxe room, 24m tenure)
      → Coverage rules (waiting clocks, exclusions, sub-limits, room caps)
        → Cost estimation (head-wise bill reconstruction)
          → Out-of-pocket (deduction cascade → payable vs liability)
            → Explainability (verdicts stamps, trace, citations)
              → Uncertainty detection (missing data, degraded models)
```

If a step breaks, the software does not hallucinate an answer — it degrades honestly, shows you which subsystem is "off," and keeps the math running deterministically on local fallback.

---

## 1. Product Identity: "The Policy, Dissected."

The defining idea of Insurixx's UX is: **treat a health insurance policy as a physical object laid on a forensic-lab bench.**

| Metafor | Realised In UI |
|---|---|
| Policy is a physical thing | `PolicyStack3D` hero; stacked paper; manila folder tabs for Star/Royal/HDFC |
| Evidence is pinned to a corkboard | `RedStringBoard`, `CitationChip` (teal background = evidence) |
| Verdict stamped like a file | `VerdictStamp` component: all-caps ink border, slight rotation (Verdict: COVERED · WITH DEDUCTIONS) |
| Deduction is a cut, not a number | `PenaltySlab3D` — chunk carved off the money slab proportional to the penalty |
| Waiting clocks are physical dials | `WaitingDial3D` — 24-month PED dial animates, but 2D fallback is a percentage arc |
| Final financials are a receipt | `CostReceipt` — perforated bottom edge, `LedgerLine` rows, tabular Bricolage numbers |
| Grid is the cutting mat | 34 px linear-gradient grid with every 5th line heavier; viewport-edge ruler ticks; parralax on scroll |

### Why not a generic SaaS dashboard?
Because generic SaaS UX says "trust us, the AI knows." Insurixx says **"here is the clause, here is the page, we stamped the file, you can check my work."** That trust gap is the product.

---

## 2. Design Token Law (enforced, never decorative)

From [DESIGN_SPEC.md](file:///c:/Users/Rehan/OneDrive/Desktop/hacakathon/HackMetrix/docs/DESIGN_SPEC.md) → codified in [tokens.css](file:///c:/Users/Rehan/OneDrive/Desktop/hacakathon/HackMetrix/frontend/src/styles/tokens.css)

**Material:**
- `--ink: #111111`
- `--paper: #F7F3EC`
- `--sheet: #FFFDF8`
- `--grain` (photocopy noise filter, optional)

**Semantic colours (each has ONE job, never mixed):**
| Token | Meaning | Appears On |
|---|---|---|
| `--lime #DDF247` | COVERED · VERIFIED · ACTIVE | Verdict stamp background, CTA buttons, active policy tab, Online status pill |
| `--red #FF4B3E` | EXCLUDED · PENALTY · DEDUCTION · WARNING ONLY | Deduction rows in receipt, penalty carve in PenaltySlab3D, exclusion badges, CLAIM DISALLOWED stamps. **NEVER decorative.** |
| `--teal #58D9C9` | EVIDENCE · CITATION · SOURCE | CitationChip, EvidencePanel, page references, ClauseViewer header |
| `--lilac #B892FF` | ESTIMATE · UNCERTAINTY · AI-GENERATED ORACLE | Missing-info dashed border boxes, 5,760 oracle parity indicator, "DEVELOPMENT MODE" header tags. **Never for confirmed policy clauses.** |

**Shadows (zero blur, always XY ink offset — no neumorphism, no glow):**
`--shadow-sm: 3px 3px 0 --ink` → `md: 6px` → `lg: 10px` → `xl: 14px`.

**Typography (two fonts, one purpose each):**
- **Bricolage Grotesque:** UI, money (tabular-nums, 700 weight — loudest thing on screen), stamps, folder tabs
- **Newsreader Italic:** Only for verbatim quoted policy clauses inside `<ClauseViewer />` and `<EvidencePanel />`

**Corners (three radii, each meaning something):**
- Paper/receipts = `0px` (square, like an office document)
- Sticker/tag badges = `18px` (die-cut sticker)
- Chips/toggles only = `999px` (pill)

**Accessibility is designed in:**
- `:focus-visible` = 3 px solid ink outline (no fuzzy blue)
- `@media (prefers-reduced-motion)` kills hero animation, stamp bounce, 3D rotations
- Every verdict stamp carries both **colour** AND **text** + **icon** (color-independent)
- All icon buttons: aria-labels, `aria-live="polite"` on toast queue

**Dark mode (Night Lab):**
`data-theme="dark"` on `<html>` flips tokens (paper→ink, sheet→#15140F) in the same tokens.css file. Persisted in `localStorage` under key `insurix_theme` with 3 internal states: `light` / `dark` / `system`.

---

## 3. Frontend Architecture

Stack: **React 18 + TypeScript (strict) + Vite 6.4 + Pure CSS (no Tailwind).** Why pure CSS? Because the neo-brutalist material system has unique corner/shadow/grid rules that a utility layer would just repeat verbosely.

Source: [frontend/src/](file:///c:/Users/Rehan/OneDrive/Desktop/hacakathon/HackMetrix/frontend/src/)

```
App.tsx ─── shell (theme+policy state, 4-view routing, health probe, toast queue, Escape handler)
├─ hooks/             → useTheme · usePolicy · useChat · useCalculator  (own state + effects; NO inline math)
├─ components/
│   ├─ ui/            → atomic Paper/Stamp/Button/Card/Badge/Modal/Toast/VerdictStamp
│   ├─ policy/        → PolicySelector (folder tabs) · PolicySummaryCard · ClauseViewer · PolicyStack3D
│   ├─ evidence/      → CitationChip · EvidencePanel · RedStringBoard
│   ├─ calculator/    → TreatmentCalculator · PenaltySlab3D · WaitingDial3D
│   ├─ receipt/       → CostReceipt · LedgerLine
│   ├─ upload/        → PolicyUploadZone (UPLOADING → RECEIVED → PROCESSING → READY → FAILED)
│   └─ navigation/    → Header · MobileDrawer (4 routes)
├─ pages/
│   ├─ Home/          → Hero stack + 3 pillar cards + insurer logo carousel
│   ├─ Studio/        → TWO-PANEL WORKBENCH  (LEFT / RIGHT)     ← THE PRODUCT
│   ├─ Policies/      → 3 insurers, filed schedule, clause viewer modal
│   └─ HowItWorks/    → 6-step pipeline, backend-info CTA
├─ services/
│   ├─ api/           → apiClient (HTTP, auto-Content-Type, 2s timeout, structured ApiError)
│   │                  ├─ policyService   (GET /api/policy/{id}/{summary,coverage,exclusions})
│   │                  ├─ chatService     (POST /api/query)
│   │                  ├─ calculatorService (POST /api/estimate, GET /api/treatments)
│   │                  └─ uploadService   (POST /api/documents/upload, FormData)
│   └─ data/          → samplePolicies.ts (3 insurers, real clauses w/ page refs) · sampleTreatments.ts (5 surgeries w/ head-wise costs)
├─ types/             → policy.ts · query.ts · estimate.ts  (UI ↔ FastAPI contracts shared verbatim)
├─ utils/             → money · formatting · security (sanitizeInput, sanitizeFilename, validatePolicyFile: %PDF- magic, 10MB, keyword scan)
├─ styles/            → tokens.css · globals.css
├─ scenes/            ← (empty dir) reserved for GSAP/Three.js scene slices
└─ features/          ← (empty dirs: 7 slices) reserved for feature-based code-splitting in Phase 3
```

**Hard rules in code:**
1. **No component ever calls `fetch()` directly.** All HTTP goes through `services/api/*`. Every service has a `*Local()` path that activates automatically on any fetch exception.
2. **No financial math in React hooks or components.** `useCalculator` → `calculatorService.calculate()` → either FastAPI `/api/estimate` or `calculateLocal` (the same 14-rule cascade ported to TS). Never inline arithmetic.
3. **No `innerHTML`, no `eval`, no dynamic script tags.** `sanitizeInput()` strips angle brackets before rendering. `sanitizeFilename()` whitelists `[A-Za-z0-9._-]`. Upload validation enforces: PDF magic bytes, 10 MB cap, ≥3 insurance keyword hits from a 27-keyword lex.
4. **Every answer has evidence.** If the backend doesn't return citations (e.g. offline mode synthesizes an answer), the UI explicitly labels it "Citation development state — backend offline" in a lilac dashed box rather than inventing page numbers.

---

## 4. Studio (the workbench): the left-right split

Source: [StudioPage.tsx](file:///c:/Users/Rehan/OneDrive/Desktop/hacakathon/HackMetrix/frontend/src/pages/Studio/StudioPage.tsx#L1-L212)

The Studio is the product. Everything else (Home, Policies, How It Works) supports it.

### LEFT PANEL — "ASK THE POLICY"
Powered by `useChat` → `chatService.askQuestion(question, activePolicyId)`.

1. Welcome message with 4 preset chips (knee, cataract, room cap, PED waiting).
2. User types → submits.
3. Assistant renders:
   - **Verdict Stamp** (COVERED / CONDITIONAL / CLAIM DISALLOWED)
   - Short answer paragraph (synthesized by LLM OR the 4-branch offline rule in `askQuestionLocal`)
   - **Evidence Panel** — up to 3 teal `CitationChip`s: each chip reads `Page X · §Y.Z · Score`, click opens `ClauseViewer` modal showing the clause body in Newsreader italic.
   - **Red String Board** — SVG lines connecting the question → evidence chips → verdict (metaphor for "the evidence pins the answer down").
   - **Uncertainty Box** — lilac dashed border listing missing info + recommendation, if the uncertainty service says so.
4. Thread scrolls, keyboard: Enter to send, Escape to close clause viewer.

### RIGHT PANEL — "WHAT WILL I PAY?"
Powered by `useCalculator` → `calculatorService.calculate({procedure, hospital, room, age, tenure, quoted_total, waiting_status, ped})`.

1. Inputs (all re-calc on change via `useEffect`):
   - Procedure dropdown (5 default: knee, cataract, appendectomy, CABG, dialysis)
   - Hospital type: network / non-network (triggers 12% customary deduction)
   - Room category: within_limit / standard / deluxe / exceeds_deluxe / suite (triggers the Rule 7 proportional cascade)
   - Patient age
   - Tenure months (drives 30-day / 24-month / PED 36-month clocks)
   - Quoted total bill (₹)
2. Live re-calculation on mount + every change (no submit button required; offline so instant; FastAPI ~40 ms via Vite proxy).
3. Result:
   - **CostReceipt** — perforated, ledger rows in order of 14-rule cascade, final Insurer Payable vs Out-of-Pocket in bold tabular money.
   - **PenaltySlab3D** — a money block with the penalty portion literally carved out; 2D fallback: stacked bar chart.
   - **WaitingDial3D** — tenure/required ratio arc; 2D fallback: progress bar.
   - **Confidence** pill + `VerdictStamp` (partial coverage vs full coverage vs denied).

### TOP OF STUDIO
- `PolicySelector` — three manila folder tabs (Star ₹5L / Royal ₹10L / HDFC ₹5L), underlines selected with lime
- `PolicySummaryCard` — schedule table (room cap, ICU cap, co-pay, sub-limits)

---

## 5. Backend Architecture (Python FastAPI — 100% audited)

Backend audit score: **62/62 (100.0%)** — [BACKEND_AUDIT_REPORT.md](file:///c:/Users/Rehan/OneDrive/Desktop/hacakathon/HackMetrix/docs/BACKEND_AUDIT_REPORT.md)

Source: [backend/](file:///c:/Users/Rehan/OneDrive/Desktop/hacakathon/HackMetrix/backend/)

**Stack:** FastAPI 0.110 + SQLAlchemy 2.0 async + pgvector (SQLite fallback) + Pydantic v2 + Alembic + PyMuPDF + pdfplumber + sentence-transformers (BGE-small-en-v1.5 384d) + rank_bm25 + Groq (Llama-3.3-70b-Versatile, temp ≤0.2).

**App factory & lifespan** in [main.py:25-130](file:///c:/Users/Rehan/OneDrive/Desktop/hacakathon/HackMetrix/backend/main.py#L25-L130):
- lifespan: `init_db()` → `load_sample_policies()` (3 insurers into the chunk index)
- middleware: CORS (from settings) + `X-Request-ID` + `X-Response-Time` (ms)
- exception handler: structured `InsurixError` → JSONResponse
- routers: documents_router · query_router · estimate_router · policy_router
- `/health` actively probes 4 subsystems (DB, vector store, embedding model, LLM) and honestly returns `"degraded"` with a list — no silent failures.

### 4 Routers

| Prefix | Router | Endpoints |
|---|---|---|
| `/api/documents` | `documents.py` | POST `/upload` — multipart, `%PDF-` magic, 10 MB, returns 201 w/ doc_id · pages · chunks; GET `/{id}` (status); DELETE `/{id}` (204 purge index) |
| `/api/query` | `query.py` | POST `/` → grounded answer w/ citations + estimate + uncertainty + trace; POST `/stream` Server-Sent Events reason steps; GET `/history` session-scoped |
| (root `/api`) | `estimate.py` | POST `/estimate` 14-rule calculation → lines ledger + trace; GET `/treatments`, `/treatments/{id}` catalog |
| `/api/policy` | `policy.py` | GET `/{id}/summary`, `/coverage`, `/exclusions` (Star, Royal, HDFC = 3 sample policies) |

### End-to-end ingestion pipeline → [pipeline.py](file:///c:/Users/Rehan/OneDrive/Desktop/hacakathon/HackMetrix/backend/services/pipeline.py#L1-L82)
```
PDF bytes
  → pdf_service.extract_pdf_content (PyMuPDF prose + pdfplumber tables, preserved page # per block)
    → chunking_service.chunk_policy_blocks (section regex: §4.2 / Excl01 / DEFINITIONS; 500-token fallback)
      → PII scrub (utils/pii.py: emails, phones, PAN, Aadhaar, policy IDs, patient names) BEFORE embedding
        → embedding_service.encode_texts (BGE-small 384d OR deterministic SHA hash fallback if sentence-transformers unavailable)
          → vector_service.register_in_memory_chunks (pgvector + BM25Okapi fused by Reciprocal Rank Fusion k=60 + EXCLUSION GUARANTEE)
```

### Retrieval (hybrid + exclusion guarantee)
`vector_service.query_similar(question)` — dense cosine top-25 + sparse BM25 top-25 → RRF merged + reranked → exclusion clauses boosted to never be filtered out by the dense model (so the system cannot accidentally hide a "not covered" rule).

### 14-Rule Deterministic Deduction Engine — the soul of the product
[rule_engine.py](file:///c:/Users/Rehan/OneDrive/Desktop/hacakathon/HackMetrix/backend/services/rule_engine.py#L12-L200)

**Ledger Identity (non-negotiable):**
```
Total Quoted Cost − Σ Deductions ≡ Insurer Payable ≡ Total Quoted Cost − Out-of-Pocket
```

Verified by **5,760 parity vectors**: `pytest backend/tests/test_rule_engine_parity.py` — 100.0% pass (both Python `rule_engine.py` and the standalone TS `calculatorService.calculateLocal` are cross-checked to the exact rupee on every single vector).

Rule cascade in order:
```
1.  PERMANENT EXCLUSION SCAN   ─ cosmetic/aesthetic → CLAIM DISALLOWED
2.  30-DAY INCEPTION CLOCK     ─ tenure ≤ 30d non-accident → disallowed
3.  SPECIFIED PROCEDURE CLOCK  ─ cataract, joint replacement, CABG require 24m
4.  PRE-EXISTING DISEASE CLOCK ─ Star=36m, Royal/HDFC=24m
5.  BILL RECONSTRUCTION        ─ 8% non-medical consumables + 12% non-network tariff
6.  ROOM RENT CAP CHECK        ─ policy capping (e.g. 1% SI/day = ₹5,000 for Star)
7.  PROPORTIONAL DEDUCTIONS    ─ if room exceeds, cascade across doctor/OT/nursing (Star=22%, Royal=15%, Suite=38% universal)
8.  ICU DAILY LIMIT            ─ within 2% SI/day, no proportionality
9.  IMPLANT / PROSTHESIS CAPS  ─ e.g. intraocular lens (Star=₹15,000, Royal=₹25,000)
10. ADMISSIBLE ASSEMBLY        ─ allowable_base = total − room − nonmedical − tariff (floor 0)
11. DISEASE SUB-LIMITS         ─ cataract (Star ₹25,000, Royal ₹50,000), etc.
12. SUM INSURED CEILING        ─ cap at annual policy sum_insured
13. VOLUNTARY DEDUCTIBLE       ─ if declared
14. CO-PAYMENT CASCADE         ─ ≥60 age 10% (Star) OR non-network co-pays
```

Every rule appends a `TraceStep(rule="RULE X · …", detail=…)` returned in the API response, so the frontend can show the exact reasoning chain on demand.

### Honest Degradation (never silent)

If any model is missing, the `/health` endpoint returns `{"status": "degraded", "degraded": ["llm", "embedding"], …}`. Both LLM and embedding have deterministic fallbacks:
- No LLM key → `llm_service.deterministic_citation_synthesizer` stitches evidence chunks into a quoted answer.
- No sentence-transformers → `embedding_service.deterministic_hash_fallback` (128-dim SHA-based vectors that still allow cosine ordering).

**No hallucinations. No "I don't know but let me guess." Every answer either cites, or degrades, or disclaims.**

---

## 6. Frontend-Backend Contract (shared verbatim)

| Direction | Path | Contract Source |
|---|---|---|
| UI → FastAPI | Vite dev proxy: `localhost:5173/api/*` → `http://127.0.0.1:8123/api/*` and `/health` → `8123/health` | [vite.config.ts](file:///c:/Users/Rehan/OneDrive/Desktop/hacakathon/HackMetrix/frontend/vite.config.ts) |
| Pydantic ↔ TS types | `backend/models/schemas.py` ↔ `frontend/src/types/{policy,query,estimate}.ts` | Hand-maintained structural parity (no codegen yet); tests in `test_api_contract.py` |
| QueryResponse | `{answer, verdict, verdict_label, confidence, evidence:[{text,page,section,score,policy_id}], cost_estimate, uncertainty:{confidence,missing_info,recommendation}, trace, disclaimer}` | Both sides identical |
| EstimateResponse | `{verdict, verdict_label, estimate:{total_cost, payable, out_of_pocket, admissible, deduction_total, pct, lines:[{label,amount,kind}]}, trace}` | Both sides identical |
| Upload lifecycle in UI | UPLOADING → RECEIVED → PROCESSING → READY → FAILED | Mirrors `documents.py` state + `processing` flag in uploadService (never shows READY before document GET returns `chunks_count > 0`) |

---

## 7. Test Philosophy: Oracle Parity + Contracts

No unit test without a contract, no contract without a parity oracle.

### Python (pytest) — [backend/tests/](file:///c:/Users/Rehan/OneDrive/Desktop/hacakathon/HackMetrix/backend/tests/)
```
conftest.py               ← fixtures: app_client, in_memory_vector_index
test_api_contract.py      ← 14 HTTP calls vs 14 endpoints, asserts full response schema (21 tests total — ALL PASS)
test_chunking.py          ← section-detect regex, atomic table blocks, 500-token fallback
test_money.py             ← rupee-safe arithmetic + paise rounding edge cases
test_pii.py               ← scrub PAN / Aadhaar / phone / email / names
test_retrieval.py         ← hybrid RRF quality + exclusion guarantee (excl clause ≥1 in top-5 on a "knee" query)
test_rule_engine_parity.py← 5,760 combinatorial vectors × ledger identity  (both sides of the TS/PY parity)
parity_vectors.json       ← the 5,760 vector oracle (policy × treatment × hospital × room × age × tenure × quoted)
```

### JavaScript (node, no Jest needed for pure math)
```
frontend/tests/rule-engine.test.js   ← loads parity_vectors.json, runs 5,760 through the *frontend TS local calculator*, asserts ledger identity + non-neg + payable==OOP inverse.
frontend/tests/dom.test.js           ← 69 structural assertions on the LEGACY root index.html (preserved — still passes because we never deleted the old SPA).
```

### Frontend TS Strict
`tsconfig.json` → `strict: true, noUncheckedIndexedAccess: true, noImplicitOverride: true`. Build gate is:
```json
"build": "tsc --noEmit && vite build"
```
So if TS catches one implicit any, the build aborts **before Vite even starts.**

---

## 8. Dual Frontends (Legacy vs Modern) — Why both exist

| App | Location | How to Run | Status |
|---|---|---|---|
| **Legacy single-file SPA** | Root `index.html` (~4,338 lines) generated by `generate_site.py` (~1,964 lines) | `python -m http.server 3000` then open `index.html` | ✅ Fully functional. `dom.test.js` 69/69 pass. Neo-Brutalist Space Grotesk theme, reactive calculator, insurer carousel. |
| **React/Vite modern** | `frontend/` (modular components, TS strict) | `cd frontend && npm run dev` → `http://localhost:5173/` (478 ms boot) | ✅ Fully functional. `npm run build` → 240 kB / 71 kB gz. |

**Migration rule (per AGENTS.md #17):** Never delete the old `index.html` until the React app has been proven to cover every legacy view. Old single-file home hero includes views the React app has not yet fully ported (Pricing hero, FAQ, Contact forms, Features 2–3). Old SPA is the reference surface; React SPA is the target surface. dom.test.js pins the legacy DOM structure so we can detect accidental regression of the reference during future migration.

---

## 9. Deployment

**Vercel config**: [vercel.json](file:///c:/Users/Rehan/OneDrive/Desktop/hacakathon/HackMetrix/vercel.json) → `cleanUrls: true`. Live demo: [https://insurix-nine.vercel.app](https://insurix-nine.vercel.app) serves the legacy single-file app from the repo root.

To deploy React app instead: `cd frontend && npx vercel --prod` (Vite build step is auto-detected by `vercel.json` via the presence of package.json).

Backend is not yet cloud-deployed; runs locally on port 8123. Frontend gracefully degrades to local deterministic mode if backend is unreachable (so the vercel.app demo still works perfectly without FastAPI).

---

## 10. Known Gaps (what Phase 3 must do)

Ordered by user value:

1. **Real OCR + IRDAI chunker** — `pdf_service.py` uses PyMuPDF text, which fails on scanned-image PDFs. Phase 4 task (per AGENTS.md): wire Tesseract/PaddleOCR or an IRDAI commercial PDF chunker into `/api/documents/upload`'s `ocr_needed = True` branch.
2. **pgVector vs in-memory fallback** — `database.py` auto-falls back to SQLite in-memory list indexing. Production deployment must export `DATABASE_URL=postgresql+psycopg://…` with the pgvector extension enabled to actually scale policy ingestion beyond 3 insurers.
3. **Live hospital tariff benchmarking** — `treatments.json` has fixed 2025 price ranges. Phase 6 is real API integration with hospital TPAs / Healthcloud-style tariff databases to refresh `quoted_total` suggestions by procedure × geography × hospital tier.
4. **Streaming `/api/query/stream` not yet in the UI** — endpoint exists in FastAPI (SSE), `chatService` POSTs to non-stream `/api/query`. Phase 3 can swap `fetch` for `EventSource` to display reason tokens as they arrive.
5. **Query history not in UI** — `GET /api/query/history` works; no drawer/page renders it yet.
6. **`features/` and `scenes/` directories are architectural placeholders.** Phase 3 moves logic from `hooks + pages` into feature-sliced modules (e.g., `features/policy-chat/` owns `useChat + chatService + EvidencePanel`), and 3D scenes out of `components/*` into `scenes/*` with lazy `React.lazy` loading so the app ships 0 WebGL when users never scroll to it.
7. **MobileDrawer does not show policy selector inside it** — mobile user must navigate to Studio then use the folder tabs. Quick fix in Phase 3: pass policies+activeId+onSelect to MobileDrawer and add a section under the nav items.

---

## 11. The One-Sentence Pitch

> *Insurixx dissects your 60-page Indian health insurance policy into a lab-bench workbench: every coverage verdict cites a page-stamped clause, every rupee of out-of-pocket flows through a 14-rule audit trail, and when a model degrades the software admits it instead of guessing — turning claim-day shock into pre-admission clarity.*
