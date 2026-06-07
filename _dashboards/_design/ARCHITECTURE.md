---
title: Dashboard Family — Architecture & Conventions
version: 1.0.0
date: 2026-05-25
author: Becze Szabolcs
status: active
owner: curator
description: A `_dashboards/` család normatív "alkotmánya". A DESIGN_SYSTEM.md a vizuális token-referencia; ez a fájl a WHY + HOW spec — adat-folyam, komponens-rétegek, fájl-szervezés, naming, version-bump, anti-patternek, pattern-promotion folyamat. Minden nem-triviális dashboard-változtatás előtt olvasandó.
tags: [dashboards, architecture, conventions]
id: c69180ae-30c3-4e2b-aed8-7b37ae3e1260
index_schema_version: 1
---

# Dashboard Family — Architecture & Conventions

> **Ez a normatív spec.** A [`DESIGN_SYSTEM.md`](DESIGN_SYSTEM.md) a kanonikus vizuális
> referencia (tokenek, komponens-CSS); ez a fájl a **WHY + HOW** — miért így néz ki
> az architektúra, és hogyan kell változtatni anélkül, hogy összetörne.
>
> Belépő: [`../CLAUDE.md`](../CLAUDE.md) (auto-loaded discovery layer).
> Karbantartó: **Curator agent** (`/dash-audit`, `/dash-promote`).

---

## 1. Az alap-filozófia — 5 invariáns

A dashboard család összes döntése visszavezethető 5 alapelvre. Ha új feature
ezeket sérti, a feature rossz, nem az alapelv.

### 1.1 **Markdown a single source of truth.** Dashboard a renderer
Minden adat markdown-ban (vagy SQLite-ban, ami markdown-ból regenerálódik) él.
A dashboard **soha NEM ír** vissza markdown-ba. Edit Obsidianban vagy agent-tel
történik; a dashboard csak fetch + parse + render.

**Miért:** a markdown nyitva van Obsidian, git, Sage harvest, Librarian retrieve,
ChatGPT, és bármi más AI/tool felé. Egy "dashboard-only" state írás eltörné ezt
a kompozíciót. A dashboard egy nézet, nem egy adatbázis.

### 1.2 **Zero build step.** Vanilla HTML + ESM + CSS
Nincs webpack, Vite, npm install, TypeScript compile. Egy `git pull` után minden
működik. A `dash-server.mjs` (Node stdlib only) szolgálja ki a vault gyökerét
a 4321 porton. Browser nyit `http://localhost:4321/_dashboards/<x>.html`.

**Miért:** a vault Google Drive-on szinkronizál. `node_modules/` (30K+ apró fájl)
brutálisan lassítaná. Az agentek (Curator, Librarian) is markdown-szerű fájlokat
látnak — nincs minified bundle ami megakadályozná őket az audit-ban. A "csak nyisd
meg" egyszerűség strukturális érték.

### 1.3 **Hibrid model — copy-inline most, engine extracted lazy módon**
A DS §0 szerint: a tokenek inline másolva élnek minden dashboardban, AMÍG nincs
`_design/tokens.css` engine. Amikor van engine (Sprint 2 után), új dashboard `<link>`-eli,
és minden meglevő dashboard MIGRÁL `<link>`-re ahogy egyébként is hozzá nyúlunk.

**Miért:** korai engine-extrakció (mielőtt a minta stabilizálódott) törékeny absztrakció.
A "másold inline, amíg fáj" politika lehetővé teszi a minta evolúcióját PROMOTE-ig.
A promote-tól kezdve egy a forrás — addig sok példa van, és látjuk, melyik a kanonikus.

### 1.4 **Event-driven live update, soha sűrű polling**
Az adat változását SSE (`events_server.py`, port 4322, `vault.db` mtime watchdog)
push-olja. Ha SSE nem érhető el → 8s `setInterval` auto-fallback. Ezt mindenhol
a `_design/live-updates.js` shared helper csinálja. **Per-dashboard saját polling
loop tilos.**

**Miért:** 16 dashboard × 8s polling = 2 fetch/sec a szerverre alapból. SSE-vel
gyakorlatilag 0 fetch nyugalmi állapotban, és sub-sekundum latency vault-edit
után. A pill (`.lu-pill`) megmutatja, melyik mód él.

