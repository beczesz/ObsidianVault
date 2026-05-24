---
title: CPS Case Studies - Index
version: 1.0
date: 2026-03-20
author: Sonrisa - Cloud Platform Services (CPS)
description: Master index of all CPS case studies for sales outreach matching
id: d55d2203-5aad-47b5-b06d-c956b1cdac08
index_schema_version: 1
---

# CPS Case Studies - Index

This folder contains anonymized case studies from real CPS/Sonrisa client engagements.
Used by the sales team and AI tools to match relevant experience to prospects during outreach.

## How to Use

When drafting outreach or preparing for a call, pick the case study that best matches the prospect on:
1. **Industry** -- closest sector match
2. **Problem type** -- what pain brought them to us
3. **Company size** -- same ballpark (employees)
4. **Entry point** -- how they started with us (replaces hire, cost saving, migration, etc.)

Reference in outreach as: *"We've done this before for a similar company -- [one-liner]"*

---

## Quick Reference Table

| ID | File | Industry | Size | Problem Type | Result (one-liner) | Package | Tags |
|----|------|----------|------|--------------|--------------------|---------|------|
| cs-001 | [MVMI](Clients/cs-001-mvmi-energy-openshift.md) | energy | Large (3M+ customers) | migration, team-augmentation, 24x7-coverage | Quarterly to bi-weekly releases, zero downtime for 3M+ households, OpenShift in weeks | Project + Ongoing | HU, OpenShift, K8s, hypercare |
| cs-002 | [Observer](Clients/cs-002-observer-media-aws-migration.md) | media | Small-medium (4TB data) | migration, replacement-hire, greenfield | Hostile vendor takeover, 4TB migrated to AWS EKS in 3 months, hit go-live deadline | Project + Ongoing | EU, AWS, EKS, vendor-replacement |
| cs-003 | [Onriva/myRiva](Clients/cs-003-onriva-travel-aws-operations.md) | saas (travel) | Small-medium (80 EC2) | team-augmentation, 24x7-coverage, cost-reduction | Stabilized 80-instance AWS fleet, blue/green deployments, off-peak ops from EU timezone | Ongoing support | US, AWS, Jenkins, Terraform, timezone-advantage |
| cs-004 | [MVMI Azure DevOps Support](Clients/cs-004-mvmi-azure-devops-support.md) | energy | Large (3M+ customers) | team-augmentation, 24x7-coverage, replacement-hire | Azure DevOps platform L3 SLA support -- Critical bugs fixed in 8h, containerization consulting, developer enablement 5x11 | Essential + Ongoing | HU, Azure DevOps, K8s, Docker, CI/CD, SLA |
| cs-005 | [OKFŐ Azure DevOps Install](Clients/cs-005-okfo-azure-devops-install.md) | healthcare, government | Large (national institution) | migration, greenfield, team-augmentation | Replaced outdated ALM with on-premises Azure DevOps Server -- demo, test, production envs + 2-year consulting | Project + Ongoing | HU, Azure DevOps Server, CI/CD, on-premises, government |

---

## Problem Type Taxonomy

Use these tags consistently across case studies so matching works:

| Tag | Meaning |
|-----|---------|
| `replacement-hire` | Company lost/couldn't find a DevOps person |
| `cost-reduction` | AWS bill too high, FinOps needed |
| `migration` | On-prem to cloud or cloud-to-cloud |
| `24x7-coverage` | Needed on-call coverage, no internal capacity |
| `compliance` | ISO 27001, NIS2, SOC2, GDPR pressure |
| `scale-up` | Growing fast, infra couldn't keep up |
| `incident-recovery` | Major outage or security incident |
| `team-augmentation` | Had DevOps team but needed extra capacity |
| `greenfield` | No cloud infra, built from scratch |

---

## Industry Taxonomy

| Tag | Meaning |
|-----|---------|
| `energy` | Energy, utilities, renewables |
| `fintech` | Finance, payments, banking |
| `ecommerce` | Online retail, marketplaces |
| `saas` | B2B or B2C software products |
| `manufacturing` | Industrial, production |
| `healthcare` | Medical, pharma, health tech |
| `logistics` | Transport, supply chain |
| `media` | Publishing, streaming, content |
| `real-estate` | Property, construction |
| `other` | Anything else |

---

## Case Study Files

- [cs-001 - MVMI Energy OpenShift Migration](Clients/cs-001-mvmi-energy-openshift.md)
- [cs-002 - Observer Media AWS Migration](Clients/cs-002-observer-media-aws-migration.md)
- [cs-003 - Onriva/myRiva Travel AWS Operations](Clients/cs-003-onriva-travel-aws-operations.md)

---

## Adding a New Case Study

1. Copy `TEMPLATE.md` and rename to `cs-[NNN]-[short-slug].md` (e.g. `cs-001-energy-replacement.md`)
2. Fill in all sections -- use anonymized client name if needed
3. Add a row to the Quick Reference Table above
4. Make sure the one-liner in the table is punchy and specific (numbers preferred)
