---
title: "Füstölt Nyakas Karaj"
date: 2026-05-09
author: Becze Szabolcs
status: active
description: "Füstölt nyakas karaj termékadata, márványos szerkezettel és füstös ízzel, szeletelhető vagy egész formában elérhető."
description_source: auto
description_hash: 267f17046bfa61b3
id: 1d9600a4-f86c-4a5a-9776-5c3fdf22f052
index_schema_version: 1
bdos_index: true
---
# Füstölt Nyakas Karaj

```yaml
# ─── SCHEMA-COMPLIANT FIELDS (kerülnek a JSON-ba) ──────────
id: fustolt_nyakas_karaj
category: fustolt_aruk
image: fustolt_nyakas_karaj.webp

product_type: weight
unit: kg
price: 49.0

is_available: true
popularity_score: 100
internal_code: "948"


# ─── DH-173 OPTIONS (v1.2 — bound to _options.yaml) ──────────
option_ids: [szeletes]

# ─── MD-ONLY METADATA (NEM kerül JSON-ba) ──────────
last_updated: 2026-05-07
sources: ['meeting-2026-05-07', 'internal-printout-2026-05-07']
```

## Név
- **HU:** Füstölt Nyakas Karaj
- **RO:** Ceafă porc afumat
## Leírás
- **HU:** Márványos szerkezetű füstölt nyakas karaj, gazdag füstös ízzel, hidegen és melegen is kiváló.
- **RO:** Ceafă afumată cu structură marmorată, gust bogat de fum, excelentă rece și caldă.
---

> **Az alábbi szekciók CSAK az MD-ben élnek — a build.py NEM exportálja őket a JSON-ba.**
## Opciók (MD-only — DH-173 forward-looking, Sprint 4)

### Szeletelés
*ID:* `szeletes` · *Type:* `single_select` · *Required:* false · *Default:* `szeletelt` · *RO:* Tăiere

| ID | HU | RO | Megjegyzés |
|----|------|------|------------|
| egesz | Egész | Întreg | — |
| szeletelt | Szeletelt | Feliat | — |
## Termelői megjegyzések (MD-only)

> **2026-05-07 — termelői meeting (Mikado):**
> Vastagság-variáció NEM („egy variáns elég").
## History (MD-only)
- **2026-05-07** — Schema v1.1 migráció — `internal_code: 948` hozzáadva, opciók (DH-173) MD-only-ban rögzítve, termelői meeting-info bedolgozva
- **2026-04-01** — (archív, pre-v1.0)
