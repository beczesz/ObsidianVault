---
title: CPS Collaborative Lead Scanner Script
version: 2.0
date: 2026-05-13
author: Szabolcs + Claude
description: Manual trigger script for multi-AI lead scanning. Uses Think Agent Orchestrator -- Perplexity searches, ChatGPT analyzes, Claude executes. Updated for the post-2026-04-27 simplified engine (HOT/WARM/COLD, no Jira, Pipeline.md as source of truth).
id: fa6f1ca9-49ba-4e80-8a75-a702ff3ee813
index_schema_version: 1
---

# CPS Collaborative Lead Scanner Script

> **How to use:** Say "run the lead scanner" or "start a lead scan" and Claude will orchestrate a session across Perplexity (search), ChatGPT (quality analysis), and Claude (execution + pipeline updates). Target: 2-3 HOT leads per run.
>
> **NOTE on cadence:** This scanner has been paused since 2026-04-01. The 2026-04-27 thinking-team review concluded that the bottleneck is execution (touches sent), not intelligence. Resume only after we have 50+ outreach data points or when ENGINE A coverage is genuinely thin. See `SALES_ENGINE.md` for the current engine model.

---

## 1. Mission

Find 2-3 HOT leads every run by scanning job boards, news, and business signals for companies matching our ICP. This is a manually triggered collaborative workflow using the Think Agent Orchestrator skill.

**Goal per run:** 2-3 HOT leads, plus any WARM leads as bonus. (Simplified HOT/WARM/COLD scoring since 2026-04-27; see Section 6.)

---

## 2. AI Role Assignment

| Agent | Role | What They Do |
|-------|------|-------------|
| **Perplexity** | Search & Fact-Finding | Runs search queries, finds job postings, confirms company details, checks tech stacks, finds decision-maker names. Sources everything. |
| **ChatGPT** | Quality Analysis & Strategy | Classifies leads as HOT/WARM/COLD against ICP, reverse-engineers cloud situations, identifies pain points, crafts outreach hypotheses, flags disqualifications. |
| **Claude** | Orchestration & Execution | Triggers searches, feeds results between agents, updates Pipeline.md (Kanban card), drafts/refreshes leads.md dossier, updates seen-companies.md, writes daily brief. |

---

## 3. Geographic Priority

### Tier 1: Hungary (PRIMARY -- every run)
Budapest, Szeged, Debrecen, Pecs, Gyor. Same timezone, same language, personal network, can meet in person.

### Tier 2: Western & Northern Europe (SECONDARY -- expand after HU yields thin)
- **Nordics (Sweden first):** We have a Swedish client (Colosseum Dental) and will soon have a case study. Sweden, Denmark, Finland, Norway.
- **DACH:** Germany, Austria, Switzerland. Higher budgets, English-speaking tech teams.
- **Benelux:** Netherlands, Belgium. Strong tech scene.

### Tier 3: Romania (TERTIARY)
Bucharest, Cluj-Napoca, Timisoara. Sonrisa office presence, cultural proximity.

**Rule:** Always run Hungary searches first. If fewer than 2 HOT leads found, expand to Tier 2/3.

---

## 4. ICP Profiles

### Profile #1: "The Replacement Hire" (Original)
Companies that lost their DevOps person and are hiring a replacement.

| Attribute | Ideal |
|-----------|-------|
| Company age | 5-20 years (founded 2005-2020) |
| Employees | 30-200 (acceptable up to 500) |
| Cloud | AWS or Azure (confirmed in posting or public info) |
| Trigger | Active DevOps/Cloud/Platform Engineer job posting |
| Team gap | Sole or small (1-2) DevOps team |
| NOT | Startups (<3yr), consulting firms, staffing agencies, enterprises (500+) |

### Profile #2: "The Scaling Company" (New -- from Strategy v2.0)
Companies growing fast whose developers are stuck doing infrastructure work.

| Attribute | Ideal |
|-----------|-------|
| Sector | SaaS, fintech, e-commerce, healthtech, logistics |
| Cloud | AWS or Azure workloads |
| Team | Small IT team, developers doing infra, no dedicated DevOps |
| Trigger | Hiring multiple backend/fullstack engineers + no DevOps role filled |
| Pain | Developers wasting time on infra, deployments slow, incidents increasing |

