# Sertés Őrölt Hús

```yaml
# ─── SCHEMA-COMPLIANT FIELDS (kerülnek a JSON-ba) ──────────
id: sertes_orolt_hus
category: friss_serteshus
image: sertes_orolt_hus.webp

product_type: weight
unit: kg
price: 21.0

is_available: true
popularity_score: 100
internal_code: "902"


# ─── DH-173 OPTIONS (v1.2 — bound to _options.yaml) ──────────
option_ids: [zsirossag]

# ─── MD-ONLY METADATA (NEM kerül JSON-ba) ──────────
last_updated: 2026-05-07
sources: ['meeting-2026-05-07', 'internal-printout-2026-05-07']
```

## Név
- **HU:** Sertés Őrölt Hús
- **RO:** Carne tocată porc
## Leírás
- **HU:** Frissen darált sertéshús, kolbászkészítéshez, fasírthoz és töltött ételekhez.
- **RO:** Carne de porc tocată proaspătă, pentru cârnați, chiftele și mâncăruri umplute.
---

> **Az alábbi szekciók CSAK az MD-ben élnek — a build.py NEM exportálja őket a JSON-ba.**
## Felhasználás (MD-only)
- **HU:** Kolbász, Fasírt, Bolognai alap
- **RO:** Cârnați, Chiftele, Bază pentru Bolognese
## Opciók (MD-only — DH-173 forward-looking, Sprint 4)

### Zsírosság
*ID:* `zsirossag` · *Type:* `single_select` · *Required:* false · *Default:* `normal` · *RO:* Conținut de grăsime

| ID | HU | RO | Megjegyzés |
|----|------|------|------------|
| kevesbe_zsiros | Kevésbé zsíros | Mai slab | Bolognai, ragú |
| normal | Normál | Normal | Alapértelmezett, fele-fele |
| zsirosabb | Zsírosabb | Mai gras | Fasírt, töltelékes káposzta |
## Termelői megjegyzések (MD-only)

> **2026-05-07 — termelői meeting (Mikado) + 2026-05-07 termelői tisztázás:**
> **Egyelőre nem lehet választani**, hogy miből legyen őrölve (alapanyag opció kivéve). Csak a **zsírosság** opció él. Az ár fix 21 RON. UX: a zsírosság opció alá szöveges magyarázat („zsírosabból sütöd a fasírtot, kevésbé zsírosból a bolognait, ragút"). Az eladó (Anna Mari) magyarázza a vásárlóknak. Megnyitva: ha a jövőben elérhető lesz alapanyag-választás, könnyen visszahozható az opció.
## History (MD-only)
- **2026-05-07 (delután)** — `alapanyag` opció ELTÁVOLÍTVA (termelő tisztázása: egyelőre nincs választás miből legyen őrölve, csak zsírosság). MD-only marad a v1.1 schema-ban — opció vissza-hozható később.
- **2026-05-07** — Schema v1.1 migráció — `internal_code: 902` hozzáadva, opciók (DH-173) MD-only-ban rögzítve, termelői meeting-info bedolgozva
- **2026-04-01** — (archív, pre-v1.0)
