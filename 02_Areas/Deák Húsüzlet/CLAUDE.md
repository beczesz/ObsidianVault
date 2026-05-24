# Memory – Szabolcs / Exar Labs munkaterülete

---

## 🚀 Session Startup — Automatikus protokoll

> **Ezt olvasd el először. Minden munkamenet elején futtasd le az alábbi lépéseket, Szabolcs külön kérése nélkül.**

### 📚 Kötelező olvasmány (minden session elején)

> **Mielőtt bármilyen érdemi munkát kezdesz, olvasd be ezeket a fájlokat sorrendben.**
> Ez biztosítja, hogy a DH projekt teljes kontextusát értsd.

| # | Fájl | Miért fontos |
|---|------|-------------|
| 1 | `01_PROJECT_STATE.md` | Projekt összefoglaló, aktuális státusz |
| 2 | `Business Development/pilot-husuzlet/BMC-v2.2.md` | Business Model Canvas — stratégia alapja |
| 3 | `Business Development/pilot-husuzlet/founding50-spec-v1.0.md` | Founding 50 early adopter program |
| 4 | `brainstorm/brainstorm_deak-pricing-revenue-share.md` | Platformdíj modell |
| 5 | `design/app-flow-v0.3.md` | App Flow Map — teljes funkcionalitás snapshot (képernyők, termékek, API, admin) |

**Összesen:** ~1700 sor (~12-14% kontextus) — bőven belefér és nem akadályozza az érdemi munkát.

### Ha Szabolcs designról / screenről / wireframe-ről beszél:

```
1. Töltsd be a design kontextust:
   cd "design" && node ~/.agents/skills/impeccable/scripts/load-context.mjs

2. Ha új screent kér → $impeccable craft [screen neve]
   Ha meglévőt szerkeszt → olvasd be a fájlt, aztán $impeccable harden / polish / stb.

3. Deploy előtt MINDIG kérdezz: "Deployoljam?" — soha ne deployolj automatikusan.
```

### Eszközök amelyek be vannak kötve (azonnal használhatók):

| Eszköz | Mire jó | Hogyan |
|--------|---------|--------|
| **Jira MCP** | Ticket olvasás, státusz váltás, komment | `mcp__faf18963...__getJiraIssue`, cloudId: `exarlabs.atlassian.net` |
| **Netlify API** | Deploy (zip → curl) | Token és Site ID lejjebb a "Netlify deploy workflow" szekcióban |
| **impeccable skill** | Design workflow | `$impeccable [parancs]` — referencia: `~/.agents/skills/impeccable/` |

### Fájlrendszer — ahol a dolgok vannak:

```
Deák Húsüzlet/
  CLAUDE.md              ← ez a fájl (single source of truth)
  01_PROJECT_STATE.md    ← projekt összefoglaló
  TASKS.md               ← task tracking
  Business Development/  ← BMC, KPI, legal, savings-engine specs, analytics dict
  Marketing/             ← Brand/, Kampány/, logo, szorolap, sales
  Products/              ← product listing + fotók + JSON
  brainstorm/            ← Think Engine brainstorm state fájlok
  design/
    PRODUCT.md           ← brand, users, anti-references (impeccable betölti)
    DESIGN.md            ← color tokens, typography, components (impeccable betölti)
    approved-sample-screens/ ← jóváhagyott referencia screének
    screen-catalog/
      index.html         ← DH Hub — inline MANIFEST (const MANIFEST = {...})
      screens/           ← MINDEN HTML fájl ide kerül (screens + docs egyaránt)
        v0.3-*.html
        v0.4-*.html
        v0.5-*.html
  manual/                ← v0.2 user manual (HU + RO)
  memory/                ← productivity plugin memory fájlok
  plugins/               ← deak-design plugin
  BIN/                   ← archivált / elavult fájlok (NE HASZNÁLD, csak referencia)
```

### Gyors referencia — legfontosabb szabályok:

- **Build szám:** mindig az `index.html` MANIFEST-ből olvasd (`meta.build`) — ne manifest.json-ból
- **Deploy = zip az összes fájllal:** `index.html` + `screens/*.html` egy zipbe, aztán curl API
- **Back button:** minden screen-ben `<a href="../index.html" class="back-to-catalog">` (relatív path!)
- **Design token:** primary `#9B2335`, cream `#FFFBF7`, Inter + Playfair Display, Lucide SVG ikonok

