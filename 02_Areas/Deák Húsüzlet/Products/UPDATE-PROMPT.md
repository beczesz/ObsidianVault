---
title: "Termék frissítés — Onboarding prompt egy új Claude sessionhöz"
date: 2026-05-09
author: Becze Szabolcs
status: active
description: "Onboarding prompt új Claude sessionhöz a Deák Húsmíves termékkatalógus kezelésére, amely tartalmazza a teljes pipeline-t: MD-fájlok szerkesztése, JSON-build, Netlify-deploy, és a konkrét módosítási procedúrákat (ár, leírás, opciók, új termék)."
description_source: auto
description_hash: 8b62c34513133d5a
id: fbdea8d3-afde-4705-9248-81faa821396a
index_schema_version: 1
bdos_index: true
---
# Termék frissítés — Onboarding prompt egy új Claude sessionhöz

> **Másold be ezt a promptot egy új sessionbe.** Tartalmazza az összes kontextust amire szükséged van a Deák Húsmíves termékkatalógus módosításához és deploymentjéhez.

---

## 🎯 Mit fogsz csinálni

A Deák Húsmíves online termékkatalógusát frissíted. Ez egy **MD-master → JSON-build → Netlify-deploy** pipeline. A jelenlegi állapot:

- **46 termék**, 6 kategóriában
- **Schema v1.1** (Frappe DocType-aligned + `internal_code` mező)
- **Élő deploy:** https://deakhus.netlify.app/data/products-v1.1.json
- **Source of truth:** `Products/MASTER/products/*.md` (egy MD fájl per termék)

## 📚 Olvasd el először (prioritás-sorrendben)

**Ezt a 4 fájlt kötelezően olvasd be a session elején, mielőtt bármilyen módosítást teszel:**

1. **`/Users/becze-mac/My Drive (beczesz.szabolcs@gmail.com)/0. Ideas Vault/02_Areas/Deák Húsüzlet/CLAUDE.md`**
   → A workspace fő dokumentáció. Tartalmazza a Netlify deploy szabályokat (Site ID, token, build szám szinkron, deploy permission).

2. **`Products/CLAUDE.md`**
   → A termékkatalógus konkrét workflow-ja. **Itt találod a teljes release proceduálát.** Olvasd el alaposan!

3. **`Products/MASTER/version_history.md`**
   → Az aktuális verzió + release log.

4. **`Products/MASTER/products/sertes_csulok.md`** (vagy bármelyik másik az opciókkal rendelkezők közül)
   → Példa MD struktúra. Az MD formátum „Option C": YAML frontmatter + MD szekciók.

**Opcionális — ha a feature struktúrát is meg akarod érteni:**

- `Business Development/pilot-husuzlet/product-variations/README.md` — DH-173 feature mappa overview
- `Products/products_v1.1_review.xlsx` — vizuális review az összes termékről

---

## 🛠️ Gyakori scenáriók — hogyan csináld

### 1) Termék árának módosítása

**Példa:** A Sertés Csülök ára 19 → 21 RON.

```bash
# 1. Edit the MD file
# File: Products/MASTER/products/sertes_csulok.md
# YAML frontmatter-ben módosítsd:
#   price: 19.0
# →  price: 21.0
```

Plus add a history bejegyzést:
```markdown
## History (MD-only)
- **YYYY-MM-DD** — Ár módosítás: 19.0 → 21.0 RON ([indok])
- ... (előző bejegyzések)
```

### 2) Termék leírásának módosítása

**Példa:** Új RO leírás a Sertés Bélszínhez.

Edit `Products/MASTER/products/sertes_belszin.md` — keresd a `## Leírás` szekciót:
```markdown
## Leírás
- **HU:** A sertés legpuhább, legnemesebb része...
- **RO:** [új szöveg]
```

### 3) Opció hozzáadása / módosítása (DH-173 forward-looking)

**FONTOS:** Az opciók jelenleg **MD-only** mezők — nem kerülnek be a JSON-ba (Sprint 4-re várnak).

