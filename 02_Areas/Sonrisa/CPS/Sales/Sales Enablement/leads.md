---
title: CPS Lead Research Dossiers
version: 1.1
date: 2026-05-13
author: Sonrisa - Cloud Platform Services (CPS)
status: active
description: Per-lead deep research dumps that fed the Pipeline. Not a pipeline tracker. For lead stages see Sales/Pipeline.md. For rolling per-account notes see Accounts/Leads/<name>/NOTES.md.
dashboard_contract: Sales/DASHBOARD_CONTRACT.md
dashboard_note: "Live source for the dashboard drawer enrichment. Format: `### CompanyName` per lead, then `- **Field:** value` bullets. Multi-line values are NOT parsed. Read DASHBOARD_CONTRACT.md before adding new field names you want surfaced."
id: 89775650-0730-4fae-a658-d81d5ceb4ecf
index_schema_version: 1
---

<!--
  ===========================================================================
  LIVE DATA SOURCE for Sales/dashboard.html. Polled every 8s.
  ===========================================================================
  This file feeds the per-lead drawer content. The dashboard matches each
  dossier here to a Pipeline.md card via a smart name key that strips
  parens, slashes, and corporate suffixes (Kft, Zrt, Inc, hu, com, etc.).

  PER-LEAD HEADER:
      ### CompanyName
      (optional)  ### CompanyName -- Score: 14/15 -- HOT

  FIELD BULLET FORMAT (single-line values only, multi-line is NOT parsed):
      - **Location:** ...
      - **Company:** ...   (auto-extracts founded year + employee count)
      - **Signal:** ...    (or **Signal history:**)
      - **AWS stack:** ...
      - **Decision-maker:** ...
      - **Pain points:** (1) ... (2) ... (3) ...    <-- numbered for clean split
      - **CPS fit:** ...
      - **Best outreach angle:** ...
      - **Recommended package:** Essential EUR 2,000/mo + FinOps EUR 500/mo
      - **Scoring:** Maturity 3/3 | Posting age 3/3 | AWS 2/3 | Team gap 3/3 | Geo fit 3/3
      - **Next step:** ...

  Any other `- **Field:**` is captured but not given a dedicated drawer slot.

  FULL CONTRACT: Sales/DASHBOARD_CONTRACT.md
  ===========================================================================
-->

# CPS Lead Research Dossiers

> This file holds the one-time deep research dumps per lead. Pipeline stage and current outreach posture live in [Pipeline.md](../Pipeline.md). Rolling per-account notes (contact channels, decision-maker IDs, latest touches) live in `Accounts/Leads/<Name>/NOTES.md`.

## How To Use This File

| You are looking for ... | Read this |
|--------------------------|-----------|
| Current stage of any lead (HOT / WARM / COLD / Contacted / etc.) | [Pipeline.md](../Pipeline.md) |
| Decision-maker names, contact channels, latest touches | `Accounts/Leads/<Name>/NOTES.md` |
| The deep one-time research dump that justified putting the lead in the pipeline | This file |
| Daily action queue and what to send today | [TODAY.md](../../TODAY.md) |
| Sales engine overview (positioning, KPIs, 3-engine model) | [SALES_ENGINE.md](../SALES_ENGINE.md) |

When a lead converts to a paying client, copy the relevant dossier section into `Accounts/Active/<Name>/` and remove it from here.

## Active Dossiers

### KBOSS.hu Kft. (Szamlazz.hu)

