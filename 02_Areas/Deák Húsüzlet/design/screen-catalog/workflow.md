# DH Screen Catalog — Workflow Documentation

> **Státusz:** Aktív  
> **Létrehozva:** 2026-04-25  
> **Plugin célja:** Egyetlen parancssorral deploy-olható, metadata-vezérelt UI screen katalógus

---

## 1. Architektúra áttekintés

### A két Claude rendszer szétválasztása

| Rendszer | Feladata | Mit lát |
|----------|----------|---------|
| **Claude Design** | Izolált képernyő-szerkesztés (high-fidelity HTML) | Csak 1 screen HTML + rövid instrukció |
| **Claude CoWork** | Repo karbantartás, manifest, index, deploy | Az egész `screen-catalog/` mappa |

**Alapelv:** A Claude Design soha nem látja az egész projektet. Minden session = 1 feature, minimális scope.

---

## 2. Mappastruktúra

```
design/
  screen-catalog/          ← ez a repo gyökere
    index.html             ← GENERÁLT (ne szerkeszd kézzel!)
    manifest.json          ← GENERÁLT (ne szerkeszd kézzel!)
    workflow.md            ← ez a dokumentum
    screens/               ← a képernyő HTML fájlok helye
      [feature]-[screen].html
      ...
  wireframes/
    archive/
      b33-final/           ← korábbi build archívum (b33)
        *.html
      ...
    *.zip                  ← régi build zip-ek
```

---

## 3. Screen HTML metadata blokk (kötelező)

Minden képernyő HTML fájlnak tartalmaznia kell az alábbi blokkot a `<head>`-ben:

```html
<script type="application/json" id="screen-meta">
{
  "title": "Checkout — Szállítás kiválasztása",
  "feature": "checkout",
  "sprint": "Sprint 3",
  "status": "draft",
  "publish": true,
  "order": 10,
  "platform": "mobile",
  "version": "v1",
  "tags": ["cart", "delivery", "checkout"]
}
</script>
```

### Mezők magyarázata

| Mező | Kötelező | Értékek | Leírás |
|------|----------|---------|--------|
| `title` | ✅ | szöveg | Megjelenített cím az indexben |
| `feature` | ✅ | szöveg | Feature csoport (pl. "checkout", "reorder") |
| `sprint` | ✅ | "Sprint 1"–"Sprint N" | Sprint azonosító — csoportosításhoz |
| `status` | ✅ | `draft` / `review` / `approved` / `done` | Aktuális állapot |
| `publish` | ✅ | `true` / `false` | `false` = nem kerül az indexbe |
| `order` | ✅ | szám (10, 20, 30...) | Sprint-en belüli sorrend (10-es lépésközzel) |
| `platform` | — | `"mobile"` | Célplatform |
| `version` | — | `"v1"`, `"v2"` | Verziószám |
| `tags` | — | string tömb | Keresési/szűrési tagek |

**Konvenció az `order` mezőhöz:** Használj 10-es lépésközöket (10, 20, 30...), hogy könnyen lehessen közéjük szúrni.

---

## 4. manifest.json struktúra

A `manifest.json` mindig generált fájl — a CoWork agent hozza létre a screen HTML-ekből.

```json
{
  "meta": {
    "build": 1,
    "generatedAt": "2026-04-25T10:00:00+03:00",
    "description": "Generált fájl. Ne szerkeszd kézzel."
  },
  "screens": [
    {
      "file": "screens/checkout-delivery.html",
      "title": "Checkout — Szállítás kiválasztása",
      "feature": "checkout",
      "sprint": "Sprint 3",
      "status": "approved",
      "publish": true,
      "order": 10,
      "platform": "mobile",
      "version": "v1",
      "tags": ["cart", "delivery"]
    }
  ]
}
```

---

## 5. index.html működése

Az `index.html` dinamikusan olvassa be a `manifest.json`-t `fetch()`-chel.

### Megjelenítési logika
1. **Sprint csoportosítás** — numerikus sorrendben (Sprint 1, Sprint 2, ...)
2. **`order` alapú rendezés** — spriten belül növekvő sorrendben
3. **Státusz szűrők** — All / Approved / Review / Draft
4. **Sprint szűrők** — automatikusan generálva a manifest adataiból
5. **iframe preview** — minden kártya mutatja a képernyő miniatűrjét
6. **Build badge** — a manifest `meta.build` értékéből

