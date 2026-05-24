---
title: Microsite Factory — Fejlesztési és Deploy Metodológia
version: 0.1
date: 2026-05-11
author: Becze Szabolcs
status: design · learning prompt
description: Hogyan fejleszt különböző sessionökben különböző projektekhez gyors landing oldalakat egy ember Claude Code-dal, /impeccable polish-sal, Cloudflare Pages deploy-jal. Ez egy hosszú tanulási prompt — szándékosan részletes.
id: d460ea46-5960-4329-b471-667991aba6ef
index_schema_version: 1
---

# Microsite Factory — Fejlesztési és Deploy Metodológia

> **Hogyan használd ezt a dokumentumot:** Ez nem reference, hanem **tanulási anyag**. Olvasd lassan, mindegyik szekciónál tedd fel magadnak a kérdést: „elfogadom-e ezt az alapelvet?" Ha nem, jelöld meg, és a sprint végén beszéljük át. A metodológia akkor működik, ha a benne lévő konvenciók *automatikusan jönnek a kezed alá* — addig olvasd újra, amíg nem kell visszanézned.

---

## 0. Cél és scope (mi a Microsite Factory)

A Microsite Factory egy **AI-asszisztált landing-oldal gyár**. Egy ember (te) Claude Code-dal és Cloudflare Pages-szel **5-15 perc alatt** ki tud tolni egy új marketing micro-website-ot egy ügyfél domainre, *anélkül* hogy:

- minden ügyfélhez külön workflow-t kelljen kitalálnod
- minden projekt másmilyen mappastruktúrát használjon
- emlékezned kelljen melyik token, melyik domain, melyik build-szám hová tartozik
- bárhol kézzel kelljen FTP-zni / dashboardban file-okat húzgálni

**Mit IS csinál:**
- Generálj egy új microsite-ot (sablonból vagy nulláról)
- Fejleszd `/impeccable`-lel iteratívan, lokálisan
- Validáld pre-deploy script-tel
- Deploy staging URL-re egy paranccsal
- Promote production-re custom domainnel egy paranccsal

**Mit NEM csinál (legalábbis v0.1-ben):**
- Multi-page szerves website-ok (cms-szerű blog, e-commerce, kliens-loginnal védett zónák)
- Dynamic backend logika (űrlap fogadás Workers-szel külön capability lesz)
- Server-side rendering, framework-alapú build (Next.js, Astro)
- Image-pipelining lokálisan (CF Images / Transformations átveszi)

A Microsite Factory **statikus HTML/CSS/JS** + opcionálisan egy-két Cloudflare Worker. Ennek az egyszerűségnek tudatos szerepe van: **minden microsite, amelyet kiállítasz, ugyanazon módszerrel debug-olható**.

---

## 1. Mentális modell — három réteg

A Microsite Factory három absztrakciós szinten él. Ha bármikor zavarba jössz, kérdezd meg magadtól: *„melyik rétegben vagyok most?"*

```
   ┌─────────────────────────────────────────────────────────────┐
   │ RÉTEG 3: PROJEKTEK (élő microsite-ok)                       │
   │   02_Areas/<ügyfél>/microsite/                              │
   │   02_Areas/<ügyfél>/<kampány>-microsite/                    │
   │   Per-microsite tartalom: HTML, manifest, config, history   │
   └─────────────────────────────────────────────────────────────┘
                              ▲ használja
   ┌─────────────────────────────────────────────────────────────┐
   │ RÉTEG 2: CAPABILITY (Microsite Factory mint eszközcsomag)   │
   │   00_Prompts/BDOS/capabilities/web-publishing/              │
   │   - methodology.md (ez a fájl)                              │
   │   - infrastructure.md (Cloudflare, tokenek, hostok)         │
   │   - prototype/microsite_deploy.py (deploy CLI)              │
   │   - agents/ (jövő: deploy-agent, polish-agent, seo-agent)   │
   │   - .env (token, account ID)                                │
   └─────────────────────────────────────────────────────────────┘
                              ▲ használja
   ┌─────────────────────────────────────────────────────────────┐
   │ RÉTEG 1: BDOS + CLAUDE CODE (a meta operációs rendszer)     │
   │   00_Prompts/BDOS/                                          │
   │   - agents/ (Librarian + jövőbeli BDOS agentek)             │
   │   - /impeccable, /lib-find, /lib-index, /lib-audit          │
   │   - persistent state, retrieval-based cognition             │
   └─────────────────────────────────────────────────────────────┘
```

**A három réteg szigorúan elválik:**

- **Réteg 3** *(projekt)* csak a saját tartalmáról tud (HTML, brief, history). Nem tudja, hogy Cloudflare van mögötte vagy Netlify.
- **Réteg 2** *(capability)* tudja a deploy mechanikát, a tokeneket, a hostok közti különbséget. Nem tud konkrét ügyfélről.
- **Réteg 1** *(BDOS)* az ember-AI kollaboráció alapszintje. Skill-ek, slash command-ok, agentek élnek itt.

**Miért fontos ez:** ha pl. holnap át akarsz váltani Cloudflare-ről egy másik hostra, **csak a Réteg 2-t cseréled**, és minden projekt automatikusan az új deploy-pipeline-on megy. Ha új ügyfelet veszel fel, **csak Réteg 3-ban hozol létre új mappát**, és a metodológia minden lépése azonnal alkalmazható.