- **Location:** Budapest, Hungary
- **Company:** Hungary's largest online invoicing platform. Founded 2004. ~50 employees. 100,000+ businesses use their service. Owned by Visma International Holding AS (Norwegian software group, 14K+ global employees).
- **Signal history:** Persistent DevOps hiring through 2025 (multiple Profession.hu postings). As of 2026-05-11 the career page shows full-stack/Java roles only, no DevOps. Working thesis: after a 12+ month failed hire, the in-house developers absorbed the AWS operations work.
- **AWS stack:** Confirmed (customer data on AWS per privacy policy, posting explicitly referenced AWS ops).
- **Visma centralization:** CONFIRMED NOT centralized (Perplexity validation 2026-04-01). Szamlazz.hu runs its own local AWS infrastructure as an autonomous product team within Visma.
- **Reverse-engineered cloud setup:** Likely EC2/EKS for compute, RDS (PostgreSQL or MySQL) for invoicing DB, S3 for document storage, CloudFront CDN, SQS/SNS for async processing, GitLab CI/CD pipeline.
- **Estimated cloud spend:** EUR 5,000 to 20,000 / month
- **Pain points:** (1) Cannot find/retain DevOps after 12+ months of trying. (2) If devs are absorbing it, dev time is the most expensive ops time. (3) Single point of failure for a 100K+ business platform. (4) Likely 20-35% cloud waste without FinOps discipline.
- **Best outreach angle:** Cloud cost waste plus operational fragility (Angle A+C from SCANNER_SCRIPT).
- **Best case study match:** cs-003 Onriva (SaaS platform, ops support).
- **Recommended package:** Essential EUR 2,000/mo + FinOps EUR 500/mo.
- **Added / validated:** 2026-03-31 / 2026-04-01.
- **Where it lives now:** Pipeline HOT, Account NOTES at `Accounts/Leads/KBOSS_Szamlazz/NOTES.md`, v2 outreach draft `#4` in `outreach-batch-1-hot-leads.md`.

### Allonic

- **Location:** Budapest, Hungary
- **Company:** Robotics infrastructure startup. Raised $7.2M pre-seed in early 2026 (reportedly the largest Hungarian pre-seed round on record). Investors include Visionaries Club and angels from OpenAI and Hugging Face. ~15 employees, scaling toward 25-30.
- **Signal:** No active DevOps posting. Active Robotics Engineer / SWE / Operations hiring on LinkedIn Feb 2026. Profile 2 latent need.
- **ICP fit:** Profile #2 "The Scaling Company". Developers building product, no dedicated platform team, scaling fast.
- **AWS stack:** Unconfirmed. Robotics infra likely uses cloud (AWS or GCP) for control planes, data pipelines, CI/CD.
- **Pain points:** Developers doing infra instead of building product. No DevOps discipline as team scales from 15 to 30. Robotics infra complexity beyond an early-stage startup's bandwidth.
- **Best outreach angle:** Scaling Bottleneck (Angle B). "Your developers should be building product, not managing AWS instances."
- **Best case study match:** cs-003 Onriva (scaling SaaS, ops support).
- **Recommended package:** Safety Net EUR 990/mo entry, path to Essential.
- **Added / validated:** 2026-03-19 / 2026-04-01.
- **Where it lives now:** Pipeline WARM, Account NOTES at `Accounts/Leads/Allonic/NOTES.md`, v2 outreach draft TBD (drafting Thursday 2026-05-14).

### EOS Faktor Zrt.

- **Location:** Budapest, Hungary (Vaci ut 30)
- **Company:** Receivables management / debt collection. Founded 2008. 226 employees. Part of EOS Group (Otto Group subsidiary). Hungarian market leader in financial receivables.
- **Signal history:** Hiring DevOps mernok on Profession.hu (Nginx, Jenkins/GitLab CI/CD, IaC, Linux, Bash, Python, Docker, Prometheus, Grafana; AWS certificates listed as advantage). As of 2026-05-11 the April DevOps posting is gone and the career page is collections-focused. The remaining hook is the Otto Group / EOS Group gateway angle.
- **AWS stack:** Partial signal only (certificates as advantage, not requirement). May use on-prem or other cloud.
- **Caveats:** Part of EOS Group / Otto Group (30K+ employees globally). 226 employees slightly above the 200 target. AWS usage not confirmed.
- **Pain points (if validated):** Compliance pressure (financial services), DevOps gap signaled by the (now-gone) posting.
- **Recommended package:** Safety Net EUR 990/mo entry.
- **Added:** 2026-03-31.
- **Where it lives now:** Pipeline WARM, Account NOTES at `Accounts/Leads/EOS_Faktor/NOTES.md`.

### NETOPIA Payments S.R.L.

