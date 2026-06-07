---
title: Dashboard family — kontextus minden dashboard-editáláshoz
date: 2026-05-25
author: Becze Szabolcs
status: active
description: Auto-loaded discovery layer minden `_dashboards/` alatti munkához. Felsorolja a 7 törvényt, a shared library import-kötelezettségeit, és az új dashboardra vonatkozó scaffold-szabályt. Ez a fájl pointer az ARCHITECTURE.md normatív specre + a DESIGN_SYSTEM.md teljes referenciára.
tags: [dashboards, conventions, claude-md]
id: 643d2304-30be-4e0c-be34-84f07ee246e6
index_schema_version: 1
---

# Dashboard family — olvasd el ezt MIELŐTT bármit szerkesztenél itt

> **Claude Code automatikusan beolvassa ezt a fájlt**, amikor bármit módosítasz
> a `_dashboards/` alatt. Ez a discovery layer. A teljes normatív specifikáció:
> **[`_design/ARCHITECTURE.md`](_design/ARCHITECTURE.md)** — olvasd el azt is
> minden nem-triviális változtatás előtt. A vizuális design-rendszer (32K, tokenek,
> komponensek, az "alkotmány" összes szabálya): **[`_design/DESIGN_SYSTEM.md`](_design/DESIGN_SYSTEM.md)**.

## A 7 törvény (DS §6) — NEM megsérthető

1. **Home button** — minden dashboard masthead-jén `<a class="home-link" href="/_dashboards/index.html">`
2. **Verzió-pill + audit-trail HTML komment** — minden HTML-érintés verzió-bumppal jár, és audit-trail sorral a fejlécben
3. **Csak kanonikus design-tokenek** — semmi custom hex; minden szín `var(--token)` formában
4. **Live read-only sync** — `LiveUpdates` shared helper (SSE primary + 8s poll fallback); **soha NE írj vissza** markdownba JS-ből
5. **Edit a markdown forrást** (`02_Areas/...` vagy `00_Prompts/...`), nem a dashboardot — a dashboard csak renderer
6. **Regisztráld** új dashboardot az `index.html` launcher-ben + a `00_DASHBOARD_INDEX.md`-ben
7. **Kód a `_dashboards/`-ban**, content máshol — soha NE co-locate

## Shared library — ezeket KÖTELEZŐ használni új kód előtt

Mielőtt írnál egy függvényt vagy egy CSS-blokkot, **nézd meg, létezik-e már**:

| Funkció | Hol él | Mit ad |
|---|---|---|
| `LiveUpdates.subscribe()`, `mountStatusIndicator()` | `_design/live-updates.js` | SSE → `/__events` (dash-server, port 4321); auto-fallback 8s poll; status pill render. **Single-server (2026-05-29): port 4322 retired** — dash-server.mjs is the only browser-facing server (SSE + `/health`). |
| `AdminBar.mount()` (auto) | `_design/admin-bar.js` | Fixed dark top bar, 5 health pill, system drawer. Watchdog pill reads dash-server `/health` (4321). |
| `setTheme()`, `initTheme()` ✅ | `_design/theme.js` (DS 0.7.0) | Theme toggle + localStorage `dash-theme` cross-tab sync. **Auto-wires `#themeToggle` és cross-tab storage sync DOMContentLoaded-kor.** |
| `copyText()`, `wireCopyRef()` ✅ | `_design/clipboard.js` (DS 0.7.0) | Clipboard API + textarea fallback; pulse-state. `wireCopyRef(gridEl)` explicit hívandó render után. |
| `parseYamlFrontmatter()` ✅ részleges | `_design/markdown-parser.js` (DS 0.7.2) | Kanonikus 87-soros parser (nested obj, indent stack, quote-aware comment-strip, scalar coercion). **3 dashboardon élesen** (partnerships, team, navigator); a többi 6 inline parsert tart fenn (sales/aiops/broker/librarian/presto/sage — funkcionálisan eltérnek, Curator promote backlog). **Új dashboardban**: töltsd be ezt, NE inline-old. |
| Kanonikus design-tokenek ✅ | `_design/tokens.css` (DS 0.7.1) | `<link rel="stylesheet" href="...tokens.css">` a `<head>`-ben, a `<style>` blokk ELŐTT. Tartalom: DS §1 light :root + §1a dark override + `@media prefers-color-scheme`. **Domain-specifikus tokenek** (pl. `--hot`, `--info`, `--sonrisa`) maradnak a dashboard saját `:root`-jában. |
| `escapeHtml()`, `toSlug()` ✅ | `_design/dom-utils.js` (DS 0.7.3) | Új dashboardnál használd ezeket. Meglevő dashboardok inline-os verzióit nem migráljuk (3-soros függvények, mass-migráció kockázat > nyereség). |
| `AgentLogs.fetch()`, `filterByAgent()`, `formatTimestamp()` ✅ | `_design/agent-logs.js` (DS 0.7.3) | Sidecar `agent_logs.json` helper-réteg. Schema v2 aware. Új per-agent dashboardban kötelező; meglevők saját inline-os mintát tarthatnak. |

> **DS 0.7.0–0.7.1 óta (Sprint 1+2a):** a `theme.js`, `clipboard.js`, és
> `tokens.css` engine-extracted — új dashboardban NE inline-old, hanem `<script src=>`
> / `<link rel=stylesheet>` taggel töltsd be. A komponens-CSS (`.theme-toggle`,
> `.home-link`, `.card-copy-ref` stb.) és a YAML parser EGYELŐRE inline marad
> (Sprint 3 a parsert extrahálja; a komponens-CSS Curator promote-feladat).

