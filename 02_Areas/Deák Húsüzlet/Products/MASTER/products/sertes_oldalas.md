---
title: "Sertés Oldalas"
date: 2026-05-09
author: Becze Szabolcs
status: active
description: "Sertés oldalas termék metadata: csontos sertéshús, 26 Ft/kg, szeletelés és pácolás opciókkal (hagyományos vagy BBQ). Termékkatalógus szerkesztőknek és elektronikus rendszerre exportáláshoz."
description_source: auto
description_hash: 48cf3c8531d3dd24
id: ebc0d804-9fe7-434c-a0cd-5bf86495f6a0
index_schema_version: 1
bdos_index: true
---
# Sertés Oldalas

```yaml
# ─── SCHEMA-COMPLIANT FIELDS (kerülnek a JSON-ba) ──────────
id: sertes_oldalas
category: friss_serteshus
image: sertes_hasresz.webp

product_type: weight
unit: kg
price: 26.0

is_available: true
popularity_score: 100
internal_code: "020"


# ─── DH-173 OPTIONS (v1.2 — bound to _options.yaml) ──────────
option_ids: [szeletes, pacolas]
option_value_overrides:
  szeletes:
    vekony: { meta_hint_hu: "1,5 cm", meta_hint_ro: "1,5 cm" }
    normal: { meta_hint_hu: "2 cm", meta_hint_ro: "2 cm" }
    vastagabb: { meta_hint_hu: "3 cm", meta_hint_ro: "3 cm" }

# ─── MD-ONLY METADATA (NEM kerül JSON-ba) ──────────
last_updated: 2026-05-07
sources: ['meeting-2026-05-07', 'internal-printout-2026-05-07']
```

## Név
- **HU:** Sertés Oldalas
- **RO:** Costiță
## Leírás
- **HU:** Csontos sertés oldalas, bőr nélkül — szeletelve és pácolva kérhető. Grillezésre, lerbe sütésre ideális.
- **RO:** Costiță de porc cu os, fără piele — disponibilă feliată și marinată. Ideală pentru grătar și cuptor.
---

> **Az alábbi szekciók CSAK az MD-ben élnek — a build.py NEM exportálja őket a JSON-ba.**
## Opciók (MD-only — DH-173 forward-looking, Sprint 4)

### Szeletelés
*ID:* `szeletes` · *Type:* `single_select` · *Required:* false · *Default:* `egesz` · *RO:* Tăiere

| ID | HU | RO | Megjegyzés |
|----|------|------|------------|
| egesz | Egész | Întreg | — |
| szeletelt | Szeletelt | Feliat | — |

### Pácolás
*ID:* `pacolas` · *Type:* `single_select` · *Required:* false · *Default:* `nem_pacolt` · *RO:* Marinare

| ID | HU | RO | Megjegyzés |
|----|------|------|------------|
| nem_pacolt | Pácolatlan | Nemarinate | — |
| hagyomanyos | Pácolt — Hagyományos | Marinat — Tradițional | Só, bors, fokhagyma |
| barbecue | Pácolt — Barbecue | Marinat — Barbecue | Paradicsomos, BBQ-szerű |
## Termelői megjegyzések (MD-only)

> **2026-05-07 — termelői meeting (Mikado):**
> Csont van rajta, bőr nincs. Román nevén „kosztica" (costiță).
## History (MD-only)
- **2026-05-07** — ÚJ termék — felvéve a Sheet „Új termékek" + belső printout alapján (kód: `020`)
- **2026-04-01** — (archív, pre-v1.0)
