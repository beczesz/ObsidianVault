---
title: CPS AI-Native Operating System — dashboard source
date: 2026-05-22
author: Becze Szabolcs
status: draft
version: 0.1.0
description: Single-frontmatter data source for the AI Ops strategy dashboard (_dashboards/aiops.html). Edit this file in Obsidian; the dashboard re-renders live. Three pillars + open strategic questions. Canonical strategy doc is 01_STRATEGY.md in this folder.
direction_name: "AI-Native Operating System"
direction_tagline: "CPS runs your AI layer, not just your infrastructure."
direction_status: forming
beachhead: "CCHBC / Magyar Telekom (Agentic AIOps sub-bid)"
strategy_doc: "02_Areas/Sonrisa/CPS/Strategy/AI Ops/01_STRATEGY.md"
pillars:
  - name: "Inference Substrate"
    layer: "The kernel"
    status: live
    accent: "#1f7a4d"
    maturity: "Live in production"
    summary: "Sonrisa LLMaaS. Private, EU-sovereign, OpenAI-compatible LLM runtime on AWS GPU (Qwen-32B, DeepSeek, Llama). Token-billed, 40-70% cheaper than public APIs. The runtime the agents and clients run on."
    metrics:
      - label: "AWS spend"
        value: "$863/mo"
      - label: "Pricing"
        value: "EUR 500-5,000/mo"
      - label: "Pilots targeted"
        value: "3-5 external"
    next_actions:
      - "Land 1 referenceable paying customer to anchor the cost-savings story"
      - "Decide: sell standalone, bundle into the OS, or both"
    source_files:
      - "02_Areas/Sonrisa/CPS/Services/Inference Farm/Description.md"
      - "02_Areas/Sonrisa/CPS/Services/Inference Farm/LLMaaS — ACE Opportunity Summary.md"
  - name: "Agentic AIOps"
    layer: "The processes"
    status: productized
    accent: "#D97757"
    maturity: "Priced & validated, not yet shipped"
    summary: "Catalog of autonomous ops agents (Alert Triage, RCA Drafter, Remediation, Capacity Forecaster, Deploy Verifier, FinOps Optimizer) on a Hermes/OpenClaw orchestration layer, deployed into client cloud. Time-boxed per agent with KPI acceptance. The headline of the direction."
    metrics:
      - label: "Tier 2 (default)"
        value: "EUR 280-400k/yr"
      - label: "Sonrisa FTE"
        value: "2-2.5"
      - label: "Risk"
        value: "Medium"
    next_actions:
      - "Default to Tier 2 (Agent Builder) shape; gate 24/7 operation as add-on"
      - "Ship the first agent to a paying client (CCHBC lighthouse)"
      - "Position as Davis-extender, not AIOps-engine replacement"
    source_files:
      - "02_Areas/Sonrisa/CPS/Accounts/Leads/CCHBC/brainstorm_cchbc-aiops-tiers.md"
  - name: "FinOps Automation"
    layer: "The resource manager"
    status: service
    accent: "#b07a18"
    maturity: "Service exists, automation layer is new"
    summary: "Cost intelligence plus autonomous rightsizing: tagging enforcement, chargeback dashboards, automated rightsizing actions, outcome-tied savings bonus (1-2% of validated savings, capped). Closes the cost loop automatically."
    metrics:
      - label: "FinOps add-on"
        value: "EUR 500/mo"
      - label: "Outcome bonus"
        value: "1-2% savings"
      - label: "Funnel"
        value: "Free assessment"
    next_actions:
      - "Wire the automation layer onto the existing assessment funnel"
      - "Define the chargeback + rightsizing acceptance criteria as standard"
    source_files:
      - "02_Areas/Sonrisa/CPS/Services/Cost optimization/CLAUDE.md"
open_questions:
  - "Naming: internal direction name + client-facing offer name (blocked on ChatGPT thread review)"
  - "New business line or evolution of CPS managed services?"
  - "Adopt the CCHBC hybrid model (retainer + per-agent fixed fee + outcome bonus) as the standard?"
  - "Capacity gate: how many signed engagements before staffing beyond 2.5 FTE?"
  - "Is CCHBC the lighthouse for the whole direction, or one of several?"
---

# AI-Native Operating System — dashboard source

This file feeds `_dashboards/aiops.html`. Edit the frontmatter above in Obsidian; the
dashboard re-renders within 8 seconds (instantly when the SSE file-watcher server is running).

The narrative strategy lives in [01_STRATEGY.md](01_STRATEGY.md). This file is the structured
snapshot the board renders. Keep the two in sync when the direction evolves.

**Status legend:** `live` = in production, `productized` = priced and validated but not yet
shipped to a paying client, `service` = existing service line, `concept` = idea stage.
