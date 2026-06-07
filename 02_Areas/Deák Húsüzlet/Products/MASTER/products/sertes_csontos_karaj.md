---
title: "Sertés fehérkaraj csontos szalonnás"
date: 2026-05-09
author: Becze Szabolcs
status: active
description: "Csontján hagyott sertéskaraj szalonnával, 1,5 kg-os darabban, grillezéshez vagy sütőbe való, pácolási opciókkal."
description_source: auto
description_hash: 8534db77800aa95e
id: 8cadd428-ccc9-424c-829f-f95fb49ee818
index_schema_version: 1
bdos_index: true
---
# Sertés fehérkaraj csontos szalonnás

```yaml
# ─── SCHEMA-COMPLIANT FIELDS (kerülnek a JSON-ba) ──────────
id: sertes_csontos_karaj
category: friss_serteshus
image: sertes_csontos_karaj.webp

product_type: hybrid
unit: kg
price: 25.5
estimated_weight_per_piece: 1.5
weight_range_min: 1.2
weight_range_max: 1.8

is_available: true
popularity_score: 100
internal_code: "016"


# ─── DH-173 OPTIONS (v1.2 — bound to _options.yaml) ──────────
option_ids: [pacolas]

# ─── MD-ONLY METADATA (NEM kerül JSON-ba) ──────────
last_updated: 2026-05-07
sources: ['meeting-2026-05-07', 'internal-printout-2026-05-07']
```

## Név
- **HU:** Sertés fehérkaraj csontos szalonnás
- **RO:** Cotlet porc cu os și slănină
## Leírás
- **HU:** Csontján hagyott karajszelet, saftos és ízletes, grillezéshez vagy sütőbe.
- **RO:** Cotlet cu os, suculent și gustos, perfect pe grătar sau la cuptor.
## Megjegyzés
- **HU:** Darab — kb. 1.5 kg-os
- **RO:** Bucată — aprox. 1.5 kg
---

> **Az alábbi szekciók CSAK az MD-ben élnek — a build.py NEM exportálja őket a JSON-ba.**
## Felhasználás (MD-only)
- **HU:** Steak
- **RO:** Steak
## Opciók (MD-only — DH-173 forward-looking, Sprint 4)

### Pácolás
*ID:* `pacolas` · *Type:* `single_select` · *Required:* false · *Default:* `nem_pacolt` · *RO:* Marinare

| ID | HU | RO | Megjegyzés |
|----|------|------|------------|
| nem_pacolt | Pácolatlan | Nemarinate | — |
| hagyomanyos | Pácolt — Hagyományos | Marinat — Tradițional | Só, bors, fokhagyma |
| barbecue | Pácolt — Barbecue | Marinat — Barbecue | Paradicsomos, BBQ-szerű |
## Termelői megjegyzések (MD-only)

> **2026-05-07 — termelői meeting (Mikado):**
> Szeletelve adják alapból, csonton hagyva (BBQ-hoz). Vastagság-variáció NINCS („ahogy fogja adni a borda"). Felhasználás: bárbekű, grillezés.
## History (MD-only)
- **2026-05-07** — Schema v1.1 migráció — `internal_code: 016` hozzáadva, opciók (DH-173) MD-only-ban rögzítve, termelői meeting-info bedolgozva
- **2026-04-01** — (archív, pre-v1.0)
