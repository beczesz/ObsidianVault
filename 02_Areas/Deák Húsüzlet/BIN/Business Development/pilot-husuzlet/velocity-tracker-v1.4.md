---
title: "DH Velocity Tracker — AI vs. Tradicionális Fejlesztés"
version: 1.4
date: 2026-04-17
author: Claude (Anthropic) + Szabolcs
description: >
  Valós idejű mérés: mennyire gyorsabb az AI-alapú fejlesztés
  a tradicionális szoftverfejlesztéshez képest. Sprint 2 LEZÁRVA + Sprint 3 partial snapshot (2. nap).
  **v1.4 update:** Story Pointok LIVE Jira-ban (18/20 = 90% coverage) + felelősségi kör tisztázás (Deák ANSVSA engedélye él, Exar = order management only).
supersedes: velocity-tracker-v1.3.md
id: b4a36b31-6231-4dcf-92b5-4872c2794b49
index_schema_version: 1
---

# DH Velocity Tracker v1.4 — Sprint 3 snapshot + SP rögzítés + felelősségi kör

## 🆕 v1.4 KÜLÖNBSÉGEK (v1.3-hoz képest)

| Terület | v1.3 (2026-04-17 reggel) | **v1.4 (2026-04-17 délután)** |
|---------|---------------------------|-------------------------------|
| Story Point lefedettség | 0/20 (0%) ❌ | **18/20 (90%) ✅ JIRA-BAN RÖGZÍTVE** (2 Epic nélkül) |
| DH-136 ANSVSA státusz | blocker (ismeretlen átfutás) | **ELHÁRÍTVA** — Deáknál megvan az engedély |
| DH-133 jogi szolgáltató | open decision | **Marketplace modell megerősítve** (Exar=tech/order mgmt, Deák=seller/delivery) |
| Sprint 3 kockázati profil | 2 hatósági + 1 jogi blocker | **1 csak jogi blocker (DH-133)** — mérhetően csökkent |

---

## I. ÖSSZEFOGLALÓ — A nagy szám

| Mutató | v1.1 (ápr. 3) | v1.2 (ápr. 15) | v1.3 (ápr. 17 AM) | **v1.4 (ápr. 17 PM)** |
|--------|---------------|-----------------|-------------------|------------------------|
| **AI szorzó (mért, kumulatív)** | 10.3x | 11.7x | 11.7x (stabil) | **11.7x (stabil)** |
| Szabolcs becslése | 10x | 10x | 10x ✅ | 10x ✅ MEGERŐSÍTVE 3. alkalommal |
| Tradicionális sebesség | 4 nap/ticket | 4 nap/ticket | 4 nap/ticket | 4 nap/ticket |
| AI tényleges sebesség | 0.40 nap/ticket | 0.34 nap/ticket | 0.34 nap/ticket | **0.34 nap/ticket** |
| Teljes projekt throughput (átlag) | 18.6 ticket/hét | 16.6 ticket/hét | ~17 ticket/hét (43 nap) | **~17 ticket/hét** (43 nap) |
| Sprint-szintű throughput | — | 20.5 ticket/hét (Sprint 2) | ~21 ticket/hét (Sprint 3 kezdés) | **~21 ticket/hét** (Sprint 3 2. nap) |

> **Mérföldkő:** 43 nap alatt 103 ticket Done (Sprint 1.1 + Sprint 2 + Sprint 3 kezdés). Hagyományos csapat (2-3 fő): ~5-6 hónap.

---

## II. PROJEKT IDŐVONAL — változatlan

| Mérföldkő | Dátum | Nap# |
|-----------|-------|------|
| Projekt indulás (első ticket) | 2026-03-05 | 0 |
| Első hét zárás (19 ticket) | 2026-03-22 | 17 |
| Második hét zárás (25 ticket) | 2026-03-29 | 24 |
| Harmadik hét zárás (22 ticket) | 2026-04-02 | 27 |
| Negyedik hét (DH migráció + Sprint 2 start) | 2026-04-03 | 29 |
| v0.2 Beta TÉNYLEGES | 2026-04-15 | 41 ✅ |
| Sprint 3 indulás | 2026-04-16 | 42 |
| **Ma (v1.4 snapshot)** | **2026-04-17 PM** | **43** |
| Sprint 3 várható zárás (AI) | ~2026-04-28 – 05-05 | ~54-61 |
| v0.3 Beta target (eredeti) | ~2026-05-15 | ~71 |
| v0.3 Beta target (extrapolált) | **~2026-05-05** | **~61** (10 nappal korábbi) |

