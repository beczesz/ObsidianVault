---
title: CPS AI-Native Operating System — Strategic Direction
date: 2026-05-22
author: Becze Szabolcs + Think Agent Orchestrator v0.9 (Solo Claude)
status: draft
version: 0.1.0
description: Canonical strategy + brainstorm state file for the new CPS strategic direction. CPS evolves from managed cloud platform services into an AI-Native Operating System for companies. Unifies three already-started pillars (LLMaaS/Inference Farm substrate, Agentic AIOps, FinOps automation). Round 1 = Solo Claude strategist + validator pass; ChatGPT thread synthesis still pending (blocked on browser access).
tags: [cps, aiops, ai-native, strategy, brainstorm, inference-farm, llmaas]
id: 75d0547d-0860-463b-9fbe-e1589381b2a0
index_schema_version: 1
---

# CPS AI-Native Operating System — Strategic Direction

**Session:** 2026-05-22
**Driver:** Becze Szabolcs
**Round 1 status:** Solo Claude strategist + self-validator pass complete. External AI synthesis (ChatGPT thread) pending.

> Working name only. Final naming is an open question (see Open Questions). The user's working phrase is "AI Native Operating System for companies / AI Ops".

---

## Team

| AI | Role | Transport | Model / URL | Status |
|----|------|-----------|-------------|--------|
| Claude Opus 4.7 | Strategist + Orchestrator | local | claude-opus-4-7 | done |
| Claude (self) | Validator (devil's advocate) | local | claude-opus-4-7 | done |
| ChatGPT (Custom GPT, Project) | Source thread to synthesize | Browser (Chrome MCP) | [thread](https://chatgpt.com/g/g-p-67626f61e6608191b05499a1941f57cc/c/6a10422f-6584-83eb-ba78-44cce9ff59c9) | BLOCKED (browser access denied) |

Notes: API key check and Chrome browser listing were both denied by the auto-mode classifier this session, so the external team (GPT-5 / Perplexity / the ChatGPT thread) could not be activated. Round 1 ran Solo Claude per the orchestrator's "Solo Claude" preset.

---

## Context (canonical anchors)

These are the already-started pieces the new direction sits on top of:

- **Agentic AIOps tier model** (the first productized form): [../../Accounts/Leads/CCHBC/brainstorm_cchbc-aiops-tiers.md](../../Accounts/Leads/CCHBC/brainstorm_cchbc-aiops-tiers.md)
- **Inference substrate, live on AWS**: [../../Services/Inference Farm/Description.md](../../Services/Inference%20Farm/Description.md) (Sonrisa LLMaaS) + [../../Services/Inference Farm/LLMaaS — ACE Opportunity Summary.md](../../Services/Inference%20Farm/LLMaaS%20%E2%80%94%20ACE%20Opportunity%20Summary.md)
- **FinOps / cost optimization service**: [../../Services/Cost optimization/](../../Services/Cost%20optimization/)
- **Unified strategic journey (the prior roadmap this extends)**: [../Roadmap.md](../Roadmap.md)
- **Business model canvas**: [../BMC v1.3.md](../BMC%20v1.3.md)
- **CPS positioning**: Vision "We are the Backstage Crew who runs the show". Mission: Stabilitas, Innovacio, Fejlodes.

---

## The thesis (one paragraph)

CPS today sells **managed cloud platform services**: it runs other companies' AWS/Azure infrastructure. The next strategic direction is to run their **AI layer** too, as one managed program. Three pieces already exist independently and now compose into a single offering: a **private inference substrate** (LLMaaS / Inference Farm, already live on AWS at ~$863/mo), **agentic operations** (autonomous AIOps agents productized in the CCHBC tier model), and **autonomous cost economics** (FinOps automation). Put together, CPS does not just keep the infrastructure running; it operates the company's day-to-day technical operations with AI agents, on a private model runtime, with the cost loop closed automatically. That is the "operating system" claim: substrate + agents + economics, delivered and run by CPS as the backstage crew.

---

## The three pillars (the "OS" stack)

```
              AI-NATIVE OPERATING SYSTEM (CPS-run, managed)
  ┌─────────────────────────────────────────────────────────────┐
  │  PILLAR 2 — AGENTIC AIOPS  (the "processes")                  │
  │  Autonomous ops agents: Alert Triage, RCA Drafter,            │
  │  Remediation, Capacity Forecaster, Deploy Verifier,           │
  │  FinOps Optimizer. Orchestrated via Hermes/OpenClaw.          │
  │  Productized in the CCHBC Tier 1/2/3 model.                   │
  ├─────────────────────────────────────────────────────────────┤
  │  PILLAR 3 — FINOPS AUTOMATION  (the "resource manager")       │
  │  Tagging enforcement, chargeback, autonomous rightsizing,     │
  │  outcome-tied savings. Already a CPS service line.            │
  ├─────────────────────────────────────────────────────────────┤
  │  PILLAR 1 — INFERENCE SUBSTRATE  (the "kernel")               │
  │  Sonrisa LLMaaS / Inference Farm. Private, EU-sovereign,      │
  │  OpenAI-compatible runtime on AWS GPU. Live in production.    │
  └─────────────────────────────────────────────────────────────┘
        Delivered & operated by CPS  ·  300-engineer bench
        EU data sovereignty  ·  AWS-native  ·  integrated delivery
```

| Pillar | What it is | Maturity | First proof |
|---|---|---|---|
| **1. Inference Substrate** | Sonrisa LLMaaS, private LLM runtime on AWS GPU (Qwen-32B, DeepSeek, Llama). OpenAI-compatible, token-billed, EU-resident. | **Live in production** (AWS acct 382113323075, ~$863/mo) | Internal + 3-5 external pilots targeted |
| **2. Agentic AIOps** | Catalog of autonomous ops agents on a Hermes/OpenClaw orchestration layer, deployed into client cloud, time-boxed per agent with KPI acceptance. | **Productized (priced)**, not yet shipped to a paying client | CCHBC sub-bid (Magyar Telekom) Tier model |
| **3. FinOps Automation** | Cost intelligence + autonomous rightsizing, outcome-tied savings bonus. | **Service exists**, AI-automation layer is the new part | Free cost-optimization assessment funnel |

The strategic move is that these stop being three separate service descriptions and become **one program with one story**: the AI-native operating system that CPS runs for you.

---

## Why CPS can make this claim (the unfair advantages)

- **It is already running**, not a pitch deck. The substrate is live; the agent model is priced and validated by a real tender (CCHBC/MT).
- **300-engineer bench** absorbs the FTE depth that the CCHBC validator flagged as the killer for small MSPs (24/7 rotation needs 5-7 FTE).
- **EU data sovereignty + self-hosted models** is the wedge against US public-API AI; directly answers the GDPR / no-external-data-exposure objection.
- **AWS-native + partnership track** gives a co-sell and Marketplace path the AIOps line can ride on.
- **Integrated delivery story**: "we modernize, migrate, manage, AND now operate your AI" is a promise no 10-person MSP can match.

---

## Positioning evolution

- Yesterday: "Managed Cloud Platform Services. We run the show, backstage crew."
- Today's extension: **"We run your AI-native operations."** The backstage crew now also runs the AI layer, the agents, and the cost loop, on infrastructure you control.

The vision metaphor still holds and even strengthens: the company is the show on stage, CPS is the crew that makes the AI-native production run.

---

## Round 1 — Solo Claude validator pass (devil's advocate)

Honest pushback, so the direction is stress-tested before it gets resourced:

1. **Is this a real new direction or a rebrand of three existing services?**
   Risk: high if we just staple the three service PDFs together. It becomes real only if (a) the agentic layer ships to a paying client, and (b) the three pieces share one delivery motion, one runbook standard, one commercial model. Otherwise it is marketing, not strategy.

2. **Capacity is the binding constraint, not demand.**
   The CCHBC Round-1 work already flagged Tier 3 (5-7 FTE, 24/7) as too big a bet at Sonrisa's current size (13 engineers, recruitment paused). An "AI-native OS" sold broadly multiplies that. The direction must default to the **Tier 2 / Agent Builder** shape (2-2.5 FTE, time-boxed agents) and treat full 24/7 operation as a gated add-on, not the headline.

3. **Differentiation vs hyperscaler-native + Dynatrace Davis AI.**
   Much of "agentic ops" is being shipped by the platforms themselves. The defensible position is the **integration + sovereignty + outcome layer**: "Davis extender", private-model RAG on your own data, custom remediation tied to your ServiceNow, FinOps savings you actually bank. Not "we built a better AIOps engine."

4. **The substrate's economics are unproven at scale.**
   $863/mo and "3-5 pilots targeted" is pre-revenue. The 40-70% cost-savings story is real but needs one referenceable paying customer before it anchors a strategic direction.

5. **Naming risk.** "AI Ops" already means a crowded category (Gartner AIOps = ML-on-telemetry). If we name the direction "AI Ops" we inherit that narrow meaning. "AI-Native Operating System" is more ownable but vaguer. Naming needs a real decision (below), ideally informed by the ChatGPT thread the user already worked in.

**Validator's bottom line:** the direction is sound *as a unifying story over assets that already exist*, and weak *as a promise to operate everything for everyone*. Lead Tier-2-shaped, land one paying agentic engagement, get one substrate reference, then widen.

---

## Naming — candidates (OPEN, do not lock yet)

The user is undecided and has thinking in the ChatGPT thread that should be folded in first. Working candidates from this pass:

| Candidate | Reads as | Risk |
|---|---|---|
| **AI Native Operating System (AI-NOS)** | Ownable, big-tent, "the OS for the AI-native company" | Vague until the three pillars are visibly one product |
| **Agentic AIOps Program** | Already the CCHBC framing; concrete, sells today | Inherits the narrow Gartner "AIOps" meaning |
| **Sonrisa Run** / **CPS Run** | "We run your operations" verb-brand | Generic |
| **Backstage AI** | Ties to the existing "backstage crew" vision | Could read as gimmicky |

Recommendation: keep "AI-Native Operating System" as the **internal strategic-direction name** and "Agentic AIOps Program" as the **client-facing offer name** until the ChatGPT thread + a positioning round resolve it.

---

## Open questions (need user / external-AI input)

- [ ] **Naming**: internal direction name + client-facing offer name. (Blocked on ChatGPT thread review.)
- [ ] **Is this a new business line or an evolution of CPS managed services?** Affects P&L, team, and how it shows up on the website.
- [ ] **Default commercial shape**: adopt the CCHBC hybrid model (retainer + fixed-fee per agent + outcome bonus) as the standard for ALL AI-native engagements?
- [ ] **Capacity gate**: what is the hiring trigger (how many signed engagements) before we staff beyond 2.5 FTE?
- [ ] **Substrate go-to-market**: is LLMaaS sold standalone, bundled into the OS, or both?
- [ ] **Beachhead**: is CCHBC the lighthouse account for the whole direction, or one of several?

---

## Decisions log

- 2026-05-22: New strategic direction opened: "AI-Native Operating System for companies". Framed as a unification of three already-started pillars (Inference Substrate / Agentic AIOps / FinOps Automation), not a from-scratch initiative.
- 2026-05-22: Round 1 ran Solo Claude (strategist + validator) because API-key and Chrome-browser access were denied this session. External synthesis (ChatGPT thread, GPT-5, Perplexity) deferred to Round 2.
- 2026-05-22: Naming deliberately left OPEN pending the ChatGPT thread the user already worked in.
- 2026-05-22: Dashboard created at `_dashboards/aiops.html` (source: `Strategy/AI Ops/aiops.md`); launcher leaf flipped from TBD to live.

---

## Next steps

- [ ] **User**: grant Chrome/browser access OR paste the ChatGPT thread so Round 2 can fold in the existing thinking (especially any naming + positioning work already done there).
- [ ] **Round 2 (external team)**: GPT-5 validator on positioning + naming, Perplexity on market size / competitor framing for "AI-native operations" in CEE.
- [ ] Decide the six open questions above.
- [ ] If green-lit: write the client-facing one-pager for the offer and add it to Marketing.
- [ ] Tie the CCHBC engagement explicitly to this direction as the lighthouse account.
