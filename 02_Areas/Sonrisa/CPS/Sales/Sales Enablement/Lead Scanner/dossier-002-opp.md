---
title: Lead Dossier - Online Payment Platform (OPP)
version: 0.1
date: 2026-03-16
author: Sonrisa - Cloud Platform Services (CPS)
description: Pre-outreach research dossier for OPP, a Delft-based payment infrastructure company
id: b8ec9a6b-440f-4dcb-bed5-6ba2bbddf7ac
index_schema_version: 1
---

# Lead Dossier: Online Payment Platform (OPP)

**Priority: HOT -- #1 International Lead**
**Score: 9/10**

## Company Profile

| Field | Detail |
|-------|--------|
| Company | Online Payment Platform B.V. (OPP) |
| Founded | 2013 |
| HQ | Delft, Netherlands |
| Offices | Delft, Berlin, London |
| Employees | 100+ |
| Partner | Worldline (major payment processor) |
| Website | onlinepaymentplatform.com |
| Revenue | Processing billions in transactions yearly |
| Clients | eBay, Ikea, and other major e-commerce platforms |

## What They Do

OPP is a payment service provider built for **platform economy** -- marketplaces, e-commerce platforms, and multi-sided business models. They handle the complex payment flows (splitting, escrow, onboarding, compliance) that platforms need. Billions in transactions flow through their systems from companies like eBay and Ikea.

They are PSD2 regulated (listed on Open Banking UK), meaning they operate under strict financial compliance requirements.

## Their Tech Stack (Confirmed)

From their job postings, their infrastructure is well-documented:

| Layer | Technology |
|-------|-----------|
| Cloud | **AWS** (confirmed: EC2, Lambda, EKS) |
| Orchestration | **Kubernetes** (EKS) |
| IaC | **Terraform** (or CloudFormation) |
| CI/CD | **GitLab CI/CD** |
| Backend | **PHP** (core application) |
| Databases | **MySQL**, OpenSearch, Redis |
| Monitoring | Not specified (opportunity for CPS) |

## Why They're Hiring

OPP is currently hiring for **two infrastructure roles simultaneously**:

1. **DevOps Engineer** -- Salary up to EUR 70K, permanent contract. "You'll work with a sophisticated AWS environment combining EC2 instances and Kubernetes clusters."
2. **Site Reliability Engineer (SRE)** -- Focus on reliability, performance, and scaling.

**Hiring two infra roles at once = their current team is stretched.** This is classic CPS territory.

## Why This Matters for CPS

This is a **high-value, high-retention** lead:

1. **Mission-critical infrastructure** -- Payment processing cannot go down. Billions in transactions. Their clients (eBay, Ikea) have zero tolerance for downtime.
2. **Compliance-heavy** -- PSD2, Open Banking regulation. They need operational maturity and auditability.
3. **AWS-native** -- Their entire stack is on AWS. CPS is built for this.
4. **They're hiring TWO roles** -- A DevOps Engineer at EUR 70K + an SRE is roughly EUR 140-160K/year combined. CPS Scale (EUR 72K/year) + 24/7 (EUR 24K/year) = EUR 96K/year for a full team. **They save EUR 50-60K/year AND get a team instead of two individuals.**
5. **Long customer lifecycle** -- Payment platforms don't switch ops providers easily. Once CPS is embedded, this is a multi-year relationship.

## Leadership

| Name | Role | Notes |
|------|------|-------|
| CTO (name not publicly identified) | Technical decision-maker | Data team reports directly to CTO. Engineering office in Delft. |
| **Gijs Cooijmans** | Recruiter / HR | Contact for job postings: gijs.cooijmans@onlinepaymentplatform.com. NOT the decision-maker, but can be the door opener. |

**Gap:** CTO name not found publicly. Options:
- Check LinkedIn company page for C-level titles
- Contact Gijs Cooijmans referencing the DevOps/SRE roles as entry point
- Check if anyone at Sonrisa has connections to the Dutch fintech scene

## The Angle

**Payment infrastructure needs a team, not a person.** When their DevOps engineer goes on vacation or gets sick, who monitors the systems processing billions in transactions for eBay? A single hire is a single point of failure for mission-critical payment infrastructure.

### Specific value propositions for OPP:

1. **Immediate capacity** -- They're hiring 2 roles (3-6 month process). CPS starts in 2 weeks.
2. **Team > Individual** -- 3-4 engineers with backup coverage vs. 2 individual hires
3. **Cost advantage** -- EUR 96K/year (Scale + 24/7) vs. EUR 140-160K/year (2 hires + benefits + recruiting)
4. **Compliance alignment** -- Sonrisa has 19 years of enterprise experience, Lufthansa/Oracle audit history, SOC2/ISO readiness
5. **24/7 for payment systems** -- Our 24/7 add-on is built for exactly this: mission-critical systems that cannot have gaps in coverage
6. **Terraform + K8s + GitLab CI** -- Their exact stack is our core competency

## Suggested Package

**Scale (EUR 6,000/month) + 24/7 On-Call (EUR 2,000/month) = EUR 8,000/month**

This is a premium client. 120 hours/month + round-the-clock coverage for a payment platform processing billions. If they want Solution Architect advisory too, that's EUR 9,000/month total.

Annual value: EUR 96,000-108,000 -- one of the highest-value individual contracts CPS can land in Horizon 1.

## Draft Outreach

### Option A: Email to Gijs Cooijmans (Recruiter - Door Opener)

**Subject:** Alternative to your DevOps + SRE hiring -- managed team approach

> Hi Gijs,
>
> I noticed OPP is hiring both a DevOps Engineer and an SRE. Finding two strong infrastructure engineers at the same time is one of the hardest hiring challenges in the EU market right now.
>
> I lead Cloud Platform Services at Sonrisa Technologies -- we provide managed AWS operations teams at a fixed monthly price. For a payment platform like OPP, we offer 3-4 dedicated engineers with 24/7 coverage, starting within 2 weeks.
>
> The math: your two hires will cost roughly EUR 140-160K/year (salary + benefits + recruiting). Our Scale package with 24/7 support is EUR 96K/year -- and you get a team, not two individuals.
>
> I'm not suggesting you stop hiring -- but we could provide immediate capacity while you search, and you might find the team model works even better long-term.
>
> Would you be able to connect me with the right technical decision-maker to explore this? Happy to share more details.
>
> Best,
> [Szabolcs]

### Option B: LinkedIn to CTO (once identified)

> Hi [CTO Name],
>
> OPP processes billions in transactions for eBay and Ikea -- that's the kind of infrastructure that needs a team, not just a hire.
>
> I noticed you're looking for both a DevOps Engineer and an SRE. We provide exactly that capability as a managed AWS operations team: 3-4 engineers, 24/7 coverage, Terraform/K8s/GitLab expertise, starting in 2 weeks.
>
> We're Sonrisa Technologies (300+ engineers, EU-based, 19 years in business). Our team handles the same stack you're running: AWS EKS, Terraform, GitLab CI, MySQL -- and we've done it for compliance-heavy environments.
>
> Worth a 15-minute call to see if there's a fit?

## Action Items

- [ ] Find CTO name on LinkedIn (search OPP company page)
- [ ] Send email to Gijs Cooijmans this week
- [ ] Prepare OPP-specific Cost Health Check scope (focus on payment infrastructure optimization)
- [ ] If meeting booked: prepare compliance/security credentials overview (SOC2, ISO, audit history)
- [ ] Research Worldline connection -- any Sonrisa relationship with Worldline?