### Profile #3: "The Cloud Cost Pain" (New -- from Strategy v2.0)
Companies showing signals of cloud cost pressure.

| Attribute | Ideal |
|-----------|-------|
| Cloud spend | Estimated EUR 3,000-30,000/month |
| Signal | Hiring FinOps, mentioning cost optimization, rapid growth, scaling |
| Team | No FinOps capability, developers doing infra |
| Pain | 20-40% invisible cloud waste |

---

## 5. Search Phase -- Perplexity Queries

### Hungary Queries (run every time)

```
1. "DevOps engineer" OR "cloud engineer" site:profession.hu Budapest 2026 -EPAM -SAP -OTP -Telekom -PwC -Siemens -IBM -Accenture -Deloitte
2. "platform engineer" OR "infrastructure engineer" Hungary "AWS" OR "Azure" job 2026 -outsourcing -consulting
3. "DevOps mernok" OR "uzemelteto" OR "felhoalapu" Budapest job 2026
4. site:linkedin.com/jobs "DevOps" OR "cloud engineer" Hungary posted
5. Hungarian company "cloud migration" OR "scaling" OR "growing" hiring engineers 2026
```

### Western & Northern Europe Queries (when HU yields < 2 HOT)

```
6. "DevOps engineer" Sweden OR Denmark OR Finland OR Norway AWS job 2026 -EPAM -Accenture -Deloitte company:small
7. "cloud engineer" OR "platform engineer" Germany OR Austria AWS OR Azure job 2026 30-200 employees
8. "DevOps engineer" Netherlands OR Belgium AWS job 2026 -consulting -outsourcing
9. site:linkedin.com/jobs "DevOps" OR "SRE" Sweden Stockholm posted
10. "infrastructure engineer" Nordic startup OR scaleup AWS 2026
```

### Romania Queries (supplemental)

```
11. "DevOps engineer" Romania AWS Bucharest Cluj job 2026 -EPAM -Endava -Accenture
12. "cloud engineer" OR "infrastructure engineer" Romania AWS 2026
```

### Expanded Trigger Queries (ENGINE A+ from Strategy v2.0)

```
13. Hungarian company recently funded OR expanding cloud team 2026
14. "cloud migration" OR "AWS migration" Hungary OR Romania company 2026
15. Hungarian companies hiring multiple engineers backend OR fullstack 2026 (growth chaos signal)
```

**Perplexity instructions:** For each query, find actual company names, job posting URLs, posting dates, company sizes. Provide sources. Skip any company already in the seen-companies list (Claude will provide the list).

---

## 6. Classification Phase -- ChatGPT Analysis

> **Changed 2026-04-27:** The old 15-point scoring matrix was dropped in the thinking-team review. It became a procrastination device. Replace with a fast HOT/WARM/COLD gut-check informed by the criteria below.

ChatGPT classifies each candidate Perplexity finds as **HOT / WARM / COLD** based on the strength of the signal.

| Bucket | Signal pattern | Action |
|--------|----------------|--------|
| **HOT** | Active DevOps/Platform/SRE posting on the company's OWN career page (not just a job board) + ICP match (Profile #1, #2, or #3) + AWS or Azure confirmed + reachable decision-maker | Add to Pipeline.md HOT column. Drafting / outreach decision this week. |
| **WARM** | ICP match but signal is weaker: posting only on a 3rd-party board, older than 30 days, AWS/Azure not directly confirmed, or indirect (funding + scaling) trigger only | Add to Pipeline.md WARM column. Outreach decision within 2 weeks. |
| **COLD** | Possible fit but unvalidated or weak signals (Tier 3 geo, small founding-team data, partial AWS hints) | Add to Pipeline.md COLD column for monthly review, or push to seen-companies.md if borderline. |

