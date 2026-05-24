---
title: 00_GAPS
generated_by: librarian v0.3
generated_at: 2026-05-11T00:00:00
scope: 02_Areas/Deák Húsüzlet/
mode: index
file_count: 180
id: 435a4b95-40a8-401c-8a77-527123b63a60
index_schema_version: 1
---

# DH — Gaps & Inconsistencies (tier-2)

> Itt jelzem (NEM oldom meg) a duplikációkat, ellentmondásokat, elavulás-gyanús fájlokat, broken-linkeket és cross-unit utalásokat. v0.3 futás: v0.1-ben (2026-05-10) flag-elt items reconcile-olva — minden tétel mellett `[status]` jelzés.

**Status legend:**
- `[STANDING]` — v0.1 óta változatlan, még él
- `[NEW]` — v0.3-ban újként detektálva
- `[RESOLVED]` — v0.1 óta rendezve
- `[STALE-FRESH]` — v0.1-ben flag-elt elavult, de a forrás-fájl azóta nem frissült (még mindig stale)

---

## 1. DUPLIKÁCIÓ-GYANÚ

### 1.1 `legal.md` két helyen `[STANDING]`
- `Business Development/legal/legal.md`
- `Business Development/pilot-husuzlet/legal.md`
- Eltérés: cégnevezéktan (régi `Exar Labs SRL` vs. új `EXARGROUPS S.R.L.`). A pilot-husuzlet/legal.md v1.2 (2026-04-20) frontmatter.
- Javaslat: egyik canonical kijelölése. Még él.

### 1.2 `messaging_ervrendszer_v1.1.md` két helyen `[STANDING]`
- `Marketing/Brand/messaging_ervrendszer_v1.1.md`
- `Marketing/sales/messaging_ervrendszer_v1.1.md`
- Plusz `Marketing/sales/messaging_ervrendszer.md` (verzió nélküli régebbi).

### 1.3 BMC verziók — fájlnév vs. tartalom `[STANDING]`
- `BMC-v2.2.md` (fájlnév szerint v2.2, de a frontmatter szerint **valójában v2.3**)
- `BMC-v2.4.md` canonical (2026-05-03)

### 1.4 Brand voice — hivatkozott v0.1 nem található `[STANDING]`
- `brainstorm/brainstorm_brand-voice-v2.md:46` hivatkozik: `Marketing/brand_voice.md (v0.1)` — NEM létezik.

### 1.5 Adalékanyag-kutatás két helyen `[STANDING]`
- `Marketing/Brand/adalekanyag_kutatas.md`
- `Marketing/kutatas_ipari_hus_adalekanyagok.md`
- Lehet előd/utód kapcsolat — érdemes ellenőrizni.

---

## 2. INKONZISZTENCIÁK (különböző fájlok mást mondanak)

### 2.1 Sprint 3 állapot — több verzió él egyszerre `[STALE-FRESH]`
- `01_PROJECT_STATE.md:18` (v1.6, **2026-04-17, 24 napja nem frissült**): "6 Done / 1 IP / 12 To Do = 33%"
- `CLAUDE.md:137` (2026-04-22): "7 Done / 2 IP / 1 To Do = 70%, scope szűkült 21→10"
- `TASKS.md:2` (2026-04-22): "7 Done / 2 IP / 1 To Do (70%)"
- `dev-roadmap-v2.0.md` (2026-04-17): "5 Done / 1 IP / 13 To Do (26%)"
- `memory/projects/dh.md:14` (2026-04-15): "97 Done / 0 IP / 48 To Do"
- **Helyzet:** `CLAUDE.md`/`TASKS.md` (2026-04-22) a legfrissebb. `01_PROJECT_STATE.md` v1.7 bumpra megérett — **az 01_PROJECT_STATE engine dolga, NEM a Librarian-é**.

### 2.2 Jira ticket szám `[STANDING]`
- `01_PROJECT_STATE.md`: 145 ticket
- `CLAUDE.md:133`: 153 ticket (DH-1 → DH-157)
- `TASKS.md:2`: 153 ticket (DH-1 → DH-146)
- `memory/projects/dh.md`: 145 ticket
- Sync-dátum különbség. Konsensus: ~153 ticket.

### 2.3 Sprint 3 prioritization MUST lista vs. Jira `[STANDING]`
- `01_PROJECT_STATE.md:30` jelzi: 4 ticket (DH-51, DH-121, DH-122, DH-139) nincs a Sprint 3 Jira scope-ban. A hivatkozott `**sprint-3-prioritization-2026-04-15.md` fájl már nincs a vault-ban (lásd 3.1).

### 2.4 KPI Framework verzió a project-mapben `[STANDING]`
- `01_PROJECT_STATE.md:151`: `KPI Framework - v1.2.md`
- Valójában: `KPI Framework - v1.3.md`

### 2.5 Velocity Tracker verzió a project-mapben `[STANDING]`
- `01_PROJECT_STATE.md:152`: `velocity-tracker-v1.3.md`
- Valójában: `velocity-tracker-v1.5.md`

