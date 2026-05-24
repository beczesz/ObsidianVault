<!--
  =============================================================================
  Vault Dashboards — Design System.   Version: 0.5.0
  =============================================================================
  Canonical source of truth for the visual language shared by every dashboard
  in _dashboards/. The Curator agent OWNS this file: it audits dashboards
  against it, updates it when a new rule is learned (promote mode), and applies
  it across the family.

  Hybrid model (decided 2026-05-22): this markdown is the human-readable source
  of truth NOW. Dashboards still copy tokens inline. Engine extraction
  (_dashboards/_engine/tokens.css + shared JS) is deferred and done lazily —
  when a dashboard is next touched, migrate it to import rather than copy.

  Audit trail:
    0.1.0 (2026-05-22) initial extraction from partnerships.html :root + the
          seven laws + DASHBOARD_CONTRACT shared conventions.
    0.2.0 (2026-05-22) added .card-copy-ref + data-card-id convention +
          copyable component family (promoted from agents.html chip-copyable /
          invocation-row patterns + new per-card hover copy button).
    0.3.0 (2026-05-22) added canonical dark theme tokens + .theme-toggle +
          shared dash-theme persistence + system-aware default. Dark palette
          harmonized from navigator.html reference implementation. All
          dashboards now use shared localStorage key "dash-theme".
    0.4.0 (2026-05-24) PROMOTE: event-driven live update pattern (SSE via
          events_server.py / port 4322, vault.db mtime watcher). Shared helper
          _design/live-updates.js created. Status indicator pill (.lu-pill)
          canonicalized. Old 8s setInterval polling deprecated — preserved as
          automatic fallback only. Family-wide rollout: all 7 targeted dashboards
          bumped (index.html 0.7.4→0.7.5, others 0.2.0→0.3.0). Law 4 updated.
    0.5.0 (2026-05-24) PROMOTE: ops-header strip component (.bdos-ops-header /
          .ops-pill) + BDOS Job Scheduler (scheduler.py attached to
          events_server.py). Shared helper _design/ops-header.js created.
          System status drawer housed in _dashboards/scheduler/index.html.
          Family-wide rollout: all 15 dashboards bumped. New §6 added below.
  =============================================================================
-->
---
title: Vault Dashboards Design System
version: 0.5.0
date: 2026-05-24
author: Becze Szabolcs
status: active
owner: curator
description: A _dashboards/ család közös vizuális nyelve — design token-ek, tipográfia, komponens-konvenciók, a hét törvény. A Curator agent kanonikus forrása; ő auditál ellene, frissíti (promote mód), és ráhúzza minden dashboardra.
---

# Vault Dashboards — Design System

> **A Curator kanonikus design-forrása.** Minden dashboard ugyanazt a vizuális nyelvet beszéli. Ez a fájl az igazság forrása; ha egy szabály itt változik, a Curator `promote` módban ráhúzza az egész családra. Új palette/font per-dashboard = szabálysértés.

## 0. Hibrid modell (2026-05-22)

Ez a markdown a **source of truth most**. A dashboardok egyelőre **inline másolják** a token-blokkot (a capability doc "copy from reference" elve szerint). Az **engine-extrakció** (`_dashboards/_engine/tokens.css` + shared JS modulok, amit a dashboardok `<link>`/import-tal hivatkoznak) **lustán** történik: amikor egy dashboardhoz úgyis hozzányúlunk (`tend`/`promote`), átállítjuk import-ra. Amíg nincs engine, a `promote` mód a token-blokkot **fájlonként szerkeszti** (N edit), de mindig EBBŐL a fájlból mint forrásból.

## 1. Design tokens (`:root`)

A kanonikus token-blokk. Másold verbatim minden dashboard `:root`-jába (vagy importáld az engine-ből, ha már létezik).

