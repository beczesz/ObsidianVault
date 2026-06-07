---
title: CCHBC AIOps sub-bid — Tier A/B/C refinement brainstorm
date: 2026-05-19
author: Becze Szabolcs + Think Agent Orchestrator v0.9
status: round-1-synthesized
description: Multi-AI brainstorm a CCHBC AIOps sub-bid Tier A/B/C ajánlat finomítására. Round 1 lefutott (Claude Opus 4.7 Strategist + GPT-5 Validator + Perplexity Sonar Researcher). Pricing 2-6x emelve, framing átalakítva, deliverable-ek szerződés-szinten újrafogalmazva.
tags: [cchbc, aiops, brainstorm, tier-refinement, magyar-telekom]
id: 564a9c77-afb5-4b84-af70-3cac2260990c
index_schema_version: 1
---

# CCHBC AIOps Tier Refinement — Round 1 Synthesis

**Session:** 2026-05-19 evening
**Driver:** Becze Szabolcs
**Round 1 status:** ✅ COMPLETE — synthesis below

---

## Context (canonical anchors)

- **CCHBC dossier**: [NOTES.md](NOTES.md)
- **RFP full text**: [Tender/rfp-full-text.md](Tender/rfp-full-text.md)
- **Email thread**: [Tender/email-thread.md](Tender/email-thread.md)
- **Internal implementation phases doc** (KEY new input): [Tender/implementacios-fazisok.md](Tender/implementacios-fazisok.md)
- **Glossary**: [GLOSSARY.md](GLOSSARY.md)
- **Inference Farm**: [../../../Practices/Inference-Farm/proposals/01-sonrisa-llmaas-platform-description.md](../../../Practices/Inference-Farm/proposals/01-sonrisa-llmaas-platform-description.md)

## Team & Round 1 raw findings

| AI | Role | Transport | Findings file | Status |
|---|---|---|---|---|
| Claude Opus 4.7 (running) | Strategist + Orchestrator | local | [_round1_strategist_claude.md](Tender/_round1_strategist_claude.md) | ✅ |
| GPT-5 | Validator | OpenAI API | [_round1_gpt5_extracted.md](Tender/_round1_gpt5_extracted.md) | ✅ |
| Perplexity Sonar Pro | Researcher | Perplexity Sonar API | [_round1_pplx_extracted.md](Tender/_round1_pplx_extracted.md) | ✅ |

API cost ezért a roundért: ~$0.20 (GPT-5) + ~$0.12 (Perplexity) = **~$0.32**.

---

## 🎯 Round 1 — Key insights (where the 3 AIs converge)

### Convergence point 1 — **Pricing was 2-6x too low**

Mindhárom forrás megerősíti:
- **Perplexity** (market data): EU/CEE senior day-rates €700-1,300; Big-4 GenAI deals €5-50M; single PoC €250k-750k typical; FMCG managed services 15-40% of cloud spend
- **GPT-5** (validator): Tier B (€100-160k/év) 2-4x under market for 1.5-2 FTE; Tier C (€240-400k/év) 3-6x under market; quarterly PoCs alone €75-150k each at industry standard
- **Claude** (strategist): innovation szelet a teljes CCHBC deal-ből kb. €1-3M/év → Tier A 2-5%-ot fed le, kb. túl kicsi

**Az új sávok lent láthatók a Refined Tiers szekcióban.**

### Convergence point 2 — **Tier C 24/7 rotation impossible at 3-4 FTE**

GPT-5: "24x7 L2/L3 coverage needs ~5-7 FTE to rotate (not 3-4). At €110k/FTE loaded cost (CEE) your cost floor is €550-770k before margin."

**Implikáció:** vagy emeljük a Tier C team-méretet 5-7 főre és árazzunk hozzá, vagy **levesszük a 24/7-et** a default Tier C-ből és **opcionális add-on**-ként hozzáadjuk readiness gate-tel.

### Convergence point 3 — **Vague deliverables = contract trap**

