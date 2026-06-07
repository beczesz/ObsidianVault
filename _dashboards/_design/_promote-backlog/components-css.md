---
title: Promote — components.css alignment
description: "Align divergent component CSS variants across 16 dashboard files before extracting them into a shared _design/components.css. Includes divergence matrix, canonical form proposals for .home-link, .version-pill, and .masthead-toprow, plus phased rollout plan."
description_source: auto
description_hash: 5dc6c26b2078b4d2
date: 2026-05-25
status: pending
priority: medium
estimated_loc_savings: 500
risk: medium
discovered_in: Sprint 2b (2026-05-25)
id: f9d17c52-ed44-479b-be54-3baedd9ec852
index_schema_version: 1
---
# Promote — components.css alignment

> **Cél:** kivonni a duplán élő komponens-CSS-eket (`.theme-toggle`, `.home-link`, `.masthead*`, `.version-pill`, `.card-copy-ref`, `.eyebrow`) egy közös `_design/components.css`-be, ÉS előtte aligningolni a divergens variánsokat.

## Miért nem ment mechanikusan a Sprint 2b-ben

A 2026-05-22 audit "100% identikusnak" mondta a komponens-CSS-eket. A 2026-05-25 reality check (Sprint 2b) szerint **legalább 4 valós divergencia** van — mechanikus extract vagy összetörne intentional variációkat, vagy fragments-only nyereséget adna.

## Divergencia-mátrix (2026-05-25 állapot)

### `.home-link`

| Variáns | Fájlok | Eltérés a "canonical" partnerships-től |
|---|---|---|
| Canonical | team, agents, partnerships, sales, navigator, aiops, plugins, … (~12) | font-size 12px, weight 500, padding `5px 11px 5px 9px`, transition `all` |
| Compact uppercase | broker | font-size **11px**, weight **600**, letter-spacing `.04em`, **text-transform: uppercase**, padding `5px 12px`, transition `color, border-color` |
| Pretty-printed | sales | mint a canonical, de multi-line CSS + extra `text-decoration: none` |

### `.version-pill`

| Variáns | Fájlok | Eltérés |
|---|---|---|
| Canonical multi-line | majority | font-size 10px, padding `1px 7px`, border-radius `999px` |
| Compact one-line | broker, curator, librarian, scheduler | font-size 10.5px, padding **`2px 8px` vagy `2px 6px`**, border-radius `999px`, többi azonos |

### `.masthead-toprow`

| Variáns | Fájlok | Eltérés |
|---|---|---|
| Canonical | majority | gap 12px, margin-bottom **14px** |
| Compact one-line | broker (és néhány más) | gap 12px, margin-bottom **20px** |

### `.card-copy-ref`

| Variáns | Fájlok | Eltérés |
|---|---|---|
| Canonical | majority | top 10px, right 10px |
| Variant | (TBD audit) | esetleg más pozícionálás per card-container |

## Javasolt kanonikus formák

### `.home-link` — JAVASLAT: maradjon a **canonical** (12 fájl-os többség)

```css
.home-link {
  display: inline-flex; align-items: center; gap: 7px;
  font-size: 12px; font-weight: 500; color: var(--ink-3);
  text-decoration: none; padding: 5px 11px 5px 9px;
  border: 1px solid var(--line); border-radius: 999px;
  background: var(--bg-elev); transition: all var(--t-fast);
}
.home-link:hover { color: var(--accent-deep); border-color: var(--accent); background: var(--accent-tint); transform: translateX(-2px); }
.home-link svg { flex-shrink: 0; }
```

**Broker-edge case:** a 11px uppercase forma "compact-monospace" érzetet ad ami a Broker dashboard "trading-terminal" hangulatához passzol. Lehet hogy szándékos. **Curator döntés szükséges**: mash to canonical, vagy promote broker-mintát egy második `.home-link.compact` modifier-ként?

### `.version-pill` — JAVASLAT: új kanonikus = **a minority** (broker/curator/librarian/scheduler)

A `2px 8px` padding + 10.5px font-size visually jobban olvasható kicsinél (verzió-pill kicsi UI elem). Javaslom **promote ezt a verziót** kanonikussá:

```css
.version-pill {
  font-family: 'JetBrains Mono', monospace; font-size: 10.5px; color: var(--ink-3);
  background: var(--bg-elev); border: 1px solid var(--line); padding: 2px 8px;
  border-radius: 999px; font-weight: 500;
}
```

Rollout: 13 fájl alignol erre (1px font-size + padding bump). Vizuálisan minimális változás.

### `.masthead-toprow` — JAVASLAT: maradjon **canonical** (margin-bottom 14px)

Broker 20px valószínűleg accidental. Align broker-en.

## Rollout terv

### Fázis 1: alignment (DS-promote döntéseket nem hoz, csak alignol)
Per komponens, per fájl: a divergens variánst → canonical formára cseréljük.

- `.home-link` broker outlier: DECIDE FIRST. Ha "promote modifier" → új `.home-link.compact` class, broker használja. Ha "align" → broker style canonical-re cserélődik.
- `.version-pill` 13 fájl: padding+font-size bump
- `.masthead-toprow` broker: margin-bottom 20px → 14px
- `.home-link` sales pretty-printed: kompresszálni canonical-re (kozmetikus, nem funkcionális)

### Fázis 2: engine extract (csak alignment UTÁN)
- Új `_design/components.css` a kanonikus blokkokkal
- 16-17 fájlból törlés a `.home-link`, `.theme-toggle`, `.masthead-toprow`, `.version-pill`, `.card-copy-ref` definíciók (most már mindegyik azonos a kanonikussal)
- `<link rel="stylesheet" href="/_dashboards/_design/components.css">` mindenhol a `tokens.css` után

### Fázis 3: validate
- Vizuális regression: minden dashboardot megnyitsz light+dark mode-ban
- Screenshot diff opcionális
- `node lint.mjs` zöld

## Kockázatok

- 🟡 **Vizuális regression** — kicsi padding/margin változások szemmel láthatóak lehetnek. Mitigation: dry-run + screenshot per dashboard.
- 🟡 **Broker compact ethos** — ha broker tudatosan compact, az alignment elveszi a karakterét. Mitigation: confirm first.
- 🟢 **Lint** — egyik rule sem érintett.

## Becsült LOC nyereség

| Komponens | LOC per fájl | × fájl | Total |
|---|---|---|---|
| `.home-link` family (3 selector) | 10 | 16 | 160 |
| `.theme-toggle` family (3 selector) | 10 | 16 | 160 |
| `.masthead-toprow` | 3 | 16 | 48 |
| `.version-pill` | 5 | 16 | 80 |
| `.card-copy-ref` family (3 selector) | 12 | 16 | 192 |
| **Kanonikus components.css** | -200 | 1 | -200 |
| **Net** | | | **~440 LOC** |

## Rollback terv

Ha a vizuális regression elfogadhatatlan: `git checkout` a `_dashboards/*.html` fájlokra. Az új `components.css` fájl törölhető. Audit-trail entry-k Curator promote modjából megőrződnek.

## Kapcsolódó

- [`../DESIGN_SYSTEM.md`](../DESIGN_SYSTEM.md) §0 hibrid model
- [`../../00_DASHBOARD_INDEX.md`](../../00_DASHBOARD_INDEX.md) DS 0.7.3 audit-trail "Sprint 2b NOT EXECUTED" entry
- Sprint 2b reality check (2026-05-25): kiderült a divergencia
