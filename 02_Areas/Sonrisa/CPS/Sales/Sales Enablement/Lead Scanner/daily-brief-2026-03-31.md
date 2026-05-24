# CPS Daily Lead Scanner -- Daily Brief
**Date:** 2026-03-31 (Monday)
**Profile:** #1 -- The Replacement Hire
**Run type:** Automated

---

## Summary

| Metric | Value |
|--------|-------|
| Prescribed queries run | 5 |
| Supplemental queries run | 8 |
| New companies screened | 6 |
| HOT leads (11-15) | 1 |
| WARM leads (7-10) | 1 |
| Disqualified | 4 |

---

## HOT Leads

### KBOSS.hu Kft. (Szamlazz.hu) -- Score: 12/15

| Criterion | Score | Rationale |
|-----------|-------|-----------|
| Company maturity | 3/3 | Founded 2004, 22 years old, stable and well-known Hungarian SaaS brand |
| Posting age | 2/3 | Multiple DevOps/operations postings from 2025 (IDs: 2603572, 2692781); persistent need signal but freshness unverifiable |
| AWS/cloud confirmed | 2/3 | Confirmed via privacy policy: customer data stored on AWS; cloud monitoring for security |
| Team gap severity | 2/3 | ~50 employees running Hungary's most popular invoicing SaaS. Persistent hiring = likely small/no dedicated DevOps |
| Geographic fit | 3/3 | Budapest, Hungary |
| **TOTAL** | **12/15** | **HOT** |

**Company:** KBOSS.hu Kft. operates Szamlazz.hu, Hungary's largest online invoicing platform used by 100,000+ businesses. Founded 2004, ~50 employees, Budapest. Now majority-owned by Visma International Holding AS (Norwegian software group, 14K+ employees globally).

**Trigger:** "Uzemelteto / DevOps" postings on Profession.hu. Requirements include AWS, cloud, security, Python, JavaScript, Linux. Multiple postings found from March-June 2025, suggesting persistent difficulty filling this role.

**Why CPS fits:** Mission-critical financial SaaS running on AWS. Downtime impacts 100K+ businesses and NAV compliance. CPS can provide immediate fractional DevOps support. DevSecOps and FinOps add-ons directly relevant.

**Recommended package:** Safety Net (EUR 990/mo) or Essential (EUR 2,000/mo) + DevSecOps (EUR 700/mo)

**Caveats:**
- Visma parent company may provide centralized DevOps resources -- needs validation
- Posting freshness cannot be confirmed (profession.hu blocked by egress proxy)
- Company is technically outside ICP founding range (2004 vs. 2005-2020 target) but only by 1 year

**Jira ticket:** NOT CREATED -- sonrisa-cps.atlassian.net is not accessible via the current Atlassian MCP connector (only exarlabs.atlassian.net is available). Manual creation required.

**Next actions:**
1. Validate posting is still active (manual check on profession.hu)
2. Research whether KBOSS operates infra independently from Visma
3. Find CTO/Head of Engineering on LinkedIn
4. Create Jira ticket manually on sonrisa-cps.atlassian.net under Epic KAN-4

---

## WARM Leads

### EOS Faktor Zrt. -- Score: 9/15

| Criterion | Score | Rationale |
|-----------|-------|-----------|
| Company maturity | 3/3 | Founded 2008, 18 years, financial services |
| Posting age | 1/3 | Appears to be a recent posting |
| AWS/cloud confirmed | 1/3 | AWS certificates listed as "advantage" only, not confirmed user |
| Team gap severity | 1/3 | 226 employees, likely has existing IT team |
| Geographic fit | 3/3 | Budapest, Hungary |
| **TOTAL** | **9/15** | **WARM** |

**Company:** Receivables management / debt collection. 226 employees, Budapest. Part of EOS Group (Otto Group subsidiary, 30K+ employees globally). Hiring DevOps mernok with Nginx, Jenkins, Docker, Linux skills.

**Caveats:** Otto Group subsidiary (large enterprise parent). 226 employees slightly above 200 target. Weak AWS signal. Added to Unvalidated for manual review.

---

## Disqualified Companies

| Company | Reason | Details |
|---------|--------|---------|
| Tata Consultancy Services Hungary | Too large (2,400+ in HU, 600K+ globally) | IT consulting firm, Budapest. Founded 2001 in Hungary |
| ITWorx Romania | Too large (851 employees) + IT consulting | Cairo HQ, global IT services provider with Romania office |
| LIGHTWARE Zrt. | No AWS signal, 350+ employees, outside ICP age | AV equipment manufacturer, founded 1998, Budapest. Score 6/15 |
| LaniSys | Too small (1-10 employees) | Software dev shop, Budapest. Below 30 employee ICP minimum |

---

## Pipeline Health Snapshot

| Stage | Count |
|-------|-------|
| Unvalidated | 3 (NETOPIA, SafeFleet, EOS Faktor) |
| Researched | 1 (KBOSS.hu/Szamlazz.hu) |
| Ready to Approach | 0 |
| Contacted | 2 (Greenergy-Service, CIG Pannonia) |
| Discovery Call | 0 |
| Proposal | 0 |
| Won | 0 |
| Lost/Disqualified | 50 |

**Follow-up alerts:**
- Greenergy-Service Kft follow-up was due 2026-03-31 (TODAY). LinkedIn connect request sent 2026-03-24. Check if connection was accepted and send MVMI case study if so.
- CIG Pannonia Eletbiztosito follow-up was due 2026-03-31 (TODAY). Career page application sent 2026-03-24. Follow up with LinkedIn connect to Zankai Attila or Pataki Laszlo.

**Ongoing monitoring:**
- Randstad Budapest AWS postings (Cloud Platform Engineer, Senior DevOps Engineer, DevOps Engineer) remain active. End employers unknown. randstad.com blocked by egress proxy. Recommend manual investigation to identify the hiring companies behind these postings.

---

## Scanner Log Entry

| Date | Queries | Companies Found | Leads Added | Notes |
|------|---------|-----------------|-------------|-------|
| 2026-03-31 | 5 prescribed + 8 supplemental | 6 new companies | 1 HOT + 1 WARM | KBOSS.hu/Szamlazz.hu is first HOT lead since Greenergy-Service (2026-03-20). Jira ticket creation blocked by MCP connector access issue. Market continues to be challenging -- most postings are from large enterprises or staffing agencies. profession.hu, glassdoor, devjob.ro remain blocked by egress proxy. |
