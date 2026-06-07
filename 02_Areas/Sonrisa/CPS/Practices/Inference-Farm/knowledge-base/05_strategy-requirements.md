---
title: "Inference Farm — Strategy, Plan & Requirements"
date: 2026-05-29
author: Becze Szabolcs
status: active
description: "Strategic foundation of the LLMaaS / Inference Farm: the merged business plan (problem statement, value proposition, business impact, risk register, 3-phase roadmap MVP→scale→strategic adoption, success KPIs), the 10-area business-development checklist (strategy, product, infra, security, ops, financials, legal, team, marketing, risk), and the original AI Integration Requirement Document framing the build-vs-buy decision (self-hosted EC2 vs AWS Bedrock vs open APIs) with DevOps/Developer requirements. Source: Plan.docx, Planning.docx, AI Integration Requirement Document.docx."
practice_area: cps-inference-farm
type: strategy-reference
audience: internal-business
provenance: "Extracted by Forge on 2026-05-29 from: Plan.docx (2025-09-05, merged LLMaaS plan), Planning.docx (2025-07-31, 10-area checklist), AI Integration Requirement Document.docx (2025-06-20, Sonrisa)."
id: 4ea5bfc7-7941-4e68-a8c7-a02d63a7bab4
index_schema_version: 1
bdos_index: false
---

# Strategy, Plan & Requirements

> Sources: `Plan.docx`, `Planning.docx`, `AI Integration Requirement Document.docx`. See [00_SOURCE_INDEX.md](00_SOURCE_INDEX.md). This is the 2025 internal-first framing; the practice has since productized externally (see [../proposals/](../proposals/)).

## Merged LLMaaS business plan (Plan.docx)

An **internal Enterprise LLM-as-a-Service platform** delivering secure, token-based LLM access to enterprise teams, hosted on AWS GPU infra using open-source models (Qwen-32B, DeepSeek). Scoped to the ~$500/mo POC budget.

### Problem statement

Public LLM services (OpenAI, Anthropic) create barriers:
- **Data privacy & compliance risk** — sensitive data sent externally; GDPR-like violations in regulated sectors.
- **High & unpredictable cost** — per-token pricing escalates (20–30% higher than in-house), opaque budgeting, no cost ceilings.
- **Vendor lock-in & no customization** — limited fine-tuning / proprietary-data integration.
- **Performance & latency** — throughput constraints >50 users, variable latency.
- **Operational fragmentation** — disparate tools → silos, duplicated effort.

Estimated drag: $1M+/year in lost productivity and inefficiency.

### Solution & value proposition

Self-hosted LLM SaaS on AWS: secure on-demand access to open-source models, abstracting complexity, ensuring compliance, predictable pricing.

Key components: secure in-house hosting; token-based access with TPS/TPM quotas; open-source model support (Qwen-32B, DeepSeek, Llama); Open WebUI / custom frontend; usage tracking + chargebacks; tiered plans (Entry / 8-5 / 24-7).

Value: data sovereignty; up to 50% cost savings ($0.005/token internal vs $0.01+ public); model flexibility; ~20% productivity gains; simplified operations.

### Business impact

| Area | Outcome | Quantification |
|---|---|---|
| Cost savings | Lower external API reliance | 40–60% reduction (~$100K/yr) |
| Productivity | Faster task completion | 20% time savings on routines |
| Internal revenue | Department chargebacks | $100K+ annually |
| Innovation | Custom AI apps | 10+ new use cases in Year 1 |
| Risk reduction | Fewer breaches | 99% uptime, zero external leaks |

ROI: MVP $5–10K vs annual savings $50–100K → payback 3–6 months; gross margin target 60%+.

### Risk register

| Category | Risk | Level | Mitigation |
|---|---|---|---|
| Performance & scalability | Latency/throughput >50 users; spikes → downtime | Medium | Phased rollout + auto-scaling; benchmark; monitor uptime 99% / response <5s; queue at peaks |
| Cost & resource | High GPU cost; $500/mo POC limits scope | **High** | Spot/reserved instances; throttle; monthly ROI reviews; prioritize basic tiers; horizontal scaling post-MVP |
| Monitoring & billing | Token-tracking complexity; billing errors | Medium | Automated logging (Redis/PostgreSQL); test with 5–10 teams; dashboards |
| Adoption & change mgmt | User resistance; low initial usage | Low | Awareness/training; high-visibility demos; >60% adoption target |
| Governance & compliance | Audit/logging; GDPR-like alignment | Medium | Early auth/auditing; legal from Day 1; SOC2-style docs; quarterly audits |
| Market & competition | External price drops weaken proposition | Low | Quarterly competitor analysis; differentiate via in-house customization |
| Talent & expertise | AI-ops / cloud skill gaps | Medium | Upskilling/consultants; cross-functional IT+business teams |

### 3-phase roadmap