GPT-5 3 deliverable-re ad szerződés-szintű újrafogalmazást:
- "Quarterly Agentic AI PoCs" → time-boxed 6 hét, 1 primary KPI threshold, exit criteria, artifact list
- "FinOps platform delivery" → 3 increment (tagging 85% coverage, chargeback 5% variance, automation 10 actions/month)
- "24x7 named team" → 5-min ack, 30-min P1 engagement, 6 named engineers, max 8 concurrent automations, exclusions

**Implikáció:** minden Tier deliverable-jét **konkrét számokkal és acceptance criteria-val** át kell írnunk. Ezek lentebb beépítve.

### Convergence point 4 — **Tier 0 (pre-engagement assessment) szükséges**

Claude + GPT-5 egyetért: 4-6 hetes Tier 0 fixed-fee assessment, **€30-60k**, 2026 Q4-ben.
**Indok:** SOC 2 umbrella + Azure landing zone + GPU quota + Dynatrace permissions = ezek **blocker-ek 2027 startra** ha nem front-load-oljuk.

### Convergence point 5 — **Hybrid pricing model > pure FTE**

Mindhárom megerősíti: small retainer + fixed-fee per PoC + (Tier C-nél) outcome bonus.
- Retainer = governance/integration kapacitás (MT-nek kell)
- Fixed PoC fee = acceptance-kötött, scope-clear
- Outcome bonus = FinOps savings tied (1-2% of validated savings, capped)

### Convergence point 6 — **Tier model framing változtatása**

GPT-5 erős steelman: a "Tier A/B/C menu" SMB-packaging érzetet ad, cherry-picking-et hív elő.

**Javasolt új framing** (Claude + GPT-5 fúziója):
**"Agentic AIOps Program for CCHBC"** — egyetlen program, 3 workstream-mel + readiness-gated add-on-okkal:

```
Agentic AIOps Program
├── Workstream 1: FOUNDATIONS (mandatory)
│   • Azure landing zone integration
│   • Dynatrace Davis AI tuning
│   • ServiceNow workflow integration
│   • Compliance umbrella alignment
│
├── Workstream 2: INTELLIGENT OPS (mandatory)
│   • Quarterly named-agent production deployment
│   • Hermes/OpenClaw orchestration framework
│   • Inference Farm Azure deployment
│
├── Workstream 3: FINOPS AUTOMATION (optional, Tier 2+)
│   • Tagging enforcement
│   • Chargeback dashboards
│   • Rightsizing automation
│
└── Add-ons (readiness-gated):
    • 24x7 AI Ops Support (after maturity gate)
    • GPU Inference Farm (after quota approval)
    • Innovation Accelerator (quarterly PoC factory)
```

**MT-nek 3 capacity-tier-t mutatunk** (Discovery/Specialist/Operator), de a deliverable-ek workstream-szinten vannak elnevezve, nem "Tier A/B/C".

### Convergence point 7 — **Sub-bid trap mitigation**

GPT-5 explicit: "Becoming an underpriced sub absorbing integration risk without back-to-back SLAs."

Mitigáció (Round 1 javaslat):
- **Sticky pricing clause**: Sonrisa árszint érvényes csak ±10% scope-on belül
- **Back-to-back SLAs** MT-vel (nem CCHBC-vel direktben)
- **Dependency register** mint formal bid attachment (MT mit kell biztosítania)
- **Termination protection**: Q1 után minimum 6 hónap retainer payable

---

## 🔧 REFINED TIER MODEL (Round 1 output)

### Tier 0 — Pre-Engagement Discovery (NEW)

**€40-60k fixed fee, 4-6 weeks, scheduled 2026 Q4 (before 2027 engagement start)**

Deliverables:
- CCHBC Azure estate audit (resource inventory, tag coverage, cost baseline)
- Dynatrace tenant deep-dive (Davis AI usage audit + gap analysis)
- ServiceNow workflow mapping
- Azure AI landing zone readiness review (private networking, GPU quota assessment)
- Agent portfolio prioritization workshop (with CCHBC product owners)
- SOC 2 / NIS2 umbrella scope confirmation with MT
- **Output**: signed dependency-locked SOW for 2027 Tier 1/2/3 engagement