A formátum a `## Opciók` szekcióban (lásd `sertes_csulok.md` mintaként):
```markdown
## Opciók (MD-only — DH-173 forward-looking, Sprint 4)

### Opció Neve
*ID:* `option_id` · *Type:* `single_select` · *Required:* false · *Default:* `default_value_id` · *RO:* Opció Romania Neve

| ID | HU | RO | Megjegyzés |
|----|------|------|------------|
| value_id_1 | HU label | RO label | producer note vagy — |
| value_id_2 | ... | ... | ... |
```

**Támogatott `option_type`-ok (3):**
- `single_select` — radio gombok (jelenleg az összes 20 opció ezt használja)
- `multi_level` — cascading (deklarálva, még nincs aktív termék)
- `text` — szabad szöveg (deklarálva, még nincs aktív termék)

> ⚠️ Az `ingredient` típus el lett távolítva (termelő nem támogatja) — ne használd.

### 4) Új termék hozzáadása

**Mérlegelés:** A kategória létezik-e már? (`Products/MASTER/_categories.yaml`)

```bash
# 1. Új MD fájl: Products/MASTER/products/uj_termek.md
```

Másold le egy hasonló típusú meglévő MD-t mintának, és módosítsd:
- `id`: `uj_termek` (snake_case)
- `category`: az 5/6 érvényes közül egy (`friss_serteshus`, `friss_novendekhus`, `friss_csirkehus`, `fustolt_aruk`, `kolbasz_szalami`, `felvagott_egyeb`)
- `internal_code`: ha van a Baczo Annamaria belső listán (vagy `null`)
- `image`: ha van fotó a `Products/product_photos/`-ban (különben placeholder)
- `product_type`: `weight` / `piece` / `hybrid`
- `price`: szám (RON)
- `unit`: `kg` vagy `pcs`
- A 3 kötelező MD szekció: `## Név`, `## Leírás` (HU + RO mindegyiken)

**FIGYELEM: új kategória bevezetése külön schema-elemzést igényel** — kérdezd meg Szabolcsot mielőtt új kategóriát hozol létre.

### 5) Termék eltávolítása

A FUSE mount NEM engedi a fájl-törlést közvetlenül. Két lehetőség:

**(a)** A `is_available: true` mezőt `false`-ra állítod — ezzel a termék nem látszik, de a fájl marad.

**(b)** Ha tényleg törölni akarod a fájlt, használd a `mcp__cowork__allow_cowork_file_delete` toolt:
```python
# request delete permission, then os.remove()
```

### 6) Schema módosítása (új mező)

⚠️ **Ez nagyobb beavatkozás** — schema bump kell. Csak akkor csináld, ha tényleg kell.

Lépések:
1. Bump verzió: `_schema-v1.1.json` → `_schema-v1.2.json`
2. Frissítsd `build.py`-ben a `SCHEMA_ALLOWED_FIELDS` listát (ha új field)
3. Frissítsd a `--schema-version` default-ot `build.py`-ben
4. Update `version_history.md` az új release-szel
5. Frissítsd a 46 termék MD-t ha kell az új mezővel
6. Build + validate + deploy

A production team is el kell fogadja a v1.2-t — koordináld Szabolccsal!

---

## ⚙️ Build pipeline — MD → JSON

A `build.py` szkriptet kell futtatni minden módosítás után:

```bash
# Default: v1.1 + schema v1.1
python3 "Products/MASTER/scripts/build.py"

# Override version-eket:
python3 "Products/MASTER/scripts/build.py" --version 1.2 --schema-version 1.2
```

**Mit csinál a build.py:**
1. Beolvas minden `Products/MASTER/products/*.md`-t
2. Extractálja a YAML frontmatter-t + MD szekciók (Név, Leírás, Megjegyzés)
3. Validálja a JSON Schema ellen (`_schema-vX.Y.json`)
4. Ha bármi hibás → fail, megmondja melyik termék melyik mezője
5. Ha OK → kiírja: `Products/generated/products-vX.Y.json`

**MD-only szekciók** (NEM kerülnek a JSON-ba):
- `## Felhasználás`
- `## Opciók`
- `## Termelői megjegyzések`
- `## History`

**MD-only YAML kulcsok:**
- `seasonal`
- `sources`
- `last_updated`

