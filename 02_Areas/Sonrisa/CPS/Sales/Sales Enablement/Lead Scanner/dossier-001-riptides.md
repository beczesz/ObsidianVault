---
title: Lead Dossier - Riptides
version: 0.1
date: 2026-03-16
author: Sonrisa - Cloud Platform Services (CPS)
description: Pre-outreach research dossier for Riptides, a Budapest-based non-human identity security startup
id: fa25412a-8a20-42d9-92d7-189fc407d3a3
index_schema_version: 1
---

# Lead Dossier: Riptides

**Priority: HOT -- #1 Local Lead**
**Score: 9/10**

## Company Profile

| Field | Detail |
|-------|--------|
| Company | Riptides (Riptides Labs Inc.) |
| Founded | 2024/2025 |
| HQ | Budapest, Hungary |
| Employees | ~10-15 (estimated, early stage post-funding) |
| Stage | Pre-seed ($3.3M -- largest in CEE history) |
| Investors | PortfoLion Capital Partners (HU), Kaya VC (CZ) |
| Website | riptides.io |
| LinkedIn | linkedin.com/company/riptides-ai |

## What They Do

Riptides builds a platform for **non-human identity management** -- securing machine-to-machine communication (services, workloads, AI agents) using the SPIFFE standard. Their platform issues and rotates identities automatically, enforces identity at the kernel level (not user space), and includes dashboards for credential inventory and compliance reporting.

In plain terms: as companies deploy more microservices and AI agents, every service needs an identity (like a passport) to talk to other services securely. Riptides automates this.

## Why This Matters for CPS

This is a cloud-native security product that runs **on top of Kubernetes**. Their entire platform depends on:
- Kubernetes clusters (they use K8s metadata for identity building)
- AWS or cloud infrastructure (hybrid deployment model: control plane as managed service, enforcement runs locally)
- CI/CD pipelines for rapid iteration
- Infrastructure as Code
- High availability (security infrastructure cannot go down)

They're a 10-15 person team. Their founders are infrastructure experts (ex-Banzai Cloud, Cisco), so they know what good ops looks like. But post-funding, their priority is **building the product and getting customers**, not running infrastructure. Every hour a founder spends on ops is an hour not spent on product-market fit.

## Leadership (Decision Makers)

| Name | Role | Background | Approach |
|------|------|------------|----------|
| **Marton Sereg** | CEO & Co-Founder | Co-founded Banzai Cloud (acquired by Cisco), SequenceIQ (acquired by Hortonworks). Serial entrepreneur, deep K8s/cloud expertise. | Strategic decision-maker. Understands infrastructure intimately. Won't respond to generic pitches. Needs peer-level conversation. |
| **Janos Matyas** | Head of R&D & Co-Founder | Same exits as Sereg. Pipeline architecture, cloud-native systems. | Technical decision-maker. Will evaluate CPS on engineering quality. |
| **Zsolt Varga** | CTO & Co-Founder | Early Banzai Cloud hire, became key member. | Day-to-day tech leader. Most likely to feel infrastructure ops burden. |
| **Nandor Istvan Kracser** | CISO & Co-Founder | 15+ years building secure infrastructure at Cisco and IBM. | Security-focused. Will care about CPS's security practices and compliance posture. |

## The Angle

**Do NOT pitch managed services to these founders the traditional way.** They built Banzai Cloud -- they know more about Kubernetes operations than most DevOps engineers. A standard "we'll manage your AWS" pitch will fall flat.

**Instead, the angle is: "You've done this before. You know how much ops eats into founder time during the 0-to-1 phase. Let us handle the boring stuff so you can focus on building what only you can build."**

The pitch is about **founder time allocation**, not about technical capability they lack.

### Specific value propositions for Riptides:

