---
title: CPS Lead Scanner - Historical Validation Sweep
date: 2026-04-01
type: validation-sweep
author: Claude (orchestrating Perplexity research)
description: Full re-validation of all historical HOT leads from daily briefs March 16-31
id: 6b5e6be9-dd94-49f4-bb2a-d3fec79e36a9
index_schema_version: 1
---

# Validation Sweep -- 2026-04-01

## Summary

Re-validated all 15 historical HOT leads found across 10 daily briefs (March 16-31, 2026) using Perplexity for real-time research. ChatGPT scoring was attempted but rendered in Canvas artifact (unreadable); Claude performed re-scoring using the 15-point matrix.

**Input:** 15 HOT leads (8 Hungarian, 7 international)
**Output:** 1 SUPER HOT, 1 Profile #2 HOT, 2 WARM, 11 STALE/DROP

## Validated Leads

### SUPER HOT -- Pursue Immediately

**1. KBOSS / Szamlazz.hu (Budapest) -- 14/15**

| Criterion | Score | Evidence |
|-----------|-------|----------|
| Maturity | 3/3 | Founded 2004, 22 years, stable fintech |
| Posting age | 3/3 | Persistent hiring 12+ months, listing still visible |
| AWS confirmed | 2/3 | AWS in privacy policy + posting (IaC, GitLab CI/CD) |
| Team gap | 3/3 | Cannot find/retain DevOps, critical for 100K+ business platform |
| Geographic | 3/3 | Budapest, Tier 1 |

**Key validation finding:** Visma does NOT provide centralized DevOps for KBOSS. Szamlazz.hu runs its own local AWS infrastructure as an autonomous product team. This was the biggest caveat and it's been resolved in our favor.

**Outreach draft:** Ready in `Strategy/CPS Sales Strategy v2.0.md`
**Next:** Find CTO on LinkedIn, validate profession.hu posting, send outreach.

### PROFILE #2 HOT -- Early Stage Outreach

**2. Allonic (Budapest) -- 7/15 (Profile #1) / EXCELLENT (Profile #2)**

| Criterion | Score | Evidence |
|-----------|-------|----------|
| Maturity | 0/3 | Startup, pre-seed stage |
| Posting age | 0/3 | No DevOps posting |
| AWS confirmed | 1/3 | Robotics infra likely uses cloud, unconfirmed |
| Team gap | 3/3 | 15 emp, NO DevOps capability, scaling to 25-30 |
| Geographic | 3/3 | Budapest, Tier 1 |

**Why this is still HOT:** $7.2M pre-seed (largest Hungarian pre-seed EVER), robotics infrastructure company, investors from OpenAI/HuggingFace/Visionaries Club. They will NEED cloud platform capability as they scale. CPS should position as "fractional platform team."

**Outreach angle:** Scaling Bottleneck -- "Your developers should be building your robotics platform, not managing cloud infra."

### WARM -- Keep Monitoring

**3. CIG Pannonia (Budapest) -- 8/15**
- Active insurance company, no current DevOps posting found
- Strategic target for NIS2/DORA compliance angle
- Already contacted via career page (March 24), follow-up overdue
- Reposition messaging from "we saw your posting" to "compliance/risk"

**4. OPP (Netherlands) -- 10/15**
- Senior DevOps posting still live (evergreen since 2023)
- Sophisticated AWS setup (EC2, K8s, Terraform, Lambda)
- BUT: explicitly want in-house ownership, strong internal DevOps preference
- Lower conversion probability; consider "fractional backup" angle only

**5. BitNinja (Budapest) -- 8/15**
- Active Hungarian server-security SaaS, infra-heavy
- Original DevOps posting dates from 2020, not a fresh 2026 ad
- Underlying need persistent but they likely have in-house capability
- Warm target for "augmenting your security-SaaS infra team" framing

### STALE / DROP -- Remove from Active Pipeline

| Company | Reason | Action |
|---------|--------|--------|
| Greenergy Solar | No confirmable 2026 DevOps posting, company identity unclear | Keep in Contacted (LinkedIn sent), but deprioritize. Check if connect was accepted. |
| Riptides | EUR 3.3M funded, active, but no DevOps posting. Latent need. | Monitor. Could become Profile #2 target later. |
| Axoflow | Active OSS company, strong infra culture. Not a buyer. | Reclassify as ecosystem/partnership contact. |
| OmniLogic | Cannot confirm Hungarian entity exists. | DROP completely. |
| Cloudprinter | No 2026 posting. | STALE. |
| Reonic | No 2026 posting. | STALE. |
| Runware | No 2026 posting, limited public footprint. | STALE. |
| AVILOO | No 2026 posting. | STALE. |
| Chatlyn | No 2026 posting. | STALE. |
| Qdrant | Active hiring but building dedicated internal SRE/Cloud Ops team. | DISQUALIFIED -- not a buyer, building in-house. |
| Duna | Historical lead, no current signal. | STALE. |
| Genezio | Historical lead, no current signal. | STALE. |

## Pipeline Health After Validation

**Active pipeline (worth pursuing):**
- KBOSS 14/15 SUPER HOT -- #1 priority, outreach ready
- Allonic Profile #2 HOT -- early-stage, research founders first
- CIG Pannonia 8/15 WARM -- compliance angle, follow up on LinkedIn
- SafeFleet 10/15 WARM -- existing from March 27 scan, needs validation
- NETOPIA 9/15 WARM -- existing from March 20 scan, needs validation
- EOS Faktor 9/15 WARM -- existing from March 31 scan, needs validation

**Key insight:** Out of 15 historical HOT leads, only 1 (KBOSS) remains clearly HOT with an active, validated signal. This confirms what the Strategy v2.0 diagnosed: Profile #1 (replacement hire) yields very few matches in Hungary. ENGINE B (pain-based outbound) is essential to generate volume.

## Recommendation

1. Send KBOSS outreach THIS WEEK (Week 1 of 90-day plan)
2. Research Allonic founders for Profile #2 approach
3. Follow up on Greenergy LinkedIn (check accept status)
4. Follow up on CIG Pannonia via LinkedIn (Zankai Attila)
5. Run fresh scan TODAY to find new leads -- the historical pipeline is thin