---

## III. HETI VELOCITY BREAKDOWN — változatlan

| Hét | Dátum | Lezárt ticketek | Kumulatív | Sprint |
|-----|-------|-----------------|-----------|--------|
| 1-2 | márc. 5-15 | 0 | 0 | (setup + tervezés) |
| 3 | márc. 16-22 | 19 | 19 | Sprint 1.1 |
| 4 | márc. 23-29 | 25 | 44 | Sprint 1.1 |
| 5 | márc. 30 – ápr. 2 | 22 | 66 | Sprint 1.1 (close) |
| 6 | ápr. 3-9 | 6 | 72 | Sprint 2 (DH migráció + indulás) |
| 7 | ápr. 10-14 | 19 | 91 | Sprint 2 |
| 8 | ápr. 15 (1 nap!) | +7 | 97 | Sprint 2 (close) |
| **9** | **ápr. 16-17 (2 nap)** | **+6** | **103** | **Sprint 3 (start)** |

> **🚀 Sprint 3 start velocity:** 6 ticket Done / 2 nap = **3.0 ticket/nap** — meghaladja a Sprint 2 átlagát (2.9/nap).

---

## IV. SPRINT 3 — RÉSZLETES SNAPSHOT (2. nap, 2026-04-17)

### Sprint 3 scope: 18 feature/task + 2 Epic

| Státusz | Ticket# |
|---------|---------|
| ✅ Done | **6** |
| 🟡 In Progress | **1 + 1 Epic** |
| 📋 To Do | **11 + 1 Epic** |
| **Összesen** | **18 + 2 Epic = 20 item** |

### Sprint 3 Done (6 ticket / 2 nap)

| Ticket | Summary | Resolved (UTC+3) | SP |
|--------|---------|------------------|----|
| DH-98 | „Înapoi la cumpărături" — Coșul meu | 2026-04-16 09:19 | 1 |
| DH-117 | Running Savings Counter — Backend | 2026-04-17 09:01 | 3 |
| DH-118 | Running Savings Counter — Frontend | 2026-04-17 09:01 | 3 |
| DH-103 | Rendelés keresése szám alapján mobilon | 2026-04-17 11:09 | 2 |
| DH-38 | Customer list (admin) | 2026-04-17 12:46 | 2 |
| DH-112 | Guest checkout | 2026-04-17 15:23 | 3 |
| **Össz** | | | **14 SP** |

### Sprint 3 In Progress (1 + 1 Epic)

| Ticket | Summary | SP |
|--------|---------|-----|
| DH-116 | **Epic 10 — v0.3 Savings Engine** (parent) | — (Epic) |
| DH-119 | Post-order Recap — Megtakarítás összegző | 5 |

### Sprint 3 To Do (11 + 1 Epic)

**Savings Engine core (Epic 10):**

| Ticket | Summary | SP |
|--------|---------|-----|
| DH-120 | Reorder Basket Loader + merge modal | 5 |
| DH-123 | Rendeléseim — Spórolás badge + újrarendelés | 3 |
| DH-129 | Savings Engine Firebase eventek (10) | 3 |

**Legal & Compliance (Epic DH-138):**

| Ticket | Summary | SP | 🆕 Felelősségi kör |
|--------|---------|-----|---------------------|
| DH-138 | Epic — Legal & Compliance (parent) | — (Epic) | Exar + Deák közösen |
| DH-130 | ÁSZF draft | 2 | **Exar (platform T&C) + Deák (seller T&C)** |
| DH-131 | Impresszum | 1 | **Mindkettő** — marketplace model |
| DH-132 | GDPR consent checkbox | 1 | Exar (tech) |
| DH-133 | Jogi szolgáltató tisztázás | 2 | **Szabolcs döntése** → marketplace modell javasolt |
| DH-136 | ANSVSA szállítási engedély | 1 | ✅ **DEÁKNÁL MEGVAN** — csak visszaigazolás Exar felé |
| DH-137 | Cookie policy | 1 | Exar (tech) |

**Mérés / Infra:**

| Ticket | Summary | SP |
|--------|---------|-----|
| DH-145 | Firebase+GDPR cookie banner spec | 3 |

**UX:**

| Ticket | Summary | SP |
|--------|---------|-----|
| DH-143 | Vezérlőpult — Wireframe gyorslink | 1 |

---

## V. ✅ BECSLÉSI ÁLLAPOT — 90%-os lefedettség (v1.4 frissítés)

