<!--
  =============================================================================
  Vault Dashboards — Design System.   Version: 0.9.1
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
    0.9.1 (2026-05-29) PROMOTE: Global ESC-back navigation. When ESC is pressed
          and no overlay is open (popup or drawer) and focus is not in a text-
          entry field (INPUT / TEXTAREA / SELECT / contenteditable), ESC
          navigates back: history.back() when history.length > 1, otherwise
          falls back to the launcher (/_dashboards/index.html). Overlay-close
          always wins over navigation (priority: input-guard > popup > drawer >
          back). Integrated into the single capture-phase ESC listener in
          admin-bar.js mount(). Zero dashboard HTML touched — shared layer only.
          Canonical rule added to DS §10 keyboard shortcuts table. admin-bar.js
          0.8.21 → 0.8.22. DS version bump 0.9.0 → 0.9.1.
    0.9.0 (2026-05-28) PROMOTE: Alfred Tasks Sidebar — family-wide persistent
          sidebar. New shared helper _design/alfred-tasks.js (v1.0.0). Every
          dashboard gets a two-column shell (.app-shell / .app-main) with a
          240px sticky right sidebar listing all open tasks from Alfred's
          todos/<scope>.md files, sorted by due-state (overdue → today → soon
          → planned → none). Responsive: stacks below main at ≤900px. All 20
          dashboards updated (version-bumped + audit-trail entry). New §12 added.
          Layout change: .app (single-column max-width:1200px) replaced by
          .app-shell (flex row max-width:1440px) + .app-main (flex:1
          max-width:1200px). DS version bump 0.8.13 → 0.9.0.
    0.8.13 (2026-05-28) TEND: §10 keyboard-shortcut table fixed. While the Agent
          Quick-Nav popup is OPEN, 'A' now quick-jumps to Alfred (its initial)
          instead of re-toggling the popup — Alfred was previously the only agent
          unreachable by keyboard. Popup CLOSED: 'A' still opens it. Close is via
          Escape / backdrop / × button. Mirrors admin-bar.js 0.8.15. 0 dashboard
          HTML touched (shared layer + doc only).
    0.8.12 (2026-05-26) TEND: Calendar pill AREA·CHANNEL meta-prefix pattern added to §11
          promote-candidates. New row documents .mb-cal-pill-meta, .mb-cal-pill-area,
          .mb-cal-pill-ch, .mb-cal-pill-title CSS classes + AREA_CODES/CHANNEL_CODES JS maps
          + _pillMeta() helper. Presto-specific for now; promote when second calendar dashboard
          needs the pattern. DS version bump 0.8.11 → 0.8.12.
    0.8.11 (2026-05-25) TEND: MB Detail Drawer promote-candidates documented in §11.
          New component family from presto/index.html v0.10.0 (P3.5 UX polish):
          .mb-detail-header, .mb-detail-stage-badge (9 stage variants), .mb-detail-id-chip
          (copyable mono chip), .mb-detail-section/-label/-props, .mb-detail-disclaimer,
          .mb-detail-md (rendered markdown), .mb-detail-raw (error fallback), .mb-detail-empty,
          .mb-detail-timeline/-item/-dot/-date/-label, .mb-detail-analytics/-row/-metric/-sparkline,
          .mb-detail-actions, .mb-detail-action-btn/-secondary/-destructive, .mb-detail-tag,
          .mb-detail-collapse-toggle/-body, .mb-detail-variation/-head/-body, .mb-detail-lineage-item,
          .mb-detail-error-block, .mb-detail-loading. All Presto-specific; promote when second
          dashboard needs a rich entity detail drawer. DS version bump 0.8.10 → 0.8.11.
    0.8.10 (2026-05-25) TEND: wirePanelAnchors() behavior fix. (1) Copy formula
          changed from full URL (origin+pathname+hash) to relative path+hash
          (pathname+href only) — avoids port-dependent dead links when the
          copied value is used outside the local server. Example copied value:
          /_dashboards/presto/index.html#panel-4-campaigns. (2) Primary click
          now ONLY writes to clipboard — hash is NOT updated, scrollIntoView is
          NOT called, no navigation side-effect. (3) A11y: title and aria-label
          updated from "Click to copy panel link" to "Másolás vágólapra" to
          reflect the pure copy-only behavior. clipboard.js 1.1.0 → 1.1.1.
          §9 JS spec updated (no-scroll + relative path semantics). 0 dashboard
          HTML touched (shared layer only).
    0.8.9 (2026-05-25) PROMOTE: Panel-anchor copy behavior extracted to shared
          layer. wirePanelAnchors() moved from 8 inline dashboard definitions
          into /_design/clipboard.js (v1.1.0). New behavior vs DS 0.8.0:
          modifier-key pass-through (middle/Cmd/Ctrl/Shift+click open natively);
          a11y attributes set at wire time (aria-label="Panel link másolása",
          title="Click to copy panel link"); auto-mount on DOMContentLoaded —
          no per-dashboard call needed. Inline definitions removed from all 8
          dashboards (team, aiops, broker, sage, curator, maestro, librarian,
          presto). ~240 LOC saved. §9 JS spec updated. clipboard.js 1.0.0 →
          1.1.0. New §4b-panel sub-section added under §9.
    0.8.8 (2026-05-25) TEND: AGENT_CARDS avatar sync (admin-bar.js). Presto emoji
          corrected 🎯→🐰, Sage emoji corrected 🌿→🦉. Single source of truth for
          agent avatars is AGENT_PROFILES.md (emoji field per ## Agent section).
          §10 "AGENT_CARDS static list" updated with avatar-sync rule. admin-bar.js
          version bump 0.8.0→0.8.1. 0 dashboard HTML touched.
    0.8.7 (2026-05-25) TEND: ESC fix + letter shortcuts + .anav-kbadge badge.
          (1) ESC close bug fixed: dedicated capture-phase keydown listener now
          registered at mount() time, so ESC reliably closes the agent-nav popup
          even when the drawer has never been opened. (2) Letter quick-jump
          shortcuts: when popup is open, pressing the first letter of an agent
          name (L/M/C/P/S/B) navigates to their dashboard. Map built dynamically
          from AGENT_CARDS — first agent with a given initial wins, console.warn
          on collision. (3) .anav-kbadge: 10px JetBrains Mono badge in
          anav-name-row (between .anav-name and .anav-arrow) showing the shortcut
          letter. Styled var(--bg-sunken) bg, var(--line-soft) border, var(--ink-4)
          text, var(--radius-s) corners. Fades to 0.4 opacity on card hover.
          _agentNavKeyListener and _drawerKeyListener state vars removed (unused).
          admin-bar.js version bump 0.7.9 → 0.8.0. DS §10 updated. DS 0.8.6 →
          0.8.7 (skipping: 0.8.5 and 0.8.6 were admin-bar.js-only tends that
          updated the index version but did not bump the DS file itself).
    0.8.4 (2026-05-25) TEND: Agent Quick-Nav popup craft polish (admin-bar.js
          0.7.6 → 0.7.7). Typography ratio: anav-name 13.5px/600 vs oneliner
          10px (ratio 1.35, was 1.14). Spacing rhythm: header 14/20px, card
          18/20px, footer 11/20px (distinct zones). Emoji promoted to avatar-slot
          (.anav-avatar: 36px var(--radius-m) square, var(--bg-sunken), accent-tint
          on hover). Card structure: anav-card-meta wraps name-row + oneliner;
          .anav-arrow translateX affordance (ease-out-quart, no layout shift).
          Hover: var(--shadow-1) + var(--bg-tint). Focus ring: 2px var(--accent)
          outline-offset 3px. Open animation: scrim 120ms fade, frame
          scale(0.96→1) + opacity 200ms ease-out-quart. Footer underline on hover.
          DS version bump 0.8.3 → 0.8.4. No new tokens introduced.
    0.8.3 (2026-05-25) TEND: Agent Quick-Nav popup switched to light surface.
          Panel (.anav-frame) and cards use DS page tokens (var(--bg-elev),
          var(--bg-tint), var(--ink-1/3), var(--line/line-soft), var(--accent))
          instead of hardcoded dark-surface hex values. Scrim backdrop stays
          dark (invariant). Focus rings added (var(--accent) outline). DS §10
          visual spec updated: panel = light surface, scrim = dark backdrop.
          admin-bar.js version bump 0.7.5 → 0.7.6.
    0.8.2 (2026-05-25) TEND: Global keyboard shortcut changed from Cmd+Shift+A
          to bare A/a (modifier-free). Rationale: Cmd+Shift+A is a system-reserved
          hotkey on macOS. Dashboards currently have no text inputs, so bare A is
          safe; input-guard added to admin-bar.js for future-proofing (ignores
          keydown when focus is on INPUT/TEXTAREA/SELECT/[contenteditable]).
          §10 shortcut table updated. admin-bar.js version bump 0.7.4 → 0.7.5.
          DS version bump 0.8.1 → 0.8.2.
    0.8.1 (2026-05-25) PROMOTE: Global keyboard shortcut + Agent Quick-Nav
          popup pattern added to admin-bar.js (shared layer, 0 dashboard HTML
          touched). Cmd+Shift+A / Ctrl+Shift+A toggles a centered modal overlay
          (blur backdrop, ESC + outside-click closes). 6 agent mini-cards:
          emoji + name + 1-liner + absolute link to per-agent dashboard.
          Footer "Open full graph →" link to index.html#agents. Dark-theme
          aware, DS dark-surface tokens. AGENT_CARDS static list lives in
          admin-bar.js. .ab-agents-btn added to admin bar right zone.
          New §10 added below (keyboard shortcuts + Agent Quick-Nav pattern).
          DS version bump 0.8.0 → 0.8.1.
    0.8.0 (2026-05-25) PROMOTE: Panel Anchor System. Every scrollable panel or
          section wrapper in a dashboard now carries a deep-link anchor so the
          user can copy-paste a URL that scrolls directly to that panel.
          New §9 added below (CSS + HTML + JS canonical spec).
          Family-wide rollout: all dashboards with multi-panel layout updated.
          Dashboards that are single-surface or tab-navigated (personal-growth)
          are exempt — they use tab state for navigation instead.
    0.7.3 (2026-05-25) Sprint 4+5 — convention alignment + template baseline.
          Sprint 4: plugins.html outlier eliminated (.wrap → .app, 1240 →
          1200px, removed double body padding). v0.1.7. Other "planned drifts"
          (.chip vs .chip-copyable, --info/--contact tokens) were false alarms
          (already separated) or out-of-scope (domain tokens, Curator decision).
          Sprint 5: three new shared libs added (NO mass migration of existing
          dashboards — Sprint 2b/3 lesson re: risk-vs-reward for tiny helpers):
            • _design/dom-utils.js  → escapeHtml + toSlug (3-line canonical
              versions extracted from the 5/7-file clusters)
            • _design/agent-logs.js → AgentLogs.fetch + filterByAgent +
              filterByLevel + formatTimestamp/Absolute (schema-v2 aware)
            • _design/_template/index.html → "hello world" dashboard scaffold
              that uses ALL shared libs (tokens.css, theme.js, clipboard.js,
              live-updates.js, admin-bar.js, markdown-parser.js, dom-utils.js,
              optional agent-logs.js). 100% lint-green baseline. The
              canonical starting point for every new dashboard from now on.
            • _design/_template/ONBOARDING.md → 9-step build guide
          New dashboards MUST start from _template/ (NOT copy from sales/agents
          /any other complex dashboard). Existing dashboards continue with
          their inline equivalents unchanged.

    0.7.2 (2026-05-25) Sprint 3 — parseYamlFrontmatter engine extraction.
          New _design/markdown-parser.js exposes window.parseYamlFrontmatter
          (canonical 87-line implementation: nested objects, indent-based
          stack, quote-aware comment stripping, scalar coercion to int/float/
          bool/null, inline + block arrays).
          Hash-audit-gated rollout: only the 3 dashboards whose inline parser
          normalized-hash matched the canonical (41edbbd902e5) were migrated:
            • partnerships.html  v0.2.6 → v0.2.7
            • team.html          v0.1.7 → v0.1.8
            • navigator.html     v0.1.7 → v0.1.8
          Saved ~260 LOC. The other 6 dashboards with inline parsers were
          SKIPPED with reasons:
            • sales.html (hash 1f1861cebd1d, 124 LOC) — extended for nested
              lead structures
            • aiops.html (hash d6249b7a1875, 88 LOC) — variant
            • broker/index.html, librarian/index.html (hash 41c36beb495e,
              29-33 LOC) — compact with hex-preserving comment stripping
            • presto/index.html (hash bfc697f4c043, 35 LOC) — block scalar
              support
            • sage/index.html (hash aeabaf0877d6, 14 LOC) — modular stub
              delegating to parseYamlBlock
          These 6 are REASSIGNED to Curator /dash-promote backlog: a curator-
          led behavioral alignment pass (which features are canonical?
          which dashboards need block scalars? hex-preserving comments?)
          must precede engine extraction. Until then they keep their inline
          parsers (lint passes since they ARE defined inline).

    0.7.1 (2026-05-25) Sprint 2a — CSS tokens engine extraction. New
          _design/tokens.css contains the canonical DS §1 (light :root), §1a
          (dark override), and §1a (prefers-color-scheme fallback) blocks.
          Family-wide rollout: 16/16 dashboards patched, ~1,000 LOC removed.
          Per-file behavior depends on what they had: 5 dashboards
          (curator, librarian, partnerships, plugins, scheduler) had ONLY
          canonical tokens → whole :root/dark/@media blocks dropped; 11 had
          a mix of canonical + domain-specific tokens (sales --hot/--warm/
          --cold/--contact/--discovery/--proposal/--won/--lost, team --info,
          navigator pipeline tokens, index --sonrisa/--exar etc.) → those
          custom tokens PRESERVED, only canonical lines removed. Hybrid
          model status (§0) flipped for tokens: NEW DASHBOARDS MUST
          <link rel="stylesheet" href="/_dashboards/_design/tokens.css">,
          NOT copy DS §1 inline. The DS §1 / §1a code blocks below are now
          DOCUMENTATION (reference for what tokens.css contains); they are
          no longer the "copy verbatim into your dashboard" instruction.

    Sprint 2b NOT EXECUTED — investigation finding (2026-05-25): the
          per-dashboard component CSS (.theme-toggle, .home-link, .masthead,
          .version-pill, .card-copy-ref) is NOT in fact 100% identical
          across the family (the original 2026-05-22 audit overcounted
          uniformity). broker uses compact one-line format with distinct
          font-size/padding/margin; sales has extra text-decoration; etc.
          Mechanical extraction would either silently break intentional
          variations or net only fractional savings. Components.css is
          REASSIGNED to Curator /dash-promote workflow: a curator-led
          alignment pass to equalize variants FIRST (DS decision: which
          variant is canonical?), THEN engine-extract. Estimated work:
          1 promote cycle per component family.

    0.7.0 (2026-05-25) ENGINE EXTRACTION milestone (Sprint 0 + Sprint 1 of the
          dashboard refactor plan). Five new files in _design/:
            • CLAUDE.md (auto-loaded discovery layer, _dashboards/ root)
            • _design/ARCHITECTURE.md (normative spec — 5 invariants, 5
              component layers, naming, anti-patterns, promote workflow)
            • _design/_template/checklist.md (~80 pre-commit checks, §A-§N)
            • _design/lint.mjs (21 rules, 3 severities, --strict / --json /
              --quiet flags; 0-dep Node)
            • _design/theme.js + _design/clipboard.js (Sprint 1 — extracted
              from DS §1c and §4a inline blocks duplicated across all 16
              dashboards; classic <script src=> pattern, parity with
              admin-bar.js / live-updates.js)
          Family-wide rollout: 11 version-pill mismatches fixed (Sprint 0
          drift cleanup); 16/16 dashboards bumped patch + audit-trail line
          (Sprint 1 engine import). Saved ~600 LOC of duplicated theme +
          clipboard boilerplate. Lint: 0 error across family. The hybrid
          model (§0) status flipped for theme + clipboard: these ARE NOW
          engine-extracted; new dashboards MUST import via <script src=>,
          NOT copy inline. Token CSS (§1) remains hybrid pending Sprint 2.
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
    0.6.0 (2026-05-25) PROMOTE: Admin Bar replaces ops-header strip. New shared
          helper _design/admin-bar.js. WordPress-style fixed dark top bar (34px,
          #1d2327, always dark). Left: BDOS logo+breadcrumb. Center: 5 compact
          status pills with tooltip. Right: System drawer button. Body receives
          padding-top:34px compensation. Backward-compat: mounts into
          #bdos-admin-bar OR legacy #bdos-ops-header. window.OpsHeader aliased
          to window.AdminBar. §5b deprecated (preserved). §5c added.
          Family-wide rollout: all 16 dashboards bumped. index.html Task 1 fix
          included (missing ops-header tags added).
    0.6.1 (2026-05-25) RULE: Canonical sidecar JSON field name for agent identity
          is `agent_name` (not `agent`). All per-agent logs filter expressions
          MUST use `e.agent_name === LOGS_AGENT`. The `agent` field name was the
          old schema; `agent_name` is the correct column in `agent_logs` table
          (schema v1.2+) and in the sidecar JSON export. Bug fix rolled out to
          all 6 per-agent dashboards (librarian, curator, sage, presto, broker,
          maestro) — promote rollout 2026-05-25.
    0.6.3 (2026-05-25) MANDATORY BUILD RULE: DS §4a Card copy-ref is now
          MANDATORY at build time, not optional tend. Every new dashboard MUST
          include DASH_STEM const, .card-copy-ref CSS block, copyText +
          wireCopyRef JS helpers, and data-card-id + copy-ref button on every
          bounded card-like element — ALL as part of the initial build, before
          first commit. Family-wide audit rollout: librarian 0.5.4→0.5.5,
          curator 0.5.3→0.5.4, broker 0.5.3→0.5.4, scheduler 0.1.3→0.1.4.
    0.6.2 (2026-05-25) RULE: Sidecar JSON schema v2 — agent_logs.json now exports
          `scheduled_jobs` array (full scheduled_jobs table rows) in addition to
          `events`. schema_version field: "1.2" → "2". Scheduler dashboard Jobs
          tab reads sidecar.scheduled_jobs directly (schema v2 path); backward-
          compat fallback to event-tag logic when schema < 2 or array missing.
          Scope: agent_log.py + scheduler/index.html 0.1.2→0.1.3.
  =============================================================================
-->
---
title: Vault Dashboards Design System
version: 0.9.1
date: 2026-05-29
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

> **MANDATORY at build time — not optional tend. Every new dashboard MUST include this from v0.1.0.** Add `DASH_STEM` const, `.card-copy-ref` CSS block, `copyText` + `wireCopyRef` JS helpers, and `data-card-id` + copy-ref button on every bounded card-like element as part of the initial scaffold — before first commit. NO EXCEPTIONS.

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

## 5b. Ops Header Strip (DS 0.5.0) — DEPRECATED as of DS 0.6.0

> **Deprecated.** Replaced by `§5c Admin Bar` (DS 0.6.0). Existing dashboards
> migrated to `admin-bar.js` during the 2026-05-25 promote rollout.
> `ops-header.js` is preserved for reference and backward compat — `admin-bar.js`
> accepts `#bdos-ops-header` as a mount target and exposes `window.OpsHeader`
> as an alias. Do NOT add `ops-header.js` to new dashboards; use `admin-bar.js`.

The (now legacy) system-status strip rendered **above every dashboard masthead**.
Implemented as shared helper `_design/ops-header.js` (auto-mounts on load).

### Legacy usage (DO NOT use in new dashboards — see §5c)

```html
<!-- In <body>, first element: -->
<div id="bdos-ops-header"></div>

<!-- Before </body>, after live-updates.js: -->
<!-- ops-header.js (DS 0.5.0) — DEPRECATED, use admin-bar.js -->
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

## 5c. Admin Bar (DS 0.6.0) — CANONICAL — replaces §5b

WordPress-style **fixed dark top bar** rendered at the very top of every
dashboard, above all page content. 34 px tall. **Always dark** — ignores
the page dash-theme (`data-theme` attribute). This is the canonical
system-status component from DS 0.6.0 onward.

### Visual design

| Zone | Content |
|---|---|
| Left | BDOS wordmark (layers icon + "BDOS") · current-page breadcrumb (if not root) |
| Center | Five compact status pills (hover tooltip shows detail text) |
| Right | "System ⚙" button → opens `scheduler/index.html` drawer |

**Colors (own dark-surface scope — not inherited from :root):**

| Token | Value | Usage |
|---|---|---|
| Bar background | `#1d2327` | fixed bar surface |
| Bar text muted | `#a7aaad` | labels, System button |
| Bar text strong | `#c3c4c7` | BDOS wordmark, breadcrumb current |
| Bar accent | `#e8a87c` | logo hover, system-btn hover |
| Pill ok | `rgba(87,167,115,.18)` bg · `#88d9a7` text | Watchdog/Server/DB ok |
| Pill warn | `rgba(200,155,46,.18)` bg · `#f2c96e` text | stale / unhealthy |
| Pill gap | `rgba(217,83,79,.18)` bg · `#f08a86` text | offline / error |
| Pill idle | `rgba(255,255,255,.06)` bg · `#6c7075` text | initial state |

### Usage (two lines per dashboard)

```html
<!-- In <body>, first element — replaces legacy #bdos-ops-header: -->
<div id="bdos-admin-bar"></div>

<!-- Before </body>, after live-updates.js — replaces ops-header.js: -->
<!-- admin-bar.js (DS 0.6.0) -->
<script src="/_dashboards/_design/admin-bar.js"></script>
```

`admin-bar.js` auto-mounts on `DOMContentLoaded`. It also sets
`document.body.style.paddingTop = "34px"` automatically to prevent the
fixed bar from obscuring masthead content.

**Backward compat:** `admin-bar.js` mounts into `#bdos-admin-bar` OR the
legacy `#bdos-ops-header` (normalizes to the new id). `window.OpsHeader`
is aliased to `window.AdminBar` — no callers need updating.

### Component selectors

```css
#bdos-admin-bar          /* bar root — position:fixed, 34px, #1d2327 */
.ab-left                 /* left zone: logo + breadcrumb */
.ab-logo                 /* BDOS wordmark link */
.ab-breadcrumb           /* breadcrumb nav (hidden on root launcher) */
.ab-bc-current           /* current page name */
.ab-center               /* center zone: pill row */
.ab-pill                 /* individual status pill */
.ab-pill-dot             /* 5px status dot inside pill */
.ab-pill-label           /* text label (hidden on narrow screens) */
.ab-right                /* right zone: system button */
.ab-system-btn           /* System ⚙ button */
```

### Five status pills (checked every 30 s, same logic as ops-header.js)

| Pill | Label | Check |
|---|---|---|
| Watchdog | Watchdog | `events_server.py` `/health` (port 4322) |
| Server | Server | `dash-server.mjs` HEAD / (port 4321) |
| DB | DB | `agent_logs.json` freshness + row count |
| Scheduler | Sched | last `agent_logs` row tagged `scheduler` within 5 min |
| Index | Index | `agent_logs.json` `generated_at` within 24 h |

### Public API

```js
AdminBar.mount()       // auto-called on DOMContentLoaded
AdminBar.refresh()     // force immediate re-check of all pills
AdminBar.openDrawer()  // open system status drawer
AdminBar.closeDrawer() // close drawer (Escape + backdrop also work)

// Backward-compat alias (window.OpsHeader === window.AdminBar):
OpsHeader.mount()
OpsHeader.refresh()
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

## 7. Sidecar JSON field name convention (DS 0.6.1)

The canonical agent identity field in `agent_logs` (SQLite, schema v1.2+) and in
the sidecar export `_design/agent_logs.json` is **`agent_name`** — not `agent`.

Rule: every per-agent dashboard that filters the sidecar by agent MUST use:

```js
const agentEvents = events.filter(e => e.agent_name === LOGS_AGENT);
```

Never use `e.agent === LOGS_AGENT` — that field does not exist in the sidecar export
and will silently produce an empty result. The `audit` mode checks this; `promote`
uses this as the rollout guard when a new per-agent dashboard is built.

Note: Maestro's global logcat uses a multi-source fallback chain
(`e.agent_name || e._agent || '?'`) to support both the sidecar JSON and
legacy markdown YAML log blocks parsed at runtime — this is intentional and
correct; do not simplify it to a single field.

## 8. Ismert kivétel

*(Korábban: `plugins.html` dark-theme outlier — 2026-05-22 promote 0.3.0 keretében a kanonikus tokenekre migrálva, kivétel-státusz megszűnt.)*

---

## 9. Panel Anchor System (DS 0.8.0)

Every scrollable panel or section wrapper in a multi-panel dashboard carries a
**deep-link anchor** so the user can hover to see a `#N` badge, click it to copy
the full URL (including the hash), and share or paste it back to navigate directly
to that panel. This is the "every panel is linkable" invariant.

### When to apply

Apply to every persistent top-level panel/section element in a dashboard. Exempt:
- Single-surface dashboards with no distinct panel sections (e.g., `agents.html` — one grid)
- Tab-navigated dashboards where the tab IS the navigation (`personal-growth/index.html`)
- The `<div class="widget-strip" id="panel-1-header-strip">` header stat row — anchored by ID but not given `.panel-anchor-host` (no header element to attach the badge to)

### ID naming convention

```
id="panel-N-<slug>"
```

- `N` = 1-based integer (1 = header strip / masthead area, 2 = first content panel, etc.)
- `<slug>` = lowercase, hyphen-separated, descriptive name (e.g., `agent-overview`, `dashboard-family`, `logs`)
- The widget-strip / stat row at the top gets `id="panel-1-header-strip"` (no anchor badge — no heading to attach to)

### CSS

```css
/* ===== Panel Anchor System (DS 0.8.0) ===== */
/* scroll-margin-top clears the fixed 34px admin bar + 8px breathing room */
[id^="panel-"] { scroll-margin-top: 42px; }
.panel-anchor {
  font-family: 'JetBrains Mono', monospace;
  font-size: 10px; font-weight: 600;
  color: var(--ink-5);
  background: transparent;
  border: none;
  padding: 1px 4px;
  border-radius: var(--radius-s);
  text-decoration: none;
  opacity: 0;
  transition: opacity var(--t-fast), color var(--t-fast), background var(--t-fast);
  white-space: nowrap;
  cursor: pointer;
  line-height: 1;
  flex-shrink: 0;
}
.panel-anchor-host:hover .panel-anchor,
.panel-anchor-host:focus-within .panel-anchor { opacity: 1; }
.panel-anchor:hover { color: var(--accent-deep); background: var(--accent-tint); }
/* Section-head variant: anchor sits at the end of the flex row */
.section-head .panel-anchor { align-self: center; margin-left: 2px; }
/* Panel-head variant: anchor sits after the title text */
.panel-head .panel-anchor { margin-left: 2px; }
```

### HTML: markup pattern

Add `panel-anchor-host` class to the panel/section wrapper, and place the anchor `<a>` inside the panel heading flex row:

```html
<!-- Panel wrapper: add panel-anchor-host class + id="panel-N-slug" -->
<div class="panel panel-anchor-host" id="panel-2-my-panel">
  <div class="panel-head">
    Panel Title
    <a class="panel-anchor" href="#panel-2-my-panel" title="Link to this panel">#2</a>
  </div>
  <!-- panel content -->
</div>
```

For `<section>` wrappers with a `.section-header` or `.section-head` div:

```html
<section class="section panel-anchor-host" id="panel-3-overview">
  <div class="section-head">
    <h2>Section Title</h2>
    <a class="panel-anchor" href="#panel-3-overview" title="Link to this panel">#3</a>
  </div>
</section>
```

### JS: `wirePanelAnchors()` — shared layer (DS 0.8.10)

> **Engine-extracted as of DS 0.8.9.** The canonical implementation lives in
> `/_design/clipboard.js` (v1.1.1). **Do NOT define `wirePanelAnchors()` inline
> in dashboard HTML** — it auto-mounts on `DOMContentLoaded` when `clipboard.js`
> is loaded. No per-dashboard boot call required.

**Behavior (DS 0.8.10, supersedes DS 0.8.9):**
- Primary click (no modifier): copies the **relative path + hash** (`location.pathname + anchor.href`) to the clipboard — **no origin, no hash update, no scroll**. Example: `/_dashboards/presto/index.html#panel-4-campaigns`. Shows `✓` for 1.5 s then restores `#N`.
- Middle-click / Cmd+click / Ctrl+click / Shift+click: pass through — browser handles natively (open in new tab / window).
- A11y: `aria-label="Másolás vágólapra"` and `title="Másolás vágólapra"` set at wire time.
- Textarea fallback: used when `navigator.clipboard` is unavailable.

**Rationale for no-scroll / no-hash-update:** the anchor is a pure copy affordance, not a navigation element. Updating the hash caused the page to jump to the top or to the target panel unexpectedly. The relative path (no origin) ensures the copied link works across localhost ports and other deployment contexts.

**Integration (zero per-dashboard code):**

```html
<!-- clipboard.js already required by DS §4a — panel anchors get wired automatically -->
<script src="/_dashboards/_design/clipboard.js"></script>
```

No boot call. No inline function. `window.wirePanelAnchors` is exposed as a global
if manual re-wiring is ever needed (e.g., after dynamically inserting new panel markup).

**Reference implementation:** `/_design/clipboard.js` lines ~100–165 (v1.1.1).

### Boot call (removed as of DS 0.8.9)

~~`wirePanelAnchors();` in the dashboard boot section~~ — no longer needed.
Remove any existing inline definition and boot call when next touching a dashboard.

---

## 10. Global Keyboard Shortcuts + Agent Quick-Nav Popup Pattern (DS 0.8.7)

This pattern is implemented entirely in `_design/admin-bar.js` — **zero dashboard
HTML changes required**. Every dashboard that loads `admin-bar.js` automatically
gets the shortcut and popup.

### Keyboard shortcuts

| Shortcut | Condition | Action |
|---|---|---|
| `A` (bare, no modifier) | Popup **closed**, focus NOT in text field | Open Agent Quick-Nav popup |
| `Escape` | Popup or drawer **open** | Close overlay (popup wins over drawer) |
| `Escape` | Nothing open, focus NOT in text field | Navigate back: `history.back()` or launcher fallback |
| `Escape` | Focus in INPUT / TEXTAREA / SELECT / contenteditable | Native browser action (blur/clear field) — no navigation |
| `A`, `L`, `M`, `C`, `P`, `S`, `B`, `F`, … | Popup **open** | Quick-jump to that agent's dashboard (`A` → Alfred) |

> **DS 0.9.1 (2026-05-29):** ESC-back navigation added. When no overlay is open
> and focus is not in a text-entry field, ESC navigates to the previous history
> entry (`history.back()`). Falls back to `/_dashboards/index.html` (the launcher)
> when `history.length <= 1` (directly-opened tab). Overlay-close still wins:
> popup ESC, then drawer ESC, then navigate. Input guard: ESC inside INPUT /
> TEXTAREA / SELECT / contenteditable does its normal browser thing — never
> navigates.

> **DS 0.8.15 (2026-05-28):** while the popup is open, `A` quick-jumps to **Alfred**
> (its initial) instead of re-toggling. Previously `A` toggled unconditionally, so
> Alfred — the only A-initial agent — was unreachable by keyboard. Close the open
> popup with `Escape`, backdrop click, or the `×` button.

All shortcuts share the same **input guard**: silently ignored when
`document.activeElement` is an `INPUT`, `TEXTAREA`, `SELECT`, or any element
with `isContentEditable === true`.

**ESC implementation (DS 0.8.5 fix, extended DS 0.9.1):** a dedicated `capture: true`
keydown listener is registered at `mount()` time. It fires before all bubble-phase
listeners. Priority chain: (1) input guard — return immediately if focus is in a
text field; (2) if popup open, close popup + `stopPropagation`; (3) if drawer open,
close drawer + `stopPropagation`; (4) navigate back. This ensures ESC always works
regardless of whether the drawer was ever opened, and the input guard ensures text
fields retain their normal ESC behaviour.

**Letter quick-jump (DS 0.8.5):** the `_agentLetterMap` is built dynamically from
`AGENT_CARDS[i].name[0].toLowerCase()` at mount time. First agent with a given initial
wins; if two share an initial, `console.warn` is emitted and the first registration
stands. Navigation uses `window.location.href` (same-tab), mirroring the default
`<a href>` card behavior.

The two listeners registered in `mount()`:
1. Capture-phase ESC handler (`{ capture: true }`)
2. Bubble-phase A/letter handler (no modifier, input-guarded)

### Agent Quick-Nav popup

A centered modal overlay that lists all 6 BDOS agents as mini-cards.

**Visual spec (DS 0.8.4):**
- Scrim (backdrop): `rgba(20,20,19,.55)` bg + `backdrop-filter: blur(4px)` — always dark (invariant)
- Panel (`.anav-frame`): **light surface** — `var(--bg-elev)` background, `var(--line)` border, `border-radius: var(--radius-xl)` (14px), `width: min(96vw, 680px)`. Uses DS page tokens.
- **Open animation:** scrim `opacity 0→1` over 120ms ease-out-quart; frame `scale(0.96)→scale(1) + opacity 0→1` over 200ms ease-out-quart. No layout-property animation.
- Header padding: `14px 20px 12px`; `var(--line)` divider (stronger than card separators).
- Grid: `3 × 2` card grid, gap 0. Card padding `18px 20px 16px`.
- **Card anatomy:** `.anav-avatar` (36px `var(--radius-m)` square, `var(--bg-sunken)`, emoji 18px) + `.anav-card-meta` (`.anav-name-row` row: name + `.anav-kbadge` + arrow, + `.anav-oneliner` below).
- **Letter badge (`.anav-kbadge`):** 10px JetBrains Mono, `var(--bg-sunken)` bg, `var(--line-soft)` border, `var(--ink-4)` text, `var(--radius-s)` corners, `1px 5px` padding. Sits between `.anav-name` and `.anav-arrow` in the name-row flex. Fades to `opacity: 0.4` on card hover (arrow takes visual focus). `aria-hidden="true"` — decorative affordance only.
- **Typography ratio:** name 13.5px/600/`letter-spacing: -0.01em` vs oneliner 10px = 1.35 ratio (min 1.25 law).
- **Card hover:** `var(--bg-tint)` + `var(--shadow-1)` micro-elevation; avatar gets `var(--accent-tint)` bg.
- **Arrow affordance:** `.anav-arrow` `→`, `opacity 0 + translateX(-4px)` at rest; `opacity 1 + translateX(0) + var(--accent)` on hover. Transform only — no layout shift.
- **Focus ring:** `outline: 2px solid var(--accent); outline-offset: 3px`
- Text: `var(--ink-1)` name, `var(--ink-3)` one-liner, `var(--ink-2)` title
- Borders: `var(--line-soft)` card separators, `var(--line)` header/footer dividers
- Footer padding: `11px 20px 12px`; `"Open full graph →"` link in `var(--accent)`, underline on hover.
- **Invariant:** scrim is ALWAYS dark; panel surface follows DS page tokens (light by default).

**DOM IDs:**
- `#bdos-agent-nav` — overlay root
- `#bdos-agent-nav-grid` — card grid
- `#bdos-agent-nav-close` — close button

**Interaction rules:**
- Outside-click (on backdrop) closes the popup
- `Escape` key closes the popup (shared with system drawer close)
- Clicking a card link navigates directly (no `e.preventDefault`)
- "Open full graph →" navigates to `/_dashboards/index.html#agents`

### AGENT_CARDS static list

Lives in `admin-bar.js`. Each entry:

```js
{
  emoji:    '📚',          // visual identifier — MUST match AGENT_PROFILES.md
  name:     'Librarian',  // display name
  oneliner: '…',          // 1-sentence description (≤ 60 chars)
  url:      '/_dashboards/librarian/index.html',  // absolute path
}
```

**Maintenance rule:** when a new per-agent dashboard is built (`build` mode),
add the corresponding entry to `AGENT_CARDS` in `admin-bar.js`. Absolute paths
(`/_dashboards/…`) work correctly at any dashboard nesting depth.

**Avatar-sync rule (DS 0.8.8):** the `emoji` field in every `AGENT_CARDS` entry
MUST match the `avatar.emoji` in the corresponding `## <Agent>` section of
`/00_Prompts/BDOS/AGENT_PROFILES.md`. That file is the **single source of truth**
for all agent visual identity (emoji + color). Never invent an emoji for admin-bar.js
from memory — always read AGENT_PROFILES.md first. If they drift, `tend` admin-bar.js
to realign. Canonical values (DS 0.8.8):

| Agent | Canonical emoji |
|---|---|
| Librarian | 📚 |
| Maestro | 🎼 |
| Curator | 🖼️ |
| Presto | 🐰 |
| Sage | 🦉 |
| Broker | 🤝 |

### Public API additions (DS 0.8.1)

```js
AdminBar.openAgentNav()    // open the popup
AdminBar.closeAgentNav()   // close the popup
AdminBar.toggleAgentNav()  // toggle (used by keyboard shortcut + button click)
```

### Component selectors

```css
.ab-agents-btn               /* "Agents" button in admin bar right zone */
#bdos-agent-nav              /* overlay root — position:fixed, z-index:9300 */
#bdos-agent-nav .anav-frame       /* modal frame */
#bdos-agent-nav .anav-header      /* header row: left group + close */
#bdos-agent-nav .anav-header-left /* title + shortcut badge group */
#bdos-agent-nav .anav-title       /* "BDOS Agent Family" eyebrow label */
#bdos-agent-nav .anav-shortcut    /* "A" monospace badge */
#bdos-agent-nav .anav-close       /* close button */
#bdos-agent-nav .anav-grid        /* 3-column card grid */
#bdos-agent-nav .anav-card        /* individual agent mini-card (link) */
#bdos-agent-nav .anav-card-top    /* avatar + meta row */
#bdos-agent-nav .anav-avatar      /* 36px rounded square emoji container */
#bdos-agent-nav .anav-card-meta   /* name-row + oneliner wrapper */
#bdos-agent-nav .anav-name-row    /* name + arrow flex row */
#bdos-agent-nav .anav-name        /* agent name, 13.5px 600 */
#bdos-agent-nav .anav-kbadge      /* letter shortcut badge, 10px mono, fades on hover */
#bdos-agent-nav .anav-arrow       /* "→" affordance, translateX on hover */
#bdos-agent-nav .anav-oneliner    /* 1-liner description, 10px muted */
#bdos-agent-nav .anav-footer      /* footer with full-graph link */
#bdos-agent-nav .anav-full-link   /* "Open full graph →" terracotta link */
```

---

## 11. Promote Candidates (not yet promoted — Presto-specific as of 2026-05-25)

The following patterns were introduced in `presto/index.html` v0.9.0 as part of the Marketing Board panel (P3). They are **Presto-specific** for now. If a second dashboard needs kanban or calendar views, run `/dash-promote` to codify them family-wide.

| Pattern | CSS classes | Presto location | Promote trigger |
|---|---|---|---|
| **Kanban lane** | `.mb-panel`, `.mb-kanban`, `.mb-lane`, `.mb-lane-header`, `.mb-cards`, `.mb-card`, `.mb-age-badge` | `presto/index.html` §Marketing Board | Second dashboard needs a 6-lane kanban |
| **Calendar grid** | `.mb-cal-grid`, `.mb-cal-cell`, `.mb-cal-pill`, `.mb-cal-day-header`, `.mb-cal-controls` | `presto/index.html` §Marketing Board Calendar | Second dashboard needs a week/month/day calendar |
| **Calendar pill 3-tier (P1 confidence chain)** | `.mb-cal-pill-locked` (solid fill, wt 600), `.mb-cal-pill-approved` (8% tint + 2px solid border, wt 500), `.mb-cal-pill-plan` (transparent + 1px dashed `--line` + leading dot `::before` + italic, wt 400) — channel color exposed as `--ch-color` CSS custom prop | `presto/index.html` v0.16.0 §Calendar pill tiers | Second dashboard needs a calendar with 3-tier confidence visualization |
| **Calendar pill AREA·CHANNEL meta-prefix** | `.mb-cal-pill-meta` (inline-flex, ui-monospace 8.5px 700, flex-shrink:0, font-style:normal overrides tier italic), `.mb-cal-pill-area` (opacity 0.55 — subordinate), `.mb-cal-pill-ch` (opacity 1 — primary disambiguator), `.mb-cal-pill-title` (flex:1, overflow ellipsis); `AREA_CODES` + `CHANNEL_CODES` JS maps + `_pillMeta(p)` helper; title attribute on each span for hover tooltip; color inherited per tier (#fff / ink-1 / ink-3) | `presto/index.html` v0.16.0 §calPillsForDate | Second calendar dashboard needs AREA·CHANNEL pill prefix |
| **Next-action box** | `.mb-next-action`, `.mb-next-cmd`, `.mb-next-reason` | `presto/index.html` §Marketing Board | Family-wide "recommended next step" pattern |
| **Entity detail drawer** | `.mb-detail-header`, `.mb-detail-stage-badge` (9 variants), `.mb-detail-id-chip`, `.mb-detail-section`, `.mb-detail-section-label`, `.mb-detail-props`, `.mb-detail-disclaimer`, `.mb-detail-md`, `.mb-detail-raw`, `.mb-detail-empty`, `.mb-detail-timeline`, `.mb-detail-timeline-item`, `.mb-detail-timeline-dot`, `.mb-detail-analytics`, `.mb-detail-analytics-row`, `.mb-detail-analytics-metric`, `.mb-detail-sparkline`, `.mb-detail-actions`, `.mb-detail-action-btn`, `.mb-detail-action-secondary`, `.mb-detail-action-destructive`, `.mb-detail-tag`, `.mb-detail-collapse-toggle`, `.mb-detail-collapse-body`, `.mb-detail-variation`, `.mb-detail-lineage-item`, `.mb-detail-error-block`, `.mb-detail-loading` | `presto/index.html` §MB Detail Drawer (v0.10.0) | Second dashboard needs a rich right-side entity detail drawer with SEED/PUBLICATION duality, sticky action footer, fetch-from-file, cache, analytics sparkline |

**DS version at time of noting (kanban/cal/next-action):** 0.8.8. **MB Detail Drawer noted:** 0.8.11. Run `promote` when ready to canonicalize.

---

## 12. Alfred Tasks Sidebar (DS 0.9.0)

A **persistent right-side column** that is always visible on every dashboard in
the family, listing all open tasks from Alfred's `todos/<scope>.md` files. The
user can see their cross-scope task list alongside any dashboard's own content
without switching tabs.

### Architecture

- **Shared helper:** `/_dashboards/_design/alfred-tasks.js` (v1.0.0).
  Auto-mounts on `DOMContentLoaded` when `#alfred-tasks-sidebar` is present.
- **Data sources:** `parseTasks` + `dueState` logic identical to
  `alfred/index.html` (extracted verbatim). Fetches the same six scope files:
  `personal.md`, `family.md`, `cps.md`, `navigator.md`, `exarlabs.md`,
  `fokuszpont.md` from `/02_Areas/Personal Growth/Alfred/todos/`.
- **Refresh:** 30 s poll; listens for `alfred-tasks:refresh` CustomEvent if
  dispatched by `live-updates.js` for tighter SSE-driven updates.
- **Sorting:** overdue → today → soon → planned → none.

### Layout shell

Every dashboard replaces the outer `.app` single-column wrapper with a two-
element flex shell:

```html
<!-- Replace the outer <main class="app"> with: -->
<div class="app-shell">
  <main class="app-main">
    <!-- existing dashboard content unchanged -->
  </main>
  <aside id="alfred-tasks-sidebar"></aside>
</div>
```

**CSS (injected by alfred-tasks.js — do NOT copy into dashboard `<style>`):**

```css
/* .app-shell / .app-main / #alfred-tasks-sidebar are injected by alfred-tasks.js */
/* Dashboards that previously used  .app  now use  .app-main  for their own CSS rules.   */
/* The outer max-width guard changes: .app (1200px) → .app-shell (1440px) + .app-main (1200px). */
```

**Responsive breakpoint (≤ 900 px):** sidebar stacks below the main content
column — `flex-direction: column`, sidebar `position: static`, `width: 100%`.
No JS toggle needed. At 900–1200 px the sidebar is 240 px wide on the right.

### Per-dashboard migration (mandatory with this promote)

1. In each dashboard's `<style>` block, rename every `.app {` selector to
   `.app-main {` (the class name changes; the rules stay identical).
2. In the HTML, rename `<main class="app">` (or `<div class="app">`) to
   `<main class="app-main">`, and wrap it plus a new `<aside>` in
   `<div class="app-shell">…</div>`.
3. Add `<script src="/_dashboards/_design/alfred-tasks.js"></script>` before
   `</body>` (after all other shared scripts).
4. Bump version + add audit-trail line: "promoted: Alfred Tasks Sidebar DS 0.9.0".

### Component selectors

```css
.app-shell              /* outer flex row — max-width: 1440px, margin: 0 auto */
.app-main               /* main content column — flex:1, max-width: 1200px */
#alfred-tasks-sidebar   /* sidebar — width: 240px, sticky top: 50px */
.ats-header             /* sidebar header row: title + count badge + Alfred link */
.ats-title              /* "Feladatok" label */
.ats-count              /* open-task count badge (mono pill) */
.ats-link               /* "Alfred →" link to alfred/index.html */
.ats-body               /* scrollable task list */
.ats-row                /* individual task row (position:relative, card-copy-ref inside) */
.ats-row-body           /* flex-col inner: scope-badge + text + chips */
.ats-scope-badge        /* 9px uppercase scope label (Személyes / CPS / …) */
.ats-text               /* task text, 12px */
.ats-chips              /* due + prio chip row */
.ats-due                /* due-date chip */
.ats-due--overdue       /* red — past due */
.ats-due--today         /* accent/terracotta — due today */
.ats-due--soon          /* alfred slate-blue — due within 7 days */
.ats-prio               /* priority indicator chip */
.ats-prio--high         /* red */
.ats-prio--med          /* alfred blue */
.ats-prio--low          /* muted grey */
.ats-empty              /* "no tasks" empty state */
```

### Public API

```js
AlfredTasks.refresh()       // force immediate re-fetch + re-render
AlfredTasks.startPolling()  // start 30s interval
AlfredTasks.stopPolling()   // stop interval
AlfredTasks.mount()         // inject styles + first fetch + start polling (auto on DOMContentLoaded)
```

### Alfred dashboard special case

`alfred/index.html` already has its own full Tasks panel (panel 02) with
per-scope grouping and archive counts. The sidebar is intentionally also
present on Alfred's own dashboard for family consistency — it shows the
compact cross-scope view, while the full panel 02 shows per-scope detail.
No duplication concern: the sidebar reads the same files but presents a
flat sorted list (useful at a glance), while panel 02 shows structure.

### Do NOT

- Define `.app-shell`, `.app-main`, or `#alfred-tasks-sidebar` styles in
  individual dashboard `<style>` blocks — they are injected by `alfred-tasks.js`.
- Hardcode task data in the sidebar — it always fetches from the markdown sources.
- Apply custom width, background or border overrides to `#alfred-tasks-sidebar`
  per-dashboard — family visual language must stay consistent.

---

**Hivatkozott:** capability doc `00_Prompts/BDOS/capabilities/vault-dashboards/CLAUDE.md` · format contract `02_Areas/Sonrisa/CPS/Sales/DASHBOARD_CONTRACT.md` · Curator agent `00_Prompts/BDOS/agents/curator.md`
