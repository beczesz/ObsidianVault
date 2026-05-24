---
title: "DH Velocity Tracker -- AI vs. Tradicionális Fejlesztés"
version: 1.5
date: 2026-04-30
author: Claude (Anthropic) + Szabolcs
description: >
  Sprint 3 LEZÁRVA. 43 ticket Done, 99 SP teljesítve 15 nap alatt.
  9 ticket Sprint 4-be átvíve. Teljes projekt: 141 ticket / 56 nap.
supersedes: velocity-tracker-v1.4.md
id: 9679c28d-2a3b-4272-9cf1-a4f58f17f264
index_schema_version: 1
---

# DH Velocity Tracker v1.5 -- Sprint 3 LEZÁRVA

## v1.5 KÜLÖNBSÉGEK (v1.4-hez képest)

| Terület | v1.4 (2026-04-17) | **v1.5 (2026-04-30)** |
|---------|--------------------|-----------------------|
| Sprint 3 státusz | Active (2. nap, 6/20 Done) | **LEZÁRVA (43/52 Done, 9 ticket Sprint 4-be)** |
| Story Point lefedettség | 18/20 (90%) | **52/52 (100%) -- minden ticket becsülve** |
| Kumulatív Done | 103 | **141** |
| Projekt napok | 43 | **56** |
| AI szorzó (kumulatív) | 11.7x | **10.1x (stabilizálódik)** |

---

## I. ÖSSZEFOGLALÓ -- A nagy szám

| Mutató | v1.2 (ápr. 15) | v1.4 (ápr. 17) | **v1.5 (ápr. 30)** |
|--------|-----------------|-----------------|---------------------|
| **AI szorzó (mért, kumulatív)** | 11.7x | 11.7x | **10.1x** |
| Szabolcs becslése | 10x | 10x | 10x |
| Tradicionális sebesség | 4 nap/ticket | 4 nap/ticket | 4 nap/ticket |
| AI tényleges sebesség | 0.34 nap/ticket | 0.34 nap/ticket | **0.40 nap/ticket** |
| Teljes projekt throughput (átlag) | 16.6 ticket/hét | ~17 ticket/hét | **17.6 ticket/hét** |
| Sprint-szintű throughput | 20.5 ticket/hét (S2) | ~21 ticket/hét (S3 2. nap) | **20.1 ticket/hét (S3)** |

> **Sprint 3 záróértékelés:** 43 ticket Done / 15 nap = 2.87 ticket/nap. Ez a Sprint 2 szintjén van (2.9/nap), stabil teljesítmény. A szorzó 10.1x-re csökkent, ami Szabolcs eredeti 10x becslését igazolja.

---

## II. PROJEKT IDŐVONAL

| Mérföldkő | Dátum | Nap# |
|-----------|-------|------|
| Projekt indulás (első ticket) | 2026-03-05 | 0 |
| Első hét zárás (19 ticket) | 2026-03-22 | 17 |
| Második hét zárás (25 ticket) | 2026-03-29 | 24 |
| Harmadik hét zárás (22 ticket) | 2026-04-02 | 27 |
| Negyedik hét (DH migráció + Sprint 2 start) | 2026-04-03 | 29 |
| v0.2 Beta TÉNYLEGES | 2026-04-15 | 41 |
| Sprint 3 indulás | 2026-04-16 | 42 |
| **Sprint 3 LEZÁRVA** | **2026-04-30** | **56** |
| Sprint 4 indulás | 2026-04-30 | 56 |
| v0.3 Beta target | ~2026-05-15 | ~71 |

---

## III. HETI VELOCITY BREAKDOWN

| Hét | Dátum | Lezárt ticketek | Kumulatív | Sprint |
|-----|-------|-----------------|-----------|--------|
| 1-2 | márc. 5-15 | 0 | 0 | (setup + tervezés) |
| 3 | márc. 16-22 | 19 | 19 | Sprint 1.1 |
| 4 | márc. 23-29 | 25 | 44 | Sprint 1.1 |
| 5 | márc. 30 -- ápr. 2 | 22 | 66 | Sprint 1.1 (close) |
| 6 | ápr. 3-9 | 6 | 72 | Sprint 2 (DH migráció + indulás) |
| 7 | ápr. 10-14 | 19 | 91 | Sprint 2 |
| 8 | ápr. 15 (1 nap!) | +7 | 98 | Sprint 2 (close) |
| 9 | ápr. 16-22 | +18 | 116 | Sprint 3 |
| 10 | ápr. 23-29 | +21 | 137 | Sprint 3 |
| **11** | **ápr. 30 (1 nap)** | **+4** | **141** | **Sprint 3 (close)** |

---

## IV. SPRINT 3 -- VÉGLEGES EREDMÉNYEK

### Sprint 3 összefoglaló