```css
:root {
  /* Surfaces — cream paper */
  --bg-page:   #faf9f5;
  --bg-elev:   #ffffff;
  --bg-sunken: #f3f1ea;
  --bg-tint:   #f5f4ef;

  /* Ink scale (1 darkest → 5 lightest) */
  --ink-1: #141413;
  --ink-2: #3a3a37;
  --ink-3: #6d6d6a;
  --ink-4: #9c9c98;
  --ink-5: #c8c8c2;

  /* Lines */
  --line:      #e5e4df;
  --line-soft: #efede7;

  /* Accent — terracotta */
  --accent:      #D97757;
  --accent-deep: #b35a3f;
  --accent-tint: #fbeee6;

  /* Status */
  --ok:        #1f7a4d;  --ok-tint:   #e6f3ec;
  --warn:      #b07a18;  --warn-tint: #fbf2dc;
  --gap:       #c0392b;  --gap-tint:  #fbeae6;
  --idle:      #7a7a76;  --idle-tint: #efeeeb;

  /* Elevation */
  --shadow-1: 0 1px 2px rgba(20,20,19,.04), 0 1px 1px rgba(20,20,19,.02);
  --shadow-2: 0 4px 14px rgba(20,20,19,.07), 0 2px 4px rgba(20,20,19,.04);

  /* Radius */
  --radius-s: 4px;  --radius-m: 6px;  --radius-l: 10px;  --radius-xl: 14px;

  /* Motion */
  --t-fast: 120ms cubic-bezier(.2,.7,.3,1);
  --t-med:  220ms cubic-bezier(.2,.7,.3,1);
}
```

**Tilos:** per-dashboard palette vagy hex-érték a token-eken kívül. Új szín csak úgy léphet be, ha token-né válik EBBEN a fájlban (`promote` mód).

## 1a. Dark theme token override (`:root[data-theme="dark"]`)

Canonical dark-mode override block. Copy verbatim into every dashboard's `<style>` block, immediately after the `:root` block. Harmonized from navigator.html reference palette (2026-05-22).

WCAG AA guidance: `--ink-1` on `--bg-page` passes AA at all sizes; `--accent` on `--bg-page` passes AA for large text. Status colors (`--ok`, `--warn`, `--gap`) are lightened to ~60% luminance for dark-bg legibility.

```css
/* ===== Dark theme override (DS 0.3.0) ===== */
:root[data-theme="dark"] {
  /* Surfaces — warm dark paper */
  --bg-page:   #1a1916;
  --bg-elev:   #232220;
  --bg-sunken: #2c2a26;
  --bg-tint:   #262420;

  /* Ink scale (inverted ramp — 1 lightest on dark) */
  --ink-1: #f5f4ef;
  --ink-2: #d6d4ce;
  --ink-3: #a8a6a0;
  --ink-4: #7c7a74;
  --ink-5: #54524d;

  /* Lines */
  --line:      #36342f;
  --line-soft: #2c2a26;

  /* Accent — warmer/lighter terracotta for dark bg (WCAG AA large text) */
  --accent:      #e08a6a;
  --accent-deep: #f0a085;
  --accent-tint: #3a2a22;

  /* Status — lightened for dark-bg legibility */
  --ok:        #5cc08a;  --ok-tint:   #1e3329;
  --warn:      #d6a94a;  --warn-tint: #352c18;
  --gap:       #e57c6e;  --gap-tint:  #3a221e;
  --idle:      #9a9892;  --idle-tint: #2a2925;

  /* Elevation — deeper shadows on dark */
  --shadow-1: 0 1px 2px rgba(0,0,0,.30), 0 1px 1px rgba(0,0,0,.20);
  --shadow-2: 0 4px 14px rgba(0,0,0,.40), 0 2px 4px rgba(0,0,0,.25);
}

/* System-aware fallback: when no explicit choice is stored, honor OS preference */
@media (prefers-color-scheme: dark) {
  :root:not([data-theme="light"]) {
    --bg-page:   #1a1916;
    --bg-elev:   #232220;
    --bg-sunken: #2c2a26;
    --bg-tint:   #262420;
    --ink-1: #f5f4ef;
    --ink-2: #d6d4ce;
    --ink-3: #a8a6a0;
    --ink-4: #7c7a74;
    --ink-5: #54524d;
    --line:      #36342f;
    --line-soft: #2c2a26;
    --accent:      #e08a6a;
    --accent-deep: #f0a085;
    --accent-tint: #3a2a22;
    --ok:        #5cc08a;  --ok-tint:   #1e3329;
    --warn:      #d6a94a;  --warn-tint: #352c18;
    --gap:       #e57c6e;  --gap-tint:  #3a221e;
    --idle:      #9a9892;  --idle-tint: #2a2925;
    --shadow-1: 0 1px 2px rgba(0,0,0,.30), 0 1px 1px rgba(0,0,0,.20);
    --shadow-2: 0 4px 14px rgba(0,0,0,.40), 0 2px 4px rgba(0,0,0,.25);
  }
}
```

