---
type: lead
id: cchbc
company: "Coca-Cola HBC (CCHBC)"
stage: hot

# --- Triage / priority ---
score: 13
score_breakdown:
  maturity: 3
  posting: 3
  aws: 0
  team_gap: 3
  geo_fit: 1
tags: [enterprise, rfp, partner-channel, magyar-telekom, openminds, azure, aiops, agentic-ai, finops, dynatrace, lang-en, multi-country]
geo: INT
language: en

# --- Next action ---
due: 2026-05-31
next_action: "Decide AIOps/Agentic AI go/no-go for openminds; if go, scope deliverable for end of May"
status: research

# --- About the company ---
location: "Zug, Switzerland (HQ); operations in 29 countries across Europe, Africa, and Eurasia"
industry: "FMCG / Consumer Goods (Coca-Cola bottler)"
founded: 1969
employees: "~33,000"
icp: "Off-ICP: enterprise RFP arriving via partner channel, not Profile #1/#2/#3 outbound"

# --- *** THE primary link, REQUIRED *** ---
source_url: "https://mtelekom-my.sharepoint.com/personal/berecz_sandor10_telekom_hu/_layouts/15/Doc.aspx?sourcedoc=%7B26CF9FDF-AE81-4772-B604-323A4D5BDD36%7D&file=Cloud%20Platform%20Management.docx&action=default&mobileredirect=true"

# --- Recommended package ---
package:
  tier: ""
  monthly_eur:
  addons: []
  total_eur:
  note: "Standard CPS packages (Safety Net to Scale, 990-6000 EUR/mo) DO NOT FIT. This is an enterprise managed-services RFP. Sonrisa role here is most likely a sub-bid component (AIOps/Agentic AI) inside a larger Magyar Telekom proposal, not a prime contract."

# --- Additional links beyond source_url ---
sources:
  rfp_doc_local: "Tender/Cloud Platform Management.docx"
  rfp_text_local: "Tender/rfp-full-text.md"
  email_thread_local: "Tender/email-thread.md"
  posting: ""
  career_page: ""
  linkedin: "https://www.linkedin.com/company/coca-cola-hellenic-bottling-company/"
  validation_pass: "2026-05-19 received via openminds (Szurdi Miklos) forwarded from Magyar Telekom (Bartok Tamas, Molnar Attila, Berecz Sandor). Originator: OTE Group / Petropoulos Argyris."

# --- Channels ---
channels: [partner-rfp]
primary_channel: partner-rfp
partner: "openminds.hu (Szurdi Miklos) -> Magyar Telekom NyRT. -> OTE Group (Greece)"

# --- Context ---
case_study_match: "cs-001-mvmi-energy-openshift (large-enterprise managed ops); cs-004-mvmi-azure-devops-support (Azure DevOps managed service) - both demonstrate enterprise scale on Azure ecosystem"
created: 2026-05-19
validated: 2026-05-19
last_signal_check: 2026-05-19
---

# Coca-Cola HBC (CCHBC)

## Signal

RFP arrived via partner chain on 2026-05-19. Originator at OTE Group (Greece): Petropoulos Argyris, ICT Sales Consultant, Global Accounts. Forwarded through Magyar Telekom NyRT. (Bartok Tamas -> Molnar Attila -> Szurdi Miklos at openminds.hu) and into Sonrisa.

The full RFP is for Cloud Platform Managed Services for CCHBC's Azure environment from 2027 onward, with future-readiness for GCP. Magyar Telekom is preparing a bid; Sonrisa is being asked to cover the AIOps / Agentic AI / FinOps / automation differentiator portion. Berecz Sandor at MT is consolidating.

Key dates:
- Financial proposal due end of May 2026 (~12 days from receipt)
- Technical presentation due mid-June 2026
- DT-level focus on the deal; VP-level CC on the originating mail (Petric Anton, Telekom Deutschland)

## What They Want

Full lifecycle managed services for an Azure-based cloud platform, with explicit emphasis that the engagement is NOT ops-heavy (~40-50% classical operations only). The remaining 50-60% is what makes this strategic for MT and where Sonrisa is being asked to contribute:

- **FinOps & cost optimization** (tagging, forecasting, RI/SP, chargeback, GreenOps)
- **Automation & platform engineering** (IaC, CI/CD, GitOps, self-service, policy-as-code)
- **Governance & agile delivery** (quarterly innovation backlog, OKRs, PI Planning alignment)
- **Innovation: AIOps** (AI/ML in Dynatrace, Azure Advisor, Defender; predictive capacity, cost-spike forecasting, MTTR projection)
- **Innovation: Agentic AI** (autonomous detect-decide-act loops; quarterly PoCs required)
- **Self-learning automation** (closed-loop, pipeline-failure pattern learning)
- Classical: 24x7 ops, Dynatrace observability, ServiceNow integration, IMCR participation, SOC 2 Type 2 required of vendor