### Amit soha nem kell kézzel szerkeszteni
- `index.html` — mindig generált
- `manifest.json` — mindig generált

---

## 6. CoWork agent workflow (lépésről lépésre)

### Új képernyő hozzáadása

```
1. Claude Design → exportált HTML letöltve
2. CoWork: fájl bemásolása → screens/ mappába
3. CoWork: metadata blokk ellenőrzése / hozzáadása
4. CoWork: catalog update futtatása (lsd. 7. fejezet)
```

### Catalog update folyamata (automatikus)

```
1. Beolvassa az összes screens/*.html fájlt
2. Minden HTML-ből kiolvassa a #screen-meta JSON blokkot
3. Validálja a kötelező mezőket (title, feature, sprint, status, publish, order)
4. Kiszűri a publish: false bejegyzéseket
5. Generálja a friss manifest.json-t (build++ )
6. Generálja a friss index.html-t (manifest alapján)
7. Opcionálisan: Netlify deploy
```

---

## 7. Netlify deploy (egyetlen parancs)

> ## 🛑 STOP — DEPLOY ELŐTT KÖTELEZŐ
>
> **SOHA ne deployolj automatikusan.**
> Minden deploy előtt explicit kérdezd meg a usert:
>
> **„Deployoljam? (ez 15 kreditet fogyaszt)"**
>
> Csak **igenlő válasz után** (`igen`, `deploy`, `mehet`, stb.) szabad elkezdeni a deployt.
> Ez nem opcionális — ez a legfontosabb szabály a deploy szekción belül.
>
> **Miért:** 1 production deploy = 15 Netlify kredit. Personal plan = 1 000 kredit/hó.
> Munkamenetenként 1 deploy a cél — ne deployolj minden apró változás után!

### Konfiguráció

| Paraméter | Érték |
|-----------|-------|
| Site | deakhus-catalog.netlify.app *(még nem létrehozva)* |
| Deploy módszer | Zip → curl API |
| API token | Netlify Bearer token |

### Deploy parancs (CoWork agent futtatja)

```bash
# 1. Flat deploy csomag összekészítése
# 2. Zip
cd /tmp/catalog-deploy && zip -r /tmp/catalog.zip .

# 3. Netlify API deploy
curl -s -H "Content-Type: application/zip"   -H "Authorization: Bearer <TOKEN>"   --data-binary "@/tmp/catalog.zip"   "https://api.netlify.com/api/v1/sites/<SITE_ID>/deploys"
```

### Deploy szabályok
- A zip **flat struktúra**: `index.html`, `manifest.json`, `screens/*.html` egy szinten
- Minden deploy lecseréli az összes fájlt (Netlify atomi deploy)
- Deploy előtt mindig fuss catalog update-et

---

## 8. Claude Design → CoWork átadási protokoll

### Claude Design session szabályok
- 1 session = 1 feature (pl. "checkout flow")
- Input: 1 referencia HTML (minél egyszerűbb: 4-5 elem, ne 30)
- Output: 1 önálló high-fidelity HTML fájl
- A session **nem lát** más feature HTML-eket

### Átadási lépések
```
[Claude Design] Képernyő kész
       ↓
[Export] HTML letöltés
       ↓
[CoWork] screens/ mappába másolás
       ↓
[CoWork] screen-meta blokk ellenőrzés
       ↓
[CoWork] catalog update futtatás
       ↓
[CoWork] Netlify deploy (opcionális)
```

---

## 9. Input HTML optimalizálás

A Claude Design sessionbe vitt referencia HTML-nek **minimális** kell legyen:

| Helyett | Inkább |
|---------|--------|
| 30 termék | 4–5 reprezentatív termék |
| Teljes scrollolható lista | 1 normál + 1 akciós + 1 elfogyott + 1 edge case |
| Összes variáció | Csak az aktuális feature variációi |

**Szabály:** minimum content, maximum pattern coverage.

---

## 10. Státuszok életciklusa

```
draft → review → approved → done
```

| Státusz | Jelentés | Szín |
|---------|----------|------|
| `draft` | Folyamatban, nem végleges | Sárga |
| `review` | Design review alatt | Kék |
| `approved` | Elfogadva, fejlesztőknek átadható | Zöld |
| `done` | Implementálva, lezárva | Szürke |

---

## 11. Plugin / Skill terv