## 1b. FOUC-preventing theme-init snippet

Place this **inline `<script>` in `<head>` before any stylesheet** to read `localStorage` and set `data-theme` before paint, preventing a flash of wrong theme.

```html
<!-- Theme init — must run before paint (DS 0.3.0) -->
<script>
(function(){
  var t;
  try { t = localStorage.getItem('dash-theme'); } catch(e) {}
  if (!t) {
    t = (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) ? 'dark' : 'light';
  }
  document.documentElement.dataset.theme = t;
})();
</script>
```

## 1c. Shared `dash-theme` persistence contract

- **Key:** `localStorage` key `dash-theme` (shared across ALL dashboards — switch in one tab, updates all).
- **Values:** `"light"` | `"dark"` | *(absent = follow system via `prefers-color-scheme`)*.
- **Canonical `setTheme(t)` function** (one copy per file):

```js
/* ===== Theme toggle (DS 0.3.0) ===== */
function setTheme(t) {
  document.documentElement.dataset.theme = t;
  try { localStorage.setItem('dash-theme', t); } catch(e) {}
  const btn = document.getElementById('themeToggle');
  if (btn) {
    btn.querySelector('.theme-icon').textContent = t === 'dark' ? '☀' : '☾';
    btn.querySelector('.theme-label').textContent = t === 'dark' ? 'Light' : 'Dark';
    btn.setAttribute('aria-label', t === 'dark' ? 'Switch to light theme' : 'Switch to dark theme');
  }
}

document.getElementById('themeToggle').addEventListener('click', function() {
  setTheme(document.documentElement.dataset.theme === 'dark' ? 'light' : 'dark');
});

// Cross-dashboard live sync: when another tab/dashboard changes the theme
window.addEventListener('storage', function(e) {
  if (e.key === 'dash-theme' && e.newValue) setTheme(e.newValue);
});

// Boot: apply persisted or system theme
(function initTheme() {
  var t;
  try { t = localStorage.getItem('dash-theme'); } catch(e) {}
  if (!t) {
    t = (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) ? 'dark' : 'light';
  }
  setTheme(t);
})();
```

**Note:** `setTheme` must be defined before the boot IIFE. The FOUC-init in `<head>` handles the pre-paint case; this JS block handles the post-paint state (label/icon sync).

## 1d. `.theme-toggle` component

Canonical masthead button. Always placed in the masthead `toprow` (or equivalent flex row), consistent across all dashboards.

### CSS

```css
/* ===== Theme toggle button (DS 0.3.0) ===== */
.theme-toggle {
  display: inline-flex; align-items: center; gap: 6px;
  font-size: 12px; font-weight: 500; color: var(--ink-3);
  padding: 5px 11px; border: 1px solid var(--line);
  border-radius: 999px; background: var(--bg-elev);
  transition: color var(--t-fast), border-color var(--t-fast), background var(--t-fast);
  cursor: pointer; user-select: none;
}
.theme-toggle:hover { color: var(--accent-deep); border-color: var(--accent); }
.theme-toggle:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; border-radius: 999px; }
```

### HTML

```html
<!-- Place in masthead toprow, next to .home-link -->
<button class="theme-toggle" id="themeToggle"
        aria-label="Switch to dark theme"
        title="Toggle day / night theme">
  <span class="theme-icon">&#9790;</span>
  <span class="theme-label">Dark</span>
</button>
```

### Masthead `toprow` pattern

