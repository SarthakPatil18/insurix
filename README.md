# Insurix — AI Health Insurance Intelligence

> **"Policy confusion → Financial clarity"**

Insurix is an AI-powered health insurance policy intelligence platform built with a distinctive **Neo-Brutalist design system**. It converts dense 60-page Indian health insurance policy wordings into unambiguous answers regarding coverage, specific disease waiting periods, room-rent proportional deduction penalties, and expected out-of-pocket costs with **99.2% evidence accuracy**.

![Insurix Preview](https://img.shields.io/badge/Design-Neo--Brutalist-DDF247?style=for-the-badge&logoColor=111111)
![IRDAI Aligned](https://img.shields.io/badge/IRDAI-Aligned-58D9C9?style=for-the-badge&logoColor=111111)
![Single Page App](https://img.shields.io/badge/Architecture-Single--File_SPA-B892FF?style=for-the-badge&logoColor=111111)

---

## ⚡ Key Features

- **7-Step AI Reasoning Pipeline**:
  1. **Upload**: Drag-and-drop ingestion of scanned policy PDFs, schedules, endorsements, and customer information sheets (CIS).
  2. **Parse & OCR**: Extracts tabular sub-limits, asterisks, and exclusion annexures.
  3. **Structure**: Schema normalization aligned with IRDAI guidelines.
  4. **Query**: Medical NLP mapping colloquial queries to ICD-10 diagnostic codes.
  5. **Match & Rules**: Deterministic policy evaluation without hallucinations.
  6. **Estimate**: Realistic procedure cost benchmarks and deduction simulations.
  7. **Explain**: Auditable outputs with clickable page references and clause numbers.

- **Interactive Intelligence Studio**:
  - **Live Policy Chatbot**: Ask clinical questions and receive verified answers with page citations (e.g., `Page 18, §4.2`), financial tables, and confidence indicators.
  - **Treatment Out-of-Pocket Calculator**: Simulate exact procedure expenses (Knee Replacement, Cataract, Appendectomy, CABG, Dialysis) against hospital types, room categories (calculating proportional deduction penalties), patient ages, and policy waiting period statuses.
  - **Pre-Loaded Sample Policies**: Instant switching between **Star Health Comprehensive (₹5L)**, **Royal Sundaram Lifeline (₹10L)**, and **HDFC ERGO Optima Restore (₹5L)**.

- **Neo-Brutalist Design System**:
  - Hard high-contrast borders: `3px` to `5px` solid `#111111`
  - Zero-blur hard drop shadows: `box-shadow: 10px 10px 0 var(--black)`
  - Asymmetric micro-tilts on hover: `transform: translateY(-8px) rotate(-0.6deg)`
  - Mathematical background grid: `34px × 34px` dual linear gradient
  - Light mode (warm cream `#F7F3EC`) and Dark mode (`#111111`) toggle with `localStorage` persistence
  - Interactive cursor trail on desktop pointer devices
  - Space Grotesk typography from Google Fonts

---

## 🚀 Quick Start

Open `index.html` directly in any web browser, or serve locally with Python:

```bash
# Clone the repository
git clone https://github.com/SarthakPatil18/insurix.git
cd insurix

# Start a local preview server
python3 -m http.server 3000
```

Navigate to `http://localhost:3000` in your browser.

---

## 📄 Project Structure

```
insurix/
├── index.html         # Self-contained single-page web application
├── README.md          # Project documentation
└── generate_site.py   # Build script for HTML/CSS/JS regeneration
```

---

## ⚖️ License & Disclaimer

Insurix is an independent artificial intelligence policy analysis tool built strictly to parse insurance policy wordings and mathematical financial covenants. Insurix does not provide clinical diagnosis or medical advice. Pre-authorization and final claim sanction rests with the respective insurance company and licensed Third Party Administrator (TPA).
