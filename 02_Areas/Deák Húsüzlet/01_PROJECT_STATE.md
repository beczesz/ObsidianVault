---
title: 01_PROJECT_STATE
version: 1.6
date: 2026-04-17
author: Becze Szabolcs
description: Canonical project state snapshot for DH — primary AI entry point with current status, blockers, focus, and project map. Sprint 3 2. nap snapshot, DH-112 Done, velocity v1.3 frissítve.
id: e422e41c-01bd-4f17-9ed7-aa0cdaa7c802
index_schema_version: 1
---

## Objective

Launch the DH (Deák Húsmíves Online Platform) beta on ~2026-05-15 (v0.3 release után). Validate the online ordering + home delivery model for a local artisan butcher shop in Székelyudvarhely with 30 registrations, 15 orders, and 5 returning customers within 30 days.

## Current Status

- **Phase:** Sprint 3 ACTIVE (v0.3 Savings Engine + Legal + maradék v0.2 follow-up) — **Sprint 2 LEZÁRVA ✅ 100%**
- **Jira projekt:** DH (exarlabs.atlassian.net) — **145 ticket** — Sprint 3 2. nap (DH-1 → DH-145)
- **Sprint 3 valós scope (Jira openSprint 2026-04-17):** 19 feature/task + 2 Epic (DH-116 IP, DH-138 To Do)
- **Sprint 3 haladás:** **6 Done / 1 IP / 12 To Do** = 33% Done (+DH-112 guest checkout ápr. 17 15:23)
- **Beta status:** **NEM AKTÍV** — v0.3 release után indul (~2026-05-15)

### v0.2 "Látjuk az adatokat" ✅ KÉSZ
Teljes analytics stack telepítve (DH-43 → 44 → 80 → 104 → 109). Firebase Analytics + UTM/QR tracking live.

### Sprint 3 — Jira valós scope (2026-04-17)

**Done (6):** DH-38, DH-98, DH-103, DH-112, DH-117, DH-118
**In Progress (1):** DH-119 (+ DH-116 Epic 10 parent IP)
**To Do (12):** DH-120, DH-123, DH-129, DH-130, DH-131, DH-132, DH-133, DH-136, DH-137, DH-143, DH-145, DH-138 (Legal Epic parent)

> **FONTOS:** a `**sprint-3-prioritization-2026-04-15.md` MUST listájából 4 ticket (DH-51, DH-121, DH-122, DH-139) valójában **NINCS** a Sprint 3 Jira scope-ban. Ezek backlog-on maradtak. Elavult a doc. (Részletek: lásd `dev-roadmap-v2.0.md` — egyesített roadmap.)

### Dev progress

Minden v0.2 ticket Done. Running Savings Counter (Epic 10 első pillér) ✅ Done ápr. 17-ig — **AI velocity multiplier bizonyított újra**. Post-order Recap aktívan fut.

- Domain: deakhus.ro LIVE ✅ (2026-03-30); staging.deakhus.ro LIVE ✅
- Products: 37 termék, 5 kategória
- Ignis (KAN): Oktatási platform — külön projekt, párhuzamosan fut
- Exar Labs: 12 fős csapat, diverzifikáció zajlik
- Revenue share AGREED 2026-04-15: Customer 3% / Platform 6.6% / Deák 9.9%

## Key Metrics

| Metric | Target | Current |
|--------|--------|---------|
| Beta launch date | v0.3 után (~máj. 15) | **NEM aktív — Sprint 3 alatt fejlesztés** |
| Sprint 3 Done | 19 total | **6 Done (33%)** |
| Sprint 3 In Progress | — | **1** |
| Sprint 3 To Do | — | **12** 
| Pilot registrations (30d) | 30 | tracking ready, beta NEM indult |
| Pilot orders (30d) | 15 | tracking ready, beta NEM indult |
| Returning customers (30d) | 5 | tracking ready, beta NEM indult |
| Stop cap | 12-13k EUR | Not yet tracked |
| North Star: 2nd Order Rate (14d) | >=40% | tracking ready, beta NEM indult |