### 2.6 BMC link a project-mapben `[STANDING]`
- `01_PROJECT_STATE.md:150`: `BMC-v2.2.md`
- Canonical: `BMC-v2.4.md`

### 2.7 legal.md verzió a project-mapben `[STANDING]`
- `01_PROJECT_STATE.md`: "v1.1 — 2026-04-05"
- A fájl frontmatter szerint: v1.2 — 2026-04-20

### 2.8 Brand voice link a project-mapben `[STANDING]`
- `01_PROJECT_STATE.md:158`: `Marketing/brand_voice.md` — NEM létezik.
- Canonical: `Marketing/Brand/brand_voice_v2.0.md`.

### 2.9 Wireframes link a project-mapben `[STANDING]`
- `01_PROJECT_STATE.md:155`: `design/wireframes/README.md` — NEM létezik közvetlenül.
- Csak `design/README.md` + `design/wireframes/archive/b70-final/`.

### 2.10 CLAUDE.md vs. memory: platformdíj 6,8% vs. 6,6% `[STANDING]`
- `CLAUDE.md:108`: 6,8% (Comanda nr.1 v1.3 alapján)
- `memory/projects/dh.md:37`, `deak-meeting-results-2026-04-15.md`: 6,6%
- 0,2 pp eltérés. Contract-cadru v1.2 + Comanda v1.5 ténylegesen használt száma ellenőrzendő.

### 2.11 Beta status `[STANDING]` (konzisztens)
- `01_PROJECT_STATE.md:18` és `CLAUDE.md` egyaránt: "Beta NEM AKTÍV — v0.3 release után". ✅

---

## 3. ELAVULT FÁJLOK / TÖRLÉSRE JELÖLT FÁJLOK

### 3.1 `**` prefix-szel megjelölt elavult fájlok — fizikailag nem találhatók `[STALE-FRESH]`
A `01_PROJECT_STATE.md:160` szekciója szerint `**` prefix-szel jelölt fájlok:
- `**dev-roadmap-v1.5.md`
- `**sprint-5-6-review-2026-04-11.md`
- `**sprint-3-prioritization-2026-04-15.md`
- `**v0.4-v0.6-roadmap-plan.md`
- `**velocity-tracker-v1.2.md`

Egyik fájl sem található a vault-ban — valószínűleg már a 2026-05-01 nagytakarításkor BIN/-be kerültek. **Az `01_PROJECT_STATE.md` "Elavult dokumentumok" szekció ürítése az engine dolga, NEM a Librarian.**

### 3.2 BMC v2.2 (= v2.3) elavult? `[STANDING]`
- `BMC-v2.4.md` frontmatter `predecessor: BMC-v2.2.md (v2.3, 2026-04-04)`
- A 2.2/2.3 fájl még a fájlrendszerben. Archiválandó? Szabolcs döntése.

### 3.3 Sprint 3 prioritization cross-reference `[STANDING]`
- A `v0.3-release-plan.md` stb. még hivatkozzák — a hivatkozott fájl eltűnt.

---

## 4. BROKEN / GYANÚS LINKEK

### 4.1 `01_PROJECT_STATE.md` projekt map sok elavult linkje `[STALE-FRESH]`
- Lásd 2.4–2.9.

### 4.2 `CLAUDE.md` "v0.3 Wireframes v3" — fájl-referencia hiányzik `[STANDING]`
- `CLAUDE.md:438`. Valószínűleg Netlify deploy.

### 4.3 `CLAUDE.md` `Marketing/brand_voice.md` és `velocity-tracker-v1.1.md` `[STANDING]`
- Mindkettő hibás. Canonical: `Marketing/Brand/brand_voice_v2.0.md`, `velocity-tracker-v1.5.md`.

### 4.4 `01_PROJECT_STATE.md` "Sprint 2 retrospective" link ✅ `[RESOLVED-by-existence]`
- Helyesen mutat (`Business Development/pilot-husuzlet/sprint-2-retrospective-2026-04-15.md` létezik).

### 4.5 Brainstorm kontextus-referenciák `[STANDING]`
- `brainstorm/brainstorm_dhop-valsag-pozicionalas.md` és `brainstorm_brand-voice-v2.md` BMC-v2.2.md-re utal — már elavult.
- `brainstorm_brand-voice-v2.md:45-46` `Marketing/brand_voice.md` — broken.

---

## 5. ÁRVA FÁJLOK (heurisztika — nem teljes link-graph)

- `Business Development/legal/contract/archive/comanda-nr1-phase1-v1.0..v1.4.md` (5 db, szándékos archív, NEM árva)
- `Business Development/legal/contract/archive/contract-cadru-exar-deak-v1.0..v1.1.md` (szándékos archív)
- `Products/legacy/product_listing_v0.7_hu.md`, `_ro.md` — legacy referencia
- `manual/v0.2-hu/`, `manual/v0.2-ro/` — top-szinten nincs `.md`, csak screenshot mappák
- `Business Development/strategy/Features/` — üres almappa (`[STANDING]`, lásd 7.6)
- `Marketing/Brand/message_library_v1.0.md` — új vs v0.1, hivatkozottság ellenőrizendő `[NEW]`