### 1.5 **Curator a tulajdonos.** A változás audit-ozott, verziózott, promote-olt
A család tulajdonosa a Curator agent. Új minta megjelenése → promote a DS-be →
ráhúzás minden dashboardra. Audit-trail HTML kommentként a fejlécben + a DS audit
trail-ben + a `00_DASHBOARD_INDEX.md`-ben.

**Miért:** 16+ dashboard kézi szinkron-tartása lehetetlen. Curator orchestrálja
a változást, és minden lépés visszamenőleg dokumentált.

---

## 2. Adat-folyam — végponttól végpontig

```
                    Felhasználó / agent
                            ↓ (Obsidian / git / agent script)
              ┌─────────────────────────────────┐
              │  Markdown fájlok                │
              │  02_Areas/.../X.md              │
              │  00_Prompts/BDOS/...            │
              └─────────────────────────────────┘
                            ↓ (watchdog 6.x — capabilities/vault-indexing/)
              ┌─────────────────────────────────┐
              │  vault.db (SQLite + FTS5)       │
              │  capabilities/vault-indexing/   │
              │  cache/vault.db                 │
              └─────────────────────────────────┘
                            ↓ (mtime change)
              ┌─────────────────────────────────┐
              │  events_server.py (port 4322)   │
              │  SSE: { type: "vault-update" }  │
              └─────────────────────────────────┘
                            ↓ (EventSource)
              ┌─────────────────────────────────┐
              │  Browser dashboard              │
              │  LiveUpdates.subscribe(fn)      │
              │  → fn() fetch-eli a markdownt   │
              │  → parse + change-on-diff       │
              │  → re-render DOM                │
              └─────────────────────────────────┘

Párhuzamos: dash-server.mjs (port 4321) — static + own SSE fallback
            (`__events`), Drive-friendly path traversal guard
```

**Kulcs garanciák:**
- Az **adat-irány egyirányú**: markdown → DB → SSE → browser. Vissza soha.
- Az SSE az **elsődleges** mechanizmus. A polling fallback. A `.lu-pill` jelzi.
- A render **idempotens, change-on-diff**: ugyanaz a markdown ugyanazt a DOM-ot termeli.
- A `vault.db` **csak cache**; bármikor regenerálható (`build_index.py`). Soha NE
  függj olyantól, ami csak a DB-ben van és nem a markdownban.

---

## 3. Komponens-rétegek — az 5 logikai szint

```
┌──────────────────────────────────────────────────────┐
│ 5. SHELL                                             │
│    HTML váz, masthead, app container, FOUC-init      │
│    (per-dashboard, de struktúrája egyforma)          │
├──────────────────────────────────────────────────────┤
│ 4. DOMAIN                                            │
│    "Ez a dashboard mit jelent" — fetch URL,          │
│    parse-mintázat, kártya-struktúra, üzleti logika   │
│    (per-dashboard, intencionálisan különbözik)       │
├──────────────────────────────────────────────────────┤
│ 3. PATTERNS                                          │
│    Komponens-családok: card, card-copy-ref, chip,    │
│    invocation-row, sync-status, pill, version-pill   │
│    (DS §4 — minden dashboard ezeket használja)       │
├──────────────────────────────────────────────────────┤
│ 2. COMPONENTS                                        │
│    Shared JS: AdminBar, LiveUpdates, setTheme,       │
│    copyText, wireCopyRef, parseYamlFrontmatter       │
│    (_design/*.js — shared library)                   │
├──────────────────────────────────────────────────────┤
│ 1. TOKENS                                            │
│    Színek, távolságok, radius, shadow, timing        │
│    (DS §1 — _design/tokens.css Sprint 2 után)        │
└──────────────────────────────────────────────────────┘
```

**Szabály:** új kód mindig a **legalacsonyabb** rétegben éljen, ahol értelmes.
- Új szín → token (1. réteg)
- Új helper-fv → component (2. réteg)
- Új vizuális komponens → pattern (3. réteg) → promote DS §4-be
- Új adat-séma → domain (4. réteg)
- Új shell-elem → DS §4-be promote

Ha egy domain-réteg kód olyat csinál, amit egy pattern-réteg is csinálhatna → **refaktor + promote**.

---

## 4. Fájl-szervezés

