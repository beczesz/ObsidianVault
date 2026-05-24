---
title: CPS Sales Strategy v2.0
version: 2.0
date: 2026-04-01
author: Szabolcs + Claude + ChatGPT + Perplexity (multi-AI brainstorming session)
description: Strategic framework for bringing in first own-pipeline CPS customers, Hungary-first with Western Europe expansion path. Strategy still valid. Operational timeline + KPIs superseded; see SALES_ENGINE.md + Dashboard.md + TODAY.md.
status: framework-active / timeline-superseded
id: f7b88868-e26c-4cc0-b964-4d0c034890d6
index_schema_version: 1
---

# CPS Sales Strategy v2.0

> **Status banner (2026-05-13):** The strategic framework in this document (3-engine model, repositioning, ICP Profiles #1-#3, Free Cloud Health Check entry, competitive positioning) is the canonical reference. The **90-day timeline below is historical** (it ran Apr 1 to Jul 5, 2026, with zero conversions). The 90-day clock was reset on 2026-05-11. For current operational state read these instead, in order:
>
> 1. `Sales/SALES_ENGINE.md` -- current engine documentation, KPIs, post-2026-04-27 simplifications
> 2. `Sales/Dashboard.md` -- current 90-day clock and weekly velocity tracker
> 3. `CPS/TODAY.md` -- daily action queue
> 4. `Sales/Pipeline.md` -- live Kanban
>
> Decisions made on 2026-04-27 that supersede parts of this file: 15-point scoring dropped in favor of HOT/WARM/COLD, multi-AI per-lead validation paused, weekly KPI is now "first touches sent" (target 25/week by Day 45). See `brainstorm/brainstorm_sales-strategy-agentic-review.md`.

## Executive Summary

CPS has built strong sales infrastructure (scanner, enablement toolkit, case studies, pipeline) but has zero own-pipeline conversions. This strategy addresses the real bottleneck: **activation + conversion + sharper positioning**, not more tools or theory.

**Core insight from brainstorming session:** CPS has NO direct competitor in Hungary offering standardized managed DevOps monthly packages for mid-sized companies. The market gap is confirmed. We are closer to our first deal than we think -- we need tight execution and repositioned messaging.

**Target:** 2-3 signed CPS customers within 90 days, Hungary-first.

---

## Strategic Repositioning

### Old Positioning (Profile #1 only)
"We replace your DevOps engineer."

### New Positioning (broader, pain-driven)
**"We find and fix invisible cloud cost leaks and operational risks -- without slowing your team down."**

Why this works better:
- CFO understands cost savings (20-40% cloud spend waste is common)
- CTO feels operational fragility (single point of failure)
- Creates urgency without being pushy
- Justifies the Free Audit as entry point

### Messaging Framework

| Audience | Primary Hook | Supporting Message |
|----------|-------------|-------------------|
| CTO / VP Engineering | "Your cloud is operationally fragile" | Team > single hire, proactive monitoring, SLA-backed |
| CFO / Finance | "You're likely wasting 20-40% of cloud spend" | FinOps optimization, predictable monthly cost vs. hire |
| CEO / Founder | "One person can't keep the lights on AND innovate" | CPS = backstage crew, you focus on product |
| Compliance / Legal | "Your cloud needs documented change management" | Logged change management, incident response, audit trail |

---

## The 3-Engine Model

### ENGINE A: "Triggered Outbound" (Keep & Expand)

**What it is:** Current Profile #1 scanner + expanded triggers.
**Role:** High-intent side channel (1-3 leads/month).

**Current triggers:**
- DevOps job postings older than 30 days

**New triggers to add:**
- Companies hiring multiple engineers (growth chaos signal)
- Recent funding / expansion announcements
- Cloud migration signals in job postings for OTHER roles ("some AWS knowledge helpful")
- Companies removing DevOps person from LinkedIn
- Regulated industries (energy, finance, insurance) posting any IT role

**Owner:** Automated scanner (Claude) + Molnar Daniel (validation)
**Expected yield:** 2-4 leads/month (up from 1-2)

### ENGINE B: "Pain-Based Outbound" (FASTEST PATH TO FIRST DEAL)

**What it is:** Proactive outreach to companies matching our ICP, regardless of job postings. Lead with pain, not triggers.

**Target universe:**
- Hungarian companies, 30-500 employees
- Running AWS or Azure (44.9% of HU companies with 10+ employees use cloud)
- SaaS, fintech, energy, insurance, logistics, healthtech
- Especially regulated sectors (energy, finance, insurance, healthcare)

**Outreach sequence (3-touch):**

**Message 1 -- Insight Hook (LinkedIn or email):**
> "Hi [Name], I lead a cloud operations team that works with companies like [reference -- MVMI, Green Hill]. We consistently see a pattern: mid-sized Hungarian companies running AWS lose 20-35% of their cloud spend to invisible inefficiencies -- oversized instances, orphaned resources, missing reserved capacity. Is this something you'd want to validate? We do a 60-minute Cloud Health Check, no strings attached."

**Message 2 -- Specific Hypothesis (3-5 days later):**
> "Quick follow-up -- based on companies similar to [their company] in [their industry], the most common issues we find are: (1) no FinOps visibility (20-35% cloud waste is typical), (2) single-person infrastructure risk, (3) developers wasting time on infra instead of shipping features. Would a quick call to see if any of these resonate be useful?"

**Message 3 -- Low-Friction CTA (5-7 days later):**
> "Last note -- if now isn't the right time, no problem. But if your cloud ops ever keeps you up at night, here's what we do: [link to one-pager]. Happy to chat whenever it makes sense."

**Owner:** Szabolcs + Molnar Daniel
**Expected yield:** 5-10 outreach conversations/month, 1-2 Free Audits/month

### ENGINE C: "Authority Inbound" (Start Now, Harvest Later)

**What it is:** Content + events to build credibility and generate inbound interest. Not the primary lead source in the first 90 days, but essential for compounding.

**Minimum viable inbound (build in parallel):**

1. **One killer article:** "Hol pazarolnak a magyar cegek a cloudban?" (Where do Hungarian companies waste money in the cloud?) -- publish on website + LinkedIn + Medium
2. **One lead magnet PDF:** "Cloud Cost Leak Checklist -- 10 things mid-sized companies miss" -- gate behind email
3. **One conference talk:** Target Craft Conference (June 4, Budapest) or AWS Community Day CEE (Sep 17, Budapest)

**Conference Strategy (2026):**

| Event | Date | Why | Action |
|-------|------|-----|--------|
| BSides Budapest | Apr 29 | Security angle, meet technical buyers | Attend, network, collect contacts |
| Craft Conference | Jun 4 | DevOps/platform engineering crowd, CTOs | Submit talk: "What we learned managing cloud for 11 companies" |
| AWS Community Day CEE | Sep 17 | AWS-native audience, perfect ICP match | Submit talk + sponsor booth. Show Free Audit live. |
| HUNOG | Sep 30 | Operations/SRE focused | Attend, network |
| HUSTEF | Oct 6 | IT service management | Attend, distribute one-pager |

**Owner:** Szabolcs (talks), Molnar Daniel (networking), Claude (content drafts)
**Expected yield:** 0-1 inbound leads in first 90 days, but credibility compounds

---

## KBOSS/Szamlazz.hu -- First Target Activation

> **Outreach draft superseded:** The inline message in this section is the original 2026-04-01 draft. It was replaced on 2026-05-11 by the v2 sharpened draft in `Sales/Sales Enablement/outreach-batch-1-hot-leads.md` (section `v2 #4. KBOSS / Szamlazz.hu`). The v2 message uses a different thesis: career-page-shows-no-DevOps means devs absorbed the AWS work, not "persistent hiring." Use v2 for any send. The text below is kept for context only.

### Company Profile
- Hungary's largest online invoicing platform
- ~50 employees, founded 2004
- AWS confirmed (privacy policy references AWS cloud)
- Persistent DevOps hiring (multiple postings from 2025-2026)
- Now owned by Visma (Norwegian software group, 14K+ employees)
- 100,000+ businesses depend on their platform

### Likely Cloud Situation (Reverse-Engineered)
- **AWS workload:** Production SaaS platform serving 100K+ businesses. Likely EC2/EKS, RDS (PostgreSQL or MySQL), S3 for document storage, CloudFront CDN, SQS/SNS for async processing.
- **Estimated AWS spend:** EUR 5,000-20,000/month (based on user base and complexity)
- **Pain points:**
  1. Persistent DevOps hiring = they cannot find or retain someone. A junior cannot manage this alone.
  2. Financial SaaS = NAV integration, GDPR = reliability and compliance pressure
  3. Visma parent may or may not provide centralized DevOps -- if not, KBOSS is on their own
  4. 100K+ businesses depend on uptime = operational fragility with thin DevOps coverage

### Outreach Draft for KBOSS

**Subject:** Szamlazz.hu cloud operations -- egy gondolat

**Message:**
> Kedves [CTO neve],
>
> A Sonrisa Cloud Platform Services csapatot vezetem -- 13 mernokkol kezeljuk magyar es europai cegek AWS/Azure infrastrukturat havidijas alapon.
>
> Lattam, hogy a Szamlazz.hu tobbszor is keresett DevOps/uzemelteto kollegat az elmult evben. Hasonlo meretu SaaS cegeknel, akikkel dolgozunk, harom dolgot latunk visszateroen:
>
> 1. A cloud koltsegek 20-35%-a lathatatlan pazarlas (tulmeretezett instance-ok, hianyzó RI-k)
> 2. Egyetlen uzemelteto = egyetlen meghibasodasi pont, ami 100.000+ ugyfelet erint
> 3. Egy ember nem tudja lefedni a monitoringot, az incidenskezelest es a napi uzemeltetest -- ehhez csapat kell
>
> Szivesen megcsinalnek egy 60 perces Cloud Health Check-et -- ingyenes, csak olvasasi hozzaferes kell, es konkret szamokkal terunk vissza.
>
> Van ertelme egy rovid beszelgetesnek?
>
> Udvozlettel,
> Szabolcs

**Validation needed before sending:**
- [ ] Confirm posting is still active on profession.hu
- [ ] Research if Visma provides centralized DevOps (if yes, KBOSS may not need us)
- [ ] Find CTO/Head of Engineering name on LinkedIn
- [ ] Confirm they are NOT already a Sonrisa client through another channel

---

## 90-Day Execution Plan

### PHASE 1: Activate & Convert (Weeks 1-4)

**Theme:** Fix execution discipline. Activate existing pipeline. Validate Free Audit.

| Week | Actions | Owner | Expected Outcome |
|------|---------|-------|-----------------|
| W1 (Apr 1-7) | 1. Check Greenergy LinkedIn connect status, send follow-up if accepted. 2. Validate KBOSS (Visma check, find CTO). 3. Send CIG Pannonia follow-up via LinkedIn to Zankai Attila. | Szabolcs + Nandi | 3 leads re-activated |
| W2 (Apr 8-14) | 1. Send KBOSS outreach (if validated). 2. Draft Pain-Based outreach template (ENGINE B). 3. Set up daily follow-up SLA: every lead touched every 3-5 days. | Szabolcs + Claude | Outreach sent to KBOSS, ENGINE B template ready |
| W3 (Apr 15-21) | 1. Identify 10 Hungarian companies for ENGINE B (cloud-using, 30-500 emp, regulated or scaling sectors). 2. Send first ENGINE B batch (5 companies). 3. Follow up on all active leads. | Nandi + Claude | 5 new outreach conversations started |
| W4 (Apr 22-28) | 1. Send ENGINE B batch 2 (5 more companies). 2. BSides Budapest (Apr 29) -- attend, network, collect 10+ contacts. 3. First Free Audit if any lead converts to call. | Szabolcs + Nandi | 10 total ENGINE B outreaches, BSides contacts |

**Phase 1 KPIs:**
- Leads contacted: 15+
- Discovery calls booked: 2-3
- Free Audits conducted: 1
- Pipeline value: EUR 5,000+ potential MRR

### PHASE 2: Scale & Refine (Weeks 5-8)

**Theme:** Run the engines in parallel. Conduct Free Audits. Close first deal.

| Week | Actions | Owner | Expected Outcome |
|------|---------|-------|-----------------|
| W5 (Apr 29 - May 5) | 1. Process BSides contacts. 2. Publish first article: "Hol pazarolnak a magyar cegek a cloudban?" 3. Continue ENGINE B outreach (5/week). | Szabolcs + Claude | Article live, 5 more outreaches |
| W6 (May 6-12) | 1. Conduct Free Audit #1 (whoever converts first). 2. Refine audit structure based on experience. 3. Submit Craft Conference talk proposal. | Szabolcs + team | First Free Audit completed |
| W7 (May 13-19) | 1. Free Audit follow-up -- present findings, propose package. 2. Continue ENGINE B (5/week). 3. Create Cloud Cost Leak Checklist PDF. | Szabolcs + Nandi | First proposal sent |
| W8 (May 20-26) | 1. Close first deal (target). 2. If not closed: analyze why, adjust messaging. 3. Greenergy follow-up reminder fires (Apr 10 scheduled). | Szabolcs | FIRST CPS CUSTOMER (target) |

**Phase 2 KPIs:**
- Free Audits conducted: 2-3
- Proposals sent: 2
- Deals closed: 1 (target)
- Article published: 1
- Conference talk submitted: 1

### PHASE 3: Compound & Expand (Weeks 9-12)

**Theme:** Second and third customers. Begin Western Europe preparation.

| Week | Actions | Owner | Expected Outcome |
|------|---------|-------|-----------------|
| W9-10 (May 27 - Jun 9) | 1. Craft Conference (Jun 4) -- present, network, collect leads. 2. Continue ENGINE B (5/week). 3. Conduct Free Audits from Phase 2 pipeline. | Szabolcs + Nandi | Conference exposure, 2-3 warm leads |
| W11 (Jun 10-16) | 1. Process Craft Conference leads. 2. Close deal #2. 3. Begin Western Europe research: identify 3 target countries, adapt messaging to English. | Szabolcs + Claude | Second customer (target) |
| W12 (Jun 17-23) | 1. Close deal #3. 2. First case study from own-pipeline customer. 3. Plan ENGINE B expansion to Western Europe (DACH first). | Szabolcs + Nandi | Third customer (target), WEU plan ready |

**Phase 3 KPIs:**
- Total deals closed: 2-3
- New MRR from own pipeline: EUR 2,000-6,000
- Case studies from own clients: 1
- Western Europe expansion plan: drafted

---

## Profile #2: "The Scaling Company" (New ICP)

Based on the brainstorming session, here is the second ICP to develop alongside Profile #1:

**Target:** Hungarian companies that are growing fast (hiring multiple engineers, expanding product) but whose developers are stuck doing infrastructure work because there is no dedicated DevOps person or the DevOps team is overwhelmed.

**Trigger signals:**
- Hiring multiple backend/fullstack engineers (growth chaos)
- No DevOps role posted or filled (developers covering infra)
- Recent funding or expansion announcements
- Cloud migration underway or planned

**Entry message:**
> "A fejlesztoi neked arra kellene, hogy termeked epitsek -- nem arra, hogy AWS instance-okat menedzseljenek. Mi 13 fos csapattal atvesszuk a cloud uzemeltetest, hogy a csapatod arra fokuszalhasson, amiert felvetted oket. Havidijas alapon, EUR 2,000-tol."

**Package fit:** Essential (EUR 2,000/mo) or Growth (EUR 4,000/mo)

**Priority:** Begin research in Week 5, activate in Week 9.

---

## Competitive Positioning (Hungary)

| Competitor Type | Examples | Their Model | CPS Advantage |
|----------------|----------|-------------|---------------|
| Enterprise consultancies | Accenture, Deloitte, 4iG, NTT | EUR 10,000+/mo, enterprise-only | CPS is 5-10x cheaper, serves mid-market |
| Local consultancies | Cheppers, dyrector, GetTech | Hourly (EUR 80-150/h) or project-based | CPS offers predictable monthly cost, team not individuals |
| Freelance DevOps | Individual contractors | EUR 40-80/h, single person | CPS = team with backup, SLA, no single point of failure |
| **Nobody** | - | Standardized managed DevOps monthly packages for SMEs | **THIS IS OUR BLUE OCEAN** |

---

## Key Metrics to Track

| Metric | Week 4 Target | Week 8 Target | Week 12 Target |
|--------|---------------|---------------|----------------|
| Outreach sent (ENGINE B) | 15 | 35 | 55 |
| Discovery calls booked | 2 | 5 | 8 |
| Free Audits conducted | 1 | 3 | 5 |
| Proposals sent | 0 | 2 | 4 |
| Deals closed | 0 | 1 | 2-3 |
| New MRR (own pipeline) | EUR 0 | EUR 2,000+ | EUR 4,000-8,000 |
| Articles published | 0 | 1 | 2 |
| Conference talks submitted | 0 | 1 | 1 |

---

## Immediate Next Actions (This Week)

1. **TODAY:** Check Greenergy LinkedIn connect status
2. **TODAY:** Research KBOSS -- find CTO name, check Visma centralization
3. **By Friday:** Send KBOSS outreach (if validated)
4. **By Friday:** Send CIG Pannonia follow-up to Zankai Attila on LinkedIn
5. **By Friday:** Draft ENGINE B outreach template (use messaging framework above)
6. **Next Monday:** Identify first 10 ENGINE B target companies (Hungarian, 30-500 emp, cloud-using, scaling or regulated sectors)

---

## Sources

- **ChatGPT (Sonrisa CPS GPT):** Strategic framework -- 3-engine model, repositioning from "replace your hire" to "cloud cost leaks + operational risks", activation sequence, Free Audit validation
- **Perplexity:** Hungarian market research -- cloud adoption rates (IVSZ-Deloitte study), competitor landscape, conference calendar (techconf.hu, dev.events), B2B sales channels
- **CPS Internal:** Pipeline data (Jira), lead scanner results, case studies, pricing, team capacity
