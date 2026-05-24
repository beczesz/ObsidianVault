# Füstölt Csülök Csont Nélkül

```yaml
# ─── SCHEMA-COMPLIANT FIELDS (kerülnek a JSON-ba) ──────────
id: fustolt_csulok_csont_nelkul
category: fustolt_aruk
image: fustolt_csulok_csont_nelkul.webp

product_type: hybrid
unit: kg
price: 44.0
estimated_weight_per_piece: 1.2
weight_range_min: 1.0
weight_range_max: 1.5

is_available: true
popularity_score: 100
internal_code: "945.1"


# ─── DH-173 OPTIONS (v1.2 — bound to _options.yaml) ──────────
option_ids: [meret]
option_value_overrides:
  meret:
    kisebb: { meta_hint_hu: "1,0-1,2 kg", meta_hint_ro: "1,0-1,2 kg", weight_range_min: 1.0, weight_range_max: 1.2 }
    kozepes: { meta_hint_hu: "1,2-1,4 kg · alapértelmezett", meta_hint_ro: "1,2-1,4 kg · standard", weight_range_min: 1.2, weight_range_max: 1.4 }
    nagyobb: { meta_hint_hu: "1,4-1,5 kg", meta_hint_ro: "1,4-1,5 kg", weight_range_min: 1.4, weight_range_max: 1.5 }

# ─── MD-ONLY METADATA (NEM kerül JSON-ba) ──────────
last_updated: 2026-05-07
sources: ['meeting-2026-05-07', 'internal-printout-2026-05-07']
```

## Név
- **HU:** Füstölt Csülök Csont Nélkül
- **RO:** Ciolan porc afumat fără os
## Leírás
- **HU:** Kicsontozott füstölt csülök, kényelmes szeletelésre, hideg tálakhoz vagy melegítve.
- **RO:** Ciolan afumat dezos, comod de feliat, pentru platouri reci sau reîncălzit.
## Megjegyzés
- **HU:** Darab — kb. 1.2 kg (belső név: „Csemege Csülök")
- **RO:** Bucată — aprox. 1.2 kg
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
## Termelői megjegyzések (MD-only)

> **2026-05-07 — termelői meeting (Mikado):**
> Belső termelői név: „Csemege Csülök" (kód 945.1). Csont kivéve.
## History (MD-only)
- **2026-05-07** — Schema v1.1 migráció — `internal_code: 945.1` hozzáadva, opciók (DH-173) MD-only-ban rögzítve, termelői meeting-info bedolgozva
- **2026-04-01** — (archív, pre-v1.0)
