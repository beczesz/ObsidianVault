---
title: BDOS TODO — Pending Operational Tasks
date: 2026-05-24
author: Becze Szabolcs
status: active
version: 1.0
description: Pending feladatok lista, amelyek user-action-t vagy időkeretet igényelnek. Frissül minden session végén.
tags: [BDOS, todo, pending]
id: 96dcf91e-1857-4287-9d2e-a307e692c3ae
index_schema_version: 1
---

# BDOS Pending Tasks

> Minden user-action-t vagy testing-et igénylő feladat egyetlen helyen.
> Sessionönként frissítjük.

---

## 🔴 P0 — User action szükséges

### Sage smoke test
**Mit kell tenni:** felhasználó beilleszti a mockolt referenciát a Referencia chatbe (lásd `agents/sage/REFERENCE_FORMAT.md` §smoke test), aztán futtatunk `/sage-harvest`-et.

**Miért most:** validálja a teljes Phase 1 stack-et — Chrome MCP integráció, markdown-state írás, Sage dashboard kitelése.

**Várt eredmény:** 1 új thought-note + 1 atomic-proposal + `state/last_run.md` update + journal append + dashboard auto-fill.

**Blokkolja:** Sage scheduling (lokális launchd), Phase 2.B family rollout (akkor érdemes, ha tudjuk Sage működik).

---

## 🟠 P1 — Smoke test után

### Sage local scheduling (macOS launchd)
**Mit kell tenni:** **Plist fájlok megírva** — `00_Prompts/BDOS/agents/sage/scheduling/` alatt.
**User action: 3 parancs futtatása** (cp + launchctl load) — lásd a setup README-t ugyanott.

**Schedule:** daily 06:00 Europe/Bucharest (`/sage-harvest`) + hétfő 06:05 (`/sage-curate`).

### ~~Maestro observe smoke test~~ ✅ KÉSZ (2026-05-24)
End-to-end Phase 2.A validáció lefutott valós log-adattal. 6/6 agent logolva, Presto 1 op-entry (Strategic Prep Phase 1), version logok mind a 6 agent-re (Phase 2.B rollout). Parsing tiszta, no errors. Az `observe` mód működik.

---

## 🟡 P2 — Phase 2 folytatása

### ~~Phase 2.B — Family rollout~~ ✅ KÉSZ (2026-05-24)
6 agent log-rollout, 18 új log fájl, 14 fájl szerkesztve. Verzió-bumpok: Lib v0.6, Maestro v0.4, Curator v0.3, Sage v0.3, Presto v0.4, Broker v0.2.

### Phase 2.C — Token capture
**Mit kell tenni:** dönteni a token-capture mechanizmusról (harness-extrakció subagent `<usage>` blokkokból vs self-report estimate). Implementálni a kiválasztott mechanizmust. Update `LOG_SCHEMAS.md` (jelenleg `tokens: null` — fel kell tölteni).

**Feltétel:** Phase 2.B kész.

---

## 🟢 P3 — Háttér munka, párhuzamos

### ~~Per-agent detail dashboardok~~ ✅ KÉSZ (2026-05-24)
Sage ✅, Maestro ✅, Presto ✅, Librarian ✅, Curator ✅, Broker ✅. **15 dashboard összesen** a `_dashboards/` családban. Launcher v0.7.3. Minden agent-graph node él (zero coming-soon overlay).

**Curator build-eli őket egyenként** (`/dash-build`). Sage és Maestro Observatory a reference implementations.

### ~~Broker v0.2 capability design~~ ✅ KÉSZ (2026-05-24)
9 mód kidolgozva (7 operational + 2 cognition: learn/reflect). 12 slash command létrehozva. Sales-learnings folder skeleton. Presto-integráció dokumentálva (sibling distribution agents).

**Még pending:** `_dashboards/00_SALES_INDEX.md` (a `brk-index` mód generálja amikor először fut), `SalesEngine.md` template (per-Area, amikor első sales-munka konkretizálódik).

### Detail dashboardok és Broker párhuzamosan mehetnek

---

## ⚪ Halasztott / opcionális

- Per-agent meta-learning loop kiterjesztése (Sage-mintára) — Presto, Broker, esetleg Maestro saját szabályaira
- Cross-vault retrieval optimization (Librarian tier-2 bővítés új Area-kra)
- Curator design-system audit a Phase 2 dashboardok után (Sage + Maestro Observatory hozzáadta-e új patterneket?)

---

## Update szabály

- **Új P0/P1 task** érkezésekor: hozzáadás itt + említés a session-output-ban
- **Task elvégezve:** áthúzás (`~~Task title~~`) + dátum + 1-mondatos eredmény-jegyzet
- **Heti review:** törölni a 30+ napja "ott ülő" tételeket vagy átszámozni — élő dokumentum, nem temető
