---
description: "Chemaxon is a Budapest-based chemistry SaaS firm acquired by Certara in 2022; the original DevOps hiring signal is stale but the engineering team still exists and likely faces post-acquisition cloud-ops autonomy or cost-discipline challenges."
description_source: auto
description_hash: 81a26f9fc9a692e4
type: lead
id: chemaxon
company: "Chemaxon"
stage: warm
score: 5
score_breakdown:
  maturity: 3
  posting: 0
  aws: 2
  team_gap: 1
  geo_fit: 3
tags: [pharma, saas, engine-b, lang-en, acquired]
geo: HU
language: en
due: 2026-05-22
next_action: "Re-research Budapest team autonomy + verify any fresh local hiring signal before any send"
status: research
location: "Budapest, Hungary (subsidiary of Certara, HQ Princeton NJ)"
industry: "Cheminformatics / pharma SaaS, Certara subsidiary"
founded: 1998
employees: "~200 Budapest team within ~1,500+ Certara group"
icp: "Profile #1 broken (no longer independent buyer). Profile #3 possible (cloud cost pain) but parent-IT centralization risk is high."
source_url: "https://chemaxon.com/careers"
package:
  tier: Essential
  monthly_eur: 2000
  addons:
    - name: FinOps
      eur: 500
  total_eur: 2500
sources:
  career_page: "https://chemaxon.com/careers (301-redirects to https://careers.certara.com/)"
  linkedin: "https://www.linkedin.com/company/chemaxon"
  validation_pass: "WebFetch 2026-05-18: chemaxon.com/careers and chemaxon.com/about/careers both 301-redirect to certara.com. careers.certara.com Budapest filter returns zero open roles, zero DevOps roles."
channels: [linkedin-inmail-en, linkedin-dm-en]
primary_channel: linkedin-inmail-en
case_study_match: "cs-003 Onriva (compute-heavy SaaS), with caveats post-acquisition"
created: 2026-05-11
validated: 2026-05-11
last_signal_check: 2026-05-18
index_schema_version: 1
---
# Chemaxon

## Signal

**Original signal (2026-05-11 Perplexity validation pass):** Active Senior DevOps Engineer role on chemaxon.com/careers. AWS / Terraform / Docker / GitLab CI stack confirmed via the parallel full-stack engineer Greenhouse posting. Pharma/chemistry SaaS, compute-heavy workloads. Pipeline card placed in HOT and v2 #2 outreach drafted on that basis.

**Re-check 2026-05-18 (WebFetch validation):**

- `chemaxon.com/careers` 301-redirects to `https://www.certara.com/cxn/careers`.
- `chemaxon.com/about/careers` 301-redirects to `https://www.certara.com/cxn/about/careers`.
- `careers.certara.com/` does not list specific roles inline; routes everyone to a Career Center.
- `careers.certara.com/jobs?location=Budapest` returns zero open positions and shows the "Can't find what you're looking for" placeholder.
- No DevOps, SRE, Platform Engineer, or Cloud Engineer role for Budapest / Hungary is publicly visible at Certara as of 2026-05-18.

**Conclusion:** The fresh-posting hook that justified HOT status no longer holds. The original v2 #2 message ("I noticed the Senior DevOps Engineer role on chemaxon.com careers") would land on stale ground. The Perplexity pass on 2026-05-11 missed the acquisition redirect, this is a research-pipeline lesson learned.

## What They Want

- Stack was AWS / Terraform / Docker / GitLab CI (per stale 2026-05 posting)
- No verified current public requirement set to anchor a stack-driven pitch

## About the Company

Chemaxon was founded 1998 in Budapest as a cheminformatics software company serving global pharma R&D (Pfizer, AstraZeneca, Roche, Merck-tier customers). Best known for the Marvin chemistry drawing toolkit and the JChem search/structure platform.

**Acquired by Certara in 2022.** Certara is a NASDAQ-listed biosimulation and pharma-software group, ~1,500+ employees, headquartered in Princeton NJ, with European offices in Germany, France, Netherlands, Poland, Switzerland, UK. The Chemaxon brand continues as a Certara product line. The Budapest office and engineering team still exist and ship Chemaxon products under the Certara umbrella.

Stack: AWS, Terraform, Docker, GitLab CI (per stale 2026-05 posting; current setup unverified post-integration).

Cloud spend estimate: Unverified. Pre-acquisition independent Chemaxon would have run EUR 5,000-15,000/month on AWS for the SaaS components. Post-acquisition the workload may have migrated to Certara group infrastructure, or stayed local.

## Why This Is Interesting

Chemaxon Budapest is still a real engineering team running compute-heavy chemistry workloads. If they retain operational autonomy (similar to how Visma did NOT centralize DevOps for KBOSS), there is still a Profile #3 (Cloud Cost Pain) angle: GPU/compute optimization on chemistry simulations, FinOps on AWS reserved capacity.

The entry point is fundamentally different from the original Profile #1 ("you have an open hire"). It needs a pain-based (Engine B) approach pitched to the Budapest engineering lead, framed around the post-acquisition integration moment.

