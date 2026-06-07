---
title: "Onriva"
date: 2026-03-31
author: Becze Szabolcs
status: active
description: "Active AWS operations account managing Onriva's myRiva travel SaaS platform across 80 EC2 instances with 72% profit margin; awaits TAM assignment decision and requires proactive communication to prevent missed issues despite client silence."
description_source: auto
description_hash: 6c573fae6bc79b18
id: 84aa9556-f98a-412c-8e5b-5114f66810eb
index_schema_version: 1
bdos_index: true
---
# Onriva

## Quick Info

| Field | Value |
|-------|-------|
| **Status** | Active |
| **Package** | Ongoing support (AWS operations) |
| **MRR** | TBD |
| **TAM** | UNDECIDED -- Kovacs Attila (KV) or Vaida Mark-Adam? Needs decision. |
| **Unit Members** | Vaida Mark-Adam, Gall Botond |
| **Client Contact** | Irina Kuznetsova (prod DB coordination), Sergey Kuznetsov |
| **Start Date** | Pre-2026 (established account) |
| **Contract End** | TBD |

## What Is This Account

Onriva operates myRiva, a travel-tech SaaS platform. CPS manages their AWS fleet (~80 EC2 instances), providing operations support, blue/green deployments, and off-peak coverage from EU timezone for a US-based service.

## Current Situation

Stable account, profitable (72% margin per workshop data). TAM assignment still needs to be formalized -- workshop identified KV (Kovacs Attila) or Mark as candidates but no final decision was made. Cost optimization report was already delivered.

Key concern from workshop: "Kliens csendjeben nem lehet megbizni" -- Onriva was mentioned as an example where client silence did not mean everything was OK.

## Key History

- Long-standing CPS client, one of the established accounts
- Cost optimization report delivered (v1 + Final version)
- Free cost optimization assessment used as "wrench service" / door opener -- Onriva responded immediately when 5 emails hadn't worked
- 72% profitability -- healthy account
- Case study created (cs-003): stabilized 80-instance AWS fleet, blue/green deployments

## Open Items

- [ ] **TAM decision: KV or Mark?** -- discuss with team and finalize
- [ ] Communicate TAM assignment formally to the unit and client
- [ ] Ensure proactive communication cadence (don't rely on client silence)

## Profitability

**72%** -- healthy, mentioned in workshop as a recovered "beteg projekt" (sick project) that's now running well.

## Technical Context

- **Product:** myRiva (travel technology platform, hosted on AWS)
- **Infrastructure:** ~80 EC2 instances, RabbitMQ, AWS RDS (Fintech DB)
- **Architecture concerns:** Travel Marketplace monolith (Ignite, Liferay) flagged for decomposition. Booking tables at ~7GB+ (DB growth concern).
- **Bi-weekly syncs:** Teams calls (20:00-20:30 UTC+2)
- **Ticket prefixes:** WEB- (product issues), TECHOPS- (infrastructure)

## People

| Name | Role | Contact |
|------|------|---------|
| Irina Kuznetsova | Onriva -- prod DB coordination (DBA/eng lead) | -- |
| Sergey Kuznetsov | Onriva/CPS | -- |
| Denis Viktorov | CPS -- primary technical contact, day-to-day AWS ops | -- |
| Vaida Mark-Adam | CPS -- meeting notes, bi-weekly sync attendee | vaida.mark@sonrisa.hu |
| Banfi Istvan | CPS/Onriva -- attendee | -- |
| Gall Botond | CPS/Onriva -- attendee | -- |
| Ceclan Sandor | CPS -- occasionally absent | -- |

## Open Tickets (as of Feb 2026)

| Ticket | Topic | Owner | Status |
|--------|-------|-------|--------|
| WEB-16205 | OnTelligent Analytics export fails (RabbitMQ recreated, LB investigation pending) | Denis Viktorov | In Progress |
| TECHOPS-5522 | RDS upgrade (Fintech DB). Test done, prod to schedule with Irina | CPS + Irina | Pending scheduling |
| TECHOPS-5523 | MQ planned lifecycle event (missing AWS instance info) | Denis Viktorov | Investigating |
| Strategic | Travel Marketplace monolith decomposition | TBD | Flagged |
| Strategic | Booking tables ~7GB+ DB growth concern | TBD | Flagged |

## Related Files

- Case study: `Sales/Case Studies/Clients/cs-003-onriva-travel-aws-operations.md`
- Cost Optimization Report (Final): `Accounts/Active/Onriva/Cost Optimization Report - Onriva (Final).pdf`
- Cost Optimization Report (v1): `Accounts/Active/Onriva/Cost Optimization Report - Onriva v1.pdf`
