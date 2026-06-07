---
title: BDOS Agent Profiles — Avatars + Capability Inventory
date: 2026-05-24
author: Becze Szabolcs
status: active
version: 1.0
description: Single source of truth a BDOS agent-család vizuális identity-jéhez (avatar emoji + szín) és teljes capability inventory-jához (tools, connectors, MCPs, APIs, plugins, skills, test access trace). 7 aktív agent (Librarian, Maestro, Curator, Alfred, Presto, Broker, Forge) + Sage deprecated section. Dashboardok élőben olvassák.
tags: [BDOS, agents, profiles, capabilities, inventory]
id: f7c9e525-7334-4140-ba2a-8f9f06a1835b
index_schema_version: 1
---

# BDOS Agent Profiles

> **Source of truth** a 6 aktív agent vizuális identity-jéhez és capability inventory-jához. Dashboardok élőben fetchelik. Új capability vagy MCP érkezésekor itt frissítsük — a dashboardok automatikusan követik.

---

## Schema

Minden agent egy YAML-blokk a `## <Agent>` szekció alatt:

```yaml
avatar:
  emoji: <single emoji>
  color: <hex>           # color identity (cards, accents)
  fallback_svg: <path>   # opcionális, ha SVG-vé upgrade-eljük

capabilities:
  tools:                 # registration `tools:` field
    - Read
    - Write
    ...
  connectors_mcp:        # MCP servers / connectors
    - <name>
  apis:                  # API providers (direct or via Thinking Engine)
    - <provider>
  plugins:               # Cowork plugins, skill packs
    - <plugin>
  skills:                # slash commands + skills it can invoke
    own_commands_count: <N>
    can_invoke: [<skill names>]
  test_access_trace:     # what's been accessed in operational logs
    last_updated: <date>
    chrome_mcp_used: <bool>
    thinking_engine_used: <bool>
    plugin_skills_invoked: [<list>]
```

---

## Librarian

```yaml
avatar:
  emoji: "📚"
  color: "#8B6F4E"   # warm parchment brown
  symbolism: "books — knowledge keeper, archivist"

capabilities:
  tools:
    - Read
    - Write
    - Edit
    - Glob
    - Grep
    - Bash
  connectors_mcp:
    - filesystem (via Bash + Read/Write)
  apis: []
  plugins:
    - poppler (pdftotext for PDF reading — v0.5 capability)
  skills:
    own_commands_count: 6
    own_commands:
      - /lib-index
      - /lib-find
      - /lib-tidy
      - /lib-audit
      - /lib-integrate
      - /lib-deepclean
    can_invoke: []  # Librarian doesn't invoke other agents/skills
  test_access_trace:
    last_updated: 2026-05-24
    chrome_mcp_used: false
    thinking_engine_used: false
    plugin_skills_invoked: []
    operational_logs_observed: 0  # not yet operationally active in Phase 2 era
```

---

## Maestro

```yaml
avatar:
  emoji: "🎼"
  color: "#6B5B95"   # deep purple — gravitas, orchestration
  symbolism: "conductor sheet — orchestrates, partitúrát olvas"

capabilities:
  tools:
    - Read
    - Write
    - Edit
    - Glob
    - Grep
    - Bash
  connectors_mcp:
    - filesystem
  apis: []
  plugins:
    - brand-toolkit (Brand Spine domain reference)
  skills:
    own_commands_count: 10
    own_commands:
      - /maestro (legacy)
      - /maestro-status
      - /maestro-next
      - /maestro-continue
      - /maestro-start
      - /maestro-audit
      - /maestro-team-status
      - /maestro-team-audit
      - /maestro-team-promote
      - /maestro-team-introduce
      - /maestro-observe (v0.3+ Phase 2)
      - /maestro-reflect
      - /maestro-optimize
    can_invoke:
      - "all agent canonicals via team-promote"
      - "AGENTS_INDEX self-updating"
  test_access_trace:
    last_updated: 2026-05-24
    chrome_mcp_used: false
    thinking_engine_used: false
    plugin_skills_invoked: []
    operational_logs_observed: 1   # first observe+reflect run today
```