**Risk:** very low. Even if CCHBC walks, we got paid for a real assessment.

---

### Tier 1 — "Discovery / Architect" (was Tier A)

**€60-100k / year** (was €32-60k → +60-90% adjustment based on market data)

**Structure**: €5-8k/month retainer + €10-15k per quarterly demo PoC

Deliverables:
- Quarterly AIOps capability assessment (8-week cycle, signed report)
- Architecture review board membership (MT engineers consult us before building)
- Dynatrace Davis AI quarterly tuning workshop (delivered audit + recommendations + 10-20 named config changes)
- 1 lab-environment demo PoC per quarter (video walkthrough + reproducible artifacts)
- Reference architecture document maintenance (Hermes-on-Azure pattern)

Team capacity: 0.5 FTE (architect-led, ML engineer part-time)

**Risk: low.** Advisory + lab-only PoC; no production exposure.

---

### Tier 2 — "Agent Builder" ⭐ DEFAULT RECOMMENDATION (was Tier B)

**€280-400k / year** (was €100-160k → ~3x adjustment, matches market for 1.5-2 FTE + production PoCs)

**Structure**: €12-18k/month retainer + €40-60k per delivered production agent (4 per year)

Deliverables — INCLUDES Tier 1 +:
- **Q1 of each year**: Hermes/OpenClaw orchestration framework deployment on CCHBC Azure
  - Acceptance: framework live, 1 reference agent (Alert Triage) running on synthetic data, runbook + monitoring in place
- **Each quarter Q2-Q4**: 1 named production agent from catalog:
  - Alert Triage Agent (Dynatrace events → ServiceNow consolidated incidents)
  - FinOps Optimizer Agent (Cost data → rightsizing recommendations, auto-execute on small resources)
  - Operator Remediation Agent (autonomous response to known patterns)
  - RCA Drafter Agent (incident logs → first-draft RCA in ServiceNow)
  - Capacity Forecaster Agent (predictive CPU/memory/storage warnings)
  - Deploy Verifier Agent (pre/post-deploy health checks)
  - Each agent: 6-week time-box, 1 primary KPI with target, full Terraform module, runbook, security review, demo, sign-off in CAB
- Inference Farm Azure deployment (one-time setup billed separately, see below)
- ServiceNow + Dynatrace integration design + implementation
- Monthly SLA/SLO report + quarterly governance review with MT
- Reference case study contribution (CCHBC-anonymized)

Team capacity: 2-2.5 FTE (0.5 architect, 1 ML engineer, 0.5-1 DevOps engineer + part-time SRE)

**Risk: medium.** Production agents = real responsibility. Mitigated by:
- Time-boxed PoC scope per agent
- Human-in-the-loop guardrails for Q2 (Q3+ can have higher autonomy)
- Back-to-back SLA with MT (not direct CCHBC)
- Dependency register (Azure quota, Dynatrace API access, ServiceNow integration permissions) as bid attachment

**One-time setup fees** (year 1 only):
- Inference Farm Azure port: **€30-45k** (3-4 weeks engineering)
- Hermes/OpenClaw foundation: included in Q1 deliverable

---

### Tier 3 — "Agent Operator" (was Tier C)

**€650-900k / year** (was €240-400k → ~2.5x adjustment, reflects 5-7 FTE 24/7 reality)

**Structure**: €30-45k/month retainer + €40-60k per delivered production agent (4-6/year) + €5-8k/month 24/7 ops fee + 1-2% outcome bonus on validated FinOps savings (capped at €100k/year)

Deliverables — INCLUDES Tier 2 +:
- **Production operation** of all deployed agents (24/7 monitoring, on-call rotation)
  - 5-minute acknowledgment, 30-minute engagement for P1 agent incidents
  - Minimum 6 named engineers on rotation
  - Max 8 concurrent production agents under support (gated by maturity)
