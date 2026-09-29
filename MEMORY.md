# INSURIXX — MEMORY.md (Engineering Memory Bank)

## 1. Project Context & State

- **Product:** Insurixx — AI Health Insurance Intelligence Platform
- **Core Journey:** `Policy → Evidence → Treatment → Coverage → Cost`
- **Design System:** "The Policy, Dissected." (Tactile paper, cutting-mat grid, rubber stamps, evidence pins, Bricolage Grotesque + Newsreader typography)
- **Current Phase:** Phase 2 Repair — React/Vite Frontend Established & Functional
- **Repository Root:** `c:\Users\Rehan\OneDrive\Desktop\hacakathon\HackMetrix`

---

## 2. Agent History

| Date | Agent | Work | Why | Files |
|---|---|---|---|---|
| 2026-09-29 | Lead Architect | Full codebase audit & reconnaissance | Establish ground truth before changing code | `audit.md`, `docs/CURRENT_STATE.md` |
| 2026-09-29 | Lead Architect | Governance & rules initialization | Define 8 agent roles, constraints & definition of done | `AGENTS.md` |
| 2026-09-29 | Lead Architect | Architectural blueprinting | Map CURRENT → MIGRATION → TARGET system architecture | `docs/ARCHITECTURE.md` |
| 2026-09-29 | Lead Architect | 8-Phase migration plan | Detailed roadmap preventing disruptive rewrites | `docs/MIGRATION_PLAN.md` |
| 2026-09-29 | Lead Architect | Target modular folder structure & contracts | Set up `src/` modular foundation and interfaces | `src/styles/`, `src/engine/`, `src/data/`, etc. |
| 2026-09-29 | QA / Security Agent | Critical security & stability patches | Fix DOM XSS, filename injection, quote escaping, cross-platform path | `index.html`, `generate_site.py` |
| 2026-09-29 | Insurance Engine Agent | Reactive calculator synchronization & structured rules | Ensure active policy drives calculation without hardcoded insurer checks | `index.html`, `src/engine/` |
| 2026-09-29 | Frontend / UI Agent | Accessibility baseline & keyboard handling | Enter key on chat, Escape key on modals, high contrast focus ring | `index.html` |
| 2026-09-29 | Full Stack Core Team | Phase 2: Full-Stack Core + Frontend Migration | Connected React + Vite + Express + FastAPI + PostgreSQL schema | `frontend/`, `backend/`, `services/intelligence/` |
| 2026-09-29 | Lead Architect (Gemini 3.8 Flash) | Remote Git Synchronization & Conflict Resolution | Pulled `origin/main` (`063072a`), cleanly merged remote policy document validation with local security and modular architecture patches | `index.html`, `MEMORY.md` |
| 2026-09-29 | Workspace Operations (Gemini 3.8 Flash) | Workspace Cleanup & Reset | Deleted all files and subdirectories (`.git/`, `backend/`, `docs/`, `frontend/`, `services/`, `src/`, `test/`, etc.) keeping strictly `AGENTS.md` and `MEMORY.md` per explicit user request | All root directories & files except `AGENTS.md`, `MEMORY.md` |
| 2026-09-29 | Git Integration Agent (AI Model: Gemini 3.8 Flash) | Remote Git Ingestion | Initialized git, connected `origin` to `https://github.com/SarthakPatil18/insurix.git`, fetched all remote refs, checked out `origin/main` tracking branch while keeping `AGENTS.md` and `MEMORY.md` intact | `index.html`, `generate_site.py`, `README.md`, `MEMORY.md` |
| 2026-09-29 | Git Integration Agent (AI Model: Gemini 3.8 Flash) | Full Codebase Ingestion | Pulled complete codebase from `origin/main` (commits `8d0c422` & `f9d9343`), integrating full FastAPI backend (4 REST routers, PyMuPDF+pdfplumber chunking, hybrid search, 14-rule deterministic engine, Alembic models), tests, audit reports, and docs | `backend/`, `docs/`, `frontend/tests/`, `samples/`, `index.html`, `README.md`, `MEMORY.md` |
| 2026-09-29 | Frontend Repair Agent | **Phase 2 Repair: Created missing React entry points `main.tsx` & `App.tsx`** | Phase 2 frontend was structurally incomplete — `frontend/src/` had 30+ components, hooks, services, pages, types, styles but was missing the two critical React entry files (`main.tsx` and `App.tsx`) causing `npm run dev` to serve a blank page. Also fixed MobileDrawer/Toast prop-interface mismatches, added missing `HowItWorksPage`, created `scenes/` and 7 `features/*` architecture directories, verified all 5 npm scripts pass (dev, build, preview, typecheck, test). | `frontend/src/main.tsx`, `frontend/src/App.tsx`, `frontend/src/pages/HowItWorks/HowItWorksPage.tsx`, `frontend/src/scenes/`, `frontend/src/features/{policy-chat,policy-upload,coverage,treatment-cost,evidence,scenarios}/` |
| 2026-09-29 | Frontend / UI & DevOps Agent (Gemini 3.8 Flash) | **Real Insurer Logos Carousel & Vercel Production Deployment** | Added real high-res SVG & PNG logos for all 9 supported insurers (Star Health, HDFC ERGO, Care Health, ICICI Lombard, Niva Bupa, Tata AIG, Bajaj Allianz, National Insurance, New India Assurance). Implemented infinite sliding marquee carousel animation with seamless looping, hover-to-pause UX, and live official external links. Created `vercel.json` and deployed project to Vercel production: `https://insurix-nine.vercel.app`. | `assets/insurers/*`, `index.html`, `generate_site.py`, `vercel.json`, `frontend/public/assets/insurers/*`, `MEMORY.md` |
| 2026-09-29 | Documentation & QA Agent (Gemini 3.8 Flash) | **README Overhaul & Link Integrity Polish** | Completely overhauled `README.md` to ensure neat, clean formatting with 100% valid links: verified live Vercel badge (`https://insurix-nine.vercel.app`), updated Supported Insurers table with official portal URLs, fixed table of contents navigation with explicit HTML anchors, updated project directory tree reflecting the full workspace, verified all internal file links. | `README.md`, `MEMORY.md` |
| 2026-09-29 | Frontend / UI Agent (Gemini 3.8 Flash) | **Extended Hero Banner & Centered Live Policy Parser** | Redesigned the hero landing page: extended the Hero Card to full-width with a deep Dark Ink theme (`#111111`), luminous typography, neon-lime accents (`box-shadow: 10px 10px 0 var(--lime)`), and high-contrast metrics. Re-architected the Live Policy Parser as a standalone centered workstation card (`max-width: 1080px`) placed directly below the hero banner, featuring an active Vision OCR indicator, enhanced dropzone with progress bar, and sample policy selector. Deployed to Vercel production without unprompted git push. | `index.html`, `generate_site.py`, `MEMORY.md` |
| 2026-09-30 | Frontend / UI Agent (Gemini 3.8 Flash) | **Landing Page Container Color Redesign & Interactive Theme Palette** | Restored the container colors to the user's uploaded reference (`media_1790705744230.png`): default vibrant Lilac Violet (`#A882FF`) with solid black borders (`5px solid #111111`), hard black drop shadow (`10px 10px 0 #111111`), warm radial corner glow, high-contrast dark typography, white tagline box, and crisp metric cards. Added interactive Neo-Brutalist color palette selector with 7 curated themes (Lilac, Lime, Paper, Cyan, Pink, Royal Indigo, Dark Obsidian) and `localStorage` persistence. Synchronized `generate_site.py` and deployed live to Vercel. | `index.html`, `generate_site.py`, `MEMORY.md` |
| 2026-09-30 | Frontend / UI Agent (Gemini 3.8 Flash) | **Dynamic Red Hover Outlines for Boxes & Cards** | Implemented interactive red hover outlines across all box components (`.metric-box`, `.hero-tagline`, `.card`, `.highlight-card`, `.step-card`, `.feature-card`, `.pricing-card`, `.upload-zone`, `.sample-btn`, etc.). Configured `--red` (`#FF4B3E`) and `--red-hover` (`#FF3B30`) design tokens, applying `border-color: #FF3B30` and `outline: 3.5px solid #FF3B30; outline-offset: 3px;` on `:hover` with smooth 0.18s transitions. Deployed to Vercel production without unprompted git push. | `index.html`, `generate_site.py`, `MEMORY.md` |
| 2026-09-30 | Frontend / UI Agent (Gemini 3.8 Flash) | **Locked Landing Container Color to Cyan (`#59D9C9`) & Removed Color Switcher** | Set the permanent landing page hero container background color to vibrant Sky Cyan (`#59D9C9`) with rich black borders and shadow. Completely removed the color switcher UI, swatch buttons, and theme manager script logic per user request. Synchronized `generate_site.py` and deployed live to Vercel production. | `index.html`, `generate_site.py`, `MEMORY.md` |
| 2026-09-30 | Frontend / UI Agent (Gemini 3.8 Flash) | **Reverted Red Hover Outlines & Cleaned Up Landing Header Text** | Reverted the red hover outline styles (`#FF3B30`) across all boxes and cards back to their clean original Neo-Brutalist hover states. Verified and removed any residual `COLOR:` text and swatch elements from the landing hero container header. Synchronized `generate_site.py` and deployed live to Vercel production. | `index.html`, `generate_site.py`, `MEMORY.md` |
| 2026-09-30 | Frontend / UI Agent (Gemini 3.8 Flash) | **Removed Hover Violet Border on Features Page** | Removed `border-color: var(--purple)` from `.feature-card:hover` and `.card:hover`. When hovered, cards elevate and deepen their solid black drop shadow with zero color shift, preserving crisp black borders. Synchronized `generate_site.py` and deployed live to Vercel. | `index.html`, `generate_site.py`, `MEMORY.md` |
| 2026-09-30 | Frontend / UI Agent (Gemini 3.8 Flash) | **Removed Dark Theme Toggle Mode** | Completely removed dark theme toggle button (`#theme-btn`), `.theme-toggle` styles, `body.dark` variables block, and `setupThemeToggle()` script logic. Added initialization cleanup ensuring any legacy dark mode classes or stored preferences in `localStorage` are cleared. Synchronized `generate_site.py` and deployed live to Vercel. | `index.html`, `generate_site.py`, `MEMORY.md` |
| 2026-09-30 | Frontend / UI & DevOps Agent (Gemini 3.8 Flash) | **Removed Contact Section, Synced Generator, Git Committed & Pushed to Remote** | Completely removed the Contact section (`#view-contact`), navbar and mobile drawer links, `.contact-*` and `.social-badge-*` CSS, footer link, and form submit JS handler. Added safe fallback in `navigateTo()` for any legacy routing. Synchronized `generate_site.py` and executed `git push origin main` per explicit user instruction. Deployed live to Vercel production. | `index.html`, `generate_site.py`, `MEMORY.md` |

