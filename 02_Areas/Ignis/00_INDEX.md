---
title: 00_INDEX — Ignis (scoped)
date: 2026-06-03
author: Becze Szabolcs
status: active
description: Scoped index az 02_Areas/Ignis/ mappa teljes tartalmáról. Két fő terület: Ignis Academy (profit-orientált képzések, 3 szint + Catalog) és IgnisXY/IgnisCafe (közösségi tér). Librarian v0.8.3 generálta 2026-06-03-án.
id: 7f3a2e41-bc09-4d8e-a12f-001ignis00001
index_schema_version: 1
bdos_index: true
generated_by: librarian v0.8.3
generated_at: 2026-06-03
scope: 02_Areas/Ignis
mode: index
file_count: 700
---

# 00_INDEX — Ignis (scoped index)

> Scope: `02_Areas/Ignis/` | Generálva: 2026-06-03 | Librarian v0.8.3
> Összes fájl: ~700 | Markdown fájlok: 223 | Könyvtárak: 130+

---

## Márka-architektúra (egy pillantásra)

```
02_Areas/Ignis/
├── Ignis Academy/          ← profit-orientált képzési ág
│   ├── 1. szint/           ← Alapozó (Tájoló) — KÉSZ, él
│   ├── 2. szint/           ← Haladó (Műhely) — KÉSZ, fut in-company
│   │   ├── Haladó/         ← tananyag + Műhely backstage
│   │   ├── Pozicionalas/   ← brand-brief, messaging, ernyő-hierarchia
│   │   └── Marketing/      ← 21 Alkalom elölap (1 PNG)
│   ├── 7 szokás/           ← Szervezetfejlesztési vonal forrásanyag
│   ├── Catalog/            ← marketing metaadat (4 COURSE.md)
│   └── Palyazat/           ← (tartalom ismeretlen, ellenőrzendő)
├── IgnisXY/                ← IgnisCafe közösségi tér
└── Marketing/              ← 1 PNG (21 Alkalom elölap)
```

---

## 1. szint — Alapozó (Tájoló)

**Kanonikus path:** `Ignis Academy/1. szint/`
**Státusz:** aktív, él (webinar futott 2026-03-24)

| Fájl | Leírás |
|---|---|
| `1. szint/README.md` | Főbejárat: struktúra, hivatkozások, rendezési napló |
| `Tananyag/ai_learning_material_v0.4.md` | A 28 tipp teljes szövege (EP42 forrás, 4 dimenzió: Ethos/Logos/Pathos/Thelos) |
| `Tananyag/28_AI_Tipp_Tananyag.pdf` | HU tananyag PDF kész verzió |
| `Tananyag/slide_structure.md` | A 24 diás webinar-struktúra leírása |
| `Prezentáció/webinar_presentation.pptx` | Kész 24 diás prezentáció |
| `Prezentáció/webinar_presentation.pdf` | PDF export a pptx-ből |
| `Diaképek/pptx-slide-01..24.jpg` | 24 dia + 2 QA-javított kép |
| `Diaképek/_korabbi-16-dia/slide-01..16.jpg` | Korábbi 16 diás verzió (archív jelleggel megőrizve) |

---

## 2. szint — Haladó (Műhely)

**Kanonikus path:** `Ignis Academy/2. szint/Haladó/`
**Státusz:** aktív (v2.0), fut in-company (HBC ügyfél)

### Két fő mappa

| Mappa | Szerepe |
|---|---|
| `Haladó/Tananyag/` | Tanulói csomag (zip-elhető, 94 fájl) |
| `Haladó/Műhely/` | Fejlesztői backstage (nem kerül a zip-be) |

### Tananyag/ — kulcsfájlok

| Fájl | Leírás |
|---|---|
| `CLAUDE.md` | Struktúra-magyarázó, master entry point az agenteknek |
| `Tananyag/00_Bevezetes/Ceg_leiras_TransOffice.md` | A fiktív TransOffice Trade SRL cégleírása |
| `Tananyag/01_Ceg_megertes/Feladat_1.1.md` | F1 feladatleírás (fájlrendezés) |
| `Tananyag/02_Meeting_Productivity/` | F2 feladatok + meeting transcript |
| `Tananyag/03_Dontes_Elemzes/` | F3 feladatok + pályázati kiírás (Ghidul IMM) |
| `Tananyag/04_Legal_Szerzodes/` | F4 feladatok + emailek, Excel, szerződés |
| `Tananyag/05_Kommunikacio_Email/` | F5 feladatok (üzleti terv, csomag, form) |
| `Tananyag/06_Marketing_Honlap/` | F6 feladatok + régi ANAF-stílusú weboldal |
| `Tananyag/TransOffice/` | Kiindulópontként kaotikus 27+ asset (SZÁNDÉKOSAN zűrös) |

### Műhely/00_Tervezes/ — fejlesztői backstage kulcsfájlok

