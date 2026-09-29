# INSURIXX — AGENTS.md

## Project Mission

Insurixx is an AI-powered insurance policy intelligence platform.

Core journey:

Policy
→ Evidence
→ Treatment
→ Coverage
→ Cost

The goal is not to build a generic insurance chatbot.

The product must connect:
1. Policy understanding
2. Evidence retrieval
3. Treatment scenario analysis
4. Treatment cost estimation
5. Coverage rule evaluation
6. Out-of-pocket estimation
7. Explainability
8. Uncertainty detection

---

## Sources of Truth

### Product / UX
The approved frontend design specification: [`design (1).md`](file:///c:/Users/Rehan/OneDrive/Desktop/hacakathon/HackMetrix/design%20(1).md) ("The Policy, Dissected.").

### Existing Implementation & Findings
Current repository audit and state assessment: [`audit.md`](file:///c:/Users/Rehan/OneDrive/Desktop/hacakathon/HackMetrix/audit.md) and [`docs/CURRENT_STATE.md`](file:///c:/Users/Rehan/OneDrive/Desktop/hacakathon/HackMetrix/docs/CURRENT_STATE.md).

### Architecture & Roadmap
The migration plan documented in [`docs/ARCHITECTURE.md`](file:///c:/Users/Rehan/OneDrive/Desktop/hacakathon/HackMetrix/docs/ARCHITECTURE.md) and [`MEMORY.md`](file:///c:/Users/Rehan/OneDrive/Desktop/hacakathon/HackMetrix/MEMORY.md).

When sources conflict:
1. Preserve existing working behavior where possible.
2. Follow approved product requirements.
3. Never silently remove functionality.
4. Document architectural changes.

---

## Agent Responsibilities (8 Specialized Roles)

### 1. Architecture Agent
- **Responsibilities:** Repository analysis, modularization, system design, folder structure, contract definitions, dependency decisions.
- **Allowed Changes:** Folder structure, shared interface contracts, build scripts, configuration.
- **Must NOT Change:** Redesign product UX independently, delete working features without documenting why.
- **Dependencies:** Consulted before any structural migration.

---

### 2. Frontend / UI Agent
- **Responsibilities:** Implementing the approved Insurixx design system ("The Policy, Dissected"), typography (Bricolage Grotesque + Newsreader), paper surfaces, rubber stamps, evidence pins, hard shadows, responsive layouts, dark mode, keyboard accessibility.
- **Allowed Changes:** CSS design tokens, HTML markup, component rendering, responsive styles, theme toggle.
- **Must NOT Introduce:** Glassmorphism, generic fintech gradients, soft glows, decorative 3D objects without product meaning, generic rounded cards.
- **Dependencies:** Depends on Architecture Agent for contracts and Insurance Engine for calculation outputs.

---

### 3. Insurance Engine Agent
- **Responsibilities:** Policy schema design, coverage rules, room-rent proportional deduction formulas, deductibles, co-pay rules, disease sub-limits, waiting periods, treatment eligibility, deterministic financial calculations.
- **Allowed Changes:** `src/engine/`, `src/data/policies/`, calculation helper functions.
- **Must NOT Change:** Never hardcode insurer-specific logic into generic calculation functions; never allow an LLM to perform financial arithmetic without deterministic validation.
- **Dependencies:** Provides verified math functions to UI Agent and AI/RAG Agent.

---

### 4. Document Intelligence Agent
- **Responsibilities:** PDF ingestion, OCR text processing, IRDAI document parsing, clause chunking, metadata extraction, page references, clause indexing.
- **Allowed Changes:** Ingestion pipelines, PDF extraction scripts, document schema definitions.
- **Must NOT Change:** Never discard source metadata; every extracted clause must retain page number, section number, and original verbatim quote.
- **Dependencies:** Feeds extracted clauses and metadata to the AI/RAG Agent.

---

### 5. AI / RAG Agent
- **Responsibilities:** Grounded evidence retrieval, medical query NLP, IRDAI clause matching, cited answer generation, uncertainty detection.
- **Allowed Changes:** Prompt templates, retrieval pipelines, uncertainty detection logic, citation formatting.
- **Must NOT Change:** Never allow hallucinated policy answers; every claim must cite verifiable policy evidence. Never invent coverage without retrieved clauses.
- **Dependencies:** Depends on Document Intelligence for clauses and Insurance Engine for coverage rules.

---

### 6. Backend / API Agent
- **Responsibilities:** Node.js/Express and Python/FastAPI service architecture, REST endpoints, database integration (PostgreSQL + pgVector), authentication contracts, rate limiting.
- **Allowed Changes:** Server code, routing, API contracts, middleware, database migrations.
- **Must NOT Change:** Never fabricate backend/API behavior or create fake mocks labeled as production services.
- **Dependencies:** Exposes endpoints to Frontend Agent and coordinates with Intelligence services.

---

### 7. 3D / Motion Agent
- **Responsibilities:** Interactive 3D scene enhancements (The Policy Stack, Penalty Slab, Waiting Dial, Pinboard) using Three.js / React Three Fiber, GSAP, and ScrollTrigger.
- **Allowed Changes:** WebGL canvases, 3D models, shaders, scroll animations.
- **Must NOT Change:** Business logic or accessibility; the entire application (answers, citations, calculator, evidence) must remain 100% usable without WebGL.
- **Dependencies:** Progressive enhancement over the Frontend UI.

---

### 8. QA / Security Agent
- **Responsibilities:** XSS prevention, input sanitization, accessibility compliance (WCAG 2.1 AA), calculation regression testing, error boundary validation, performance testing.
- **Allowed Changes:** Sanitization utilities, test suites, accessibility attributes, error handlers.
- **Must NOT Change:** Never allow unchecked `innerHTML` insertions or broken quote escaping.
- **Dependencies:** Final gatekeeper before any code is considered done.

---

## Global Rules for All Agents

1. **Read Before Modifying:** Read `AGENTS.md` and check `MEMORY.md` before making any code modifications.
2. **Inspect Existing Code:** Inspect existing implementations before creating replacements.
3. **Preserve Working Functionality:** Never silently delete or break existing working features.
4. **Avoid Duplicate Implementations:** Do not create parallel conflicting implementations.
5. **No Fake Intelligence:** Never simulate backend or AI functionality and present it as real.
6. **Ground All Claims:** Every insurance claim must link to traceable evidence.
7. **Deterministic Math:** Financial calculations must be deterministic.
8. **Sanitize Everything:** Never trust user input, uploaded filenames, or OCR text strings in the DOM.
9. **Update Memory:** Update `MEMORY.md` after every significant architectural or design change.
10. **Definition of Done:** A task is complete only when UI works, mobile works, accessibility is verified, calculations are tested, security regressions are absent, and docs are updated.

# Agent Instructions

**RULE 1: Before doing ANYTHING in this codebase, read memory.md completely.**

**RULE 2: After completing any task, update memory.md to reflect what changed. and which agent model used**

**RULE 3: Never assume — if something is unclear, check memory.md first before exploring files.**

This applies to all AI agents, Claude Code sessions, and automated pipelines working in this repo.
