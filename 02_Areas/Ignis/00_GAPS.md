---
title: 00_GAPS — Ignis (scoped)
date: 2026-06-03
author: Becze Szabolcs
status: active
description: Inkonzisztenciák, duplikációk, stale anyagok és strukturális hiányosságok az Ignis területen. Legkritikusabb: a 2. szint Haladó mappájában 6 TransOffice dry-run másolat és 4 ZIP fájl halmozódott fel, ezek nagy részének archivalása vagy törlése ajánlott.
id: 7f3a2e41-bc09-4d8e-a12f-001ignis00005
index_schema_version: 1
bdos_index: true
generated_by: librarian v0.8.3
generated_at: 2026-06-03
scope: 02_Areas/Ignis
mode: index
---

# 00_GAPS — Ignis (scoped)

> Inkonzisztenciák, duplikációk, elavult anyagok, strukturális hiányosságok.
> Librarian v0.8.3 — index mód — 2026-06-03.
> **TIDY/DEEP-CLEAN akcióra jelölt elemek** kizárólag javaslatok — tényleges törlés csak explicit `deep-clean --apply` hívással.

---

## GAP-1 [KRITIKUS] — TransOffice dry-run másolat-burjánzás

**Hol:** `Ignis Academy/2. szint/Haladó/`
**Probléma:** A fiktív TransOffice cég adatainak 6 különböző másolata él egymás mellett:

| Mappa | Fájlszám | Szerepe |
|---|---|---|
| `Tananyag/TransOffice/` | (részleges) | Kanonikus kiindulópont (kaotikus) |
| `TransOfficeCopy/` | 59 | dry-run #1 eredmény |
| `TransOfficeDryRun2.0/` | 65 | dry-run #2 eredmény |
| `TransOfficeCopy_v3/` | 35 | dry-run #3 |
| `TransOfficeCopy_v4/` | 38 | dry-run #4 |
| `TransOffice_LIVE/` | 94 | Aktuális LIVE állapot (valószínűleg KANONIKUS) |
| `dryrun3/` | 87 | Legújabb dry-run (87 fájl) |

**Becslés:** 400+ duplikált fájl a dry-run másolatokban.
**Ajánlott akció:** deep-clean módban:
- `TransOffice_LIVE/` megtartása kanonikusként
- `TransOfficeCopy/`, `TransOfficeDryRun2.0/`, `TransOfficeCopy_v3/`, `TransOfficeCopy_v4/` archiválása `Műhely/_archivum/`-ba vagy törlése (cross-reference check után)
- `dryrun3/` státuszának tisztázása (aktív fejlesztés alatt van-e?)

**Blokkoló:** tisztázni kell, hogy a `dryrun3/` aktív fejlesztési kontextus-e (ha igen, megtartandó), vagy szintén archivált dry-run eredmény.

---

## GAP-2 [FONTOS] — ZIP fájl duplikátum és régi verziók

**Hol:** `Ignis Academy/2. szint/Haladó/`
**Probléma:**

| Fájl | MD5 | Státusz |
|---|---|---|
| `Tananyag_Haladó_v1.0.zip` | (ellenőrizetlen) | ELAVULT — törlendő |
| `Tananyag_Haladó_v1.1.zip` | (ellenőrizetlen) | ELAVULT — törlendő |
| `Tananyag_Haladó_v1.2.zip` | `1def696e...` | KANONIKUS — megtartandó |
| `_FELTOLTENDO/Tananyag_Halado_v1.2.zip` | `1def696e...` | BYTE-AZONOS másolat a v1.2-vel |

**Ellenőrzött:** `Tananyag_Haladó_v1.2.zip` és `_FELTOLTENDO/Tananyag_Halado_v1.2.zip` MD5 azonos (`1def696e17310e9a62e216c09c968ff2`).
**Ajánlott akció (deep-clean):**
- `v1.0.zip` és `v1.1.zip` törlése (ha nincs hivatkozás rájuk)
- `_FELTOLTENDO/Tananyag_Halado_v1.2.zip` törlése (byte-azonos duplikátum — a `_FELTOLTENDO/` mappa a staging terület, a v1.2.zip a kanonikus)

