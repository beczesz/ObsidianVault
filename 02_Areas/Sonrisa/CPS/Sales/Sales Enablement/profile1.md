---
title: "CPS Ideal Customer Profile #1: The Replacement Hire"
version: 0.2
date: 2026-05-13
author: Sonrisa - Cloud Platform Services (CPS)
description: Detailed definition of ICP Profile #1. For Profiles #2 (Scaling Company) and #3 (Cloud Cost Pain) see SALES_ENGINE.md.
id: 19405d12-c330-4bc9-8afc-b857523469f0
index_schema_version: 1
---

# CPS Ideal Customer Profile #1: "The Replacement Hire"

> **Scope note:** This file is the deep definition of **Profile #1 only**. The CPS sales engine now targets three ICP profiles in parallel. For Profile #2 ("The Scaling Company") and Profile #3 ("The Cloud Cost Pain"), see the ICP Profiles section of `Sales/SALES_ENGINE.md`. ENGINE B (Pain-Based Outbound) is the primary outreach motion as of 2026-04-27 and works across all three profiles.

## Profile Summary

Our ideal Profile #1 customer is an established, stable company that recently lost their only (or primary) DevOps/infrastructure person and is now scrambling to replace them. They are not looking for innovation -- they need someone to keep the lights on, reliably, starting immediately. CPS replaces the risk of a single hire with a team, at equal or lower cost, with no recruiting delay.

## Company Characteristics