## Új dashboard előtt

→ **NE másolj** `sales.html`-ből vagy más bonyolult dashboardból — túl sok domain-specifikus kód.
→ Indulj **[`_design/_template/index.html`](_design/_template/index.html)**-ből (DS 0.7.3 óta él, 100% lint-zöld baseline).
→ Kövesd: **[`_design/_template/ONBOARDING.md`](_design/_template/ONBOARDING.md)** — 9 lépéses step-by-step.
→ Commit előtt: **[`_design/_template/checklist.md`](_design/_template/checklist.md)**.
→ Validációs futtatás: `node _design/lint.mjs <fájl>` — minden DS-szabályt automatikusan checkol.

## Card copy-ref — KÖTELEZŐ minden kártyán (DS §4a)

> **Minden bounded card-like elemen** `data-card-id` + `.card-copy-ref` button kell legyen.
> Ez NEM opcionális tend — build-time kötelező, az első commit-tól. **NO EXCEPTIONS.**

Ha bármilyen kártya-szerű elemet renderelsz (`.card`, `.vendor`, `.agent-card`, `.channel-card`,
`.learning-card`, `.entity-card`, bármi ami kártya-kinézetű doboz), a sablon **mindig** tartalmazza:

1. `data-card-id="<type>/<slug>"` a wrapper elemen (stabil, determinisztikus slug)
2. `<button class="card-copy-ref" aria-label="Kártya-azonosító másolása" data-for-card onclick="event.stopPropagation()">` a kártyán belül
3. `wireCopyRef(containerEl)` hívás a render után

**Miért:** a felhasználó bármelyik kártyát tudja referálni (`presto:channel/linkedin`,
`presto:learning/timing-thursday-peak`) — hover-re megjelenik a copy gomb, click-re
a vágólapra másolódik `DASH_STEM:card-id`. Ez a vault-szintű "mindent meg tudok hivatkozni" elv.

**Hogyan marad ki:** új panel/kártya típus hozzáadásakor a fejlesztő a domain logikára
koncentrál (frontmatter parse, render, empty state), és elfelejti a copy-ref wiring-et.
**Ellenőrzés:** minden `innerHTML = ...map(...)` hívás után keresd a `data-card-id` +
`.card-copy-ref` + `wireCopyRef()` hármast.

## Edit-előtti rituálé (kötelező nem-triviális változtatáshoz)

1. Olvasd el a [`_design/ARCHITECTURE.md`](_design/ARCHITECTURE.md) releváns szekcióját
2. Ellenőrizd: a változtatás megsérti-e a 7 Laws egyikét?
3. Ellenőrizd: létezik-e már a funkció shared library-ben? (lásd táblázat fent)
4. **Új kártya/panel?** → `data-card-id` + `.card-copy-ref` + `wireCopyRef()` (DS §4a — lásd fent)
5. Edit után **bump a version-pillt** + új audit-trail sor a HTML komment fejlécben
6. Ha új vizuális/JS minta születik → DS-promote candidate, jelezd Curator-nak (`/dash-promote`)
7. Futtasd: `node _dashboards/_design/lint.mjs <a-fájl>` — zöld kell hogy legyen

## Tilalmas (lint-elt szabályok)

- ❌ Custom hex color (`#abc123`) `:root` token-deklaráción kívül
- ❌ Saját `setTheme()` / `copyText()` / `parseYamlFrontmatter()` implementáció (Sprint 1-3 után)
- ❌ Inline `:root { --token: ... }` blokk új dashboardban (Sprint 2 után — `<link>` helyette)
- ❌ Write-back JS-ből markdownba (mindig csak fetch)
- ❌ `npm install`, build step, `node_modules/` bevezetése (vault konvenció: **zero build**)
- ❌ Hiányzó home-link, hiányzó verzió-pill, hiányzó admin-bar mount-point
- ❌ FOUC-init script ELHAGYÁSA (a `<head>`-ben kötelező, pre-paint kényszer)
- ❌ Új dashboard launcher-regisztráció nélkül
- ❌ Kártya-elem `data-card-id` és `.card-copy-ref` NÉLKÜL (DS §4a — build-time mandatory, nem opcionális tend)

## Curator agent kapcsolat

A `_dashboards/` család tulajdonosa a **Curator agent** (`00_Prompts/BDOS/agents/curator/`). Ő:
- auditál a 7 Laws ellen (`/dash-audit`)
- promote-ál új patterneket a DS-be (`/dash-promote`)
- karbantartja a `00_DASHBOARD_INDEX.md` live indexet (`/dash-survey`)
- buildel új dashboardokat a `_design/_template/`-ből (`/dash-build`)

Ha bármit változtatsz a családon, Curator-ot is értesítsd — vagy futtasd magad a `/dash-audit`-ot a végén.

## Hivatkozott fájlok

- [`_design/ARCHITECTURE.md`](_design/ARCHITECTURE.md) — normatív spec (WHY + HOW)
- [`_design/DESIGN_SYSTEM.md`](_design/DESIGN_SYSTEM.md) — teljes vizuális referencia
- [`_design/_template/checklist.md`](_design/_template/checklist.md) — pre-commit lista
- [`_design/lint.mjs`](_design/lint.mjs) — automatikus konvenció-checker
- [`00_DASHBOARD_INDEX.md`](00_DASHBOARD_INDEX.md) — live családi index
- [`README.md`](README.md) — szerver-futtatás, dev workflow