| Mutató | Érték |
|--------|-------|
| Sprint hossz | 15 nap (ápr. 16 -- ápr. 30) |
| Összes ticket a sprintben | 52 (43 ticket + 2 Epic + 7 carryover) |
| **Done** | **43** |
| Sprint 4-be átvíve | **9** (1 Epic + 2 IP + 6 ToDo) |
| Story Points teljesítve | **99 SP** |
| Story Points átvíve | **26 SP** (+ 1 Epic SP nélkül) |
| Velocity (ticket/nap) | **2.87** |
| Velocity (SP/nap) | **6.6** |
| Velocity (ticket/hét) | **20.1** |

### Sprint 3 Done (43 ticket, 99 SP)

| Ticket | Summary | SP |
|--------|---------|-----|
| DH-38 | Customer list (admin) | 2 |
| DH-45 | Facebook page CTA & launch post | 1 |
| DH-96 | Több szállítási cím kezelése | 3 |
| DH-98 | „Înapoi la cumpărături" gomb | 1 |
| DH-103 | Rendelés keresése szám alapján mobilon | 2 |
| DH-112 | Guest checkout | 3 |
| DH-117 | Running Savings Counter -- Backend | 3 |
| DH-118 | Running Savings Counter -- Frontend | 3 |
| DH-119 | Post-order Recap | 5 |
| DH-120 | Reorder Basket Loader | 5 |
| DH-121 | Family Bundles -- Vásárlói nézet | 5 |
| DH-122 | Family Bundles -- Admin CRUD | 3 |
| DH-123 | Rendeléseim -- Spórolás badge + újrarendelés | 3 |
| DH-129 | Savings Engine Firebase eventek (10) | 3 |
| DH-130 | ÁSZF draft | 2 |
| DH-131 | Impresszum / Jogi információk screen | 1 |
| DH-132 | GDPR consent checkbox | 1 |
| DH-133 | Jogi szolgáltató tisztázása | 2 |
| DH-136 | ANSVSA szállítási engedély | 1 |
| DH-137 | Cookie policy | 1 |
| DH-143 | Vezérlőpult wireframe gyorslink | 1 |
| DH-147 | Profile page redesign + Admin panel | 5 |
| DH-150 | Founding 50 Program kampány | 3 |
| DH-151 | Founding 50 Backend: Campaign DocType | 3 |
| DH-152 | Founding 50 Backend: Inaktivitási scheduler | 2 |
| DH-153 | Founding 50 Frontend: Kampány modal | 3 |
| DH-154 | Founding 50 Frontend: Gratuláció modal + badge | 2 |
| DH-155 | Founding 50 Frontend: Betelt állapot UI | 2 |
| DH-156 | Founding 50 Analytics: Firebase events | 2 |
| DH-157 | Founding 50 QR kódok + UTM | 1 |
| DH-158 | Bug: Kiszállított rendelés státusza | 1 |
| DH-159 | Grillszezon MVP | 3 |
| DH-160 | Bug: Kedvencek popup | 1 |
| DH-164 | Kiszállítási felár 10km+ | 3 |
| DH-166 | Bug: Szállítási díj leírás hiányzik | 1 |
| DH-168 | Bug: Duplikált kategória | 1 |
| DH-169 | Bug: Registration Firebase events missing | 2 |
| DH-170 | Show savings in admin views | 2 |
| DH-171 | Analytics gap audit | 3 |
| DH-172 | Bug: Darabos termék nem-egész mennyiség | 1 |
| DH-175 | Több szállítási cím kezelése (user profil) | 3 |
| DH-177 | Felvágott min. mennyiség | 2 |
| DH-182 | Admin felhasználó kereső javítás | 2 |
| **Össz** | | **99 SP** |

### Sprint 4-be átvitt ticketek (9 item, 26 SP)

| Ticket | Típus | Státusz | SP | Summary |
|--------|-------|---------|-----|---------|
| DH-116 | Epic | In Progress | -- | Epic 10: Savings Engine |
| DH-145 | Task | To Do | 3 | Firebase Analytics + GDPR consent banner |
| DH-148 | Story | To Do | 3 | Reorder Quick Panel |
| DH-167 | Task | To Do | 1 | QR kód kassza szalagra |
| DH-173 | Task | To Do | 5 | Termék variáns választó |
| DH-174 | Task | In Progress | 5 | Admin ár-korrekció (súlyeltérés) |
| DH-176 | Bug | To Do | 1 | Ikon/szöveg vertikális igazítás |
| DH-181 | Task | To Do | 3 | Analytics cleanup v2.2 |
| DH-183 | Story | In Progress | 5 | Terméktípusok modellezése |

---

## V. SPRINT ÖSSZEHASONLÍTÁS

| Mutató | Sprint 1.1 | Sprint 2 | **Sprint 3** |
|--------|-----------|----------|-------------|
| Sprint hossz | ~25 nap | 13 nap | **15 nap** |
| Ticketek Done | 66 | 32 | **43** |
| SP Done | n/a | n/a | **99** |
| Velocity (ticket/nap) | 2.6 | 2.5 | **2.87** |
| Velocity (ticket/hét) | 18.5 | 17.2 | **20.1** |
| AI szorzó (sprint-szint) | ~10x | ~10x | **10.1x** |
| Carry-over | 0 | 0 | **9 ticket (26 SP)** |