**Megjegyzés:** `_FELTOLTENDO/` mappát megőrizni a `_README.md`-vel és a `Ghidul-IMM-2026.pdf`-fel, ha még nem lett feltöltve a platformra.

---

## GAP-3 [FONTOS] — Oktató segédlet verzió-burjánzás (Műhely/00_Tervezes/)

**Hol:** `Ignis Academy/2. szint/Haladó/Műhely/00_Tervezes/`
**Probléma:** Az oktató segédletnek 3 MD és 3 PDF verziója él egymás mellett:

| Fájl | Státusz |
|---|---|
| `09_Oktatoi_segedlet_v1.0.md` | ELAVULT (archívumban is van másolat) |
| `09_Oktatoi_segedlet_v2.0.md` | ELAVULT (v2.1 felváltotta) |
| `09_Oktatoi_segedlet_v2.1.md` | KANONIKUS |
| `Oktatoi_segedlet_ROVID_v2.1.md` | AKTÍV (rövidített változat) |
| `Oktatoi_segedlet_v2.0.pdf` | régi PDF |
| `Oktatoi_segedlet_v2.1.pdf` | KANONIKUS PDF |
| `Oktatoi_segedlet_v2.2.pdf` | Újabb PDF — MD forrás nincs? Inkonzisztencia! |
| `Oktatoi_spickli_v2.1.pdf` | Spickli (kísérő) |
| `Oktatoi_spickli_v2.2.pdf` | Spickli újabb verzió |

**Inkonzisztencia:** `Oktatoi_segedlet_v2.2.pdf` létezik, de `09_Oktatoi_segedlet_v2.2.md` nem — PDF forrása ismeretlen. Honnan generálódott?
**Ajánlott akció:** v1.0 és v2.0 MD fájlok archiválása; PDF verziók dokumentálása.

---

## GAP-4 [FONTOS] — DryRun prompt fájlok sora (10-16 sorszám)

**Hol:** `Ignis Academy/2. szint/Haladó/Műhely/00_Tervezes/`
**Probléma:** 7 különböző DryRun prompt fájl (10..16):
- `10_DryRun_kontext.md`
- `11_DryRun_prompt.md`
- `13_DryRun_v2_prompt.md`
- `14_DryRun_v3_foolproof_prompt.md`
- `15_DryRun_v4_narrativ_tengely.md`
- `16_DryRun_3_lepes_F1_F4.md`

Ezek fejlesztési iterációk. Vajon mind aktív referencia, vagy többnyire archivált kísérlet?
**Ajánlott akció:** Tidy mód — a korábbi verziók (10-14) archiválhatók a `_archivum/`-ba, ha a legfrissebb (15-16) a kanonikus.

---

## GAP-5 [KÖZEPES] — HandsOn iterációk (08, 12)

**Hol:** `Ignis Academy/2. szint/Haladó/Műhely/00_Tervezes/`
**Probléma:**
- `08_HandsOn_javitas.md` (javítás egy korábbi verzióhoz)
- `12_HandsOn_v1.1_strategia.md` (stratégiai verzió)

Ezek viszonya az aktív F1..F6 feladatleírásokhoz nem egyértelmű.

---

## GAP-6 [KÖZEPES] — _archivum/ belső duplikáció

**Hol:** `Ignis Academy/2. szint/Haladó/Műhely/_archivum/`
**Probléma:** Az archívum maga is tagolt al-mappákkal rendelkezik (`F2_F6_v1.0/`, `datum_pivot_v1_2/`, `v2.0_pre_hint_refactor/`, `09_Oktatoi_segedlet_v1.0.md`).
- A `_archivum/09_Oktatoi_segedlet_v1.0.md` ugyanolyan nevű, mint az aktív `00_Tervezes/09_Oktatoi_segedlet_v1.0.md` — byte-azonos-e?
- A `_archivum/meeting_transcript_20250224_v1.md` és az `_archivum/02_Meeting_Productivity/meeting_transcript_20250224_v1.md` is duplikációnak tűnik.

---

## GAP-7 [KÖZEPES] — Pozicionalas/ frontmatter inkonzisztencia