For dashboards that lack a `.toprow` wrapper, add one to hold `.home-link` + `.theme-toggle`:

```css
.masthead-toprow {
  display: flex; align-items: center; justify-content: space-between;
  gap: 12px; margin-bottom: 14px;
}
```

```html
<header class="masthead">
  <div class="masthead-toprow">
    <a class="home-link" href="/_dashboards/index.html" ...>Ideas Vault</a>
    <button class="theme-toggle" id="themeToggle" ...>...</button>
  </div>
  <!-- eyebrow, h1, submeta as before -->
</header>
```

**Tilos:** per-dashboard palette vagy hex-érték a token-eken kívül. Új szín csak úgy léphet be, ha token-né válik EBBEN a fájlban (`promote` mód).

## 2. Tipográfia

- **UI font:** `Inter` (400/500/600/700) — `font-feature-settings: 'ss01','cv11','tnum' 0`
- **Mono font:** `JetBrains Mono` (400/500) — kód, metrika, dátum, verzió-pill. Class: `.mono`
- **Tabular nums:** `.tabular` (`font-variant-numeric: tabular-nums`) számoszlopokhoz
- **Base:** `html { font-size: 15px }`, `body { line-height: 1.45 }`
- **H1 (masthead):** `clamp(28px, 3.2vw, 40px)`, weight 700, `letter-spacing: -0.02em`
- **Eyebrow:** 11px, uppercase, `letter-spacing: .12em`, `--ink-4`
- Google Fonts link: `Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500`

## 3. Layout

- App container: `max-width: 1200px; margin: 0 auto; padding: 28px 36px 96px`
- Widgets row: `grid-template-columns: repeat(4, 1fr); gap: 16px`
- Kártya/widget: `--bg-elev` + `1px solid --line` + `--radius-l`, padding `18px 20px 16px`
- Box-sizing: `border-box` mindenre, `margin/padding: 0` reset

## 4. Kötelező komponensek (másold reference-ből, ne találd ki)

| Komponens | CSS hook | Forrás |
|---|---|---|
| **Home button** | `.home-link` — pill, `href="/_dashboards/index.html"` (absolute) | partnerships.html |
| **Eyebrow + version pill** | `.eyebrow`, `.version-pill` (mono, 10px) | partnerships.html |
| **Masthead** | `.masthead h1 .accent`, `.submeta`, `.dot` | partnerships.html |
| **Sync indicator** | `.sync-status` (dot + `.sync-bar` + countdown/shuttle keyframe) | partnerships.html / sales.html |
| **Favicon** | inline SVG, cream rounded rect + terracotta motif | bármelyik reference |
| **Card copy-ref button** | `.card-copy-ref` (lásd §4a) | agents.html → DS 0.2.0 |
| **Copyable chips** | `.chip-copyable` (lásd §4b) | agents.html |
| **Copyable invocation rows** | `.invocation-row` (lásd §4b) | agents.html |

## 4a. Card copy-ref — hover "copy reference" button

Every bounded card-like element the user might point at carries a **stable, human-readable reference** so they can paste it back to a developer to locate that exact card.

### Convention: `data-card-id` + `stem:card-id`

- Every card element carries `data-card-id="<card-id>"` — a stable slug (may use `/` for nesting, e.g. `cps/partnerships`).
- The **reference** = `<dashboard-stem>:<card-id>` where `dashboard-stem` = HTML filename without extension (e.g. `partnerships`, `sales`, `index`).
- Each file defines `const DASH_STEM = "<stem>"` (or derives it from `location.pathname`).
- Clicking the copy button copies `stem:cardId` to clipboard.

**slug rules:** lowercase, words joined by `-`, nesting with `/`. Examples:
- launcher leaves: `cps/partnerships`, `cps/sales`, `cps/aiops`, `cps/team`, `cps/marketing`
- launcher branch headers: `cps`, `sonrisa`, `exar`, `navigator-podcast`
- launcher standalones: `standalone/media-muhely`, `standalone/plugins`, `standalone/agents`
- partnerships vendors: `aws`, `oracle`, `azure`
- aiops pillars: slugified pillar name from data (`inference-substrate`, etc.)
- agents: slugified agent name from data (`librarian`, `maestro`, `curator`)
- sales leads: derived from lead slug/name in data
- team units: unit name slug; team members: member name slug
- navigator episodes: episode number slug (`ep01`, `ep42`, etc.)
- plugins cards: plugin name slug

