# Füstölt Fehér Karaj

```yaml
# ─── SCHEMA-COMPLIANT FIELDS (kerülnek a JSON-ba) ──────────
id: fustolt_feher_karaj
category: fustolt_aruk
image: fustolt_feher_karaj.webp

product_type: weight
unit: kg
price: 49.0

is_available: true
popularity_score: 100
internal_code: "949"


# ─── DH-173 OPTIONS (v1.2 — bound to _options.yaml) ──────────
option_ids: [szeletes]
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
- **HU:** Füstölt Fehér Karaj
- **RO:** Cotlet porc afumat
## Leírás
- **HU:** Enyhén füstölt fehér karaj, sovány és aromás, szendvicsbe vagy hideg tálra.
- **RO:** Cotlet alb ușor afumat, slab și aromat, pentru sandvișuri sau platouri reci.
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
- **2026-05-07** — Schema v1.1 migráció — `internal_code: 949` hozzáadva, opciók (DH-173) MD-only-ban rögzítve, termelői meeting-info bedolgozva
- **2026-04-01** — (archív, pre-v1.0)