---

## Curator

```yaml
avatar:
  emoji: "🖼️"
  color: "#7BA098"   # sage green — curation, calm exhibition
  symbolism: "frame — curates representations, exhibits"

capabilities:
  tools:
    - Read
    - Write
    - Edit
    - Glob
    - Grep
    - Bash
  connectors_mcp:
    - filesystem
    - local HTTP server (port 4321 — dashboard serve)
  apis: []
  plugins:
    - d3.js (via CDN, in built dashboards)
  skills:
    own_commands_count: 7
    own_commands:
      - /dash-survey
      - /dash-build
      - /dash-tend
      - /dash-retire
      - /dash-audit
      - /dash-serve
      - /dash-promote
    can_invoke: []
  test_access_trace:
    last_updated: 2026-05-24
    chrome_mcp_used: false
    thinking_engine_used: false
    plugin_skills_invoked: []
    operational_logs_observed: 0   # built 15 dashboards but pre-logging in their session
    dashboards_built_today: 6      # Sage, Maestro, Presto, Librarian, Curator, Broker
```

---

## ~~Sage~~ (DEPRECATED 2026-05-28, merged into Alfred v0.3)

Capabilities absorbed into Alfred. The profile below is kept for historical reference only. Alfred is the active source of truth for cognition.

```yaml
# DEPRECATED 2026-05-28 — see Alfred section below
avatar:
  emoji: "🦉"
  color: "#5B7C99"   # twilight blue — wisdom, contemplative night
  symbolism: "owl — wisdom, low-noise high-signal observation"

capabilities:
  tools:
    - Read
    - Write
    - Edit
    - Glob
    - Grep
    - Bash
  connectors_mcp:
    - filesystem
    - Chrome MCP (via main orchestrator — for ChatGPT Referencia chat reads)
  apis: []
  plugins: []
  skills:
    own_commands_count: 14
    own_commands:
      - /sage-status
      - /sage-harvest
      - /sage-curate
      - /sage-summary
      - /sage-find
      - /sage-chat
      - /sage-edit
      - /sage-promote
      - /sage-index
      - /sage-learnings
      - /sage-learning-accept
      - /sage-learning-reject
      - /sage-learning-retire
      - /sage-learning-edit
    can_invoke:
      - "Librarian retrieve (weekly curate, via main Claude)"
  test_access_trace:
    last_updated: 2026-05-24
    chrome_mcp_used: true             # smoke test integration today
    thinking_engine_used: false
    plugin_skills_invoked: []
    operational_logs_observed: 1      # first real harvest (smoke test)
    chatgpt_chats_read: 1             # ExarLabs - AI alapú operációs rendszer
```

---

## Alfred

```yaml
avatar:
  emoji: "🧭"
  color: "#4A7B6F"   # deep teal — calm executive navigator
  symbolism: "compass — human-facing executive layer, finds direction for the user"

capabilities:
  tools:
    - Read
    - Write
    - Edit
    - Glob
    - Grep
    - Bash
  connectors_mcp:
    - filesystem
    - Chrome MCP (for ChatGPT Referencia chat harvest + Alfred Inbox sync)
  apis: []
  plugins: []
  skills:
    own_commands_count: 17
    own_commands:
      - /alf-capture
      - /alf-sync
      - /alf-today
      - /alf-status
      - /alf-todo
      - /alf-remind
      - /alf-done
      - /alf-tasks
      - /alf-harvest
      - /alf-curate
      - /alf-chat
      - /alf-learn
      - /alf-learnings
      - /alf-learning-accept
      - /alf-learning-edit
      - /alf-learning-reject
      - /alf-learning-retire
    can_invoke:
      - "Librarian retrieve (curate mode, via main Claude)"
  test_access_trace:
    last_updated: 2026-05-28
    chrome_mcp_used: true             # harvest channel (ChatGPT Referencia + Alfred Inbox)
    thinking_engine_used: false
    plugin_skills_invoked: []
    operational_logs_observed: 0      # v0.3 launched 2026-05-28; Sage historical logs in sage/ archive
  cognition_source_note: "Alfred v0.3 is the active cognition owner (Sage-merged). Scheduler jobs: alfred-daily-harvest + alfred-weekly-curate."
```

