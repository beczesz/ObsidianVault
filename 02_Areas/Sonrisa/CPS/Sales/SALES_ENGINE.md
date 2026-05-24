---
title: CPS Sales Engine - Agentic Flow Documentation
version: 1.0
date: 2026-04-27
author: Szabolcs + Thinking Team (ChatGPT, Perplexity, Gemini, Claude Chat, Claude Cowork)
description: Complete documentation of the CPS agentic sales process. Read this file to quickly catch up on the sales system.
id: d8100a8a-2411-4e98-9b80-bdb556ccd54c
index_schema_version: 1
---

# CPS Sales Engine

## Quick Start (for new sessions)

Read these files in this order to get full context:

1. **This file** -- system overview, agentic flow, KPIs, team roles
2. `Sales/Pipeline.md` -- Obsidian Kanban board (single source of truth for leads)
3. `Sales/Sales Enablement/leads.md` -- detailed lead research notes (v0.2)
4. `Strategy/CPS Sales Strategy v2.0.md` -- full strategy document
5. `brainstorm/brainstorm_sales-strategy-agentic-review.md` -- thinking team session notes

### Live dashboard, per-lead schema (read before adding or editing leads)

There is a live HTML dashboard at `Sales/dashboard.html` that polls the vault every 8 seconds and renders an interactive kanban + today panel. **It rebuilds itself from markdown on every poll**, no HTML editing needed.

**Per-lead is now the primary source.** Each lead lives at `Accounts/Leads/<Name>/NOTES.md` with strict frontmatter and H2 body sections. Template: `Accounts/_Template/LEAD_NOTES.md`. Full contract: `Sales/DASHBOARD_CONTRACT.md`.

Required frontmatter for the dashboard to surface a lead:
- `type: lead`
- `company`
- `stage` (hot / warm / cold / contacted / discovery / proposal / won / lost)
- `source_url` (the original opportunity URL, posting or career page, REQUIRED, rendered prominently in the drawer)

**Scraper protocol** when any lead-scanner / engine / agent finds a new opportunity:

1. Copy `Accounts/_Template/LEAD_NOTES.md` to `Accounts/Leads/<NormalizedName>/NOTES.md`.
2. Fill `source_url` with the actual URL. This is mandatory.
3. Fill frontmatter from research (score, tags, due, next_action, package, location, industry).
4. Fill body sections: Signal, What They Want, About the Company, Why This Is Interesting (with Pain Hypotheses), Value Propositions, Key Contacts, The Angle, Timing, Red Flags, Drafts, Action Items, Next Step. Skip sections you do not have data for.
5. Add a kanban card to `Sales/Pipeline.md` in the right stage column: `- [ ] **CompanyName** #tag1 #tag2 @{YYYY-MM-DD} 1-line teaser`.
6. Wait up to 8 seconds. Dashboard picks up the new lead.
7. Do not edit `dashboard.html`.

**Read `Sales/DASHBOARD_CONTRACT.md` before:**
- Adding new top-level frontmatter keys you want the dashboard to surface
- Adding new H2 section names (parser is case-sensitive)
- Adding new column headers in Pipeline.md
- Changing the day-section header format in TODAY.md
- Renaming or moving Pipeline.md, TODAY.md, or per-lead NOTES.md files
- Swapping `@{YYYY-MM-DD}` for `📅` or vice versa (Pipeline uses `@{}`, TODAY uses `📅`, do not mix)

Legacy `leads.md` is still parsed as a fallback when a per-lead NOTES.md is absent or has no `type: lead` frontmatter. For new leads, always create the per-lead file.

## What CPS Sells

Monthly managed cloud operations packages for mid-sized companies (30-500 employees):

| Package | Price | Hours | Best For |
|---------|-------|-------|----------|
| Safety Net | EUR 990/mo | 6h | Backup support, small teams |
| Essential | EUR 2,000/mo | 40h | Core managed ops |
| Growth | EUR 4,000/mo | 80h | Scaling teams |
| Scale | EUR 6,000/mo | 120h | Full platform team |

Add-ons: 24/7 On-Call (EUR 2,000/mo), Solution Architect (EUR 1,000/mo), FinOps (EUR 500/mo), DevSecOps (EUR 700/mo), Extra hours (EUR 70/h).

## The 3-Engine Model

### ENGINE A: Triggered Outbound (background)
Scan job boards and career pages for DevOps/cloud hiring signals. Low yield (1-3 leads/month in Hungary) but high-intent when found.

### ENGINE B: Pain-Based Outbound (PRIMARY -- fastest path to first deal)
Proactive outreach to ICP companies regardless of job postings. Lead with cloud cost waste (20-35%) and operational fragility. Target: 25 first touches per week.

### ENGINE C: Authority Inbound (long-term)
Content marketing + conference talks. Articles, lead magnets, speaking engagements. Compounds over time.

## Positioning

**Old:** "We replace your DevOps engineer."
**New:** "We find and fix invisible cloud cost leaks and operational risks -- without slowing your team down."

Entry point: Free Cloud Health Check (60-min audit, read-only access, concrete findings).