---

## 2. Egy microsite projekt anatómiája (Réteg 3 részletesen)

Minden microsite projekt **ugyanezt a struktúrát** kapja. Ez nem öncélú: a deploy script, a polish workflow, a státuszkövetés mind ezen a konvención áll.

```
02_Areas/<ügyfél>/microsite/                  ← projektgyökér
├── CLAUDE.md                                 ← projekt-specifikus instrukciók AI-nak
├── README.md                                 ← ember-olvasható brief
├── brief.md                                  ← üzleti brief (cél, audience, ajánlat)
├── microsite.config.json                     ← deploy konfiguráció
├── manifest.json                             ← build metadata
├── history.md                                ← deploy napló (ember-olvasható)
│
├── src/                                      ← FORRÁS — itt dolgozol
│   ├── index.html
│   ├── styles.css                            (vagy /assets/css/main.css)
│   ├── script.js                             (vagy /assets/js/main.js)
│   ├── assets/
│   │   ├── img/
│   │   └── icons/
│   └── sections/                             (opcionális — komponens-bontás)
│
├── dist/                                     ← BUILD output — ez deployolódik
│   └── (generált — `microsite-build` script tölti meg)
│
├── pre-deploy-check.py                       ← validátor (opcionális)
│
└── archive/                                  ← régi verziók (build-számmal)
    ├── v0.1-2026-05-11/
    └── v0.2-2026-05-13/
```

### A kulcs fájlok szerepe

**`CLAUDE.md`** — projekt-specifikus AI-instrukciók. Tartalmazza:
- ügyfél neve, brand-hangja, tabu szavak
- design-irányelvek (szín, tipográfia, motion-preferencia)
- *„soha ne tedd ezt"* lista (pl. „ne használj stock-fotót")
- a CTA pontos szövegét, telefonszámot, kontakt-formot
- ki vagyok én az ügyfél szemszögéből (Szabolcs mint külső consultant vs in-house designer stb.)

**`brief.md`** — üzleti brief, amit a kick-off interjún rögzítesz:
- 1 mondatos value proposition
- 3 fő benefit
- target persona (1-2)
- konverziós cél (lead form? hívás? letöltés? esemény-regisztráció?)
- siker-metrika (lead/hét? CTR?)

**`microsite.config.json`** — gép-olvasható deploy konfig:
```json
{
  "project_name": "deakhus-microsite",
  "cf_pages_project": "deakhus-microsite",
  "production_domain": "deakhusuzem.hu",
  "staging_domain": "staging.deakhusuzem.hu",
  "version": "0.3.1",
  "owner": "Becze Szabolcs",
  "client": "Deák Húsüzlet",
  "created": "2026-05-11",
  "tags": ["food", "local", "premium"]
}
```

**`manifest.json`** — build-metadata (a DH-konvencióból átvéve):
```json
{
  "build": 47,
  "version": "0.3.1",
  "generated_at": "2026-05-11T14:32:00+02:00",
  "files": [
    {"path": "/index.html", "hash": "..."},
    {"path": "/assets/css/main.css", "hash": "..."}
  ]
}
```

A `build` szám **monoton növekszik**, sosem reset-elődik (még major release-nél sem). Ez a deploy-történet egyetlen igazságforrása.

**`history.md`** — ember-olvasható deploy-napló:
```markdown
## Build 47 (2026-05-11 14:32)
- prod: ✅ https://deakhusuzem.hu (deploy_id: abc123)
- staging: ✅ https://staging.deakhusuzem.hu
- changes: hero CTA átszínezve narancsra; alsó form egyszerűsítve
- jóváhagyta: Szabolcs
- /impeccable round: 3

## Build 46 (2026-05-10 09:18)
- staging only ✅ — prod nem ment
- changes: új második szekció (USP grid)
...
```

---

## 3. A development lifecycle — öt fázis

Minden microsite **ezt az öt fázist** futja végig. A fázisok közt kapcsoló pontok vannak (commit-szerűen jelöld) — ne keverj össze két fázist egy lépésben.

### Fázis 1 — BRIEF (15-30 perc)

**Cél:** annyi információt összeszedni, hogy a polish-fázist ne kelljen ismételni stratégiai döntések miatt.

**Lépések:**
1. Új projektmappa: `02_Areas/<ügyfél>/microsite/`
2. Másold be a sablont: `cp -r 00_Prompts/BDOS/capabilities/web-publishing/templates/microsite-skeleton/* .` (későbbi iterációkban lesz template)
3. Töltsd ki a `brief.md`-t. **NE ugord át** — a brief gyengesége exponenciálisan többszöröződik a polish-fázisban.
4. Töltsd ki a `CLAUDE.md`-t a projekt-specifikus konvenciókkal (brand-hang, no-go listák).
5. Töltsd ki a `microsite.config.json`-t a deploy-paraméterekkel (domain név, projekt név).
6. **Checkpoint:** olvasd át a brief-et. Ha 30 másodperc alatt *nem tudod elmondani a microsite értelmét egy ismerősnek*, a brief még nem kész.

**Anti-pattern:** kerüld a *„majd menet közben kitaláljuk a value prop-ot"* csapdát. A polish-fázisban Claude **a brief alapján** generálja a tartalmat — ha a brief homályos, a HTML is homályos lesz.

---

### Fázis 2 — BUILD (30-90 perc)

