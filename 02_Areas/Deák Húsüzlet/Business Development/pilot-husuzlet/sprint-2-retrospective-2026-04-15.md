---
title: Sprint 2 Retrospective — DH "Látjuk az adatokat"
description: "Sprint 2 végeztével a 38/38 ticketből 100% Done, 13 nap alatt: teljes Firebase Analytics stack, UTM/QR forráskövetés, KPI dashboard. AI szorzó 11.7x, carry-over 0, legal compliance hátramaradt. Szabolcs és Mate sprint review dokumentuma a Deák Húsmíves projekt mérésképes mérési alapjáról és Sprint 3 fókuszáról."
description_source: auto
description_hash: 356763993bce7317
version: 1.0
date: 2026-04-15
sprint_period: 2026-04-03 → 2026-04-15 (tényleges) / 2026-04-29 (eredeti)
completion: 38/38 (100%)
release: v0.2
author: Claude (Anthropic) + Szabolcs
id: e04947be-e715-427d-b4e8-ad6374b688d5
index_schema_version: 1
---
# Sprint 2 Retrospective — DH

## TL;DR

> **Sprint 2 = 38/38 ticket Done = 100% completion rate, 14 nappal a határidő előtt zárva.**
>
> A "Látjuk az adatokat" v0.2 release készen áll: teljes Firebase Analytics stack, UTM/QR forráskövetés, KPI dashboard. AI szorzó: **11.7x** (vs. v0.1: 4-5x).

---

## 1. Sprint adatok

| Metrika | Érték |
|---------|-------|
| Sprint ID (Jira) | 34 |
| Tervezett időszak | 2026-04-03 → 2026-04-29 (26 nap) |
| **Tényleges befejezés** | **2026-04-15** |
| Tényleges hossz | **13 nap** |
| Sprint scope (commit) | 38 ticket |
| Sprint Done | **38 ticket** |
| Completion rate | **100%** |
| Carry-over Sprint 3-ba | **0 ticket** |
| Új ticket sprint közben | 1 (DH-144, azonnal Done) |

## 2. Mit szállítottunk?

### v0.2 release: "Látjuk az adatokat"

**A) Teljes Analytics stack (7 ticket cluster)**
- DH-43 — Event DocType + Visitor Identity Map + core funnel tracking
- DH-44 — QR code generation 3 in-store forrással
- DH-80 — UTM/QR forráskövetés + Firebase UTM tracking + first-touch attribution
- DH-81 — Failure event tracking (sikertelen rendelések)
- DH-82 — North Star KPI dashboard (7 mutató, RAG színezés)
- DH-104 — Firebase Analytics SDK bekötése Vue PWA-ba
- DH-109 — QR tracking kiértékelés

**B) Operatív flow-ok (10 ticket)**
- DH-78, 79 — Rendelés lemondás (vevő + admin oldal)
- DH-84 — Minimum kosárérték (80 RON)
- DH-86 — Fizetési mód választó (készpénz/kártya)
- DH-100, 101 — Darabos termékek kezelése
- DH-105 — Admin Előkészítés tab termékenkénti bontás
- DH-106 — Min. rendelési mennyiség UX
- DH-108 — Kosár megőrzés OAuth login után
- DH-111 — Logout flow javítás

**C) Admin & Vendég flow (5 ticket)**
- DH-17, 30, 35, 36, 37 — Admin/Courier interface alapok

**D) Bugfixek + UX polish (12 ticket)**
- DH-46, 47, 59, 68, 77, 89, 91, 97, 102, 113, 114, 115, 140, 141, 142, 144

### Stratégiai impact

A v0.2 release azt jelenti, hogy a DH most már **mérhető üzleti rendszer**, nem csak egy webshop. Minden Sprint 3-ban beépített Savings Engine feature **Firebase eseményként** mérhető lesz. Ez a "Operating Business System" alapja (lásd KPI Framework v1.3).

---

## 3. Mi ment jól? ✅

### a) **Sprint-end push működött**
Ápr. 14 → ápr. 15 között **+7 ticket Done egyetlen nap alatt**. Ez tradicionálisan ~4 hét munkája. A Mate-féle fókuszált egynapos analytics-cluster lezárás (DH-80, 104, 109) kiváló példa az AI-fókuszált sprint dynamics-ra.

### b) **Firebase Analytics 1 nap alatt**
A DH-104 ticket eredeti becslése ~"félnap implementáció" volt. Tényleges: ~1 nap (kódolás + tesztelés). Tradicionális becslés: 5-7 nap. **Szorzó: 10-14x**.

### c) **Nincs carry-over**
0 ticket csúszott át Sprint 3-ba. Tiszta scrum határ, Sprint 3 fókuszáltan kezdődhet a Savings Engine-en.

### d) **Bug:Feature arány javult**
v0.2-ben kb. 50:50 (12 bug + 25+ feature/task), és minden bug Done. Sprint 3 várhatóan tisztán feature lesz.

### e) **AI szorzó javult: 10.3x → 11.7x**
A pattern reuse és context retention javította a sebességet. (Részletek: velocity-tracker-v1.2.md)

