---
title: CPS Weekly Competitor Scan Prompt
version: 0.1
date: 2026-03-16
author: Sonrisa - Cloud Platform Services (CPS)
description: Scheduled task prompt for weekly competitor monitoring -- detects pricing changes, new services, blog posts, case studies, and AWS badge changes across 6 key competitors
id: 5b26403e-82d3-490c-9f69-d212d3e59b8d
index_schema_version: 1
---

# CPS Weekly Competitor Scan

## Purpose

This prompt powers a weekly scheduled task that scans CPS's key competitors for changes in pricing, services, content, and AWS partnership status. The output is a concise diff report saved to the CPS folder.

## Competitors to Monitor

| # | Company | Primary URL | What to Check |
|---|---------|-------------|---------------|
| 1 | **SDH Global** | https://sdh.global/services/devops-services/ | Pricing page, service tiers |
| 2 | **Romexsoft** | https://www.romexsoft.com/services/devops-support/ | Pricing, AWS badge level, services |
| 3 | **Dedicatted** | https://dedicatted.com/what-we-do/devops/devops-as-a-service | Tiers, pricing, 24/7 bundling |
| 4 | **Palark** | https://palark.com/services/ | Pricing (XS-XL), SOS DevOps, new services |
| 5 | **Kloia** | https://www.kloia.com/daas | Pricing, SLAs, service scope |
| 6 | **DevOPSGroup** | https://devopsgroup.eu/pricing/ | Component pricing, categories |

### Secondary URLs to Check (if primary shows changes)

| Company | Additional URLs |
|---------|----------------|
| SDH Global | https://sdh.global/aws-devops-services/ |
| Romexsoft | https://www.romexsoft.com/services/ |
| Palark | https://palark.com/services/emergency/ |
| All | /blog, /case-studies, /about (for AWS badges) |

## Scan Procedure

### Step 1: Load Baseline

Read the file `competitor-baseline.md` from the same folder. This contains the last known state of each competitor's pricing, service tiers, and content.

### Step 2: Fetch Each Competitor

For each competitor:

1. Fetch the primary URL using WebFetch
2. Extract:
   - **Service tier names and descriptions**
   - **Published prices** (monthly, hourly, or project-based)
   - **SLA levels** (response times, availability)
   - **AWS partnership level** (Select, Advanced, Premier, any competencies)
   - **Number and names of services listed**
   - **New blog posts** (titles and dates from /blog if accessible)
   - **New case studies** (titles from /case-studies if accessible)
3. Compare extracted data against the baseline

### Step 3: Generate Diff Report

Produce a report with this structure:

```markdown
# CPS Competitor Scan - Week of [DATE]

## Summary
- [X] competitors scanned
- [Y] changes detected / No changes detected

## Changes Detected

### [Competitor Name]
**What changed:** [description]
**Previous:** [old value]
**Current:** [new value]
**Strategic implication for CPS:** [one sentence]

## No Changes
- [List competitors with no changes]

## New Content Detected
- [Competitor]: "[Blog post title]" (date)
- [Competitor]: New case study: "[Title]"

## Scan Failures
- [Any URLs that could not be fetched, with reason]

## Baseline Updated
- [Yes/No - list what was updated in the baseline]
```

### Step 4: Update Baseline

If changes were detected:
1. Update `competitor-baseline.md` with the new values
2. Note the date of change in the baseline

### Step 5: Save Report

Save the weekly report as:
`weekly-scan-[YYYY-MM-DD].md` in the `Strategy/Competitor Reports/` folder.

## What Counts as a Change

**Always flag:**
- Price increase or decrease (any tier)
- New service tier added or removed
- SLA terms changed
- AWS partnership level changed (e.g., Select -> Advanced)
- New competency or designation badge
- New service category added to their portfolio

**Flag if notable:**
- New blog post about pricing, services, or strategy
- New case study (especially if in our target verticals)
- Major website redesign or messaging shift
- New geographic expansion

**Ignore:**
- Minor wording changes in descriptions
- Blog posts about generic tech topics
- Social media updates
- Job postings (unless indicating major expansion)

## Strategic Context for Analysis

When flagging changes, evaluate against CPS positioning:
- CPS packages: Safety Net (EUR 990), Essential (EUR 2,000), Growth (EUR 4,000), Scale (EUR 6,000)
- CPS add-ons: 24/7 (EUR 2,000), Solution Architect (EUR 1,000), FinOps (EUR 500), DevSecOps (EUR 700)
- CPS differentiators: 300-engineer bench, EU-based, enterprise DNA, bundled Migrate+Manage
- CPS AWS status: Select Tier (targeting Advanced)

## Extending the Competitor List

To add a new competitor:
1. Add their row to the "Competitors to Monitor" table above
2. Add their baseline data to `competitor-baseline.md`
3. Increment the version of this prompt file
