---
title: CPS Lead Qualification Checklist
version: 0.1
date: 2026-03-16
author: Sonrisa - Cloud Platform Services (CPS)
description: Structured qualification framework for evaluating whether a prospect is a good fit for CPS managed services
id: 0b6fa323-9b5b-44cd-96a9-4a605932b40d
index_schema_version: 1
---

# CPS Lead Qualification Checklist

## Quick Qualification (Pre-Call)

Before investing time in a discovery call, verify at least 2 of 3:

- [ ] **Cloud spend signal:** Company appears to run production workloads on AWS (job posts mention AWS, tech blog references cloud, product is SaaS/web-based)
- [ ] **Team gap signal:** No DevOps/Platform team listed on LinkedIn, or only 1-2 people in that function, or actively hiring for DevOps roles
- [ ] **Trigger signal:** Recent funding round, rapid growth, migration announcement, compliance deadline, or key person departure

If fewer than 2 are present, deprioritize and move to nurture track.

---

## Full Qualification Framework (During/After Discovery Call)

### BANT+ Criteria

#### B - Budget

| Question | What you're looking for |
|----------|------------------------|
| "What's your approximate monthly AWS spend?" | Minimum $1,000/month for Cost Health Check, $5,000/month for managed services |
| "Do you have budget allocated for cloud operations support?" | Pre-allocated budget = faster close |
| "How does your company typically handle new vendor decisions?" | Understand approval process and timeline |

**Scoring:**
- 5: Budget confirmed, > $5K AWS spend, procurement process known
- 3: Budget likely, $1-5K AWS spend, decision process unclear
- 1: No budget, minimal AWS spend, or purely exploratory

#### A - Authority

| Question | What you're looking for |
|----------|------------------------|
| "Who else would be involved in this decision?" | Map the buying committee |
| "Have you evaluated similar services before?" | Prior experience speeds decisions |
| "What would need to happen for you to move forward?" | Reveals the real decision-maker |

**Scoring:**
- 5: Decision-maker in the call, can sign off alone or with one other person
- 3: Influencer in the call, needs to bring it to leadership
- 1: No authority, information gathering only

#### N - Need

| Question | What you're looking for |
|----------|------------------------|
| "What's your biggest infrastructure challenge right now?" | Specific, painful problem |
| "How is this impacting your team or product delivery?" | Business impact = urgency |
| "What happens if you don't solve this in the next 3 months?" | Cost of inaction |

**Scoring:**
- 5: Acute pain (recent outage, team member left, scaling crisis)
- 3: Chronic pain (developers doing DevOps, slow deployments, cost concerns)
- 1: No clear pain, "just exploring"

#### T - Timeline

| Question | What you're looking for |
|----------|------------------------|
| "When would you ideally want to have this solved?" | Urgency level |
| "Are there any deadlines driving this? (compliance, launch, migration)" | External pressure = faster close |
| "What's your evaluation timeline?" | Buying cycle length |

**Scoring:**
- 5: Needs solution within 30 days, external deadline
- 3: 1-3 month timeline, internal priority but no hard deadline
- 1: 6+ months out, no timeline pressure

#### + Fit

| Question | What you're looking for |
|----------|------------------------|
| "Are you primarily on AWS, or multi-cloud?" | AWS-primary is ideal fit |
| "How many engineers work on your product?" | 5-200 is sweet spot |
| "Do you have any compliance requirements?" | SOC2/ISO/PCI = higher value |

**Scoring:**
- 5: AWS-primary, 10-200 engineers, compliance needs, EU-based
- 3: Mixed cloud, small team, no compliance needs
- 1: Not on AWS, very large internal DevOps team, purely on-prem

---

## Qualification Score Matrix

| Criterion | Score (1-5) | Weight | Weighted Score |
|-----------|-------------|--------|----------------|
| Budget | | x2 | |
| Authority | | x2 | |
| Need | | x3 | |
| Timeline | | x2 | |
| Fit | | x1 | |
| **Total** | | **/50** | |

### Lead Classification

| Score Range | Classification | Action |
|-------------|---------------|--------|
| 40-50 | **HOT** | Propose immediately. Book follow-up within 48 hours. |
| 30-39 | **WARM** | Offer free Cost Health Check. Nurture with 1:1 attention. |
| 20-29 | **COOL** | Add to email nurture sequence. Check back in 30-60 days. |
| Below 20 | **NOT QUALIFIED** | Politely close. Add to newsletter list only. |

---

## Disqualification Triggers

Immediately disqualify if any of these are true:

- **Not on AWS** (and no plans to migrate) -- we're AWS-focused
- **Very large internal DevOps team** (10+) that is well-functioning -- they don't need us
- **Budget below $1K/month AWS spend** -- insufficient scale to justify our services
- **Looking for body leasing / staff augmentation only** -- not our model
- **Expects 24/7 support at Essential pricing** -- unrealistic expectations signal trouble
- **Red flag behavior:** aggressive negotiation before understanding value, demanding free work beyond Cost Health Check, disrespectful to team

---

## Package Recommendation Guide

After qualification, recommend based on fit:

| Primary Signal | Package | Typical Add-ons |
|---------------|---------|-----------------|
| "We have a DevOps person but need backup" | Safety Net (EUR 990) | Extra hours |
| "We have no DevOps team, small AWS footprint" | Essential (EUR 2,000) | FinOps |
| "Growing fast, need dedicated support" | Growth (EUR 4,000) | Solution Architect |
| "Complex environment, multiple teams" | Scale (EUR 6,000) | 24/7, DevSecOps |
| "Not sure yet, want to see value first" | Free Cost Health Check | -- |

---

## Post-Qualification Checklist

After every qualified call, complete within 24 hours:

- [ ] Score entered in pipeline tracker
- [ ] Follow-up email sent with summary + relevant materials
- [ ] Next meeting booked (calendar invite sent)
- [ ] Internal Slack update posted (#cps-sales)
- [ ] If HOT: proposal draft started
- [ ] If WARM: Cost Health Check scheduling initiated
- [ ] If COOL: added to nurture sequence with personalized note
