---
title: "Product Variations — Feature Folder"
date: 2026-05-09
author: Becze Szabolcs
status: active
description: "Szabolcs (Exar Labs) és a Deák Húsmíves termelők DH-173 feature mappája: 15 termékre (59 variation érték) vonatkozó specifikáció, per-termék opció mátrix és termelői input gyűjteménye. Sprint 4-hez szükséges backend-frontend fejlesztés dokumentációja."
description_source: auto
description_hash: 0cb238365e2026b7
id: 45428e78-a127-45db-be0a-c9e547bde63c
index_schema_version: 1
bdos_index: true
---
# Product Variations — Feature Folder

> **Jira:** [DH-173 — Termék testreszabás és preferencia mentés](https://exarlabs.atlassian.net/browse/DH-173)
> **Sprint:** 4 (To Do)
> **Státusz:** SPEC — fejlesztés még nem indult, de a tartalom (15 termék × 59 variation-érték) már rögzítve a MASTER MD-kben
> **Felelős:** Szabolcs (Exar Labs) + Deák Húsmíves termelők

---

## 📁 Mi van ebben a mappában

| Fájl | Mire való |
|------|-----------|
| `README.md` | Ez a fájl — overview + linkek |
| `product-variations-spec-v1.0.md` | Teljes feature spec (DH-173) — probléma, megoldás, UX, adatmodell, kockázatok |
| `product-options-matrix-v1.0.md` | Konkrét per-termék opció mátrix — 15 termék 59 variation érték HU + RO + termelői megjegyzéssel |

---

## 🎯 Mit jelent ez a feature

**„A hentes beszélgetés digitalizálása."** Egy hagyományos kézműves húsüzletben a mészáros ismeri a törzsvásárlót — tudja, hogy a darált húst soványabban szereti, a karajt vékonyra szeletelve kéri, és a csülköt mindig pácolatlanul viszi. Ez a személyes kapcsolat versenyelőny. Ezt a feature digitalizálja.

A vásárló a termékdetail oldalon a **"Cum să-ți pregătim?"** szekcióban kiválasztja az opciókat (pl. szeletelés, pácolás, méret), a rendszer megjegyzi per user per termék, és újrarendelésnél automatikusan betölti.

## 🔗 Kapcsolódó források

### A MASTER MD-k (single source of truth a termék-szintű variációkra)
A 15 termék DH-173 opciói **MD-only mezőkben** rögzítve a `Products/MASTER/products/*.md` fájlokban (`## Opciók` szekció). A jelenlegi v1.1 schema NEM exportálja JSON-ba (Sprint 4-re vár).

→ Lásd: `Products/CLAUDE.md` és a 15 termék MD-je

### Excel review (gyors átnézet)
→ `Products/products_v1.1_review.xlsx` — a „Variációk (részletek)" oszlop teljes bontást mutat minden termékhez

### Eredeti termelői meeting (forrás)
- Hangfelvétel: `Products/meetings/DH - Mikado - Termek variációk-transcript-full.srt` (43 perc)
- Decisions kivonat: `Products/meetings/2026-05-07_decisions.md`
- Belső kódlista: `Products/meetings/2026-05-07_internal-product-codes.md`

### Előd-spec (archív)
- `Business Development/pilot-husuzlet/savings-engine/Ideas/v0.4-product-preferences-spec.md` (v0.1 — 2026-04-30, a meeting előtt)
- A jelen mappa **v1.0** spec-je hivatalosan ezt felülírja

### Kapcsolódó Jira ticketek
- **DH-173** — A jelen feature
- **DH-183** (DONE) — Terméktípusok modellezése (weight/piece/hybrid) — prerequisite
- **DH-120** — Reorder Basket Loader (preferenciák betöltése)
- **DH-127** — Familiar Favourites (preferenciákat is tartalmazza)
- **DH-174** — Admin ár-korrekció (kapcsolódó — súlyeltérés flow)

## 📊 Statisztika a tartalomról

- **15/46 termék** rendelkezik DH-173 opciókkal (a maradék 31 csak simán kilóra/db)
- **59 összes variation érték** rögzítve
- **3 opció-típus** támogatva: `single_select` (használatban), `multi_level` (deklarálva, még nincs használva), `text` (deklarálva, még nincs használva)
- **HU + RO** lokalizáció minden értékhez

## 🚦 Mi a következő lépés

1. **Spec v1.0 review** — Szabolcs átnézi a `product-variations-spec-v1.0.md`-t
2. **Per-termék pontosítás** — ha valamelyik opció mégis változik, az MD-ben módosítjuk + Excel regenerálás
3. **Sprint 4 indítás** — backend (Frappe DocType `Product Option` + `User Product Preference`) + frontend (UI komponensek)
4. **Schema bump v1.2** — amikor a backend kész, a `_schema.json`-ba bekerül az `options[]` mező + a JSON output is tartalmazni fogja

---

**Verzió:** 1.0 | **Dátum:** 2026-05-07 | **Forrás:** Termelői meeting + 46 MASTER MD-k aggregálása