**Hol:** `Ignis Academy/2. szint/Pozicionalas/`
**Probléma:**
- `brand-brief.md` frontmatter-e tartalmaz Windows-path hivatkozást: `vault_path: "C:/Users/EvoComputers/Obsidian/..."` — stale maradék egy másik gépről.
- `03_MESSAGING_ARCHITECTURE.md` és `05_ERNYO_HIERARCHIA_osszehangolas.md` státusza `draft` (v0.1) — jelenlegi állapot megfelelő?
- A `brand-brief.md`-ből hiányzik a standard frontmatter-blokk (`title`, `date`, `status` mezők YAML-ban, nem commentban).

---

## GAP-8 [ALACSONY] — Frontmatter hiányos a régebbi fájlokon

**Érintett fájlok (nem teljes lista):**
- `Ignis Academy/2. szint/Haladó/Műhely/00_Tervezes/02_ChatGPT szintézis - Workshop struktúra.md`
- `Ignis Academy/2. szint/Haladó/Műhely/00_Tervezes/05_ChatGPT szintézis v0.3 - Filozófia és delivery.md`
- `Ignis Academy/2. szint/Pozicionalas/DESIGN.md`
- `Ignis Academy/2. szint/Pozicionalas/PRODUCT.md`
- `Ignis Academy/2. szint/Haladó/Műhely/_archivum/` belső fájlok

**Probléma:** Ezeknek hiányzik a `description:` mező (Phase 3.1 kötelező), ill. egyes fájloknak `id:` és `index_schema_version:` is hiányzik.
**Ajánlott akció:** `python3 migrate_uuid.py --apply` a vault-indexing capability-vel, majd manuális description-hozzáadás.

---

## GAP-9 [ALACSONY] — 1. szint / _korabbi-16-dia/ árvaság

**Hol:** `Ignis Academy/1. szint/Diaképek/_korabbi-16-dia/`
**Probléma:** 16 JPEG fájl (slide-01..16) a korábbi, meghaladott prezentáció-verzióból. A README.md maga is jelzi: „ha biztosan elavult, törölhető."
**Ajánlott akció:** Törlés jóváhagyással.

---

## GAP-10 [ALACSONY] — Marketing/ mappa (gyökér) — egyetlen PNG

**Hol:** `02_Areas/Ignis/Marketing/`
**Probléma:** `21 Alkalom - Előlap.png` — egyetlen fájl, nincs README, nincs frontmatter, nincs kontextus. Árva asset.
**Ajánlott akció:** README vagy frontmatter hozzáadása, vagy átköltöztetés a megfelelő helyre.

---

## GAP-11 [ALACSONY] — Palyazat/ mappa tartalom ismeretlen

**Hol:** `Ignis Academy/Palyazat/`
**Probléma:** A könyvtár-lista alapján a mappa létezik, de tartalmát a Librarian nem olvasta be (a find a gyökerétől nem hozta a tartalmát jelölten). Ellenőrizendő.

---

## Összefoglalás

| GAP | Súlyosság | Ajánlott akció |
|---|---|---|
| GAP-1: TransOffice másolat-burjánzás (6 mappa, ~400 fájl) | KRITIKUS | deep-clean: archiválás/törlés |
| GAP-2: ZIP duplikátum + régi verziók (v1.0, v1.1, _FELTOLTENDO másolat) | FONTOS | deep-clean: byte-azonos törlés |
| GAP-3: Oktató segédlet verzió-burjánzás + v2.2 PDF forrás hiányzik | FONTOS | tidy + tisztázás |
| GAP-4: DryRun prompt iterációk (10-16) | FONTOS | tidy: régi verziók archiválása |
| GAP-5: HandsOn iterációk | KÖZEPES | manuális tisztázás |
| GAP-6: _archivum/ belső duplikáció | KÖZEPES | deep-clean ellenőrzés |
| GAP-7: brand-brief.md stale Windows-path + draft statusok | KÖZEPES | manuális javítás |
| GAP-8: Frontmatter hiány régi fájlokon | ALACSONY | migrate_uuid.py + description |
| GAP-9: _korabbi-16-dia/ árva JPEGs | ALACSONY | törlés jóváhagyással |
| GAP-10: Marketing/ árva PNG | ALACSONY | kontextus hozzáadása |
| GAP-11: Palyazat/ tartalom ismeretlen | ALACSONY | ellenőrzés |
