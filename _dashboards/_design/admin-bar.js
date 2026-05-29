/**
 * admin-bar.js — BDOS Admin Bar  (DS 0.8.21, 2026-05-29)
 * =======================================================
 * 0.8.21 (2026-05-29) checkScheduler() rewired: instead of scanning events[]
 *        for 'scheduler'-tagged rows (those rows are being stripped from the
 *        observability DB), liveness is now derived from scheduled_jobs[].
 *        Takes the most recent last_run_at among enabled jobs; applies the
 *        same SCHEDULER_STALE_MS threshold. Graceful fallback to idle/unknown
 *        when scheduled_jobs is absent or empty.
 * 0.8.20 (2026-05-29) "System" button now navigates to the new architecture
 *        dashboard (/_dashboards/system.html) instead of opening the scheduler
 *        drawer iframe. The live system map replaces the panel-based drawer.
 * 0.8.19 (2026-05-29) single-server consolidation: Watchdog pill now reads
 *        dash-server.mjs /health (port 4321) instead of the retired
 *        events_server.py (port 4322). Reports indexing-daemon liveness.
 * WordPress-style fixed dark admin bar rendered at the very top of every
 * dashboard. 34px tall. Always dark — does NOT follow the page dash-theme.
 *
 * Layout (left → center → right):
 *   LEFT   — BDOS wordmark + current-page breadcrumb (parsed from <title>)
 *   CENTER — five compact status pills (hover tooltip shows detail)
 *   RIGHT  — "Agents" button (A) → mini-card popup (LIGHT surface)
 *            "System ⚙" button → opens scheduler/index.html drawer
 *
 * Backward compatibility:
 *   Mounts into #bdos-admin-bar OR #bdos-ops-header (legacy).
 *   If neither exists, prepends a new #bdos-admin-bar as body.firstChild.
 *   window.OpsHeader is aliased to window.AdminBar for drop-in replace.
 *
 * Usage (two lines per dashboard — replace ops-header.js):
 *   <!-- anywhere in <body>, first element: -->
 *   <div id="bdos-admin-bar"></div>
 *
 *   <!-- before </body>: -->
 *   <script src="/_dashboards/_design/admin-bar.js"></script>
 *
 * The script also adds `padding-top: 34px` to <body> automatically to
 * compensate for the fixed bar so the masthead is never obscured.
 *
 * Five status checks (every 30 s):
 *   Watchdog  — dash-server.mjs /health (port 4321) — indexing daemon liveness
 *   Server    — dash-server.mjs HEAD / (port 4321)
 *   DB        — agent_logs.json freshness + row count
 *   Scheduler — most recent last_run_at among enabled scheduled_jobs within 5 min
 *   Index     — agent_logs.json generated_at within 24 h
 *
 * Global keyboard shortcuts:
 *   A / a (no modifier) — when popup CLOSED: open Agent Quick-Nav popup.
 *   Escape              — close popup (capture phase, highest priority).
 *   A/L/M/C/P/S/B/F etc.— when popup is OPEN: quick-jump to agent dashboard.
 *                         Keys are derived dynamically from AGENT_CARDS[i].name[0],
 *                         so 'A' jumps to Alfred while the popup is open.
 *   Input guard: all shortcuts ignored when focus is on INPUT, TEXTAREA,
 *                SELECT, or [contenteditable].
 *
 * Public API:
 *   AdminBar.mount()           — auto-called on DOMContentLoaded
 *   AdminBar.refresh()         — force immediate re-check of all pills
 *   AdminBar.openDrawer()      — open system status drawer
 *   AdminBar.closeDrawer()     — close drawer (Escape + backdrop also work)
 *   AdminBar.openAgentNav()    — open Agent Quick-Nav popup
 *   AdminBar.closeAgentNav()   — close Agent Quick-Nav popup
 *
 * DS Component: #bdos-admin-bar, .ab-pill, .ab-breadcrumb
 * This component defines its OWN dark-surface tokens for the bar itself — it
 * does NOT inherit the page :root because the bar must stay dark regardless of
 * dash-theme. The Agent Quick-Nav popup panel uses the page light DS tokens
 * (var(--bg-elev), var(--ink-1), etc.) to match the dashboard family default.
 *
 * Audit trail:
 *   DS 0.8.18 (2026-05-28) — Agent Quick-Nav popup redesigned into a portrait
 *     gallery (/impeccable). Panel widened 760→1040px. Each card is now a tall
 *     3:4 poster the Pixar portrait fills edge-to-edge; name + role are overlaid
 *     on a bottom legibility scrim (white text, gradient), keyboard letter moved
 *     to a glassy top-right corner chip, hover = lift + slow image zoom. Replaces
 *     the 40px-avatar + side-text row. .anav-card-top/.anav-avatar/.anav-card-meta
 *     markup retired; new .anav-portrait/.anav-portrait-fallback/.anav-overlay.
 *   DS 0.8.17 (2026-05-28) — Agent Quick-Nav popup (the "A" modal) now shows the
 *     real Pixar avatar portrait per agent (object-fit cover) instead of an emoji.
 *     Source: /00_Prompts/BDOS/agents/<slug>/avatar.png (slug = name lowercased).
 *     Emoji is retained as a graceful fallback (shown only if the image 404s).
 *     .anav-avatar bumped 36→40px, image fills the slot, subtle hover zoom.
 *   DS 0.8.15 (2026-05-28) — Keyboard fix: 'A' now reaches Alfred. While the
 *     Agent Quick-Nav popup is OPEN, the keydown handler used to intercept 'A'/'a'
 *     as a toggle (return early) BEFORE the letter quick-jump map ran. Alfred is
 *     the only agent whose initial is 'A', so it was the one agent unreachable by
 *     keyboard (pressing A just closed the popup). Restructured the handler:
 *     popup CLOSED → A opens it; popup OPEN → every agent-initial letter quick-jumps
 *     (A → Alfred included), and close is via Escape / backdrop / × button. The
 *     toggleAgentNav() helper is retained (public API + Agents-button path). Top-of-
 *     file shortcut doc updated. 0 dashboard HTML files touched.
 *   DS 0.8.14 (2026-05-27) — Removed broken "Open full graph" link from Agent
 *     Quick-Nav popup footer. The link pointed to `/_dashboards/index.html#agents`
 *     but the launcher's tab switcher does not listen on that fragment, so click
 *     was a no-op (user-reported dead button). Cleaner to remove than fix —
 *     the launcher Agents tab is reachable via Home button + tab click, no need
 *     to duplicate the entry-point inside the popup. Removed: (1) `fullGraphUrl`
 *     constant inside ensureAgentNav(); (2) `<div class="anav-footer">…</div>`
 *     block from the popup HTML template; (3) CSS rules for `.anav-footer`,
 *     `.anav-full-link`, `.anav-full-link:hover`, `.anav-full-link:focus-visible`.
 *     LAUNCHER_URL constant retained for potential future use. 0 dashboard HTML
 *     files touched.
 *   DS 0.8.13 (2026-05-27) — AGENT_CARDS gained 7th entry (Forge 🔨, Practice Steward).
 *     Grid CSS migrated 2-col × 3-row fixed (DS 0.7.9) → adaptive auto-fill
 *     `repeat(auto-fill, minmax(220px, 1fr))`. Rationale: 7 cards on the prior
 *     fixed 2-col layout would force a 4-row arrangement with one empty cell on
 *     the last row — awkward visual gap. Adaptive grid fills 3 columns on the
 *     760px panel (3×3 for 7 cards, last row 1 card; 3×2 for 6 cards) and
 *     gracefully falls back to 2 or 1 column on narrower viewports. The
 *     nth-child(2n) right-border rule is replaced by :last-child border-right
 *     removal — covers any "rightmost-of-row 1 card" overflow scenario in
 *     auto-fill arrangements. Panel width (`min(96vw, 760px)`) untouched. 0
 *     dashboard HTML files modified. AGENT_CARDS Forge entry was added by
 *     main Claude in the prior step; this commit handles the layout
 *     accommodation only.
 *   DS 0.8.16 (2026-05-28) — Sage entry removed from AGENT_CARDS. Sage agent
 *     deprecated and absorbed into Alfred v0.3. Letter-jump 'S' uncontested.
 *   DS 0.8.8 (2026-05-25) — AGENT_CARDS avatar sync: Presto 🎯→🐰, Sage 🌿→🦉.
 *     Single source of truth is AGENT_PROFILES.md (emoji field per agent section).
 *     admin-bar.js AGENT_CARDS MUST always match AGENT_PROFILES.md — never invent
 *     an emoji. Version bump 0.8.0 → 0.8.1 (admin-bar internal version).
 *   DS 0.8.5 (2026-05-25) — ESC fix + letter shortcuts + shortcut badge.
 *     (1) ESC bug fixed: dedicated capture-phase keydown listener registered
 *     at mount() time — fires unconditionally regardless of drawer state.
 *     Previously ESC only worked via the drawer's listener (ensureDrawer()),
 *     so if the drawer was never opened the popup had no ESC handler.
 *     (2) Letter quick-jump shortcuts: while popup is open, pressing the first
 *     letter of any agent name (L/M/C/P/S/B) navigates to their dashboard.
 *     Map built dynamically from AGENT_CARDS — no hardcoded letters. If two
 *     agents share an initial, first wins + console.warn logged.
 *     (3) UI affordance: .anav-kbadge (10px monospace, var(--bg-sunken))
 *     appears in each card's anav-name-row between the name and .anav-arrow.
 *     Shows the shortcut key letter. DS §10 updated. Version 0.7.9 → 0.8.0.
 *   DS 0.7.9 (2026-05-25) — Layout fix: 2-col × 3-row grid for Agent Quick-Nav.
 *     Root cause of 4-card / 2×2 bug: repeat(3, 1fr) on a 680px panel renders 3 narrow
 *     columns where the oneliner text (white-space: nowrap) pushes each card wider than
 *     the available column width, causing the last row to overflow/clip on real viewports.
 *     Additionally the media-query breakpoint (max-width: 520px) only applies to the
 *     viewport width, not the panel width, so the 3-col fallback never triggered properly.
 *     Fixes: (1) grid-template-columns: 1fr 1fr (fixed 2-col × 3-row — 6 agents fit
 *     cleanly, more horizontal space per card); (2) panel width bumped to min(96vw, 760px)
 *     for comfortable 2-col reading; (3) anav-oneliner white-space: normal + allow
 *     2-line wrap (removed nowrap/ellipsis) so Maestro long text wraps instead of
 *     overflowing; (4) removed now-superseded @media (max-width: 520px) 2-col override
 *     (already the default); (5) nth-child border-right rules updated for 2-col rhythm
 *     (2n instead of 3n). Version bump 0.7.8 → 0.7.9.
 *   DS 0.7.8 (2026-05-25) — Bug-fix: Agent Quick-Nav always shows all 6 agent cards.
 *     Root cause: ensureAgentNav() had early-return guard when #bdos-agent-nav existed,
 *     so a stale DOM built from an older AGENT_CARDS (4 entries) was reused on subsequent
 *     opens. Fix: always refresh the anav-grid innerHTML from AGENT_CARDS on every
 *     openAgentNav() call. Safety CSS: anav-frame gets max-height + overflow-y: auto so
 *     tall content never gets clipped on short viewports. Version bump 0.7.7 → 0.7.8.
 *   DS 0.7.7 (2026-05-25) — Agent Quick-Nav popup craft polish (tend mode).
 *     Typography: anav-name 12px → 13.5px (ratio 1.35 vs oneliner 10px, was 1.14).
 *     Spacing rhythm: header/grid/footer get distinct vertical padding, cards
 *     22px 20px vertical/horizontal (was 14px 16px flat). Emoji promoted to
 *     avatar-slot (.anav-avatar: 36px rounded square, var(--bg-sunken),
 *     var(--radius-m)). Arrow affordance (.anav-arrow) translateX(3px) on hover,
 *     ease-out-quart, no layout shift. Hover micro-elevation: var(--shadow-1) on
 *     anav-card + lift. Focus ring: 2px var(--accent) + 3px offset. Open animation:
 *     scrim fade 120ms, frame scale(0.96)→scale(1) + opacity 200ms ease-out-quart.
 *     Footer full-link gets underline-offset on hover (DS link convention).
 *     Version bump 0.7.6 → 0.7.7. No new DS tokens introduced.
 *   DS 0.7.6 (2026-05-25) — Agent Quick-Nav popup switched to light surface.
 *     Panel (.anav-frame) and cards (.anav-card) now use DS page tokens:
 *     var(--bg-elev) panel, var(--bg-page) card hover, var(--ink-1)/var(--ink-3)
 *     text, var(--line)/var(--line-soft) borders, var(--accent) hover accents,
 *     var(--accent-tint) focus ring. Scrim (backdrop) remains dark. Header,
 *     shortcut badge, close button, footer link updated for light palette.
 *     Version bump 0.7.5 → 0.7.6. DS §10 updated: panel = light surface,
 *     scrim = dark backdrop (invariant).
 *   DS 0.7.5 (2026-05-25) — Keyboard shortcut changed: Cmd+Shift+A → bare A/a
 *     (modifier-free). Input guard added: ignored when focus is on INPUT,
 *     TEXTAREA, SELECT, or [contenteditable] (future-proof). Version bump
 *     0.7.4 → 0.7.5.
 *   DS 0.7.4 (2026-05-25) — Agent Quick-Nav popup added. Global keyboard
 *     shortcut Cmd/Ctrl+Shift+A. Centered modal overlay with blur backdrop.
 *     6 agent mini-cards (emoji + name + 1-liner + link). Footer "Open full
 *     graph →" link to index.html#agents. Dark-theme aware, DS tokens.
 *     AGENT_DASHBOARD_URLS static list. .ab-agents-btn added to right zone.
 *   DS 0.6.0 (2026-05-25) — Initial admin bar replacing ops-header strip.
 */