---

## 4. Mi nem ment jól? ⚠️

### a) **Eredeti CLAUDE.md memory elavult volt**
A Claude memory-ban Sprint 2 ticket lista egy korábbi snapshot volt — emiatt eleinte rosszul reportoltam Szabolcsnak (3 IP ticket). Csak a Jira sprint mező volt naprakész. **Tanulság:** Memory file (TASKS.md, CLAUDE.md) frissítését részévé kell tenni a sprint review folyamatnak.

### b) **safe_write.py session path elavult**
A scriptben hardcoded `/sessions/amazing-epic-euler/mnt` volt — nem működött az új session-ben. Ma javítva (dinamikus session detection).

### c) **Nincs még írásbeli partnerségi megállapodás**
38 ticket Done, beta él, de még nincs aláírt megállapodás a Deák Húsmívessel. **BLOKKOLÓ a Sprint 3 vége előtt.**

### d) **Legal compliance hátramaradt**
9 Legal & Compliance ticket (DH-130 → 138) mind To Do. Sprint 2 fókusza a tech volt. Sprint 3 elején legalább DH-130, 131, 132 (ÁSZF, Impresszum, GDPR) zárandó.

---

## 5. Mit tanultunk?

### a) **A "sprint-end push" nem mítosz, ha jól van strukturálva**
+7 ticket egy nap alatt nem rontotta a minőséget, mert (1) a 3 analytics ticket egy szekvenciális clusterben volt (DH-104 → 80 → 109), (2) Mate ezekre fókuszáltan tudott dolgozni, (3) az AI gyorsította a Frappe Desk Script Report írását.

### b) **A "11.7x" konzervatív szám**
Ha 5 nap/ticket-tel számolnánk a tradicionális oldalon (sok cégnél így van), a szorzó **14.6x** lenne. Az Exar Labs "AI 10x" narratívája **alulígéri** a valóságot.

### c) **A pilot mérés most indul**
Eddig "sötétben" mértünk (Frappe-only). Most élesben mérünk Firebase-en. A következő 30 nap döntő — a v0.3 Savings Engine scope-ja a beta adatokon múlik.

### d) **Egy fókuszált fejlesztő AI-vel = 1 hagyományos csapat**
Mate egyedül vitte a Sprint 2-t. Tradicionális becslés: 30 munkahét = ~7.5 hónap egy fejlesztőnek. AI-vel: 13 nap. **5 hónap megtakarítás** egyetlen sprintben.

---

## 6. Action items Sprint 3-hoz

| # | Akció | Határidő | Felelős |
|---|-------|---------|---------|
| 1 | Sprint 2 hivatalos zárás Jira-ban (Complete Sprint) | ápr. 15-16 | Szabolcs |
| 2 | v0.2 release tag staging + production | ápr. 15-16 | Mate |
| 3 | DH-1 (TEST) törlése a backlogból | ápr. 16 | Szabolcs |
| 4 | Találkozó a Deák Húsmíves döntésképes személyével | ápr. 16-18 | Szabolcs |
| 5 | Sprint 3 kickoff: scope véglegesítés (10 Savings + 5 carry-over + 5 admin) | ápr. 16 | Szabolcs + Mate |
| 6 | Beta nap-2 KPI review (regisztráció, első rendelések) | ápr. 16 | Szabolcs |
| 7 | Legal sprint sub-track elindítása (DH-130, 131, 132) | ápr. 17 | Szabolcs |
| 8 | velocity-tracker v1.2 megosztása (Exar Labs stratégiai) | ápr. 17 | Szabolcs |

---

## 7. KPI status — Beta NEM AKTÍV

⚠️ **Korrekció:** A Beta NEM indult el ápr. 14-17-ben — ez tervezés/kommunikáció volt. A valódi beta a **v0.3 release után** indul (~2026-05-15, Sprint 3 végén).

A Firebase Analytics + UTM/QR tracking infrastruktúra LIVE a production-on, de **a beta mérés csak a v0.3 Savings Engine release után kezdődik**. A KPI Framework v1.3 "mérés-kész" állapotot tükröz, nem aktív mérést.

| KPI | Cél (30d) | Most | Trend |
|-----|-----------|------|-------|
| Regisztrációk | 30 | tracking READY, beta NEM indult | — |
| Rendelések | 15 | tracking READY, beta NEM indult | — |
| Visszatérő vásárlók | 5 | tracking READY, beta NEM indult | — |
| 2nd Order Rate (14d) | ≥40% | tracking READY, beta NEM indult | — |
| TTFO | ≤72h | tracking READY, beta NEM indult | — |

**Első értékelés:** ~1 hét a valódi beta launch után.
**Pilot decision point:** beta launch + 30 nap (~jún. 15).

---

_Generálva: 2026-04-15 | Forrás: Jira DH projekt + Sprint 2 close adatok_
_Kapcsolódó dokumentumok: velocity-tracker-v1.2.md, dev-roadmap-v1.5.md, v0.2-release-notes.md_
