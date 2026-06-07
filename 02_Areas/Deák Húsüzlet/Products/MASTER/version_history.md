---
title: "Products Master — Version History"
date: 2026-05-09
author: Becze Szabolcs
status: active
description: "Detailed changelog tracking schema and product data versions for a meat product catalog system, documenting the evolution from v1.0 through current v1.2 with variation group support, internal codes, and product option specifications for a butcher shop inventory system."
description_source: auto
description_hash: f2b2488d24b562a4
id: e5206fd6-914d-4c3a-8571-2ec3ca3b64ae
index_schema_version: 1
bdos_index: true
---
# Products Master — Version History

> **Forrás:** `Products/MASTER/products/*.md` (egy fájl per termék)
> **Schema:** `Products/MASTER/_schema-v1.1.json`
> **Generated:** `Products/generated/products-v1.1.json`
> **Élő deploy:** `https://deakhus.netlify.app/data/products-v1.1.json`

## Verziózási szabályok

- **Schema verzió** (`_schema-vX.Y.json`) — csak struktúra-változásnál bump (új mező, új validáció, új opció-típus). Adatváltozás NEM bump.
- **Products data verzió** (`products-vX.Y.json`) — minden release-nél bump (1.0 → 1.1 → 1.2…).
- **MD master** — git-alapú verzióhistória (nincs külön snapshot folder).

> **Megjegyzés:** A products versioning **2026-05-07-én újraindult v1.0-tól**, mostantól Frappe DocType-aligned. A korábbi 3.x sorozat **archív** és a `Products/legacy/` mappában található.

## Release Log

### v1.2 — 2026-05-09 (CURRENT, READY TO DEPLOY)

**Schema:** v1.2 (új `options[]` array a product-ban — DH-173 VG támogatás)
**Termékszám:** 46 (15 termék VG-opcióval)

**Változások:**
- **DH-173 VG (Variation Group) bevezetve** — az `## Opciók` MD-only szekció helyett a JSON-ban élő `options[]` array
- **Új master fájl:** `MASTER/_options.yaml` — az 5 opció-típus (Pácolás, Szeletelés-forma, Szeletelés, Méret, Zsírosság) egy helyen definiálva
- **Termék MD frontmatter bővítés:** `option_ids: [...]` lista + opcionális `option_value_overrides:` per-termék override-okhoz (pl. méret kg-tartomány, szeletelés mm)
- **build.py update:** v1.2 schema default + `_options.yaml` integráció + override merge
- **2 VG-fajta:** OPTIONAL (checkbox + opt-in) és MANDATORY (mindig látható, default kiválasztva)
- **Pricing modifier:** Pácolás +2 RON/kg (price_modifier mező új a values-ben, többi opció ingyenes)
- **OFF-equivalens drop:** Pácolatlan és Egészben értékek nem külön opció-érték (OFF = ezek)

**Termékek VG-vel (15):**
- Forma: 014 nyakaskaraj
- Méret MANDATORY: 007, 945, 945.1 (csülök-félék, kg-tartomány termékenként)
- Zsírosság MANDATORY: 902 (őrölt hús)
- Pácolás: 014, 015, 016, 019, 020, 946 (6 termék)
- Szeletelés: 015, 019, 020, 917, 946, 948, 949, 991, 9904 (9 termék, mm-érték termékenként)

**Spec:** `Business Development/pilot-husuzlet/product-variations/vg-content-spec-v1.0.md` v1.2
**Wireframe:** `design/screen-catalog/screens/v0.4-product-variations.html`

### v1.1 — 2026-05-07 (REPLACED by v1.2)

**Schema:** v1.1 (új `internal_code` mező)
**Termékszám:** 46

**Változások:**
- Új `internal_code` mező a Baczo Annamaria Sziget belső kódrendszerhez (45/46 terméken)
- Új kategória: `friss_csirkehus` (3 termék)
- Hasrész 3-féle bontás: `sertes_hasresz`, `sertes_hasresz_csont_nelkul`, `sertes_oldalas`
- 7 új termék: csirke szárny/egybe comb/mell, Sertés Lapocka, Sajtos Cérna Kolbász, Tepertőnek való szalonna (seasonal: summer), Roppanós Virsli
- Átnevezések: Növendék Szalámi → Házi szalámi, Sertés Comb → Sertés comb csontnélkül, Sertés Fehér Karaj → Sertés fehérkaraj csontnélkül, Nyakas Karaj → Sertés nyakaskaraj
- Termelői meeting (43 perces) info bedolgozva opciókba (DH-173 forward-looking, MD-only)
- Forrás-fájlok: `Products/meetings/` (transcript, decisions, internal-codes, unified-master)

### v1.0 — 2026-05-07 (REPLACED by v1.1 ugyanaznap)

**Schema:** v1.0 (eredeti Frappe-aligned referencia)
**Termékszám:** 1 (Sertés Csülök proba)

**Megjegyzés:** v1.0 csak proba deploy volt 1 termékkel — a pipeline validálására. Élesben sosem volt 1 napnál tovább. Lecserélve v1.1-re ugyanaznap, miután a 46 termék összeállt.

---

## 📁 Pre-v1.0 archív (lásd `Products/legacy/`)

> A korábbi 3.x sorozat NEM része a jelenlegi rendszernek. Csak referenciaként archivált.

- **3.x sorozat (2026-03 — 2026-05-07 reggel)** — Eredeti Google Sheet-alapú JSON. 37 termék. Ez volt az MVP induláskor használt struktúra. Replaced by v1.0+.

A pontos archív fájlok és magyarázat: `Products/legacy/README.md`.
