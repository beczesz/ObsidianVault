---
title: 00_DECISIONS_INDEX — Ignis (scoped)
date: 2026-06-03
author: Becze Szabolcs
status: active
description: Döntés-index az Ignis területre. Rögzíti a lezárt és nyitott döntéseket a képzési vonalak naming-jéről, pozicionálásáról, a 3+1 (valójában 2+2) szint-modellről, a Tájoló/Műhely párhuzamos tengelyéről és az ernyő-hierarchiáról.
id: 7f3a2e41-bc09-4d8e-a12f-001ignis00003
index_schema_version: 1
bdos_index: true
generated_by: librarian v0.8.3
generated_at: 2026-06-03
scope: 02_Areas/Ignis
mode: index
---

# 00_DECISIONS_INDEX — Ignis (scoped)

> Minden rögzített és jelölt döntés forrás-fájl + sor referenciával. Status: `LEZÁRT` | `NYITOTT` | `FÜGGŐ`

---

## Stratégiai döntések

### D1 — Ernyő-tagline (Ignis Academy)
**Status:** NYITOTT
**Leírás:** Az Ignis Academy ernyő-szintű tagline döntésre vár. Jelöltek a `Brand/05_ERNYO...`-ban; ChatGPT a „bizalmi" irányt javasolta.
**Forrás:** `Ignis Academy/Catalog/00_CATALOG.md` — „Nyitott kérdések" §
**Kontextus:** A market category „gyakorlati digitális munkamódszerek" (NEM „AI képzés") — ernyő-szintű kommunikáció ezt tükrözze.

### D2 — Műhely+ specializáció
**Status:** NYITOTT
**Leírás:** Melyik irányba induljon a Műhely+?
- Marketing specializáció
- Üzletfejlesztés specializáció
- Általános haladó AI-használat
**Forrás:** `Ignis Academy/Catalog/muhely-plus/COURSE.md` — „Nyitott döntés (D2)" §
**Blokkoló:** Mindaddig nincs tananyag, naming, pozicionálás.

### D3 — 7 szokás besorolása
**Status:** FÉLIG LEZÁRT
**Leírás:** A 7 szokás az Ignis Academy alá kerül-e, vagy önálló prémium vonal?
**Döntés (jelen modell):** Az Ignis Academy 2. (szervezetfejlesztési) vonalaként szerepel — de a vizuális hangolás (prémium vs. bizalmi-praktikus) még eldöntendő.
**Forrás:** `Ignis Academy/Catalog/het-szokas/COURSE.md` — „Nyitott döntés (D3)" §

---

## Pozicionálási döntések (lezárt)

### P1 — Tájoló és Műhely NEM szekvenciális
**Status:** LEZÁRT
**Döntés:** A két képzés párhuzamos tengely, nem kezdő→haladó progresszió.
- Tájoló = *hogyan gondolkodj* (mindset, időtálló)
- Műhely = *hogyan dolgozz* (praxis, eszköz-specifikus)
**Cross-sell logika:** Tájoló→Műhely (felemelő funnel); Műhely→Tájoló (mélyítő retroaktív)
**Forrás:** `Ignis Academy/Catalog/00_CATALOG.md` — „Tájoló és Műhely NEM szekvenciális" bekezdés

### P2 — Market category fókusz
**Status:** LEZÁRT
**Döntés:** „Gyakorlati digitális munkamódszerek és modern eszközhasználat" — NEM „AI képzés". Anti-hype, bizalmi márka.
**Forrás:** `Ignis Academy/Catalog/00_CATALOG.md` — „Ernyő-pozicionálás" §

### P3 — Villain (Miller BrandScript)
**Status:** LEZÁRT
**Döntés:** „A digitális káosz + a lemaradástól való félelem + túl sok eszköz egyszerre"
**Forrás:** `Ignis Academy/Catalog/00_CATALOG.md` — „Ernyő-pozicionálás" §

### P4 — Best-fit célközönség definiálása
**Status:** LEZÁRT
**Döntés:** „Digitálisan bizonytalan, nem-technikai tudásmunkás és KKV-vezető (35-55), a digitális bizonytalanság tengely mentén, nem korosztály szerint."
**Forrás:** `Ignis Academy/Catalog/00_CATALOG.md` — „Ernyő-pozicionálás" §

