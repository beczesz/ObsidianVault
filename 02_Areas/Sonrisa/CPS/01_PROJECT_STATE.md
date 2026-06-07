---
title: CPS Project State
version: 0.6
date: 2026-05-11
author: Szabolcs
description: Single source of truth for CPS unit status, priorities, and next actions
id: 54d4b708-04fa-4a3e-8f96-484c04c7d354
index_schema_version: 1
---

# CPS Project State

## Objective

Build CPS into a self-sustaining managed services business unit within Sonrisa. Close first own-pipeline customer, scale to 8 active contracts and EUR 28K MRR within 12 months, and achieve AWS Advanced Tier partnership.

## Current Status

CPS is in an **execution phase** across multiple fronts simultaneously. The team (~13 engineers + 1 E9+ contractor) is stable after two departures (Bakonyi, Janko-Kiraly). A workshop on 2026-03-21 formalized the Unit model, assigned TAMs to clients, and set the junior hiring direction.

**Sales: clock reset to Day 1 = 2026-05-11.** The Sales Engine v1.0 was built 2026-04-27 (full agentic-flow doc, 15 leads, Kanban pipeline, 4-AI thinking team review). Execution did not begin in the 14 days that followed. Zero outreach sent. As of 2026-05-11, the 90-day plan clock has been honestly reset to today as Day 1. Phase 1 milestones (first 5 HOT outreach by 2026-05-12, all 15 contacted by 2026-05-15, first discovery call by 2026-06-15) start fresh. Sonrisa pipeline sustains the team through May, with runway to September.

**Active client delivery:** Green Hill/SynLab, Onriva, Colosseum Dental (URGENT -- May deadline, ~20 days left; contract renewal/extension review in progress), Diligentes (new), SocialBud. MVMI AzureDevOps managed service still in contract signing phase (RED clauses need negotiation before signing). Observer project pending cost optimization report and post-mortem.

**Key risks:**
1. Colosseum Dental delivery is behind schedule. May 2026 deadline is ~20 days away. Status meeting with unit still not held.
2. Q1 2026 Unit Model deadline missed (March 31). TAM documentation, Jira boards, workshop recording docs still incomplete. Needs Q2 reschedule.
3. Sales: 14-day execution gap between Sales Engine v1.0 build (2026-04-27) and first outreach send. Clock reset to today. Risk of repeating the same procrastination pattern. Mitigation: orchestrator lead validation scheduled for Day 1, first 5 HOT messages target 2026-05-12.
4. MVMI AzureDevOps has contract RED flags that need negotiation before signing (see szerzodes_notes.md). Not yet at kickoff stage.

## Key Metrics

| Metric | Current | Target (Month 12) |
|--------|---------|-------------------|
| Own-pipeline CPS contracts signed | 0 | 8 |
| CPS MRR (own pipeline) | EUR 0 | EUR 28,000 |
| Active leads in pipeline | 15 (5 HOT, 5 WARM, 5 COLD on Obsidian Kanban) | Continuous |
| Outreach touches sent (lifetime) | 0 | 150-200 per signed deal |
| First touches sent this week (W1) | 0 of 5 target | 25/week by W5 (2026-06-08) |
| Case studies published | 5 | 8+ |
| AWS ACE Opportunities | 3/10 | 10+ |
| Team size | ~13 + 1 contractor | +2 E1 juniors planned |
| Weekly competitor scans | Running (automated Mondays 9AM) | Ongoing |
| Daily lead scanner | Running (weekdays 7:30AM) | Ongoing |

## Active Problems