### Sprint 3 ticketek becslési lefedettsége

| Mutató | v1.3 (reggel) | **v1.4 (délután)** |
|--------|---------------|---------------------|
| Sprint 3 ticket (total) | 20 | 20 |
| **Story Point** (customfield_10016) | **0/20 (0%)** ❌ | **18/20 (90%)** ✅ |
| Time estimate (timeoriginalestimate) | 0/20 (0%) | 0/20 (0%) |
| **Becslési lefedettség** | **0%** ❌ | **90%** ✅ |
| Nem becsült (Epic) | — | 2 (DH-116, DH-138) — Epic parent, nem számoljuk |

> **Story Points rögzítve Jira-ban:** 2026-04-17 ~15:31 (parallel editJiraIssue).
> Innentől a velocity mérés **nem csak ticket-szám alapon** tud menni, hanem valós SP/nap mérés lehetséges.

### Rögzített Story Point értékek (Fibonacci 1-2-3-5-8)

**Savings Engine (Epic 10):**

| Ticket | SP | Státusz |
|--------|-----|----------|
| DH-117 | 3 | ✅ Done |
| DH-118 | 3 | ✅ Done |
| DH-119 | 5 | 🟡 In Progress |
| DH-120 | 5 | 📋 To Do |
| DH-123 | 3 | 📋 To Do |
| DH-129 | 3 | 📋 To Do |
| **Epic 10 össz** | **22 SP** | **6 Done + 5 IP + 11 ToDo** |

**Legal & Compliance (Epic DH-138):**

| Ticket | SP | Státusz |
|--------|-----|----------|
| DH-130 | 2 | 📋 To Do |
| DH-131 | 1 | 📋 To Do |
| DH-132 | 1 | 📋 To Do |
| DH-133 | 2 | 📋 To Do |
| DH-136 | 1 | 📋 To Do (technikailag Done = Deák confirm) |
| DH-137 | 1 | 📋 To Do |
| **Legal össz** | **8 SP** | **mind To Do** |

**Mérés + UX:**

| Ticket | SP | Státusz |
|--------|-----|----------|
| DH-143 | 1 | 📋 To Do |
| DH-145 | 3 | 📋 To Do |
| **Egyéb össz** | **4 SP** | **mind To Do** |

**Korábbi carry-over:**

| Ticket | SP | Státusz |
|--------|-----|----------|
| DH-38 | 2 | ✅ Done |
| DH-98 | 1 | ✅ Done |
| DH-103 | 2 | ✅ Done |
| DH-112 | 3 | ✅ Done |
| **Carry-over össz** | **8 SP** | **mind Done** |

### Sprint 3 össz becslés (Jira-ban rögzítve)

| Kategória | Ticket | SP |
|-----------|--------|-----|
| ✅ Done | 6 | **14 SP** |
| 🟡 In Progress | 1 | **5 SP** |
| 📋 To Do | 11 | **23 SP** |
| **Sprint 3 total** | **18** | **42 SP** |
| Epic (nem számolt) | 2 (DH-116, 138) | — |

**Sprint 3 progress:**
- Ticket alapon: **6/18 = 33% Done**
- SP alapon: **14/42 = 33% Done** — egybecseng

---

## VI. 🆕 FELELŐSSÉGI KÖR TISZTÁZÁS (2026-04-17 PM)

### Szabolcs döntése: Marketplace modell megerősítve

**Exar Labs SRL (platform/tech):**
- Online rendelési platform üzemeltetése
- Order management + checkout flow
- User account + data processor (GDPR Art. 28)
- Cookie + consent infrastructure
- Firebase analytics + Firestore adatok
- Platform T&C + Cookie Policy kibocsátója

**Deák Húsmíves (seller/fulfillment):**
- Termékek seller-ként (jogilag eladó)
- Fizikai árukezelés + HACCP compliance
- **Szállítás (DH-136 ANSVSA engedély → Deáké)**
- Számlázás (jogilag a vásárlóval)
- ANSVSA élelmiszerbiztonság
- Seller T&C kibocsátója

### Ticket-szintű hatások