### Build hibák értelmezése

Ha a build fail-el:
- `Schema validation FAILED` → A YAML mezőkben hibás érték. Olvasd el a hibaüzenetet (path + message), és javítsd az MD-t.
- `additionalProperties` hiba → Új mezőt tettél a YAML-be ami nincs a schemában. Vagy vedd ki, vagy bumpolj sémát.
- `pattern` hiba → Az `internal_code` vagy `id` mező nem felel meg a regex-nek (snake_case ID, alfanumerikus kód `^[A-Z0-9]{3,7}(\.\d+)?$`).

---

## 🚀 Deploy flow — kötelező lépések

> ⚠️ **SOHA ne deployolj automatikusan! Mindig kérdezd meg a usert: „Deployoljam? (15 kredit)" — csak igenlő válasz után indulj.**

A deploy **a screen-catalog részeként** megy ki (ott vannak a JSON-ok is):

### 1. Másolás a deploy mappába

```bash
cp Products/generated/products-v1.1.json design/screen-catalog/data/
# Schema csak ha új verzió (új schema fájl):
cp Products/MASTER/_schema-v1.1.json design/screen-catalog/data/
```

### 2. Build szám frissítés (csak ha új JSON verzió fájl)

Ha a `products-v1.1.json` ugyanaz a fájlnév (csak frissült a tartalom), **nincs MANIFEST módosítás** — atomi deploy felülírja.

Ha **új verzió** (pl. v1.1 → v1.2), akkor frissítsd:
- `design/screen-catalog/index.html` → `const MANIFEST = {...}` inline blokk: `meta.build` += 1, `meta.generatedAt` = current ISO
- `design/screen-catalog/manifest.json` → ugyanaz
- `MANIFEST.docs.Adatok.items` → cseréld a `file`/`version` mezőket az új verzióra

**Build szám szabály:** mindig `max(idx_build, mf_build) + 1` — ne menj alacsonyabb számra!

### 3. Pre-deploy check

A `Products/CLAUDE.md`-ben van inline Python script — futtasd!

Ellenőrzései:
- ✅ Build sync (idx_build == mf_build)
- ✅ No ghost entries (manifest → disk)
- ✅ data/_schema-vX.Y.json + data/products-vX.Y.json létezik
- ✅ JSON validitás (parseolható)
- ✅ Schema validation pass
- ✅ Termékszám OK (46)
- ✅ Kategória count OK (6)
- ✅ dlAttr support az index.html-ben

Ha **bármelyik ❌** → DEPLOY TILOS, javítsd.

### 4. Kérdezd meg a usert

```
„Deployoljam? (15 kredit)"
```

**CSAK** explicit `igen`/`mehet`/`deploy` után induljon a következő lépés!

### 5. Netlify deploy

A workspace `CLAUDE.md`-ben van a Netlify token + Site ID. A deploy parancs:

```bash
SITE_ID="f5c7e6ed-1ea2-4c72-b8e8-8c342ed3549e"
TOKEN="nfp_iEqWi7A9thMrn5vsFq3dtY2tNDbqpevB750e"

# Stage clean dir + create zip from design/screen-catalog/ contents
# (kihagyni: .DS_Store, __pycache__, workflow.md, pre-deploy-check.py)

curl -s -H "Content-Type: application/zip" \
  -H "Authorization: Bearer $TOKEN" \
  --data-binary "@/tmp/dh-catalog.zip" \
  "https://api.netlify.com/api/v1/sites/$SITE_ID/deploys"
```

Sikeres válasz: `{"state": "uploaded" → "ready", "ssl_url": "https://deakhus.netlify.app", ...}`

### 6. Verifikálás

```bash
curl -sI https://deakhus.netlify.app/data/products-v1.1.json   # 200 OK
curl -s https://deakhus.netlify.app/data/products-v1.1.json | python3 -c "
import json, sys
d = json.load(sys.stdin)
print(f'Products: {len(d[\"products\"])}')
print(f'Categories: {len(d[\"categories\"])}')
print(f'Version: {d[\"meta\"][\"version\"]}')
"
```

### 7. Naplózás