A vault-szintű link-graph nem futott; v0.4 release után automatizálható.

---

## 6. CROSS-UNIT UTALÁSOK (scope-on kívülre)

- `memory/projects/exarlabs-strategia.md` — Exar Labs egész cég stratégiai memóriája (átnyúlik DH-n túlra)
- `memory/projects/ignis.md` — Ignis Learning Platform (KAN Jira, külön projekt)
- `brainstorm/brainstorm_frappe-partnership-strategy.md` + `_SYNTHESIS.md` — nagyrészt Frappe/Exar
- `brainstorm/brainstorm_dhop-valsag-pozicionalas.md`, `brainstorm_strategiai-attekintes-v1.md`
- `Business Development/strategy/24-month-roadmap.md` — Exar Labs egész stratégia
- `brainstorm/brainstorm_bdos.md` `[NEW]` — BDOS meta-szintű (Vault Librarian + agent paletta) — cross-unit relevancia van (Librarian globális vault szerep)

**Ajánlás (Szabolcs döntés):** vagy hagyni mindezt itt, vagy a tisztán cross-cutting fájlokat `02_Areas/Exar Labs/` unit alá mozgatni.

---

## 7. ÉSZREVÉTELEK / ANOMÁLIÁK

### 7.1 `BMC-v2.2.md` fájlnév vs. v2.3 tartalom `[STANDING]` — lásd 1.3

### 7.2 `Products/MASTER/products/` — 46 vs. 47 termék MD `[RESOLVED]`
v0.3 ellenőrzés: **46 .md fájl** a mappában (`velos_csont.md` is ezek között). A v0.1-ben jelzett 47 db miscount volt. ✅

### 7.3 `Products/UPDATE-PROMPT.md` `[STANDING]`
Prompt-jellegű fájl, nem doc. Lehetne `00_Prompts/`-ban — szándékosan domain-közelben tartva.

### 7.4 `design/screen-catalog/screens/` `[STANDING]`
HTML fájlok (NEM markdown). A `workflow.md` az egyetlen MD itt.

### 7.5 Lokalizációs duplikáció `[STANDING]`
- ÁSZF HU/EN/RO, Privacy HU/EN/RO — szándékos.
- `Brand/messaging_ervrendszer` + `sales/messaging_ervrendszer` — NEM lokalizációs, hely-duplikáció (lásd 1.2).

### 7.6 `Business Development/strategy/Features/` üres mappa `[STANDING]`
A mappa megjelenik, MD fájl nincs benne.

### 7.7 `00_DECISIONS_INDEX.md` lefedettség `[STANDING]`
Brainstorm "Decisions Made" szekciók részletesebbek a forrás-fájlban.

### 7.8 `brainstorm_bdos.md` meta-státusza `[NEW]`
Új fájl (2026-05-10) — meta-szintű (a BDOS agent system definíciója, NEM DH-specifikus business content). Megfontolandó:
- itt hagyni (BDOS-t DH-n validáljuk) ✅ jelenleg
- vagy felmozgatni globális scope-ra (`00_Prompts/BDOS/agents/` mellé)

---

## 8. LIBRARIAN ACTIONS TAKEN (v0.3 futás)

**SEMMI rendrakási akció.** A Sprint 3 aktív állapotában a Librarian (v0.2 anti-pattern szerint) szigorúan csak olvasott és re-indexelt:
- Nem mozgatott árva fájlt
- Nem javított broken-linkeket
- Nem törölt duplikátumot
- v0.3 only: re-generated 5 index file, entry-point/working-artifact distinction bevezetve, `[STATUS]` jelzés a GAPS items mellé

**v0.1 → v0.3 reconcile eredmény:**
- 1 RESOLVED (7.2 termék-szám 46 vs. 47 — 46 ✅)
- 1 NEW item (`brainstorm_bdos.md` + cross-unit relevancia)
- A többi v0.1 finding STANDING (`01_PROJECT_STATE.md` engine nem futott, így a project-map link-jei + Sprint 3 állapot mismatch továbbra is él)

**Jövőbeli rendrakásra javasolt feladatok (csak jelzés):**
1. `01_PROJECT_STATE.md` → v1.7 frissítés (link-fixek, KPI/velocity/BMC verziók, Sprint 3 70%, "Elavult dokumentumok" szekció ürítése).
2. `BMC-v2.2.md` → vagy átnevezni `BMC-v2.3.md`-re vagy archiválni.
3. Két `legal.md` közül egy canonical kijelölése.
4. Két `messaging_ervrendszer_v1.1.md` közül a canonical kijelölése.
5. `CLAUDE.md` `velocity-tracker-v1.1.md` és `Marketing/brand_voice.md` referenciák frissítése.
6. `brainstorm_bdos.md` helyének tisztázása (DH-vágott vs. globális meta).

**Mindezt NEM a Librarian feladata** — csak jelzem.