| Ticket | Korábbi értelmezés | 🆕 Új értelmezés |
|--------|-------------------|------------------|
| **DH-133** (Jogi szolgáltató) | Nyitott (3 opció: Exar / Deák / Both) | **Both — marketplace modell** → Exar Platform T&C-t ír, Deák Seller T&C-t ír. 1 közös impresszum oldal 2 entitással. |
| **DH-136** (ANSVSA engedély) | **Blocker** — engedélyeztetés kellhet | **Nem blocker** — Deáknál megvan. Exar felé csak **egyszeri visszaigazolás + másolat** kell. |
| **DH-130** (ÁSZF draft) | 1 dokumentum | **2 layer:** Platform T&C (Exar) + Seller T&C (Deák) — logikailag 1 ÁSZF 2 szekcióval is működhet |
| **DH-131** (Impresszum) | 1 entitás | **2 entitás 1 oldalon** — Exar (platform üzemeltető) + Deák (seller) |
| **DH-132** (GDPR checkbox) | 1 Controller | **2 Controller** (vagy 1 Controller + 1 Processor) — Szabolcs + jogász döntése |
| **DH-137** (Cookie policy) | 1 entitás | 1 entitás — **Exar** (csak a platform cookie-it kezeli) |

### Hatás a Sprint 3 velocity-re

| Tétel | Hatás |
|-------|-------|
| DH-136 de facto kész → csak confirm | **-1 SP effective** (1 SP munka kiesik, csak email Deáknak) |
| DH-133 irány tiszta → kevesebb research | **-0.5 SP effective** (döntés gyorsabb) |
| DH-130, 131 kicsit összetettebb (2 entitás) | +0.5-1 SP (de SP-értékek maradhatnak) |
| **Net hatás:** | **~1-1.5 SP gyorsabb Legal track** |

---

## VII. SPRINT 3 EXTRAPOLÁCIÓ — frissítve (v1.4)

### Feltételezések (frissítve)

- Sprint 2 cycle time: 2.9 ticket/nap
- Sprint 3 eddig (2 nap): 3.0 ticket/nap
- Hátralévő munka: **12 ticket (11 To Do + 1 IP) + 1 Epic (DH-138)**
- **DH-136 technikailag Done** (csak admin confirm) → **11 valós dev/legal ticket**
- DH-133 irány tiszta (marketplace) → gyorsabb feloldás

### Forgatókönyvek (változatlanok, de stabilabbak)

| Scenario | Ticket/nap | Hátralévő napok | Várható zárás | v0.3 beta target |
|----------|-----------|-----------------|---------------|------------------|
| **Optimista** (3.0/nap) | 3.0 | 4 munkanap | 2026-04-23 | máj. 15 előtt 22 nap |
| **Reális** (2.0/nap) | 2.0 | 6 munkanap | 2026-04-29 | máj. 15 előtt 16 nap |
| **Konzervatív** (1.5/nap) | 1.5 | 8 munkanap | 2026-05-05 | máj. 15 előtt 10 nap |

> **Konklúzió (v1.4):** A DH-136 elhárításával a kockázati profil csökkent. Legal track csak DH-133-on áll vagy bukik — ez viszont **Szabolcs + jogász ~1 hét** átfutás kérdése, nem dev blocker.

### Bottleneck újraértékelés

| Rank | Ticket | Miért bottleneck? | Státusz |
|------|--------|--------------------|---------|
| 1 | **DH-133** | Jogász beszélgetés + szerződésminták | Szabolcs hatáskörben |
| 2 | **DH-120** | Legkomplexebb dev ticket (merge modal state) | Dev queue |
| 3 | **DH-119** | Új UX flow + BE integráció | IP (ma induló) |
| ~~4~~ | ~~DH-136~~ | ~~ANSVSA átfutás~~ | ✅ **ELHÁRÍTVA (Deáknál megvan)** |

---

## VIII. CYCLE TIME ELEMZÉS — változatlan

| Mutató | Sprint 1.1 | Sprint 2 | **Sprint 3 (2. nap)** |
|--------|-----------|----------|------------------------|
| Sprint hossz | ~25 nap | 13 nap | 2 nap eddig |
| Ticketek Done | ~40 | 38 | **6** |
| Velocity (ticket/nap) | 1.6 | 2.9 | **3.0** |
| Velocity (ticket/hét) | 11.2 | 20.5 | **21** (extrapolált) |
| AI szorzó (sprint-szint) | ~10x | 11.7x | **TBD** (Sprint 3 végén) |

---

## IX. RELEASE VELOCITY — tényleges vs. becslés

### v0.3 — Sprint 3 (20 item = 18 ticket + 2 Epic)