## Sprint 2 — LEZÁRVA ✅

Minden ticket Done (38/38, 100%, 14 nappal határidő előtt). Részletek: `Business Development/pilot-husuzlet/sprint-2-retrospective-2026-04-15.md`.

## Sprint 3 — ACTIVE scope (canonical, lásd dev-roadmap-v2.0)

**Savings Engine core (Epic 10 / DH-116 IP):**
- DH-117 Running Savings Counter BE ✅
- DH-118 Running Savings Counter FE ✅
- DH-119 Post-order Recap 🟡
- DH-120 Reorder Basket Loader + merge modal
- DH-123 Rendeléseim — Spórolás badge + újrarendelés
- DH-129 Savings Engine Firebase events (10 új event)

**Legal & Compliance (Epic DH-138):**
- DH-130 ÁSZF
- DH-131 Impresszum
- DH-132 GDPR consent checkbox
- DH-133 Jogi szolgáltató tisztázás
- DH-136 ANSVSA szállítási engedély
- DH-137 Cookie policy

**Mérés / Infra:**
- DH-145 Firebase + GDPR cookie banner spec (web + Capacitor)

**v0.2 maradék / UX:**
- DH-143 Vezérlőpult — Wireframe gyorslink

**Backlog (Sprint 3-ban NINCS, v0.4-be csúsztatandó vagy új ticketté):**
- DH-51 Szállítási zóna (10 km) — Legal/Ops, ideális esetben v0.3 beta előtt
- DH-121 Family Bundles vásárlói — v0.3.1 vagy v0.4
- DH-122 Family Bundles admin — v0.3.1 vagy v0.4
- DH-127 Familiar Favourites — **promoted MUST v0.4-be** (L3 Habit Engine)
- DH-128 Swap suggestion MVP — v0.5 vagy v0.6
- DH-139 Rendelésszám egyszerűsítés — QoL, v0.3.1
- DH-134 Privacy Policy (push+device) — **v0.4 mobil app blokkoló**
- DH-135 App Store developer account — **v0.4 mobil app blokkoló**

## Active Problems

1. ~~**Partnership agreement missing**~~ ✅ Revenue share megállapodva 2026-04-15: Customer 3% / Platform 6.6% / Deák 9.9%. Írásbeli formalizálás még hátravan.
2. **Financial data not received** — Napi forgalom, kosárérték, bruttó árrés boltonként. Sprint 3 közben érkezik.
3. **Legal minimum missing** — DH-130 → DH-133, DH-137, DH-145 → Sprint 3-ban; Szabolcsnál. Beta előtt MUST.
4. **ANSVSA szállítási engedély** — DH-136 Sprint 3-ban.
5. **Szállítási zóna (10 km) nincs Sprint 3-ban** — DH-51 Backlog, de beta előtt kell. **Új döntés: húzzuk be vagy toljuk v0.4-be?**
6. **v0.4 mobil app legal blokkolók** — DH-134 (Privacy Policy), DH-135 (App Store account) Backlog-ban. **Új ticket sorrend: v0.4 kickoff előtt.**

## Current Focus

> **Sprint 3 Savings Engine befejezés + Legal sub-track + v0.4 előkészítés.**

1. **DH-119 Post-order Recap** (IP) → zárás
2. **DH-120 Reorder Basket Loader** → start (Epic 10 záró pillér)
3. **DH-123 Spórolás badge** + **DH-129 Firebase events** → Epic 10 teljesítéshez
4. **Legal sub-track zárás:** DH-130, 131, 132, 133 (Szabolcsnál) — beta előtt MUST
5. **v0.4 ticketesítés előkészítése** — mobil app + push + mobile-first UX scope (lásd `dev-roadmap-v2.0.md`)
6. **DH-51 döntés** — Sprint 3-ba behúzni vagy v0.4-be?
7. Mid-sprint review: ápr. 30. → v0.3 release target májusi harmadik hét (~05-15)

