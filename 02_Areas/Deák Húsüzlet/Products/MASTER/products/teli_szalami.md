# Téli Szalámi

```yaml
# ─── SCHEMA-COMPLIANT FIELDS (kerülnek a JSON-ba) ──────────
id: teli_szalami
category: kolbasz_szalami
image: teli_szalami.webp

product_type: weight
unit: kg
price: 68.0

is_available: true
popularity_score: 100
internal_code: "9904"


# ─── DH-173 OPTIONS (v1.2 — bound to _options.yaml) ──────────
option_ids: [szeletes]

# ─── MD-ONLY METADATA (NEM kerül JSON-ba) ──────────
last_updated: 2026-05-07
sources: ['meeting-2026-05-07', 'internal-printout-2026-05-07']
```

## Név
- **HU:** Téli Szalámi
- **RO:** Salam de iarnă
## Leírás
- **HU:** Hosszan érlelt, intenzív ízű téli szalámi, hideg tálak és szendvicsek klasszikusa.
- **RO:** Salam de iarnă maturat îndelung, cu gust intens, clasic al platourilor reci și sandvișurilor.
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
- **2026-05-07** — Schema v1.1 migráció — `internal_code: 9904` hozzáadva, opciók (DH-173) MD-only-ban rögzítve, termelői meeting-info bedolgozva
- **2026-04-01** — (archív, pre-v1.0)