---

## Én
**Szabolcs** (Becze Szabolcs) – Az **Exar Labs** IT cég alapítója és vezetője. Székelyudvarhely. Érdeklődési terület: üzleti fejlesztés, passzív jövedelemforrások, AI-alapú fejlesztés, venture studio modell.

## Cég
**Exar Labs** (jogi entitás: **EXARGROUPS S.R.L.**) – 12 fős fejlesztői csapat, Székelyudvarhely (= Újvárhely). Fő tevékenység: szoftverfejlesztési outsourcing (egy stratégiai partnernek). Jelenlegi helyzet: veszteséges / nullszaldós, diverzifikáció szükséges.

## Emberek
| Ki | Szerep |
|----|--------|
| **Szabolcs** | Becze Szabolcs – Exar Labs vezető |
| **Deák Húsmíves tulajdonos** | Kézműves mészáros, szakmailag kiváló, üzletileg gyenge |
| **Két testvér** | A Deák Húsmíves két tulajdonosa – konfliktusban |
| **Csilla** | YouTube creator (csigalak7), háziasszony/anyaság témák, Angliában él – Navigátor Podcast vendégnek felkérve, visszautasított (2026-03-18) |

## Fogalmak / Rövidítések
| Fogalom | Jelentés |
|---------|---------|
| **Exar Labs** | Szabolcs IT cége (brand név), 12 fő, Székelyudvarhely. **Jogi entitás: EXARGROUPS S.R.L.** (CUI: RO41839221, J2019000789190) |
| **Deák Húsmíves** | Partner kézműves húsüzem – 3 bolt Újvárhelyen |
| **DH** | Deák Húsmíves Online Platform – Jira projekt kulcs (exarlabs.atlassian.net) |
| **Pilot** | Az MVP online rendelési webapp kísérlet (DH) |
| **Bench** | Exar Labs-nál aktív projekt nélküli fejlesztők |
| **Frappe** | Python-alapú üzleti alkalmazásplatform (ERP, LMS stb.) |
| **Oktatási projekt** | Pályázati projekt – oktatási platform fejlesztése (2 év stabilitás) |
| **Venture Studio** | Stratégiai irány 3 – mini startup modellek gyors tesztelése |
| **Navigátor Podcast** | Szabolcs által vezetett podcast (navigator.podc@gmail.com) |
| **LocalBasket** | A DH platform-vízió neve: 1 platform, 2 mód (Daily + Local Market) |
| **Guest-first UX** | Termékek láthatók login előtt; login csak a fizetésnél |
| **Platformdíj (taxă de platformă)** | **MEGÁLLAPODVA:** Phase 1: 6,8% platformdíj a Vânzări eligibile-ből (retail ár incl. TVA). Keretszerződés v1.2 + Comanda nr.1 v1.3 rögzíti. |
| **Firebase Analytics** | A custom Frappe analytics helyett; SDK bekötés DH-104 |
| **Flywheel** | Növekedési hajtókerék: ellátás → vásárlás → szokás → volumen → jobb feltételek |
| **Stop cap** | Maximális kockázatvállalás: ~12-13k EUR; ennél tovább nem megy a pilot |
| **Dry run** | Próba-üzem: belső tesztelés a kemény launch előtt |
| **2nd order trigger** | Az első rendelés után automatikus visszacsalogatás |
| **North Star KPI** | Second Order Rate 14 napon belül (cél: ≥40%) |
| **TTFO** | Time to First Order – regisztrációtól az első rendelésig (cél: ≤72 óra) |
| **Founding 50** | Early adopter toborzási program — 50 fő, 3 hó ingyenes szállítás, soft retention filter |
| **Savings engine** | Sprint 3 fő feature – háztartási spórolás kalkulátor (counter + threshold + recap) |