| Attribute | Ideal | Acceptable | Disqualified |
|-----------|-------|------------|--------------|
| **Company age** | 5-20 years | 3-5 years | <3 years (startup risk) |
| **Total employees** | 30-200 | 20-30 or 200-500 | <20 (too small) or >500 (have platform team) |
| **Engineering team** | 5-30 developers | 3-5 developers | <3 (can't afford services) |
| **Annual revenue** | EUR 2M-50M | EUR 500K-2M | <EUR 500K (budget risk) |
| **Business model** | B2B SaaS, web platform, internal tooling | E-commerce, fintech, healthtech | Pure hardware, no cloud dependency |
| **Product maturity** | Production product with paying customers | Launched but early revenue | Pre-revenue, prototype stage |
| **Growth trajectory** | Stable or moderate growth (10-30%/year) | Flat (maintaining) | Hypergrowth (>100%) or declining |
| **Funding** | Bootstrapped or post-Series A with runway | Late seed with revenue | Pre-seed, burning cash |

## Infrastructure Profile

| Attribute | Ideal | Acceptable | Disqualified |
|-----------|-------|------------|--------------|
| **Primary cloud** | AWS | AWS + some Azure/GCP | No AWS, purely Azure/GCP |
| **Monthly AWS spend** | EUR 3,000-30,000 | EUR 1,000-3,000 | <EUR 1,000 (too small) |
| **Workload type** | Production SaaS, customer-facing app | Internal tools, data pipelines | Dev/test only, no production |
| **Infra complexity** | Moderate (EC2/EKS, RDS, S3, some IaC) | Simple (few EC2, basic setup) | Extremely complex multi-region |
| **DevOps team size** | WAS 1 person, NOW 0 | WAS 2, now 1 (overloaded) | 3+ (they have capacity) |
| **DevOps maturity** | Some Terraform, basic CI/CD, monitoring exists | Manual deployments, no IaC | Fully automated platform (don't need us) |

## The Trigger Event

The defining characteristic of this ICP is the **trigger**: something happened that created immediate, urgent need.

**Primary triggers (highest urgency):**
- DevOps person resigned or was let go
- DevOps person on extended leave (parental, medical, sabbatical)
- Single DevOps person gave notice, leaving in 2-4 weeks

**Secondary triggers (medium urgency):**
- Failed DevOps hire (3+ months searching, no suitable candidate)
- DevOps person promoted/moved to different role internally
- Developers refusing to keep doing infrastructure work
- Recent production incident caused by infrastructure gap

**Tertiary triggers (lower urgency, still valid):**
- Growing team realizes they need dedicated infra support
- CEO/CTO read about managed services and want to explore
- AWS bill growing faster than expected, need optimization

## The Buyer

| Attribute | Detail |
|-----------|--------|
| **Title** | CTO, VP Engineering, Head of Engineering, Technical Co-Founder |
| **Age** | 30-50 |
| **Background** | Software engineer who grew into leadership. Understands tech but not an infrastructure specialist. |
| **Emotional state** | Stressed, time-poor, carrying infrastructure burden personally. Worried about the next outage. |
| **Decision style** | Pragmatic, not visionary. Wants proof, not promises. |
| **Budget authority** | Can approve EUR 2,000-6,000/month without board approval |
| **Buying timeline** | Wants to solve this NOW. 1-4 week decision cycle. |

## What This Buyer Needs to Hear

**Primary message:** "You lost your DevOps person. We're a team that starts in 2 weeks, costs the same or less, and can't quit on you."

**Supporting messages:**
1. **Reliability over innovation:** "We keep things running. Boring, stable, predictable."
2. **Team over individual:** "One person is a single point of failure. We're 2-3 engineers with backup."
3. **No lock-in:** "Month-to-month after 3 months. If you hire someone great, we transition to backup (Safety Net) or step away."
4. **Immediate capacity:** "We start in 2 weeks. Your job ad will take 3-6 months to fill."
5. **Cost comparison:** "A senior DevOps engineer costs EUR 60-90K/year. Our Essential package is EUR 24K/year. Growth is EUR 48K/year for a full team."

**What NOT to say:**
- Don't lead with "managed services" (sounds corporate and abstract)
- Don't lead with "cloud optimization" (they want stability, not optimization)
- Don't talk about "digital transformation" (they hate buzzwords)
- Don't oversell capabilities (they want humble reliability, which aligns with CPS value #1: Alazat)

## Ideal Package Mapping

| Their situation | Package | Price | Why |
|----------------|---------|-------|-----|
| Lost their only DevOps person, simple setup | Essential | EUR 2,000/mo | 40h/month covers monitoring + basic ops |
| Lost DevOps person, moderate complexity | Growth | EUR 4,000/mo | 80h/month for proactive management |
| Lost DevOps person, mission-critical workload | Scale + 24/7 | EUR 8,000/mo | 120h + round-the-clock coverage |
| Have 1 DevOps person, want backup/insurance | Safety Net | EUR 990/mo | 6h/month consultation + standby |
| Interested but not ready to commit | Free Cost Health Check | EUR 0 | No-risk entry, demonstrates value |

## Upsell Path

1. **Entry:** Free Cost Health Check (shows savings, builds trust)
2. **Month 1-3:** Essential or Growth (immediate need fulfilled)
3. **Month 4-6:** Add FinOps (EUR 500/mo) after showing cost savings potential
4. **Month 7-12:** Add Solution Architect (EUR 1,000/mo) for strategic guidance
5. **If they grow:** Upgrade Essential to Growth, or Growth to Scale
6. **If they hire a DevOps person:** Downgrade to Safety Net (EUR 990/mo) -- still recurring revenue, team stays familiar

## Detection Signals (How to Find Them)

**Signal 1: Active job posting for DevOps/SRE/Platform Engineer**
- Platforms: Profession.hu, LinkedIn, Indeed, Glassdoor, company careers page
- Search terms: "DevOps engineer", "SRE", "platform engineer", "cloud engineer", "infrastructure engineer"
- Filter: company size 20-200, not a tech consulting/agency company

**Signal 2: Job posting has been live for 30+ days**
- Indicates failed hire attempt. Higher urgency. More receptive to alternatives.
- Check posting date on LinkedIn and job boards.

**Signal 3: Company recently removed DevOps person from LinkedIn**
- Former employee changed jobs, company LinkedIn shows gap in engineering team.

**Signal 4: AWS-related stack visible in job postings for OTHER roles**
- If their backend developer job mentions "some AWS knowledge helpful" or "occasional deployment tasks," it means developers are covering infra gaps.

## Geographic Priority

1. **Hungary** (Budapest, Szeged, Debrecen, Pecs) -- Home market, language advantage, personal network, can meet in person
2. **Romania** (Bucharest, Cluj-Napoca, Timisoara, Targu Mures) -- Sonrisa office presence, cultural proximity, cost-sensitive market (CPS value proposition strongest)
3. **DACH** (Germany, Austria, Switzerland) -- Higher budgets, larger market, English-speaking tech teams
4. **Benelux** (Netherlands, Belgium) -- Strong tech scene, good fit for CPS pricing
5. **Nordics** (Sweden, Denmark, Finland) -- Premium market, longer sales cycles

## Qualification Criteria (Must Meet ALL)

- [ ] Established company (3+ years, revenue-generating)
- [ ] Running production workloads on AWS
- [ ] DevOps team of 0-2 people (gap exists)
- [ ] Active trigger (hiring, incident, or person left)
- [ ] Decision-maker identifiable and reachable
- [ ] Company size 20-200 employees
- [ ] Not a competitor (not a DevOps/cloud consulting company)

## Why This Profile Wins for CPS

1. **Short sales cycle** -- They need help NOW, not in 6 months
2. **Obvious ROI** -- Direct comparison to hiring cost, easy to calculate
3. **Low churn risk** -- Stable companies don't switch providers for fun
4. **Natural upsell** -- Once they trust us, add-ons and upgrades flow naturally
5. **Reference potential** -- Stable companies make reliable case study partners
6. **Aligns with CPS values** -- We're being humble service providers, not disrupting their world. We're the backstage crew who runs the show.
