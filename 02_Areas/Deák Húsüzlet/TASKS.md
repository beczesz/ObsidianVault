---
title: "TASKS.md — DH Feladatlista"
date: 2026-04-22
author: Becze Szabolcs
status: active
description: "A Deák Húsmíves projekt Jira feladatlistájának magyar és angol nyelvű nyomvantartása, amely Sprint 2 lezárásáról (v0.2), Sprint 3 aktív statuszáról (70% kész) és scope-módosításokról tájékoztat fejlesztőket és product managementot."
description_source: auto
description_hash: 4b1b4b19b2007606
id: 168975a9-132f-4366-98ee-d2a4838bf7a7
index_schema_version: 1
bdos_index: true
---
# TASKS.md — DH Feladatlista
> Utolsó Jira sync: **2026-04-22** | **153 ticket** összesen (DH-1 → DH-146) | **Sprint 2 LEZÁRVA ✅** (38/38 = 100%) | **Sprint 3 ACTIVE** — **7 Done / 2 IP / 1 To Do** (70%)

---

## 🎉 Sprint 2 — LEZÁRVA ✅ (38 Done / 0 IP / 0 ToDo)

**Sprint időszak:** ápr. 3 – ápr. 29 (hivatalosan) | **Tényleges befejezés:** 2026-04-15 (14 nap előrébb)
**Release:** v0.2 "Látjuk az adatokat" — teljes analytics stack kész
**Retrospektív:** `Business Development/pilot-husuzlet/sprint-2-retrospective-2026-04-15.md`

### Sprint 2 — mind Done (38 ticket)

| Ticket | Típus | Leírás |
|--------|-------|--------|
| DH-17 | Task | Product availability toggle (admin) |
| DH-30 | Task | Courier login |
| DH-35 | Task | Admin login |
| DH-36 | Task | Orders dashboard (admin) |
| DH-37 | Task | Order detail & status management (admin) |
| DH-43 | Task | Analytics foundation: Event DocType + Visitor Identity Map + core funnel tracking |
| DH-44 | Task | QR code generation for in-store placement |
| DH-46 | Task | Product popularity score — sort order for catalog listing |
| DH-47 | Task | Notification banner — első kampány: ingyenes kiszállítás áprilisban |
| DH-59 | Task | Mészáros – termék elérhetőség toggle |
| DH-68 | Story | Nézet váltó – Admin nézet elérése a Contul meu oldalon |
| DH-77 | Task | Google OAuth: App name konzisztencia — „Deák Húsmíves" egységesen |
| DH-78 | Task | Rendelés lemondás funkció — vevő és Deák oldalon |
| DH-79 | Task | Rendelés lemondása és visszaállítása – cancel flow |
| DH-80 | Task | UTM/QR forráskövetés: 3 egyedi QR kód + Firebase UTM tracking |
| DH-81 | Task | Failure event tracking: sikertelen rendelések nyomon követése |
| DH-82 | Task | North Star KPI dashboard: 7 mutatós Frappe Desk Script Report |
| DH-84 | Task | Minimum kosárérték – 80 RON alatt nem lehet rendelést leadni |
| DH-86 | Task | Fizetési mód választó – készpénz vagy kártya kiszállításkor |
| DH-89 | Bug | Regisztráció után a form kitöltve marad és „Success" felirat |
| DH-91 | Bug | Email küldő neve „Frappe" – expected: Deák Húsmíves |
| DH-97 | Story | „Înapoi la cumpărături" gomb – termékdetail oldalon |
| DH-100 | Task | Termék JSON frissítés – darabos termékek kihagyása |
| DH-101 | Task | Darabszámra történő vásárlás támogatása |
| DH-102 | Task | Admin statisztika – rendelések megnyithatók legyenek |
| DH-104 | Task | Firebase Analytics SDK bekötése a Vue PWA-ba |
| DH-105 | Bug | Admin Előkészítés tab – termékenkénti bontás |
| DH-106 | Task | Minimum rendelési mennyiség UX + darabos termékek súly-tájékoztató |
| DH-108 | Bug | Kosár tartalma elveszik Google OAuth regisztráció után |
| DH-109 | Task | QR tracking kiértékelés — kasszás regisztrációs forráskövetés |
| DH-111 | Task | Kijelentkezés után zsákutca – login oldal navigáció nélkül |
| DH-113 | Bug | Admin kártyákon order creation date vs delivery date |
| DH-114 | Bug | „Kiszállítva" → „Lezárva" automatikus státuszváltás |
| DH-115 | Bug | Kiszállítás jelölése popup megerősítéssel |
| DH-140 | Story | Vendég checkout flow javítása |
| DH-141 | Bug | Betűtípus inkonzisztencia — header serif vs body sans-serif |
| DH-142 | Bug | Fiókom oldal — Bejelentkezés gomb új design rendszer |
| DH-144 | Task | Display more orders on preparation screen |