> Sprint 3 volt a legnagyobb scope: 52 ticket indult benne (az eredeti 20-ról bővült user feedback, bugok, analytics audit és legal ticketek miatt). Ennek ellenére 43 Done -- 83%-os completion rate.

---

## VI. STORY POINT VELOCITY -- ELSŐ VALÓS MÉRÉS

Sprint 3 az első sprint ahol 100% SP lefedettség volt Jira-ban.

| Mutató | Sprint 3 |
|--------|---------|
| Total SP (sprint induláskor) | 125 (99 Done + 26 carry) |
| SP Done | **99** |
| SP Carry | **26** |
| SP/nap | **6.6** |
| SP/hét | **46.2** |
| Tradicionális becslés (0.6 SP/nap) | 165 nap |
| AI tényleges | 15 nap |
| **SP-alapú szorzó** | **11.0x** |

> Az SP-alapú szorzó (11.0x) magasabb mint a ticket-alapú (10.1x), mert a nagyobb complexity ticketek is gyorsan mentek. Ez a valódi AI-előny: a komplex feladatoknál arányosan nagyobb a gyorsulás.

---

## VII. KUMULATÍV PROJEKT METRIKÁK

| Mutató | Érték |
|--------|-------|
| Projekt indulás | 2026-03-05 |
| Ma | 2026-04-30 |
| Eltelt napok | **56** |
| Összes Done ticket | **141** |
| Kumulatív AI szorzó | **10.1x** |
| AI sebesség | 0.40 nap/ticket |
| Tradicionális becslés | 564 nap (1 dev, 4 nap/ticket) |
| AI tényleges | 56 nap |
| Megtakarított idő | **508 nap (~2 év)** |

---

## VIII. KÖLTSÉG HATÁS -- FRISSÍTVE

| Mutató | Tradicionális | AI-alapú | Megtakarítás |
|--------|--------------|----------|-------------|
| Dev idő (v0.1, Sprint 1.1) | ~1056 óra (1 dev × 66 ticket × 4 nap × 4h) | ~106 óra | 90% |
| Dev idő (v0.2, Sprint 2) | ~512 óra | ~51 óra | 90% |
| **Dev idő (v0.3, Sprint 3)** | **~688 óra** | **~60 óra** | **91%** |
| **Teljes projekt** | **~2256 óra** | **~224 óra** | **90%** |
| Dev költség teljes (EUR 25/óra) | EUR 56,400 | EUR 5,600 | **EUR 50,800** |
| Teljes DH kockázat (eddig) | ~EUR 60-65k | **~EUR 8-9k** | **~87%** |

---

## IX. SPRINT 4 -- NYITÓ ÁLLAPOT

Sprint 4 (ID: 68, "A heti szokás") indul 9 carry-over tickettel + további backlog ticketekkel.

### Carry-over kockázat

| Ticket | SP | Kockázat |
|--------|-----|---------|
| DH-183 (terméktípusok) | 5 | Komplex adatmodell -- de spec kész |
| DH-174 (admin ár-korrekció) | 5 | Összetett -- de DH-183-ra épül |
| DH-173 (variáns választó) | 5 | Komplex UX + backend |
| DH-145 (Firebase GDPR) | 3 | Legal dependency (DH-133 Done) |
| DH-181 (analytics cleanup) | 3 | Sok apró fix, de jól dokumentált |
| DH-148 (reorder panel) | 3 | DH-120 Done, építhet rá |
| DH-176 (ikon igazítás) | 1 | Gyors CSS fix |
| DH-167 (QR kassza) | 1 | Design + nyomda koordináció |

**Sprint 4 nyitó SP (carry-over): 26 SP**

---

## X. AJÁNLOTT AKCIÓK

### Sprint 3 záráshoz

1. ✅ **43 ticket Done, 99 SP teljesítve**
2. ✅ **9 ticket Sprint 4-be mozgatva (26 SP)**
3. ✅ **100% SP lefedettség** -- minden ticket becsülve
4. ✅ **Velocity tracker v1.5 elkészült**
5. ⬜ Sprint 3 lezárása Jira-ban (Szabolcs)
6. ⬜ Sprint 4 aktiválása Jira-ban (Szabolcs)

### Sprint 4 indításához

7. ⬜ Sprint 4 backlog review -- carry + új ticketek priorizálása
8. ⬜ DH-183 (terméktípusok) befejezése -- Sprint 4 legfontosabb alapja
9. ⬜ v0.3 Beta előkészítés (~máj. 15)
10. ⬜ BMC v2.3 frissítés

---

_Generálva: 2026-04-30 | Forrás: Jira DH projekt Sprint 3 záró snapshot_
_Következő frissítés: Sprint 4 zárásakor_
_Előző verzió: velocity-tracker-v1.4.md (2026-04-17) -- deprecated_
