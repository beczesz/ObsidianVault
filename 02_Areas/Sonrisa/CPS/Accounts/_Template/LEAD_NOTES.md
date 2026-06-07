---
description: "A sales opportunity tracking template for documenting leads with sections for signal source, company details, pain points, value propositions, contact information, outreach angles, and follow-up actions. Used by sales teams to organize prospect research and coordinate engagement strategy."
description_source: auto
description_hash: 6ac22f3489d81d4f
# ===========================================================================
# CPS LEAD note, dashboard-driven schema, v1.0
# ===========================================================================
# This file is the canonical per-lead source of truth. Read by the live
# dashboard at Sales/dashboard.html and by sales-engine agents.
#
# Location: 02_Areas/Sonrisa/CPS/Accounts/Leads/<NormalizedName>/NOTES.md
# Contract: Sales/DASHBOARD_CONTRACT.md
#
# REQUIRED for the card to render in the dashboard:
#   type: lead
#   company: "Display Name"
#   stage: hot | warm | cold | contacted | discovery | proposal | won | lost
#   source_url: link to the original opportunity (posting / career page / signal)
#
# Everything else below is optional but populates richer card and drawer
# content when set.
# ===========================================================================

type: lead
id: company_id                     # stable lowercase alphanumeric id, derived from company
company: "Display Name"
stage: cold                        # current pipeline stage (also kept in Pipeline.md)

# --- Triage / priority ---
score:                             # 0 to 15 overall priority score, optional
score_breakdown:                   # five cells, each 0 to 3
  maturity:
  posting:
  aws:
  team_gap:
  geo_fit:
tags: []                           # extra tag chips on the card: fintech, engine-b, lang-en, ...
geo: HU                            # HU | RO | NL | DE | INT | ...
language: en                       # primary outreach language: hu | en | ro

# --- Next action ---
due: 2026-05-15                    # next action date, YYYY-MM-DD
next_action: ""                    # 1 verb-led action phrase, e.g. "Send LinkedIn DM to CTO"
status: research                   # research | ready_to_send | awaiting_reply | in_conversation | won | lost

# --- About the company ---
location: ""                       # HQ city, country
industry: ""                       # short industry phrase
founded:                           # year (number)
employees: ""                      # "~50" or "100+" etc.
icp: ""                            # "Profile #1 / #2 / #3" plus optional qualifier

# --- *** THE primary link, REQUIRED *** ---
source_url: ""                     # canonical URL to the original opportunity, posting / career page / signal

# --- Recommended package ---
package:
  tier: ""                         # Safety Net | Essential | Growth | Scale
  monthly_eur:                     # base monthly EUR (number)
  addons:                          # zero or more add-ons
    - name: ""                     # FinOps | DevSecOps | 24/7 On-Call | Solution Architect
      eur:
  total_eur:                       # monthly + sum(addons.eur)

# --- Additional links beyond source_url ---
sources:
  posting: ""                      # explicit posting URL
  career_page: ""                  # company careers page
  linkedin: ""                     # LinkedIn company URL
  jira: ""                         # internal Jira ticket if any
  validation_pass: ""              # human note about last validation pass

# --- Channels ---
channels: []                       # list of outreach channels: linkedin-dm-hu, email, career-page, warm-intro
primary_channel: ""                # which channel to use first

# --- Context ---
case_study_match: ""               # which CPS case study fits this lead
created: 2026-05-14                # YYYY-MM-DD when added to the pipeline
validated:                         # YYYY-MM-DD when last validated by Perplexity / research
last_signal_check:                 # YYYY-MM-DD when signal freshness was last checked
---
<!--
  Below this line is the drawer content. Sections by name map to drawer slots,
  see Sales/DASHBOARD_CONTRACT.md for the section-to-slot mapping.
  Keep H2 names exactly as below. The dashboard parser is case-sensitive on
  section names.
-->

# Display Name

## Signal

What surfaced this opportunity. Job posting? Funding round? LinkedIn activity?
Conference contact? Free prose, 1 to 3 paragraphs.

## What They Want

- Stack item or role requirement
- Stack item or role requirement
- ...

## About the Company

Industry, size, growth trajectory, ownership structure, regulatory regime,
anything that affects how we engage. Free prose.

Stack: AWS, Terraform, K8s, ... (single line, parser picks up known tech)
Cloud spend estimate: EUR X,XXX to Y,XXX / month.

## Why This Is Interesting

Why this lead is a CPS fit. One to three paragraphs.

### Pain Hypotheses

- First pain hypothesis (one line)
- Second pain hypothesis (one line)
- ...

## Value Propositions

- What we can offer (one line)
- What we can offer (one line)
- ...

## Key Contacts

| Name | Role | LinkedIn | Approach | Status |
|------|------|----------|----------|--------|
| TBD  | CTO  | (pending) | LinkedIn DM, persistent-hiring angle | research |

## The Angle

The core pitch in 2 to 3 sentences. What angle resonates with this lead.

## Timing

When to make the outreach. Day-of-week preferences, time-zone notes,
known constraints.

## Red Flags

- Risk to flag before outreach (one line)
- Risk to flag before outreach (one line)

## Drafts

### Option A, LinkedIn (HU)

```text
Szia {name},

[full draft text]
```

### Option B, Email backup

```text
Subject: ...

Hi {name}, ...
```

## Action Items

- [ ] Specific next step
- [ ] Specific next step

## Next Step

Single sentence: what is the very next thing to do?
