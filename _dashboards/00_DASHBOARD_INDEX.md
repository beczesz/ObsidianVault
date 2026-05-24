---
title: 00_DASHBOARD_INDEX
description: A _dashboards/ család élő indexe — minden dashboard egy sorban: verzió, cím, adatforrás, pattern, launcher-státusz, design-system megfelelőség. A Curator agent tartja frissen MINDEN build / tend / retire / promote után.
generated_by: curator (tend mode — Phase C canonical updates Phase 6 Scheduling v1)
last_updated: 2026-05-24
dashboard_count: 16
design_system_version: 0.5.0
id: b81d7930-f854-44dd-ae83-6d36b612d698
index_schema_version: 1
---

# Dashboard Index

> **Élő index — a Curator tartja karban.** Frissül MINDEN dashboard-művelet után (`build`, `tend`, `retire`, `promote`). A gyors keresés/navigáció alapja. Friss állapotért `survey` mód regenerálja.
>
> **Szerver:** `_dashboards/_tools/dash-server.mjs` · port **4321** · `/` → launcher · SSE a `02_Areas/**/*.md`-re. Indítás/megnyitás/leállítás: Curator `serve` mód.
> **Design system:** [`_design/DESIGN_SYSTEM.md`](_design/DESIGN_SYSTEM.md) v0.3.0 — kanonikus vizuális nyelv. Új (0.3.0): dark theme tokens + `.theme-toggle` + shared `dash-theme` localStorage key + FOUC-init snippet + system-aware default (promote 2026-05-22, family-wide rollout kész). Korábbi: `.card-copy-ref` + `data-card-id` konvenció (0.2.0).

## Család (live, `_dashboards/`)