```
_dashboards/
├── CLAUDE.md                  ← auto-loaded discovery (Sprint 0)
├── README.md                  ← run-instructions, dev workflow
├── 00_DASHBOARD_INDEX.md      ← live családi index (Curator-owned)
│
├── _design/                   ← SHARED LIBRARY + design system
│   ├── ARCHITECTURE.md        ← EZ A FÁJL (normatív spec)
│   ├── DESIGN_SYSTEM.md       ← vizuális referencia (Curator-owned)
│   ├── admin-bar.js           ← shared (DS §5c)
│   ├── live-updates.js        ← shared (DS §5)
│   ├── ops-header.js          ← deprecated, backward-compat
│   ├── agent_logs.json        ← sidecar (scheduler.py exports)
│   ├── lint.mjs               ← konvenció-checker (Sprint 0)
│   │
│   ├── tokens.css             ← Sprint 2 után
│   ├── components.css         ← Sprint 2 után
│   ├── theme.js               ← Sprint 1 után
│   ├── clipboard.js           ← Sprint 1 után
│   ├── markdown-parser.js     ← Sprint 3 után
│   ├── dom-utils.js           ← Sprint 5 után
│   ├── date-utils.js          ← Sprint 5 után
│   ├── agent-logs.js          ← Sprint 5 után
│   │
│   └── _template/             ← Sprint 5 után
│       ├── index.html         ← scaffold új dashboardhoz
│       ├── ONBOARDING.md      ← step-by-step build guide
│       └── checklist.md       ← pre-commit ellenőrző
│
├── _tools/                    ← server, scheduler, indexing helpers
│
├── index.html                 ← launcher (mindenki ide tér vissza)
├── agents.html, aiops.html, ... ← top-level dashboardok
│
└── <agent>/index.html         ← per-agent dashboardok (broker, curator, ...)
```

**Konvenciók:**
- Új shared kód → `_design/`. Soha NE rakd egy konkrét dashboard mappájába.
- Új dashboard → vagy top-level `<name>.html`, vagy `<name>/index.html` (per-agent / multi-fájl ha kell).
- A `_design/_template/` a "hello world" — új dashboard innen indul.

---

## 5. Naming konvenciók

### 5.1 Fájl-nevek
- HTML: `kebab-case.html` (`agents.html`, `partnerships.html`)
- Per-agent dashboard: `<agent>/index.html` (`broker/index.html`)
- JS modul: `kebab-case.js` (`live-updates.js`, `admin-bar.js`)
- CSS: `kebab-case.css` (`tokens.css`, `components.css`)

### 5.2 CSS osztály-nevek
- **BEM-szerű, de pragmatikus**: `.card`, `.card-copy-ref`, `.card-copy-ref.copied`
- **Domain-specifikus kártya**: `.vendor`, `.agent-card`, `.pillar`, `.leaf` (DS §4a megengedi)
- **Shared komponens**: `.theme-toggle`, `.home-link`, `.masthead`, `.version-pill`, `.lu-pill`, `.ab-pill` (admin-bar)
- **State**: `.copied`, `.active`, `.error`
- **Tilos**: utility class library bevezetése (Tailwind-szerű). A token-rendszer ad mindent.

### 5.3 Design token-ek
- Surface: `--bg-page`, `--bg-elev`, `--bg-sunken`, `--bg-tint`
- Ink: `--ink-1` (legsötétebb) ... `--ink-5` (legvilágosabb)
- Line: `--line`, `--line-soft`
- Accent: `--accent`, `--accent-deep`, `--accent-tint`
- Status: `--ok`, `--warn`, `--gap`, `--idle` (+ `-tint` változatok)
- Motion: `--t-fast`, `--t-med`

**Új token bevezetése:** csak Curator `/dash-promote` módban, DS §1-be írva először.
Domain-specifikus szín (pl. pipeline-stage `--hot`/`--warm`/`--cold` a `sales.html`-ben)
**pending promote** státuszban a `00_DASHBOARD_INDEX.md`-ben listázódjon.

### 5.4 JS név-konvenciók
- Függvény: `camelCase` (`parseYamlFrontmatter`, `wireCopyRef`)
- Konstans: `UPPER_SNAKE` (`DASH_STEM`, `LOGS_AGENT`)
- Modul export: ESM named exports (`export { setTheme, initTheme }`)
- Sidecar field név: **`agent_name`** soha nem `agent` (DS §7 — schema v1.2+)

### 5.5 Verzió-pill
- **Patch (`0.x.Y`)**: bugfix, audit-trail edit, doc-only change
- **Minor (`0.X.0`)**: új feature, shared lib import bevezetése, új panel
- **Major (`X.0.0`)**: breaking change (URL forrás vált, fundamental redesign)