### CSS: `.card-copy-ref`

```css
/* ===== Card copy-ref button (DS 0.2.0) ===== */
/* Card container MUST have position: relative */
.card-copy-ref {
  position: absolute;
  top: 10px;
  right: 10px;
  opacity: 0;
  display: inline-flex;
  align-items: center;
  gap: 4px;
  padding: 3px 7px;
  background: var(--bg-elev);
  border: 1px solid var(--line);
  border-radius: var(--radius-m);
  font-size: 10px;
  font-family: 'JetBrains Mono', monospace;
  font-weight: 500;
  color: var(--ink-3);
  cursor: pointer;
  transition: opacity var(--t-fast), background var(--t-fast), border-color var(--t-fast), color var(--t-fast);
  white-space: nowrap;
  z-index: 2;
  line-height: 1;
}
/* Show on card hover or keyboard focus-within */
.card-container:hover .card-copy-ref,
.card-container:focus-within .card-copy-ref {
  opacity: 1;
}
/* Hover state */
.card-copy-ref:hover {
  background: var(--bg-sunken);
  border-color: var(--accent);
  color: var(--accent-deep);
}
/* Copied confirmation */
.card-copy-ref.copied {
  background: var(--ok-tint);
  border-color: rgba(31,122,77,.3);
  color: var(--ok);
  opacity: 1;
}
```

**Note:** replace `.card-container` with the actual card selector per dashboard (`.agent-card`, `.vendor`, `.pillar`, `.leaf`, etc.).

### Accessibility

- Must be a real `<button>` element (not a `<div>`).
- `aria-label="Kártya-azonosító másolása"` on the button.
- Keyboard-activatable (inherits from `<button>`).
- `e.stopPropagation()` in the click handler — **critical**: prevents triggering the card's own click/navigation (e.g. "Open →" links, drawer openers, table row clicks).

### HTML template (static cards)

```html
<button class="card-copy-ref" aria-label="Kártya-azonosító másolása" data-for-card>
  <svg width="9" height="9" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><rect x="9" y="9" width="13" height="13" rx="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></svg>
  copy ref
</button>
```

### JS: canonical `copyCardRef` helper

```js
/* ===== Canonical clipboard helper (DS 0.2.0) ===== */
const DASH_STEM = '<stem>'; // one per file, e.g. 'partnerships'

function copyText(text, el) {
  navigator.clipboard.writeText(text).then(() => {
    el.classList.add('copied');
    setTimeout(() => el.classList.remove('copied'), 1600);
  }).catch(() => {
    const ta = document.createElement('textarea');
    ta.value = text; ta.style.position = 'fixed'; ta.style.opacity = '0';
    document.body.appendChild(ta); ta.select();
    try { document.execCommand('copy'); } catch(e) {}
    document.body.removeChild(ta);
    el.classList.add('copied');
    setTimeout(() => el.classList.remove('copied'), 1600);
  });
}

function wireCopyRef(containerEl) {
  containerEl.querySelectorAll('.card-copy-ref').forEach(btn => {
    btn.onclick = (e) => {
      e.stopPropagation(); // never trigger card navigation
      const card = btn.closest('[data-card-id]');
      if (!card) return;
      copyText(DASH_STEM + ':' + card.dataset.cardId, btn);
    };
  });
}
```

For **dynamic cards** (JS-rendered), inject `.card-copy-ref` inside the render template string and call `wireCopyRef(grid)` after `innerHTML` assignment. The `data-card-id` value is derived deterministically from a stable data field (slugified agent name, lead slug, partner name, pillar key, member name, episode number).

**Slug helper:**
```js
function toSlug(s) {
  return String(s).toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '');
}
```

## 4b. Copyable component family (DS 0.2.0)