## About the Company

Coca-Cola HBC is one of the world's largest Coca-Cola bottlers. Listed on the London Stock Exchange (FTSE 100). Operates in 29 countries spanning Western and Eastern Europe, Russia/CIS, and Africa. Cloud platform is Azure-first, GCP-ready. Internal team: Digital Technology & Platform Services (DTPS).

Stack: Azure (mandatory), Terraform (primary IaC), Azure DevOps / GitHub Actions, AKS, Dynatrace (mandatory observability), ServiceNow (mandatory ITSM), Microsoft Defender, Entra ID, Azure Hybrid Benefit, SAP on Azure (SUSE), Windows + RHEL + SUSE workloads.

Cloud spend estimate: Not disclosed; multi-country FMCG at this scale typically EUR 5-20M / year on Azure.

## Why This Is Interesting

This is **NOT a CPS Lead Scanner ICP fit** in the strict sense (CCHBC is enterprise FMCG, far outside the 30-500-employee mid-market focus of Engine A/B). But it is highly interesting for three reasons:

1. **Partner-channel monetization** — Sonrisa carrying a credible AIOps/Agentic AI story inside an MT enterprise bid strengthens the MT/Sonrisa relationship and could open recurring sub-bid roles for future enterprise opportunities.
2. **Direct match to CPS innovation thesis** — the RFP explicitly demands Agentic AI, autonomous remediation, predictive FinOps, and self-learning automation. This is exactly where the CPS roadmap is heading (see Strategy/Managed service, Marketing/Blogs/Managed Service series, Inference Farm LLMaaS).
3. **Case-study fuel** — even a partial sub-bid win (or a credible technical presentation in mid-June) becomes a reference for the FMCG and broader EU enterprise market.

### Pain Hypotheses

- MT's bid is ops-heavy by default (telco operating model); they lack a sharp AIOps/Agentic AI narrative and need a specialist partner to fill it.
- CCHBC has explicitly told MT this should NOT be an ops-heavy bid - which means proposals that look like classical NOC/MSP will lose. The differentiator is autonomy and FinOps maturity.
- Quarterly AIOps/Agentic AI PoCs are a **mandatory deliverable**, not a nice-to-have. MT needs a partner who can actually ship these PoCs - not vendor slides.

## Value Propositions

- **AIOps/Agentic AI delivery capability** that ships in quarterly cadence, not slideware (Sonrisa has the Inference Farm + agentic infrastructure stack to back this).
- **FinOps maturity** beyond Azure Cost Management - tagging coverage, RI/SP utilization, chargeback dashboards, AHUB monitoring, GreenOps.
- **Automation product mindset** - CI/CD reusable templates, policy-as-code, drift detection, self-service portals. Aligns with CPS's "platform engineering" positioning.
- **Independent specialist credibility** - Sonrisa is not a generalist SI; we can sell the AI/AIOps narrative as deep specialists, which strengthens MT's prime-vendor positioning.

## Key Contacts

| Name | Role | Org | Approach | Status |
|------|------|-----|----------|--------|
| Szurdi Miklos | (forwarder) | openminds.hu | Direct contact, our entry point | inbound 2026-05-19 |
| Molnar Attila | AICCST | Magyar Telekom (ext) | Postman; not the decision-maker | inbound |
| Bartok Tamas | Data/AI Portfolio Sales Expert | Magyar Telekom | Routed the topic, postman | inbound |
| Berecz Sandor | Bid owner for AIOps topic | Magyar Telekom | **Will contact Sonrisa**; consolidates AIOps response by end of May | awaiting his outreach |
| Horvath Varga Janos | (routing) | Magyar Telekom | Internal routing | inbound |
| Vasko Gabor, Bakos Balazs | (recipients) | Magyar Telekom | Internal | inbound |
| Adam Gabor | (earlier handler) | Magyar Telekom | Forwarded inside MT | inbound |
| Petropoulos Argyris | ICT Sales Consultant, Global Accounts | OTE Group (Greece) | RFP originator at carrier side | external |
| Petric Anton | VP | Telekom Deutschland | Senior CC; signals strategic priority | external |
| Tatjana Pecek | (referenced) | Combis (HR) | Possible Croatian Telekom involvement | external |
| Toth Laszlo (B2B_MCT) | | Magyar Telekom | CC on original mail | external |
| Nikolakopoulos Dimitrios | | OTE Group | CC on original mail | external |
| CCHBC: DTPS team | Digital Technology & Platform Services | Coca-Cola HBC | End customer; not directly accessible at this stage | end-customer |

## The Angle

Sonrisa is the AIOps/Agentic AI/FinOps specialist that MT's enterprise bid needs. We do not compete with MT - we make their bid winnable on the non-ops 50-60% that CCHBC explicitly cares about. Quarterly PoC cadence is something we can credibly commit to; MT alone likely cannot.