A pill-ben látható verzió **MUST EQUAL** a HTML komment audit-trail utolsó sora.
A `lint.mjs` ezt checkolja.

---

## 6. Anti-patternek — soha NE csináld

| Anti-pattern | Miért tilos | Mit csinálj helyette |
|---|---|---|
| Custom hex `#abc123` `var(--token)` helyett | Drift — minden dashboardon más árnyalat | Promote tokenre DS §1-ben |
| Saját `setTheme()` újra-implementáció | Cross-tab sync el fog romlani | Sprint 1 után: `import` `_design/theme.js`-ből |
| Saját `parseYamlFrontmatter()` | 9 különböző parser-implementáció már létezik — drift biztos | Sprint 3 után: `import` `_design/markdown-parser.js`-ből |
| `fetch` + `.then(...write back...)` markdown-ba | Megsérti az 1.1 invariánst (markdown source of truth) | Edit Obsidianban vagy agent-tel |
| Sűrű `setInterval` poll loop | Megsérti az 1.4 invariánst (event-driven) | `LiveUpdates.subscribe(fn)` |
| Új `<script src="cdn.../some-lib.min.js">` | Build-step felé csúszás, hálózati függés | Vanilla vagy shared `_design/` modul |
| `node_modules/` introduce | Drive-szinkron katasztrófa | Zero build elv |
| Új dashboard `sales.html`-ből copy-paste | 4775 sor, domain-specifikus, drift-bringer | `_design/_template/`-ből (vagy `team.html`) |
| FOUC-init kihagyása `<head>`-ből | Theme villog első paint-nél | DS §1b verbatim copy |
| Új dashboard launcher-regisztráció nélkül | Felhasználó nem találja meg | Bemásolni `index.html` launcher tree-be + `00_DASHBOARD_INDEX.md` |
| Hiányzó verzió-bump HTML-edit után | DS §6 §2 megsértés | Mindig bump + audit-trail sor |
| `data-card-id` nélkül kártya | Felhasználó nem tudja referálni | Mindig `data-card-id` + `.card-copy-ref` button (DS §4a) |

---

## 7. Pattern-promotion folyamat

Amikor egy dashboardon új vizuális/JS minta születik, ami máshol is hasznos:

1. **Kísérletezz** a dashboardodban (1 dashboard, 1 minta)
2. **Stabilizáld** — minimum 2 héten át használd
3. **Jelezd Curator-nak**: `/dash-promote <pattern-name>`
4. Curator:
   - Megméri a többi dashboardon, hol illeszkedne
   - DS-be írja (új szekció vagy meglevő bővítés) — verzió-bump (DS minor)
   - **Dry-run rollout** terv (mely fájlok érintettek, milyen edit)
   - **Confirmation kötelező** (te jóváhagyod)
   - Rollout → minden érintett dashboard bump (audit-trail)
   - `00_DASHBOARD_INDEX.md` audit-trail entry

**A pending promote** lista a `00_DASHBOARD_INDEX.md`-ben él — ott látod, melyik
minta vár promote döntésre.

---

## 8. Konkrét workflow-k

### 8.1 "Új panelt akarok hozzáadni egy meglevő dashboardhoz"

1. Olvasd el ezt a fájlt + a dashboardnak a fejléc-kommentjét
2. Ellenőrizd: hova illeszkedik (új card a card-grid-ben? új szekció?)
3. Adatforrás: melyik markdown-fájlt fetch-eled? Létezik már a parser?
4. Render: használj **meglevő pattern**-t (`.card` + `.card-copy-ref`)
5. **Verzió-bump** + audit-trail sor (`0.x.Y` patch ha kis fix, `0.X.0` minor ha új panel)
6. Futtasd: `node _dashboards/_design/lint.mjs <fájl>`
7. Curator audit: `/dash-audit <fájl>` (opcionális, ajánlott)

### 8.2 "Új dashboardot építek"

1. Indulj a `_design/_template/index.html`-ből (Sprint 5 után). Addig: `team.html` a legjobb minta.
2. Másold át, cseréld a `DASH_STEM` const-ot, a fetch URL-t, a title-t.
3. Tartsd meg: FOUC-init, masthead struct, admin-bar mount, live-updates subscribe, theme-toggle, version-pill, home-link.
4. Tölts fel saját domain-logikával (4. réteg).
5. Regisztráld: `index.html` launcher tree + `00_DASHBOARD_INDEX.md`.
6. Lint zöld: `node _dashboards/_design/lint.mjs <új-fájl>`.
7. Curator: `/dash-survey` (újra-felméri a családot).

