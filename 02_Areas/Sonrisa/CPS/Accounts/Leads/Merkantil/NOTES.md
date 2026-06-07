---
description: "Active multi-workstream engagement with Merkantil Bank (OTP Group subsidiary) requiring CPS infrastructure pricing for private Sonrisa AID deployment by EOD today; four additional use-cases (email routing, training, helpdesk, contracts) already in flight from other Sonrisa units since April."
description_source: auto
description_hash: d0b01fb53a2324a9
type: lead
id: merkantil
company: "Merkantil Bank Zrt."
stage: discovery
score: 14
score_breakdown:
  maturity: 3
  posting: 3
  aws: 1
  team_gap: 3
  geo_fit: 3
tags: [banking, fintech, otp-group, ai-enablement, email-routing, aid, lang-hu, cross-unit, multi-workstream, active-engagement]
geo: HU
language: hu
due: 2026-05-27
next_action: "12:00 today: CPS Discovery call (Bán József + Miklós Nándor + Becze Szabolcs, possibly Ceclan Sanyi) on AID infrastructure deployment pricing for Merkantil. Output: a number Miklós can send to Merkantil by EOD 2026-05-27."
status: in_conversation
location: "Budapest, Hungary"
industry: "Banking / Auto-leasing (OTP Group subsidiary)"
founded: 1989
employees: "~250 estimated (Merkantil Group)"
icp: "Profile #1, regulated banking, multi-workstream Sonrisa engagement"
source_url: "Internal Sonrisa Teams chat 'Merkantil' (started 2026-04-27 by Szacsúri László)"
package:
  tier: TBD
  monthly_eur: 0
  addons: []
  total_eur: 0
sources:
  email_router_exec_summary: "[[source-docs/01-email-router-exec-summary]]"
  ai_enablement_proposal_hu: "[[source-docs/02-ai-enablement-commercial-proposal]]"
  further_opportunities: "[[source-docs/03-further-opportunities-outline]]"
  teams_transcript: "[[source-docs/04-teams-transcript-202604-202605]]"
channels: [teams, meeting, warm-intro]
primary_channel: meeting
case_study_match: "MVMI (AzureDevOps Managed Service) — most relevant analog for the AID infra workstream"
created: 2026-04-27
validated: 2026-05-27
last_signal_check: 2026-05-27
index_schema_version: 1
---
# Merkantil Bank Zrt.

> **Status 2026-05-27:** Active multi-workstream Sonrisa engagement. NOT a cold lead. Multiple proposals already in flight from non-CPS Sonrisa units. CPS just plugged in TODAY for AID infrastructure deployment pricing. **Discovery call at 12:00, EOD offer required.**

## Signal