Ez a workflow egy **CoWork plugin** része lesz. A plugin képességei:

```
catalog update   → manifest + index regenerálás
catalog deploy   → Netlify deploy
catalog add      → új screen hozzáadása + metadata ellenőrzés
catalog status   → aktuális állapot kilistázása
```

Egyetlen parancs a teljes pipeline-ra:
```
catalog deploy
```

Ez automatikusan: scan → validate → manifest++ → index gen → zip → Netlify API.

---


---

## 13. Cowork + Claude Code szinkron protokoll

> Frissítve: 2026-04-29 — Build #60 reconciliation után

### Probléma amit ez megold

Cowork és Claude Code **párhuzamosan** szerkeszthetik az index.html és manifest.json fájlokat. Ha nem koordinálnak, build szám divergencia és ghost entry keletkezik.

### Szinkron szabályok

**Az `index.html` inline `const MANIFEST = {...}` az egyetlen igazság forrás.**

```
index.html build > manifest.json build → Claude Code dolgozott közbülső
  → Vedd az index.html-t alapul, ne a manifest.json-t

manifest.json build > index.html build → Cowork dolgozott közbülső
  → Szinkronizáld az index.html-be a manifest.json-t
```

**Build szám számítása minden íráskor:**
```python
# HELYES:
idx_build = extract_build_from_index_html()
mf_build  = manifest['meta']['build']
new_build = max(idx_build, mf_build) + 1

# HELYTELEN:
new_build = manifest['meta']['build'] + 1  # figyelmen kívül hagyja az index.html-t!
```

**Ghost entry ellenőrzés (deploy előtt kötelező):**
```python
for screen in manifest['screens']:
    assert os.path.exists(f"screens/{screen['file'].split('/')[-1]}"), f"GHOST: {screen['file']}"
```

### Reconciliation folyamat (ha divergáltak)

```
1. Olvasd be az index.html inline MANIFEST-jét → ez a truth
2. Olvasd be a manifest.json-t → keresd a különbségeket
3. Ha index.html build > manifest.json build:
     → manifest.json = index.html MANIFEST (build változatlanul)
4. Ha manifest.json-ban van ghost entry (fájl nem létezik):
     → Töröld az entryt
5. Szinkronizáld mindkét fájlt ugyanarra a build számra
6. Deploy
```


## 14. Pre-deploy check — kötelező protokoll

> ## 🛑 DEPLOY ENGEDÉLY — KÖTELEZŐ LÉPÉS
>
> **Mielőtt bármit deployolnál:** kérdezd meg a usert:
> **„Deployoljam? (ez 15 kreditet fogyaszt)"**
> Csak igenlő válasz után folytasd!

**Minden deploy előtt futtasd a pre-deploy checket!**

```python
# Futtatás Cowork session-ből (inline Python — nem bash path!):
python3 << 'PYEOF'
import os, json, re, sys
entries = list(os.scandir('/sessions/adoring-gifted-gates/mnt/'))
real_mount = next(e.path for e in entries if 'Dea' in e.name and e.stat().st_mode & 0o777 == 0o700)
# ... exec the full script
exec(open(os.path.join(real_mount, 'design/screen-catalog/pre-deploy-check.py')).read())
PYEOF
```

A script ellenőrzi:
1. ✅ index.html build olvasható
2. ✅ manifest.json build olvasható  
3. ✅ Build számok egyeznek
4. ✅ Nincs ghost entry (manifest → lemez)
5. ✅ Nincs orphan file (lemez → manifest)
6. ✅ Minden screen-nek van screen-meta blokkja
7. ✅ Minden screen-nek van back-to-catalog linkje
8. ⚠️ Nincs stray HTML a screens/-en kívül (pl. development/)

**Ha bármelyik ❌ → deploy TILOS!**

## 15. Root cause napló — ismétlődő hibák

### analytics-dictionary-v2.2 kiesés (2026-04-29, recurring issue)

**Tünet:** az analytics oldal "megint nem látszik" a deployolt katalóguson.

**Root cause:** A fájl a `development/analytics/` mappában volt, nem a `design/screen-catalog/screens/`-ben. A Netlify deploy zip csak a `screen-catalog/` tartalmát veszi bele — minden deploy felülírja az egész site-ot, és `development/` sosem kerül bele.