### P5 — Szint-modell (tier rendszer)
**Status:** LEZÁRT
**Döntés:** 4 tier: `belepo` (Tájoló), `core` (Műhely), `halado` (Műhely+), `premium` (7 szokás)
**Forrás:** `Ignis Academy/Catalog/00_CATALOG.md` — „Szint-modell" §

---

## Naming döntések

### N1 — „Tájoló" és „Műhely" munkanevek
**Status:** NYITOTT
**Leírás:** Mindkét képzés neve még munkanév (working title). Végleges naming döntés nem született.
**Forrás:** `tajolo/COURSE.md` — „Nyitott kérdések" §; `muhely/COURSE.md` — „Nyitott kérdések" §

### N2 — Ignis Academy saját vizuális identitása
**Status:** NYITOTT
**Leírás:** A képzési márkának nincs logója, saját színe, tipójája. Jelenleg kölcsönzött partner-arculat.
**Forrás:** `Ignis Academy/Catalog/00_CATALOG.md` — „Nyitott kérdések" §3

---

## Tananyag-fejlesztési döntések (lezárt)

### T1 — Workshop módszer (Narrated Live Experience)
**Status:** LEZÁRT
**Döntés:** 70% élő demo, 20% guided micro hands-on, 10% szabad próbálkozás. Apple keynote × HBO mini-sorozat analógia.
**Forrás:** `Ignis Academy/2. szint/Haladó/CLAUDE.md` — „Módszer" §

### T2 — Fiktív cég TransOffice Trade SRL (Székelyudvarhely)
**Status:** LEZÁRT
**Döntés:** A workshop egységes fiktív cégre épül (nem valódi), az EU pályázat elektromos autóflottára szól (70-80% támogatás).
**Forrás:** `Ignis Academy/2. szint/Haladó/CLAUDE.md` — „A 6 feladat" §

### T3 — Tananyag + Műhely kettős mappa-struktúra
**Status:** LEZÁRT
**Döntés:** `Tananyag/` = zip-elhető tanulói csomag; `Műhely/` = fejlesztői backstage. Azonos fázis-számozás (01-06).
**Forrás:** `Ignis Academy/2. szint/Haladó/CLAUDE.md` — „Miért két mappa?" §

### T4 — Kanonikus ZIP verzió: v1.2
**Status:** LEZÁRT
**Döntés:** A kiadott tananyag-csomag `Tananyag_Haladó_v1.2.zip` (5.3 MB, 94 fájl).
**Forrás:** `2. szint/Haladó/_FELTOLTENDO/_README.md`

### T5 — Oktató segédlet kanonikus verziója: v2.1
**Status:** LEZÁRT
**Döntés:** `09_Oktatoi_segedlet_v2.1.md` a kanonikus. v1.0 és v2.0 archívumba kerültek.
**Forrás:** `Műhely/00_Tervezes/` — verzió-fájlok jelenléte alapján

---

## Üzleti döntések (nyitott)

### B1 — Árazás
**Status:** NYITOTT
**Leírás:** Egyik képzésnek sincs ára. Tájoló: ingyenes lead-magnet vagy fizetős? Bundle ár Tájoló+Műhely?
**Forrás:** `Catalog/00_CATALOG.md` — „Nyitott kérdések" §1; `tajolo/COURSE.md` — „Nyitott kérdések" §

### B2 — SaaS platform viszonya
**Status:** NYITOTT
**Leírás:** A `02_Areas/Ignis Academy/` (EU-pályázatos B2B SaaS platform) viszonya az oktatási ághoz tisztázandó. Jelen Catalog NEM érinti azt a mappát.
**Forrás:** `Catalog/00_CATALOG.md` — „Nyitott kérdések" §7

### B3 — Nyitott workshop vs in-company arány
**Status:** NYITOTT
**Leírás:** A Műhely jelenleg in-company fut (HBC). Nyitott workshop formátum és árazás még nincs.
**Forrás:** `muhely/COURSE.md` — „Nyitott kérdések" §

---

## IgnisCafe / IgnisXY döntések

### I1 — IgnisCafe önfenntarthatósága
**Status:** NYITOTT (implicit)
**Leírás:** A Napló.md felveti: az Ignis Academy „nem is önfenntartó... Talán az Ignis jövője?" — a két ág stratégiai viszonya nem tisztázott.
**Forrás:** `IgnisXY/Napló.md` — 2025-12-26 bejegyzés
