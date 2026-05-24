---
title: CPS Lead Scanner - ENGINE B Scan (Pain-Based)
date: 2026-04-01
type: engine-b-scan
author: Claude (orchestrating Perplexity + web search)
description: First ENGINE B scan -- Hungarian product companies matching ICP regardless of job postings
id: 4702182e-9be8-4d8a-b1aa-429b59dbc2f0
index_schema_version: 1
---

# ENGINE B Scan -- 2026-04-01

## Summary

First pain-based ENGINE B scan targeting Hungarian product companies (not IT consulting/outsourcing) with 30-200 employees running cloud infrastructure. Instead of looking for DevOps job postings, we identified companies where CPS can lead with "cloud cost leaks + operational risks."

**Companies found:** 10+ Hungarian product companies
**Method:** Perplexity research + web search (GetLatka, Wellfound, EU-Startups, AWS partner pages)

## ENGINE B Targets

### Tier A -- Strong ICP Match (pursue first)

**1. SEON (seon.io) -- Fraud Detection SaaS**
- Budapest | 100-200 employees | Fintech
- Cloud: AWS-style infra, microservices, CI/CD (from job posts and tech profiles)
- Why CPS: Global SaaS with low-latency APIs = high infra complexity. Fraud detection = zero-downtime requirement. NIS2/DORA compliance pressure as fintech.
- Outreach angle: "Cloud cost efficiency + compliance posture for a scaling fintech"
- Package: Essential EUR 2,000/mo or Growth EUR 4,000/mo

**2. Lensa (lensa.com) -- Job Matching Platform**
- Budapest (HQ) | 100-200 employees | HR SaaS
- Cloud: AWS CONFIRMED -- listed by Amazon as Hungarian ISV using AWS
- Why CPS: High-traffic SaaS with recommendation/data-processing workloads. Feature velocity = DevOps under pressure.
- Outreach angle: "We help AWS-native SaaS companies stabilize infra and cut 15-30% cloud waste"
- Package: Essential EUR 2,000/mo + FinOps EUR 500/mo

**3. Barion Payment (barion.com) -- Payment Processor**
- Budapest | 50-150 employees | Fintech
- Cloud: Payment APIs + real-time processing = cloud-native, likely AWS or Azure
- Why CPS: Payment processing = zero downtime, PCI-DSS compliance. NIS2/DORA directly applies. Scaling across CEE.
- Outreach angle: "Payment infra serving merchants needs bulletproof ops + cost visibility"
- Package: Essential EUR 2,000/mo + DevSecOps EUR 700/mo

**4. Loxon Solutions -- Banking Software**
- Budapest | Mid-sized | Fintech/Banking
- Cloud: AWS CONFIRMED -- named by Amazon as Hungarian ISV using AWS. Transitioning from on-prem to cloud-hosted for banking clients.
- Why CPS: Regulated banking clients = NIS2/DORA compliance critical. Cloud migration in progress = needs DevOps bandwidth.
- Outreach angle: "NIS2-aware cloud operations for banking software providers"
- Package: Growth EUR 4,000/mo + DevSecOps EUR 700/mo

**5. Pentech (pentech.hu) -- Digital Factoring**
- Budapest | 30-60 employees | Fintech
- Cloud: Cloud-native product, scalable architecture, API integrations
- Why CPS: Mid-stage fintech with likely 1-2 DevOps people. Transaction volume growth = cost control + security posture matter.
- Outreach angle: "Your factoring platform needs reliable ops as transaction volume scales"
- Package: Safety Net EUR 990/mo or Essential EUR 2,000/mo

### Tier B -- Good Fit, Needs Research

**6. Chemaxon (chemaxon.com) -- Chemistry Informatics**
- Budapest | ~100-200 employees | Pharma/Biotech SaaS
- Cloud: Likely AWS/Azure for compute-heavy chemistry simulations and APIs
- Why CPS: Pharma clients = compliance-heavy. Data-intensive workloads = cost optimization opportunity.
- Outreach angle: "Compute-heavy SaaS needs FinOps discipline + reliable platform ops"
- Package: Essential EUR 2,000/mo + FinOps EUR 500/mo

**7. Colossyan (colossyan.com) -- AI Video Platform**
- Budapest | Growing | AI/Media
- Cloud: GPU clusters, media pipelines = cloud-intensive, likely AWS
- Why CPS: GPU/compute cost optimization is critical. Small infra team juggling autoscaling + availability.
- Outreach angle: "AI companies waste 30-40% on GPU compute without FinOps discipline"
- Package: Essential EUR 2,000/mo + FinOps EUR 500/mo
- Note: Highlighted in "most promising Hungarian startups 2026"

**8. ABZ Innovation (abzinnovation.com) -- Drone/AgriTech**
- Budapest | 30-70 employees | AgriTech/IoT
- Cloud: EUR 7M funding (2026) earmarked for platform capabilities, implying cloud-backed services
- Why CPS: Hardware + SaaS = small but overworked backend/DevOps. Transitioning from prototype to production.
- Outreach angle: "Fractional platform team for your IoT/SaaS backend"
- Package: Safety Net EUR 990/mo

### Tier C -- Monitor / Early Stage

**9. TrustChain -- Privacy/Compliance**
- Budapest | Small | RegTech
- Why CPS: Compliance-focused company likely needs compliant infra itself
- Action: Research further, may be too small

**10. Semeris -- Data/Analytics**
- Budapest | Small-mid | Data
- Why CPS: Data workloads = cloud cost optimization
- Action: Research further

## Outreach Priority Order

1. **KBOSS/Szamlazz.hu** (14/15, already validated, outreach draft ready) -- KAN-8
2. **Allonic** (Profile #2, $7.2M, fractional platform team pitch) -- KAN-9
3. **Barion Payment** (fintech, NIS2/DORA, payment compliance)
4. **Loxon Solutions** (banking software, AWS confirmed, NIS2/DORA)
5. **SEON** (fraud SaaS, scaling, compliance)
6. **Lensa** (AWS confirmed by Amazon, cost optimization)
7. **Pentech** (small fintech, Safety Net entry)
8. **Chemaxon** (pharma SaaS, compute-heavy)
9. **Colossyan** (AI, GPU cost optimization)
10. **ABZ Innovation** (drone/agritech, Safety Net entry)
11. **CIG Pannonia** (warm, compliance angle follow-up) -- KAN-6
12. **Greenergy** (stale, check LinkedIn connect status) -- KAN-5

## Messaging Templates for ENGINE B Targets

**Template A (Fintech/Compliance):**
"Hi [Name], we work with Hungarian fintech/SaaS companies on AWS and consistently find two things: 20-30% cloud cost waste from unoptimized resources, and single-point-of-failure risks around cloud operations. With NIS2 now in effect, these become compliance exposure, not just inefficiency. We run a 60-min Cloud Health Check (read-only, no disruption) to validate this. Worth a quick look?"

**Template B (Scaling SaaS):**
"Hi [Name], companies at your stage on AWS typically have 1-2 people managing all cloud infrastructure. That works until it doesn't -- a scaling incident, a cost spike, or a key person leaving can halt product delivery. We provide a 13-person managed DevOps team at a fraction of one senior hire's cost. Happy to show what we'd find in a 60-min Cloud Health Check."

**Template C (Startup/Fractional):**
"Hi [Name], congrats on the [funding/growth]. Scaling from [X] to [Y] employees means your cloud infra needs grow faster than your team can hire for it. We act as your fractional platform team -- your engineers focus on product, we handle cloud ops, CI/CD, monitoring, and cost optimization. Starting at EUR 990/month."