---

## Presto

```yaml
avatar:
  emoji: "🐰"
  color: "#D17A5F"   # tempo orange — speed + warm Pixar Presto reference
  symbolism: "Pixar Presto magician rabbit — transforms, adapts"

capabilities:
  tools:
    - Read
    - Write
    - Edit
    - Glob
    - Grep
    - Bash
  connectors_mcp:
    - filesystem
  apis:
    - "Thinking Engine Orchestrator (auto-invokable in discover + reflect modes only)"
    - "via Thinking Engine: Anthropic, OpenAI, Perplexity Sonar"
  plugins:
    - "Cowork marketing plugin (8 skills)"
  skills:
    own_commands_count: 16
    own_commands:
      - /pres-status
      - /pres-today
      - /pres-plan
      - /pres-run
      - /pres-resume
      - /pres-measure
      - /pres-index
      - /pres-adapt
      - /pres-reflect
      - /pres-audience
      - /pres-discover
      - /pres-learnings
      - /pres-learning-accept
      - /pres-learning-reject
      - /pres-learning-retire
      - /pres-learning-edit
    can_invoke:
      - /marketing:campaign-plan
      - /marketing:draft-content
      - /marketing:brand-review
      - /marketing:competitive-brief
      - /marketing:seo-audit
      - /marketing:performance-report
      - /marketing:email-sequence
      - /marketing:content-creation
      - "Thinking Engine Orchestrator (think-agent-orchestrator-v09)"
  test_access_trace:
    last_updated: 2026-05-24
    chrome_mcp_used: false
    thinking_engine_used: false       # authorized but not invoked this session
    plugin_skills_invoked: []         # only assessment/proposal modes ran, no draft-content
    operational_logs_observed: 2      # strategic-prep-phase-1 + distribution-proposal-editorial-taste-modeling
  sage_integration:
    # NOTE: Alfred is now the cognition owner (Sage merged into Alfred v0.3, 2026-05-28).
    # The sage-signals/ folder name is kept as-is for backward compatibility.
    permitted_flow_inbox: "02_Areas/Personal Growth/Ideas/_inbox/sage-signals/"
    can_read_sage_outputs: true
    can_write_sage_outputs: false
```

---

## Broker

```yaml
avatar:
  emoji: "🤝"
  color: "#A47551"   # leather brown — handshake, trust, deal
  symbolism: "handshake — one-to-one deal, sales trust"

capabilities:
  tools:
    - Read
    - Write
    - Edit
    - Glob
    - Grep
    - Bash
  connectors_mcp:
    - filesystem
  apis: []   # may add Thinking Engine later (v0.3+) for prospect research
  plugins: []  # dedicated sales plugin still pending
  skills:
    own_commands_count: 12
    own_commands:
      - /brk-status
      - /brk-today
      - /brk-plan
      - /brk-run
      - /brk-resume
      - /brk-measure
      - /brk-index
      - /brk-reflect
      - /brk-learnings
      - /brk-learning-accept
      - /brk-learning-reject
      - /brk-learning-retire
    can_invoke:
      - "/legal:* (ad-hoc, for contract prep)"
      - "/product-management:* (ad-hoc, for proposal/spec work)"
  test_access_trace:
    last_updated: 2026-05-24
    chrome_mcp_used: false
    thinking_engine_used: false
    plugin_skills_invoked: []
    operational_logs_observed: 0   # capability designed today but not yet operationally invoked
  sage_integration:
    # NOTE: Alfred is now the cognition owner (Sage merged into Alfred v0.3, 2026-05-28).
    # The sage-signals/ folder name is kept as-is for backward compatibility.
    permitted_flow_inbox: "02_Areas/Personal Growth/Ideas/_inbox/sage-signals/"
    can_read_sage_outputs: true
    can_write_sage_outputs: false
```