Useful inputs to the gut-check (NOT a scoring rubric, just context for the call):
- Company maturity (sweet spot 5-20 years; <3 years usually too early; >20 years usually has established IT)
- Posting age (30+ days is a failed-hire signal, very strong)
- AWS/cloud signal strength (explicit in posting > inferred from product > none)
- Team gap (sole DevOps or no DevOps at all is the strongest pain)
- Geographic fit (Tier 1 Hungary preferred; Tier 2 Nordics/DACH/Benelux next; Tier 3 Romania bonus)

**ChatGPT additional analysis for HOT leads:**
1. Reverse-engineer likely cloud setup (what AWS/Azure services they probably use)
2. Estimate cloud spend range
3. Identify 2-3 specific pain points (cost waste, single-person risk, scaling bottleneck)
4. Suggest best outreach angle (cost, compliance, or reliability)
5. Recommend entry package (Safety Net, Essential, Growth, or Scale)
6. Identify best case study match from our portfolio

---

## 7. Disqualification Rules

Immediately disqualify (do not score, add to seen-companies as DISQUALIFIED):

- Companies with 500+ employees
- IT outsourcing / consulting / staffing / recruitment firms
- Companies already in seen-companies.md
- Direct competitors (managed cloud / DevOps service providers)
- Startups founded after 2021 (unless well-funded and scaling fast)
- Companies with zero AWS/cloud signal
- Government entities requiring formal procurement (unless strong fit)
- Companies headquartered outside our geographic tiers

---

## 8. Execution Phase -- Claude Updates

> **Changed 2026-04-27:** Jira was abandoned in favor of the local Obsidian Kanban board at `Sales/Pipeline.md`. Single source of truth for stage is the Kanban. Do not recreate Jira tickets.

### 8a. Update Pipeline.md (Kanban)

File: `Sales/Pipeline.md`

For each HOT or WARM lead, add a card to the corresponding column. Card format:
```
- [ ] **<Company>** #hot|warm|cold #engine-a|b|c #<vertical-tag> #lang-hu|en @{YYYY-MM-DD outreach-due-date} <One-line signal summary>. Stack: <key tech>. Package: <fit>. Career page: <url>. [[Accounts/Leads/<Name>/NOTES]]
```

COLD leads go to the COLD column only if they pass the Disqualification Rules (Section 7). Otherwise log them to seen-companies.md and stop.

### 8b. Create or refresh Account NOTES.md

File: `Accounts/Leads/<Name>/NOTES.md` (use `Accounts/_Template/NOTES.md`).

For HOT leads only: write a NOTES.md with decision-maker names, contact channels, current outreach posture, open items. This is the rolling per-account memory.

### 8c. Add to leads.md dossier (HOT and rich-data WARM only)

File: `Sales/Sales Enablement/leads.md`

Add a dossier section if the lead has unique deep research (estimated cloud spend, reverse-engineered stack, multi-angle pain analysis). Skip if the NOTES.md already captures everything useful. leads.md is the one-time research dump, not a pipeline tracker.

### 8d. Update seen-companies.md

File: `Sales/Sales Enablement/Lead Scanner/seen-companies.md`

Add every company evaluated (HOT, WARM, COLD, DISQUALIFIED):
`- [Company Name] | [Date] | [Signal] | [Status: NEW/RESEARCHED/DISQUALIFIED]`

### 8e. Write Daily Brief

Save to: `Sales/Sales Enablement/Lead Scanner/daily-brief-[YYYY-MM-DD].md`

Contents:
- Summary (queries run, companies screened, HOT/WARM/COLD counts)
- HOT leads with classification rationale and reverse-engineered cloud setup
- WARM leads list
- Disqualified companies with reason
- Pipeline.md changes made
- Outreach recommendations for HOT leads

---

## 9. Outreach Angle Templates (from Strategy v2.0)

### Angle A: Cloud Cost Waste
> "We consistently see mid-sized companies waste 20-35% of cloud spend on oversized instances, orphaned resources, and missing RI coverage. We validate this in a 60-minute Cloud Health Check -- read-only access, no commitment."

### Angle B: Scaling Bottleneck
> "Your developers are spending 30-40% of their time on infrastructure instead of building product. We take over cloud operations so your team can focus on what they were hired for -- shipping features."

### Angle C: Operational Fragility
> "One DevOps person is a single point of failure. If they leave, get sick, or go on vacation, your production infrastructure is exposed. We're a team of 13 engineers with SLA-backed support -- your backstage crew."

