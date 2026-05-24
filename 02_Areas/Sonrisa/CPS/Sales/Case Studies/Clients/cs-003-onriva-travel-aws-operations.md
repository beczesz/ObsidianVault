---
title: "Case Study: Onriva/myRiva - Travel Platform AWS Operations"
id: cs-003
industry: saas
size: "~80 EC2 instances, small-medium company"
country: US (client), CPS operates from EU
problem_type: team-augmentation, 24x7-coverage, cost-reduction
entry_package: Ongoing support (Essential/Growth equivalent)
current_package: Ongoing support
date_started: 2025-01
status: active
author: Sonrisa CPS
index_schema_version: 1
---

# Case Study: Onriva/myRiva - Travel Platform AWS Operations

> **One-liner for outreach:** "We took over AWS operations for a US travel platform (80 EC2 instances, 9 databases, 50+ Lambdas) -- stabilized deployments, eliminated manual steps, and run all maintenance outside their business hours from our EU timezone."

---

## Client Profile

| Field | Detail |
|-------|--------|
| **Industry** | Travel technology (flights, hotels, rental cars, vacation planning) |
| **Company size** | Small-to-medium |
| **Location** | United States (PST timezone) |
| **Tech stack** | AWS: ~80 EC2, 25 Load Balancers, 30 ASGs, 2 Aurora clusters (9 DBs), 51 S3 buckets, 8 DocumentDB clusters, 7 MemoryDB clusters, 5 Amazon MQ brokers, 50+ Lambdas, 14 Route 53 zones, Jenkins, Terraform |
| **Founded** | Established (expanding from business to personal travel) |
| **Name** | Onriva / myRiva (shareable) |

---

## The Situation

Onriva operates a travel platform enabling customers to plan trips across the US -- booking flights, hotels, and rental cars. The company was expanding from business travel into personal travel, putting more pressure on infrastructure reliability. Their AWS footprint was substantial (80+ EC2 instances, multiple database engines, 50+ Lambda functions) but deployments were a mix of manual scripts, partial automation, and tribal knowledge. No documentation existed for release or rollback procedures. The client wanted to avoid any maintenance during business hours (09:00-20:00 PST) but had no team to handle off-peak operations.

---

## The Problem

- **No deployment documentation:** Release and rollback procedures were effectively undocumented, increasing risk with every deployment
- **Manual, inconsistent processes:** Deployments combined manual script execution, manual resource configuration, and pipeline triggers -- different every time
- **Configuration drift:** Client-side personnel occasionally made manual AWS changes not captured in Terraform, causing IaC state mismatches and increasing change risk
- **No off-peak operations capacity:** The client needed maintenance, releases, and DB work done outside business hours but had no team available in those windows
- **Environment separation gaps:** Test, stage, and prod were separated by naming conventions and tags, not account-level isolation

---

## What We Did

- Assigned 3 cloud engineers working part-time, with EU working hours naturally aligning to off-peak US business windows
- Built standardized CI/CD pipelines in Jenkins for both manual and automated deployment triggers
- Implemented blue/green deployment strategy for production, reducing deployment risk and enabling instant rollback
- Improved Terraform IaC coverage to manage infrastructure changes consistently and prevent drift
- Created lifecycle management pipelines -- not just deploy, but also create, configure, and destroy AWS resources as part of release and rollback workflows
- Built a growing set of operational runbooks documenting every process created or improved
- Performed targeted cost optimization through storage cleanup actions
- Established a ticket-based collaboration model via Slack with PR-based approval workflows

---

## The Result

| Metric | Before | After | Timeframe |
|--------|--------|-------|-----------|
| Deployment process | Manual, inconsistent | Standardized CI/CD + blue/green | First 2 months |
| Documentation | Absent | Growing runbook library | Ongoing |
| Release incidents | Frequent, manual recovery | Significantly reduced | After pipeline stabilization |
| Off-peak maintenance | Not possible (no team) | All maintenance runs off-peak via EU team | From day 1 |
| IaC coverage | Partial, drift-prone | Improved Terraform consistency | Ongoing |
| Rollback capability | Manual, risky | Automated blue/green rollback | After implementation |

**Summary:** Stabilized operations for a growing US travel platform by replacing ad-hoc manual processes with standardized CI/CD pipelines, blue/green deployments, and runbook-driven execution -- all delivered during off-peak hours from a European timezone, exactly when the client needed it.

---

## Why They Chose CPS Over Hiring

Hiring US-based DevOps engineers to work off-peak (evenings and nights PST) would be expensive and impractical. CPS's EU-based team naturally operates during the client's off-peak window, turning a timezone gap into an advantage. The client gets experienced AWS engineers running maintenance and releases when it matters most -- without paying US-market salaries or asking anyone to work night shifts.

---

## Quotable

*(Client quote pending)*

---

## Relevance Tags

- **Industry:** `saas` (travel tech)
- **Problem type:** `team-augmentation`, `24x7-coverage`, `cost-reduction`
- **Company size:** `30-100`
- **Geography:** `US` (client), CPS team in EU
- **Entry point:** Ongoing operations support, initially driven by off-peak maintenance need
- **Use for prospects like:** Companies needing off-peak operations coverage, AWS-heavy environments with no internal DevOps, companies with configuration drift and manual deployment problems, SaaS platforms expanding rapidly, companies looking for EU-timezone support for US infrastructure