Frissítsd a `Products/MASTER/version_history.md`-t az új release-szel — mit változtattál, mikor, miért.

---

## 🛡️ Kritikus szabályok (NE FELEDD!)

1. **🚫 SOHA ne deployolj engedély nélkül** — minden deploy 15 kredit, és atomi (mindent felülír)

2. **MD-only szekciók NEM kerülnek a JSON-ba** — ha valamit a JSON-ban akarsz látni, az a YAML frontmatter része kell legyen, nem a `## Opciók` vagy más MD szekció

3. **Schema-strict** — a v1.1 schema `additionalProperties: false`. Új YAML mező = hibás build. Ha új mező kell, schema bump

4. **Internal_code pattern**: `^[A-Z0-9]{3,7}(\.[0-9]+)?$` — pl. `014`, `0221`, `ACS04`, `945.1`. Ha a kód nem illeszkedik, vedd ki vagy módosítsd

5. **Hybrid termékek mindenképpen tartalmazzanak**: `estimated_weight_per_piece`, `weight_range_min`, `weight_range_max`. Weight + piece termékeknél ezek mind `null`

6. **Pre-deploy check 0 errors** kell legyen — ha akár 1 piros van, NE deployolj

7. **A `data/` mappa a screen-catalog részévé vált** — minden screen-catalog deploy mindent felülír. Ezért ha csak products-t deploy-olsz, az index.html + manifest.json + screens/* is megy a zipbe

8. **`ingredient` opció-típus** — ne használd, eltávolítva. 3 típus van: `single_select`, `multi_level`, `text`

---

## 📂 A fontosabb file path-ok

```
/Users/becze-mac/My Drive (beczesz.szabolcs@gmail.com)/0. Ideas Vault/02_Areas/Deák Húsüzlet/

CLAUDE.md                                              ← workspace fő docs
Products/
  CLAUDE.md                                            ← termékkatalógus workflow
  MASTER/
    _schema-v1.1.json                                  ← AKTUÁLIS schema
    _categories.yaml                                   ← 6 kategória
    _settings.yaml                                     ← global default-ok
    version_history.md                                 ← release napló
    products/                                          ← 46 MD fájl ⭐
    scripts/build.py                                   ← MD → JSON
    reference/                                         ← production schema referencia
  generated/
    products-v1.1.json                                 ← AKTUÁLIS generated JSON
  meetings/                                            ← termelői meeting dokumentumok
  legacy/                                              ← archív (v3.X, pre-v1.0) — NE használd
  product_photos/                                      ← *.webp képek

design/screen-catalog/                                 ← deploy zip forrás
  index.html                                           ← inline MANIFEST
  manifest.json                                        ← szinkronban
  data/
    _schema-v1.1.json                                  ← AKTUÁLIS deploy schema
    products-v1.1.json                                 ← AKTUÁLIS deploy JSON
  screens/                                             ← wireframe HTML-ek

Business Development/pilot-husuzlet/product-variations/
  README.md                                            ← DH-173 feature overview
  product-variations-spec-v1.0.md                      ← teljes spec
  product-options-matrix-v1.0.md                       ← per-termék opció bontás
```

---

## 🔍 Hogyan kezdj a session-be

```
1. Olvasd be a workspace CLAUDE.md-t
2. Olvasd be a Products/CLAUDE.md-t
3. Olvasd be a Products/MASTER/version_history.md-t
4. Olvasd be 1-2 termék MD-jét mintáért (pl. sertes_csulok.md, nyakas_karaj.md)
5. Hallgasd meg a usert — milyen módosítást szeretne
6. Csináld meg a módosítást a megfelelő MD-ben
7. Add hozzá a History bejegyzést
8. Futtasd a build.py-t — verifikáld a passes-t
9. Másold a generated JSON-t a deploy mappába
10. Pre-deploy check
11. KÉRDEZD MEG: "Deployoljam? (15 kredit)"
12. Igenlő válasz után: deploy + verifikálás + version_history.md frissítés
```

---

**Verzió:** 1.0 | **Dátum:** 2026-05-07 | **Workspace:** Deák Húsmíves termékkatalógus
