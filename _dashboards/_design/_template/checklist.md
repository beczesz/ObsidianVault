---
title: Dashboard pre-commit checklist
date: 2026-05-25
author: Becze Szabolcs
status: active
description: Ellenőrző lista új vagy módosított dashboard commit-olása előtt. A `lint.mjs` ennek a nagy részét automatikusan checkolja — de ez a humán-olvasható "ne felejtsd el" lista. Új dashboardnál mind a 30+ pontot fusd át; meglevő dashboard editálásánál a változás-érintett részeket.
tags: [dashboards, checklist, conventions]
id: 3994cf82-bb8f-474b-b99a-60cb1cad86d5
index_schema_version: 1
---

# Dashboard pre-commit checklist

> **Mikor használd:** új dashboard buildelésénél (mind a 30+ pont), vagy meglevő
> editálásánál (a változás-érintett részek). Automatizált check: `node ../lint.mjs <fájl>`.
> A teljes architektúra-spec: [`../ARCHITECTURE.md`](../ARCHITECTURE.md).

---

## §A — HTML váz (Shell layer)

- [ ] `<!DOCTYPE html>` első sorban
- [ ] HTML komment fejléc 5-soros, audit-trail-lel:
  ```html
  <!--
    =============================================================================
    <Dashboard név>, <egy mondat — mit mutat>.   Version: 0.1.0
    =============================================================================
    Renders from: <markdown forrás path>
    Audit trail:
      0.1.0 (YYYY-MM-DD) initial: ...
    =============================================================================
  -->
  ```
- [ ] `<html lang="en">`
- [ ] `<meta charset="UTF-8">` + viewport
- [ ] `<title>` egyedi, beszédes
- [ ] Inline SVG favicon (cream rounded rect + domain-motívum)
- [ ] Google Fonts preconnect + link: `Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap`
- [ ] **FOUC-init `<script>` a `<head>`-ben** (DS §1b verbatim) — fontok ELŐTT vagy után, de stylesheet előtt

## §B — Design tokens (1. réteg)

*Amíg `tokens.css` engine nincs (Sprint 2 előtt):*
- [ ] `:root { --bg-page: #faf9f5; ... }` blokk **verbatim** a DS §1-ből
- [ ] `:root[data-theme="dark"] { ... }` blokk **verbatim** a DS §1a-ból
- [ ] `@media (prefers-color-scheme: dark) { :root:not([data-theme="light"]) { ... } }` blokk **verbatim**
- [ ] **0 custom hex** a `:root` blokkon kívül (mindenhol `var(--token)`)

*Sprint 2 után:*
- [ ] `<link rel="stylesheet" href="/_dashboards/_design/tokens.css">` jelen
- [ ] Inline `:root` blokk eltávolítva

## §C — Shared shell komponensek (DS §4)

- [ ] **Masthead** `.masthead` → `.masthead-toprow` → `.home-link` + `.theme-toggle`
- [ ] **Home-link**: `<a class="home-link" href="/_dashboards/index.html">Ideas Vault</a>`
      *(absolute URL kötelező, nem relative)*
- [ ] **Theme-toggle button**: `<button class="theme-toggle" id="themeToggle" aria-label="..." title="...">`
- [ ] **Eyebrow + verzió-pill**: `.eyebrow` + `.version-pill` (10px mono)
- [ ] **H1**: `clamp(28px, 3.2vw, 40px)`, weight 700, `.accent` span használat
- [ ] **Submeta** (opcionális): `.submeta` + `.dot` szeparátorral
- [ ] **App container**: `<main class="app">` (NEM `.wrap`), `max-width: 1200px; margin: 0 auto; padding: 28px 36px 96px`
- [ ] **Admin-bar mount-point**: `<div id="bdos-admin-bar"></div>` a `<body>` ELSŐ eleme
- [ ] **Admin-bar script**: `<script src="/_dashboards/_design/admin-bar.js"></script>` a `</body>` előtt

## §D — Theme + clipboard helpers (2. réteg)

*Sprint 1 előtt (jelenleg):*
- [ ] `setTheme(t)` függvény + click listener + storage listener + `initTheme()` IIFE — **verbatim** DS §1c-ből
- [ ] `copyText(text, el)` függvény — **verbatim** DS §4a-ból
- [ ] `wireCopyRef(container)` függvény — **verbatim** DS §4a-ból
- [ ] `const DASH_STEM = '<stem>'` (a HTML fájl neve `.html` nélkül) ‹kötelező›

*Sprint 1 után:*
- [ ] `<script type="module">import { setTheme, initTheme } from '/_dashboards/_design/theme.js'; ...</script>`
- [ ] `import { copyText, wireCopyRef } from '/_dashboards/_design/clipboard.js'`
- [ ] Inline `setTheme`/`copyText`/`wireCopyRef` definíciók eltávolítva

## §E — Live updates (DS §5)

- [ ] `<script src="/_dashboards/_design/live-updates.js"></script>` a `</body>` előtt
- [ ] `LiveUpdates.subscribe(refetchAndRender)` a boot-ban
- [ ] `LiveUpdates.mountStatusIndicator(document.querySelector('.masthead-toprow'))` a masthead-be
- [ ] **NINCS saját** `setInterval(8000, ...)` poll loop (csak a fallback élhet — az is a shared lib-ben)
- [ ] **NINCS** `EventSource(...)` direct (csak a shared lib-ben)

## §F — Kártyák + copy-ref (DS §4a)