---

## Sprint 3 — ACTIVE (Jira sync 2026-04-22) — szűkített scope

**10 ticket (1 Epic)** — **7 Done / 2 IP / 1 To Do = 70%**

> ⚠️ **Scope változás (ápr. 17 → ápr. 22):** A sprint 21 ticketről 10-re szűkült. A Legal & Compliance blokk (DH-130–138), analytics (DH-129, DH-145), UX (DH-123, DH-143) kikerültek a sprintből — backlogba visszakerültek.

### ✅ Done (7)

| Ticket | Típus | Leírás |
|--------|-------|--------|
| DH-38 | Task | Customer list (admin) |
| DH-98 | Story | „Înapoi la cumpărături" gomb — Coșul meu oldalon |
| DH-103 | Task | Rendelés keresése szám alapján mobilon |
| DH-112 | Story | **Regisztráció nélküli rendelés (guest checkout)** ✅ ÚJ DONE |
| DH-117 | Story | **Running Savings Counter — Backend** (Epic 10) |
| DH-118 | Story | **Running Savings Counter — Frontend progress bar + nudge** (Epic 10) |
| DH-119 | Story | **Post-order Recap** — Megtakarítás összegző + visszacsalogatás (Epic 10) ✅ ÚJ DONE |

### 🟡 In Progress (1 + 1 Epic)

| Ticket | Típus | Leírás |
|--------|-------|--------|
| DH-116 | Epic | **Epic 10 — v0.3 Savings Engine** (IP) |
| DH-120 | Story | **Reorder Basket Loader + merge modal** (Epic 10 záró pillér) 🔄 ÚJ IP |

### 📋 To Do (1)

| Ticket | Típus | Leírás |
|--------|-------|--------|
| DH-121 | Story | **Family Bundles — Vásárlói nézet** (grid + detail) — sprintbe húzva |

---

## 🔴 Sprintből kikerült ticketek (backlogba visszakerültek, ápr. 22-i Jira sync)

> Ezek a ticketek az ápr. 17-i TASKS.md-ben Sprint 3-ban voltak, de a Jira-ban már NINCSENEK a sprintben.

**Savings Engine / Analytics:**

| Ticket | Típus | Leírás | Javasolt target |
|--------|-------|--------|----------------|
| DH-123 | Story | Rendeléseim — Spórolás badge + újrarendelés | Sprint 3 visszahúzás? |
| DH-129 | Story | Savings Engine Firebase eventek — 10 új event | Beta előtt MUST |

**Legal & Compliance (Epic DH-138):**

| Ticket | Típus | Leírás | Javasolt target |
|--------|-------|--------|----------------|
| DH-138 | Epic | Epic — Legal & Compliance | Beta előtt MUST |
| DH-130 | Task | ÁSZF draft készítése | Beta előtt MUST |
| DH-131 | Task | Impresszum oldal létrehozása | Beta előtt MUST |
| DH-132 | Task | GDPR consent checkbox | Beta előtt MUST |
| DH-133 | Task | Jogi szolgáltató tisztázása (BLOCKER) | Beta előtt MUST |
| DH-136 | Task | DH szállítási engedély (ANSVSA) | Beta előtt MUST |
| DH-137 | Task | Cookie policy ellenőrzés | Beta előtt MUST |