**Fix:**
1. Fájl áthelyezve: `development/analytics/analytics-dictionary-v2.2.html` → `screens/v0.2-analytics-dictionary.html`
2. screen-meta blokk hozzáadva
3. back-to-catalog link javítva (`href="index.html"` → `href="../index.html"`)
4. manifest.json + index.html frissítve (build #62, 15 screen)
5. `pre-deploy-check.py` létrehozva — 8. check figyelmeztet ha stray HTML van

**Végleges megoldás:** A pre-deploy check ⚠️ warninggal jelez ha `.html` fájl van `development/` vagy más, screens/-en kívüli mappában.


## 16. Tab struktúra — döntési szabályok

### A két tab és logikájuk

| Tab | MANIFEST kulcs | Mi kerül ide |
|-----|---------------|--------------|
| **Képernyők** | `MANIFEST.screens[]` | UI wireframe, app screen, interakciós flow, komponens |
| **Dokumentáció** | `MANIFEST.docs[]` | Referencia dokumentum, szótár, business model, analytics spec |

---

### Tab 1 — Képernyők

**Forrás:** `MANIFEST.screens[]`  
**Megjelenítés:** sprint szerinti csoportokban, státusz-szűrőkkel

#### Screen entry kötelező mezők
```json
{
  "file": "screens/v0.3-feature-name.html",
  "title": "Feature — Leírás",
  "feature": "feature-slug",
  "sprint": "Sprint 3",
  "status": "draft",
  "tags": ["DH-XXX"],
  "order": 10,
  "description": "Rövid leírás"
}
```

#### Sprint csoportok (megjelenítési sorrend)
| Sprint érték | Mikor használd |
|---|---|
| `Sprint 2` | v0.2 release — analytics, bugfix screének |
| `Sprint 3` | v0.3 release — savings engine, core loop |
| `Sprint 4` | v0.4 release — natív mobil experience |
| `Sprint 5` | v0.5 release — növekedési platform |
| `Legal` | Jogi dokumentumok wireframe-jei (ÁSZF, Privacy, GDPR) |

#### Státusz értékek
| Status | Jelentés | Filter gomb |
|--------|----------|-------------|
| `draft` | Munka alatt | Draft |
| `review` | Visszajelzésre vár | Review |
| `approved` | Jóváhagyva, ready | Approved |
| `done` | Implementálva | Done |

---

### Tab 2 — Dokumentáció

**Forrás:** `MANIFEST.docs[]`  
**Megjelenítés:** kategória-kártyák, ikon + verzió + live badge

#### Doc entry kötelező mezők
```json
{
  "file": "screens/v0.2-doc-name.html",
  "title": "Dokumentum neve",
  "desc": "Egy soros leírás",
  "icon": "analytics",
  "version": "v2.2",
  "tags": ["DH-XXX", "tag"],
  "updated": "2026-04-29",
  "live": true
}
```

#### Icon típusok és kategóriák
| Icon | Szín | Mikor |
|------|------|-------|
| `analytics` | Lila (#5B21B6) | Firebase events, tracking, GA |
| `design` | Kék (#1E40AF) | Design system, component docs |
| `business` | Amber (#92400E) | Business model, economics, KPI |
| `legal` | Piros (primary) | Jogi docs (ha NEM wireframe) |

#### Jelenlegi docs kategóriák
| Kategória | Tartalom |
|-----------|----------|
| Analytics | Analytics Dictionary v2.2 — Firebase event szótár |
| Business | Economic Loop — flywheel és unit economics |

---

### Döntési fa: melyik tab alá kerüljön?

```
Új HTML fájl hozzáadása?
│
├─ Ez egy UX/UI WIREFRAME vagy APP SCREEN?
│   (felhasználói nézet, interakció, navigáció)
│   → KÉPERNYŐK tab (screens[])
│   → sprint = aktuális sprint (Sprint 3/4/5)
│   → file prefix: v0.X-feature-name.html
│
├─ Ez egy JOGI DOKUMENTUM wireframe-je?
│   (ÁSZF, Privacy Policy, GDPR, cookie policy)
│   → KÉPERNYŐK tab (screens[])
│   → sprint = "Legal"
│   → feature = "legal"
│
└─ Ez egy REFERENCIA DOKUMENTUM?
    (analytics szótár, business model, design spec, KPI framework)
    → DOKUMENTÁCIÓ tab (docs[])
    → icon = analytics / design / business / legal
    → kategória = Analytics / Business / Design / Legal
    → file: screens/ mappában kell lennie!
```

#### Gyors példák
| Fájl | Tab | Sprint/Kategória |
|------|-----|-----------------|
| `v0.3-savings-counter.html` | Képernyők | Sprint 3 |
| `v0.5-favorites-v3.html` | Képernyők | Sprint 5 |
| `aszf-wireframe-v2.html` | Képernyők | Legal |
| `v0.2-analytics-dictionary.html` | Dokumentáció | Analytics |
| `economic-loop-v1.html` | Dokumentáció | Business |

---

### ⚠️ Kritikus szabályok

1. **MINDEN fájlnak a `screens/` mappában kell lennie** — még a docs tab fájljai is!
2. **Docs tab fájljainál a `file` path** `screens/v0.X-name.html` formátumú legyen
3. **Sosem kerülhet wireframe a docs-ba**, és sosem kerülhet referencia doc a screens-be
4. **Új sprint indításakor** add hozzá a sprint nevét a manifest entries-hoz és a workflow doc táblájához

## 17. Wireframe craft konvenciók — Szabolcs preferenciái

> Hozzáadva: 2026-05-09 — DH-173 product-variations szülötte. **Új session esetén is tartsd be ezeket a mintákat**, ne találd ki újra a struktúrát képernyőnként. Referencia implementációk: [`screens/v0.4-courier-route.html`](screens/v0.4-courier-route.html) és [`screens/v0.4-rural-delivery.html`](screens/v0.4-rural-delivery.html).

### 17.1 Felső struktúra (kötelező)

Minden új self-contained katalógus képernyő (NEM iframe-resource) a következő blokkokkal kezdődik, **ebben a sorrendben**:

```html
<!-- 1. Fixed back-to-catalog gomb (sötét kör, top-left) -->
<a href="../index.html" class="back-to-catalog" title="Vissza a katalógusba">…</a>

<!-- 2. Másolható breadcrumb (.dh-crumb + .dh-copy) -->
<div class="dh-crumb">
  <span class="crumb-text">
    <strong>Feature neve</strong><span class="sep">›</span>Képernyő neve<span class="crumb-file">v0.X-fajl.html</span>
  </span>
  <button type="button" class="dh-copy"
          data-ref="[DH] Feature neve › Képernyő neve (v0.X-fajl.html)"
          aria-label="Hivatkozás másolása"></button>
</div>

<!-- 3. Page intro: eyebrow + h1 + p -->
<div class="page-intro">
  <div class="eyebrow">Sprint X · DH-XXX · 1 mondatos hook</div>
  <h1>Egyértelmű képernyő-cím (kérdés vagy állítás)</h1>
  <p>2-3 mondatos összefoglaló mit látunk és miért.</p>
</div>

<!-- 4. .panels grid: auto-fit minmax(min(100%, 448px), 1fr) -->
```

A `.dh-copy` JS (toast + clipboard fallback) kötelezően ott van — másold át a courier-route.html `<script>` blokk végéből. Minden panel-meta-ban is legyen egy `.dh-copy` per-panel hivatkozás-másolásra.

### 17.2 Panel struktúra

Minden panel:
```html
<section class="panel">
  <div class="panel-meta">
    <span class="num">A</span>  <!-- A/B/C/D számozás -->
    <span class="ttl">Panel cím <span class="muted">· kontextus</span></span>
    <button type="button" class="dh-copy" data-ref="[DH] … › A — Panel cím (…)"></button>
  </div>
  <!-- (opcionálisan tabok, kívül a screen-en — lásd 17.3) -->
  <div class="screen">…</div>
</section>
```

### 17.3 Tabok ALWAYS a phone framen kívül

Ha egy panelen több variánst akarsz (pl. termék típus, állapot-snapshotok), a kapcsoló **a `.screen` FÖLÖTT, a `.panel`-en BELÜL** legyen — soha ne a `.screen` belsejében (`.scr-header` alatt vagy bármi módon a phone frame-be ékelve). A tab-row egy önálló `<div class="type-tabs">` blokk a `panel-meta` után, a `.screen` előtt. A frame magassága fix marad, csak a `.scr-body` tartalma cserélődik.

### 17.4 Phone frame architektúra (scroll fix)

A `.screen` egy fix magasságú flex column (760px). Belül **HÁROM réteg, mindegyik flex-shrink kontroll**:

```css
.screen        { display: flex; flex-direction: column; height: 760px; overflow: hidden; }
.scr-header    { flex-shrink: 0; }              /* sticky top */
.scr-body      { flex: 1; overflow-y: auto; }   /* az EGYETLEN scrollolható réteg */
.scr-cta       { flex-shrink: 0; }              /* sticky bottom CTA */
.scr-nav       { flex-shrink: 0; }              /* bottom nav */
```

**SOHA ne használj `position: absolute`-ot a CTA-ra vagy bottom-nav-ra a phone framen belül** — flex-shrink:0 elemekkel oldd meg, mert az absolute pozíciójú elemek átfedik a tartalmat és törik a scrollt. Ez a DH-173 első iterációjának hibája volt.

A `.scr-body` `display: flex; flex-direction: column;` legyen, hogy a `.variant` gyermekek (display:none/flex toggle) tisztán cserélődjenek.

### 17.5 Panels grid méretezés

```css
.panels {
  max-width: 1480px;
  display: grid;
  gap: 28px 24px;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 448px), 1fr));
  align-items: start;
}
.panel.panel-wide { grid-column: 1 / -1; }   /* széles panel pl. A4 dokumentumhoz */
```

Phone frame `.screen` mindig `max-width: 448px`, magasság `760px` fix. Dokumentum-frame (pl. A4) `aspect-ratio: 1 / 1.414`, `max-width: 794px`, `panel-wide` panelben.

### 17.6 Anti-bans (a DESIGN.md-n felül, wireframe-specifikusan)

1. **NE rakj tab-ot a phone framen belülre** — mindig kívül, a panel-meta után.
2. **NE használj `position: absolute`-ot a phone frame CTA-ra/nav-ra** — flex-shrink:0 a megoldás.
3. **NE hagyd ki a másolható breadcrumb-ot** — minden self-contained képernyőn legyen `.dh-crumb` + `.dh-copy`.
4. **NE használj em dash-t a copy-ban** — `·`, `:`, vesszó vagy zárójel helyettesíti.
5. **NE használj `user-scalable=no`-t** a viewport meta-ban — WCAG 1.4.4 sértés.
6. **Modal NEM első ötlet** — inline expand vagy bottom-sheet előbb (pl. cart "Módosítás" → `.edit-inline` a kártyán belül).
7. **Iframe-shell esetén** (mint v0.4-rural-delivery.html) a tab-ok a header-en belül, a `<main>` iframe pedig csak a sub-screen-t mutatja — NE keverj iframe-shellt és panels grid-et egy fájlban.

### 17.7 Fájlnév és metadata konvenció

- Fájlnév: `v{verzió}-{feature-slug}.html` — pl. `v0.4-product-variations.html`
- A `screen-meta` JSON `id` egyezzen a fájlnévvel kiterjesztés nélkül.
- A `tags` tartalmazza a Jira ticket azonosítót (pl. `"DH-173"`).
- A nyelvi megjegyzést (HU wireframe / RO production) HTML-kommentben rögzítsd a `<head>` elején.

### 17.8 Build sync szabály

Új képernyő esetén **mindig frissítsd MIND a `manifest.json`-t MIND az `index.html` inline `const MANIFEST` blokkját** azonos build számmal és entry-vel. A 13. szekció reconciliation szabálya elsőbbséget ad az `index.html`-nek divergencia esetén.

---

## 12. Verzióhistória

| Dátum | Esemény |
|-------|---------|
| 2026-04-25 | screen-catalog/ létrehozva, dinamikus index.html, manifest.json, workflow.md |
| — | b33 wireframes archiválva → design/wireframes/archive/b33-final/ |
| 2026-04-29 | Build #60 reconciliation — Cowork+Claude Code szinkron, ghost entry eltávolítva, deploy |
| 2026-04-29 | Build #61 — QR SVG fix (kassza-qr.html: inline segno SVG, CDN-mentes) |
| 2026-04-29 | Build #62 — analytics-dictionary-v2.2 integrálva screens/-be, pre-deploy-check.py létrehozva |
| 2026-05-09 | Build #87 — v0.4-product-variations.html (DH-173) hozzáadva; 17. szekció (Wireframe craft konvenciók) dokumentálva |

*Ez a dokumentum a DH Screen Catalog CoWork plugin alapja lesz.*