For Sonrisa internally: this is a partner-channel opportunity that lives outside our standard ICP and packaging, but it amplifies the CPS innovation narrative we are already building (managed service blog series, Inference Farm, FinOps push, ACE/LLMaaS).

## Timing

- **2026-05-19** (today): RFP received. Awaiting Berecz Sandor's reach-out.
- **2026-05-19 to 2026-05-22**: Internal CPS go/no-go decision on AIOps/Agentic AI scope.
- **End of May 2026** (~2026-05-31): Financial proposal to MT for inclusion in their CCHBC submission.
- **Mid-June 2026**: Technical presentation deck/demo content.

Very tight. Action this week or the window closes.

## Red Flags

- Sonrisa is NOT the prime; MT controls the customer relationship, deal economics, and shortlist positioning. We are a sub-bid component.
- **SOC 2 Type 2 is a hard vendor requirement** in the RFP. We do not have this (and we lack NIS2 too per CLAUDE.md). MT presumably carries the compliance umbrella for the prime bid, but our sub-component still needs to be operable inside CCHBC's policies. Confirm with MT before committing.
- Quarterly Agentic AI PoCs as a **contractual deliverable** is ambitious. We can deliver, but we must scope what counts as a PoC vs. production agent to avoid scope creep.
- Greek/international stakeholder coordination (OTE, CCHBC HQ Switzerland, Telekom DE VP) - we will not be at that table. Trust MT entirely on customer signals.
- "DT szintű focus" (Deutsche Telekom group-level focus) means visibility but also rigidity; ad-hoc scope changes from MT side likely.
- Standard CPS pricing packages do not fit. We need a per-FTE/per-deliverable commercial model for this sub-bid, which we have not previously priced.
- Date scope is 2027 onward - if MT wins, the engagement only starts in 2027. So the immediate revenue impact is small; the value is positioning and partnership depth.

## Drafts

### Internal go/no-go check questions (for Szabolcs)

1. Capacity: Do we have the AIOps/Agentic AI delivery bandwidth to commit to quarterly PoCs from 2027 onward, on top of Sprint 3 launch and existing 11 clients?
2. Compliance: Can MT carry SOC 2 Type 2 obligation at the prime level, with Sonrisa operating inside CCHBC controls? (Required by RFP.)
3. Commercials: What is our pricing model for a sub-bid sub-component? Day-rate? FTE allocation? Outcome-priced PoCs?
4. Strategic: Is this the door-opener to a recurring MT enterprise sub-bid stream, or a one-off?
5. People: Who from CPS leads this from our side? E9+ Architect + Molnar Daniel? Or pull in BDOS Maestro for innovation deliverables?

### Outbound draft to Szurdi Miklos (English, after internal decision)

```text
Subject: Re: Fw: CCH Cloud Managed Services - AIOps/Agentic AI sub-bid

Szia Miklos,

Megkaptuk az anyagot, koszi az iranyitast. Atneztuk az RFP-t es a 
[AIOps/Agentic AI/FinOps/Automation] sub-scope megfelel a CPS innovacios 
roadmap-jeben felepitett kepessegeknek.

Mielott elkotelezzuk magunkat a majus vegi deadline-hez, harom dolgot kell 
tisztaznunk Sandor-ral:

1. Commercial modell a sub-bid komponensre (FTE / day-rate / outcome-based PoC)
2. SOC 2 Type 2 compliance umbrella (MT prime szinten vagy Sonrisa-tol elvart?)
3. Hatarvonal MT ops-delivery es Sonrisa innovacio-delivery kozott

Kerlek, kapcsolj ossze Sandor-ral amint lehet - heten belul tudunk egy elso 
hivast tartani.

Udv,
Szabolcs
```

## Action Items

- [ ] **2026-05-19**: Read full RFP text in `Tender/rfp-full-text.md` (Szabolcs)
- [ ] **2026-05-20**: Internal go/no-go decision with CPS leadership (Ceclan, Szanto, E9+ Architect)
- [ ] **2026-05-20**: Reply to Szurdi Miklos with intent + ask to be connected with Berecz Sandor
- [ ] **2026-05-21 to 2026-05-23**: Define commercial model for sub-bid (Szabolcs + Molnar Daniel)
- [ ] **2026-05-22 to 2026-05-28**: Draft AIOps/Agentic AI/FinOps technical narrative and financial proposal to MT
- [ ] **2026-05-31**: Submit financial proposal to Berecz Sandor for MT consolidation
- [ ] **2026-06-01 to 2026-06-13**: Prepare technical presentation content for mid-June
- [ ] Track all activity in Pipeline.md kanban (HOT lane)

## Next Step

Reply to Szurdi Miklos within 24 hours acknowledging receipt and asking him to connect us with Berecz Sandor at Magyar Telekom for the AIOps sub-scope conversation.