**Infra / UX:**

| Ticket | Típus | Leírás | Javasolt target |
|--------|-------|--------|----------------|
| DH-145 | Task | Firebase + GDPR cookie banner spec | Beta előtt MUST |
| DH-143 | Story | Vezérlőpult — Wireframe gyorslink | Nice to have |

---

## Döntések (2026-04-22)

**DH-51 — Szállítási zóna korlátozás (Székelyudvarhely + 10 km)** → **Sprint 5** (Szabolcs döntése)

---

## Backlog — Founding 50 Program (DH-150, Beta launch feature)

| Ticket | Típus | Leírás | Effort |
|--------|-------|--------|--------|
| DH-150 | Task | **[v0.3 Beta] Founding 50 Program** — parent ticket, teljes spec | Epic-szerű |
| DH-151 | Task | Backend: Campaign DocType + User mezők + delivery fee override | M |
| DH-152 | Task | Backend: Inaktivitási scheduler (30 napos retention filter) | S |
| DH-153 | Story | Frontend: Kampány modal (counter + CTA + megjelenési logika) | M |
| DH-154 | Story | Frontend: Gratuláció modal + Alapító tag badge + checkout override UI | S |
| DH-155 | Story | Frontend: Betelt állapot UI + waitlist regisztráció | S |
| DH-156 | Task | Analytics: Firebase events (8 új event) | S |
| DH-157 | Task | QR kódok + UTM kampány linkek generálása | XS |

**Spec:** `Business Development/pilot-husuzlet/founding50-spec-v1.0.md`
**Brainstorm:** `brainstorm/brainstorm_founding50.md`

---

## Backlog — v0.4 mobile blokkolók (pre-v0.4 kickoff MUST)

**Ezek a ticketek NINCSENEK Sprint 3-ban, de a v0.4 mobil app indítását blokkolják:**

| Ticket | Típus | Leírás | Target |
|--------|-------|--------|--------|
| DH-134 | Task | Privacy Policy frissítés (push + device) | v0.4 pre-kickoff |
| DH-135 | Task | App Store developer account + compliance | v0.4 pre-kickoff |

---

## Backlog — v0.3.1 (post-beta bug fix + QoL)

| Ticket | Típus | Leírás |
|--------|-------|--------|
| DH-139 | Task | Rendelésszám egyszerűsítése (QoL) |
| DH-122 | Story | Family Bundles — Admin CRUD |

---

## Backlog — v0.4 target (Habit Engine előkészítés)

| Ticket | Típus | Leírás | BMC Layer |
|--------|-------|--------|-----------|
| DH-127 | Story | **„Szokásos rendelésem" gomb — Familiar Favourites** (promoted MUST v0.4) | L3 Habit Engine |

---

## Backlog — v0.5+ target

| Ticket | Típus | Leírás |
|--------|-------|--------|
| DH-51 | Task | Szállítási zóna korlátozás (Székelyudvarhely + 10 km) |
| DH-128 | Story | Swap suggestion MVP — „Cseréld erre, X lejt spórolsz" |
| DH-150 | Task | **Első 100 teszter kampány megtervezése** (placeholder) |
| DH-48 | Task | Térkép alapú cím-validáció és futár térkép nézet |
| DH-49 | Task | Auto SMS értesítés kiszállítási státuszhoz |
| DH-50 | Task | Best route kalkulátor futárnak |
| DH-146 | Story | NEW-11: Kedvenc Termékek — Csillag toggle + lista rendezés |

---

## Backlog — Email (v0.6+, push notification priority over email)

| Ticket | Típus | Leírás |
|--------|-------|--------|
| DH-124 | Story | TTFO Engine — Email drip |
| DH-125 | Story | Post-delivery reorder trigger |
| DH-126 | Story | Savings recap email |

---

## Backlog — Egyéb / Inactive