- **FinOps workstream** (3 increments):
  - I: Tagging baseline to ≥85% resource coverage in top-10 Azure services, real-time enforcement via Azure Policy/Terraform
  - II: Chargeback dashboards in Power BI/Azure Cost Management, ≤5% variance vs Azure invoice
  - III: Rightsizing automation, minimum 10 automated actions/month with rollback
- **Self-learning automation on CI/CD**: pipeline failure pattern analysis, alert tuning AI, deploy/test agents
- Quarterly innovation backlog with measured outcomes (FinOps savings, MTTR reduction)
- Joint go-to-market right (Sonrisa named in MT-CCHBC delivery materials)

Team capacity: **5-7 FTE** (1 architect lead, 2 ML engineers, 2 DevOps engineers, 1 SRE, 1 FinOps engineer, rotation pool for 24/7)

**Risk: high.** Mitigated by:
- Readiness gate before 24/7 activates (3 months parallel run minimum)
- Outcome bonus aligns Sonrisa incentives
- Quarterly capacity review with MT (scale up/down with 60-day notice)
- Sprint 3 wind-down complete before Tier 3 starts

**CAUTION**: Tier 3 is **stratégiailag túl nagy fogadás** Sonrisa jelenlegi méreténél (13 fő + recruitment paused) **HACSAK** a CCHBC engagement nem 2027-re halasztott, ami időt ad új ML engineer és SRE-k felvételére.

---

## 📊 New pricing summary

| Tier | Year 1 (incl. one-time) | Years 2-4 (recurring) | Sonrisa FTE | Risk |
|---|---|---|---|---|
| **Tier 0** | €40-60k (one-time) | — | 1-2 FTE for 6 weeks | Very low |
| **Tier 1 Discovery** | €60-100k | €60-100k | 0.5 FTE | Low |
| **Tier 2 Agent Builder** ⭐ | €310-445k (incl. €30-45k Inference Farm port) | €280-400k | 2-2.5 FTE | Medium |
| **Tier 3 Agent Operator** | €680-945k (incl. setup) | €650-900k | 5-7 FTE | High |

**4-year total (recommended path):** Tier 0 + 4× Tier 2 = €40-60k + 4× €280-400k + €30-45k one-time = **€1.19M - €1.71M over 4 years**

---

## 📋 Contract-grade deliverable rewrites (GPT-5 generated, accepted)

### "Quarterly Agentic AI PoC" → contract-grade:
> *"Per calendar quarter, deliver one scoped agent in CCHBC Azure using only approved data and tools, time-boxed to 6 weeks from kickoff. Scope includes: problem statement, success criteria (one primary KPI with target threshold agreed by MT/CCHBC), architecture diagram, security review, Terraform module(s), runbook, demo, and written report. Exclusions: production SLAs, PII processing unless DPIA approved. Acceptance = KPI ≥ agreed threshold and artifact delivery in repo + ServiceNow knowledge article."*

### "FinOps Platform Delivery" → contract-grade:
> *"Deploy FinOps capability in three increments: (I) Tagging baseline to ≥85% resource coverage across top-10 Azure services in 3 scoped subscriptions; real-time policy enforcement via Azure Policy/Terraform within 90 days. (II) Chargeback showback reports in Power BI/Azure Cost Management for 100% of tagged resources with monthly variance ≤5% vs Azure invoice. (III) Rightsizing automation covering VMs and Managed Disks with change window enforcement; execute min. 10 automated actions/month in pilot scope with rollback. Acceptance: documented controls, reports, and automation jobs reviewed in CAB and signed-off by MT."*

### "24x7 Named AI Ops Support" → contract-grade:
> *"Provide 24x7 L2 incident response for AIOps automations and agent workflows in scope, with on-call roster guaranteeing 5-minute acknowledgment and 30-minute engagement for P1 incidents. Coverage requires minimum 6 named engineers (no single point of failure) with skills matrix. Back-to-back SLAs with MT/CCHBC; monthly SLO report; maximum 8 concurrent automations supported in GA scope. Exclusions: underlying Azure platform incidents, Dynatrace platform incidents, and ServiceNow outages."*