### 8.3 "Új design pattern-t találtam — promote-olni szeretném"

1. Stabilizáld a dashboardodban (~2 hét).
2. `/dash-promote <pattern>` — Curator átveszi.
3. Te jóváhagyod a rollout-tervet.
4. Curator rollout + audit-trail.

### 8.4 "Új shared utility-t építek (`_design/x.js`)"

1. Ellenőrizd: tényleg 2+ dashboard használná?
2. ESM modul, named exports, JSDoc minimum.
3. Add hozzá a CLAUDE.md "Shared library" táblázatához.
4. Add hozzá a `lint.mjs` legacy-detector listájához (hogy a régi inline implementációkat észrevegye).
5. DS-bump (új minor, audit-trail sor).

---

## 9. Konvenció-checkolás: `lint.mjs`

A `_design/lint.mjs` Node script (0 dep) ellenőrzi:

- ✅ FOUC-init `<script>` jelen van a `<head>`-ben
- ✅ Home-link href = `/_dashboards/index.html`
- ✅ Verzió-pill jelen + matchel az audit-trail utolsó sorával
- ✅ Admin-bar mount-point (`#bdos-admin-bar` vagy legacy `#bdos-ops-header`) jelen
- ✅ `<script src="/_dashboards/_design/admin-bar.js">` jelen
- ✅ Live-updates script jelen, ha SSE-t használ
- ✅ `data-card-id` minden kártya-szelektoron (ha van card-copy-ref)
- ✅ Custom hex colors `:root`-on kívül = warning
- ✅ Sprint 1+ után: saját `setTheme()` definíció = warning (használd a shared-et)
- ✅ Sprint 3+ után: saját `parseYamlFrontmatter()` definíció = warning
- ✅ `agent_name` field használt `agent` helyett (DS §7)
- ✅ Sidecar JSON v2 schema check (`scheduled_jobs` array)

Futtatás:
```bash
node _dashboards/_design/lint.mjs                     # minden dashboard
node _dashboards/_design/lint.mjs team.html            # konkrét fájl
node _dashboards/_design/lint.mjs --strict             # warning-ok is error-ek
node _dashboards/_design/lint.mjs --json               # JSON output (CI / agent)
```

---

## 10. Külső érintkezések

- **Curator agent** (`00_Prompts/BDOS/agents/curator/`) — owner. `/dash-*` slash commands.
- **Librarian agent** — a `00_DASHBOARD_INDEX.md`-t Curator karbantartja, de a globális
  vault-index a Librarian-é. Egymástól függetlenül futnak.
- **vault-indexing capability** (`00_Prompts/BDOS/capabilities/vault-indexing/`) — a
  `vault.db` és a watchdog. Dashboard FRONTEND egyelőre **nem** queryzi közvetlenül —
  csak fetch-eli a markdown fájlokat. (Jövőbeli optimalizáció: Astro endpoint vagy
  shared SQL.js mód.)
- **scheduler.py** — a sidecar `agent_logs.json`-t exportálja. A 6 per-agent dashboard
  ebből olvas. Schema v2 (DS §7).
- **dash-server.mjs** — static + own SSE fallback (port 4321).
- **events_server.py** — primary SSE (port 4322).

---

## 11. Verziózás (ennek a fájlnak)

- **1.0.0** (2026-05-25) — initial. Sprint 0 keretében. A 11 szekció a refactor-terv
  alapján született. Karbantartó: Curator. Frissítés akkor, ha az architektúra-elv
  változik (új réteg, új invariáns, új top-level fájl-szervezés).

Audit-trail bővítés szabálya: minden architektúra-érintő DS-promote után írj sort.

---

**Hivatkozott:**
[`DESIGN_SYSTEM.md`](DESIGN_SYSTEM.md) ·
[`../CLAUDE.md`](../CLAUDE.md) ·
[`_template/checklist.md`](_template/checklist.md) ·
[`lint.mjs`](lint.mjs) ·
[`../00_DASHBOARD_INDEX.md`](../00_DASHBOARD_INDEX.md) ·
[`../../00_Prompts/BDOS/agents/curator/`](../../00_Prompts/BDOS/agents/curator/)
