---
title: "Strategic positioning — Pillar 1 of CPS AI-Native OS direction"
date: 2026-05-27
status: active
description: "Practice-area scoped excerpt from the broader CPS AI-Native OS strategy doc. Positions Inference Farm / Sonrisa LLMaaS as Pillar 1 (the 'kernel') of a three-pillar AI-Native OS direction. Source-of-truth is the parent strategy doc — this is a scoped summary + cross-link for practice-area discoverability."
practice_area: cps-inference-farm
type: strategic-context
audience: internal-strategy
provenance: "extracted from 02_Areas/Sonrisa/CPS/Strategy/AI Ops/01_STRATEGY.md on 2026-05-27 — that file remains the canonical strategy source-of-truth"
id: 7f1c4b89-3e62-4d57-8a14-2c5d0f9a7b48
index_schema_version: 1
bdos_index: false
---

# Inference Farm — Strategic Positioning

> **Pillar 1 of the CPS AI-Native Operating System strategic direction.** The Inference Farm / Sonrisa LLMaaS is positioned as the **"kernel"** of the broader AI-native OS — a private, EU-sovereign, OpenAI-compatible runtime on AWS GPU. **Live in production.**

## The 3-pillar strategy

CPS evolves from managed cloud platform services into an **AI-Native Operating System for companies**. Three already-started pillars:

| Pillar | What it is | Maturity | First proof |
|---|---|---|---|
| **1. Inference Substrate** | Sonrisa LLMaaS, private LLM runtime on AWS GPU (Qwen-32B, DeepSeek, Llama). OpenAI-compatible, token-billed, EU-resident. | **Live in production** (AWS acct 382113323075, ~$863/mo) | Internal + 3-5 external pilots targeted |
| **2. Agentic AIOps** | Catalog of autonomous ops agents on a Hermes/OpenClaw orchestration layer, deployed into client cloud, time-boxed per agent with KPI acceptance. | **Productized (priced)**, not yet shipped to a paying client | CCHBC sub-bid (Magyar Telekom) Tier model |
| **3. FinOps Automation** | Cost intelligence + autonomous rightsizing, outcome-tied savings bonus. | **Service exists**, AI-automation layer is the new part | Free cost-optimization assessment funnel |

## Architecture position

```
  ┌─────────────────────────────────────────────────────────────┐
  │  PILLAR 1 — INFERENCE SUBSTRATE  (the "kernel")             │
  │  Sonrisa LLMaaS / Inference Farm. Private, EU-sovereign,    │
  │  OpenAI-compatible runtime on AWS GPU. Live in production.  │
  └─────────────────────────────────────────────────────────────┘
              ↑                              ↑
              │                              │
  Pillar 2: Agentic AIOps          Pillar 3: FinOps Automation
  (consumes substrate              (consumes substrate
   for agent inference)              for cost intel agents)
```

## Why Pillar 1 (Inference Substrate) matters for the OS

The inference substrate is the **foundation that makes the rest of the AI-Native OS possible**:

- **Private LLM endpoint** — no public LLM = EU + regulated sector compatible
- **OpenAI-compatible API** — existing tooling works (LangChain, LlamaIndex, custom code)
- **Token-billed** — predictable economics for clients
- **AWS GPU substrate** — G5.12XL family, auto-scaling, EU-resident

Other pillars (Agentic AIOps, FinOps Automation) **depend on this substrate** — Tier-1 agents call into it for inference. Without Pillar 1, Pillars 2-3 lose the "private/sovereign" promise.

## Open strategic questions (from parent doc)

The CPS AI-Native OS strategy currently has these unresolved questions touching Inference Farm:

- **Substrate go-to-market**: is LLMaaS sold standalone, bundled into the OS, or both?
- **Default commercial shape**: adopt the CCHBC hybrid model (retainer + fixed-fee per agent + outcome bonus) as the standard for ALL AI-native engagements?
- **Capacity gate**: what is the hiring trigger (how many signed engagements) before we staff beyond 2.5 FTE?
- **Beachhead**: is CCHBC the lighthouse account for the whole direction, or one of several? Where does Merkantil fit?

These should also be tracked in the practice's [[../open-questions|open-questions.md]] under "Strategic" category.

## Canonical reference

Full strategy document (source of truth): [[../../../Strategy/AI Ops/01_STRATEGY|CPS AI-Native OS Strategy v0.1.0]]

Related pillar references from the parent strategy:
- **Agentic AIOps tier model** — `02_Areas/Sonrisa/CPS/Accounts/Leads/CCHBC/brainstorm_cchbc-aiops-tiers.md`
- **FinOps service** — `02_Areas/Sonrisa/CPS/Services/Cost optimization/`