| Ticket | Típus | Leírás |
|--------|-------|--------|
| DH-1 | Task | TEST – Workflow teszt (törlendő) |
| DH-39 | Task | Product management (admin) — low priority |
| DH-45 | Task | Facebook page CTA & launch post — v0.3 beta indítás |
| DH-83 | Task | „Miért rendeltél?" post-order mikro prompt |
| DH-96 | Story | Több szállítási cím kezelése |

---

## Epics (összesen 11)

| Ticket | Leírás | Státusz |
|--------|--------|---------|
| DH-2 | Epic 1 – Authentication & User Onboarding | Done components |
| DH-3 | Epic 2 – Product Catalog | Done components |
| DH-4 | Epic 3 – Cart & Checkout | Done components |
| DH-5 | Epic 4 – Order Status & Lifecycle | Done components |
| DH-6 | Epic 5 – Courier Interface | Done components |
| DH-7 | Epic 6 – Super Admin Interface | Done components |
| DH-8 | Epic 7 – Infrastructure & Launch Prep | Done components |
| DH-53 | Epic 8 – Admin nézet (Pregătire és Livrare) | Done |
| DH-110 | Epic 9 – UX & Lokalizáció | Done |
| **DH-116** | **Epic 10 – v0.3 Savings Engine** | **IP** |
| **DH-138** | **Epic — Legal & Compliance** | **Backlog (sprintből kikerült)** |

---

## Összesítés (2026-04-22)

### Sprint 3 bontás (Jira élő adat)

| Státusz | Ticket# |
|---------|---------|
| Done | **7** (DH-38, 98, 103, 112, 117, 118, 119) |
| In Progress | **1 + 1 Epic** (DH-120 + DH-116) |
| To Do | **1** (DH-121) |
| **Összesen** | **9 + 1 Epic** (70% Done) |

### Projekt szintű státusz

| Kategória | Ticket# |
|-----------|---------|
| Sprint 2 (LEZÁRVA) — Done | 38 |
| Sprint 3 — Done | 7 |
| Sprint 3 — In Progress | 2 |
| Sprint 3 — To Do | 1 |
| Sprintből kikerült (beta előtt MUST) | 11 |
| v0.4 mobile blockers (Backlog) | 2 |
| v0.3.1 Backlog | 2 |
| v0.4 Habit Backlog | 1 |
| v0.5+ Backlog | 5 |
| Email Backlog (v0.6+) | 3 |
| Egyéb Backlog | 5 |
| Epics | 11 |
| **ÖSSZESEN** | **153** |

---

## Kanonikus dokumentumok

- `01_PROJECT_STATE.md` v1.5 — állapot snapshot
- `Business Development/pilot-husuzlet/dev-roadmap-v2.0.md` — **egyesített roadmap (canonical)**
- `Business Development/pilot-husuzlet/BMC-v2.2.md` — business model
- `Business Development/pilot-husuzlet/legal.md` — jogi teendők
- `Business Development/pilot-husuzlet/sprint-2-retrospective-2026-04-15.md` — Sprint 2 retro

## Elavult dokumentumok (`**` prefix, törölhető)

- `**dev-roadmap-v1.5.md`
- `**sprint-5-6-review-2026-04-11.md`
- `**sprint-3-prioritization-2026-04-15.md`
- `**v0.4-v0.6-roadmap-plan.md`

---

## Sprint 3 zárási kritériumok (v0.3 release) — FRISSÍTVE 2026-04-22

1. ✅ DH-112 guest checkout Done
2. ✅ DH-119 Post-order Recap Done
3. 🟡 DH-120 Reorder Basket Loader — In Progress
4. ⬜ DH-121 Family Bundles — To Do
5. ⬜ Epic 10 (DH-116) lezárása: DH-120, 121 Done után
6. ⬜ **Sprintből kikerült MUST ticketek** döntés: visszahúzás vagy külön sprint?
7. ⬜ v0.3 release tag (~2026-05-15)
8. ⬜ Beta aktiválás: első 30 user meghívása
9. ⬜ v0.4 ticketesítés megtörténik (mobile app + push + mobile-first UX)
