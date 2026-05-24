# Sertés Hasrész Csontnélkül

```yaml
# ─── SCHEMA-COMPLIANT FIELDS (kerülnek a JSON-ba) ──────────
id: sertes_hasresz_csont_nelkul
category: friss_serteshus
image: sertes_hasresz.webp

product_type: weight
unit: kg
price: 26.0

is_available: true
popularity_score: 100
internal_code: "019"


# ─── DH-173 OPTIONS (v1.2 — bound to _options.yaml) ──────────
option_ids: [szeletes, pacolas]
option_value_overrides:
  szeletes:
    vekony: { meta_hint_hu: "1,5 cm", meta_hint_ro: "1,5 cm" }
    normal: { meta_hint_hu: "2 cm", meta_hint_ro: "2 cm" }
    vastagabb: { meta_hint_hu: "3 cm", meta_hint_ro: "3 cm" }

# ─── MD-ONLY METADATA (NEM kerül JSON-ba) ──────────
last_updated: 2026-05-07
sources: ['meeting-2026-05-07', 'internal-printout-2026-05-07']
```

## Név
- **HU:** Sertés Hasrész Csontnélkül
- **RO:** Piept porc fără os
## Leírás
- **HU:** Bőrös, csontnélküli hasrész — szeletelve, pácolva is kérhető. Grill, lerben kisütés ideális.
- **RO:** Piept de porc cu piele, fără os — disponibil feliat și marinat. Ideal pentru grătar și cuptor.
---

> **Az alábbi szekciók CSAK az MD-ben élnek — a build.py NEM exportálja őket a JSON-ba.**
## Opciók (MD-only — DH-173 forward-looking, Sprint 4)

### Szeletelés
*ID:* `szeletes` · *Type:* `single_select` · *Required:* false · *Default:* `egesz` · *RO:* Tăiere

| ID | HU | RO | Megjegyzés |
|----|------|------|------------|
| egesz | Egész | Întreg | — |
| szeletelt | Szeletelt | Feliat | — |

### Pácolás
*ID:* `pacolas` · *Type:* `single_select` · *Required:* false · *Default:* `nem_pacolt` · *RO:* Marinare

| ID | HU | RO | Megjegyzés |
|----|------|------|------------|
| nem_pacolt | Pácolatlan | Nemarinate | — |
| hagyomanyos | Pácolt — Hagyományos | Marinat — Tradițional | Só, bors, fokhagyma |
| barbecue | Pácolt — Barbecue | Marinat — Barbecue | Paradicsomos, BBQ-szerű |
## Termelői megjegyzések (MD-only)

> **2026-05-07 — termelői meeting (Mikado):**
> Bőr van rajta, csont nincs. Felhasználás: grill, lerben kisütni („hasonló mint a nyakas karaj").
## History (MD-only)
- **2026-05-07** — ÚJ termék — felvéve a Sheet „Új termékek" + belső printout alapján (kód: `019`)
- **2026-04-01** — (archív, pre-v1.0)