| Módszer | Becslés | Tényleges |
|---------|---------|-----------|
| Tradicionális (4 nap/ticket, 1 dev) | 72 nap = 14.4 munkahét | — |
| AI becslés (11.7x trend) | ~6-7 dev-nap = ~1.3 munkahét | TBD |
| Claude optimista | ~2 hét | TBD (~4-6 nap eddig) |
| Szabolcs target | ~4 hét (máj. 15) | 2 nap = **33% Done (SP)** |

### SP alapú — valós mérés Jira-ból (NEW v1.4)

| Sprint | Total SP | Days | SP/day |
|--------|----------|------|--------|
| **Sprint 3 eddig** | **14/42** | 2 | **7.0 SP/day** |
| Sprint 3 extrapolált (11.7x) | 42 | ~6 | 7.0 SP/day |
| Tradicionális (1 dev) | 42 | ~70 | 0.6 SP/day |

> **Mostantól ez már Jira-ból re-fetchelhető** — nem Claude extrapoláció.

---

## X. KÖLTSÉG HATÁS — változatlan

| Mutató | Tradicionális | AI-alapú | Megtakarítás |
|--------|--------------|----------|-------------|
| Dev idő (v0.1) | ~640 óra (2 dev × 16 hét) | ~160 óra | 75% |
| Dev idő (v0.2) | ~1216 óra (1 dev × 30 hét) | ~104 óra (1 dev × 13 nap) | 91% |
| **Dev idő (v0.3 extrapolált)** | **~576 óra (1 dev × 14.4 hét)** | **~48 óra (1 dev × 6 nap)** | **92%** |
| Dev költség v0.2 (€25/óra) | €30,400 | €2,600 | €27,800 |
| Dev költség v0.3 extrapolált (€25/óra) | €14,400 | €1,200 | €13,200 |
| Teljes DH kockázat (eddig) | ~€60-65k | **~€7-8k** | **~88%** |

---

## XI. AJÁNLOTT AKCIÓK — frissítve (v1.4)

### ✅ Azonnal (ma) — elvégzett

1. ✅ **Story Pointok hozzáadva a Jira ticketekhez** (18 ticket, Fibonacci 1-2-3-5-8, customfield_10016) — **DONE 2026-04-17 ~15:31**
2. ✅ **DH-133 irány tiszta** — marketplace modell javaslat megerősítve (Exar=platform, Deák=seller)
3. ✅ **DH-136 elhárítva** — Deáknál megvan az ANSVSA engedély, csak confirm kell

### 🟡 Még ma / holnap

4. ⬜ **DH-136 transition Done + komment** — "Deáknál megvan az engedély, visszaigazolás Szabolcs felé megtörtént. Exar oldalon nincs teendő."
5. ⬜ **DH-133 komment** — "Marketplace modell: Exar=tech/order management (Platform T&C), Deák=seller+delivery (Seller T&C + ANSVSA). Jogász dönt 2 entitás vs 1 entitás + kiegészítés közt."
6. ⬜ **DH-130, 131 refinement** — 2 entitás tükrözése copy-ban

### Sprint 3 közben

7. ⬜ Mid-sprint review: ápr. 25 (sprint közepe)
8. ⬜ Legal track párhuzamosítás: DH-130, 131, 132, 137 együtt, nem egymás után (copywriting batch)
9. ⬜ DH-138 Epic transition "In Progress" amikor az első Legal ticket elindul

### Sprint 3 zárásakor

10. ⬜ v1.5 velocity tracker — 2. teljes Sprint-szintű AI szorzó mérés (most már valós SP-alapon)
11. ⬜ BMC v2.2 → v2.3 frissítés (L1-L4 réteg validáció)

---

## XII. ÉRTEKKETLEN: MI LETT MÉRT ELŐSZÖR

v1.4-től kezdve a következő adatok **valósak, nem becsültek**:

| Adat | Forrás | Update frekvencia |
|------|--------|--------------------|
| Story Points per ticket | Jira customfield_10016 | Valós idejű |
| Sprint 3 SP breakdown | Jira JQL `sprint in openSprints()` | Valós idejű |
| SP/nap velocity | Jira Done + resolved date | Minden Done-nál |
| Epic parent structure | Jira issueLinks | Valós idejű |

Korábban Claude extrapolációra támaszkodott a velocity, most **re-fetch-elhető metrika** lett.

---

_Generálva: 2026-04-17 PM | Forrás: Jira DH projekt + openSprint snapshot + SP rögzítés_
_Következő frissítés: Sprint 3 zárásakor vagy ápr. 25 mid-sprint review-n_
_Előző verzió: velocity-tracker-v1.3.md (2026-04-17 AM) — deprecated, lásd ** prefix_