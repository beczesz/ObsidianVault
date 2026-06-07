---
title: "Füstölt Csülök"
date: 2026-05-09
author: Becze Szabolcs
status: active
description: "Smoked pork knuckle product entry with size options ranging from 1.2 to 1.9 kg, priced at 34.0 per kg, with Hungarian and Romanian descriptions for a hybrid retail product catalog."
description_source: auto
description_hash: 28ff0f69a5a9e326
id: 8a24ce34-4e4c-42a5-8aa1-cabad8cbab59
index_schema_version: 1
bdos_index: true
---
# Füstölt Csülök

```yaml
# ─── SCHEMA-COMPLIANT FIELDS (kerülnek a JSON-ba) ──────────
id: fustolt_csulok
category: fustolt_aruk
image: fustolt_csulok.webp

product_type: hybrid
unit: kg
price: 34.0
estimated_weight_per_piece: 1.5
weight_range_min: 1.2
weight_range_max: 1.8

is_available: true
popularity_score: 100
internal_code: "945"


# ─── DH-173 OPTIONS (v1.2 — bound to _options.yaml) ──────────
option_ids: [meret]
option_value_overrides:
  meret:
    kisebb: { meta_hint_hu: "1,2-1,5 kg", meta_hint_ro: "1,2-1,5 kg", weight_range_min: 1.2, weight_range_max: 1.5 }
    kozepes: { meta_hint_hu: "1,5-1,7 kg · alapértelmezett", meta_hint_ro: "1,5-1,7 kg · standard", weight_range_min: 1.5, weight_range_max: 1.7 }
    nagyobb: { meta_hint_hu: "1,7-1,9 kg", meta_hint_ro: "1,7-1,9 kg", weight_range_min: 1.7, weight_range_max: 1.9 }

# ─── MD-ONLY METADATA (NEM kerül JSON-ba) ──────────
last_updated: 2026-05-07
sources: ['meeting-2026-05-07', 'internal-printout-2026-05-07']
```

## Név
- **HU:** Füstölt Csülök
- **RO:** Ciolan porc afumat
## Leírás
- **HU:** Csontján füstölt csülök, mélyen átitatott füstös ízzel, főzve vagy sütve omlós.
- **RO:** Ciolan afumat pe os, cu aromă profundă de fum, fraged la fiert sau la cuptor.
## Megjegyzés
- **HU:** Darab — kb. 1.5 kg
- **RO:** Bucată — aprox. 1.5 kg
---

> **Az alábbi szekciók CSAK az MD-ben élnek — a build.py NEM exportálja őket a JSON-ba.**
## Opciók (MD-only — DH-173 forward-looking, Sprint 4)

### Méret
*ID:* `meret` · *Type:* `single_select` · *Required:* false · *Default:* `kozepes` · *RO:* Mărime

| ID | HU | RO | Megjegyzés |
|----|------|------|------------|
| kisebb | Kisebb | Mai mic | — |
| kozepes | Közepes | Mediu | — |
| nagyobb | Nagyobb | Mai mare | — |
## History (MD-only)
- **2026-05-07** — Schema v1.1 migráció — `internal_code: 945` hozzáadva, opciók (DH-173) MD-only-ban rögzítve, termelői meeting-info bedolgozva
- **2026-04-01** — (archív, pre-v1.0)
