# ProSharp

## Quick Info

| Field | Value |
|-------|-------|
| **Status** | Active (project in progress) |
| **Package** | Fixed price project (Phase 1: OTel implementation) |
| **Contract Value** | EUR 11,900 net (revised from EUR 10,750 after scope dispute) |
| **Payment** | 50% upfront, 50% on completion |
| **TAM** | Szabolcs (took over from Gergely Bajan) |
| **Unit Members** | Szanto Zoltan (tech lead), .NET developer (onboarded for annotation) |
| **Client Contact** | Adam Kovacs (Development Manager, adam.kovacs@pro-sharp.hu) |
| **Related Entity** | TradeConnectors -- Mads Blankenburg (mads.blankenburg@tradeconnectors.org), Gabor Krizsanits |
| **Start Date** | 2026-01 (kick-off Jan 16) |
| **Deadline** | April 30, 2026 (extended from March 31) |

## What Is This Account

Pro-Sharp is a Budapest-based software company building GDSN (Global Data Synchronisation Network) solutions. Their key product is ProSharp.Gdsn.Web with an Item Editor module. Tech stack: AngularJS (frontend), C# (backend), MSSQL (database), Entity Framework.

TradeConnectors is a related entity (Danish connection) -- Mads Blankenburg and Gabor Krizsanits are involved.

CPS is implementing OpenTelemetry-based monitoring for their GDSN web app.

## Current Situation

**Project is actively in delivery.** A scope dispute in February was resolved through a 50/50 cost split. Szabolcs took over from Gergely Bajan as project lead. A .NET developer has been onboarded for trace annotation work.

Key deliverables:
1. Grafana docker-compose for local dev
2. Terraform infrastructure setup
3. OpenTelemetry Collector configuration
4. Application-level instrumentation (Item Editor spans for ~10 operations)
5. Documentation and knowledge transfer

Updated SOW (v3+) sent to client. MSA signed. Deadline extended to April 30, 2026.

## Key History

- **Jan 16, 2026:** Kick-off meeting
- **Jan 22-23:** Scoping Q&A (19 questions, detailed answers from Adam)
- **Jan 29-30:** Proposal negotiation, Phase 2 made optional at client request
- **Feb mid:** Work started
- **Feb 24:** Scope dispute surfaced -- Pro-Sharp expected full Item Editor span annotation in Phase 1, Sonrisa interpreted it as baseline auto-instrumentation
- **Feb 25:** Resolution meeting, misalignment acknowledged
- **Feb 26:** Szabolcs called Adam, agreed 50/50 split on extra effort. New price EUR 11,900.
- **Mar 5:** Contract review completed (MSA + SOW). Email to Mads drafted and sent.
- **Szabolcs took over** from Gergely Bajan as CPS project lead

## Scope Dispute Summary

Pro-Sharp expected Phase 1 to include full end-to-end span coverage for ~10 Item Editor operations (frontend-backend-SQL). Evidence supports their interpretation (scoping Q&A answers explicitly mention "10 end-to-end operations" and "frontend-backend-SQL"). Sonrisa's proposal language was ambiguous. Resolved professionally: Sonrisa absorbs 50% of extra annotation effort, price increased to EUR 11,900.

**Lesson learned:** Scoping Q&A answers must be explicitly reflected in SOW deliverables. Ambiguous scope wording creates risk.

## Open Items

- [ ] Complete Item Editor span annotations (in progress with .NET dev)
- [ ] Deliver by April 30 deadline
- [ ] Knowledge transfer to Pro-Sharp for extending to other modules
- [ ] Get acceptance certificate signed within 8 days of delivery
- [ ] Consider Safety Net (EUR 990/mo) upsell for post-project support

## Contract Notes

- **MSA risk:** Non-hire clause is aggressive (36 months, HUF 25M penalty). Cannot hire anyone who worked on this project for 3 years.
- **IP:** Full transfer to Pro-Sharp. Cannot reuse project-specific instrumentation patterns.
- **Late penalty:** 0.5%/day, capped at 10% (EUR 1,190 max). Pro-Sharp can deduct from invoices.
- **Termination:** Either party, 30 days notice, no reason needed.

## Profitability

Original EUR 10,750 for ~8 weeks work. After scope expansion, EUR 11,900 but absorbing ~EUR 2,500 extra effort (50/50 split). Likely thin margins on this project, but relationship value + potential Safety Net upsell.

## People

| Name | Company | Role | Contact |
|------|---------|------|---------|
| Adam Kovacs | Pro-Sharp | Development Manager | adam.kovacs@pro-sharp.hu |
| Mads Blankenburg | TradeConnectors | Stakeholder | mads.blankenburg@tradeconnectors.org |
| Gabor Krizsanits | TradeConnectors | Stakeholder | gabor.krizsanits@tradeconnectors.org |
| Ricardo Pardo | Pro-Sharp | Team member | ricardopardo@pro-sharp.hu |
| Gergely Matyas | Pro-Sharp | Team member | gergelymatyas@pro-sharp.hu |
| Szanto Zoltan | Sonrisa/CPS | Tech lead | szanto.zoltan@sonrisa.hu |
| Vaida Mark-Adam | Sonrisa/CPS | Team | vaida.mark@sonrisa.hu |
| Gergely Bajan | Sonrisa | Original project lead (handed off) | -- |

## Related Files

- Contracts (signed): `contracts/` subfolder
- Contract review: `contract_review.md`
- Email to Mads: `email_to_mads.md`
- SOW versions: multiple .docx files (v1-v6)
- MSA: `MSA_HUN_EN_SON_prosharp_v3.pdf` (signed)