- **Location:** Bucharest, Romania
- **Company:** Romania's largest online payment processor. Founded 2003. 29-55 employees. 25K+ businesses depend on the platform.
- **Signal:** Hiring Junior DevOps Engineer (AWS, Terraform, Jenkins, Grafana, Linux).
- **AWS stack:** Confirmed (posting explicit).
- **Team gap:** Hiring Junior suggests no existing senior DevOps. Critical gap for a payment processor.
- **Pain points:** Payment processing = zero-downtime requirement, PCI-DSS / PSD2 compliance.
- **Recommended package:** Safety Net EUR 990/mo or Essential EUR 2,000/mo.
- **Best case study match:** cs-003 Onriva (similar size, transaction systems).
- **Added:** 2026-03-20.
- **Where it lives now:** Pipeline COLD (Romania = Tier 3 geo), Account NOTES at `Accounts/Leads/NETOPIA_Payments/NOTES.md`.

### SafeFleet Telematics (ETA Automatizari Industriale)

- **Location:** Timisoara, Romania
- **Company:** Fleet telematics / IoT / M2M provider. Founded 1994. ~52 employees. 110,000+ vehicles monitored globally. Revenue ~25.5M lei (~EUR 5M). Branches in Italy, Poland, Hungary.
- **Signal:** Hiring DevOps Engineer (strong Linux & AWS experience required).
- **AWS stack:** Confirmed (AWS in posting, web-based SaaS platform).
- **Team gap:** 52 employees total, likely sole or very small infra team. Critical for a real-time IoT platform.
- **Pain points:** Fleet telematics = real-time data, high availability requirement. IoT platform needs reliable cloud infrastructure.
- **Recommended package:** Safety Net EUR 990/mo or Essential EUR 2,000/mo.
- **Added:** 2026-03-27.
- **Where it lives now:** Pipeline COLD (Romania = Tier 3 geo). No Account NOTES yet.

### CIG Pannonia Eletbiztosito Nyrt.

- **Status:** Active deep research lives in `Accounts/Leads/CIG_Pannonia/NOTES.md` (last refreshed 2026-05-11 by Perplexity deep-research pass).
- **Why dossier is short here:** The NOTES.md is more current and more detailed than this file ever was. Use NOTES.md.

## Disqualification Log (Historical)

Companies evaluated and disqualified by the lead scanner between 2026-03-20 and 2026-03-31. Kept here as a "do not re-evaluate" reference. New disqualifications go directly into `Lead Scanner/seen-companies.md`.