## Projektek
| Név | Mi ez |
|-----|-------|
| **DH (Deák Húsmíves Online Platform)** | Online rendelési + házhozszállítási rendszer – 146 Jira ticket (104 Done, 2 IP, 40 ToDo), Sprint 2 LEZÁRVA (38/38), Sprint 3 ACTIVE **70%** (7/10 Done, scope szűkült), Beta v0.3 után (~2026-05-15) |
| **Navigátor Podcast** | Szabolcs podcastje – vendégeket keres Székelyudvarhely/Erdély témákban |
| **Ignis Learning Platform** | Oktatási platform – pályázati projekt, Frappe + LangChain AI, Jira: KAN (exarlabs.atlassian.net) |
| **LocalBasket Platform** | Hosszú távú vízió – 1 platform, 2 mód; csak DH pilot után kidolgozni |

## Stratégiai irányok (3 pillér)
1. **AI-alapú fejlesztési hatékonyság** – Frappe + AI, ~10x fejlesztési sebesség (mérve)
2. **Közvetlen ügyfélprojektek** – outsourcing helyett direkt ügyfélkapcsolat, co-venture modell
3. **Pilot ciklusok / tanulás** – gyors kísérletezés, DH az első példa

## DH kulcsadatok
- **Jira:** DH projekt (exarlabs.atlassian.net) — 153 ticket, DH-1 → DH-157
- **Státusz:** 104 Done | 2 In Progress | 40 To Do — frissítve 2026-04-22
- **Sprint 2 (LEZÁRVA):** 38 ticket — **38 Done / 0 IP / 0 ToDo = 100%** (befejezés ápr. 15)
- **v0.2 release:** "Látjuk az adatokat" — teljes analytics stack ✅ KÉSZ
- **Sprint 3 (ACTIVE):** **10 ticket — 7 Done / 2 IP / 1 To Do = 70%** (scope szűkült 21→10, Legal kikerült)
- **Helyszín:** Székelyudvarhely (Újvárhely), ~30.000 lakos
- **AI előny:** ~10x fejlesztési sebesség (mérve, velocity-tracker-v1.1.md)
- **Üzemeltetési kltg:** ~3.900 EUR/év (Exar Labs viseli)
- **Stop cap:** ~12-13k EUR teljes kockázat (dev + ops + marketing)
- **Fizetés (pilot):** Csak készpénz szállításkor; online fizetés post-MVP
- **Termékek:** 37 termék, 5 kategória
- **Domain:** deakhus.ro ✅ ÉLES (2026-03-30) | staging.deakhus.ro ✅ ÉLES
- **Platformdíj:** **MEGÁLLAPODVA** — Phase 1: 6,8% taxă de platformă (retail ár incl. TVA alapon). Contract-cadru v1.2 + Comanda nr.1 v1.3.
- **Beta dátum:** v0.3 release után (~2026-05-15, Sprint 3 végén)
- **Elsődleges csatorna:** Bolt + személyes ajánlás + QR (NEM Facebook)
- **Célszegmens (első 30):** Digitálisan nyitott, időszűkében lévő helyi vásárlók, 25-45 év

## Release Roadmap
| Verzió | Sprint | Fókusz |
|--------|--------|--------|
| v0.1 | Sprint 1.1 (CLOSED) | „Az első rendelés" — MVP ✅ |
| v0.2 | Sprint 2 (CLOSED 2026-04-15) | „Látjuk az adatokat" — analytics, bugfixek ✅ |
| v0.3 | Sprint 3 (ACTIVE, indul ápr. 16) | „A spórolás motora" — Savings engine, core loop |
| — | 2 hét szünet | Management tesztelés + natív mobil előkészítés |
| v0.4 | Sprint 4 | Natív mobil experience (iOS prioritás) |
| v0.5 | Sprint 5 | Növekedési platform — online fizetés |

## DH Pilot döntési logika (max 3 hónap)
- **Skálázás** (mindkettő teljesül): ≥50 regisztráció + ≥20 visszatérő vásárló (újrarendelés 14 napon belül)
- **Stop** (3 hónap után, efort maxim mellett sem teljesülnek a kritériumok): pilot lezárás
- A pilot **bármikor** véget érhet közös döntéssel, penalitás nélkül

## DH kritikus kockázat
> A modell **nem marketingen** fog elbukni – hanem **operáció + supply stabilitás**-on. Validálandó: napi kapacitás, fulfillment flow, döntéshozó a két testvér közül.

