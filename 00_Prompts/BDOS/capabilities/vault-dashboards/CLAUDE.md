---
title: Vault Dashboards Capability
version: 0.2
date: 2026-05-20
author: Becze Szabolcs
status: active
description: BDOS capability for building live, read-only, markdown-driven HTML dashboards for any vault unit. Extracted from two working reference implementations (CPS Sales, CPS Partnerships) plus the tree launcher. All dashboard code lives in `_dashboards/`; a zero-dependency Node server (`_dashboards/_tools/dash-server.mjs`) serves the vault root and pushes file-change events over SSE. Any session asked to build or develop a dashboard reads this first.
id: d3bfd81e-3126-4af6-ba00-0b0b0519c972
index_schema_version: 1
---

# Vault Dashboards

> A repeatable way to turn any set of vault markdown into a live, interactive HTML dashboard that auto-syncs and never needs to be regenerated when the data changes.

## When to use this capability

Trigger when the user asks to build, develop, or extend a dashboard for an Area, sub-Area, or data set in the vault (for example: "build a dashboard for Marketing", "make an AI Ops board", "develop the Deák dashboard"). Also when extending an existing dashboard with a new widget, view, or data source.

Do NOT regenerate a dashboard's HTML to change its displayed data. The HTML is a renderer. Content lives in markdown. Edit the markdown.

## The model in one paragraph

A vault dashboard is a single self-contained `dashboard.html` file that, when served over HTTP, fetches one or more markdown files every 8 seconds, parses them, and renders an interactive view (kanban, status board, cards, widgets). It is read-only: the markdown is the single source of truth, all edits happen in Obsidian. The HTML carries the design system, the parsers, and the sync loop inline. No build step, no database, no framework.

## Reference implementations (study these before building)

| Dashboard | Path | Version | Pattern it demonstrates |
|---|---|---|---|
| **CPS Sales** | `_dashboards/sales.html` | 0.7.0 | Pipeline kanban + today panel + drawer. **Per-record file** data pattern (one NOTES.md per lead, discovered via Pipeline.md). Multi-file sync. Rich drawer with `source_url` CTA, copy-to-clipboard drafts. SSE push + poll fallback. |
| **CPS Partnerships** | `_dashboards/partnerships.html` | 0.2.0 | Status board with vendor cards, coverage bars, requirement met/gap tracking, renewal countdown. **Single-frontmatter-file** data pattern (one `partners.md` with a frontmatter array). |
| **Launcher** | `_dashboards/index.html` | 0.3.0 | Tree-style navigation. Collapsible Areas, org-chart sub-trees, TBD vs live leaves. Served at `/`. |
| **Server** | `_dashboards/_tools/dash-server.mjs` | n/a | Zero-dependency Node static server + `fs.watch` file watcher pushing SSE on `02_Areas/**/*.md` changes. |

Format contract for the Sales family: `02_Areas/Sonrisa/CPS/Sales/DASHBOARD_CONTRACT.md` (its "Shared dashboard conventions" section is the law for every dashboard).

## Two data-source patterns, pick one

**1. Per-record files** (Sales pattern). One markdown file per record, discovered via an index file.
- Use when: records are numerous (15+), edited individually, each has rich per-record content (prose sections, drafts, contacts).
- Example: `Accounts/Leads/<Name>/NOTES.md` discovered through `Pipeline.md`.
- Cost: more fetches per poll (one per record), needs a folder-name derivation + index parser.

**2. Single frontmatter file** (Partnerships pattern). One markdown file with a frontmatter array.
- Use when: few records (3 to 15) with structured fields, the whole set is naturally edited together.
- Example: `Partnership/partners.md` with a `partners:` array.
- Cost: one fetch per poll, simplest to parse. Heavy nested prose does not fit well in YAML.

When unsure, start with pattern 2 (single file). Promote to pattern 1 only when the per-record content outgrows frontmatter.

## Shared building blocks (copy from a reference, do not reinvent)

- **Design tokens**: the `:root` CSS block. Cream `--bg-page: #faf9f5`, accent `--accent: #D97757`, the ink scale (`--ink-1` to `--ink-5`), line colors, radius scale, motion timings. Inter for UI, JetBrains Mono for code / metrics / dates.
- **YAML frontmatter parser**: `parseYamlFrontmatter(md)`. Handles scalars, inline + block arrays, block objects, arrays of objects with nested arrays. Quote-aware comment stripping (so `#2` inside a string is safe). Copy verbatim from the Partnerships dashboard.
- **Markdown section parser**: `parseMarkdownSections(body)`. H2 / H3 sections to slots, with bullet lists, checklists, tables, and fenced code blocks. Copy from the Sales dashboard when the dashboard needs body-section content (drafts, tables).
- **Sync layer**: `pollVault()` + `startPolling()`. Fetch with `cache: 'no-store'`, compare to last content, rebuild + render only on change, 8 second interval.
- **Sync indicator**: the dot + "Updated Ns ago, next in Ms" label + progress bar + click-to-refresh. Copy the CSS (`.sync-status`, `.sync-bar`, the `sync-countdown` / `sync-shuttle` keyframes) and the JS (`syncLabel`, `setSyncState`, `tickSyncLabel`, `resetSyncBar`).
- **Home button**: top-left of the masthead, `href="/_dashboards/index.html"` (absolute). Copy the `.home-link` CSS + the markup snippet.
- **SSE client**: ~15 lines that connect to `/__events`, fire `pollVault()` on a `change` event, and relax the poll timer to 30s while connected (8s fallback on error). Copy from either reference dashboard's `connectEventStream()`.

