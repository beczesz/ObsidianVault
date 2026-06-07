---
title: New Dashboard — Onboarding (step-by-step)
date: 2026-05-25
author: Becze Szabolcs
status: active
description: Step-by-step guide to scaffolding a new dashboard from `_template/index.html`. Lists the 8 places to edit, the canonical naming rules, registration, and the lint validation gate. Use this together with `checklist.md`.
tags: [dashboards, onboarding]
id: dbff869f-ef00-4dc7-973e-64dac892420d
index_schema_version: 1
---

# New Dashboard — Onboarding

> **Pre-read**: [`../../CLAUDE.md`](../../CLAUDE.md) → [`../ARCHITECTURE.md`](../ARCHITECTURE.md).
> **Validation**: every step ends with `node _dashboards/_design/lint.mjs <your-file>` — must be green.

## Step 0 — Decide where the dashboard lives

| Pattern | Location | When to use |
|---|---|---|
| Top-level single-file | `_dashboards/<name>.html` | Most dashboards (agents, plugins, partnerships, …) |
| Per-agent subdir | `_dashboards/<agent>/index.html` | Per-agent observatory (broker, curator, …) |

Pick `<name>` — kebab-case, no extension. Examples: `marketing`, `learnings`, `mybrand`.

This becomes your **DASH_STEM** (the card-id prefix). E.g. `team.html` → `DASH_STEM = 'team'`; cards then get refs like `team:unit/acme`.

## Step 1 — Copy the scaffold

```bash
cp _dashboards/_design/_template/index.html _dashboards/<name>.html
```

Or for a per-agent dashboard:

```bash
mkdir -p _dashboards/<agent>
cp _dashboards/_design/_template/index.html _dashboards/<agent>/index.html
```

## Step 2 — Edit the HTML comment header (top of file)

8 things to update:

1. Replace `TEMPLATE — replace with: ...` → real dashboard name + one-line description
2. `Version: 0.1.0` → keep at 0.1.0 for initial
3. `Renders from:` → list the markdown source path(s)
4. `Audit trail:` → keep the `0.1.0 (today) initial: <what>` line
5. `<title>` → human-readable, used in browser tab + admin-bar breadcrumb
6. Favicon SVG — adjust the inline icon if you want a domain-specific glyph
7. `TEMPLATE` eyebrow text → real eyebrow label
8. `Dashboard Name` H1 → real name (keep the `<span class="accent">` highlight on the key word)

## Step 3 — Edit the per-dashboard config (`<script>` near bottom)

```js
const DASH_STEM = 'mydashboard';                       // == filename without .html
const DATA_URL  = '/02_Areas/Foo/Bar/source.md';       // markdown source
```

If you fetch multiple sources, change `fetchData()` to fetch them in parallel and merge.

## Step 4 — Adjust the data shape

The template assumes frontmatter has an `items:` array. Replace with your real schema:

```yaml
---
title: My data
items:
  - name: Foo
    description: A thing
  - name: Bar
    description: Another thing
---
```

OR for a flat single-record dashboard:

```yaml
---
title: Status
status: green
last_update: 2026-05-25
---
```

Adjust `refetchAndRender()` accordingly. Use `parsed.frontmatter.<your-field>`.

## Step 5 — Adjust the render

The template's `renderCards()` is a card-grid skeleton. You may want:
- multiple sections / tabs
- a table instead of cards
- a "single big record" layout

**Whatever the layout, every bounded card-like element MUST have**:
- `data-card-id="<stable-slug>"` (slug derived from data via `toSlug()`)
- `.card-copy-ref` button inside (mandatory per DS §4a)
- after rendering, call `wireCopyRef(containerEl)`

## Step 6 — Register in the launcher

Edit `_dashboards/index.html` and add your dashboard to the appropriate tab + leaf-card tree. The launcher itself uses card-ids — pick a unique one.

## Step 7 — Register in `00_DASHBOARD_INDEX.md`

Add a row to the table (Curator-managed file): name, version, data source, pattern, DS compliance.

## Step 8 — Lint validation gate

```bash
node _dashboards/_design/lint.mjs <your-new-file>
```

Must show:

```
✓ PASS — 1 file(s) · 0 error · 0 warning · 0 info
```

If you get warnings, look up the rule ID in [`checklist.md`](checklist.md) and fix. **Do not commit with errors.** Warnings should have a known reason (and ideally be addressed).

## Step 9 — Final pre-commit checklist

Open [`checklist.md`](checklist.md) and tick through §A-§N. Most are auto-covered by the template, but some need your verification (e.g. theme toggle works in both modes, SSE live-update fires when you edit the markdown).

## Anti-pattern reminders (don't!)

- ❌ Don't copy from `sales.html`, `agents.html`, or any large dashboard — those have domain-specific code that won't apply.
- ❌ Don't inline `setTheme()`, `copyText()`, `parseYamlFrontmatter()`, `escapeHtml()`, `toSlug()` — all loaded as globals from `_design/`.
- ❌ Don't inline `:root { --bg-page: ... }` canonical tokens — `tokens.css` is `<link>`-ed.
- ❌ Don't add `npm install`, `node_modules/`, build step. Vault is zero-build.
- ❌ Don't write back to markdown from JS. Dashboards are read-only renderers.
- ❌ Don't set up your own `setInterval` poll loop. Use `LiveUpdates.subscribe()`.

## Hivatkozott

- [`../../CLAUDE.md`](../../CLAUDE.md) — discovery layer
- [`../ARCHITECTURE.md`](../ARCHITECTURE.md) — normative spec
- [`../DESIGN_SYSTEM.md`](../DESIGN_SYSTEM.md) — vizuális token-referencia
- [`checklist.md`](checklist.md) — pre-commit ellenőrző
- [`../lint.mjs`](../lint.mjs) — auto-validator
- [`index.html`](index.html) — a scaffold maga (lint-zöld baseline)