The following "copy to clipboard" patterns are codified as the canonical copyable family. All share the `copyText(text, el)` helper above (a single function per file, not duplicated).

### `.chip-copyable` — copyable monospace chip

Used for slash commands and short codes. On click: copies `data-copy` value, adds `.copied` class for 1.6s.

```css
.chip-copyable {
  font-family: 'JetBrains Mono', monospace; font-size: 11px; font-weight: 500;
  color: var(--accent-deep); background: var(--accent-tint); border: 1px solid rgba(217,119,87,.25);
  border-radius: var(--radius-s); padding: 2px 8px; white-space: nowrap;
  cursor: pointer; display: inline-flex; align-items: center; gap: 5px;
  transition: background var(--t-fast), border-color var(--t-fast);
  user-select: none;
}
.chip-copyable:hover { background: #f4d5c6; border-color: var(--accent); }
.chip-copyable .copy-icon { opacity: 0.5; flex-shrink: 0; }
.chip-copyable.copied { color: var(--ok); background: var(--ok-tint); border-color: rgba(31,122,77,.3); }
.chip-copyable.copied .copy-icon { opacity: 0.7; }
```

### `.invocation-row` — copyable code+description row

Used for multi-field copyable items (code + description). On click: copies `data-copy` value, adds `.copied` class.

```css
.invocation-row {
  display: flex; align-items: flex-start; gap: 10px;
  padding: 7px 10px; margin-bottom: 4px;
  background: var(--bg-sunken); border-radius: var(--radius-m);
  cursor: pointer; transition: background var(--t-fast);
  border: 1px solid transparent;
}
.invocation-row:hover { background: var(--bg-tint); border-color: var(--line); }
.invocation-row.copied { background: var(--ok-tint); border-color: rgba(31,122,77,.2); }
```

**Wire-up:** `el.onclick = () => copyText(el.dataset.copy, el);`

## 5. Live Update Pattern v0.2 — Event-driven (DS 0.4.0)

**Canonical pattern from 2026-05-24.** Every dashboard uses the shared helper
`/_dashboards/_design/live-updates.js`. Import it before your `<script>` block
and call `LiveUpdates.subscribe(refetchAndRender)`.

### Architecture

- **Primary:** SSE `EventSource('http://localhost:4322/events')` → `events_server.py` watches `vault.db` mtime. When the vault-indexing watcher (watchdog 6.x, PID in `cache/watch.pid`) applies changes to `vault.db`, the events server broadcasts `data: {"type":"vault-update","ts":<unix>}`.
- **Fallback:** If SSE fails to connect within 3 seconds (events server not running, or `file://` context), `live-updates.js` automatically activates `setInterval(8000)` polling. Status indicator shows "polling (fallback)".
- **Heartbeat:** events_server.py sends `: heartbeat\n\n` every 15s to keep connection alive.

### Integration (per-dashboard)

```html
<!-- Before closing </body> or in <head> after fonts -->
<script src="/_dashboards/_design/live-updates.js"></script>
```

```js
// In each dashboard's boot section — replaces connectEventStream() + startPolling()
LiveUpdates.subscribe(refetchAndRender);   // your existing data-load function

// Mount status indicator into masthead toprow (right side, next to theme-toggle)
LiveUpdates.mountStatusIndicator(document.querySelector('.masthead-toprow'));
```

### Status indicator — `.lu-pill` component

Small pill in dashboard header, top-right, next to the theme-toggle button.
Rendered by `live-updates.js` — **do not recreate per-dashboard**.

| State | Color | Meaning |
|---|---|---|
| `active` | Green (`--ok` / `--ok-tint`) | SSE stream connected, receiving events |
| `polling` | Amber (`--warn` / `--warn-tint`) | 8s poll fallback (events_server.py not running) |
| `connecting` | Grey, blinking dot | Waiting for SSE to open |
| `error` | Red (`--gap` / `--gap-tint`) | SSE error, transitioning to fallback |

Hover shows tooltip: engine, last update timestamp, connection state.
Click opens an explanatory modal (what watchdog is, how to start it).

### Deprecated: 8s setInterval polling (DS <0.4.0)