1. **Colosseum Dental delivery risk** -- May deadline (~20 days away), unclear how many days remain, credential issues caused delays, status meeting with unit (Marci, Boti, Zoli) STILL NOT HELD
2. **No own-pipeline customer yet** -- Sales Engine v1.0 built 2026-04-27 with 15 validated leads and ready drafts. Zero outreach sent in 14 days. Clock reset 2026-05-11. First HOT batch targets 2026-05-12 send.
3. **MVMI AzureDevOps contract RED flags** -- Contract has RED clauses needing negotiation before signing (see szerzodes_notes.md). Not at kickoff stage yet.
4. **Observer cost optimization report** -- Needs completion before post-mortem can proceed
5. **Onriva TAM undecided** -- Workshop identified KV (Kovacs Attila) or Mark as candidates, decision not yet made
6. **Unit Model Q1 deadline missed** -- TAM list, Jira boards, workshop recording documentation still incomplete. Missed March 31 deadline, needs Q2 reschedule.
7. **ITIL processes** -- Need to be built up from scratch; only a tool comparison doc and a merged ITIL reference exist
8. **Inference Farm monitoring** -- Status unclear, needs assessment
9. **Jira hygiene** -- SAM1 example project has overdue items. Should be cleaned up or completed. CIG Pannonia (KAN-6) Jira status is "Contacted" but pipeline docs show "Unvalidated" -- needs sync.

## Current Focus

1. **Sales: Engine warm-up (Day 1 of 90, reset 2026-05-11)** -- Run orchestrator lead validation today, sharpen 5 HOT outreach drafts with hyper-specific icebreakers, send Tuesday 2026-05-12. WARM batch Wednesday. All 15 contacted by Friday 2026-05-15.
2. **Colosseum Dental -- CONTRACT REVIEW** -- Reviewing contract for renewal/extension beyond May 2026. Hold status meeting with unit (Marci, Boti, Zoli). ~20 days to current May deadline.
3. **MVMI AzureDevOps** -- Negotiate RED contract clauses before signing. Team assignment and kickoff blocked until contract done.
4. **Observer** -- Complete cost optimization report, then post-mortem.
5. **Unit Model** -- Q1 missed. Reschedule to Q2: TAM list, Jira boards, workshop recording docs.
6. **Admin** -- Review all projects, prepare stats and invoices. Clean up SAM1 example project in Jira.

## Next Actions

**Sales (this week):**
- [ ] Run /general-utils:think-agent-orchestrator-v07 to refresh HOT/WARM validation and surface better leads (2026-05-11)
- [ ] Sharpen 5 HOT outreach drafts with hyper-specific icebreakers (KBOSS, Chemaxon, Loxon, SEON, Colossyan)
- [ ] Find decision makers on LinkedIn for each of the 5 HOT prospects
- [ ] Send 5 HOT messages 2026-05-12 (HU for KBOSS/Loxon, EN for SEON/Colossyan, Chemaxon TBD)
- [ ] Draft + send 5 WARM messages 2026-05-13 to 2026-05-14
- [ ] All 15 leads contacted by 2026-05-15
- [ ] Log every send to Pipeline.md (move card from HOT/WARM to Contacted with date) and Dashboard.md (W1 row)

**Delivery and ops:**
- [ ] Colosseum Dental: Contract renewal/extension review (when doc provided)
- [ ] Colosseum Dental: status meeting with unit (Marci, Boti, Zoli)
- [ ] Communicate Colosseum status to Csaba
- [ ] MVMI AzureDevOps: negotiate RED contract clauses, then assign team and kick off
- [ ] Observer: complete cost optimization report
- [ ] Observer: schedule post-mortem after report done
- [ ] Onriva TAM decision: KV or Mark
- [ ] Document TAM assignments from workshop into formal unit list
- [ ] Set up Jira boards per unit
- [ ] Junior Program: identify source/program for 2x E1 hires
- [ ] ITIL: create initial process frameworks (Incident, Change, Problem, Release)
- [ ] Inference Farm: assess current monitoring state, define gaps
- [ ] Review all active projects for stats and invoicing
- [ ] Case study generator demo for Nandi
- [ ] Ramp-up template for new client contracts
- [ ] Teams communication rules: document and communicate to team
- [ ] Reporting AI-ification: schedule meeting with Mark + Banfi Istvan
- [ ] Jira: Clean up or archive SAM1 example project
- [ ] Jira: Sync CIG Pannonia status -- KAN-6 shows "Contacted" but pipeline docs show "Unvalidated"

