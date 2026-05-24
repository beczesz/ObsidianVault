# Sertés Csülök

```yaml
# ─── SCHEMA-COMPLIANT FIELDS (kerülnek a JSON-ba) ──────────
id: sertes_csulok
category: friss_serteshus
image: sertes_csulok.webp

product_type: hybrid
unit: kg
price: 19.0
estimated_weight_per_piece: 1.5
weight_range_min: 1.2
weight_range_max: 1.8

is_available: true
popularity_score: 100
internal_code: "007"


# ─── DH-173 OPTIONS (v1.2 — bound to _options.yaml) ──────────
option_ids: [meret]
option_value_overrides:
  meret:
    kisebb: { meta_hint_hu: "1,2-1,4 kg", meta_hint_ro: "1,2-1,4 kg", weight_range_min: 1.2, weight_range_max: 1.4 }
    kozepes: { meta_hint_hu: "1,4-1,6 kg · alapértelmezett", meta_hint_ro: "1,4-1,6 kg · standard", weight_range_min: 1.4, weight_range_max: 1.6 }
    nagyobb: { meta_hint_hu: "1,6-1,8 kg", meta_hint_ro: "1,6-1,8 kg", weight_range_min: 1.6, weight_range_max: 1.8 }

# ─── MD-ONLY METADATA (NEM kerül JSON-ba) ──────────
last_updated: 2026-05-07
sources: ['meeting-2026-05-07', 'internal-printout-2026-05-07']
```

## Név
- **HU:** Sertés Csülök
- **RO:** Ciolan porc
## Leírás
- **HU:** Kollagénben gazdag friss csülök, párolt fogásokhoz és húsleveshez ideális.
- **RO:** Ciolan proaspăt bogat în colagen, ideal pentru mâncăruri înăbușite și supă de carne.
## Megjegyzés
- **HU:** Darab — kb. 1.5 kg-os, ±10% utólagos súlykorrekció
- **RO:** Bucată — aprox. 1.5 kg, posibilă corecție de greutate ±10%
---

> **Az alábbi szekciók CSAK az MD-ben élnek — a build.py NEM exportálja őket a JSON-ba.**
## Felhasználás (MD-only)
- **HU:** Lerbe sült csülök, Pörkölt
- **RO:** Ciolan la cuptor, Tocană
## Opciók (MD-only — DH-173 forward-looking, Sprint 4)

### Méret
*ID:* `meret` · *Type:* `single_select` · *Required:* false · *Default:* `kozepes` · *RO:* Mărime

| ID | HU | RO | Megjegyzés |
|----|------|------|------------|
| kisebb | Kisebb | Mai mic | 1.2-1.4 kg |
| kozepes | Közepes | Mediu | 1.4-1.6 kg |
| nagyobb | Nagyobb | Mai mare | 1.6-1.8 kg |
## Termelői megjegyzések (MD-only)

> **2026-05-07 — termelői meeting (Mikado):**
> Méret-eltérés ~10-30 deka. Vásárlók kérik („mama a kisebbiket szereti").
## History (MD-only)
- **2026-05-07** — Schema v1.1 migráció — `internal_code: 007` hozzáadva, opciók (DH-173) MD-only-ban rögzítve, termelői meeting-info bedolgozva
- **2026-04-01** — (archív, pre-v1.0)