| Fájl | Cím | Verzió | Adatforrás | Pattern | Launcher | DS |
|---|---|---|---|---|---|---|
| [`index.html`](index.html) | Ideas Vault (launcher) | 0.8.0 | — (Areas: statikus fa-navigátor; Agents: live from `/00_Prompts/BDOS/00_AGENTS_INDEX.md` 8s poll) | launcher + agent-graph | — (IS the launcher) | ✅ DS 0.3.0 — dark theme toggle + shared `dash-theme` key; area-brand tokens dark-mapped; `.card-copy-ref` on all leaf articles; v0.7.0: top-level tab switcher (#areas / #agents), D3.js force-directed agent graph, detail panel, coming-soon modal |
| [`sales.html`](sales.html) | CPS Sales Pipeline | 0.7.4 | `/02_Areas/Sonrisa/CPS/TODAY.md` + `/02_Areas/Sonrisa/CPS/Sales/Pipeline.md` + `/02_Areas/Sonrisa/CPS/Sales/Sales Enablement/leads.md` + per-lead `NOTES.md` | per-record | ✅ live | ✅ DS 0.3.0 — dark theme toggle; pipeline-stage tokens dark-mapped; industry tag dark overrides; `.card-copy-ref` on all lead cards |
| [`partnerships.html`](partnerships.html) | CPS Partnerships | 0.2.3 | `/02_Areas/Sonrisa/CPS/Partnership/partners.md` | single-file | ✅ live | ✅ DS 0.3.0 — dark theme toggle + canonical dark tokens; `.card-copy-ref` on vendor cards |
| [`navigator.html`](navigator.html) | Navigátor Podcast | 0.1.4 | `/02_Areas/Navigátor Podcast/EPISODES.md` + `/02_Areas/Navigátor Podcast/TODO.md` + per-episode synthesis `.md` | per-record + single-file hybrid | ✅ live | ✅ DS 0.3.0 — bespoke dark-mode replaced with canonical implementation; shared `dash-theme` key (was `nav-dash-theme`); `--info`/`--info-tint`, `--shadow-3` preserved as navigator extras |
| [`aiops.html`](aiops.html) | CPS AI Ops | 0.1.4 | `/02_Areas/Sonrisa/CPS/Strategy/AI%20Ops/aiops.md` | single-file | ✅ live | ✅ DS 0.3.0 — dark theme toggle; `--prod`/`--prod-tint` dark-mapped; `.card-copy-ref` on pillar cards |
| [`team.html`](team.html) | CPS Team | 0.1.4 | `/02_Areas/Sonrisa/CPS/Team/team.md` | single-file | ✅ live | ✅ DS 0.3.0 — dark theme toggle; `--info`/`--info-tint` dark-mapped; `.card-copy-ref` on unit + person cards |
| [`plugins.html`](plugins.html) | Claude Code Plugins — Vault Fit | 0.1.3 | hardcoded (live-fetch wiring deferred) | static / hardcoded | ✅ live | ✅ DS 0.3.0 — dark theme toggle + canonical dark tokens; `.card-copy-ref` on all plugin cards; outlier status cleared |
| [`agents.html`](agents.html) | Agent Team — Cheat Sheet | 0.2.1 | `/00_Prompts/BDOS/00_AGENTS_INDEX.md` (primary, 8s poll) + `/.claude/commands/<cmd>.md` (lazy, per-drawer-open) | cheat-sheet / card-grid + clickable detail drawer | ✅ live | ✅ DS 0.3.0 — dark theme toggle + canonical dark tokens; `.card-copy-ref` on all agent cards; new: clickable agent cards open right-side drawer with full detail + per-slash-command descriptions + examples |
| [`sage/index.html`](sage/index.html) | Sage — Cognition Curator | 0.5.1 | `/00_Prompts/BDOS/agents/sage/state/last_run.md` + `/02_Areas/Personal Growth/Ideas/00_INDEX.md` + individual thought/atomic files (lazy) + `_journal/YYYY-MM.md` + `curate/YYYY-Www.md` + `learnings/00_INDEX.md` | multi-file (last_run primary + per-record thoughts/atomic lazy) | ✅ live | ✅ DS 0.3.0 — dark theme toggle + canonical dark tokens; `.card-copy-ref` on thought + atomic + inbox cards; graceful never_run empty-state on all 9 panels |
| [`maestro/index.html`](maestro/index.html) | Maestro — BDOS Observatory | 0.5.1 | `/00_Prompts/BDOS/00_AGENTS_INDEX.md` + `/00_Prompts/BDOS/agents/*/logs/operational/*.md` + `.../logs/learning/*.md` + `.../logs/version/*.md` (Phase 2.B pending) + `/02_Areas/Personal Growth/Ideas/_journal/YYYY-MM.md` (Sage legacy alias) | multi-source log aggregation (YAML block parser — bdos.*.log.v1 schemas) | ✅ live | ✅ DS 0.3.0 — dark theme toggle + canonical dark tokens; `.card-copy-ref` on agent + learning cards; graceful Phase-2.B empty-state on all log-driven panels; Phase 2.C token-intel placeholder |
| [`presto/index.html`](presto/index.html) | Presto — Marketing Observatory | 0.5.1 | `/_dashboards/00_MARKETING_INDEX.md` + `/02_Areas/*/Marketing/Pipeline.md` + `.../Campaigns/<slug>/CAMPAIGN.md` + `.../Results-*.md` + `/00_Prompts/BDOS/agents/presto/audience-learnings/active\|proposals\|retired/*.md` + `.../reflections/*.md` + `.../discovery/*.md` + `/02_Areas/Personal Growth/Ideas/_inbox/sage-signals/*.md` | multi-source: campaign frontmatter + section parser + presto.sage-signal.v1 schema | ✅ live | ✅ DS 0.3.0 — dark theme toggle + canonical dark tokens; `.card-copy-ref` on campaign + learning + discovery + signal cards; graceful Phase-2.B empty-state; area-identity color tokens (dh/cps/exar/nav/ignis); learning-type color tokens (8 types); Phase 2.C token-intel placeholder |
| [`librarian/index.html`](librarian/index.html) | Librarian — Knowledge Manager | 0.5.1 | `/00_INDEX.md` + `/00_KNOWLEDGE_MAP.md` + `/00_OPEN_QUESTIONS.md` + `/00_GAPS.md` + `/00_Prompts/BDOS/00_AGENTS_INDEX.md` (tier-2 table) + `/00_Prompts/BDOS/agents/librarian.md` | multi-file: index frontmatter + section parser + tier-2 table regex | ✅ live | ✅ DS 0.3.0 — dark theme toggle + canonical dark tokens; Lora serif headings (library tone); graceful Phase-2.B empty-state on activity panel; tier-2 freshness dots (fresh/stale/very-stale) |
| [`curator/index.html`](curator/index.html) | Curator — Dashboard Family | 0.5.1 | `/_dashboards/00_DASHBOARD_INDEX.md` + `/_dashboards/_design/DESIGN_SYSTEM.md` + `/00_Prompts/BDOS/agents/curator.md` | multi-file: dashboard family table parser + audit log parser + DS version parser | ✅ live | ✅ DS 0.3.0 — dark theme toggle + canonical dark tokens; self-referential ("I am the dashboard about dashboards"); graceful Phase-2.B empty-state on mode frequency + audit backlog; promote history hardcoded from DS changelog |
| [`scheduler/index.html`](scheduler/index.html) | BDOS System Status | 0.1.0 | `/_dashboards/_design/agent_logs.json` (sidecar) + `http://localhost:4322/health` + `http://localhost:4321/` HEAD | infrastructure / observability | ✅ live | ✅ DS 0.5.0 — three tabs: Health (5 pills) / Jobs (scheduler state) / Logcat (filterable 5s live stream). Doubles as ops-header drawer target. |
| [`broker/index.html`](broker/index.html) | Broker — Sales Observatory | 0.5.1 | `/_dashboards/00_SALES_INDEX.md` (not yet created) + `/00_Prompts/BDOS/agents/broker.md` + `/02_Areas/*/Sales/Cohorts/*/COHORT.md` + `.../sales-learnings/active\|proposals\|retired/*.md` + `.../reflections/*.md` | multi-source: pipeline stage parser + COHORT.md frontmatter + sales-learning frontmatter | ✅ live | ✅ DS 0.3.0 — dark theme toggle + canonical dark tokens; graceful Phase-2.B empty-state on all panels; pipeline stage tokens (6 stages); area-identity tokens (family from Presto); Presto sister cross-link; Phase 2.C token-intel placeholder |

**Jelmagyarázat — DS (design-system megfelelőség):** ✅ a kanonikus token-rendszert használja · ⚠️ funkcionális extra (intentionally preserved, pending promote) · ❌ szabálysértés.

## Gyors megnyitás (serve mód)

```
http://localhost:4321/                              # launcher
http://localhost:4321/_dashboards/sales.html
http://localhost:4321/_dashboards/partnerships.html
http://localhost:4321/_dashboards/navigator.html
http://localhost:4321/_dashboards/aiops.html
http://localhost:4321/_dashboards/team.html
http://localhost:4321/_dashboards/plugins.html
http://localhost:4321/_dashboards/agents.html
http://localhost:4321/_dashboards/sage/index.html
http://localhost:4321/_dashboards/maestro/index.html
http://localhost:4321/_dashboards/presto/index.html
http://localhost:4321/_dashboards/librarian/index.html
http://localhost:4321/_dashboards/curator/index.html
http://localhost:4321/_dashboards/broker/index.html
http://localhost:4321/_dashboards/scheduler/index.html
http://localhost:4322/health                            # events_server health
```

## Pending promote — funkcionális extrák

A következő tokenek / blokkok szándékosan megmaradtak, és egy jövőbeli `promote` mód fogja eldönteni, hogy bekerülnek-e a DS-be vagy eltávolítják őket:

| Token / blokk | Hol él | Leírás |
|---|---|---|
| `--info` / `--info-tint` | navigator.html, team.html | Kék info-szín; eltérő értékek — unifikáció vagy DS-promote szükséges |
| `--shadow-3` | navigator.html | Mélység árnyék drawer-hez |
| `--prod` / `--prod-tint` | aiops.html | Exact alias of `--accent-deep`/`--accent-tint` — cleanup vagy promote |
| `--t-slow` | sales.html | Lassabb animáció-token |
| 16 pipeline-stage tokens | sales.html | `--hot`, `--warm`, `--cold`, `--contact`, `--discovery`, `--proposal`, `--won`, `--lost` + tint variánsaik |
| 13 area-brand tokens | index.html | `--branch`, `--sonrisa`, `--exar`, `--media`, `--vez`, `--ignis`, `--nav` + tint variánsaik |

*(Promoted 2026-05-22: dark-mode `:root[data-theme="dark"]` block — now canonical DS 0.3.0, rolled out family-wide.)*

## Legacy (Areas-ban, nem migrált — jövőbeli `migrate` mód)

Valódi dashboard-ok (migrálhatók):

| Fájl | Area |
|---|---|
| `02_Areas/Média Műhely/dashboard.html` | Média Műhely |
| `02_Areas/ExarLabs/dashboard.html` | ExarLabs |
| `02_Areas/ExarLabs/Clients/dashboard.html` | ExarLabs Clients |
| `02_Areas/ExarLabs/marketing/dashboard.html` | ExarLabs Marketing |
| `02_Areas/Mikado/dashboard.html` | Mikado |
| `02_Areas/Ignis Academy/dashboard.html` | Ignis Academy |
| `02_Areas/Sonrisa/Vision Corner/dashboard.html` | Sonrisa Vision Corner |
| `02_Areas/Personal Growth/Movies/dashboard.html` | Personal Growth / Movies |
| `02_Areas/Deák Húsüzlet/BIN/dashboard.html` | Deák Húsüzlet BIN |
| `02_Areas/Sonrisa/CPS/Strategy/dashboard.html` | CPS Strategy |
| `01_Projects/Gergely István/Dashboard_2025.html` | Gergely István |
| `04_Archive/Ignis/AI Kurzus/dashboard.html` | Ignis AI Kurzus (archive) |

Nem-dashboard HTML (microsites, design assets — nem migrálhatók, nem is kell):

`02_Areas/Deák Húsüzlet/Marketing/szorolap_a5.html` · `02_Areas/Sonrisa/CPS/Marketing/CPS.html` · `02_Areas/Sonrisa/CPS/Marketing/selvio/*.html` · `02_Areas/Ignis/AI Course HBC/Pozicionalas/04_one-pager_v0.1.html` · `02_Areas/ExarLabs/design/fb-cover.html` · `02_Areas/ExarLabs/design/fb-post-microsite.html` · `02_Areas/ExarLabs/brand/fb-cover.html`

## Karbantartási napló

| Dátum | Művelet | Dashboard | Megjegyzés |
|---|---|---|---|
| 2026-05-22 | bootstrap | (mind) | Curator v0.2 — index létrehozva, 7 family-tag felmérve. |
| 2026-05-22 | survey (regenerate) | (mind) | Teljes újraszkennelés: adatforrások, verziók, home-link, launcher-reg, DS-drift pontosítva. Legacy HTML-ek felderítve (12 dashboard + 7 nem-dashboard asset). |
| 2026-05-22 | tend (align drift) | sales.html | `--shadow-2` és `--t-med` javítva DS 0.1.0-ra; version pill hozzáadva; 0.7.0 → 0.7.1. |
| 2026-05-22 | tend (align drift) | aiops.html | h1 type scale javítva DS 0.1.0-ra (clamp + letter-spacing); 0.1.0 → 0.1.1. |
| 2026-05-22 | tend (align drift) | index.html | Comment verzió szinkronizálva pill-hez; kanonikus status token csoport hozzáadva; area-brand tokenek megőrizve; plugins.html regisztrálva; 0.5.0 → 0.6.1. |
| 2026-05-22 | tend (review + note) | navigator.html | DS 0.1.0 ellen ellenőrizve; funkcionális extrák (--info, dark-mode) szándékosan megőrizve pending promote; 0.1.0 → 0.1.1. |
| 2026-05-22 | tend (review + note) | team.html | DS 0.1.0 ellen ellenőrizve; funkcionális extra (--info) szándékosan megőrizve pending promote; 0.1.0 → 0.1.1. |
| 2026-05-22 | migrate | plugins.html | Dark theme → DS 0.1.0 light tokenek; home button + version pill + audit trail hozzáadva; launcherben regisztrálva; 0.1.0 indulóverzió. Live-fetch wiring deferred. |
| 2026-05-22 | build | agents.html | Agent Team cheat sheet v0.1.0. Forrás: 00_AGENTS_INDEX.md (## Active agents). Kártya-grid: 3 agent (Librarian, Maestro, Curator). Mode chips, copyable slash-command chips, copyable példa-hívás sorok, autonómia callout, closing summary band. SSE + 8s poll. Launcherben regisztrálva (standalone row). DS 0.1.0 aligned. |
| 2026-05-22 | promote | (family-wide) | DS 0.1.0 → 0.2.0: `.card-copy-ref` + `data-card-id` konvenció bevezetve. Rollout mind a 8 dashboardra: agents 0.1.0→0.1.1, partnerships 0.2.0→0.2.1, aiops 0.1.1→0.1.2, team 0.1.1→0.1.2, plugins 0.1.0→0.1.1, navigator 0.1.1→0.1.2, index 0.6.2→0.6.3, sales 0.7.1→0.7.2. Ref formátum: `<stem>:<card-id>`. `overflow:visible` fix alkalmazva a stripe-os kártyákon. |
| 2026-05-22 | promote | (family-wide) | DS 0.2.0 → 0.3.0: canonical dark theme tokens + `.theme-toggle` + shared `dash-theme` localStorage key + FOUC-init + system-aware default. Rollout mind a 8 dashboardra: index 0.6.3→0.6.4, sales 0.7.2→0.7.3, partnerships 0.2.1→0.2.2, navigator 0.1.2→0.1.3 (bespoke impl replaced), aiops 0.1.2→0.1.3, team 0.1.2→0.1.3, plugins 0.1.1→0.1.2 (outlier status cleared), agents 0.1.1→0.1.2. Pipeline-stage + area-brand + industry tag dark variants added. `plugins.html` dark-theme outlier status cleared — now canonical family member. |
| 2026-05-24 | tend | agents.html | 0.1.2 → 0.2.0 (minor): clickable agent cards with right-side detail drawer (sales.html pattern). Card collapsed view uses Pozíció one-liner. Drawer sections: header (name+version+status+close), Pozíció, Capabilities detail, Felelősség, Autonómia callout, mode chips, per-slash-command rows (lazy-fetched from /.claude/commands/*.md — description + example, cached in JS memory). Keyboard-accessible (role=button, tabindex, Enter/Space, Esc, scrim-click). stopPropagation on .card-copy-ref preserved. Drawer non-destructive on live poll (cards only re-render when drawer is closed). Server confirmed to serve .claude/ files (HTTP 200). |
| 2026-05-24 | build | sage/index.html | 0.1.0 initial build. First per-agent dashboard in BDOS family. 9 panels: header status strip, last harvest, last curate, thoughts feed (live from individual .md files via 00_INDEX wikilinks), atomic grid, inbox (uncertain thoughts + atomic proposals), learnings meta-cognition panel with preamble token bar, journal timeline (YAML block parser), weekly curate highlights. Zero hardcoded content. Graceful never_run empty-state on every panel. DS 0.3.0 aligned. Registered in launcher (standalone/sage). index.html → 0.6.5. |
| 2026-05-24 | tend | index.html | 0.6.5 → 0.7.0 (minor: new feature). Top-level tab switcher added: Tab 1 "Areas" (existing hierarchy, intact) + Tab 2 "Agents" (D3.js v7 force-directed graph of BDOS agent family). Tab state persists in URL fragment (#areas / #agents). Agents graph reads live from /00_Prompts/BDOS/00_AGENTS_INDEX.md (8s poll + SSE). 15 static edges from canonical relationship map. Agent node cards: name, 5-word description, version badge, status dot. Sage card links to /_dashboards/sage/index.html (live). All other cards open a "coming soon" modal with Sage reference link. Right-side detail panel shows connections + open button. Empty-state graceful. Re-renders on theme toggle. Broker auto-appears when added to AGENTS_INDEX. |
| 2026-05-24 | build | presto/index.html | 0.1.0 initial build. Third per-agent dashboard. Marketing Observatory + Campaign Command Center + Reflection System. 10 panels: Phase 2 banner, campaign ops (active campaigns + 7-day schedule + approval queue), multi-project navigation (area color identity + platform chips), analytics + audience intelligence (atomic cross-links, resonance table, platform effectiveness), strategic reflection (weekly/monthly + drift indicators), content lineage (Sage→adapt→publish→analytics→signal thread), operational intelligence (Phase 2.C placeholder), audience learnings (8-type meta-cognition + proposals), discovery panel (4-filter status grid), Sage-signal flow (presto.sage-signal.v1). Schema-aware parsers: CAMPAIGN.md frontmatter, Results-*.md, presto.sage-signal.v1, audience-learning frontmatter. Area-identity tokens + learning-type tokens (local extensions). Graceful Phase-2.B empty-state on all panels. Launcher 0.7.1→0.7.2; AGENT_DASHBOARD_URLS updated (presto live). DS 0.3.0 aligned. |
| 2026-05-24 | build | maestro/index.html | 0.1.0 initial build. Second per-agent dashboard in BDOS family. Phase 2 Reflective Nervous System era (CONSTITUTION_PHASE_2.md §D). 6 panels: Phase 2 banner (rollout state 2.A/2.B/2.C), Agent Overview (family grid + recent activity feed), Time Navigation (weekly/monthly comparison + version timeline), Token Intelligence (Phase 2.C placeholder — all fields null, schema note), Organizational Intelligence (static dependency graph + bottleneck/risk signals), Evolution Tracking + Reflection Layer ("What did the system learn?" — open/actioned learnings with type chips). Schema-aware YAML block parser (bdos.operational.log.v1, bdos.learning.log.v1, bdos.version.log.v1 per LOG_SCHEMAS.md). Graceful Phase-2.B empty-state on every log-driven panel. Sage legacy journal alias noted. Zero hardcoded operational state. DS 0.3.0 aligned. Registered in launcher (standalone/maestro). index.html → 0.7.1. AGENT_DASHBOARD_URLS updated (maestro now live). |
| 2026-05-24 | build | librarian/index.html | 0.1.0 initial build. Knowledge Manager Observatory. 9 panels: header strip (total files indexed, tier-2 count, freshness), tier-1 PARA distribution, knowledge map domains, tier-2 scoped units table (11 units, freshness dots — fresh/stale/very-stale), tier-2 candidates (Ignis Academy 22, Média Műhely 21), open questions, gaps, recent activity (Phase 2.B empty), 6 modes reference. Lora serif headings (library/archivist tone). Tier-2 table parsed from 00_AGENTS_INDEX.md regex. DS 0.3.0 aligned. Registered in launcher (standalone/librarian). index.html → 0.7.3. AGENT_DASHBOARD_URLS updated (librarian now live). |
| 2026-05-24 | build | curator/index.html | 0.1.0 initial build. Self-referential Dashboard Family Observatory ("I am the dashboard about dashboards"). 9 panels: header strip (family count live from index, launcher version, DS version, Curator version), dashboard family grid (all 15 dashboards, self-highlighted with "← you are here"), DS overview (6 token groups, 7 laws, last promoted), mode frequency (Phase 2.B empty), 7 modes reference, audit backlog (0 findings), promote history (DS 0.1.0–0.3.0 changelog), server status (port 4321), recent builds (parsed from audit log). Dashboard family table parser + audit log section parser. DS 0.3.0 aligned. Registered in launcher (standalone/curator). AGENT_DASHBOARD_URLS updated (curator now live). |
| 2026-05-24 | tend (multi-target) | index.html + 6 per-agent dashboards | Avatar + Capabilities tend (0.7.4 / 0.2.0). All 7 dashboards: (1) emoji avatar circle in masthead — fetched live from AGENT_PROFILES.md, 8s poll, no hardcoded values. (2) Capabilities panel — 7 subsections: Tools, MCPs, APIs, Plugins, Own commands (copyable chips), Can invoke, Test access trace. parseAgentProfile() regex parser shared across all files. Launcher (0.7.3→0.7.4): avatar circles on all 6 graph nodes + capability summary chips (tools/MCPs/APIs/plugins count) in click detail panel. Per-agent dashboards (0.1.0→0.2.0): librarian, maestro, curator, sage, presto, broker. Curator special: renderDashFamily() enriched — per-card avatar chip from gAvatarMap. AGENT_PROFILES.md single source of truth — no emoji or color hardcoded in any HTML/JS. |
| 2026-05-24 | build | broker/index.html | 0.1.0 initial build. Sales Engine Observatory for BDOS Broker v0.2. 10 panels: header strip (active cohorts, total leads, win rate), cross-project pipeline (6 stage cards), today's actions queue, active cohorts grid (area-identity color tokens), conversion funnel (empty state), sales learnings (8-type lifecycle meta-cognition with active/proposed/retired counts), outreach drafts (empty), reflection panel (empty), Presto sister cross-link (distribution layer duality), operational intelligence (Phase 2.C placeholder). Pipeline stage tokens (qualification/discovery/proposal/negotiation/won/lost). Area-identity tokens (family from Presto). Graceful Phase-2.B empty-state on all panels. DS 0.3.0 aligned. Registered in launcher (standalone/broker). AGENT_DASHBOARD_URLS updated (broker now live). All 6 agent nodes in graph now link to live dashboards. |
| 2026-05-24 | promote | (family-wide, 7 dashboards) | DS 0.3.0 → 0.4.0: Live Update Pattern v0.2 (event-driven SSE replaces 8s polling). Header status indicator (`.live-status` pill: active/polling/inactive). Shared helper `_design/live-updates.js` (10KB, single source of truth). Dedicated `events_server.py` on port 4322 (clean separation from dash-server.mjs). All 7 dashboards refactored: launcher 0.7.4→0.7.5, sage/maestro/curator/presto/librarian/broker 0.2.0→0.3.0. Polling fallback preserved (auto-trigger after 3s SSE-fail). Sub-second update latency. Curator v0.4→v0.5. |
| 2026-05-24 | build (infra) | (observability stack) | Phase B — Agent Observability Stack. Created `agent_observability.db` (SQLite WAL, FTS5, 13 indices, triggers) in `cache/`. Written `agent_log.py` (writer API: `log_event()`, `AgentLogger` class, model cost table, atomic sidecar refresh). Written `agent_log_query.py` (reader API: 12 filter primitives, `agent_summary()`, `global_stats()`, FTS5 search). Seeded 34 test rows (8 scenarios, all 6 agents). Sidecar JSON: `_design/agent_logs.json` (19,826 bytes, last-500-events export). Write p50=4.8ms, p95=13.5ms. All query latencies <3ms. |
| 2026-05-24 | tend | maestro/index.html | 0.3.0 → 0.4.0. Logcat global tab added (Observatory tab preserved). 6 cross-agent summary cards. Full filter strip: agent, project, level, event_type, time range, model, tool, token threshold, duration threshold, text search, error-only, slow-op (12 chip groups). Logcat table: ts, agent, mode, project, level, event_type, message, model, tokens, cost, duration. URL hash persistence (#observatory / #logcat). Wired to `_design/agent_logs.json` sidecar (change-on-diff guard via `generated_at`). |
| 2026-05-24 | tend | librarian/index.html | 0.3.0 → 0.4.0. Logs panel added: 6 summary cards (token totals, avg duration, error count, recent events, slowest op, highest-token op). Scoped to LOGS_AGENT='librarian'. 9 seed rows visible. Wired to sidecar; LiveUpdates.subscribe() extended. |
| 2026-05-24 | tend | sage/index.html | 0.3.0 → 0.4.0. Logs panel added. Scoped to LOGS_AGENT='sage'. 4 seed rows visible. Wired to sidecar. |
| 2026-05-24 | tend | curator/index.html | 0.3.0 → 0.4.0. Logs panel added. Scoped to LOGS_AGENT='curator'. 9 seed rows visible. Wired to sidecar. |
| 2026-05-24 | tend | presto/index.html | 0.3.0 → 0.4.0. Logs panel added. Scoped to LOGS_AGENT='presto'. 4 seed rows visible. Wired to sidecar. |
| 2026-05-24 | tend | broker/index.html | 0.3.0 → 0.4.0. Logs panel added. Scoped to LOGS_AGENT='broker'. 4 seed rows visible. Wired to sidecar. |
| 2026-05-24 | promote (Phase B) | all 15 + 1 new | DS 0.4.0 → 0.5.0. BDOS Job Scheduler: `scheduler.py` + `scheduler_schema.sql` (schema v1.3 — `scheduled_jobs` + `job_runs`). `events_server.py` wired with `scheduler_loop()` daemon thread (60s scan). `ops-header.js` shared helper. `scheduler/index.html` (Health/Jobs/Logcat). Ops-header injected into all 15 existing dashboards (version bumps: index 0.7.5→0.8.0, sales 0.7.3→0.7.4, partnerships 0.2.2→0.2.3, navigator/aiops/team 0.1.3→0.1.4, agents 0.2.0→0.2.1, plugins 0.1.2→0.1.3, sage/maestro/librarian/curator/presto/broker 0.5.0→0.5.1). Sage plist unloaded + removed. Sage daily/weekly jobs seeded in `scheduled_jobs`. device_id generated at `~/.bdos/device_id`. |
| 2026-05-24 | tend (schema realign, family-wide) | maestro + 6 agent dashboards | 0.4.0 → 0.5.0 (all 7). Schema v1.2 realignment: `agent_events`→`agent_logs` table, `log_level` replaces `level`, `agent_name` replaces `agent`, `input_tokens`/`output_tokens`/`total_tokens` replace `tokens_in`/`tokens_out`, `timestamp` replaces `ts`, `task_id` replaces `session_id`, `status` replaces `outcome`. 15 event_type vocabulary (was 8). 6 log_level vocabulary (`notice`/`warning`/`critical` replace `info`/`warn`/`fatal`). Maestro logcat: filter chips, column headers, JS fully updated; `Q ms` column added for `query_duration_ms`; 10-column layout. Librarian: slowest-query callout box, `Q ms` column header + cell rendering. All 6 agent per-page logs panels updated. DB verified: `agent_logs` table, 28 columns, 34 migrated rows, FTS5 on title+message. |
| 2026-05-24 | canonical update (Phase C) | (all 6 agent canonicals + registrations) | Phase C documentation pass complete. `## Scheduling v1` section added to all 6 agent canonical files. Patch bumps: Librarian 0.8.2→0.8.3, Maestro 0.5.2→0.5.3, Curator 0.5.2→0.5.3, Sage 0.4.2→0.4.3, Presto 0.5.2→0.5.3, Broker 0.3.2→0.3.3. All 6 registration files lockstep synced. `CONSTITUTION_PHASE_6.md` written (scheduler control plane, launchd deprecation, multi-device SQLite locks, 9 job states, requires_approval semantics, scheduler tag taxonomy). `LOG_SCHEMAS.md` bumped 1.2→1.3 (§0.S scheduler tag-discriminator + §0.J DDL cross-reference). `00_AGENTS_INDEX.md` maintenance logs updated with new patch versions. Scheduler family rollout complete. |
