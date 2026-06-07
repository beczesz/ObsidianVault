---
title: "Házi szalámi"
date: 2026-05-09
author: Becze Szabolcs
status: active
description: "Háztartási szalámi termékadatlap, amely a finomszemcsés, enyhén fűszerezett szalámi árát, elérhetőségét és vastagság-opciót tartalmazza szendvicsek és hideg tálak készítéséhez."
description_source: auto
description_hash: 97b0db2448ce5b65
id: 87d4d817-2f5f-4153-85f1-9ecd82f4ca11
index_schema_version: 1
bdos_index: true
---
# Házi szalámi

```yaml
# ─── SCHEMA-COMPLIANT FIELDS (kerülnek a JSON-ba) ──────────
id: novendek_szalami
category: kolbasz_szalami
image: novendek_szalami.webp

product_type: weight
unit: kg
price: 46.0

is_available: true
popularity_score: 100
internal_code: "991"


# ─── DH-173 OPTIONS (v1.2 — bound to _options.yaml) ──────────
option_ids: [szeletes]

# ─── MD-ONLY METADATA (NEM kerül JSON-ba) ──────────
last_updated: 2026-05-07
sources: ['meeting-2026-05-07', 'internal-printout-2026-05-07']
```

## Név
- **HU:** Házi szalámi
- **RO:** Salam de casă
## Leírás
- **HU:** Finomszemcsés, enyhén fűszerezett szalámi, hideg tálak és szendvicsek kedvelt alapanyaga.
- **RO:** Salam fin, ușor condimentat, ingredient preferat pentru platouri reci și sandvișuri.
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
## Termelői megjegyzések (MD-only)

> **2026-05-07 — termelői meeting (Mikado):**
> Belső név (kód 991): „Száraz Házi Szalámi". UX-megjegyzés: szeleteléskor a bőr lehúzása fontos (Petriben így van).
## History (MD-only)
- **2026-05-07** — Schema v1.1 migráció — `internal_code: 991` hozzáadva, opciók (DH-173) MD-only-ban rögzítve, termelői meeting-info bedolgozva
- **2026-04-01** — (archív, pre-v1.0)