---

## ⚠️ Critical risks identified (Round 1)

1. **Azure landing zone + GPU quota** (GPT-5 high-confidence flag) — Inference Farm deployment can be blocked by CCHBC private networking policy or Microsoft GPU quota delays. **Mitigation**: dual-path contingency (preferred Inference Farm OR fallback to Azure OpenAI/Model Catalog).
2. **SOC 2 Type 2 gap** — without MT umbrella, Sonrisa cannot sign. **Mitigation**: written umbrella clause in MT sub-contract; alternative: start SOC 2 audit in Q3 2026 (€20-65k, 6-9 months prep).
3. **Tier 3 bandwidth** — 5-7 FTE conflicts with Sprint 3 + 11 clients. **Mitigation**: hire 3 new engineers in 2026 H2; or default to Tier 2 unless CCHBC explicitly upgrades.
4. **MT rate-squeeze** — sub-bid vendors typically rebilled at 15-30% markup with margin pressure. **Mitigation**: hybrid pricing + sticky pricing clause + back-to-back SLAs.
5. **Dynatrace Davis AI overlap** — Davis already does much of what we'd build. **Mitigation**: positioning as "Davis extender" (custom remediation, ServiceNow agentic, FinOps integration), not "Davis replacement".

---

## 🎤 Recommended approach for Berecz Sándor call

When Szurdi Miki connects you to Berecz:

1. **Lead with the program framing**: "We propose an Agentic AIOps Program for CCHBC, structured around 3 mandatory workstreams (Foundations, Intelligent Ops, FinOps) and readiness-gated add-ons (24x7, GPU Inference Farm)."

2. **Show the 3 capacity tiers** (Discovery/Specialist/Operator) with **the new pricing** (€60-100k / €280-400k / €650-900k recurring annually).

3. **Pitch Tier 0 hard**: "Before any 2027 engagement, we'd recommend a 4-6 week pre-engagement assessment (€40-60k fixed fee) in Q4 2026 to lock dependencies. This protects MT's bid from scope surprises and gives CCHBC confidence."

4. **Ask the 4 critical questions** (need clarity before May 31):
   - **Compliance umbrella**: Will MT carry SOC 2 Type 2 + NIS2 obligation, or do we need our own?
   - **Commercial model**: Pass-through Sonrisa pricing or markup? What % markup is expected?
   - **Deal economics**: What's the total CCHBC bid value MT is targeting? What % is the AIOps slice?
   - **Engagement model**: Are we co-named to CCHBC, or white-label under MT?

5. **Flag the dependencies**: Azure landing zone access, GPU quota pre-approval, Dynatrace API entitlements, ServiceNow agentic permissions. **All of these must be MT's responsibility to secure**, written in dependency register.

---

## Next steps

- [ ] **2026-05-20**: Internal Sonrisa go/no-go on Tier 3 capacity feasibility (Szabolcs + Ceclan + Szántó)
- [ ] **2026-05-20**: Reply to Szurdi Miki, request Berecz introduction
- [ ] **2026-05-21**: Berecz call with the 4 critical questions above
- [ ] **2026-05-22-27**: Refine pricing with Molnár Dani (FTE cost modeling)
- [ ] **2026-05-28-30**: Draft 4-6 page sub-bid document for MT
- [ ] **2026-05-31**: Submit to Berecz Sándor

---

## Decisions log

- 2026-05-19 17:00: Team locked: Opus (local), GPT-5 (API), Perplexity Sonar (API).
- 2026-05-19 17:31: Round 1 complete. Pricing adjusted 2-6x upward. Tier 0 added. Hybrid model adopted. Framing changed from "A/B/C menu" to "Agentic AIOps Program with capacity tiers".
- 2026-05-19 17:35: All 6 critical risks logged with mitigations.
- 2026-05-19 17:35: Tier 3 flagged as conditional on Sprint 3 wind-down + 3-engineer hiring in 2026 H2.