**Cél:** az első futtatható HTML — *„hello world" szintű* hierarchiával, helyes meta-tag-ekkel, semantic HTML5-tel.

**Lépések:**
1. Új Claude Code session a projektmappában (`cd 02_Areas/<ügyfél>/microsite/`).
2. Indítsd a sessiont *kontextus-rekonstrukcióval*: a Claude olvassa be a `CLAUDE.md`-t, `brief.md`-t. Egy mondatban kéred meg, hogy summázza vissza a célt — ha a summary nem stimmel, a brief még nem elég jó (vissza Fázis 1-re).
3. Kérd meg, hogy generálja a `src/index.html`-t a brief-ből. Add meg a szekciókat (hero, USP, social proof, CTA, footer — vagy bármi a briefben).
4. Indítsd a lokális preview-t (lásd 4. fejezet).
5. **Checkpoint:** a HTML semantic? (h1, section, nav, footer használat). Mobile-szerű viewportban olvasható? Alt-szöveg minden képnél?

**Anti-pattern:** ne kérd Claude-tól a CSS-t és JS-t a HTML-lel egyszerre. Külön kérdés:
- *„Generálj `src/index.html`-t a brief alapján, csak a struktúra fontos most, inline styling NE legyen."*
- *„Most generáld a `src/styles.css`-t. Használj design tokeneket a brand színekhez."*
- *„Most a JS — csak az interakciókat, nincs framework."*

A szétválasztás azért fontos, mert a polish-fázisban (Fázis 3) `/impeccable` külön nyúl ehhez a 3 rétegekhez. Ha mindent egyben generálsz, a polish-iterációk konfliktusba ütköznek.

---

### Fázis 3 — POLISH (több iteráció, projektenként változó)

**Cél:** abból ami „működik" (Fázis 2) eljutni odáig, hogy *„be merném mutatni"*.

**Hogyan használd `/impeccable`-t:**

A `/impeccable` skill BDOS-szintű (Réteg 1) képesség: UI/UX kritikát, hierarchia-javítást, vizuális polish-t ad. Iteratívan használd, **nem egyszer**:

**Iteration 1 — Struktúra-polish:**
```
/impeccable

A src/index.html struktúrája jelenleg ilyen [paste vagy szabadon]. 
A brief.md alapján: a cél lead-generálás családi vásárlóknak. 
Adj kritikát csak a HTML-struktúrára: hierarchia, semantic tag-ek, 
section sorrend. Vizuális dolgokat hagyd ki most. Adj 3-5 konkrét 
javítási javaslatot.
```

**Iteration 2 — Visual hierarchy:**
```
/impeccable

A src/styles.css mostani állapota [paste]. A hero section dominál 
de a USP grid túl halvány. Tipográfia: heading hierarchia nem 
tisztult ki. Adj 3-5 konkrét CSS-változást.
```

**Iteration 3 — Micro-interactions:**
```
/impeccable

A landing oldal *technikailag* kész. Most kérnék 2-3 mikro-interakciót: 
hover state-ek, scroll-trigger animáció, CTA gomb pulse vagy hasonló. 
Tartózkodj a túlzástól — 2026 minimal aesthetic.
```

**Iteration 4 — Copy & UX writing:**
Itt áthozhatod a `design:ux-copy` skill-t a Réteg 1-ből:
```
/ux-copy

A CTA gomb most: „Foglalj asztalt". A kontext: Deák Húsüzlet boltja, 
nem étterem — a CTA itt rosszul illeszkedik. Adj 5 alternatívát, 
mindegyik egy mondatban indokold miért működik.
```

**A polish-iterációk maximális száma:** ne legyen több 5-7 körnél. Ha a 6. körön is *„még egy kicsit"*, gondolj rá hogy:
1. A brief talán nem volt elég pontos (vissza Fázis 1-re egy mini-update-tel)
2. Túl-engineereled a design-t (a marketing landingnél *„elég jó"* gyorsabban convertál mint *„tökéletes"*)
3. Nem te vagy a cél-célközönség (mutasd meg az ügyfélnek staging URL-en, ne magadnak iterálj)

**Checkpoint Fázis 3 végén:** lokálisan végignézed mobile- és desktop-viewportban. Ha mindkettő OK, mehet a Fázis 4.

---

### Fázis 4 — VALIDATE (5-15 perc)

**Cél:** a deploy előtti utolsó technikai szűrő, amit *AI nem szabad átugorjon*.

A `pre-deploy-check.py` script futtatása (vagy egy minimal beépített check). Mit ellenőriz:
- `index.html` létezik
- Minden image `src=` ténylegesen létezik (no broken links)
- `<title>`, `<meta name="description">`, OG-tagek kitöltve (SEO)
- Manifest.json build száma az index.html-ben hivatkozott build-számmal egyezik (DH-konvenció)
- Nincs lokális `file://` referencia (Claude néha betesz tévedésből)
- Nincs `localhost`, `127.0.0.1` referencia
- Inline secret-szerű string-ek nincsenek (`sk-`, `Bearer`, `AKIA` prefixek)
- Favicon és Apple-touch-icon létezik
- HTML validátor pass (opcionálisan)
- Lighthouse score előírt küszöb fölött (opcionálisan, Browser Run-nal automatizálható, későbbi iteráció)