The old `setInterval(8000)` as the primary refresh mechanism is **deprecated**.
It is preserved as the automatic fallback inside `live-updates.js` — dashboards
must NOT implement their own primary polling loop. The only valid polling in the
family is the fallback path in `live-updates.js`.

### Sync invariants (unchanged)

- Change-on-diff rebuild + idempotent render (pure function of parsed data)
- **Read-only**: never write back to markdown
- `file://` fallback: polling activates automatically (no SSE in file:// context)

## 5b. Ops Header Strip (DS 0.5.0)

The canonical system-status strip rendered **above every dashboard masthead**.
Implemented as a shared helper `_design/ops-header.js` (auto-mounts on load).

### Usage (two lines per dashboard)

```html
<!-- In <body>, first element: -->
<div id="bdos-ops-header"></div>

<!-- Before </body>, after live-updates.js: -->
<!-- ops-header.js (DS 0.5.0) -->
<script src="/_dashboards/_design/ops-header.js"></script>
```

`ops-header.js` auto-mounts into `#bdos-ops-header` on `DOMContentLoaded`.
If the element is absent it prepends itself as `document.body.firstChild`.

### Component classes

```css
/* Strip container — sticky, above masthead */
.bdos-ops-header { ... }   /* see ops-header.js §CSS */

/* Individual status pill */
.ops-pill          { ... }  /* base pill */
.ops-pill.ok       { ... }  /* green */
.ops-pill.warn     { ... }  /* amber */
.ops-pill.gap      { ... }  /* red */
.ops-pill.idle     { ... }  /* grey */
.ops-pill .ops-dot { ... }  /* 6px circle */
```

### Five pills (checked every 30 s)

| Pill | Check |
|---|---|
| **Watchdog** | `events_server.py` `/health` (port 4322) |
| **Server** | `dash-server.mjs` HEAD / (port 4321) |
| **DB** | sidecar `agent_logs.json` freshness + row count |
| **Scheduler** | last `agent_logs` row with `tags includes 'scheduler'` within 5 min |
| **Index** | sidecar `generated_at` within 24 h |

### System drawer

The "System" button opens `/_dashboards/scheduler/index.html` as an iframe overlay.
Three tabs: **Health** (pill detail cards) · **Jobs** (scheduled_jobs state) · **Logcat** (filterable event stream, 5 s live refresh).

### Public API

```js
OpsHeader.mount()        // auto-called on DOMContentLoaded
OpsHeader.refresh()      // force immediate re-check of all pills
OpsHeader.openDrawer()   // open system status drawer
OpsHeader.closeDrawer()  // close drawer (also: Escape key, backdrop click)
```

---

## 6. A hét törvény (a Curator audit-ja ezeket méri)

1. **Home button** `/_dashboards/index.html`-re (absolute), minden masthead-ben.
2. **Versioning** `0.1.0`-tól (`0.0.x`/`0.x.0`/`x.0.0`), dated audit trail a comment headerben; látható pill == comment-verzió.
3. **Shared design token-ek** (ez a fájl), sosem per-dashboard palette.
4. **Live read-only sync** — event-driven SSE primary (`live-updates.js` + `events_server.py`), 8s poll auto-fallback, soha write-back. Status indicator pill kötelező minden masthead-ben (DS 0.4.0).
5. **Edit markdown, not HTML** — a HTML renderer; HTML-érintéskor verzió-bump.
6. **Register in the launcher**, amikor élesedik.
7. **Kód `_dashboards/`-ban, tartalom Areas-ban** — soha co-locate.

## 7. Ismert kivétel

*(Korábban: `plugins.html` dark-theme outlier — 2026-05-22 promote 0.3.0 keretében a kanonikus tokenekre migrálva, kivétel-státusz megszűnt.)*

---

**Hivatkozott:** capability doc `00_Prompts/BDOS/capabilities/vault-dashboards/CLAUDE.md` · format contract `02_Areas/Sonrisa/CPS/Sales/DASHBOARD_CONTRACT.md` · Curator agent `00_Prompts/BDOS/agents/curator.md`