1. **Founder time liberation** -- With $3.3M and 12-18 months runway, every founder-hour on ops instead of product/sales is wasted capital
2. **CPS as scaling insurance** -- When they land their first enterprise customers, those customers will demand SLAs. CPS gives them instant operational maturity.
3. **Complementary expertise** -- They're identity/security experts. CPS handles the underlying infrastructure layer (compute, networking, monitoring, CI/CD) so they stay focused on their layer.
4. **Shared DNA** -- Sonrisa is also a Central European tech company. Same timezone, same culture, can meet in person in Budapest.

## Suggested Package

**Essential (EUR 2,000/month)** to start, growing to Growth as they scale.

At their stage, 40 hours/month covers monitoring, basic incident response, CI/CD maintenance, and cost optimization. As they onboard enterprise customers and need better SLAs, upgrade to Growth + 24/7.

## Connection Map

**Do you know any of these people?**
- Marton Sereg and Janos Matyas are well-known in the Budapest Kubernetes/cloud-native community
- They did a "First Monday" event with Kaya VC and PortfoLion -- other portfolio companies might be mutual connections
- Banzai Cloud was acquired by Cisco -- any Sonrisa connections to Cisco Hungary?
- The Hungarian startup ecosystem is tight -- check with Szurdi Miklos or other contacts

**If you have a mutual connection:** Use Sequence D (Referral). A warm intro is 5x more effective than cold outreach.

**If no mutual connection:** Use the approach below.

## Draft Outreach

### Option A: LinkedIn Message (Hungarian, personal from Szabolcs)

> Szia Marton,
>
> Gratulalok a Riptides pre-seed korohoz -- rekord meret a regioban, megerdmelten.
>
> Szabolcs vagyok a Sonrisa Cloud Platform Services-tol. Tudom, hogy a Banzai Cloud hatterted alapjan az infrastruktura ops nem ismeretlen terep szamodra. De pontosan ezert gondolom, hogy most, a 0-to-1 fazisban az utolso dolog, amire a founderek idejet kellene forditani, az a K8s cluster karbantartasa es a CI/CD pipeline debuggolasa.
>
> Mi pont ezt csinaljuk -- kezeljuk az AWS infrat fix havi aron, hogy a csapat a termekre fokuszalhasson. Nem egy generic MSP vagyunk: 300+ mernokkel dolgozo EU-s ceg, Budapestrol.
>
> Erdekelne egy kave, hogy megbeszeljuk, van-e ertelme?

### Option B: LinkedIn Message (English, if they prefer English)

> Hi Marton,
>
> Congrats on the Riptides pre-seed -- record-breaking for CEE, well deserved.
>
> I lead Cloud Platform Services at Sonrisa Technologies (300+ engineers, Budapest-based). Given your Banzai Cloud background, I know you understand infrastructure ops better than most. Which is exactly why I think you'd rather not spend founder time on it during the 0-to-1 phase.
>
> We manage AWS infrastructure at a fixed monthly price -- monitoring, CI/CD, incident response -- so teams like yours can stay focused on product. Not a generic MSP pitch; happy to show you what makes us different.
>
> Coffee in Budapest to discuss? Or a quick 15-min call if that's easier.

### Timing

**Reach out this week.** They raised in April 2025, so they've had almost a year to start building. They're likely past initial prototype and heading toward first enterprise customers. This is the moment when ops maturity starts to matter.

## Red Flags / Risks

- **They might insist on doing ops themselves** -- founders with deep infra background often want to keep control. Counter: "We're not replacing your expertise, we're giving you leverage."
- **Budget sensitivity** -- pre-seed stage, EUR 2,000/month might feel significant. Counter: frame it as less than a part-time contractor, and it frees up founder hours worth 10x that.
- **They might already use a managed K8s service** (EKS, GKE) and feel "managed enough." Counter: managed Kubernetes is not managed operations. EKS handles the control plane; CPS handles everything else.

## Success Criteria

- [ ] Identify if mutual connection exists (check this week)
- [ ] Send LinkedIn message (by Friday)
- [ ] Get response and book meeting
- [ ] Offer free Cost Health Check as low-friction entry
- [ ] If engaged: propose Essential package pilot (3 months, personal Szabolcs involvement)