- [ ] Minden bounded kártya `data-card-id="<slug>"`-gel
- [ ] Minden ilyen kártyán `.card-copy-ref` button (SVG icon + "copy ref")
- [ ] A kártya-szelektor (`.card`, `.vendor`, `.agent-card`, stb.) `position: relative`
- [ ] Hover/focus-within → `.card-copy-ref` `opacity: 1`
- [ ] Click handler: `e.stopPropagation()` + `copyText(DASH_STEM + ':' + card.dataset.cardId, btn)`
- [ ] Dynamic render után: `wireCopyRef(gridEl)` hívás
- [ ] `<button>` real element (nem `<div>`), `aria-label="Kártya-azonosító másolása"`

## §G — Markdown parsing (Domain layer)

*Sprint 3 előtt:*
- [ ] `parseYamlFrontmatter()` **verbatim** a DS-ből vagy a `team.html`-ből másolva (87 sor)

*Sprint 3 után:*
- [ ] `import { parseYamlFrontmatter } from '/_dashboards/_design/markdown-parser.js'`
- [ ] Inline parser definíció eltávolítva

- [ ] **Read-only**: `fetch()` mindig `{ cache: 'no-store' }`-ral, soha `POST`/`PUT`
- [ ] **Hibakezelés**: ha a markdown fetch fail, "data unavailable" empty-state, nem white screen

## §H — Sidecar JSON (csak agent-dashboardoknak)

- [ ] `agent_logs.json` fetch: `/_dashboards/_design/agent_logs.json`
- [ ] Filter: `events.filter(e => e.agent_name === LOGS_AGENT)` *(NEM `e.agent`!)*
- [ ] Schema v2 check: `sidecar.scheduled_jobs` array preferred, fallback ha hiányzik
- [ ] `schema_version >= 2` esetén a `scheduled_jobs` path él

## §I — Verzió + audit trail

- [ ] Verzió-pill HTML-ben matchel a HTML komment audit-trail UTOLSÓ sorával
- [ ] Verzió-bump szabály:
  - patch (`0.x.Y`): bugfix, doc-only, audit-trail edit
  - minor (`0.X.0`): új feature, shared lib bevezetés, új panel
  - major (`X.0.0`): URL-forrás vált, breaking redesign
- [ ] Audit-trail új sor formátum: `0.x.y (YYYY-MM-DD) <imperativ leírás>`

## §J — Launcher + index regisztráció

- [ ] **Új dashboard esetén**: `index.html` launcher tree-jébe bekerült (megfelelő tab + leaf-card)
- [ ] **Új dashboard esetén**: `00_DASHBOARD_INDEX.md` tábla új sor (név, verzió, adatforrás, pattern, DS compliance)
- [ ] **Új dashboard esetén**: `data-card-id` egyedi a launcher leaf-en is

## §K — Tilalmas (anti-pattern guard)

- [ ] **NINCS** `npm install`, `package.json`, `node_modules/`
- [ ] **NINCS** új `<script src="cdn..../*.min.js">` CDN bevezetés
- [ ] **NINCS** custom hex `#...` `:root` token-deklaráción kívül
- [ ] **NINCS** saját `EventSource` vagy direct `setInterval` polling
- [ ] **NINCS** markdown write-back (`fetch(..., {method: 'POST'})`)
- [ ] **NINCS** `e.agent === ...` field használat (csak `e.agent_name`)
- [ ] **NINCS** ops-header.js script új dashboardban (használd admin-bar.js-t — DS §5b deprecated)
- [ ] **NINCS** Tailwind/utility-class library
- [ ] **NINCS** TypeScript compile step

## §L — Vizuális regression

- [ ] Megnyitod a dashboardot light + dark mode-ban → mindkettő olvasható
- [ ] Theme-toggle működik, label/icon vált, localStorage perzisztens
- [ ] Másik tabban másik dashboard → theme-váltás szinkronizál (storage event)
- [ ] Admin-bar 5 status pill látszik, hover tooltip működik
- [ ] Hover egy kártyán → `.card-copy-ref` előjön
- [ ] Click rajta → "copied" pulse, valóban a vágólapon a helyes `stem:card-id`
- [ ] Markdown forrást módosítod → SSE event érkezik → re-render automatikus (sub-sekundum)
- [ ] events_server.py-t leállítod → `.lu-pill` amberre vált ("polling fallback"), továbbra is működik

## §M — Lint + audit

- [ ] `node _dashboards/_design/lint.mjs <fájl>` → **zöld** (0 error)
- [ ] Warning-ok címkézve a commit message-ben, ha tudatosan hagyod ott
- [ ] `/dash-audit <fájl>` Curator-tal → green report (opcionális, ajánlott új dashboardnál)

## §N — Commit message

Sablon:
```
feat(dashboards): <dashboard> <change>

- <bullet 1>
- <bullet 2>
- DS <version> compliant
- lint: green
- audit: <result>

Affected: <fájl>, <fájl>
Audit-trail bump: <old> → <new>
```

---

## Quick reference — minimum scaffold méret

Új dashboard tipikus minimum (csontváz + 1 kártya):
- HTML: ~250 sor (a fenti §A-§F)
- JS boot: ~80 sor (parser + render + wire)
- Total: ~330 sor

Bármi 200 sor alatti gyanúsan rövid (valami kimaradt), bármi 600 sor feletti
csontvázként gyanúsan hosszú (valami nincs shared lib-ben).