(function () {
  'use strict';

  // ---------------------------------------------------------------------------
  // Configuration
  // ---------------------------------------------------------------------------
  const DASH_SERVER     = 'http://localhost:4321';   // single browser-facing server
  const SIDECAR_PATH    = '/_dashboards/_design/agent_logs.json';
  const SCHEDULER_URL   = '/_dashboards/scheduler/index.html';
  const LAUNCHER_URL    = '/_dashboards/index.html';
  const REFRESH_MS      = 30_000;    // poll every 30 s
  const BAR_HEIGHT_PX   = 34;

  // ---------------------------------------------------------------------------
  // Agent Quick-Nav — static list (DS 0.7.4)
  // Depth-independent relative path: everything is under _dashboards/, so
  // using an absolute path from vault root works at any nesting level.
  // ---------------------------------------------------------------------------
  const AGENT_CARDS = [
    {
      emoji:  '📚',
      name:   'Librarian',
      oneliner: 'Knowledge Manager — vault indexing & retrieval',
      url:    '/_dashboards/librarian/index.html',
    },
    {
      emoji:  '🎼',
      name:   'Maestro',
      oneliner: 'Conductor & Reflective Nervous System — BDOS observatory',
      url:    '/_dashboards/maestro/index.html',
    },
    {
      emoji:  '🖼️',
      name:   'Curator',
      oneliner: 'Representation layer — dashboard family master',
      url:    '/_dashboards/curator/index.html',
    },
    {
      emoji:  '🐰',
      name:   'Presto',
      oneliner: 'Marketing Cognition Layer — distribution engine',
      url:    '/_dashboards/presto/index.html',
    },
    {
      emoji:  '🤝',
      name:   'Broker',
      oneliner: 'Sales Engine Executor — one-to-one pipeline ops',
      url:    '/_dashboards/broker/index.html',
    },
    {
      emoji:  '🔨',
      name:   'Forge',
      oneliner: 'Practice Steward — cross-client capability stewardship',
      url:    '/_dashboards/forge/index.html',
    },
    {
      emoji:  '🤵',
      name:   'Alfred',
      oneliner: 'Executive Cognition Layer — cognitive inbox & personal ops',
      url:    '/_dashboards/alfred/index.html',
    },
  ];

  /** Age thresholds */
  const SCHEDULER_STALE_MS = 5  * 60 * 1000;   // 5 min
  const INDEX_STALE_MS     = 24 * 60 * 60 * 1000; // 24 h

  // ---------------------------------------------------------------------------
  // Dark-surface design tokens (own scope — never inherits page :root)
  // ---------------------------------------------------------------------------
  //   Background:  #1d2327  (WP-style dark surface)
  //   Text:        #a7aaad  (muted label)
  //   Text strong: #c3c4c7  (breadcrumb / pill label)
  //   Accent:      #e8a87c  (terracotta lightened for dark bg)
  //   Border:      rgba(255,255,255,.08)
  //   Pill ok:     #57a773 bg, #c9ebd5 text
  //   Pill warn:   #c89b2e bg, #faebbf text
  //   Pill gap:    #d9534f bg, #fde9e8 text
  //   Pill idle:   rgba(255,255,255,.08) bg, #a7aaad text

  const CSS = `
/* ===== Admin Bar (DS 0.8.8) ===== */
#bdos-admin-bar {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  z-index: 9100;
  height: ${BAR_HEIGHT_PX}px;
  min-height: ${BAR_HEIGHT_PX}px;
  background: #1d2327;
  border-bottom: 1px solid rgba(255,255,255,.06);
  display: flex;
  align-items: center;
  gap: 0;
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, system-ui, sans-serif;
  font-size: 11px;
  font-weight: 500;
  color: #a7aaad;
  box-sizing: border-box;
  user-select: none;
  -webkit-font-smoothing: antialiased;
}

/* ---- Left zone ---- */
.ab-left {
  display: flex;
  align-items: center;
  gap: 0;
  flex-shrink: 0;
  height: 100%;
}

.ab-logo {
  display: flex;
  align-items: center;
  gap: 6px;
  padding: 0 14px;
  height: 100%;
  color: #c3c4c7;
  font-weight: 700;
  font-size: 11.5px;
  letter-spacing: .04em;
  text-transform: uppercase;
  text-decoration: none;
  border-right: 1px solid rgba(255,255,255,.06);
  transition: color 120ms;
  white-space: nowrap;
  cursor: pointer;
}
.ab-logo:hover { color: #e8a87c; }

.ab-logo-icon {
  width: 16px;
  height: 16px;
  flex-shrink: 0;
  opacity: .85;
}

.ab-sep {
  width: 1px;
  height: 18px;
  background: rgba(255,255,255,.08);
  flex-shrink: 0;
  display: none; /* only shown when breadcrumb exists */
}

.ab-breadcrumb {
  display: flex;
  align-items: center;
  gap: 4px;
  padding: 0 12px;
  color: #8c8f94;
  font-size: 11px;
  white-space: nowrap;
  overflow: hidden;
  max-width: 260px;
  text-overflow: ellipsis;
}

.ab-breadcrumb .ab-bc-home {
  color: #8c8f94;
  text-decoration: none;
  transition: color 120ms;
}
.ab-breadcrumb .ab-bc-home:hover { color: #c3c4c7; }

.ab-breadcrumb .ab-bc-sep {
  color: rgba(255,255,255,.2);
  font-size: 10px;
  flex-shrink: 0;
}

.ab-breadcrumb .ab-bc-current {
  color: #c3c4c7;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

/* ---- Center zone ---- */
.ab-center {
  flex: 1;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 6px;
  padding: 0 8px;
  min-width: 0;
}

.ab-pill {
  display: inline-flex;
  align-items: center;
  gap: 4px;
  padding: 2px 7px 2px 5px;
  border-radius: 999px;
  font-size: 10.5px;
  font-family: 'JetBrains Mono', 'Fira Mono', monospace;
  font-weight: 500;
  white-space: nowrap;
  cursor: default;
  transition: opacity 120ms;
}

.ab-pill-dot {
  width: 5px;
  height: 5px;
  border-radius: 50%;
  flex-shrink: 0;
}

.ab-pill.ok   { background: rgba(87,167,115,.18);  color: #88d9a7; }
.ab-pill.ok   .ab-pill-dot { background: #57a773; }

.ab-pill.warn { background: rgba(200,155,46,.18);  color: #f2c96e; }
.ab-pill.warn .ab-pill-dot { background: #c89b2e; }

.ab-pill.gap  { background: rgba(217,83,79,.18);   color: #f08a86; }
.ab-pill.gap  .ab-pill-dot { background: #d9534f; }

.ab-pill.idle { background: rgba(255,255,255,.06); color: #6c7075; }
.ab-pill.idle .ab-pill-dot { background: rgba(255,255,255,.2); }

/* On very small screens, hide the text label and only show the dot */
@media (max-width: 640px) {
  .ab-pill-label { display: none; }
  .ab-pill { padding: 2px 5px; }
}

/* ---- Right zone ---- */
.ab-right {
  display: flex;
  align-items: center;
  gap: 0;
  flex-shrink: 0;
  height: 100%;
}

.ab-system-btn {
  display: inline-flex;
  align-items: center;
  gap: 5px;
  padding: 0 14px;
  height: 100%;
  font-size: 11px;
  font-family: 'Inter', sans-serif;
  font-weight: 500;
  color: #a7aaad;
  background: transparent;
  border: none;
  border-left: 1px solid rgba(255,255,255,.06);
  cursor: pointer;
  transition: color 120ms, background 120ms;
  white-space: nowrap;
}
.ab-system-btn:hover {
  color: #e8a87c;
  background: rgba(255,255,255,.04);
}
.ab-system-btn:focus-visible {
  outline: 2px solid rgba(232,168,124,.7);
  outline-offset: -2px;
}

/* ---- Agents quick-nav button (DS 0.7.4) ---- */
.ab-agents-btn {
  display: inline-flex;
  align-items: center;
  gap: 5px;
  padding: 0 12px;
  height: 100%;
  font-size: 11px;
  font-family: 'Inter', sans-serif;
  font-weight: 500;
  color: #a7aaad;
  background: transparent;
  border: none;
  border-left: 1px solid rgba(255,255,255,.06);
  cursor: pointer;
  transition: color 120ms, background 120ms;
  white-space: nowrap;
}
.ab-agents-btn:hover {
  color: #e8a87c;
  background: rgba(255,255,255,.04);
}
.ab-agents-btn:focus-visible {
  outline: 2px solid rgba(232,168,124,.7);
  outline-offset: -2px;
}

/* ---- Agent Quick-Nav overlay (DS 0.7.7 — light surface panel + craft polish) ---- */
/* Scrim stays dark (invariant). Panel is light surface. */

/* === Open animation keyframes (DS 0.7.7) === */
@keyframes anav-scrim-in  { from { opacity: 0; } to { opacity: 1; } }
@keyframes anav-frame-in  {
  from { opacity: 0; transform: scale(0.96) translateY(-4px); }
  to   { opacity: 1; transform: scale(1)    translateY(0);     }
}

#bdos-agent-nav {
  position: fixed;
  inset: 0;
  z-index: 9300;
  display: none;
  align-items: flex-start;
  justify-content: center;
  padding-top: 56px;
  background: rgba(20,20,19,.55);
  backdrop-filter: blur(4px);
  -webkit-backdrop-filter: blur(4px);
}
#bdos-agent-nav.open {
  display: flex;
  animation: anav-scrim-in 120ms cubic-bezier(.2,.7,.3,1) both;
}
#bdos-agent-nav.open .anav-frame {
  animation: anav-frame-in 200ms cubic-bezier(.2,.7,.3,1) both;
}

#bdos-agent-nav .anav-frame {
  width: min(96vw, 1040px);
  /* Safety: cap height so content is never clipped on short viewports.
     overflow-y: auto enables scrolling if content grows beyond the cap. (DS 0.7.8) */
  max-height: calc(100vh - 80px);
  overflow-x: hidden;
  overflow-y: auto;
  background: var(--bg-elev, #ffffff);
  border-radius: var(--radius-xl, 14px);
  border: 1px solid var(--line, #e5e4df);
  box-shadow: 0 24px 64px rgba(20,20,19,.22), 0 4px 14px rgba(20,20,19,.10);
  display: flex;
  flex-direction: column;
}

/* === Header (DS 0.7.7) === */
#bdos-agent-nav .anav-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 14px 20px 12px;
  border-bottom: 1px solid var(--line, #e5e4df);
  gap: 10px;
}
#bdos-agent-nav .anav-header-left {
  display: flex;
  align-items: center;
  gap: 10px;
  flex: 1;
  min-width: 0;
}
#bdos-agent-nav .anav-title {
  font-size: 11px;
  font-weight: 700;
  letter-spacing: .10em;
  text-transform: uppercase;
  color: var(--ink-2, #3a3a37);
  font-family: 'Inter', sans-serif;
  white-space: nowrap;
}
#bdos-agent-nav .anav-shortcut {
  font-size: 10px;
  font-family: 'JetBrains Mono', 'Fira Mono', monospace;
  font-weight: 500;
  color: var(--ink-4, #9c9c98);
  background: var(--bg-sunken, #f3f1ea);
  border: 1px solid var(--line, #e5e4df);
  border-radius: var(--radius-s, 4px);
  padding: 2px 7px;
  letter-spacing: .02em;
  flex-shrink: 0;
}
#bdos-agent-nav .anav-close {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 24px;
  height: 24px;
  border-radius: 50%;
  border: 1px solid var(--line, #e5e4df);
  background: transparent;
  color: var(--ink-3, #6d6d6a);
  font-size: 12px;
  cursor: pointer;
  transition: background 120ms cubic-bezier(.2,.7,.3,1),
              color      120ms cubic-bezier(.2,.7,.3,1),
              border-color 120ms cubic-bezier(.2,.7,.3,1);
  flex-shrink: 0;
}
#bdos-agent-nav .anav-close:hover {
  background: var(--gap-tint, #fbeae6);
  color: var(--gap, #c0392b);
  border-color: rgba(192,57,43,.35);
}
#bdos-agent-nav .anav-close:focus-visible {
  outline: 2px solid var(--accent, #D97757);
  outline-offset: 3px;
}

/* === Poster gallery (DS 0.8.18) — image-dominant cards, text overlaid on a
   legibility scrim. The Pixar portraits ARE the content; each card is a tall
   3:4 poster the portrait fills edge-to-edge, with name + role floated on a
   bottom gradient and the keyboard letter as a corner chip. Replaces the old
   40px-avatar + side-text row layout. === */
#bdos-agent-nav .anav-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(210px, 1fr));
  gap: 16px;
  padding: 20px;
}

#bdos-agent-nav .anav-card {
  position: relative;
  display: block;
  aspect-ratio: 3 / 4;
  border-radius: var(--radius-l, 10px);
  overflow: hidden;
  text-decoration: none;
  background: var(--bg-sunken, #f3f1ea);
  box-shadow: 0 1px 3px rgba(20,20,19,.10);
  transition: transform 260ms cubic-bezier(.2,.7,.3,1),
              box-shadow 260ms cubic-bezier(.2,.7,.3,1);
  cursor: pointer;
  outline: none;
}
#bdos-agent-nav .anav-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 20px 40px rgba(20,20,19,.26), 0 6px 14px rgba(20,20,19,.14);
  z-index: 1;
}
#bdos-agent-nav .anav-card:focus-visible {
  outline: 2px solid var(--accent, #D97757);
  outline-offset: 3px;
}

/* Portrait fills the whole poster, slow zoom on hover */
#bdos-agent-nav .anav-portrait {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
  transition: transform 460ms cubic-bezier(.2,.7,.3,1);
}
#bdos-agent-nav .anav-card:hover .anav-portrait { transform: scale(1.06); }
#bdos-agent-nav .anav-portrait-fallback {
  position: absolute;
  inset: 0;
  display: none;
  align-items: center;
  justify-content: center;
  font-size: 72px;
  line-height: 1;
  background: var(--bg-sunken, #f3f1ea);
}

/* Keyboard letter as a glassy corner chip (legible over any portrait) */
#bdos-agent-nav .anav-kbadge {
  position: absolute;
  top: 10px;
  right: 10px;
  z-index: 2;
  font-size: 11px;
  font-family: 'JetBrains Mono', 'Fira Mono', monospace;
  font-weight: 600;
  color: #fff;
  background: rgba(15,14,13,.45);
  border: 1px solid rgba(255,255,255,.28);
  border-radius: var(--radius-s, 4px);
  padding: 2px 7px;
  line-height: 1.3;
  letter-spacing: .04em;
  backdrop-filter: blur(4px);
  -webkit-backdrop-filter: blur(4px);
  transition: background 200ms cubic-bezier(.2,.7,.3,1),
              border-color 200ms cubic-bezier(.2,.7,.3,1);
  user-select: none;
}
#bdos-agent-nav .anav-card:hover .anav-kbadge {
  background: var(--accent, #D97757);
  border-color: var(--accent, #D97757);
}

/* Text overlay on a bottom-anchored legibility scrim */
#bdos-agent-nav .anav-overlay {
  position: absolute;
  left: 0;
  right: 0;
  bottom: 0;
  padding: 34px 14px 13px;
  background: linear-gradient(to top,
              rgba(15,14,13,.92) 0%,
              rgba(15,14,13,.70) 36%,
              rgba(15,14,13,.26) 66%,
              transparent 100%);
}
#bdos-agent-nav .anav-name-row {
  display: flex;
  align-items: baseline;
  justify-content: space-between;
  gap: 8px;
}
#bdos-agent-nav .anav-name {
  font-size: 16px;
  font-weight: 700;
  letter-spacing: -0.01em;
  color: #fff;
  font-family: 'Inter', sans-serif;
  line-height: 1.15;
  text-shadow: 0 1px 4px rgba(0,0,0,.45);
}
#bdos-agent-nav .anav-arrow {
  font-size: 15px;
  color: #fff;
  opacity: 0;
  transform: translateX(-5px);
  transition: opacity 240ms cubic-bezier(.2,.7,.3,1),
              transform 240ms cubic-bezier(.2,.7,.3,1);
  flex-shrink: 0;
  line-height: 1;
}
#bdos-agent-nav .anav-card:hover .anav-arrow {
  opacity: 1;
  transform: translateX(0);
}
#bdos-agent-nav .anav-oneliner {
  margin-top: 3px;
  font-size: 11px;
  color: rgba(255,255,255,.82);
  font-family: 'Inter', sans-serif;
  line-height: 1.4;
  text-shadow: 0 1px 3px rgba(0,0,0,.4);
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

/* === Footer removed in DS 0.8.14 — "Open full graph" link was broken (target #agents fragment had no listener), and the graph itself is a separate Agents tab in the launcher. Removing rather than fixing keeps the popup tight. === */

/* ---- Drawer overlay (shared with ops-header — same ID so no double) ---- */
#bdos-ops-drawer {
  position: fixed;
  inset: 0;
  z-index: 9200;
  display: none;
  align-items: flex-start;
  justify-content: center;
  padding-top: 50px;
  background: rgba(20,20,19,.5);
  backdrop-filter: blur(3px);
}
#bdos-ops-drawer.open { display: flex; }

#bdos-ops-drawer .drawer-frame {
  width: min(96vw, 1100px);
  height: min(85vh, 860px);
  background: var(--bg-page, #faf9f5);
  border-radius: var(--radius-xl, 14px);
  border: 1px solid var(--line, #e5e4df);
  box-shadow: 0 24px 64px rgba(20,20,19,.28);
  overflow: hidden;
  position: relative;
  display: flex;
  flex-direction: column;
}
#bdos-ops-drawer .drawer-close {
  position: absolute;
  top: 12px; right: 14px;
  width: 28px; height: 28px;
  border-radius: 50%;
  border: 1px solid var(--line, #e5e4df);
  background: var(--bg-elev, #fff);
  cursor: pointer;
  font-size: 14px;
  color: var(--ink-3, #6d6d6a);
  display: flex; align-items: center; justify-content: center;
  z-index: 2;
  transition: background 120ms, border-color 120ms;
}
#bdos-ops-drawer .drawer-close:hover {
  background: var(--gap-tint, #fbeae6);
  border-color: var(--gap, #c0392b);
  color: var(--gap, #c0392b);
}
#bdos-ops-drawer iframe {
  flex: 1;
  border: none;
  width: 100%;
  height: 100%;
}
`;

  // ---------------------------------------------------------------------------
  // State
  // ---------------------------------------------------------------------------
  const state = {
    watchdog:  { status: 'idle', label: 'Watchdog', detail: '' },
    server:    { status: 'idle', label: 'Server',   detail: '' },
    db:        { status: 'idle', label: 'DB',        detail: '' },
    scheduler: { status: 'idle', label: 'Sched',    detail: '' },
    index:     { status: 'idle', label: 'Index',     detail: '' },
  };

  // ---------------------------------------------------------------------------
  // Check functions (identical logic to ops-header.js)
  // ---------------------------------------------------------------------------
  async function checkWatchdog() {
    try {
      const r = await fetch(DASH_SERVER + '/health', { signal: AbortSignal.timeout(4000) });
      const j = await r.json();
      if (j.ok) {
        state.watchdog = { status: 'ok', label: 'Watchdog', detail: `clients:${j.clients}` };
      } else if (j.daemon_alive === false) {
        state.watchdog = { status: 'gap', label: 'Watchdog', detail: 'daemon down' };
      } else {
        state.watchdog = { status: 'warn', label: 'Watchdog', detail: j.db_exists ? 'unhealthy' : 'no index' };
      }
    } catch (_) {
      state.watchdog = { status: 'gap', label: 'Watchdog', detail: 'offline' };
    }
  }

  async function checkServer() {
    try {
      const r = await fetch(DASH_SERVER + '/', {
        method: 'HEAD',
        signal: AbortSignal.timeout(4000),
      });
      state.server = {
        status: r.ok || r.status === 301 || r.status === 302 ? 'ok' : 'warn',
        label: 'Server',
        detail: String(r.status),
      };
    } catch (_) {
      state.server = { status: 'gap', label: 'Server', detail: 'offline' };
    }
  }

  async function checkDB() {
    try {
      const r = await fetch(SIDECAR_PATH + '?_=' + Date.now(), { signal: AbortSignal.timeout(4000) });
      const j = await r.json();
      const ageMs = Date.now() - new Date(j.generated_at).getTime();
      const rows = j.total_rows || 0;
      if (ageMs < 5 * 60 * 1000) {
        state.db = { status: 'ok', label: 'DB', detail: `${rows}r` };
      } else {
        state.db = { status: 'warn', label: 'DB', detail: 'stale' };
      }
    } catch (_) {
      state.db = { status: 'gap', label: 'DB', detail: 'no sidecar' };
    }
  }

  async function checkScheduler() {
    // Liveness is derived from scheduled_jobs[].last_run_at (enabled jobs only).
    // This survives the removal of scheduler-tagged noise rows from agent_logs.
    try {
      const r = await fetch(SIDECAR_PATH + '?_=' + Date.now(), { signal: AbortSignal.timeout(4000) });
      const j = await r.json();
      const jobs = Array.isArray(j.scheduled_jobs) ? j.scheduled_jobs : [];
      const enabledJobs = jobs.filter(job => job && job.enabled);
      if (enabledJobs.length === 0) {
        state.scheduler = { status: 'idle', label: 'Sched', detail: 'no jobs' };
        return;
      }
      // Find the most recent last_run_at among enabled jobs.
      let latestMs = 0;
      for (const job of enabledJobs) {
        if (!job.last_run_at) continue;
        const t = new Date(job.last_run_at).getTime();
        if (!isNaN(t) && t > latestMs) latestMs = t;
      }
      if (latestMs === 0) {
        // Jobs exist but none have run yet.
        state.scheduler = { status: 'idle', label: 'Sched', detail: 'never run' };
        return;
      }
      const ageMs = Date.now() - latestMs;
      if (ageMs < SCHEDULER_STALE_MS) {
        state.scheduler = { status: 'ok', label: 'Sched', detail: 'active' };
      } else {
        const mins = Math.round(ageMs / 60000);
        state.scheduler = { status: 'warn', label: 'Sched', detail: `${mins}m` };
      }
    } catch (_) {
      state.scheduler = { status: 'gap', label: 'Sched', detail: 'unknown' };
    }
  }

  async function checkIndex() {
    try {
      const r = await fetch(SIDECAR_PATH + '?_=' + Date.now(), { signal: AbortSignal.timeout(4000) });
      const j = await r.json();
      const ageMs = Date.now() - new Date(j.generated_at).getTime();
      if (ageMs < INDEX_STALE_MS) {
        state.index = { status: 'ok', label: 'Index', detail: 'fresh' };
      } else {
        const h = Math.round(ageMs / 3600000);
        state.index = { status: 'warn', label: 'Index', detail: `${h}h` };
      }
    } catch (_) {
      state.index = { status: 'gap', label: 'Index', detail: 'unknown' };
    }
  }

  // ---------------------------------------------------------------------------
  // Breadcrumb helper — derive from document title
  // ---------------------------------------------------------------------------
  function parseBreadcrumb() {
    // Title format: "PageName — Dashboard" or just "PageName"
    const raw = document.title || '';
    // Common patterns: "Ideas Vault" / "Curator — Dashboard Family Observatory" / etc.
    const parts = raw.split(/\s[—–-]\s/).map(s => s.trim()).filter(Boolean);
    if (parts.length === 0) return { current: '', isRoot: true };
    const current = parts[0];
    const isRoot = current === 'Ideas Vault';
    return { current, isRoot };
  }

  // ---------------------------------------------------------------------------
  // Render helpers
  // ---------------------------------------------------------------------------
  function pillHTML(key) {
    const s = state[key];
    const tooltip = s.detail ? `${s.label}: ${s.detail}` : s.label;
    return `<span class="ab-pill ${s.status}" title="${tooltip}" data-pill="${key}">
      <span class="ab-pill-dot"></span><span class="ab-pill-label">${s.label}</span>
    </span>`;
  }

  function render() {
    const host = document.getElementById('bdos-admin-bar') ||
                 document.getElementById('bdos-ops-header');
    if (!host) return;

    const bc = parseBreadcrumb();

    const breadcrumbHTML = bc.isRoot
      ? ''
      : `<span class="ab-sep" style="display:block"></span>
         <nav class="ab-breadcrumb" aria-label="Breadcrumb">
           <a class="ab-bc-home" href="/_dashboards/index.html">Vault</a>
           <span class="ab-bc-sep">›</span>
           <span class="ab-bc-current" title="${bc.current}">${bc.current}</span>
         </nav>`;

    host.innerHTML = `
      <div class="ab-left">
        <a class="ab-logo" href="/_dashboards/index.html" title="Ideas Vault Launcher">
          <svg class="ab-logo-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
            <path d="M12 2L3 7l9 5 9-5-9-5z"/><path d="M3 12l9 5 9-5"/><path d="M3 17l9 5 9-5"/>
          </svg>
          BDOS
        </a>
        ${breadcrumbHTML}
      </div>
      <div class="ab-center" role="status" aria-label="System status">
        ${Object.keys(state).map(k => pillHTML(k)).join('')}
      </div>
      <div class="ab-right">
        <button class="ab-agents-btn" id="bdos-ab-agents-btn"
                title="Agent Quick-Nav (A)"
                aria-label="Open Agent Quick-Nav">
          <svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="8" r="4"/><path d="M4 20c0-4 3.6-7 8-7s8 3 8 7"/></svg>
          Agents
        </button>
        <button class="ab-system-btn" id="bdos-ab-system-btn"
                title="Open BDOS system architecture"
                aria-label="Open BDOS system architecture">
          <svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="3"/><path d="M19.07 4.93a10 10 0 0 1 0 14.14M4.93 4.93a10 10 0 0 0 0 14.14"/></svg>
          System
        </button>
      </div>
    `;

    // Re-wire buttons (re-rendered on every refresh)
    const agentsBtn = document.getElementById('bdos-ab-agents-btn');
    if (agentsBtn) agentsBtn.addEventListener('click', openAgentNav);
    const btn = document.getElementById('bdos-ab-system-btn');
    if (btn) btn.addEventListener('click', () => { window.location.href = '/_dashboards/system.html'; });
  }

  // ---------------------------------------------------------------------------
  // Body padding compensation
  // ---------------------------------------------------------------------------
  function applyBodyPadding() {
    // Only set if not already accounting for admin bar
    const current = parseInt(window.getComputedStyle(document.body).paddingTop, 10) || 0;
    if (current < BAR_HEIGHT_PX) {
      document.body.style.paddingTop = BAR_HEIGHT_PX + 'px';
    }
  }

  // ---------------------------------------------------------------------------
  // Agent Quick-Nav (DS 0.7.4, updated DS 0.8.7)
  // ---------------------------------------------------------------------------
  function ensureAgentNav() {
    // DS 0.7.8 fix: always rebuild the cards grid from the live AGENT_CARDS array so
    // a stale DOM (built when AGENT_CARDS had fewer entries) never persists across opens.
    //
    // DS 0.8.7: include .anav-kbadge showing the letter shortcut for each card.
    // The badge letter is the first character of the agent name (uppercase).
    // Build the shortcut map here so the badge matches what the listener actually handles.
    const cardsHTML = AGENT_CARDS.map(a => {
      const letter = a.name[0].toUpperCase();
      const avatarSrc = `/00_Prompts/BDOS/agents/${a.name.toLowerCase()}/avatar.png`;
      return `
      <a class="anav-card" href="${a.url}" title="Open ${a.name} dashboard (${letter})">
        <img class="anav-portrait" src="${avatarSrc}" alt="" loading="lazy"
             onerror="this.style.display='none';this.nextElementSibling.style.display='flex';">
        <span class="anav-portrait-fallback" aria-hidden="true">${a.emoji}</span>
        <span class="anav-kbadge" aria-hidden="true" title="Press ${letter} to open">${letter}</span>
        <div class="anav-overlay">
          <div class="anav-name-row">
            <span class="anav-name">${a.name}</span>
            <span class="anav-arrow" aria-hidden="true">&#x2192;</span>
          </div>
          <div class="anav-oneliner">${a.oneliner}</div>
        </div>
      </a>
    `;
    }).join('');

    // If overlay already exists, only refresh the cards grid (cheap — no full DOM rebuild,
    // no event-listener churn on the close button / backdrop).
    const existing = document.getElementById('bdos-agent-nav');
    if (existing) {
      const grid = document.getElementById('bdos-agent-nav-grid');
      if (grid) grid.innerHTML = cardsHTML;
      return;
    }

    // First time: build the full overlay.

    const el = document.createElement('div');
    el.id = 'bdos-agent-nav';
    el.setAttribute('role', 'dialog');
    el.setAttribute('aria-modal', 'true');
    el.setAttribute('aria-label', 'Agent Quick Navigation');
    el.innerHTML = `
      <div class="anav-frame">
        <div class="anav-header">
          <div class="anav-header-left">
            <span class="anav-title">BDOS Agent Family</span>
            <span class="anav-shortcut">A</span>
          </div>
          <button class="anav-close" id="bdos-agent-nav-close" aria-label="Close Agent Quick-Nav">&#x2715;</button>
        </div>
        <div class="anav-grid" id="bdos-agent-nav-grid">
          ${cardsHTML}
        </div>
      </div>
    `;
    document.body.appendChild(el);

    // Outside-click closes
    el.addEventListener('click', (e) => { if (e.target === el) closeAgentNav(); });
    // Close button
    document.getElementById('bdos-agent-nav-close').addEventListener('click', closeAgentNav);
  }

  function openAgentNav() {
    ensureAgentNav();
    document.getElementById('bdos-agent-nav').classList.add('open');
    document.body.style.overflow = 'hidden';
  }

  function closeAgentNav() {
    const nav = document.getElementById('bdos-agent-nav');
    if (!nav) return;
    nav.classList.remove('open');
    document.body.style.overflow = '';
  }

  function toggleAgentNav() {
    const nav = document.getElementById('bdos-agent-nav');
    if (nav && nav.classList.contains('open')) {
      closeAgentNav();
    } else {
      openAgentNav();
    }
  }

  // ---------------------------------------------------------------------------
  // Drawer
  // ---------------------------------------------------------------------------
  function ensureDrawer() {
    if (document.getElementById('bdos-ops-drawer')) return;
    const el = document.createElement('div');
    el.id = 'bdos-ops-drawer';
    el.innerHTML = `
      <div class="drawer-frame">
        <button class="drawer-close" id="bdos-ops-drawer-close" aria-label="Close system drawer">&#x2715;</button>
        <iframe id="bdos-ops-iframe" src="" title="BDOS System Status"></iframe>
      </div>
    `;
    document.body.appendChild(el);
    el.addEventListener('click', (e) => { if (e.target === el) closeDrawer(); });
    document.getElementById('bdos-ops-drawer-close').addEventListener('click', closeDrawer);
    // Note: ESC handling for the drawer is now done by the capture-phase listener
    // registered in mount() — no separate drawer keydown listener needed. (DS 0.8.7)
  }

  function openDrawer() {
    ensureDrawer();
    const drawer = document.getElementById('bdos-ops-drawer');
    const iframe = document.getElementById('bdos-ops-iframe');
    iframe.src = SCHEDULER_URL + '?embedded=1&_=' + Date.now();
    drawer.classList.add('open');
    document.body.style.overflow = 'hidden';
  }

  function closeDrawer() {
    const drawer = document.getElementById('bdos-ops-drawer');
    if (!drawer) return;
    drawer.classList.remove('open');
    document.body.style.overflow = '';
    const iframe = document.getElementById('bdos-ops-iframe');
    if (iframe) iframe.src = '';
  }

  // ---------------------------------------------------------------------------
  // Public refresh
  // ---------------------------------------------------------------------------
  async function refresh() {
    await Promise.allSettled([
      checkWatchdog(),
      checkServer(),
      checkDB(),
      checkScheduler(),
      checkIndex(),
    ]);
    render();
  }

  // ---------------------------------------------------------------------------
  // CSS injection
  // ---------------------------------------------------------------------------
  function injectCSS() {
    if (document.getElementById('bdos-admin-bar-css')) return;
    const s = document.createElement('style');
    s.id = 'bdos-admin-bar-css';
    s.textContent = CSS;
    document.head.appendChild(s);
  }

  // ---------------------------------------------------------------------------
  // Mount
  // ---------------------------------------------------------------------------
  function mount() {
    injectCSS();

    // Resolve host: prefer #bdos-admin-bar, fall back to legacy #bdos-ops-header,
    // else create a new element
    let host = document.getElementById('bdos-admin-bar') ||
               document.getElementById('bdos-ops-header');
    if (!host) {
      host = document.createElement('div');
      host.id = 'bdos-admin-bar';
      document.body.insertBefore(host, document.body.firstChild);
    } else {
      // Normalize: always use id="bdos-admin-bar" on the mounted element
      host.id = 'bdos-admin-bar';
    }

    applyBodyPadding();

    // Render placeholder pills immediately (idle state)
    render();

    // ---------------------------------------------------------------------------
    // Build the letter → url map dynamically from AGENT_CARDS (DS 0.8.7).
    // First agent with a given initial wins; warn if a collision is detected.
    // ---------------------------------------------------------------------------
    const _agentLetterMap = {};
    for (const card of AGENT_CARDS) {
      const ch = card.name[0].toLowerCase();
      if (_agentLetterMap[ch]) {
        console.warn('[admin-bar] Letter shortcut collision: "' + ch + '" already mapped to ' +
          _agentLetterMap[ch] + ', ignoring ' + card.name);
      } else {
        _agentLetterMap[ch] = card.url;
      }
    }

    // ---------------------------------------------------------------------------
    // ESC handler — capture phase so it fires BEFORE the drawer listener and
    // before any inline onkeydown on child elements. Closes popup unconditionally
    // when popup is open; also closes drawer if open.
    // DS 0.8.7 fix: previously ESC only worked via the drawer's listener, which
    // is registered lazily in ensureDrawer() — so if the drawer was never opened,
    // ESC had no effect on the popup.
    // ---------------------------------------------------------------------------
    document.addEventListener('keydown', function(e) {
      if (e.key !== 'Escape') return;
      const nav = document.getElementById('bdos-agent-nav');
      if (nav && nav.classList.contains('open')) {
        e.stopPropagation();
        closeAgentNav();
        return;
      }
      closeDrawer();
    }, true /* capture */);

    // ---------------------------------------------------------------------------
    // Global keyboard shortcut: bare A/a (no modifier) — toggle Agent Quick-Nav.
    // When popup is open: letter keys (L/M/C/P/S/B…) quick-jump to that agent's
    // dashboard (new tab mirrors the card-click behavior — uses window.location
    // same as a plain href click, since cards are <a> tags with no target="_blank").
    // Input guard: skip if focus is inside a text-entry element (future-proof).
    // ---------------------------------------------------------------------------
    document.addEventListener('keydown', function(e) {
      if (e.metaKey || e.ctrlKey || e.shiftKey || e.altKey) return;
      const tag = (document.activeElement && document.activeElement.tagName) || '';
      if (['INPUT', 'TEXTAREA', 'SELECT'].includes(tag.toUpperCase())) return;
      if (document.activeElement && document.activeElement.isContentEditable) return;

      const nav = document.getElementById('bdos-agent-nav');
      const navOpen = nav && nav.classList.contains('open');

      if (navOpen) {
        // Popup OPEN: every agent-initial letter quick-jumps — INCLUDING 'a'/'A',
        // which jumps to Alfred. (DS 0.8.15: previously 'A' re-toggled the popup
        // here, so Alfred — the only A-agent — was unreachable by keyboard.)
        // Close is via Escape (capture-phase handler), backdrop, or the × button.
        const ch = e.key.toLowerCase();
        if (_agentLetterMap[ch]) {
          e.preventDefault();
          closeAgentNav();
          window.location.href = _agentLetterMap[ch];
        }
        return;
      }

      // Popup CLOSED: A/a opens it.
      if (e.key === 'a' || e.key === 'A') {
        e.preventDefault();
        openAgentNav();
      }
    });

    // First real async check
    refresh();

    // Periodic refresh
    setInterval(refresh, REFRESH_MS);
  }

  // ---------------------------------------------------------------------------
  // Public API
  // ---------------------------------------------------------------------------
  const AdminBar = { mount, refresh, openDrawer, closeDrawer, openAgentNav, closeAgentNav, toggleAgentNav };
  window.AdminBar = AdminBar;

  // Backward-compat alias so any code calling OpsHeader.* still works
  window.OpsHeader = AdminBar;

  // Auto-mount when DOM is ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', mount);
  } else {
    mount();
  }

})();