## Constraints

- **Financial runway:** Sonrisa pipeline covers team through May, not loss-making through September
- **Team capacity:** 13 engineers + 1 contractor. Two juniors planned but not yet hired.
- **AWS Partnership:** Select Tier. Need 7 more ACE opportunities + Service Delivery Designation for Advanced path.
- **Colosseum deadline:** May 2026 (hard)
- **Unit Model Q1 target:** Missed, needs rescheduling to Q2

## Last Updated

2026-05-11

## Project Map

| Path | Description |
|------|-------------|
| `Accounts/Active/` | 11 active client folders with NOTES.md (Green Hill, Onriva, Colosseum, Diligentes, SocialBud, OKFO, Observer, MVMI, Jumeon, ProSharp, Direct Travel) |
| `Accounts/Leads/` | 6 lead folders with NOTES.md (Greenergy, KBOSS, CIG Pannonia, NETOPIA, EOS Faktor, SafeFleet) |
| `TASKS.md` | Detailed task tracker with all active workstreams and subtasks |
| `Sales/` | Sales toolkit (scripts, checklists, outreach, lead scanner) + 5 case studies + generator prompt. **Lead Scanner Script:** `Sales/Sales Enablement/Lead Scanner/SCANNER_SCRIPT.md` -- manually triggered multi-AI lead search (Perplexity + ChatGPT + Claude via Think Agent Orchestrator) |
| `Strategy/` | Roadmap, BMC, AWS partnership, competitor reports, dashboard. **Sales Strategy v2.0:** `Strategy/CPS Sales Strategy v2.0.md` -- 3-engine model (Triggered Outbound, Pain-Based Outbound, Authority Inbound) with 90-day plan |
| `Team/` | Unit model, communication framework, recruitment, workshop summary |
| `Services/` | Service descriptions, Cost Optimization toolkit, ITIL, Inference Farm |
| `Marketing/` | Blogs, website pages, selvio CMS reference, CPS intro, Sonrisa description |

## Sales Engine Quick Start

To spin up the sales engine in a new session:

1. **Read this file** for overall CPS status
2. **Read `Strategy/CPS Sales Strategy v2.0.md`** for the full 3-engine sales strategy, positioning, 90-day plan, and outreach templates
3. **Read `Sales/Sales Enablement/Lead Scanner/SCANNER_SCRIPT.md`** to run a collaborative lead scan using the Think Agent Orchestrator (Perplexity + ChatGPT + Claude)
4. **Read `Sales/Sales Enablement/leads.md`** for the current pipeline
5. **Read `Sales/Sales Enablement/Lead Scanner/seen-companies.md`** for dedup before scanning

Say "run the lead scanner" to trigger a multi-AI scan session. Say "review the pipeline" to check current lead status.

**ChatGPT conversation:** Sonrisa CPS GPT (custom GPT with CPS context baked in)
**Perplexity:** Use for sourced market research, company validation, decision-maker identification

## Available Context

- `Strategy/CPS Sales Strategy v2.0.md` -- 3-engine sales strategy with 90-day execution plan (April 2026)
- `Sales/Sales Enablement/Lead Scanner/SCANNER_SCRIPT.md` -- Multi-AI lead scanner script (manual trigger)
- `Team/Workshop Summary 2026-03-24.md` -- Full workshop transcript summary with decisions
- `Strategy/BMC v1.3.md` -- Business Model Canvas
- `CPS Constitution.md` -- Founding principles and values
- `Strategy/AWS/` -- AWS partnership strategy docs
- `Practices/Inference-Farm/` -- LLMaaS practice area (Forge-managed): descriptions, ACE opportunity summary, model research
- `Partnership/Ingram Micro.md` -- Partnership notes
- `memory/` -- AI persistent knowledge base (team, values, packages, recruitment)
- `memory/` -- AI persistent knowledge base (team, values, packages, recruitment)