---

## 3. Key Technical & Architectural Decisions

### Decision 1: Phased Modular Migration over Rewrite
- **Context:** The codebase started as a single-file 4,338-line `index.html`.
- **Decision:** Do NOT destroy the working single-file application. First establish clean contracts, interfaces, and modular files in `src/`, patch critical security/functional issues in `index.html`, and migrate views systematically.
- **Reason:** Guarantees zero regression and maintains working software at all times.

### Decision 2: Purely Deterministic Insurance Mathematics
- **Context:** Health insurance involves complex financial liabilities (deductibles, co-pays, sub-limits, proportional penalties).
- **Decision:** Financial arithmetic is strictly executed by deterministic algorithms. LLMs are never permitted to calculate out-of-pocket totals directly.
- **Reason:** Prevent financial hallucinations and ensure regulatory compliance with IRDAI standards.

### Decision 3: "The Policy, Dissected" Design Direction
- **Context:** Approved specification in `design (1).md`.
- **Decision:**
  - Ink (`#111111`) / Paper (`#F7F3EC`) / Sheet (`#FFFDF8`).
  - Colors carry strict semantic meaning:
    - Red (`#FF4B3E`): Excluded / Penalty / Deductions (Never used decoratively).
    - Lime (`#DDF247`): Covered / Verified / Active.
    - Teal (`#58D9C9`): Evidence / Citations.
    - Lilac (`#B892FF`): AI-estimated / Uncertain values (dashed borders).
  - Fonts: **Bricolage Grotesque** (UI, numbers, tables) and **Newsreader** (quoted policy clauses).
  - Cutting-mat grid (`34px` lines, 5th-line heavy stroke, edge ruler ticks).