**A script kötelezően exit 1-gyel kilép validation failure esetén** — így a deploy nem indul el. Ne tedd ezt a checklist-et „opcionálissá" mert egyszer fáradtan átengeded és prod-ra megy egy törött link.

---

### Fázis 5 — DEPLOY (2-5 perc)

**Cél:** atomi, visszafordítható, **kéthelyű** publikálás (staging → production).

#### 5.1 Staging deploy

```bash
cd "02_Areas/<ügyfél>/microsite/"

# Aktiválod a CF tokent (egyszer per shell session)
export $(cat ../../00_Prompts/BDOS/capabilities/web-publishing/.env | xargs)

# Build (ha kell — most még csak cp src/ dist/, később lehet asset-pipeline)
microsite-build .

# Pre-deploy check
python pre-deploy-check.py

# Staging deploy
python "$VAULT/00_Prompts/BDOS/capabilities/web-publishing/prototype/microsite_deploy.py" \
  ./dist --project=<cf-pages-project> --branch=staging
```

Output: `✓ Deployed: https://staging.<project>.pages.dev` és/vagy `https://staging.<custom-domain>.hu`

**Csak ezután:** nyisd meg a staging URL-t, **két különböző böngészőben** (Chrome + Safari pl., vagy laptop + telefon). Ha bármi vizuálisan vagy szövegben nem stimmel, **vissza Fázis 3-ra**, ne fixáld közvetlenül production-on.

#### 5.2 Production deploy

Csak akkor menj tovább, ha a staging URL **abszolút OK**. A production parancs ugyanaz, csak `--branch=staging` nélkül:

```bash
python "$VAULT/00_Prompts/BDOS/capabilities/web-publishing/prototype/microsite_deploy.py" \
  ./dist --project=<cf-pages-project>
```

Output: `✓ Deployed: https://<deploy-id>.<project>.pages.dev` — ez a production alias, és a custom domain (`example.com`) is már ezt mutatja, ha a domain be van kötve.

#### 5.3 Post-deploy

1. **Tedd be a `history.md`-be** a build számot, dátumot, változtatást, deploy ID-t.
2. Bump-old a `microsite.config.json` version mezőjét.
3. Commit. *(Ha git-ezve van a projektmappa — a vault-on belüli mappáknál ez a vault root commit-ja.)*
4. Cache purge (opcionálisan, `~/.config/microsite-factory/cache-purge.sh`-ben automatizálva — későbbi iteráció).
5. Notification a Cloudflare-ből (Notifications szekció, deploy-success/failure email).

---

## 4. Lokális development workflow (Fázis 2-3 részlete)

A Microsite Factory nem futtat dev-szervert (nincs Vite, nincs webpack). A microsite **statikus HTML** — közvetlenül megnyitod a fájlt a böngészőben.

### Quick preview módok

**Mód A — Live Server / Five Server VS Code extension:**
- Jobb klikk az `src/index.html`-en → „Open with Live Server"
- Auto-reload szerkesztéskor
- Best for: gyors iteráció

