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