| Company | Reason | Date |
|---------|--------|------|
| HungaroControl Zrt | Too large (800+ employees, govt) | 2026-03-20 |
| Bluebird International Zrt | Competitor (IT staffing/consulting) | 2026-03-20 |
| SnapSoft Kft | Competitor (AWS consulting partner) | 2026-03-20 |
| Antavo Loyalty Cloud | Wrong cloud (GCP, not AWS) | 2026-03-20 |
| BKK | Too large (govt, 1000+) | 2026-03-20 |
| Euronet Magyarorszag | Too large (international, 500+) | 2026-03-20 |
| ShiwaForce.com Zrt | Competitor (DevOps/cloud consultancy) | 2026-03-20 |
| Lechner Nonprofit Kft | State-owned, govt procurement | 2026-03-20 |
| Zenitech | IT outsourcing firm | 2026-03-20 |
| Cyber Solutions Kft | IT services / potential competitor | 2026-03-20 |
| Cheppers Szolgaltato Zrt | Competitor (AWS Advanced Tier partner) | 2026-03-24 |
| BlackBelt Technology Kft | Competitor (nearshore staffing) | 2026-03-24 |
| Lab49 | Competitor (capital markets consulting) | 2026-03-24 |
| Alchemy | Wrong profile (US crypto startup) | 2026-03-24 |
| DATAPAO | Competitor (data engineering consulting) | 2026-03-24 |
| PPC Romania | Too large (1M+ customers) | 2026-03-24 |
| E-INFRA Romania | Too large (1,400+ employees) | 2026-03-24 |
| Electronic Arts Romania | Too large (global) | 2026-03-24 |
| Vodafone Shared Services Romania | Too large (telecom subsidiary) | 2026-03-24 |
| ALLCLOUD ROMANIA SRL | Competitor (cloud consulting) | 2026-03-24 |
| IHS Markit | Too large (now part of S&P Global) | 2026-03-24 |
| CGI IT Romania | Competitor (IT consulting) | 2026-03-24 |
| Orange Romania | Too large (telecom) | 2026-03-24 |
| CEC Bank | Too large, Azure not AWS | 2026-03-26 |
| PSS Prosoft Solutions | No AWS/cloud signal | 2026-03-26 |
| EEU Software | IT outsourcing firm | 2026-03-26 |
| diconium GmbH | Too large (VW subsidiary, 2,500+) | 2026-03-26 |
| INTELSOL | Competitor (IT/telecom consulting) | 2026-03-26 |
| Modash | VC-backed startup ($14M, Estonia) | 2026-03-26 |
| Accesa | Too large (1,200+) + competitor | 2026-03-26 |
| 56Bit | Competitor (AWS Advanced Tier Partner) | 2026-03-26 |
| Youmio | Post-2021 startup, too small | 2026-03-26 |
| East Vision Systems | IT outsourcing firm | 2026-03-26 |
| ProcessHunt Kft | Too small (4 employees) | 2026-03-27 |
| msg systems Romania | Too large + competitor | 2026-03-27 |
| Toughbyte | Recruitment agency | 2026-03-27 |
| Arm Budapest | Too large (6,000+ global) | 2026-03-27 |
| Profession Services | Recruitment agency (profession.hu's own) | 2026-03-27 |
| Cision (Brandwatch) | Too large (4,000+ globally) | 2026-03-30 |
| EF Education First | Too large (52,000+ globally) | 2026-03-30 |
| One Magyarorszag Zrt | Too large (3,700, telecom) | 2026-03-30 |
| Genesys | Too large (6,000+ globally) | 2026-03-30 |
| HumanField | Recruitment agency | 2026-03-30 |
| Trenkwalder | Staffing agency | 2026-03-30 |
| Key-Talents | Recruitment agency | 2026-03-30 |
| Tata Consultancy Services Hungary | Too large + IT consulting | 2026-03-31 |
| ITWorx Romania | Too large + IT consulting | 2026-03-31 |
| LIGHTWARE Zrt. | No AWS signal, outside age range | 2026-03-31 |
| LaniSys | Too small (1-10) | 2026-03-31 |
| Greenergy-Service Kft | Posting evaporated by 2026-05-11; prior 2026-03-24 LinkedIn connect to Marko Tamas Gabor never accepted | 2026-05-11 |

For the full dedup ledger (every company surfaced including pre-disqualification status) see `Lead Scanner/seen-companies.md`.

## Scanner Run History

The automated daily scanner ran 2026-03-16 through 2026-04-01. Paused since 2026-04-01 per the 2026-04-27 thinking-team review: priority is execution (touches sent), not more intelligence. ENGINE A scanning will resume after we have 50+ outreach data points.

| Date | Leads found | Validated | Notes |
|------|-------------|-----------|-------|
| 2026-03-20 (manual) | 12 companies (HU + RO) | 2 WARM (CIG Pannonia, NETOPIA) | First Romania expansion. 4 disqualified. |
| 2026-03-24 | 14 new (HU + RO) | 0 | All disqualified. Most job boards blocked by proxy. |
| 2026-03-26 | 10 new (HU + RO) | 0 | Same pattern: large enterprises, consulting, VC startups. |
| 2026-03-27 | 6 new (HU + RO) | 1 WARM (SafeFleet) | SafeFleet Telematics surfaced. |
| 2026-03-30 | 7 new (HU + RO) | 0 | All disqualified (large or recruitment agencies). |
| 2026-03-31 | 6 new (HU + RO) | 1 HOT (KBOSS), 1 WARM (EOS Faktor) | KBOSS scored 12/15 at the time. |
| 2026-04-01 (validation sweep) | 15 historical leads re-validated | 1 SUPER HOT (KBOSS), 1 Profile #2 HOT (Allonic), 2 WARM (CIG, OPP) | Perplexity-driven historical cleanup. Many leads marked STALE. |
| 2026-04-01 (fresh scan) | ~15 (HU) | 0 | Confirmed: "True mid-sized non-outsourcing Hungarian product companies publicly advertising DevOps/cloud roles are rare." This is what drove the strategy pivot to ENGINE B (Pain-Based Outbound). |

For daily-brief details see `Lead Scanner/daily-brief-*.md`.
