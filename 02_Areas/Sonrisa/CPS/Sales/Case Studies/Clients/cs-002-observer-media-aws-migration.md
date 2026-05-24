---
title: "Case Study: Observer - Media Platform AWS Migration"
id: cs-002
industry: media
size: "Small-medium team, ~4TB production data"
country: Anonymized (EU)
problem_type: migration, replacement-hire, greenfield
entry_package: Project-based (migration + ongoing support)
current_package: Ongoing support (post go-live)
date_started: 2026-01
status: active
author: Sonrisa CPS
index_schema_version: 1
---

# Case Study: Observer - Media Platform AWS Migration

> **One-liner for outreach:** "We took over a 10-year-old media platform from a hostile vendor with zero documentation, migrated 4TB of production data to AWS EKS, and hit the go-live deadline -- all in under 3 months."

---

## Client Profile

| Field | Detail |
|-------|--------|
| **Industry** | Media monitoring / competitive intelligence |
| **Company size** | Small-to-medium |
| **Location** | EU (anonymized) |
| **Tech stack** | AWS EKS, MongoDB (1.8TB+), MySQL, Elasticsearch, S3, Site-to-Site VPN, Apache Nutch, Whisper transcription |
| **Founded** | Platform in operation for ~10 years |
| **Name** | Anonymized ("Observer") |

---

## The Situation

The client operates a media monitoring platform that aggregates news from online sources and traditional media (TV, radio, newspapers). The system crawls content, records broadcast streams, transcribes audio using AI (Whisper-class), consolidates results by keywords, and generates daily reports for end customers. The platform had been built and maintained by a third-party development team for a decade. The relationship with that vendor had deteriorated, and the client needed to take back control of their own product.

---

## The Problem

- **Hostile vendor handover:** The existing third-party dev team provided limited cooperation -- documentation was effectively absent, and knowledge transfer was "drip-fed" incrementally
- **No internal DevOps capability:** The client had no team capable of operating or migrating the platform independently
- **Legacy on-premises hosting:** Bare-metal infrastructure at a third-party facility with reliability concerns
- **Massive data footprint:** ~4TB of production data across MongoDB, MySQL, and Elasticsearch requiring careful migration
- **Tight deadline:** March 31 delivery milestone, April 18 go-live -- with discovery still ongoing
- **Hidden dependencies:** Undocumented schedulers, cron jobs, hardcoded connectivity assumptions, and environmental drift expected throughout

---

## What We Did

- Assembled a team of 1 architect, 3 cloud/DevOps engineers, and 2 application developers
- Built UAT environment on AWS from scratch: EKS cluster, networking, Site-to-Site VPN for hybrid connectivity
- Integrated all major application components into EKS: web crawler (Apache Nutch), application services (Wildfly), authentication (Keycloak)
- Planned and executed data migration: MySQL, MongoDB (1.8TB+), and Elasticsearch across environments
- Managed the on-premises integration for media subsystems (broadcast recording via Veranda, audio transcription via Whisper)
- Built production AWS infrastructure mirroring UAT with full validation
- Navigated hostile vendor dynamics -- absorbed the discovery burden, mapped undocumented dependencies, and progressively uncovered hidden workflows

---

## The Result

| Metric | Before | After | Timeframe |
|--------|--------|-------|-----------|
| Hosting | On-prem bare-metal (3rd party) | AWS EKS (client-owned) | ~3 months |
| Vendor dependency | Fully dependent, hostile handover | Independent operation with CPS | After go-live |
| Data migrated | 4TB across 3 DB engines | Successfully migrated | Pre go-live |
| Availability target | 99.5% monthly | 99.5% maintained | Ongoing |
| Peak performance | Fragile during 06:00-08:00 window | Scalable EKS, optimized for peak | Post-migration |
| Documentation | Effectively absent | Growing operational runbooks | Ongoing |

**Summary:** Took ownership of a decade-old media platform away from an uncooperative vendor, migrated the entire stack (application + 4TB of data) to AWS EKS, and delivered on a tight 3-month deadline -- transitioning seamlessly into ongoing support operations.

---

## Why They Chose CPS Over Hiring

Hiring individual engineers to reverse-engineer a 10-year-old undocumented platform while simultaneously migrating it to AWS on a 3-month deadline was not realistic. The client needed a team that could discover, architect, and execute in parallel -- and absorb the risk of unknown dependencies. CPS provided the complete team (architect + engineers + developers) with immediate AWS/EKS expertise, something that would have taken 6+ months to assemble through individual hires.

---

## Quotable

*(Client quote pending)*

---

## Relevance Tags

- **Industry:** `media`
- **Problem type:** `migration`, `replacement-hire`, `greenfield`
- **Company size:** `30-100`
- **Geography:** `EU`
- **Entry point:** Vendor replacement / platform takeover, evolved into ongoing managed support
- **Use for prospects like:** Companies stuck with a bad vendor, legacy platform migrations to AWS, EKS/Kubernetes migrations, companies with no internal DevOps team and a tight deadline, data-heavy migrations (multi-TB)
