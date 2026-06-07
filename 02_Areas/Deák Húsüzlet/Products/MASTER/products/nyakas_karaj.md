---
title: "Sertés nyakaskaraj"
date: 2026-05-09
author: Becze Szabolcs
status: active
description: "Sertés nyakaskaraj termékadat: márványos hús a nyak és karaj között, 33 Ft/kg, elérhető. Forma és pácolás opciók (sima/dupla, nem pácolt/hagyományos/barbecue) dokumentálva, fotó-stratégia megadva."
description_source: auto
description_hash: df62d8777a3b8683
id: 20cac654-46a3-4cf2-816d-2ea99be1990e
index_schema_version: 1
bdos_index: true
---
# Sertés nyakaskaraj

```yaml
# ─── SCHEMA-COMPLIANT FIELDS (kerülnek a JSON-ba) ──────────
id: nyakas_karaj
category: friss_serteshus
image: nyakas_karaj.webp

product_type: weight
unit: kg
price: 33.0

is_available: true
popularity_score: 100
internal_code: "014"


# ─── DH-173 OPTIONS (v1.2 — bound to _options.yaml) ──────────
option_ids: [forma, pacolas]

# ─── MD-ONLY METADATA (NEM kerül JSON-ba) ──────────
last_updated: 2026-05-07
sources: ['meeting-2026-05-07', 'internal-printout-2026-05-07']
```

## Név
- **HU:** Sertés nyakaskaraj
- **RO:** Ceafă porc
## Leírás
- **HU:** A nyak és a karaj közötti márványos rész, kiváló sütéshez és pároláshoz.
- **RO:** Bucată marmorată între gât și cotlet, excelentă la prăjit și înăbușit.
---

> **Az alábbi szekciók CSAK az MD-ben élnek — a build.py NEM exportálja őket a JSON-ba.**
## Felhasználás (MD-only)
- **HU:** Flekken, Lesi-pecsi
- **RO:** Flekken, Lesi-pecsi
## Opciók (MD-only — DH-173 forward-looking, Sprint 4)

### Forma
*ID:* `forma` · *Type:* `single_select` · *Required:* false · *Default:* `sima` · *RO:* Formă

| ID | HU | RO | Megjegyzés |
|----|------|------|------------|
| sima | Sima | Simplă | Vékony szelet, minimum újnyi vastag (vékonyabb cipőtalp érzet) |
| dupla | Dupla | Dublă | Két szelet középen egyben, kinyitva, potyolva — férfias, nagyobb |

### Pácolás
*ID:* `pacolas` · *Type:* `single_select` · *Required:* false · *Default:* `nem_pacolt` · *RO:* Marinare

| ID | HU | RO | Megjegyzés |
|----|------|------|------------|
| nem_pacolt | Pácolatlan | Nemarinate | — |
| hagyomanyos | Pácolt — Hagyományos | Marinat — Tradițional | Só, bors, fokhagyma |
| barbecue | Pácolt — Barbecue | Marinat — Barbecue | Paradicsomos, BBQ-szerű |
## Termelői megjegyzések (MD-only)

> **2026-05-07 — termelői meeting (Mikado):**
> A vékonyra szeletelt nyakaskaraj „cipőtalp érzet"-et ad — minimum újnyi vastagság kell. A „dupla" forma a férfias, nagyobb verzió: két szelet középen egyben hagyva, kinyitva, potyolva. Foto-stratégia: minden variációhoz külön fotó (sima/dupla, pácolt/nem pácolt), háttér: zöld + piros zöldség.
## History (MD-only)
- **2026-05-07** — Schema v1.1 migráció — `internal_code: 014` hozzáadva, opciók (DH-173) MD-only-ban rögzítve, termelői meeting-info bedolgozva
- **2026-04-01** — (archív, pre-v1.0)
