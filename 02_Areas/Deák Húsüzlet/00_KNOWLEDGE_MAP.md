---
title: 00_KNOWLEDGE_MAP
generated_by: librarian v0.3
generated_at: 2026-05-11T00:00:00
scope: 02_Areas/Deák Húsüzlet/
mode: index
file_count: 180
id: 07d66e6e-79e7-4d93-8c6f-fed865147856
index_schema_version: 1
---

# DH — Knowledge Map (tier-2)

> A Deák Húsüzlet unit belső domain-térképe. Csak ezen a unit-on belüli domaineket sorolja fel; cross-unit utalások a `00_GAPS.md`-ben.

## 1. Top-level domainek

```
DH (Deák Húsmíves Online Platform)
├── 1. Project Operations    → 01_PROJECT_STATE, TASKS, CLAUDE, memory/
├── 2. Business Development  → BMC, KPI, strategy, legal, savings-engine, market research
├── 3. Product Engineering   → design/, plugins/deak-design, app-flow, screen-catalog
├── 4. Product Catalog       → Products/ (46 termék MD + build pipeline)
├── 5. Marketing & Brand     → Marketing/Brand, Marketing/Kampány, sales
├── 6. Brainstorm Lab        → brainstorm/ (multi-AI think-engine state-fájlok + BDOS meta)
└── 7. Manual / User Doc     → manual/v0.2-hu, manual/v0.2-ro
```

---

## 2. Domain leírások

### 2.1 Project Operations
- **Források:** `01_PROJECT_STATE.md`, `TASKS.md`, `CLAUDE.md`, `memory/projects/dh.md`, `memory/projects/exarlabs-strategia.md`
- **Tartalom:** Sprint állapot, blokkolók, fókusz, project map, Jira sync. AI agent identity / fogalomtár / file-handling szabályok a `CLAUDE.md`-ben.
- **Forrás-rendszer:** Jira (DH projekt, exarlabs.atlassian.net) — ~153 ticket.
- **Friss állapot:** Sprint 3 ACTIVE — **70%** (7 Done / 2 IP / 1 To Do), scope 21→10 szűkítve.

### 2.2 Business Development

Sub-domainek:
- **BMC** — `pilot-husuzlet/BMC-v2.4.md` canonical (kétzónás "lokális ellátási platform"). `BMC-v2.2.md` (= v2.3 tartalmilag) megmaradt.
- **KPI Framework** — `pilot-husuzlet/KPI Framework - v1.3.md` (North Star: Second Order Rate 14d ≥40%).
- **Pilot specifikációk** — savings-engine/, rural-delivery/, product-variations/, founding50-spec-v1.0
- **Stratégia** — `strategy/` (Exar Labs 24-month roadmap, AI dev analysis, competitive advantage, sprint-ordering-review)
- **Legal** — `legal/` (contract-cadru v1.2 + 1 archív, comanda-nr1 v1.5 + 4 archív, ÁSZF HU/EN/RO, privacy HU/EN/RO)
- **Market research** — competitors_analysis, dhop-siker-otlettar-v4.0, marketplace-benchmarks
- **Retrospektívák** — `sprint-2-retrospective-2026-04-15.md`, `sprint-ordering-review-2026-04-11.md`
- **Meeting eredmények** — `deak-meeting-checklist-2026-04-15.md`, `deak-meeting-results-2026-04-15.md`
- **Release notes** — `v0.2-release-notes.md`
- **Company data** — `Business Development/company-data.md`