**Mód B — Python `http.server`:**
```bash
cd src/
python -m http.server 8000
# nyisd: http://localhost:8000
```
- Hasznos ha `fetch()` van a JS-ben (file:// protokollnál néha CORS-zik)

**Mód C — Cloudflare Wrangler dev (csak Workers mellett):**
```bash
wrangler pages dev ./src
```
- Pages-szel teljes parityt ad, Workers Functions tesztelhető
- Lassabb mint A vagy B

**Mód D — Direct file:// (legszimplább):**
- `Cmd+O` Finder-ből → megnyitod az `index.html`-t
- Hátrány: CORS-restrictionök (`fetch()`-ek failhetnek)
- Előny: nincs setup

Default választás: **Mód A** (Live Server VS Code-ban) — ezt használd, ha nincs külön okod másra.

### Mobile testing lokálisan

Mód B esetén, miután elindítottad a Python server-t:
1. Macen: `System Settings → Network → Wi-Fi → Details → IP cím`
2. Telefonon a Wi-Fi-n: `http://192.168.X.Y:8000`
3. Reloadolhatsz, valódi mobile-ban látod

Ezt mindenképp tedd meg a Fázis 3 vége előtt — a desktop-preview hazudik a mobile-tipográfiáról.

---

## 5. Hogyan dolgozz **több projekttel párhuzamosan, különböző sessionökben**

A Microsite Factory egyik fő ígérete: **bárhol, bármikor folytatható** munka. Két ügyfél microsite-jának egyszerre kéne haladnia — ez nem kihívás, ha a metodológiát betartod.

### Munkamenet-protokoll (session-handling)

**Session start (új vagy folytatott):**
1. Először `cd` a projekt mappájába: `cd 02_Areas/<ügyfél>/microsite/`
2. **Claude Code automatikusan beolvas:** `CLAUDE.md` (projekt-spec), és ha a vault root-tól indítottad, akkor az `02_Areas/<ügyfél>/CLAUDE.md`-t is.
3. Első kérdésed Claude-nak: *„Mi a status? Hol tartunk?"* — Claude visszaolvassa a `history.md`-t és az utolsó iterációt.
4. Ha más AI session-ben (pl. ChatGPT, Perplexity) is fut munka erről a microsite-ról, a `brainstorm/` mappa (DH-mintájú) tartalmazza a `brainstorm_<topic>.md`-t. Ezt is olvastasd be.
5. **Lokális preview indítása** — minden új session-ben újraindítod (a Live Server / Python server nem perzisztens).

**Session end:**
1. Update-eld `history.md`-t (mit csináltál ebben a sessionben — két sor elég)
2. Update-eld a `manifest.json` build számát ha új build készült
3. Ha félig kész state-ben hagyod, írd `OPEN_QUESTIONS.md`-be (vagy a `history.md` végére) *„itt tartunk, ezt kell még megcsinálni"*
4. Lokális preview-t bezárod (a port felszabaduljon)

**Soha**, semmiképp sem hagysz egy microsite-ot **félig deploy-olva**. Vagy minden lépést átfutottál (Fázis 1 → 5), vagy csak local-fázisban hagytad (Fázis 1-4). A *„félig fent van staging-en"* állapot rendben van, *de* `history.md`-be írd be hogy „staging only, production pending — kérdés Y miatt".

### Projekt-regiszter (a Microsite Factory tudjon mindenkiről)

Hozz létre egy központi regisztert:

```
00_Prompts/BDOS/capabilities/web-publishing/sites.md
```

Tartalom:

```markdown
# Microsite Factory — Site Registry

| Project | Client | Status | Domain | Last Deploy | CF Project | Path |
|---------|--------|--------|--------|-------------|------------|------|
| deakhus-microsite | Deák Húsüzlet | live | deakhusuzem.hu | 2026-05-11 b47 | deakhus-ms | 02_Areas/Deák Húsüzlet/microsite/ |
| sonrisa-llmaas | Sonrisa CPS | staging | — | 2026-05-09 b12 | sonrisa-llm | 02_Areas/Sonrisa/CPS/Marketing/llmaas-microsite/ |
| ignis-academy-2026 | Ignis Academy | dev | — | — | — | 02_Areas/Ignis Academy/Microsite-2026/ |
```

Ezt **minden deploy után** frissítsd (későbbi automatizáció: a deploy script automatikusan írja vissza). Egy pillantással látod mi hol áll.

### Token / credential disciplína

Soha:
- **Ne tedd a tokent a vault-ba** unencrypted (kivéve a teszt-időszakot, mint most — de utána `~/microsite-factory.env`-be költöztetni)
- **Ne paste-old chatbe** (sem ChatGPT-be, sem Claude-ba)
- **Ne add hozzá .env-et a git-hez** (a `.gitignore` véd, de duplán figyelj)

Egy token / capability (most: `microsite-factory-deploy`). Ha *„elveszettnek"* érzed, **revoke-old a Cloudflare dashboardon és csinálj újat**. Nincs csere, nincs „titkolózás" — csak revoke + új. A token rotációja a Microsite Factory legolcsóbb művelete.

---

## 6. Domain és staging stratégia (Cloudflare-specifikus)

### Mikor melyik domain hova mutat

Egy ügyfél microsite-jának **két publikus URL-je van**, plusz a CF default:

| URL | Típus | Mikor használd |
|-----|-------|----------------|
| `<deploy-id>.<project>.pages.dev` | immutable CF default | Ezt SOHASEM adod ki ügyfélnek — minden deploy másik ID-t kap |
| `<project>.pages.dev` | mutable CF default | Production alias, mindig az aktuális prod build |
| `<project>-staging.pages.dev` (vagy `staging.<project>.pages.dev`) | staging alias | Ügyfél-jóváhagyás előtt itt mutogatsz |
| `<custom-domain>.hu` (pl. deakhusuzem.hu) | production custom | Ide irányítod a marketinget |
| `staging.<custom-domain>.hu` | staging custom (opcionális) | Csak ha az ügyfél „brand-konzisztens" staging URL-t kér |

**Konvenció:** a `staging.` subdomaint **mindig vidd át Cloudflare-re** (proxied), és a `<project>-staging.pages.dev`-re alias-old. A `staging.example.com` szebben mutat ügyfél előtt mint a `random-id.pages.dev`.

### Domain átvitel folyamata (egyszeri, ügyfélenként)

1. **Ügyféltől megszerzed a domain regisztrátorát** és a kezelői hozzáférést (vagy ő nameserver-t cserél a te utasításodra)
2. **Cloudflare dashboardon:** Domains → Add a site → domain név → Free plan
3. **CF megad 2 nameserver-t** (pl. `aria.ns.cloudflare.com`, `kirk.ns.cloudflare.com`)
4. **A regisztrátornál** (Web4U, RNAme, Gandi, OVH, stb.) átírod a nameserver-eket
5. **DNS propagation** — 5 perctől 24 óráig (általában 30 perc Európán belül)
6. **CF megerősíti:** „Active" státusz lesz a zone mellett
7. **Pages projektbe köted:** Workers & Pages → projekt → Custom domains → Add custom domain → `example.com` és `staging.example.com`
8. **CF automatikusan ad SSL-t** (Universal SSL, Let's Encrypt vagy Google CA)

A 4. lépés `microsite-config.json`-be is rögzítendő (transparency a következő AI-nak / önmagadnak):
```json
{
  "domain_setup": {
    "registrar": "Web4U",
    "nameservers_changed_at": "2026-05-10",
    "cf_nameservers": ["aria.ns.cloudflare.com", "kirk.ns.cloudflare.com"]
  }
}
```

---

## 7. Verziózás és rollback

### Verziószámozás

`semver`-szerű: `MAJOR.MINOR.PATCH`
- **PATCH** (`0.3.1 → 0.3.2`): typo-fix, kép-csere, mikrokopirajt
- **MINOR** (`0.3.2 → 0.4.0`): új szekció, layout-változás, ajánlatváltozás
- **MAJOR** (`0.4.0 → 1.0.0`): teljes redesign, rebrand, scope-bővülés

A **`build` szám** (manifest.json) `version`-től független monoton számláló — minden deploy bumpolja.

Példa időbeli haladás:
```
build 1, version 0.1.0 — első kísérlet
build 2, version 0.1.1 — header-elrendezés-fix
build 3, version 0.1.2 — második patch
build 4, version 0.2.0 — új CTA-szekció (minor)
build 5, version 0.2.0 — same version, csak typo (patch nem indokolt, de új build)
build 47, version 0.3.1 — sok deploy közben
build 48, version 1.0.0 — első élesítés, ügyfél-jóváhagyott
```

### Rollback

A Cloudflare Pages **deployment history** mindent megőriz (immutable deploy ID-k). Rollback:

**Dashboardon (gyors):**
1. Workers & Pages → projekt → Deployments → korábbi deploy ID
2. „Rollback to this deployment" gomb

**API-ból (scriptelhető, későbbi iteráció):**
```bash
microsite-rollback <project> --to=<deployment-id>
```

A rollback `history.md`-be is bekerül egy *„Rollback to build X"* sorral.

**Soha** ne töröld a régi deploy-okat a CF-ből (free-en hónapokig őrzi). Az audit-history értékesebb mint a tárhely.

---

## 8. Hibakezelési mintázatok

### Failure type 1: pre-deploy-check fail

**Szimptóma:** `pre-deploy-check.py` exit 1, deploy nem indul.
**Akció:** olvasd a check output-ot, javítsd a HTML-t/asseteket, futtasd újra. **Ne kapcsold ki a check-et.**

### Failure type 2: CF API hiba (4xx/5xx)

**Szimptóma:** `microsite_deploy.py` exception ad — `requests.exceptions.HTTPError`.
**Lehetséges okok:**
- **401 Unauthorized:** Token rossz, lejárt, vagy nincs Pages: Edit. **Akció:** `cat .env` ellenőrzés, token regenerálás ha kell.
- **404 Not Found:** A `--project=<name>` nem létezik. **Akció:** ellenőrizd a dashboardon, vagy hozd létre.
- **413 Payload Too Large:** Egy asset > 25 MiB. **Akció:** mozgasd R2-re, töröld a `dist/`-ből.
- **429 Rate Limit:** Túl sok deploy. **Akció:** várj 1-2 percet. Ha tartós, csökkentsd a deploy-frekvenciát (általában <100/nap CF-en bőven OK).
- **5xx Server Error:** CF oldali. **Akció:** retry 30s múlva. Ha 3x egymás után, írj a CF support-nak.

### Failure type 3: Custom domain nem tölt be

**Szimptóma:** `https://example.com` 522 vagy hosszú spinner.
**Lehetséges okok:**
- DNS még nem propagált (új zóna < 24 óra) — **Akció:** várj, `dig example.com NS` ellenőrzéssel
- Pages projekthez nincs odakötve a custom domain — **Akció:** Dashboardon Workers & Pages → projekt → Custom domains → ellenőrzés
- SSL még nem aktivált (új domain első kapcsolásánál néha 15 perc) — **Akció:** várj és tölt újra incognito-ban
- Apex domain CNAME helyett A record kéne, vagy fordítva — **Akció:** CF-en a Domain → DNS-ben ellenőrizd a Pages-szel kötött records-okat

### Failure type 4: Production deploy-on regression

**Szimptóma:** production buildben valami eltört (mobile menü, form, kép). Staging-en jól ment.
**Akció:**
1. **Azonnal rollback** Cloudflare dashboardon az előző deploy ID-re. Ne próbáld kézzel javítani a fennakadt prod-on.
2. Reprodukáld lokálisan, **DEV mode-ban** (nem staging-en) — a regresszió ott is meg kell hogy jelenjen, ha igazi
3. Ha nem reprodukálható lokálisan, akkor build-step közben (a `dist/`-be másolás) ment valami félre — vizsgáld a `dist/` tartalmát
4. Fix, push staging-re, validate, csak ezután prod

---

## 9. Anti-patternek, amiket aktívan kerülj

### 1. „Csak ezt az egy fixet csinálom production-ön"

Soha. Még trivialis typo se. Minden változás staging-en megy át, mert egy gyors fix után pont olyan az „új normal" hogy a következő fix is direkt prod-ra megy, és aztán véletlenül elronthatsz valamit.

### 2. Több projektben egyszerre dolgozol egy ülésen

A kontextus-keveredés garantált. Egy session = egy microsite. Ha kettőre van időd, **két shell session, két Claude Code instance**.

### 3. „Még egy /impeccable kör"

Az 5. körön túl már nem javul. Az ügyfél véleménye fontosabb. Mutasd meg staging-en.

### 4. Tokent egy `.txt`-ben tartani a Letöltések mappában

Sajnos sokan teszik. A te `.env` rendszered a megoldás. Tartsd meg.

### 5. Csak akkor commit-olsz `history.md`-t, amikor „minden kész"

A `history.md` az AI-d (és a jövőbeli te) memóriája. **Minden** session után legalább egy sor. Még akkor is, ha „még semmi sem változott" — *„próbáltam ezt és ezt, nem ment"* érvényes bejegyzés.

### 6. „Majd kitalálom a brand-konzisztens staging-domaint később"

Ha 5 microsite-od van, és csak a 4-en van `staging.example.com`, az 5-en pedig `random-staging.pages.dev` — az ügyfél meg fogja kérdezni miért nem ugyanaz. Csináld meg azonnal, a Fázis 2 (Build) elején.

### 7. Az `archive/` mappa figyelmen kívül hagyása

Ha kézzel mozgatsz régi build-eket archive-ba, azt csináld struktúráltan: `archive/<version>-<dátum>/`. Random `index-old-2.html` nevek a projektgyökerben tilos.

---

## 10. Egy teljes példa — végigjátszás (Deák Húsüzlet, fiktív új microsite)

**Kontextus:** új lokális Deák-akció: „Húsvéti kollekció előrendelés". Microsite cél: lead-form regisztráció a kollekció megnyitásakor.

### Fázis 1 — Brief (20 perc, este)

```
$ cd "02_Areas/Deák Húsüzlet/"
$ mkdir microsite-husvet-2026 && cd $_
$ cp -r ../../../00_Prompts/BDOS/capabilities/web-publishing/templates/skeleton/* .
$ open brief.md
```

Beírod:
```markdown
# Brief — Húsvéti kollekció előrendelés microsite

**1 mondatos VP:** Hagyományos hústermékek családi húsvéti asztalra,
házhoz szállítva 50km-en belül.

**3 fő benefit:**
- Hagyomány: 30+ éves családi recept
- Frissesség: csütörtök reggeltől csak rendelésre vágunk
- Kényelem: pénteken házhoz visszük

**Persona:** 35-55 közötti, gyermekes szülő, igényes minőségre,
nincs ideje boltot bejárni.

**Konverzió:** lead-form (név, email, telefon, kollekció-csomag választás).

**Siker:** 50 lead 2 hét alatt.
```

CLAUDE.md-ben rögzíted:
- brand színe: `#8B2C1B` (Deák bordó)
- tipográfia: serif (Playfair Display heading), sans body
- tabu: „olcsó", „akció" — premium brand
- CTA szöveg: „Előrendelem"

`microsite.config.json`:
```json
{
  "project_name": "deakhus-husvet-2026",
  "cf_pages_project": "deakhus-husvet-2026",
  "production_domain": "husvet.deakhusuzem.hu",
  "staging_domain": "staging-husvet.deakhusuzem.hu",
  "version": "0.1.0",
  "client": "Deák Húsüzlet",
  "campaign": "Húsvéti előrendelés 2026"
}
```

### Fázis 2 — Build (45 perc)

Új Claude Code session, projekt mappában. Kérés:
```
Olvasd be brief.md-t és CLAUDE.md-t. Egy mondatban summázd a célt.
```

Claude válasz: *„35-55 éves szülőknek családi húsvéti hústermékek
előrendelése házhoz szállítással."*

Stimmel. Tovább:
```
Generálj egy semantic HTML5-öt src/index.html-ben. 
Szekciók: 
- Hero (cím + 1 sor + CTA)
- Mit kínálunk (3 oszlopos USP grid)  
- Csomagok (3 kollekció kártya árral)
- Hogyan rendelhetsz (3 lépéses folyamat)
- Lead form (név, email, telefon, csomag-választó dropdown)
- Footer (kontakt, social, cégadatok)
Inline styling NE legyen.
```

Claude generálja. Te megnyitod `Live Server`-rel. Megnézed: szerkezet OK,
de szöveg generic. Jegyzeted: *„Fázis 3-ban kérek konkrétabb copy-t."*

Most CSS:
```
src/styles.css-be: használj design tokeneket (--brand-primary: #8B2C1B, 
--font-heading: 'Playfair Display' stb.). 
Minimalista layout, sok whitespace. Mobile-first.
```

Claude generálja. Reload. Néz ki valahogy.

### Fázis 3 — Polish (3 iteráció, 1 óra)

**/impeccable round 1:**
```
src/index.html struktúrája [paste]. A „Csomagok" szekció 3 kártyája 
egysíkú, nincs preferred / featured highlight. Adj javaslatot.
```

Claude: *„Adj a középső kártyára `featured` class-t, 1.1× scale, brand-color
border, „Legnépszerűbb" badge a tetején."* — alkalmazod.

**/impeccable round 2:**
```
A hero CTA gombja most halvány. Adj 3 alternatívát ami feltűnőbb, 
de nem agresszív.
```

Claude: 3 javaslat. A 2.-at választod.

**/ux-copy round 3:**
```
A USP grid 3 oszlopa most: "Hagyomány", "Frissesség", "Kényelem". 
Adj olyan headline-okat amik konkrétabbak. 
Pl. "Hagyomány" → "30+ éves családi recept".
```

Claude: új headline-ok. Beapplikálod.

Lokális mobile-preview (Mód B): mindkettő OK.

### Fázis 4 — Validate (5 perc)

```bash
$ python pre-deploy-check.py
✓ index.html exists
✓ All asset references resolve
✓ Meta description: 154 chars (OK)
✓ OG image present
✓ Build sync: manifest.json b3 = index.html inline b3
✓ No localhost/file:// references
✓ No secret-like strings
✓ Favicon present

OK to deploy.
```

### Fázis 5 — Deploy (3 perc)

```bash
# Token aktívvá
$ export $(cat ../../00_Prompts/BDOS/capabilities/web-publishing/.env | xargs)

# Build (most még csak cp src/ dist/)
$ cp -r src/ dist/

# Staging
$ python ../../00_Prompts/BDOS/capabilities/web-publishing/prototype/microsite_deploy.py \
    ./dist --project=deakhus-husvet-2026 --branch=staging

→ Microsite Factory deploy: deakhus-husvet-2026 (staging)
→ Collected 8 files.
→ Hashing + encoding assets...
→ Requesting upload JWT...
→ Uploading 8 assets...
   uploaded 8/8 assets (340 KB)
→ Registering hashes...
→ Creating deployment (staging)...
   deployment_id: a1b2c3d4...
→ Polling status...
   [1] deploy: success

✓ Deployed: https://staging-husvet.deakhusuzem.hu
```

Megnyitod két böngészőben + telefonon. **Két apró fix kell** — vissza Fázis 3-ra 10 percre. Új staging deploy. OK.

Production:
```bash
$ python .../microsite_deploy.py ./dist --project=deakhus-husvet-2026

✓ Deployed: https://husvet.deakhusuzem.hu
```

Update `history.md`:
```markdown
## Build 4 (2026-05-11 21:42)
- prod: ✅ https://husvet.deakhusuzem.hu (deploy_id: e5f6g7h8...)
- staging: ✅ https://staging-husvet.deakhusuzem.hu
- changes: első élesítés
- /impeccable round: 3
- /ux-copy round: 1
- jóváhagyta: Szabolcs (Hanna-jóváhagyásra vár)
```

Commit. Session vége.

**Teljes idő: ~2.5 óra**, ebből ~30 perc volt a brief, ~45 perc az MVP build, ~60 perc a polish, ~15 perc deploy + verifikáció. A következő microsite **ennek a felében** elkészül, mert a templateket és a workflow-mintát újrahasználod.

---

## 11. Mit NEM tartalmaz a metodológia (még)

Ezek **későbbi iterációkban** jönnek:

- **Form-handler backend** (Workers + D1) — lead-form posztolva → CF Worker → DB / email
- **A/B testing** — két variáns ugyanazon URL-en, Workers split-tel
- **Image pipeline** — automatikus webp/avif/responsive set generálás CF Images-szel
- **Lighthouse CI** — Browser Run-on futtatott audit minden deploy után
- **Multi-language** (HU + EN ugyanazon microsite-on) — `/hu/`, `/en/` route-okkal
- **CMS-szerű content management** — egyelőre a Markdown-ban tartott copy → HTML build elég
- **Deploy notifications integrációja** Slack-be / Telegram-ba

Ezek **mindegyike a Microsite Factory capability-bővítéseként** lesz kezelve (új sub-skill-ek, nem új capability-k).

---

## 12. Open questions amik csak Szabolcsnak válaszolhatók

Mielőtt a metodológia v1.0-ra ér, döntsd el:

1. **Template-stratégia:** lesz egy general skeleton, vagy 3-5 témamódú template (étterem / B2B SaaS / event / pályázati landing / SaaS marketing)?
2. **Asset-pipeline:** marad a sima `cp src/ dist/`, vagy adunk hozzá build-step-et (CSS minify, image-resize)? *Javaslatom: maradjon sima, amíg fáj.*
3. **Token rotáció:** 1 év no-expire OK, vagy 90 napos rotációval szigorúbb security?
4. **`/impeccable` integráció szintje:** legyen-e custom `/microsite-polish` slash command ami a capability-konvenciókat ismeri?
5. **Site Registry (sites.md) update-elése:** kézi vagy a deploy script automatikusan írja?

Ezeket vidd be az `OPEN_QUESTIONS.md`-be a következő körhöz.

---

## 13. Hivatkozott dokumentumok

- Capability belépő: [`CLAUDE.md`](CLAUDE.md)
- Infrastruktúra (Cloudflare, dashboard, ár): [`infrastructure.md`](infrastructure.md)
- Deploy script: [`prototype/microsite_deploy.py`](prototype/microsite_deploy.py)
- Prototype README: [`prototype/README.md`](prototype/README.md)
- DH precedens (Netlify workflow): [`02_Areas/Deák Húsüzlet/CLAUDE.md`](../../../../02_Areas/Deák%20Húsüzlet/CLAUDE.md), [`design/README.md`](../../../../02_Areas/Deák%20Húsüzlet/design/README.md)
- BDOS belépő: [`../../CLAUDE.md`](../../CLAUDE.md)
- Vault konvenciók: [`../../../../CLAUDE.md`](../../../../CLAUDE.md)

---

## Záró gondolat

> A Microsite Factory **nem** technológia. A technológia (Cloudflare, Python, Claude Code) cserélhető. A **konvenció** — hogy minden microsite ugyanúgy néz ki, ugyanúgy fejlődik, ugyanúgy telepedik — az ami megsokszorozza a sebességed.
>
> Ha holnap új microsite-ot kell csinálnod, ne gondolkodj a folyamaton. Csak menj végig az 5 fázison. Ha bárhol „másképp" akarsz csinálni, kérdezd meg: *az ügyfél előnye drámaian nő tőle, vagy csak nekem szebb így?* Ha a második, ne tedd.
