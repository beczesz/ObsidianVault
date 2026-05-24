---
title: Ideas Vault, Design System
version: 1.0
date: 2026-05-18
id: 657d663e-2d37-413e-aa6e-6d7384fc8a9a
index_schema_version: 1
---

# Ideas Vault, Design System

Extracted from `Sales/dashboard.html` (CPS Sales dashboard). The Sales dashboard is the visual reference; the root dashboard and any future sub-dashboards inherit this system.

## Color tokens

Warm-neutral page with one terracotta accent (Anthropic-derivative). Restrained palette. Tinted neutrals, never true `#000` or `#fff`.

```
--bg-page:     #faf9f5
--bg-elev:     #ffffff
--bg-sunken:   #f3f1ea
--bg-tint:     #f5f4ef
--ink-1:       #141413
--ink-2:       #3a3a37
--ink-3:       #6d6d6a
--ink-4:       #9c9c98
--ink-5:       #c8c8c2
--line:        #e5e4df
--line-soft:   #efede7
--accent:      #D97757
--accent-deep: #b35a3f
--accent-tint: #fbeee6
```

Semantic colors used in sub-dashboards (do not introduce more without coordination):

```
--hot:        #c0392b   --hot-tint:        #fbeae6
--warm:       #b07a18   --warm-tint:       #fbf2dc
--cold:       #4a5568   --cold-tint:       #edf0f4
--contact:    #2563a5   --contact-tint:    #e8eff8
--discovery:  #6b46c1   --discovery-tint:  #f1eafd
--proposal:   #3f489d   --proposal-tint:   #ebedf8
--won:        #1f7a4d   --won-tint:        #e6f3ec
--lost:       #7a7a76   --lost-tint:       #efeeeb
```

## Typography

Inter for everything UI. JetBrains Mono for code and tabular numerics. No display fonts.

```
font-family: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", system-ui, sans-serif;
mono: 'JetBrains Mono', ui-monospace, "SF Mono", Consolas, monospace;
font-feature-settings: 'ss01', 'cv11';
```

Scale (rem-based, not fluid):

```
h1: clamp(28px, 3.2vw, 40px) / 700 / -0.02em
h2: 18px / 600 / -0.005em
h3: 15px / 600
body: 15px / 400 / 1.45
small: 13px / 400
micro: 11px uppercase / 500 / 0.12em
```

## Spacing

Single 4px base scale: 4, 8, 12, 16, 20, 24, 28, 32, 40, 48, 64, 96. Do not interpolate.

## Radii

```
--radius-s: 4px   (chips, small)
--radius-m: 6px   (buttons)
--radius-l: 10px  (cards)
--radius-xl: 14px (large cards, hero)
```

## Elevation

Three steps. Sparing use.

```
--shadow-1: 0 1px 2px rgba(20,20,19,.04), 0 1px 1px rgba(20,20,19,.02)
--shadow-2: 0 4px 12px rgba(20,20,19,.06), 0 2px 4px rgba(20,20,19,.04)
--shadow-3: 0 12px 32px rgba(20,20,19,.10), 0 4px 12px rgba(20,20,19,.06)
```

## Motion

```
--t-fast: 120ms cubic-bezier(.2,.7,.3,1)
--t-med:  200ms cubic-bezier(.2,.7,.3,1)
--t-slow: 320ms cubic-bezier(.16,.84,.32,1)
```

Motion conveys state, never decoration. No bounce, no elastic, no orchestrated page-load sequences.

## Components

### Card

Background `--bg-elev`, border `--line`, radius `--radius-l`, shadow `--shadow-1`. Hover lifts to `--shadow-2`. Never nest cards. Never use coloured side-stripe borders.

### Pill

Inline rounded chip (`border-radius: 999px`), 4px vertical / 10px horizontal padding, 11px uppercase letter-spaced text. Background uses the relevant tint colour, text uses the matching solid.

### Button

Two variants only.

- Primary: solid `--accent` background, white text, 6px radius.
- Secondary: `--bg-elev` background, `--line` border, `--ink-1` text.

Hover and focus states required. No third variant unless extending the system.

### Resource pill (row)

Compact horizontal link in a strip. Slightly larger hit target than chip, no background, just colour change on hover.

## Layout

- Max width 1480px.
- Page padding clamp(20px, 4vw, 36px) on the sides.
- Vary block padding by section weight (hero gets more, dense data rows less).
- Two grids by default: 3-column for primary cards, list-with-meta-row for secondary content.

## Absolute bans (vault-wide)

- Em-dashes anywhere in content (`—` or `--` used as a dash). Hard rule.
- `#000` or `#fff` neutrals.
- Gradient text.
- Coloured side-stripe borders > 1px.
- Decorative glassmorphism.
- Hero-metric template (big-number-small-label-gradient).
- Identical card grids that go on for rows without rhythm.

## File pattern for sub-dashboards

Each sub-dashboard is one self-contained HTML file. It includes inline CSS (no external stylesheet beyond Google Fonts) and inline JS. It polls markdown via `fetch()` and re-renders. Lives next to the markdown it visualises. Never writes back. Never serves as edit surface. Edits happen in Obsidian.