---

## Forge

```yaml
avatar:
  emoji: "🔨"
  color: "#9B4F3A"   # warm brick red — forge-fire warmth, distinct from Broker leather (#A47551) and Presto peachy orange (#D17A5F)
  symbolism: "hammer — capability forging, iterative refinement, practice stewardship"

capabilities:
  tools:
    - Read         # v0.1 expected; v0.2 finalizes
    - Write
    - Edit
    - Glob
    - Grep
    - Bash
  connectors_mcp:
    - filesystem
  apis: []         # may add Thinking Engine later (v0.3+) for cross-area pattern reflection
  plugins: []      # capability-development plugins TBD
  skills:
    own_commands_count: 0   # v0.2 design pending; reserve forge- prefix
    own_commands: []        # planned: /forge-status, /forge-today, /forge-capture, /forge-refine, /forge-index, /forge-measure, /forge-handoff, /forge-learn, /forge-reflect, /forge-learnings, /forge-learning-accept, /forge-learning-reject, /forge-learning-retire
    can_invoke: []          # cross-agent handoff to Broker / Presto via /forge-handoff (v0.2)
  test_access_trace:
    last_updated: 2026-05-27
    chrome_mcp_used: false
    thinking_engine_used: false
    plugin_skills_invoked: []
    operational_logs_observed: 0    # v0.1 just created — no operational invocation yet
  sage_integration:
    # NOTE: Alfred is now the cognition owner (Sage merged into Alfred v0.3, 2026-05-28).
    # The sage-signals/ folder name is kept as-is for backward compatibility.
    permitted_flow_inbox: "02_Areas/Personal Growth/Ideas/_inbox/sage-signals/"   # capability-gap signals (v0.2)
    can_read_sage_outputs: true
    can_write_sage_outputs: false
  broker_integration:
    handoff_flow: "practice → engagement (when pattern matures, ready for client proposal)"
    cross_link_files: ["Practices/<area>/related-projects.md"]
  practice_areas_active:
    - "02_Areas/Sonrisa/CPS/Practices/Inference-Farm/"
    - "02_Areas/ExarLabs/Practices/Microsites/"
```

---

## Cross-family summary

| Agent | Avatar | Tools | MCPs | APIs | Plugins | Own Cmds |
|---|---|---|---|---|---|---|
| Librarian | 📚 | 6 | 1 | 0 | 1 | 6 |
| Maestro | 🎼 | 6 | 1 | 0 | 1 | 10+3 |
| Curator | 🖼️ | 6 | 2 | 0 | 1 | 7 |
| Alfred | 🧭 | 6 | 2 | 0 | 0 | 17 |
| Presto | 🐰 | 6 | 1 | 3 (via TEO) | 1 | 16 |
| Broker | 🤝 | 6 | 1 | 0 | 0 | 12 |
| **Forge** | 🔨 | 6 (v0.1) | 1 | 0 | 0 | 0 (v0.2 planned: ~13) |
| ~~Sage~~ | ~~🦉~~ | DEPRECATED | | | | 14 (commands removed) |

**Family totals (7 active agents):**
- 71 own slash commands (+ ~13 planned for Forge v0.2)
- 1 family-wide API access (Thinking Engine via Presto)
- Cowork marketing plugin (Presto only)
- Chrome MCP (Alfred operative, via main orchestrator)

---

## Update protocol

- Új capability érkezésekor: frissítsd a vonatkozó agent szekciót itt
- A `test_access_trace` mezőket Maestro `observe` mód is frissítheti (vagy adhocan a session-orchestrator)
- Schema-evolúció: új mezők hozzáadhatók, törlés tilos (`AGENT_PROFILES.v2` ha major változás)

## Dashboard integráció

A Curator dashboard-családja innen olvas:
- Main launcher Agents graph — avatar a node-okon
- Per-agent dashboardok — Capabilities panel
- Curator dashboard family-grid — avatar a kártyákon

Élő fetch, auto-refresh 8s.
