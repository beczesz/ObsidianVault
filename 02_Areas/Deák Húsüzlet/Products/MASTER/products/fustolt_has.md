---
title: "Füstölt Has"
date: 2026-05-09
author: Becze Szabolcs
status: active
description: "Füstölt sertéshasrész termék: 47 €/kg, elérhető, vékony-vastag közötti vastagság és pácolási opciókkal (hagyományos vagy barbecue). Bükkfa fűrészporral füstölt, leves és sütéshez ajánlott."
description_source: auto
description_hash: b69ad78f5a644ad1
id: f43b939a-09e7-40d0-96ea-8fa230072145
index_schema_version: 1
bdos_index: true
---
# Füstölt Has

```yaml
# ─── SCHEMA-COMPLIANT FIELDS (kerülnek a JSON-ba) ──────────
id: fustolt_has
category: fustolt_aruk
image: fustolt_has.webp

product_type: weight
unit: kg
price: 47.0

is_available: true
popularity_score: 100
internal_code: "946"


# ─── DH-173 OPTIONS (v1.2 — bound to _options.yaml) ──────────
option_ids: [szeletes, pacolas]

# ─── MD-ONLY METADATA (NEM kerül JSON-ba) ──────────
last_updated: 2026-05-07
sources: ['meeting-2026-05-07', 'internal-printout-2026-05-07']
```

## Név
- **HU:** Füstölt Has
- **RO:** Piept porc afumat
## Leírás
- **HU:** Füstölt hasrész, ízgazdag és zsíros, babos ételekhez és káposztás fogásokhoz ideális.
- **RO:** Burtă afumată, bogată în gust și grasă, ideală pentru fasole și mâncăruri cu varză.
---

> **Az alábbi szekciók CSAK az MD-ben élnek — a build.py NEM exportálja őket a JSON-ba.**
## Opciók (MD-only — DH-173 forward-looking, Sprint 4)

### Vastagság
*ID:* `vastagsag` · *Type:* `single_select` · *Required:* false · *Default:* `kozepes` · *RO:* Grosime

| ID | HU | RO | Megjegyzés |
|----|------|------|------------|
| vekony | Vékony | Subțire | 2 mm |
| kozepes | Közepes | Mediu | 4 mm |
| vastag | Vastag | Gros | 6 mm |

### Pácolás
*ID:* `pacolas` · *Type:* `single_select` · *Required:* false · *Default:* `nem_pacolt` · *RO:* Marinare

| ID | HU | RO | Megjegyzés |
|----|------|------|------------|
| nem_pacolt | Pácolatlan | Nemarinate | — |
| hagyomanyos | Pácolt — Hagyományos | Marinat — Tradițional | Só, bors, fokhagyma |
| barbecue | Pácolt — Barbecue | Marinat — Barbecue | Paradicsomos, BBQ-szerű |
## Termelői megjegyzések (MD-only)

> **2026-05-07 — termelői meeting (Mikado):**
> „Bükkfa fűrészporral füstölt". Felhasználás: leves, lerben sütés, káposztához (NEM grill).
## History (MD-only)
- **2026-05-07** — Schema v1.1 migráció — `internal_code: 946` hozzáadva, opciók (DH-173) MD-only-ban rögzítve, termelői meeting-info bedolgozva
- **2026-04-01** — (archív, pre-v1.0)