## Build recipe

1. **Identify data sources.** What vault markdown holds the data? Read it. Decide the data-source pattern (per-record vs single-file).
2. **Design the schema.** Frontmatter fields + (if needed) body sections. Keep frontmatter shallow where possible. Document required vs optional fields.
3. **Create the source markdown** from existing vault material. Do not duplicate, reformat or summarize the canonical content into the dashboard source, and link the deep reference files via `obsidian://` deep links.
4. **Scaffold the HTML**: doctype + version comment header + head (fonts, tokens) + masthead (home button, eyebrow, title, version pill, sync indicator) + content containers.
5. **Copy the parser(s)** needed for the chosen pattern.
6. **Write render functions**: widgets row (overview metrics) + the main view (cards / board / table). Keep them pure functions of the parsed data so polling can re-render idempotently.
7. **Wire the sync loop**: `pollVault` fetches, parses, sets the global data array, calls render, updates the sync indicator. Boot with one immediate poll then `startPolling` + `startTicker`.
8. **Version it**: `0.1.0` in the comment header (with a dated audit trail) and the visible pill.
9. **Serve and verify**: `npx serve .` in vault root, open `http://localhost:<port>/<path>/dashboard.html`, confirm live sync (edit the markdown, watch it update within 8s).
10. **Register in the launcher**: flip the leaf in root `index.html` from `Dashboard TBD` to an `Open →` button, bump the index version.
11. **Document new conventions**: if the dashboard introduces a new format pattern, add it to `DASHBOARD_CONTRACT.md`.

## The laws (from DASHBOARD_CONTRACT.md "Shared dashboard conventions")

1. **Home button** to `/index.html` (absolute, depth-independent) in every dashboard masthead.
2. **Versioning**: start `0.1.0`. `0.0.x` tweak, `0.x.0` structural, `x.0.0` cross-team canonical. Dated audit trail in the comment header.
3. **Shared design tokens**, never a per-dashboard palette.
4. **Live read-only sync**: fetch + 8s poll, rebuild on change, never write back, file:// fallback.
5. **Edit markdown, not HTML.** The HTML is the renderer. Bump the version when you touch it.
6. **Register in the launcher** when a dashboard goes live.

## Anti-patterns

- Hardcoding data in the HTML beyond a small offline fallback snapshot.
- Relative home-button paths (`../../../index.html`), they break per depth.
- A new color palette or font stack per dashboard.
- Regenerating the HTML to change content.
- Deep prose crammed into YAML (use the per-record + body-sections pattern instead).
- Writing back to the markdown from the dashboard (it is read-only by contract).

## Serving

Dashboards require an HTTP origin (browser security blocks `fetch()` from `file://`). The standard server is `_dashboards/_tools/dash-server.mjs` (pure Node, zero install): serves the vault root, routes `/` to the launcher, and pushes SSE on `*.md` changes.

```
# Windows
_dashboards\_tools\start.bat        (double-click) or start.ps1
# macOS / Linux
bash _dashboards/_tools/start.sh
# manual / any platform
node _dashboards/_tools/dash-server.mjs        (PORT=8000 to override)
```

Open `http://localhost:4321/`. A plain static server (`npx serve .` from vault root) also works but without the instant push (open `/_dashboards/`); the poll timer keeps it live.

## Future direction

- Extract the shared building blocks (tokens, parsers, sync, sync indicator, SSE client) into a single `_dashboards/_engine/` of importable JS/CSS modules so dashboards reference rather than copy. Deferred until a third dashboard confirms the shared surface is stable.
- A `/dash-build <unit>` slash command that runs this recipe interactively.
- Migrate the legacy ad-hoc dashboards (Strategy, ExarLabs, Movies, Onriva, Mikado, Média, Ignis, Deák/BIN) into `_dashboards/` as they are touched.

## Referenced documents

- Format contract + shared conventions: [`../../../../02_Areas/Sonrisa/CPS/Sales/DASHBOARD_CONTRACT.md`](../../../../02_Areas/Sonrisa/CPS/Sales/DASHBOARD_CONTRACT.md)
- Lead schema template: `02_Areas/Sonrisa/CPS/Accounts/_Template/LEAD_NOTES.md`
- BDOS capabilities index: [`../../CLAUDE.md`](../../CLAUDE.md)