### Pain Hypotheses

- Parent-IT centralization may have removed cloud-ops autonomy from Budapest, leaving the local team without budget authority for managed services
- OR Budapest still runs its own AWS workloads and is now under Certara group cost-discipline pressure (FinOps angle)
- Compute-heavy chemistry simulations are RI / right-sizing sensitive; 24-month committed RIs are wasted when usage shifts post-acquisition
- Post-acquisition integration commonly creates redundant IT roles that get rationalized, leaving original Budapest engineers stretched

## Value Propositions

- FinOps pass on the legacy Chemaxon AWS footprint, with concrete savings vs the new Certara cost-discipline baseline
- Operational bridge during any infrastructure migration to Certara group standards
- Independent cloud-ops capacity that lets Chemaxon Budapest stay productive on product without diverting engineers to integration plumbing

## Key Contacts

| Name | Role | LinkedIn | Approach | Status |
|------|------|----------|----------|--------|
| TBD | VP Engineering / Head of Platform (Chemaxon Budapest) | (pending Sales Nav search) | Sales Navigator filter: "Chemaxon" past or current + Budapest + engineering / platform / DevOps title | research |
| TBD | CTO / Chief Architect (Certara group level) | (pending) | Less actionable, parent-level, deprioritized | deprioritized |

## The Angle

Forget the "open DevOps role" pitch. The angle is: post-acquisition Budapest teams typically lose cloud-ops autonomy or get squeezed on costs. We can help you keep operational independence while the Certara integration runs.

Pre-condition before any send: confirm Budapest still has local AWS spend authority. Without that, the lead is dead.

## Timing

Deprioritized for Week 2 of the 90-day plan. Re-research late Week 2 or early Week 3. If the Budapest-team-autonomy thesis holds, draft a new pain-based outreach (not the stale v2 #2). If centralization is confirmed, mark Lost.

The originally planned 2026-05-18 send is **cancelled**. Replacement priority for today's HOT slot: SEON.

## Red Flags

- Acquired by Certara 2022, full domain redirect now in place (2026-05-18 verified), independent buyer status is broken
- No active DevOps role publicly listed for Budapest as of 2026-05-18
- Parent company (Certara, ~$1B market cap) may centralize cloud purchasing
- ICP fit table breaks: original 30-200 employee target was met by Chemaxon standalone; under Certara's 1,500+ headcount the original Profile #1 fit is disqualified

## Drafts

### Option A, original v2 #2 message (INVALID, do not send as-is)

The original EN message drafted 2026-05-11 in `Sales/Sales Enablement/outreach-batch-1-hot-leads.md` (section `v2 #2. Chemaxon`) leads with "I noticed the Senior DevOps Engineer role on chemaxon.com careers." This claim is no longer verifiable as of 2026-05-18 and would land flat. Do not send.

### Option B, pain-based re-draft (TBD, requires research first)

Hold until Budapest-team-autonomy thesis is validated. Then draft along these lines (placeholder, not for send):

```text
Subject: Chemaxon Budapest cloud ops post-Certara

Hi {name},

Reaching out specifically about Chemaxon Budapest's cloud operations
post the Certara integration. We work with European product
companies running AWS / Azure managed cloud ops on monthly packages.

For acquired-but-still-autonomous product teams, we usually see two
patterns after the parent's IT integration:
  1. Budapest keeps its AWS but loses dedicated DevOps headcount as
     the parent rationalizes overlap. Engineers absorb infra work.
  2. Budapest still has cost authority but lost FinOps visibility into
     committed RIs and chemistry-workload right-sizing.

Either way, a 60-minute Cloud Health Check (read-only AWS access)
surfaces what the integration has actually changed in your bill and
your operational risk. Worth a 15-minute call?

Best,
Szabolcs
```

Do not send the above without first verifying:
1. There is still a Budapest engineering team running its own AWS workloads
2. The local engineering lead is reachable on LinkedIn and identifiable
3. The Certara group does not already have a managed-cloud relationship

## Action Items

- [ ] Sales Navigator search: "Chemaxon" past or current company + Budapest + engineering / platform / DevOps / SRE titles. Save to "Current campaign" Lead List. 📅 2026-05-22
- [ ] LinkedIn check: is there a Chemaxon Budapest Director of Engineering or Head of Platform still active and reachable? 📅 2026-05-22
- [ ] Search Certara press releases / blog for any "Chemaxon Budapest now part of [Certara IT group]" announcement that explicitly confirms centralization 📅 2026-05-22
- [ ] If autonomy thesis holds, write Option B draft fresh, then resume outreach 📅 2026-05-25
- [ ] If autonomy is centralized to Certara, move card from WARM to Lost in Pipeline.md 📅 2026-05-25

## Next Step

Do not send today. Re-research Budapest team autonomy late Week 2 (target 2026-05-22) using LinkedIn Sales Navigator. Today's 2026-05-18 morning HOT slot pivots to SEON.