## Blokkolt feladatok (launch előtt)
- ~~Platformdíj véglegesítése~~ KÉSZ (2026-04-15) — Phase 1: 6,8% platformdíj (Contract-cadru v1.2 + Comanda nr.1 v1.3)
- ~~Domain véglegesítése~~ ✅ KÉSZ -- deakhus.ro él (2026-03-30)
- Írásbeli partnerségi megállapodás
- Marketing budget cap rögzítése

## Screen Catalog szabályok (design/screen-catalog/)

**Aktuális build: #64** | **14 screen** | **2 doc** | https://deakhus.netlify.app

### Mappastruktúra (FONTOS — ide dolgozz!)
```
design/
  screen-catalog/
    index.html        ← inline MANIFEST tartalmazza (const MANIFEST = {...})
    manifest.json     ← mindig szinkronban az index.html-lel
    workflow.md       ← részletes workflow dokumentáció
    screens/          ← *.html screen fájlok
      v0.3-*.html
      v0.4-*.html
      v0.5-*.html
      Raw/            ← Claude Design → ide kerülnek feldolgozás előtt
      archive/        ← Raw fájlok archiválva feldolgozás után
  DESIGN.md           ← impeccable /teach output — design system referencia
  PRODUCT.md          ← impeccable /teach output — product context
  wireframes/
    archive/b33-final/ ← régi build archívum (b33)
```

### ⚠️ Cowork + Claude Code szinkron szabályok

**Az `index.html` inline MANIFEST az egyetlen igazság forrás.**

| Szabály | Leírás |
|---------|--------|
| **Build szám olvasás** | Deploy előtt MINDIG olvasd be az index.html `const MANIFEST = {...}` blokkjából az aktuális build számot. Ne a manifest.json-ból! |
| **Build szám írás** | `new_build = max(index.html build, manifest.json build) + 1` — soha ne írj alacsonyabb számot! |
| **Szinkron kötelező** | Minden módosítás után index.html és manifest.json EGYSZERRE frissül |
| **Ghost entry tilos** | Csak létező `screens/*.html` fájl kerülhet a manifestbe. Deploy előtt ellenőrizd: `os.path.exists()`! |
| **Claude Code prioritás** | Ha index.html build > manifest.json build, Claude Code dolgozott közbülső — az index.html az újabb, azt vedd alapul |

### Screen metadata blokk (minden screen HTML-ben kötelező)
```html
<script type="application/json" id="screen-meta">
{
  "id": "v0.3-feature-name",
  "title": "Feature — Leírás",
  "sprint": "Sprint 3",
  "status": "draft",
  "tags": ["DH-XXX", "feature", "tag"],
  "order": 10,
  "description": "Rövid leírás"
}
</script>
```