### 2.3 Product Engineering / Design
- **Design system** — `design/DESIGN.md`, `design/design-system.md` (#9B2335 primary, Inter + Playfair Display, Lucide ikonok)
- **Brand context** — `design/PRODUCT.md` (impeccable skill betölti)
- **App flow** — `design/app-flow-v0.3.md` (teljes funkcionalitás snapshot)
- **Screen catalog** — `design/screen-catalog/workflow.md` + Netlify deploy (https://deakhus.netlify.app)
- **Spec docs** — `butcher-courier-full-spec.md`, `screen-base-mapping.md`, `prompt-rural-screens.md`
- **Plugin** — `plugins/deak-design/` (design system + ui-audit + ui-strings + wireframe-v0.1 skill)

### 2.4 Product Catalog
- **Source of truth:** `Products/MASTER/products/*.md` (**46 termék** — `velos_csont.md` is benne van, GAPS v0.1 7.2 ↩ tisztázva)
- **Schema:** `_schema-v1.1.json` (Frappe-aligned + internal_code)
- **Build pipeline:** `Products/MASTER/scripts/build.py` → `Products/generated/products-vX.Y.json` → `design/screen-catalog/data/`
- **6 kategória:** sertés, csirke, füstölt, kolbász/szalámi, paté, csont/zsír
- **Meeting decisions:** `Products/meetings/2026-05-07_decisions.md` + `_internal-product-codes.md` + `_unified-product-master.md`
- **Workflow:** `Products/CLAUDE.md`, `Products/UPDATE-PROMPT.md`

### 2.5 Marketing & Brand
- **Brand v2.0** — `Marketing/Brand/`: brand_voice_v2.0, messaging_ervrendszer_v1.1, vizualis_identitas, brand_review_v2.0, message_library_v1.0, adalekanyag_kutatas
- **Adalékanyag-pozicionálás** — `Marketing/kutatas_ipari_hus_adalekanyagok.md` + `Brand/adalekanyag_kutatas.md` (lehet pár hely-duplikáció — lásd GAPS)
- **Kampány — Április 23** — `Marketing/Kampány - Április 23/` (6 brief)
- **Sales** — `Marketing/sales/` (messaging_ervrendszer + duplikátum)
- **Founding50 közlemény** — `Marketing/facebook-post-founding50-v1.md`

### 2.6 Brainstorm Lab (multi-AI think-engine)
19 állapot-fájl (ápr–máj 2026). Munkaminta: ChatGPT (Deák GPT) + Perplexity + Gemini + Claude (orchestrator). Az `_SYNTHESIS.md` lezárt szintézisek.

Fő témák:
- **Pricing/revenue share** (VALIDATED)
- **Pre-launch fears** + `_SYNTHESIS`
- **Marketing launch review** `_SYNTHESIS`
- **GTM kreatív ötletek** `_SYNTHESIS`
- **Frappe partnership** + `_SYNTHESIS`
- **Falusi házhozszállítás** (kétzónás BMC alapja)
- **Zóna detekció** (T-6 döntés)
- **BMC mega review** (BMC v2.4 alapja)
- **Feature prioritization** (alap + v2)
- **Brand voice v2** → Brand/brand_voice_v2.0.md
- **Founding 50** → founding50-spec-v1.0
- **DHOP válság-pozicionálás** + **Stratégiai áttekintés**
- **Retention loop decision**
- **Május 1 grill posztok** + `_SYNTHESIS`
- **Analytics privacy stack** + **Hetzner vs Firebase**
- **BDOS** (új, 2026-05-10) — BDOS = AI-native cognition system meta-keret. Itt él a Librarian és a tervezett 4-5 agent paletta.

### 2.7 Manual
`manual/v0.2-hu/` és `manual/v0.2-ro/` — v0.2 user manual screenshots (kép-content, MD nélkül a top-szinten).

---

## 3. Domain közi kapcsolatok

```
01_PROJECT_STATE ──canonical──> dev-roadmap-v2.0 ──implements──> Jira (DH-1..DH-157)
       │                            │
       │                            └──maps──> BMC-v2.4 (4-réteg L1-L4)
       │
       ├──tracks──> KPI Framework v1.3 ──instruments──> Firebase Analytics (analytics-dictionary-v2.2)
       │
       ├──policy──> CLAUDE.md ──governs──> design/screen-catalog (Netlify deploy)
       │                                     │
       │                                     └──build──> design/screen-catalog/data ←── Products/MASTER (build.py)
       │
       └──ops──> Marketing/Brand v2.0 ──drives──> Marketing/Kampány — Április 23 + Founding50

brainstorm/* ──synthesizes──> *_SYNTHESIS.md ──promoted──> BMC, KPI, Brand, dev-roadmap
                                                            (formal docs in Business Development/)

brainstorm_bdos.md ──defines──> Librarian agent ──maintains──> 00_INDEX, 00_KNOWLEDGE_MAP, 00_DECISIONS, 00_QUESTIONS, 00_GAPS

Legal Track:
contract-cadru-v1.2 + comanda-nr1-v1.5 ──ratifies──> revenue share (3% / 6.6% / 9.9%)
ÁSZF + privacy + cookie spec (DH-130/131/132/133/137) ──blocks──> beta launch
```

---

## 4. Aktív vs. archív rétegek

- **Active canonical:** `01_PROJECT_STATE.md` (kérdéses frissesség), `dev-roadmap-v2.0`, `BMC-v2.4`, `KPI Framework v1.3`, `velocity-tracker-v1.5`, `app-flow-v0.3`, `brand_voice_v2.0`, contract-cadru v1.2, comanda-nr1 v1.5
- **Superseded inline (megmaradt):** `BMC-v2.2.md` (= v2.3 tartalom), comanda iterációk v1.0–v1.4 (`legal/contract/archive/`), contract-cadru v1.0–v1.1 (`legal/contract/archive/`)
- **`**` prefix törlésre jelölt fájlok már fizikailag eltüntek** — lásd GAPS 3.1 (BIN/-be vagy törlésre kerültek a 2026-05-01 nagytakarításkor).
- **BIN/** (NEM olvasott): ~760 fájl 2026-05-01 nagytakarítás után.

---

## 5. Külső rendszerek (vault-on kívül, itt hivatkozva)

| Rendszer | URL | Mit ad |
|----------|-----|--------|
| Jira | exarlabs.atlassian.net (project DH) | ~153 ticket |
| Production | https://deakhus.ro | Élő webshop (2026-03-30 óta) |
| Staging | https://staging.deakhus.ro | Staging |
| Wireframe galéria | https://deakhus.netlify.app | Screen catalog deploy (build #64) |
| ChatGPT projekt | g-p-69cbee4a04c481918a2a738959b92361-deak | Deák custom GPT |
| Firebase | (project ID nincs explicit a vault-ban) | Analytics + UTM tracking |
| Google Drive | "Ideas Vault/02_Areas/Deák Húsüzlet" | Ez a vault FUSE mount |

Részletek: `CLAUDE.md` és `01_PROJECT_STATE.md`.