This is **not a cold outbound lead**. Merkantil and Sonrisa have been in active conversation since at least **2026-04-27** (Teams chat opened by Szacsúri László). Multiple Sonrisa team members are engaged across multiple workstreams. The CPS unit (this account's owner in the kanban) was added on **2026-05-27** specifically to provide a CPS-side infrastructure number for the Sonrisa AID deployment, which is one workstream out of several.

The original outreach context predates the Teams chat — Merkantil was a pre-existing Sonrisa relationship (KodeSage already deployed at Merkantil before AID came up). Verify-before-send is moot here; the signal is human-verified through ~4 weeks of direct Teams discussion with Merkantil-side stakeholders.

## What They Want

Merkantil has expressed need across multiple workstreams. Each maps to a distinct deliverable that Sonrisa is scoping:

1. **Intelligent Email Router** — agentic AI to triage incoming customer emails (cards, loans, KYC, investments, insurance, complaints) and route to the correct department, with HITL fallback. Built on n8n + on-prem KodeSage LLM. **Proposal SENT 2026-05-21** (revised — see source-docs/02).
2. **AI Enablement training** — 2-tier workshop series (alap + haladó/fejlesztői) for ~20+ Merkantil developers. **Proposal SENT 2026-05-21** alongside #1 in the same commercial document.
3. **Sonrisa AID infrastructure deployment** — they want to run Sonrisa AID (SDLC-supporting agentic framework) at Merkantil. Requires private inference infra (no public LLM, banking). **DISCOVERY TODAY, OFFER EOD.** ← THIS IS CPS SCOPE.
4. **Further opportunities** (raised verbally, not yet quoted, draft outline by Bán József 2026-05-23): helpdesk automation (RAG), contract analysis & data extraction (SharePoint + RAG), knowledge-base Q&A with Teams integration, credit decisioning agentic workflow, Olga support (incident handling + SQL script generation), AI-assisted SDLC (Sonrisa AID + kiloCode CLI). See source-docs/03.

## About the Company

Merkantil Bank Zrt. — Hungarian banking institution, part of **OTP Bank Group** (one of CEE's largest banking groups). Primary business: auto/leasing finance, lending. Budapest HQ.

Stack visible from context: **KodeSage** (already deployed — Merkantil's chosen LLM platform with self-managed model lifecycle), **Outlook/Exchange** (email infrastructure), **Confluence** (internal docs), **SharePoint** (document repository, contracts), **Camunda** (BPMN workflow engine — surfaced 2026-05-21 as constraint for the email router), banking-grade regulated infrastructure (no public LLM allowed).

Constraint: in banking, public/external LLM endpoints are not allowed. All inference must run on Merkantil-controlled infrastructure. This is the central constraint driving CPS-side sizing today.

## Why This Is Interesting

Multi-workstream enterprise engagement with a tier-1 HU bank. Already in conversation, not cold. Multiple Sonrisa units already collaborating (Szacsúri László account-lead, Bán József + Komlósi Dávid technical, Gergely Baján + Miklós Nándor on training/sales, Ceclan Sanyi pending for CPS effort sizing). CPS's role is the infrastructure layer underneath the AID workstream — a natural extension of what CPS already runs internally for Sonrisa's own AID.

### Pain Hypotheses

- Manual email triage at scale = expensive, slow, error-prone (already explicitly stated by Merkantil)
- KodeSage owns its own model lifecycle → can't safely share its LLM endpoint with AID without breaking on every KodeSage update (Bán József confirmed this is why a separate inference stack is needed)
- Multiple verbal "we want AI for X" asks (helpdesk, contracts, Q&A, credit) suggest Merkantil has internal pressure to ship AI use-cases but lacks the in-house platform team to do it autonomously

## Value Propositions

**CPS-specific (for today's call):**

- Mirror the Sonrisa-internal CPS-built AID infrastructure stack (proven, in-production at Sonrisa)
- On-prem / private inference deployment that satisfies banking compliance
- Managed-service overlay so Merkantil's team doesn't need to operate it (analog: MVMI AzureDevOps Managed Service pattern)
- ITIL + ISO/IEC 27001:2022 certified delivery (per the email router proposal QA section)

**Cross-workstream:**

- Sonrisa AID framework = ready-made agent definitions, skills, workflows for SDLC and beyond
- Sonrisa academy curriculum = in-house training material for the AI Enablement workshops
- Sonrisa KnowledgeVault = pre-built RAG offering for the contract analysis / Q&A asks

## Key Contacts

### Sonrisa side (internal team on the engagement)

| Name | Role | Workstream |
|------|------|------------|
| Szacsúri László | Account lead / Sales | Overall engagement, cross-workstream coordination |
| Bán József | Technical lead | Email router design, AID-infra prep (called CPS in today) |
| Komlósi Dávid | Technical | Email router n8n demo author |
| Gergely Baján | AI Enablement lead | Training proposal, workshop curriculum |
| Miklós Nándor | Pricing / Offer dispatch | Sends commercial offers; needs the CPS number TODAY |
| Gergely Dombi | TBD | Part of the chat thread |
| **Becze Szabolcs** | **CPS lead (you)** | **AID infrastructure pricing — added 2026-05-27** |
| Ceclan Sanyi | CPS Team Lead | Needed for CPS effort sizing (per Becze 2026-05-27 10:25) |

### Merkantil side

| Name | Role | Notes |
|------|------|-------|
| Gábor (last name TBD) | Decision-maker on Merkantil side | Phone +36 70 394 1260 (passed by Szacsúri László 2026-05-18). Likely the CTO / IT lead. The "number" needs to land with him today. |

## The Angle

For the CPS workstream specifically: **"We already built the AID inference platform internally at Sonrisa. We'll deploy the same stack at Merkantil, operate it as a managed service, and keep it banking-compliant — so your team can use AID without owning the infrastructure."**

This is a textbook CPS managed-ops pitch with a known reference pattern (MVMI AzureDevOps Managed Service): one-time deployment + ongoing managed service monthly. The trick today is sizing both numbers cleanly enough to send by EOD.

## Timing

- **2026-05-27 12:00** — internal call: Bán József + Miklós Nándor + Becze Szabolcs (+ possibly Ceclan Sanyi). Goal: agree on a CPS infra number end-of-call so Miklós can send the offer to Merkantil today.
- **2026-05-27 EOD** — number out to Merkantil.
- Other workstreams (email router, AI enablement) already SENT 2026-05-21, validity 2026-05-31. Decision window on those is closing soon.

## Red Flags

- **Time pressure on today's number** — Miklós needs the figure by EOD, no time for a "elvonulunk 1-2 napra" iteration cycle (Miklós explicitly said this 2026-05-27 11:10). The number has to land in-call.
- **Sonrisa AID infra has no productized SKU** — we don't have a standard packaging for "deploy AID at customer site." Today's call has to invent or analog from MVMI.
- **KodeSage model coupling risk** — original idea to reuse KodeSage LLM was killed (Bán József 2026-05-25). The CPS proposal must include its own inference layer, which is the biggest cost driver and the biggest uncertainty in today's sizing.
- **Multi-workstream complexity** — Merkantil sees a single Sonrisa, but internally we have 4+ workstreams across 3+ units. Risk of incoherent pricing if not coordinated. Szacsúri László holds the account-level coherence, not us.
- **Camunda constraint surfaced late (2026-05-21)** — the email router pricing jumped because Camunda BPMN required structural rework. Similar surprises possible on the AID infra side if Merkantil's banking-compliance constraints add cost mid-call.

## Drafts

(Outbound message drafts not applicable — this is an internal-driven engagement, not LinkedIn outbound. The deliverable for today is a NUMBER, not a message.)

### Suggested CPS pricing shape (for the 12:00 call discussion)

Two components, analog to MVMI:

1. **One-time deployment / setup** — engineer-days for: GPU/CPU sizing, model serving stack (vLLM or similar), Kubernetes namespace, observability (Prometheus/Grafana), CI/CD for AID skills, security hardening, runbook. **Effort TBD with Ceclan.**
2. **Monthly managed service** — package tier (Essential / Growth / Scale) + add-ons (24/7 On-Call €2,000, FinOps €500, DevSecOps €700). **Tier TBD based on Merkantil-side usage volume.**

Number to ship today probably needs to be a ballpark "from X HUF setup + Y HUF/month" with a clear assumption list (so we can refine after the formal scoping).

## Action Items

- [ ] **Pre-call (now)**: read Bán József's 02-megvalositasi-vazlatok.md again with CPS lens, note any infra implications across the further-opportunities workstreams. 📅 2026-05-27 #prep
- [ ] **12:00 call**: agree on CPS infra deployment effort (Sanyi) + managed-service tier shape. Output a HUF or EUR number for the offer. 📅 2026-05-27 #meeting
- [ ] **Post-call**: send the number to Miklós Nándor so he can dispatch it to Merkantil by EOD. 📅 2026-05-27 #followup
- [ ] **Within 48h**: write up the CPS proposal section formally (will be folded into the next iteration of the merkantil_ai_enablement_proposal.docx or a separate CPS exec summary). 📅 2026-05-29 #drafting
- [ ] **Open question**: confirm Gábor's role/title at Merkantil (currently only first name + phone known). 📅 2026-05-28 #research

## Next Step

12:00 today — join the Discovery call with Bán József + Miklós Nándor (+ Ceclan Sanyi if joinable). Output a defensible CPS infrastructure number end-of-call so Miklós can include it in today's Merkantil offer.