- **Prohibited:** Glassmorphism, fintech blue gradients, floating ambient blobs, decorative 3D objects with no product meaning.

### Decision 4: Cross-Platform File Paths
- **Context:** `generate_site.py` contained hardcoded macOS path `/Users/sarthak/Desktop/Insurix/index.html`.
- **Decision:** Update to dynamic repository-relative path resolution (`os.path.join(os.path.dirname(__file__), "index.html")`).

---

## 4. Current State & Known Issues

### Completed in Phase 2 (Verified after Repair):
- [x] React + TypeScript + Vite frontend architecture (`frontend/src/`) with all entry points (main.tsx + App.tsx)
- [x] All 5 package.json scripts verified working: dev, build, preview, typecheck, test
- [x] "The Policy, Dissected" approved design system (`tokens.css`, `globals.css`, cutting-mat grid, paper sheets, verdict stamps, citation chips, receipt perforations, folder tabs)
- [x] Insurixx Studio workspace: Left panel "Ask the Policy" (chat + evidence), Right panel "What Will I Pay?" (calculator + receipt)
- [x] **Python + FastAPI backend** on port 8123 with 4 routers: `/api/policy/*`, `/api/query/*`, `/api/estimate`, `/api/treatments`, `/api/documents/*`, `/health`
- [x] Vite dev proxy: `/api` → `http://127.0.0.1:8123` with health probe and offline deterministic fallbacks
- [x] Deterministic calculation service (room-rent proportionality, sub-limits, co-pays, waiting periods) — in frontend service layer and backend rule_engine.py
- [x] 5760 parity vectors rule-engine oracle tests + 69 DOM assertions all pass
- [x] 4-page routing: Home → Studio → Policies → How It Works
- [x] 3 policies switchable: Star, Royal Sundaram, HDFC ERGO
- [x] 3D PolicyStack3D, PenaltySlab3D, WaitingDial3D with 2D fallbacks
- [x] Night Lab dark mode with `data-theme` attribute + localStorage (3 modes: light/dark/system)
- [x] API service layer with 4 services: policyService, chatService, calculatorService, uploadService (all have offline deterministic fallbacks)
- [x] Sanitization layer: security.ts (sanitizeInput, sanitizeFilename, validatePolicyFile) — zero unsafe innerHTML
- [x] Accessibility: :focus-visible outline, Escape key handling, aria-labels, reduced motion CSS, color-independent semantic stamps

### Open for Subsequent Phases:
- [ ] Connect real OCR PDF ingestion (Tesseract/PaddleOCR/IRDAI chunker) into FastAPI `/extract-policy` (Phase 4).
- [ ] Embed pgVector embeddings into PostgreSQL policy clause retrieval (Phase 5).
- [ ] Live external hospital tariff benchmarking integrations (Phase 6).