## ICP Profiles

**Profile #1 "The Replacement Hire":** Company has open DevOps/cloud posting for 30+ days. Cannot hire or retain. CPS replaces with a managed team.

**Profile #2 "The Scaling Company":** Fast-growing company (funding, hiring engineers), developers doing infra work, no dedicated DevOps. CPS = fractional platform team.

**Profile #3 "The Cloud Cost Pain":** Company running AWS/Azure with no FinOps discipline. 20-35% cloud waste typical. CPS finds savings that pay for the engagement.

## Agentic Sales Flow

### What the AI does (KEEP):
1. **Lead scanning** -- daily monitoring of job boards and career pages for DevOps/cloud hiring signals
2. **Stack reverse-engineering** -- research company's likely cloud setup from job postings, privacy policies, GitHub, tech blog posts
3. **Career page monitoring** -- check company websites directly (stronger signal than job boards)
4. **Outreach drafting** -- personalized messages based on research findings
5. **Pipeline tracking** -- maintain Kanban board and lead files

### What the AI does NOT do (HUMAN ONLY):
1. **Sending outreach** -- Szabolcs or Nandi sends every message personally
2. **Discovery calls** -- always human-to-human
3. **Proposals and pricing** -- Szabolcs decides
4. **Relationship building** -- no AI can replace this

### What we PAUSED (per thinking team review 2026-04-27):
- Multi-AI validation loop (Perplexity -> ChatGPT -> Claude for every lead). Too slow, delays action.
- 15-point scoring matrix. Replaced with simple HOT / WARM / COLD.
- Over-research before outreach. 10-min gut check replaces multi-hour validation.

## Lead Scoring (simplified)

| Score | Criteria | Action |
|-------|----------|--------|
| **HOT** | Active DevOps hiring on own website + ICP match + budget signals | Outreach THIS WEEK |
| **WARM** | ICP match but weaker signals (old posting, no cloud confirmed, indirect signals) | Outreach within 2 weeks |
| **COLD** | Possible fit but unvalidated or weak signals | Research more or deprioritize |

## KPIs (weekly tracking)

| Metric | Target | Tracking |
|--------|--------|----------|
| First touches sent/week | 25 | Pipeline.md + Dashboard |
| Discovery calls booked | 2-3/month | Pipeline.md |
| Free Audits conducted | 1-2/month | Pipeline.md |
| Proposals sent | 2/month | Pipeline.md |
| Reply rate | >5% | Track manually |
| Cycle time (first touch to proposal) | <45 days | Pipeline.md dates |

## Funnel Benchmarks (from Perplexity research)

For EUR 1-6K/mo managed services, first year with no brand:

| Stage | Conversion | Volume needed per 1 deal |
|-------|-----------|--------------------------|
| Cold outreach sent | -- | 150-200 |
| Replies received | 1-5% of outreach | 8-12 |
| Discovery calls | 30-50% of replies | 3-5 |
| Qualified opportunities | 40-60% of calls | 2-3 |
| Proposals sent | 60-80% of qualified | 1-2 |
| Deals closed | 25-35% of proposals | 0.3-0.7 |

Cycle length: 30-90 days. 8-12 touch sequences to get first meeting. CEE market: local references carry disproportionate weight.

## Thinking Team

When strategic review or complex research is needed, spin up the multi-AI thinking team:

| AI | Role | How to activate |
|----|------|----------------|
| ChatGPT | Strategist | Browser tab, chatgpt.com |
| Perplexity | Researcher | Browser tab, perplexity.ai (use paste event for input) |
| Gemini | Validator | Browser tab, gemini.google.com/app |
| Claude Chat | Domain Expert | Browser tab, claude.ai |
| Claude Cowork | Orchestrator | This session |

State files: `brainstorm/brainstorm_*.md`
Skill: `/general-utils:think-agent-orchestrator-v07`

## File Structure

```
CPS/
  Sales/
    SALES_ENGINE.md          -- THIS FILE (system overview)
    Pipeline.md              -- Obsidian Kanban board (lead tracking)
    Dashboard.md             -- KPI dashboard (Dataview queries)
    Case Studies/            -- published case studies
    Sales Enablement/
      leads.md               -- detailed lead research notes
      Lead Scanner/
        SCANNER_SCRIPT.md    -- scanner methodology
        seen-companies.md    -- all companies ever evaluated
        daily-brief-*.md     -- daily scan results
        career-page-scan-*.md -- career page analysis
  Strategy/
    CPS Sales Strategy v2.0.md -- full strategy document
  brainstorm/
    brainstorm_*.md          -- thinking team session files
```

## Critical Rules

1. **CPS does NOT have NIS2 certification.** Never advertise NIS2 readiness in outreach.
2. **Volume before quality.** First 50 outreach attempts are for learning, not closing. Send first, optimize later.
3. **Human sends everything.** AI drafts, human reviews and sends. No automated outreach.
4. **Local references win in CEE.** Use existing 11 clients as proof. Case studies in Hungarian.
5. **Weekly metric: touches sent.** If touches/week < 25 by Day 45, something is wrong.