## Constraints

- **Time:** Beta aktiválás ~2026-05-15 — pilot fázis (max 3 hónap)
- **Budget:** Stop cap ~12-13k EUR teljes kockázat (dev + ops + marketing)
- **Operations:** ~3,900 EUR/év üzemeltetés (Exar Labs viseli)
- **Payment:** Csak készpénz szállításkor (pilot fázis, online fizetés v0.6-ban)
- **Geography:** Székelyudvarhely + 10 km körzet
- **Team:** Bench fejlesztők az Exar Labs-ból, Máté Majoros aktív
- **Revenue share:** Customer 3% / Platform 6.6% / Deák 9.9% (agreed 2026-04-15)

## Pilot döntési logika (max 3 hónap)

- **Skálázás** (mindkettő teljesül): ≥50 regisztráció + ≥20 visszatérő vásárló (újrarendelés 14 napon belül)
- **Stop** (3 hónap után, max effort mellett sem teljesülnek): pilot lezárás, stop cap elérésekor
- A pilot **bármikor** véget érhet közös döntéssel

## Last Updated

2026-04-17 (v1.6 — Sprint 3 Jira valós scope szinkronizálva, elavult prioritizációs doc törlésre jelölve, egyesített dev-roadmap-v2.0.md kanonikus. Revenue share agreed, focus shift: Savings Engine zárás + v0.4 előkészítés.)

## Wireframes & Design

- **Wireframe galéria (Netlify):** https://deakhus.netlify.app
- **Netlify admin:** https://app.netlify.com/projects/deakhus
- **Lokális mappa:** `design/wireframes/`

## Project Map (canonical)

| Path | Description |
|------|-------------|
| `TASKS.md` | Full task inventory — Sprint 3 actual (Jira sync), Legal, Backlog (145 ticket) |
| `CLAUDE.md` | AI agent memory — people, glossary, project context, file handling rules |
| `01_PROJECT_STATE.md` | EZ A FÁJL — canonical snapshot |
| `Business Development/pilot-husuzlet/dev-roadmap-v2.0.md` | **Canonical unified roadmap** — Sprint 3 → v0.6, BMC 4-réteg mapping |
| `Business Development/strategy/24-month-roadmap.md` | Exar Labs 24 hónapos stratégiai roadmap |
| `Business Development/pilot-husuzlet/BMC-v2.2.md` | Business model — flywheel, revenue share, risk analysis |
| `Business Development/pilot-husuzlet/KPI Framework - v1.2.md` | Metrics & KPI Framework — pilot measurement system |
| `Business Development/pilot-husuzlet/velocity-tracker-v1.3.md` | AI vs. Traditional development velocity benchmark |
| `Business Development/pilot-husuzlet/legal.md` | Jogi követelmények és teendők (v1.1) |
| `Business Development/pilot-husuzlet/sprint-2-retrospective-2026-04-15.md` | Sprint 2 retrospektív (38/38, 14 nap előrébb) |
| `design/wireframes/README.md` | Wireframe workflow leírás + Netlify link |
| `design/wireframes/index.html` | Wireframe galéria (Netlify főoldal) |
| `design/design-system.md` | Design system — színek, fontok, spacing |
| `Marketing/brand_voice.md` | Brand voice & messaging guide |

## Elavult dokumentumok — törlésre jelölve

Az alábbi fájlok prefixe `**` (törlés előtt). Az egyesített `dev-roadmap-v2.0.md` kiváltja őket:

- `**dev-roadmap-v1.5.md` (Business Development/pilot-husuzlet/)
- `**sprint-5-6-review-2026-04-11.md` (Business Development/strategy/)
- `**sprint-3-prioritization-2026-04-15.md` (Business Development/pilot-husuzlet/)
- `**v0.4-v0.6-roadmap-plan.md` (Business Development/pilot-husuzlet/savings-engine/)
- `**velocity-tracker-v1.2.md` (Business Development/pilot-husuzlet/)