| Fájl | Leírás |
|---|---|
| `00_STORY_BOOK.md` | Workshop teljes narratívája (MINDIG EZT OLVASD ELŐSZÖR) |
| `00_Bevezető_szöveg.md` | Workshop bevezető script |
| `01_Logisztika és előfeltételek.md` | Logisztika, előfeltételek |
| `02_ChatGPT szintézis - Workshop struktúra.md` | Master plan v0.2 |
| `05_ChatGPT szintézis v0.3 - Filozófia és delivery.md` | Filozofia és delivery |
| `07_Versenytars_elemzes_ThrivenExus.md` | Versenytárs-elemzés (ThriveNexus) |
| `09_Oktatoi_segedlet_v2.1.md` | Oktató segédlet (kanonikus: v2.1) |
| `Oktatoi_segedlet_ROVID_v2.1.md` | Rövid oktató segédlet |

### Dry-run másolatok (FŐBB GAP — lásd GAPS.md)

| Mappa | Fájlszám | Szerepe |
|---|---|---|
| `Haladó/TransOfficeCopy/` | 59 | 1. dry-run másolat |
| `Haladó/TransOfficeCopy_v3/` | 35 | 3. dry-run másolat |
| `Haladó/TransOfficeCopy_v4/` | 38 | 4. dry-run másolat |
| `Haladó/TransOfficeDryRun2.0/` | 65 | 2.0 dry-run másolat |
| `Haladó/TransOffice_LIVE/` | 94 | Kanonikus LIVE állapot |
| `Haladó/dryrun3/` | 87 | 3. dry-run futtatás |
| `Haladó/Műhely/_archivum/` | sok | Archivált verziók |

### ZIP csomagok

| Fájl | MD5 | Státusz |
|---|---|---|
| `Tananyag_Haladó_v1.0.zip` | (nem ellenőrzött) | régebbi |
| `Tananyag_Haladó_v1.1.zip` | (nem ellenőrzött) | régebbi |
| `Tananyag_Haladó_v1.2.zip` | 1def696e... | KANONIKUS |
| `_FELTOLTENDO/Tananyag_Halado_v1.2.zip` | 1def696e... | AZONOS a fentivel (byte-duplikátum) |

### Pozicionálás és messaging

| Fájl | Leírás |
|---|---|
| `Pozicionalas/brand-brief.md` | Brand identity, stage: positioning |
| `Pozicionalas/03_MESSAGING_ARCHITECTURE.md` | Miller BrandScript, tagline-ok (draft v0.1) |
| `Pozicionalas/04_one-pager_v0.1.html` | One-pager prototípus |
| `Pozicionalas/05_ERNYO_HIERARCHIA_osszehangolas.md` | 2 kategória, 4 képzés ernyő-stratégia |
| `Pozicionalas/DESIGN.md` | Design brief |
| `Pozicionalas/PRODUCT.md` | Termék-szintű leírás |

---

## Catalog (marketing metaadat)

**Kanonikus path:** `Ignis Academy/Catalog/`

| Fájl | Képzés | Státusz |
|---|---|---|
| `00_CATALOG.md` | Ernyő-index (v0.1) | aktív |
| `tajolo/COURSE.md` | Tájoló | él (live) |
| `muhely/COURSE.md` | Műhely | kész, fut |
| `muhely-plus/COURSE.md` | Műhely+ | tervezett |
| `het-szokas/COURSE.md` | A 7 szokás | tervezett |

---

## 7 szokás (szervezetfejlesztési vonal forrásanyag)

**Path:** `Ignis Academy/7 szokás/Transcriptek/`

- `README.md` — index, 8 epizód, ~34 000 szó
- `01..08_*.txt` — tisztított transcript (8 fájl, Bevezető + 7 szokás)
- `01..08_*.hu.srt` — nyers felirat időbélyegekkel (8 fájl)

---

## IgnisXY (IgnisCafe közösségi tér)

**Path:** `IgnisXY/`

| Fájl | Leírás |
|---|---|
| `IgnisCafe - Alkotmány.md` | Vízió, misszió, értékek (2025-12-26) |
| `Napló.md` | Személyes napló a közösségi tér koncepciójáról (Barni atya felkérése) |

---

## Marketing (gyökér szintű)

**Path:** `Marketing/`

- `21 Alkalom - Előlap.png` — egyetlen fájl, tartalom ismeretlen

---

## Kulcs entry pointok

1. **Catalog** belépő: `Ignis Academy/Catalog/00_CATALOG.md`
2. **Tájoló** tananyag: `Ignis Academy/1. szint/README.md`
3. **Műhely** struktúra: `Ignis Academy/2. szint/Haladó/CLAUDE.md`
4. **Workshop narratíva** (STORY_BOOK): `Ignis Academy/2. szint/Haladó/Műhely/00_Tervezes/00_STORY_BOOK.md`
5. **Pozicionálás**: `Ignis Academy/2. szint/Pozicionalas/03_MESSAGING_ARCHITECTURE.md`