### Deploy QA (kötelező deploy előtt)
- **Back button:** Minden screen HTML-ben legyen `<a href="../index.html" class="back-to-catalog">` — relatív path (screens/ almappából!)
- **Ghost entry:** Minden manifest entry fájlja létezzen a lemezen (`os.path.exists()`)
- **Build szám:** index.html build == manifest.json build deploy előtt
- **Netlify atomi deploy:** Mindig MINDEN fájlt bele a zip-be (index.html + manifest.json + screens/*.html)
- **Pre-deploy check:** Futtasd a `pre-deploy-check.py` scriptet deploy előtt — ha ❌ van, NE deployolj!

### ⚠️ KRITIKUS: Screen fájlok helye
**MINDEN screen fájlnak a `design/screen-catalog/screens/` mappában kell lennie.**
Ha egy HTML fájl máshol van (pl. `development/analytics/`), a Netlify deploy NEM veszi bele — láthatatlan lesz.

| ❌ ROSSZ | ✅ JÓ |
|---------|-------|
| `development/analytics/analytics-dictionary-v2.2.html` | `design/screen-catalog/screens/v0.2-analytics-dictionary.html` |

**Root cause (2026-04-29):** az analytics-dictionary-v2.2.html a development/analytics/ mappában élt → minden deploy-nál kiesett. Fix: áthelyezve screens/ mappába + pre-deploy-check.py warning jelez ha van stray HTML fájl.

### Pre-deploy check script
```bash
# Cowork session-ből futtatás (inline Python, nem bash path!):
python3 << 'PYEOF'
import os, json, re, sys
# ... (full script: design/screen-catalog/pre-deploy-check.py)
PYEOF
```
A teljes script: `design/screen-catalog/pre-deploy-check.py`


### Tab struktúra — döntési szabályok

**DH Hub 2 tab:** `Képernyők` (screens[]) és `Dokumentáció` (docs[])

#### Melyik tab alá kerüljön?
```
UX/UI wireframe, app screen, komponens?  →  KÉPERNYŐK tab (screens[])
Jogi dokumentum wireframe-je?            →  KÉPERNYŐK tab, sprint="Legal", feature="legal"
Referencia doc, szótár, business model?  →  DOKUMENTÁCIÓ tab (docs[])
```

#### Képernyők tab — sprint értékek
| Sprint | Mikor |
|--------|-------|
| `Sprint 3` | v0.3 — savings engine screének |
| `Sprint 4` | v0.4 — natív mobil |
| `Sprint 5` | v0.5 — növekedési platform |
| `Legal` | ÁSZF, Privacy Policy, GDPR wireframe-ek |

#### Dokumentáció tab — icon és kategória
| Icon | Kategória | Mikor |
|------|-----------|-------|
| `analytics` | Analytics | Firebase events, tracking |
| `design` | Design | Design system, komponens doc |
| `business` | Business | Business model, KPI |
| `legal` | Legal | Jogi referencia (NEM wireframe) |

#### ⚠️ Kritikus: MINDEN fájlnak a `screens/` mappában kell lennie — docs tab fájljai is!

### ⛔ DEPLOY SZABÁLY — LEGFONTOSABB

> **SOHA ne deployolj automatikusan vagy kérdezés nélkül.**
>
> Minden deploy előtt kötelező megkérdezni:  
> **„Deployoljam? (ez 15 kreditet fogyaszt)"**
>
> Csak explicit igenlő válasz után (`igen`, `deploy`, `mehet`) szabad deployt indítani.  
> 1 production deploy = **15 kredit**. Personal plan = 1 000 kredit/hó.  
> Cél: munkamenetenként **1 deploy** — összegyűjtjük a változtatásokat, majd 1× deploy.

### Netlify deploy workflow (API-alapú)
1. **Site:** deakhus.netlify.app
   - **Site ID:** `f5c7e6ed-1ea2-4c72-b8e8-8c342ed3549e`
   - **API token:** `.env` fájlban — `NETLIFY_TOKEN=nfp_iEqWi7A9thMrn5vsFq3dtY2tNDbqpevB750e` (ne commitold!)
   - **Deploys URL:** https://app.netlify.com/projects/deakhus/deploys
2. **Zip struktúra** (screens/ almappa megmarad):
   ```
   index.html     ← root
   manifest.json  ← root
   screens/*.html ← screens/ almappában
   ```
3. **Deploy parancs:**
   ```bash
   curl -s -H "Content-Type: application/zip" \
     -H "Authorization: Bearer $NETLIFY_TOKEN" \
     --data-binary "@/tmp/dh-catalog.zip" \
     "https://api.netlify.com/api/v1/sites/f5c7e6ed-1ea2-4c72-b8e8-8c342ed3549e/deploys"
   ```
   Sikeres válasz: `{"state": "ready", "ssl_url": "https://deakhus.netlify.app", ...}`
4. **FONTOS:** Netlify atomi deploy — minden deploy lecseréli az ÖSSZES fájlt.
5. **NE használd a Chrome file_upload-ot** — "Not allowed" hibát ad. Mindig curl API.
6. **Cowork előfeltétel:** Settings → Capabilities → Network access → "All domains" ENGEDÉLYEZVE

### Raw workflow (Claude Design → screen-catalog)
```
Claude Design → HTML export → screens/Raw/ mappába másolás
→ Cowork: integrate_raw.py futtatása (screen-meta, back btn, CSS vars injektálás)
→ screens/*.html létrehozva
→ manifest.json + index.html frissítés (build = max+1)
→ Raw fájl → archive/ (FUSE miatt kézzel törlendő Finderből)
→ Netlify deploy (Szabolcs jóváhagyásával)
```


## Products Master Workflow (2026-05-07-től)

> **Részletes doc:** `Products/CLAUDE.md`
> **Élő deploy:** https://deakhus.netlify.app/data/(archived legacy)

**Source of truth = `Products/MASTER/products/*.md`** (Option C: minimális YAML + MD táblák).
A JSON determinisztikusan generálódik a build script-tel, schema-validálva.

| Mit | Hol |
|------|-----|
| Master MD-k | `Products/MASTER/products/*.md` |
| JSON Schema | `Products/MASTER/_schema-v1.0.json` |
| Build script | `Products/MASTER/scripts/build.py` |
| Generated JSON | `Products/generated/products-vX.Y.json` |
| Deploy mappa | `design/screen-catalog/data/` (minden screen-catalog deploy felviszi) |

### Gyors workflow
```
1. MD szerkesztés: Products/MASTER/products/{id}.md (frissítsd a History-t!)
2. Build:          python3 Products/MASTER/scripts/build.py [--version 3.X]
3. Másolás:        cp Products/generated/products-(pre-v1.0 archive).json design/screen-catalog/data/
4. MANIFEST:       (csak ha új verzió-fájl) docs[]/Adatok kategória + build++
5. Pre-deploy:     ellenőrzések (build sync, ghost, JSON valid, dlAttr patch)
6. ⚠️ ENGEDÉLY:    "Deployoljam? (15 kredit)" — explicit user válasz!
7. Deploy:         curl Netlify API (ugyanaz a Site ID mint a screen-catalog)
8. Version log:    Products/MASTER/version_history.md
```

### Verziózás
- **Schema verzió** (`_schema-vX.Y.json`) — csak struktúra-változásnál bump
- **Products data verzió** (`products-vX.Y.json`) — minden release-nél bump
- MD master = git history (nincs külön snapshot folder)

### Kritikus szabály
A `data/` mappa **a screen-catalog részévé vált**. Akármikor egy új wireframet deployolsz, a products + schema JSON automatikusan újra felmegy — soha nem vesznek el. Atomi deploy védelem.

## Nagytakarítás (2026-05-01)
- BIN/ mappába archiválva: 760 fájl (régi wireframek, worktrees, duplikációk, elavult verziók)
- development/ mappa megszüntetve (analytics dict → BD/pilot-husuzlet/)
- specs/ mappa megszüntetve (spec → BD/pilot-husuzlet/savings-engine/Ideas/)
- Kötelező olvasmány szekció hozzáadva a Session Startup-hoz
## Preferenciák
- Magyar nyelvű kommunikáció
- Gyors, minimális kockázatú validáció
- Bench kapacitás hasznosítása
- Kísérletező, tanuló megközelítés

---

## ⚠️ FÁJLKEZELÉSI SZABÁLYOK

### FUSE mount viselkedés
A workspace mappa (`Deák Húsüzlet`) **bindfs FUSE mount** a Google Drive-ról.
- **Írás:** Python `open(path, 'w')` működik (bash-ból)
- **Törlés:** `mcp__cowork__allow_cowork_file_delete` tool-lal engedélyezhető, utána `os.remove()` működik
- **Read/Edit tool:** Közvetlenül a FUSE mount-ra ír — használható végleges fájlokhoz is
- Unicode: a fájlrendszer NFD formátumot használ (pl. `Deák` = `Dea\u0301k`)

### Mikor mit használok
| Művelet | Eszköz |
|---------|--------|
| Fájl írás/szerkesztés | `Read` + `Edit` tool VAGY Python `open()` bash-ból |
| Fájl olvasás | `Read` tool VAGY Python `open()` |
| Fájl törlése | `mcp__cowork__allow_cowork_file_delete` → `os.remove()` bash-ból |
| Deliverable átadás | `mcp__cowork__present_files` → outputs/ |

## DH Jira ticket teljes lista (frissítve: 2026-04-15)

### Sprint 2 — LEZÁRHATÓ ✅ (38/38 Done, 0 maradék)

**Sprint 2 tartalom:** DH-17, 30, 35, 36, 37, 43, 44, 46, 47, 59, 68, 77, 78, 79, 80, 81, 82, 84, 86, 89, 91, 97, 100, 101, 102, 104, 105, 106, 108, 109, 111, 113, 114, 115, 140, 141, 142, 144 — **mind Done**

**v0.2 "Látjuk az adatokat" release KÉSZ** — minden analytics ticket (DH-43, 44, 80, 81, 82, 104, 109) Done.

### Backlog|---------|
| DH-116 | Epic 10 – v0.3 Savings Engine |
| DH-117 | NEW-1: Running Savings Counter — Backend |
| DH-118 | NEW-1: Running Savings Counter — Frontend |
| DH-119 | NEW-3: Post-order Recap |
| DH-120 | NEW-4: Reorder — Basket Loader |
| DH-121 | NEW-5: Family Bundles — Vásárlói nézet |
| DH-122 | NEW-5: Family Bundles — Admin CRUD |
| DH-123 | Rendeléseim — Spórolás badge + újrarendelés |
| DH-127 | NEW-9: "Szokásos rendelésem" gomb — Familiar Favourites |
| DH-128 | NEW-10: Swap suggestion MVP |
| DH-129 | Savings Engine Firebase eventek — 10 új event + guardrail |
| DH-146 | NEW-11: Kedvenc Termékek — Csillag toggle + lista rendezés (Sprint 5) |

### Backlog (email-alapú — NEM spammelünk)
| Ticket | Summary |
|--------|---------|
| DH-124 | NEW-6: TTFO Engine — Email drip |
| DH-125 | NEW-7: Post-delivery reorder trigger |
| DH-126 | NEW-8: Savings recap email |


### Legal & Compliance (mind To Do)
| Ticket | Summary |
|--------|---------|
| DH-130 | ÁSZF draft készítése |
| DH-131 | Impresszum oldal létrehozása |
| DH-132 | GDPR consent checkbox |
| DH-133 | Jogi szolgáltató tisztázása (BLOCKER) |
| DH-134 | Privacy Policy frissítés (v0.4) |
| DH-135 | App Store developer account (v0.4) |
| DH-136 | ANSVSA szállítási engedély ellenőrzés |
| DH-137 | Cookie policy ellenőrzés |
| DH-138 | Epic — Legal & Compliance |
## Dokumentum verziók (frissítve: 2026-04-15)
| Dokumentum | Verzió | Dátum |
|-----------|--------|-------|
| KPI Framework | v1.2 | 2026-04-04 |
| v0.3 Release Plan | v1.5 | 2026-04-04 |
| v0.3 Wireframes | v3 | 2026-04-04 |
| TASKS.md | Jira sync (Sprint 3 update + Founding 50) | 2026-04-22 |
| founding50-spec | v1.0 | 2026-04-22 |
| 01_PROJECT_STATE | v1.3 | 2026-04-15 |
| CLAUDE.md | Sprint 3 update + app-flow | 2026-05-02 |
| app-flow-v0.3.md | v0.3 | 2026-05-02 |
| legal.md | v1.1 | 2026-04-05 |

## KPI Alignment döntések (2026-04-04, Claude + ChatGPT egyeztetés)
- **MUST beta előtt:** Firebase v0.3 eventek (10 új), Threshold KPI, Guardrail mérés (checkout_duration)
- **SHOULD (v0.3.1 után):** TTFO 48h→24h (v0.4), "User feels smarter" mérés (v0.4)
- **NEM kell v0.3-ban:** NPS (nincs infra), extra Jira ticketek (backlogban vannak)
- **KPI Framework v1.2 kötelező frissítés** — megtörtént

## Email policy (2026-04-04, Szabolcs döntése)
> **NEM spammelünk.** A Deák Húsmíves egy kézműves húsüzlet, nem egy e-commerce óriás.

- **Maximum 1 értesítő email / user / hét** (tranzakciós emaileken kívül: rendelés visszaigazolás, státusz)
- Email ticketek (DH-124, DH-125, DH-126) backlogban maradnak — csak ha a pilot adatai indokolják
- **Prioritási sorrend** (ha mégis kell): post-delivery reorder trigger > savings recap > TTFO drip
- Ha a user rendelt a héten → nem kap marketing emailt
- Az elsődleges csatorna a **bolt + személyes ajánlás + QR**, NEM email