### Angle D: Swedish/Nordic Reference (for Tier 2 Nordic expansion)
> "We currently manage cloud infrastructure for a Swedish healthcare company [Colosseum Dental, once case study is ready]. We understand Nordic quality expectations and offer EU-timezone coverage with 24/7 on-call capability."

---

## 10. Case Study Matches

| Industry | Case Study | Best For |
|----------|-----------|----------|
| Energy | cs-001 MVMI Energy OpenShift | Energy companies, regulated sectors |
| Finance/Insurance | cs-004 MVMI Azure DevOps | Azure-using companies, regulated sectors |
| Government/Public | cs-005 OKFO | Public sector, compliance-heavy |
| SaaS/Operations | cs-003 Onriva/myRiva | SaaS platforms, operations support |
| Healthcare | Colosseum Dental (COMING SOON) | Nordic expansion, healthcare, project-to-managed |
| Generic | cs-002 [check folder] | General cloud operations |

---

## 11. CPS Packages Reference

| Package | Price | Hours | Best For |
|---------|-------|-------|----------|
| Safety Net | EUR 990/mo | 6h | Companies with DevOps team wanting backup |
| Essential | EUR 2,000/mo | 40h | Lost DevOps person, simple setup |
| Growth | EUR 4,000/mo | 80h | Moderate complexity, proactive management |
| Scale | EUR 6,000/mo | 120h | Mission-critical, complex environments |

**Add-ons:** 24/7 On-Call EUR 2,000/mo | Solution Architect EUR 1,000/mo | FinOps EUR 500/mo | DevSecOps EUR 700/mo | Extra hours EUR 70/h

---

## 12. Key Files

| File | Path | Purpose |
|------|------|---------|
| Sales engine overview | `Sales/SALES_ENGINE.md` | Start here. 3-engine model, KPIs, agentic flow. |
| Pipeline (single source of truth for stage) | `Sales/Pipeline.md` | Obsidian Kanban. HOT/WARM/COLD/Contacted/Discovery/Proposal/Won/Lost. |
| Dashboard | `Sales/Dashboard.md` | KPI tracker, 90-day clock, weekly velocity. |
| Daily action queue | `CPS/TODAY.md` | What to send/decide today. |
| Lead research dossiers | `Sales/Sales Enablement/leads.md` | One-time deep research dumps per lead. |
| ICP Profile #1 | `Sales/Sales Enablement/profile1.md` | Detailed Profile #1 definition. Profiles #2 and #3 in SALES_ENGINE.md. |
| Seen companies | `Sales/Sales Enablement/Lead Scanner/seen-companies.md` | Dedup ledger. |
| Daily briefs | `Sales/Sales Enablement/Lead Scanner/daily-brief-*.md` | Historical run record. |
| Sales Strategy v2.0 | `Strategy/CPS Sales Strategy v2.0.md` | Strategic framework (timelines superseded by SALES_ENGINE.md + Dashboard.md). |
| Case studies | `Sales/Case Studies/Clients/` | Reference for outreach. |
| Account NOTES | `Accounts/Leads/<Name>/NOTES.md` | Rolling per-account memory. |
| Current outreach drafts | `Sales/Sales Enablement/outreach-batch-1-hot-leads.md` | The actual v2 messages being sent. |

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-04-01 | Initial version. Evolved from automated daily scanner. Added multi-AI orchestration, Profile #2 (Scaling Company) and #3 (Cloud Cost), Western/Northern Europe expansion (Sweden first via Colosseum Dental), outreach angle templates from Strategy v2.0. |
| 1.1 | 2026-04-01 | Removed NIS2 references -- CPS does not have NIS2 certification yet. Replaced compliance angle with scaling bottleneck angle. |
| 2.0 | 2026-05-13 | Aligned with the 2026-04-27 thinking-team decisions: dropped 15-point scoring matrix in favor of HOT/WARM/COLD gut-check, removed Jira sections (Pipeline.md is now source of truth for stage), added NOTES.md execution step, refreshed Key Files. Scanner is paused until 50+ outreach data points are collected. |
