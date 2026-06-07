---
title: "DH — Deák Húsmíves Online Platform"
date: 2026-04-16
author: Becze Szabolcs
status: active
description: "Online ordering and delivery system for Deák Húsmíves craft butcher shop in Székelyudvarhelyon, built with Vue 3 PWA frontend and Frappe backend, currently in Sprint 3 development with 145 total tickets and 11.7x AI velocity multiplier achieved."
description_source: auto
description_hash: b35bc19afff7cc28
id: 75283eb3-519c-4eed-ae8e-8c5c14742bdd
index_schema_version: 1
bdos_index: true
---
# DH — Deák Húsmíves Online Platform

## Összefoglaló
Online rendelési + házhozszállítási rendszer a Deák Húsmíves kézműves húsüzletnek Székelyudvarhelyen.

## Jira
- **Projekt:** DH (exarlabs.atlassian.net)
- **Board:** DH Board (id: 100)
- **Cloud ID:** af628aa2-6228-4043-8ae5-fedf77390217
- **Ticketek:** **145** (97 Done | 0 IP | 48 To Do) — frissítve **2026-04-15**

## Sprint-ek
| Sprint | ID | Állapot | Ticket# | Completion |
|--------|----|---------|---------|------------|
| Sprint 1.1 | 70 | CLOSED (2026-04-02) | ~66 | ✅ |
| **Sprint 2** | 34 | **LEZÁRVA** (ápr. 3 → ápr. 15, 13 nap) | **38** | **100% ✅** |
| **Sprint 3** | 67 | **ACTIVE** (indul 2026-04-16) | 18 + 10 epic | TBD |
| Sprint 4 | 68 | FUTURE | 0 | — |
| Sprint 5 | 69 | FUTURE | 0 | — |

## Kulcs URL-ek
- **Production:** https://deakhus.ro
- **Staging:** https://staging.deakhus.ro
- **Jira board:** https://exarlabs.atlassian.net/jira/software/c/projects/DH/boards/100
- **Wireframe galéria:** https://deakhus.netlify.app

## Tech stack
- Frontend: Vue 3 PWA (single app, dual view)
- Backend: Frappe Framework
- Analytics: Firebase Analytics ✅ LIVE (DH-104 Done, 2026-04-15)
- UTM/QR tracking: ✅ LIVE (DH-80, DH-109 Done)
- Hosting: Frappe Cloud

## Release terv
v0.1 (Done, ápr. 2) → **v0.2 (Done, ápr. 15)** → v0.3 Savings Engine (Sprint 3, indul ápr. 16) → 2 hét mgmt teszt → v0.4 (natív mobil) → v0.5 (online fizetés)

## Revenue Share — MEGÁLLAPODVA (2026-04-15)
- **Retail cost validálva:** 19,5% (konkrét boltok adatai alapján)
- **Phase 1 (Pilot):** Customer 3% / Platform 6,6% / Deák 9,9%
- **Phase 2 (Scale):** Platform ~7-9% (trigger: repeat >= 40%)
- **Phase 3 (Multi-product):** Platform ~9-12% (trigger: AOV + cross-sell)
- **Részletes:** `Business Development/pilot-husuzlet/deak-meeting-results-2026-04-15.md`
- **Brainstorm:** `brainstorm/brainstorm_deak-pricing-revenue-share.md`

## Velocity (mért adatok)
- **AI szorzó:** 11.7x (Sprint 2 mért, 2026-04-15)
- **Sprint 2 throughput:** 20.5 ticket/hét (38 ticket / 13 nap)
- **Projekt átlag:** 16.6 ticket/hét (97 ticket / 41 nap)
- **Költségmegtakarítás:** ~85% a tradicionális fejlesztéshez képest
- Részletes adatok: `Business Development/pilot-husuzlet/velocity-tracker-v1.2.md`

## Beta status
- **NEM AKTÍV** — Sprint 3 (v0.3 Savings Engine) után indul
- **Várható launch:** ~2026-05-15 (Sprint 3 végén)
- **Tracking infra KÉSZ:** Firebase Analytics + UTM/QR + KPI dashboard (DH-82)
- **Pilot célok (max 3 hónap):** ≥50 regisztráció + ≥20 visszatérő vásárló (14 napon belül újrarendel)
