---
title: "Products — Master Data Workflow"
date: 2026-05-09
author: Becze Szabolcs
status: active
description: "Master product dataset for a meat supplier, containing 46 products across six categories with markdown source files, JSON schema v1.1, internal product codes, and automated build workflow for web deployment."
description_source: auto
description_hash: fa73c998fd44cc78
id: a0ad4bec-9319-4822-8193-b5936c9bda27
index_schema_version: 1
bdos_index: true
---
# Products — Master Data Workflow

> **Status:** Aktív (v1.1 / schema v1.1 — 46 termék, deploy-ready 2026-05-07)
> **Élő URL-ek (deploy után):**
> - https://deakhus.netlify.app/data/products-v1.1.json (46 termék, 6 kategória)
> - https://deakhus.netlify.app/data/_schema-v1.1.json (Frappe-aligned + internal_code)
> **Source of truth:** `Products/MASTER/products/*.md` (46 fájl)
> **Belső termékkódok forrása:** `Products/meetings/2026-05-07_internal-product-codes.md`

---



## 🎯 Kapcsolódó feature mappák

| Feature | Jira | Mappa | Státusz |
|---------|------|-------|---------|
| **Termék testreszabás (DH-173)** | [DH-173](https://exarlabs.atlassian.net/browse/DH-173) | `Business Development/pilot-husuzlet/product-variations/` | Sprint 4 — spec v1.0 kész |

Az opció-rendszer (DH-173) **MD-only mezőkben** él jelenleg a 15 termék MD-jében (`## Opciók` szekció). Sprint 4 indulásakor schema bump v1.2 → JSON exportba kerül.

## 📊 Külső referenciák (NEM source of truth — csak ellenőrzéshez)

> **Source of truth = `Products/MASTER/products/*.md` + `_schema-v1.1.json`.**
> Az alábbi források PÁRHUZAMOSAN frissülnek, de a mi MD/JSON rendszerünk a hivatalos.

| Forrás | URL / Path | Mire használjuk |
|--------|------------|------------------|
| **Google Sheet (Szabolcs jegyzetfüzete)** | https://docs.google.com/spreadsheets/d/15AJpMxf1Q6S-6o8DoiBvKMtTJ67AuJm7l6BmwItD084/edit?gid=0#gid=0 | Szabolcs ide is jegyzeteli a meeting-info-t, gyors munkanaplónak. **Bármikor át lehet nézni hogy ne legyen elcsúszás.** Ha új info van benne ami nincs az MD-ben, áthozzuk. |
| **Production backend** | Frappe Deak App (deakhus.ro / staging.deakhus.ro) | Élő rendszer adatok. Schema referenciánk innen jött (lásd `MASTER/reference/`). |
| **Termelői meetings** | `Products/meetings/` | Hangfelvétel, transcript, döntés-snapshot fájlok. |

**Sync szabály:** új info bárhonnan ered → strukturálva bekerül a master MD-be → build → deploy. A többi forrás INFORMÁLIS lehet.


## 🆕 Schema v1.1 (2026-05-07) — internal_code mező

A schema v1.0-hoz képest **egy új opcionális mező** került be:

```yaml
internal_code: "014"   # Belső termékkód a Baczo Annamaria Sziget belső listából
```

- **Pattern:** `^[A-Z0-9]{3,7}(\.[0-9]+)?$` — illeszti `014`, `0221`, `ACS04`, `945.1`, `9904`
- **Opcionális** (null megengedett, ha nincs kód — pl. `fustolt_kotozott_sonka`)
- **45/46 termék** rendelkezik kóddal (Füstölt Kötözött Sonka kivétel)

A production Frappe backend még a v1.0 schema-t használja — ha onnan importálnak, a `internal_code` mezőt ignorálja (vagy ha hozzáadjuk a backendre, szinkronban lesz).

## 📦 Aktuális termékszám: 46 darab, 6 kategóriában

| Kategória | Termékszám |
|-----------|-----------|
| Friss Sertéshús | 16 (incl. 2 hasrész split + lapocka új) |
| Friss Növendékhús | 1 (velős csont) |
| **Friss Csirkehús (ÚJ)** | 3 (szárny, egybe comb, mell csont+bőr nélkül) |
| Füstölt Áruk | 12 |
| Kolbász & Szalámi | 9 (incl. sajtos cérna + Roppanós virsli új) |
| Felvágott & Egyéb | 5 (incl. tepertő szalonna új) |
| **Összesen** | **46** |

## 🎯 Single Source of Truth (SSOT) modell

```
INPUT (nyersanyag — csak referencia)
  ├─ Hangfelvétel (meetings/*.mp3)
  ├─ Transcript (meetings/*.md)
  ├─ Google Sheet (DEPRECATED — csak read-only export)
  └─ Termelői megjegyzések, doksik

         ↓ info → strukturált adat (kézzel + AI-jal)

MASTER (single source of truth)
  └─ Products/MASTER/products/*.md   ◄── ITT SZERKESZTÜNK
      + _schema-v{version}.json
      + _categories.yaml

         ↓ build.py (deterministic)

OUTPUT (auto-generálva — NE szerkeszd!)
  └─ Products/generated/products-v{version}.json
      → másolva: design/screen-catalog/data/
      → deploy: Netlify (deakhus.netlify.app/data/)
```

**Alapszabály:** csak a MASTER MD-ket szerkesztjük. Minden más vagy ide *belekerül* (input), vagy *ebből származik* (output).

---

## 📁 Mappastruktúra

```
Products/
  CLAUDE.md                          ← ez a fájl
  (archived legacy)                 ← LEGACY (pre-v1.0 archive — Products/legacy/)
  product_listing_v0.7_*.md          ← LEGACY listings (autogen-elhető újra)
  product_photos/                    ← *.webp képek (NE TÖRÖLD)

  MASTER/                            ← KIRÁLY — itt szerkesztünk
    _schema-v1.1.json                ← JSON Schema (verziózva)
    _categories.yaml                 ← 5 kategória definíció
    version_history.md               ← release napló
    products/
      sertes_csulok.md               ← egy fájl per termék (Option C)
      [37 fájl, ahogy migráljuk]
    scripts/
      build.py                       ← MD → JSON, schema-validál

  generated/                         ← AUTO-GENERÁLT — ne szerkeszd
    products-v1.1.json
    products-(pre-v1.0 archive).json (régi build-ek)

  meetings/                          ← INPUT nyersanyag
    YYYY-MM-DD_audio.mp3
    YYYY-MM-DD_transcript.md
    YYYY-MM-DD_decisions.md          ← strukturált döntés-extrakció
```

---

## 📐 Verziózási szabályok

| Mit | Hogyan | Mikor bump |
|------|--------|------------|
| **Schema** | `_schema-v{MAJOR}.{MINOR}.json` | CSAK ha a struktúra változik (új mező, új validáció, új option-típus). MINOR adatváltozás = NEM bump. |
| **Products data** | `products-v{MAJOR}.{MINOR}.json` | MINDEN release-nél bump (3.2 → 3.3 → 3.4) |
| **MD master** | nincs verzió a fájlnévben | Git history a verzióforrás. Release-eléskor `version_history.md` napló frissül |

---

## 🧱 Termék MD formátum (Option C)

Minden termék MD így néz ki:

````markdown
# Termék Neve

```yaml
id: snake_case_id
category: friss_serteshus | friss_novendekhus | fustolt_aruk | kolbasz_szalami | felvagott_egyeb
image: snake_case_id.webp

product_type: weight | piece | hybrid
price_per_kg: 19.0
estimated_weight_per_piece: 1.5    # csak hybrid-nél
weight_range_min: 1.2               # csak hybrid-nél
weight_range_max: 1.8               # csak hybrid-nél
piece_weight_kg: null               # csak piece-nél (kg/db)
min_order_gramm: 500                # csak weight-nél

available: true
seasonal: year_round | winter | spring | summer | autumn | holiday

sources: [meeting-2026-05-07, DH-XXX]
last_updated: 2026-05-07
```

## Név
- **HU:** ...
- **RO:** ...

## Leírás
- **HU:** ...
- **RO:** ...

## Felhasználás
- **HU:** ...
- **RO:** ...

## Opciók
### Option Display Name
*ID:* `option_id` · *Type:* `single_select` · *Required:* false · *Default:* `xyz`

| ID | HU | RO | Megjegyzés |
|----|-----|-----|------------|
| value_id | HU label | RO label | producer_note vagy — |

## Termelői megjegyzések
> Free text idézet, megjegyzés, kontextus...

## History
- **YYYY-MM-DD** — change description
````

### Option típusok (DH-173)
- `single_select` — radio választó (kötelező `values` tábla)
- `multi_level` — cascading (Sub-options table-eket is támogat — TODO parser)
- `text` — szabadszöveg (max_length opcionális)

### Option value extra mezők
- **`Megjegyzés` oszlop** → `producer_note`
- **`Súlytartomány (kg)` oszlop** ("1.0–1.3" formátumban) → `weight_range: [1.0, 1.3]`

### Termék típusok (DH-183)
- `weight` — gramm/kg-ban rendelhető (32 termék)
- `piece` — fix darab-ár (1 termék: Pástétom)
- `hybrid` — darabra rendel, kilóáron számol becsült súllyal (4 termék)

---

## 🚀 Release folyamat — lépésről lépésre

### 1. Új info → MD frissítés

Ha bejön egy új termékinfo (termelői meeting, ár-változás, új termék):

1. Ha új termék → új fájl: `MASTER/products/uj_termek.md` (másold le egy hasonló típusút mintának)
2. Ha meglévő termék frissül → szerkeszd a `MASTER/products/{id}.md` fájlt
3. **Mindig add hozzá a `## History` szekcióhoz** a változás dátumát + leírását
4. Frissítsd a `last_updated` mezőt a YAML-ben

### 2. Build futtatás — MD → JSON

```python
# Cowork session-ből:
import os, subprocess
mount = next(e for e in os.scandir('/sessions/{SESSION_ID}/mnt/') if 'Dea' in e.name).path
script = os.path.join(mount, 'Products/MASTER/scripts/build.py')

# Default:, schema v1.1. Override: --version 3.3 --schema-version 1.0
r = subprocess.run(['python3', script, '--version', '3.3'], capture_output=True, text=True)
print(r.stdout, r.stderr)
```

**Mit csinál:**
- Beolvas minden `MASTER/products/*.md`-t
- Parseolja a YAML frontmatter-t + MD szekciókat (Név, Leírás, Felhasználás, Opciók, Termelői megjegyzések, History)
- Validálja a JSON Schema ellen (`_schema-v{version}.json`)
- Ha bármi rossz → fail-el, megmondja melyik termék melyik mezője
- Ha mind OK → kiírja: `Products/generated/products-v{version}.json`

### 3. JSON másolás a deploy mappába

A `data/` mappa **a screen-catalog részét képezi** — minden screen-catalog deploy automatikusan újra felviszi:

```bash
cp Products/generated/products-(pre-v1.0 archive).json design/screen-catalog/data/
# Schema csak ha változott:
cp Products/MASTER/_schema-vX.Y.json design/screen-catalog/data/
```

### 4. MANIFEST frissítés (csak ha új verzió)

Ha ÚJ products verzió-fájl (pl. → v3.3), frissítsd az `index.html` inline MANIFEST + `manifest.json` `docs[]` "Adatok" kategóriáját:

```json
{
  "file": "data/products-v3.3.json",
  "title": "Products Master Catalog",
  "desc": "Termékkatalógus — N termék, schema v1.1",
  "icon": "business",
  "version": "v3.3",
  "tags": ["products", "master"],
  "updated": "YYYY-MM-DD",
  "live": true,
  "download": true
}
```

**Fontos:** ha ugyanaz a fájlnév (csak frissült a tartalom, nem bumpolt a verzió), nincs MANIFEST módosítás — atomi deploy felülírja.

**Build szám bump:** `index.html` és `manifest.json` `meta.build` += 1, `meta.generatedAt` = current ISO.

### 5. Pre-deploy ellenőrzés

Inline Python a Cowork-ben:

```python
# Ellenőrzések:
# 1. index.html build == manifest.json build
# 2. Minden manifest entry fájlja létezik (no ghost)
# 3. data/_schema-vX.Y.json + data/products-vX.Y.json létezik
# 4. JSON-ok parseolhatók (valid)
# 5. "Adatok" kategória + két entry a docs[]-ban
# 6. Inline MANIFEST sync (data/ string-ek a HTML-ben)
# 7. dlAttr support patch jelen van index.html-ben
# 8. Stray HTML check (warning csak)
```

A teljes script template-je a session előzményben (build #76 deploy log).

### 6. ⚠️ DEPLOY ENGEDÉLY — KÖTELEZŐ

> **SOHA ne deployolj automatikusan.**
> Mindig kérdezd: **„Deployoljam? (15 kredit)"**
> Csak `igen` / `mehet` / `deploy` válasz után indulj.

### 7. Netlify deploy

```bash
SITE_ID="f5c7e6ed-1ea2-4c72-b8e8-8c342ed3549e"
TOKEN="nfp_iEqWi7A9thMrn5vsFq3dtY2tNDbqpevB750e"

# Stage clean directory (kihagyni: .DS_Store, __pycache__, workflow.md, pre-deploy-check.py)
# Zip-eld az egész design/screen-catalog/ tartalmat (index.html + manifest.json + screens/ + data/)
zip -r /tmp/dh-catalog.zip [stage]

# Curl deploy
curl -s -H "Content-Type: application/zip" \
  -H "Authorization: Bearer $TOKEN" \
  --data-binary "@/tmp/dh-catalog.zip" \
  "https://api.netlify.com/api/v1/sites/$SITE_ID/deploys"
```

Sikeres válasz: `{"state": "uploaded" → "ready", "ssl_url": "https://deakhus.netlify.app", ...}`

### 8. Verifikálás

```bash
curl -sI https://deakhus.netlify.app/data/products-vX.Y.json   # 200 OK
curl -sI https://deakhus.netlify.app/data/_schema-vX.Y.json    # 200 OK (csak ha frissítettük)
```

### 9. version_history.md frissítés

Új release entry a `MASTER/version_history.md`-be (mit, miért, hány termék érintett).

---

## 🛡️ Kritikus szabályok

1. **A `data/` mappa MINDEN screen-catalog deploy része** — ha valaki egy új wireframet deployol, a JSON-ok újra felmennek. Ez a védelem.
2. **Atomi deploy:** Netlify mindig minden fájlt felülír. Ezért a deploy zip-nek **mindig tartalmaznia kell az összes meglévő screen-t + a data/ fájlokat is**.
3. **MD a forrás, JSON a derivátum.** Soha ne szerkeszd a `generated/products-vX.Y.json`-t kézzel — a következő build felülírja.
4. **Schema verziózás konzervatív:** csak struktúra-változásnál bump. Adatváltozásra NEM (különben minden release schema bump-olna).
5. **Sample/proba terméket jelöld a History-ban** (pl. „PROBA SAMPLE", „transcript előtti placeholder") hogy később tudd, mit kell felülírni az igazi adattal.

---

## 🔗 Kapcsolódó

- Main `CLAUDE.md` (workspace root) — Screen Catalog deploy szabályok, Jira státusz
- `design/screen-catalog/workflow.md` — DH Hub deploy workflow (közös)
- Jira tickets:
  - **DH-183 (DONE)** — Terméktípusok modellezése (weight/piece/hybrid)
  - **DH-173 (TO DO)** — Termék testreszabás és preferencia mentés (Sprint 4)

---

## 📋 Quick reference — gyakori parancsok

```bash
# Build the JSON
python3 Products/MASTER/scripts/build.py
python3 Products/MASTER/scripts/build.py --version 3.3 --schema-version 1.0

# Where the master MDs live
ls Products/MASTER/products/

# Where the generated JSON goes
ls Products/generated/

# Where the deploy data lives (gets pushed by every screen-catalog deploy)
ls design/screen-catalog/data/
```

---

**Verzió:** 1.0 | **Utolsó frissítés:** 2026-05-07 | **Build #76 deploy:** ✅ ready
