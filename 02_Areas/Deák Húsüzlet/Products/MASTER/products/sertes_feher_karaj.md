---
title: "Sertés fehérkaraj csontnélkül"
date: 2026-05-09
author: Becze Szabolcs
status: active
description: "Boneless pork loin chop product record with weight-based pricing, slicing and marinating options, and producer notes on suitability for Wiener schnitzel and similar preparations."
description_source: auto
description_hash: ff68f895a8493c71
id: 0d18b60e-b7d4-4b68-bea1-a928480b84f8
index_schema_version: 1
bdos_index: true
---
# Sertés fehérkaraj csontnélkül

```yaml
# ─── SCHEMA-COMPLIANT FIELDS (kerülnek a JSON-ba) ──────────
id: sertes_feher_karaj
category: friss_serteshus
image: sertes_feher_karaj.webp

product_type: weight
unit: kg
price: 33.0

is_available: true
popularity_score: 100
internal_code: "015"


# ─── DH-173 OPTIONS (v1.2 — bound to _options.yaml) ──────────
option_ids: [szeletes, pacolas]
option_value_overrides:
  szeletes:
    vekony: { meta_hint_hu: "1 cm", meta_hint_ro: "1 cm" }
    normal: { meta_hint_hu: "1,5 cm", meta_hint_ro: "1,5 cm" }
    vastagabb: { meta_hint_hu: "2,5 cm", meta_hint_ro: "2,5 cm" }

# ─── MD-ONLY METADATA (NEM kerül JSON-ba) ──────────
last_updated: 2026-05-07
sources: ['meeting-2026-05-07', 'internal-printout-2026-05-07']
```

## Név
- **HU:** Sertés fehérkaraj csontnélkül
- **RO:** Cotlet porc fără os
## Leírás
- **HU:** Zsírszegény, egyenletes húsú karajdarab, könnyen szeletelhető sütéshez.
- **RO:** Cotlet slab cu carne uniformă, ușor de feliat pentru prăjit.
---

> **Az alábbi szekciók CSAK az MD-ben élnek — a build.py NEM exportálja őket a JSON-ba.**
## Felhasználás (MD-only)
- **HU:** Szeletek
- **RO:** Felii
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
> „Szeletnek való" — Bécsi szelet, flekken (sovány szereti). Pörköltnek nem ideális. Csontnélküli, szalonna nélküli verzió.
## History (MD-only)
- **2026-05-07** — Schema v1.1 migráció — `internal_code: 015` hozzáadva, opciók (DH-173) MD-only-ban rögzítve, termelői meeting-info bedolgozva
- **2026-04-01** — (archív, pre-v1.0)
