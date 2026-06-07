---
title: "Case Study: MVMI - Energy Platform Modernization"
description: "MVMI case study documenting the migration of Hungary's largest energy billing platform from monolithic to OpenShift microservices, accelerating releases from quarterly to bi-weekly while serving 3M+ households. Includes client profile, technical challenges, implementation approach, and business outcomes relevant to enterprise modernization prospects."
description_source: auto
description_hash: b222a6b71f53f3cf
id: cs-001
industry: energy
size: "3,000,000+ end customers, large enterprise"
country: HU
problem_type: migration, team-augmentation, 24x7-coverage, compliance
entry_package: Project-based (OpenShift consulting + hypercare)
current_package: Ongoing support
date_started: 2024
status: active
author: Sonrisa CPS
index_schema_version: 1
---
# Case Study: MVMI - Energy Platform Modernization

> **One-liner for outreach:** "We migrated Hungary's largest energy billing platform (3M+ households) from monolith to OpenShift microservices -- accelerating releases from quarterly to bi-weekly while maintaining zero downtime."

---

## Client Profile

| Field | Detail |
|-------|--------|
| **Industry** | Energy (gas and electricity billing) |
| **Company size** | Large enterprise, 3M+ household and commercial customers |
| **Location** | Hungary |
| **Tech stack** | SAP backend, OpenShift, Java, Angular, Grafana, Prometheus, OpenTelemetry, Jaeger, Kibana |
| **Founded** | Established national energy provider |
| **Name** | MVMI (shareable) |

---

## The Situation

MVMI operates OMNI, the central middleware and front-end platform connecting SAP systems to every customer touchpoint -- mobile apps, call centers, and self-service portals for millions of Hungarian households. After five years of development by vendor 4Sales, the monolithic on-premises architecture was limiting scalability, release speed, and operational resilience. MVMI launched a multi-year transformation to replatform OMNI into microservices on OpenShift, but lacked the internal DevOps expertise to execute it.

---

## The Problem

- **Legacy monolith:** Quarterly release cycles, bulky deployments, no agility
- **No DevOps capability:** Internal ops teams had zero OpenShift knowledge after years of planning
- **Organizational silos:** Infrastructure, operations, security, and network teams operated in isolation -- even firewall rule changes required a separate team
- **Testing bottlenecks:** Business UAT environments blocked technical load testing until just before releases, creating last-minute stability risks
- **National-scale risk:** Any failure could affect billing and account management for millions of households

---

## What We Did

- Designed and deployed OpenShift environments (test, staging, production) -- delivered in weeks, not months
- Implemented side-by-side infrastructure with L-shaped routing, allowing monolith and microservices to run concurrently during transition
- Rolled out a unified monitoring stack (Grafana, Prometheus, OpenTelemetry, Jaeger, Kibana) across both legacy and new systems
- Created a 24/7 hypercare service model for critical releases -- a new service tier designed specifically for MVMI
- Trained internal teams on DevOps and agile methodologies, ensuring knowledge transfer and long-term self-sufficiency
- Conducted DevOps maturity analysis across MVMI's verticals and delivered organizational restructuring recommendations
- Resolved live production issues during a critical August deployment -- optimized Java threading, queuing, and logging configurations over a four-day weekend hypercare window

---

## The Result

| Metric | Before | After | Timeframe |
|--------|--------|-------|-----------|
| Release frequency | Quarterly | Bi-weekly / monthly | First year |
| Major releases supported | ~4/year | 3 in under 1 year | First year |
| Scalability | Limited on-prem | 300-600 req/min validated | After migration |
| Environment build time | Months | Weeks | From day 1 |
| Post-rollout incidents | Stability concerns | Zero major incidents (3M+ accounts) | After August release |
| Monitoring visibility | Fragmented | Unified metrics, logs, and traces | After stack deployment |

**Summary:** Transformed Hungary's national energy platform from a fragile monolith with quarterly releases to a resilient microservices architecture delivering bi-weekly updates -- while maintaining uninterrupted service for over 3 million customers.

---

## Why They Chose CPS Over Hiring

MVMI had been planning this transformation for years but couldn't build internal DevOps/OpenShift capability fast enough. Hiring individual engineers would have meant months of ramp-up time on a platform they'd never seen. CPS brought an experienced team that was productive from week one, trained MVMI's own staff in parallel, and provided 24/7 hypercare during critical releases -- something no individual hire could deliver.

---

## Quotable

> "The OMNI migration was a major milestone for MVMI. Moving from a monolithic on-premises setup to OpenShift microservices improved our resilience, accelerated release cycles, and ensured stability for millions of customers. This project laid the foundation for our continued digital and cloud transformation."
> -- MVMI Leadership

---

## Relevance Tags

- **Industry:** `energy`
- **Problem type:** `migration`, `team-augmentation`, `24x7-coverage`
- **Company size:** `200-500+` (large enterprise)
- **Geography:** `HU`
- **Entry point:** Project-based consulting engagement, grew into ongoing support
- **Use for prospects like:** Energy companies, companies with monolithic legacy systems, companies needing OpenShift/Kubernetes expertise, national-scale platforms, companies that need 24/7 hypercare during critical releases
