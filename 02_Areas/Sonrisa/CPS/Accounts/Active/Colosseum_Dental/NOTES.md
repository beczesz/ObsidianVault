# Colosseum Dental

## Quick Info

| Field | Value |
|-------|-------|
| **Status** | Active -- URGENT |
| **Client Entity** | Colosseum AG, Talstrasse 70, 8001 Zurich, Switzerland |
| **Industry** | Healthcare / Dental clinic chain |
| **Package** | Project-based (SOW #3: 54 days estimated, T&M at EUR 546/day) |
| **Budget Cap (SOW #3)** | EUR 29,484 |
| **Total Contract Value** | EUR 46,944 across 3 SOWs (EUR 12,000 + EUR 5,460 + EUR 29,484) |
| **MRR** | None yet -- Managed Service proposal ready at EUR 1,950/month |
| **TAM** | Kovacs Marcell |
| **Unit Members** | Gall Botond, Szanto Zoltan |
| **CPS Contact** | Becze Szabolcs (becze.szabolcs@sonrisa.hu) |
| **Client Contacts** | Csaba Gaspar (csaba.gaspar@colosseumdental.com), Daniel Fehr (CFO), Raoul Dias (Chief HR & Legal Officer), Rachel Benevenuto (contract admin) |
| **MSA Signed** | July 16-25, 2025 (DocuSign) |
| **SOW #3 Effective** | January 29, 2026 |
| **Contract End** | May 2026 (HARD DEADLINE for SOW #3) |
| **Next Phase** | Contract renewal/extension review (initiated 2026-04-02) |

## What Is This Account

Colosseum AG is a major European dental clinic chain headquartered in Zurich. They run a complex Azure-based integration platform (Azure Logic Apps + Azure Functions) that connects Microsoft Dynamics 365 with multiple external systems (Coupa, Jaggaer, OpusCapita, Henry Schein, SAP SuccessFactors, Tagetik, Mercur, Exquise PMS, etc.). The platform was originally built by KPMG (technical design document dated Jan-May 2023) and manages 51 workflows across 6+ environments.

Sonrisa/CPS took over support and stabilization work starting mid-2025, replacing what appears to have been an earlier AMS arrangement (a 2023 contract proposal from DNL/NP exists in the archive). The engagement has grown through 3 successive SOWs from discovery to full stabilization.

## Engagement History

### SOW #1 -- Discovery & Audit (May-Aug 2025)
- **Scope:** Comprehensive audit and optimization of Azure Logic Apps supporting D365 data exchange. Technical discovery, architecture review, log analysis, documentation, and recommendations.
- **Effort:** 22 days estimated, EUR 12,000 budget cap, EUR 546/day
- **Deliverable:** Technical documentation report (analysis, issues, root causes, recommendations)
- **Term:** Effective May 22, 2025, valid until August 31, 2025
- **Status:** COMPLETED. Signed July 16, 2025 (DocuSign).

### SOW #2 -- Short-term Stabilization (Oct-Nov 2025)
- **Scope:** Corrective and performance improvement measures: resolving performance bottlenecks (separating outbound integration triggers), fixing INT02 bankStmtImport status update logic, adjusting file transformation pattern (disabling async mode), implementing retry logic for Function App calls.
- **Effort:** 10 days estimated, EUR 5,460 budget cap, EUR 546/day
- **Term:** Effective October 27, 2025, 30-day termination notice
- **Status:** COMPLETED. Signed November 4, 2025 (DocuSign).

### SOW #3 -- Long-term Stabilization & Cost Optimization (Jan 2026 - May 2026)
- **Scope:** Long-term stabilization, scalability, and cost-optimization improvements:
  - Storage table scalability (archive old records, introduce queue-based processing, blob storage for files)
  - Status update logic fixes (error handling for missing files, tracking via table not blob)
  - Cost optimization in non-production environments (remove unused resources, consolidate test envs, migrate to cheaper service plans)
- **Effort:** 54 days estimated, EUR 29,484 budget cap, EUR 546/day
- **Term:** Effective January 29, 2026, 30-day termination notice
- **Status:** IN PROGRESS -- BEHIND SCHEDULE. May 2026 deadline ~28 days away as of 2026-04-02.

### Proposed: Managed Services Agreement (not yet signed)
- **Scope:** Ongoing monitoring, diagnosis, and remediation of 51 Azure Logic Apps workflows. Quick fixes (up to 30 min) included; larger work billed T&M at EUR 68.25/hour.
- **Pricing:** EUR 1,950/month (43 Simple @ EUR 35, 5 Moderate @ EUR 50, 3 Advanced @ EUR 65)
- **SLAs:** P1 response 1h, P2 2h, P3 4h, P4 1 business day. Mon-Fri 8AM-5PM CET.
- **Team:** TAM + Service Manager + Support Engineers
- **Term:** 12 months, auto-renewing with 45-day non-renewal notice
- **Status:** PROPOSED (v1.1 ready). This is the natural next step after SOW #3 concludes.

## Current Situation

**URGENT.** May 2026 deadline for SOW #3 is approaching (~28 days remaining as of 2026-04-02) and delivery is behind schedule. Time was lost due to Idzsi being in Indonesia and credential access problems. The exact number of remaining days is unclear -- needs an immediate status check with the unit.

Szabolcs needs to communicate the status to Csaba Gaspar but first needs clarity on what to tell him.

**NEW (2026-04-02):** Contract renewal/extension review initiated. Client wants to continue the engagement beyond the current May 2026 deadline. Contract document to be reviewed once provided. This is a positive signal -- the relationship is strong enough that they want to extend. The Managed Services SOW (EUR 1,950/month) is ready as a proposal for the recurring phase.

## Key People (Client Side)

- **Csaba Gaspar** (csaba.gaspar@colosseumdental.com) -- Main operational contact, CC'd on all contracts
- **Daniel Fehr** -- CFO, contract signer
- **Raoul Dias** -- Chief HR & Legal Officer, contract signer
- **Rachel Benevenuto** (rachel.benevenuto@colosseumdental.com) -- Contract admin/DocuSign originator
- **Petteri Pasanen** (petteri.pasanen@colosseumdental.com) -- Electronic communications contact

## Technical Context

- **Platform:** Azure Integration Framework (AIF) -- Azure Logic Apps + Azure Functions + D365 F&O
- **Original architect:** KPMG (Benjamin Axiaq, Kevin Agius, Jesmond Darmanin -- technical design doc v0.22, May 2023)
- **Workflows:** 51 total (43 Simple, 5 Moderate, 3 Advanced by complexity index)
- **Environments:** 6+ (env03-env06 identified, some unused/redundant -- cost optimization target)
- **Key integrations:** Coupa (payments, bank statements), Jaggaer (procurement), OpusCapita (master data, invoices), Henry Schein (POs), SuccessFactors (HR), Tagetik (consolidation), Mercur (financial), Exquise PMS (patient data)
- **Known issues:** Storage table query timeouts, status update failures on missing files, 6 workflows need splitting, async file transformation problems

## Effort Estimation (SOW #3 / Part 4)

| Task | Min (days) | Max (days) |
|------|-----------|-----------|
| Storage table scalability -- archive old records | 6 | 11 |
| Storage table scalability -- queue-based processing | 14 | 18 |
| Status update fix -- error handling for missing files | 4 | 6 |
| Status update fix -- tracking via table (long-term) | 8 | 12 |
| Cost optimization -- research & review | 4 | 6 |
| Cost optimization -- implementation | 8 | 12 |
| **Total** | **44** | **65** |

Cost optimization potential: ~$550/month savings on test environments (Bastion service removal, env consolidation, plan migrations).

## Open Items

- [ ] **CONTRACT REVIEW: Review renewal/extension contract** -- document to be uploaded, review terms, flag key clauses
- [ ] **URGENT: Status meeting with unit (Marci, Boti, Zoli)** -- how many days used, how many remain, what's blocking
- [ ] Szabolcs communicates status to Csaba (once we know the real situation)
- [ ] Assess if May deadline is achievable
- [ ] Plan recovery if behind schedule
- [ ] Define terms for extended engagement (scope, pricing, duration)
- [ ] Decide whether to propose Managed Service SOW alongside or after the extension

## Profitability

| Item | Value |
|------|-------|
| SOW #1 revenue | EUR 12,000 (budget cap) |
| SOW #2 revenue | EUR 5,460 (budget cap) |
| SOW #3 revenue | EUR 29,484 (budget cap) |
| **Total project revenue** | **EUR 46,944** |
| Daily rate | EUR 546 |
| Proposed MRR (Managed Service) | EUR 1,950/month |
| T&M rate (Managed Service) | EUR 68.25/hour |

## Folder Structure

```
Colosseum_Dental/
  NOTES.md                    -- THIS FILE
  Contracts/
    Signed/                   -- Executed documents
      20250716_Sonrisa_MSA_final.pdf
      20251104_Sonrisa_Second SOW_final.pdf
      DocuSign_Certificate_MSA.pdf
    Active/                   -- Current SOW being delivered
      20260129_Sonrisa_Third SOW_cmts legal v1.docx
      20260129_Sonrisa_Third SOW_cmts legal v1.pdf
    Proposed/                 -- Ready to present but not signed
      Managed_Service_SOW_v1.1.docx
      Managed_Service_SOW_v1.0.pdf
      SOW4_Effort_Estimation_v2.pdf    (D365 export + Terraform drift, 13-22 days)
      SOW4_Effort_Estimation_v2.xlsx
  Drafts/                     -- Rachel's reviewed SOW3 (20260219)
  Technical/
    SOW3_Effort_Estimation - Azure Logic App Stabilization Part 4.pdf
    CDG - AIF Technical overview - v0-22.pdf   (KPMG original, May 2023)                  -- Technical documentation and estimations
    CDG - AIF Technical overview - v0-22.pdf   (KPMG original, May 2023)
    Effort Estimation v2.pdf
    Effort Estimation v2.xlsx
    Azure Logic App Stabilization Part 4 - Effort Estimation v2.pdf
  Legacy/                     -- Pre-Sonrisa documents
    20230713 CDG_D365_AMS_Contract Proposal_DNL_NP.docx
  raw/                        -- ORIGINAL DUMP (kept as backup, can be deleted once verified)
```

## Duplicate/Redundant Files in raw/ (not copied to organized structure)

- `raw/20250702_Sonrisa_SWO_ALA_v2_cmts CDG.pdf` -- PDF export of same .docx (kept docx in Drafts)
- `raw/Managed Services Agreement - Azure Logic App - SOW.pdf` -- Older v1.0, superseded by v1.1
- `raw/Managed Services Agreement - Azure Logic App.pdf` -- MSA portion without SOW, redundant with signed MSA
- `raw/Managed Service/Managed Services Agreement - Azure Logic App - SOW v1.1.pdf` -- PDF of v1.1, kept docx
- `raw/Managed Service/Statement of Work No. COL_SON_SOW_02.docx` -- v1.0, superseded by v1.1

## Related Files

- Referenced in: `TASKS.md` (Colosseum Dental section)
- Workshop summary: `Team/Workshop Summary 2026-03-24.md`