- **Phase 1 — MVP & validation (1–3 months, ~$500/mo):** deploy low-cost setup + benchmark (IT); token-tracking MVP (Ops); launch Entry/8-5 tiers + frontend, pilot 5–10 teams (Product); cost modeling (Finance); load testing (QA); competitor deep-dive (Strategy). KPIs: realistic quotas, 99% tracking reliability, 80% satisfaction, budget adherence.
- **Phase 2 — scale-up (3–6 months):** add 24/7 premium tier + SLA (Product); usage dashboards + automated chargebacks + multi-model (Ops); finalize compliance docs (Legal/Ops). KPIs: 50% adoption growth, 60%+ margins, 85% satisfaction.
- **Phase 3 — strategic adoption (6–12 months):** dedicated instances + explore external monetization + federated-learning pilots (Business Dev); quarterly KPI review (Leadership). KPIs: $100K+ revenue, >99.5% availability.

### Success KPIs

| KPI | MVP target | 6-month target | Method |
|---|---|---|---|
| Adoption rate | 3–5 depts | 10+ teams | Sign-ups/logs |
| Cost savings | 40% vs ext | 50%+ | OPEX comparison |
| Token volume | 10M/mo | 100M+ | Tracking system |
| Gross margin | 50% | 60%+ | Billing reports |
| Uptime | 99% | 99.5% | Monitoring |
| User satisfaction | 8/10 | 9/10 | Surveys |

## 10-area business-development checklist (Planning.docx)

1. **Business strategy** — competitive analysis (Together AI, Fireworks AI; multitenancy risks), SWOT, differentiate via in-house privacy; value prop & personas; phased GTM (POC→MVP), KPIs (adoption >60%, ROI 6-month payback); partnerships (Slack integration, open-source communities).
2. **Product development** — token-based access, per-user/project tracking, tiered packages; open-source model selection (Qwen-32B), multi-model + fine-tuning; UX iteration; agile MVP roadmap.
3. **Technical infrastructure** — AWS G5.12XL GPUs, spot instances, auto-scaling; vLLM serving, load balancing, fault tolerance; S3 storage, token counting, rate limiting, CloudWatch; RESTful APIs + JWT.
4. **Security & compliance** — in-house processing, encryption at-rest/transit, RBAC; secure tokens/API keys, per-user quotas; GDPR/SOC2 alignment, data sovereignty (region-specific); hallucination/bias + incident response.
5. **Operations & scaling** — CI/CD, zero-downtime updates; load testing, high TPS/TPM; SLA tiers (24/7 on-call); usage dashboards, failover.
6. **Financials & pricing** — CAPEX + OPEX, target margins 50–60%, OPEX/token pricing; token-based tiers + overage; benchmark vs OpenAI; internal chargebacks first, future external monetization.
7. **Legal & ethical** — model licenses (open-source compliance), ethical AI/usage policies, SLAs & liability, EU AI Act 2025.
8. **Team & talent** — cross-functional team (AI eng, DevOps, business analysts), MLOps/cloud gap closing, agile (Jira), retention.
9. **Marketing & adoption** — internal promotion (demos, webinars), onboarding guides, surveys/NPS, adoption KPIs.
10. **Risk management & contingency** — risk matrices, multi-region backups, pilots/stress-tests, exit strategies.

## AI Integration Requirement Document (2025-06-20)

The original requirements doc framing the **build-vs-buy** decision. Central goal: evaluate feasibility of building/maintaining our own AI infrastructure as an **alternative to AWS Bedrock**, modeling two cost categories: monthly infrastructure cost (compute, storage, transfer, networking, with FinOps optimizations) and development cost of the service layer (APIs, orchestration, security, monitoring).

**Client integration paths:**
1. Open APIs (OpenAI, Claude, Gemini) — low cost, rapid, but low control/privacy.
2. AWS Bedrock — higher data protection, managed scalability.
3. **Dedicated EC2 infrastructure** — highest privacy/control, for sensitive/proprietary data. *This is the option the doc exists to evaluate.*

**DevOps team requirements:** token-based usage tracking + reporting; autoscaling EC2; client environment isolation (logical/physical).

**Developer team requirements:** Sonrisa-maintained API abstraction layer unifying AI services; support for both public AI APIs and private models.

**Cost considerations:** token-based estimation; compare Bedrock pay-per-use vs EC2 self-host; **target 90% server utilization in EC2 shared setups**; gather client usage to project scale; determine breakeven/profitability thresholds. (TODO in source: validate assumptions with real-world testing.)

**Other:** GDPR compliance; encryption at-rest/transit; full audit trails for client deployments; custom isolation for dedicated clients; transparent handling for public-API users; dedicated AI support team; SLA-backed uptime; regular updates; usage dashboards; feedback loops.

## Related

- Pricing/OPEX detail → [04_business-model-pricing.md](04_business-model-pricing.md)
- Current customer-facing proposals → [../proposals/01-sonrisa-llmaas-platform-description.md](../proposals/01-sonrisa-llmaas-platform-description.md), [../proposals/02-aws-ace-opportunity-summary.md](../proposals/02-aws-ace-opportunity-summary.md)
- Strategic positioning (AI-native OS pillar 1) → [../research/02-strategic-positioning-pillar-1.md](../research/02-strategic-positioning-pillar-1.md)
