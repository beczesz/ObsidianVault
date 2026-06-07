---
title: "Sertés Szalámi"
date: 2026-05-09
author: Becze Szabolcs
status: active
description: "Tradicionálisan érlelt sertésszalámi termékleírás vékonyra szeletelhető verzióban; magában foglalja az árképzést, készletállapotot és vastagság opciót a product management számára."
description_source: auto
description_hash: 6cec14f1978a10d8
id: 54ed6ca3-23ff-46eb-ab52-bc28ef254f87
index_schema_version: 1
bdos_index: true
---
# Sertés Szalámi

```yaml
# ─── SCHEMA-COMPLIANT FIELDS (kerülnek a JSON-ba) ──────────
id: sertes_szalami
category: kolbasz_szalami
image: sertes_szalami.webp

product_type: weight
unit: kg
price: 43.0

is_available: true
popularity_score: 100
internal_code: "917"


# ─── DH-173 OPTIONS (v1.2 — bound to _options.yaml) ──────────
option_ids: [szeletes]

# ─── MD-ONLY METADATA (NEM kerül JSON-ba) ──────────
last_updated: 2026-05-07
sources: ['meeting-2026-05-07', 'internal-printout-2026-05-07']
```

## Név
- **HU:** Sertés Szalámi
- **RO:** Salam de porc
## Leírás
- **HU:** Tradicionálisan érlelt sertésszalámi, karakteres ízzel, vékonyra szeletelve tálalható.
- **RO:** Salam de porc maturat tradițional, cu gust caracteristic, servit feliat subțire.
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
## History (MD-only)
- **2026-05-07** — Schema v1.1 migráció — `internal_code: 917` hozzáadva, opciók (DH-173) MD-only-ban rögzítve, termelői meeting-info bedolgozva
- **2026-04-01** — (archív, pre-v1.0)
