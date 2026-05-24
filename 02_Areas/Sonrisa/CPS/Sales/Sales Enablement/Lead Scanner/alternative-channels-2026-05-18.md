---
title: Alternative Lead-Discovery Channels Research
date: 2026-05-18
author: v0.9 Scrape session learnings + research synthesis
status: working-doc
description: Where to look for HU mid-tier ICP-fit leads when LinkedIn Jobs + Perplexity-web-search prove thin. Synthesis of today's scrape findings plus structured alternative-channel inventory.
id: ce42a0a7-e53f-4f36-93b1-11bcea77ad0c
index_schema_version: 1
---

# Alternative Lead-Discovery Channels Research

## Why this document exists

Today's v0.9 scrape (HU + Azure DevOps + last 30 days) yielded **1 verified HOT (ABRIS)** + **1 verified WARM (Cardinal Software)** out of a much wider search effort. The thin yield is itself a finding: the channels we used today have specific failure modes for HU mid-tier ICP verification. This doc catalogs **what worked, what did not, and what we have not yet tried**, ranked by expected ROI per hour of operator time.

## What we learned today, per channel

### Channels that WORKED

| Channel | What it produced today | When to use again |
|---|---|---|
| **Sales Navigator company-level search** | Adam Berkecz (SEON VP Architecture) identified as 2nd-degree, Dominik Mate Kovacs (Colossyan CEO) identified as 2nd-degree, Norbert Fejer warm-path detected (then ruled out by user) | **Always** for decision-maker identification once a company is known |
| **WebFetch on company-domain careers page** | Chemaxon-Certara acquisition detected (chemaxon.com redirects to certara.com), Colossyan independence confirmed, ABRIS verified | **Always** for acquisition-check before drafting outreach. ~3 seconds per call, free. |
| **Perplexity Sonar Pro segment-discovery** | Banking-vendor cluster unlock: ABRIS sibling segment (Cardinal Software, Servera, AB-Soft, CompuTec, PBS, Cinnamon, BANIF) | Yes for vertical-specific segment mapping. NOT for live-hiring verification. |
| **LinkedIn job page direct (jobs/view/{id})** | ABRIS DevOps Fejlesztő full posting metadata: posted date, applicant count, hybrid status, contract type | Once SN or jobs-search surfaces a posting URL, use this for full posting metadata |

### Channels that did NOT WORK well

| Channel | Failure mode | What to do instead |
|---|---|---|
| **LinkedIn Jobs filtered HU + niche stack + last 30 days** | Only 5-7 results, mostly remote/international companies. Hungarian companies with active DevOps postings rarely surface on LinkedIn Jobs (probably listed on Profession.hu instead). | Widen the search: drop the time filter, broaden keywords (DevOps OR Platform OR SRE OR Infrastructure), then manually scan for HU-anchored companies. Or skip LinkedIn Jobs entirely for HU; use Profession.hu directly. |
| **Perplexity Sonar Pro for live-hiring verification of HU SMEs** | 9 out of 9 cards returned UNKNOWN for current-hiring status. Public web search does not index Profession.hu / paywall HU job boards well. | Sales Navigator company-page drilldown (one Chrome MCP call per company), OR direct company-website check. SN is more reliable per company. |
| **Generic "Hungarian companies hiring DevOps" Perplexity queries** | Returned generic advice on how to search, not specific company names | Replace with VERTICAL-SPECIFIC queries (banking, retail tech, manufacturing automation). Vertical query returned 7 named banking-vendor cluster siblings; the generic query returned 0. |

### Channels we have NOT YET tried, ranked by expected ROI

#### Tier 1, highest expected value, try within Week 2

**1. Profession.hu directly (manual or via SN integration)**
- The dominant HU job board. ~80% of HU SME job postings end up here first, often before LinkedIn.
- Public web is proxy-blocked from external scrapers. Sonar / Perplexity can NOT see Profession.hu listings cleanly.
- Manual access from your browser shows everything. 5-10 minutes per session at scrape-time.
- Recommended approach: search "DevOps mernok", "Azure DevOps", "Platform Engineer", "Infrastructure mernok" on Profession.hu. Note company names. Cross-reference with SN for ICP fit + decision-maker degree.

**2. Sales Navigator account-search with company-headcount + skills + hiring-on-LinkedIn filters**
- We touched this briefly today but didn't run it deep. SN has structured filters for "Currently hiring" + "Company headcount 51-500" + "Geography Hungary" + "Industry: Financial Services / Software / Manufacturing" + "Technologies used: Azure" or "Azure DevOps".
- This returns a pre-filtered company list with hiring signal AND key-people-degree info AND TeamLink overlap visibility.
- Highest expected per-hour ROI for HU mid-tier ICP discovery, especially now that we have the cluster pattern (banking IT vendors).

**3. LinkedIn People search for HU+Azure DevOps skill (Sales Navigator)**
- Instead of finding companies, find PEOPLE who list "Azure DevOps" as a skill, filter to Hungary geo, 50-500 emp employer. From the result set, extract company names and verify each. The people-side query often surfaces companies that don't post jobs publicly.
- 30-50 results per query typically. ~15 min to skim + tag companies.

**4. Microsoft Partner directory (HU localized)**
- partner.microsoft.com → location Hungary → filter for Digital & App Innovation (Azure), Data & AI (Azure), Infrastructure (Azure), DevOps competencies
- Returns named HU Microsoft Partners. Likely 30-50 companies, of which 5-10 are mid-tier ICP fit (not the giant consultancies).
- Use Sonar + SN for per-company verification afterward.

#### Tier 2, medium expected value, try within Week 3-4

**5. Conference attendee lists (especially Financial IT 2026, Portfolio, Budapest, May 28)**
- Cardinal Software is exhibiting, and likely a dozen more HU banking IT vendors. Conference attendee list is the most concentrated HU banking IT vendor list per square meter you can find.
- Action: in-person attendance OR scrape the exhibitor list afterward via Portfolio website.
- URL: https://www.portfolio.hu/en/events/conference-it/financial-it-2026/1996/overview

**6. Craft Conference Budapest (June 4, 2026)**
- DevOps and platform engineering crowd. CTOs and engineering managers attend.
- Either submit a talk for next year OR attend and network.
- Attendee list is event-specific, not publicly scraped.

**7. AWS Community Day CEE (September 17, 2026, Budapest)**
- AWS-native audience. Less relevant for Azure DevOps focus but useful for the broader AWS angle (which Sonrisa CPS already targets).
- Submit a talk, sponsor booth.

**8. HU tech meetups (Budapest.NET, Budapest Azure, Budapest DevOps Meetup)**
- Local engineering communities. Meetup.com or Eventbrite for HU. 30-100 engineer attendees per event.
- Use to find ACTIVE Hungarian engineers who use Azure DevOps. Their companies become candidates.
- Long-tail discovery, slower compounding.

#### Tier 3, lower expected value or longer cycle, opportunistic

**9. Hungarian business news monitoring (Portfolio.hu, HVG, Forbes Hungary, Növekedes.hu)**
- M&A signals, leadership changes, funding announcements for HU SMEs. Slower-than-LinkedIn-jobs but catches deals before they hit job boards.
- Set up Google News alerts for "magyar startup", "Series A", "felvasarlas IT", etc.
- Long-tail compounding.

**10. HVCA (Hungarian Venture Capital and Private Equity Association)**
- hvca.hu → member list + funded portfolio companies → all HU-funded SMEs in one place.
- Cross-reference with SN for ICP fit.
- Useful for Profile #2 ("Scaling Company") more than Profile #1.

**11. OPTEN / Bisnode / ZoomInfo HU company database**
- Paid services with structured HU company data: headcount, industry, revenue, executives.
- OPTEN is the canonical HU corporate registry data aggregator.
- Worth a subscription IF lead generation becomes the primary growth lever.

**12. Sonrisa's own existing client + team network mining**
- MVMI, OKFO, Colosseum Dental, ProSharp, Onriva, etc. all have engineering networks.
- Molnár Dániel (Sales Engineer) likely has 200+ HU IT 1st-degree connections.
- A 30-minute LinkedIn 1st-degree audit of the Sonrisa team's networks could surface 10-20 warm-intro candidates.
- THIS IS THE HIGHEST-CONVERSION CHANNEL OF ANY listed. Reserved for the highest-priority targets.

**13. GitHub Trending Hungary**
- HU-located GitHub developers who star/contribute to Azure DevOps / .NET / Kubernetes projects.
- Identify the developers, find their employer, qualify.
- Compounding signal but slow per-touch.

**14. Hungarian Chamber of Commerce + industry associations**
- Magyar Bankszövetség (Hungarian Banking Association) for banking sector
- Magyar Logisztikai Szövetség for logistics
- ISZTSZ for software / IT services
- Membership directories often public.

## Recommended next-scrape strategy

Based on today's learnings, the **Week 3 scrape (target: 2026-05-25 or earlier)** should run in this order:

1. **Sales Navigator account-search (deep, ~30 min)** with the structured filter set. Single richest channel for HU mid-tier with current hiring signal. Target: 5-10 new candidates from one session.

2. **Profession.hu manual scan (~15 min)** focused on DevOps mernok, Azure DevOps, Platform Engineer searches in last 30 days. Cross-reference with SN. Target: 2-3 new candidates not visible on LinkedIn.

3. **Microsoft Partner directory HU pull (~10 min)**. One-shot extraction of HU Microsoft Partners with Azure DevOps / Infrastructure competencies. Filter for 50-500 emp. Target: 3-5 named candidates for monitoring.

4. **Sonar segment-discovery for one new vertical (~5 min, 1 Sonar Pro call ~$0.025)**. Today: banking IT vendors. Next: insurance IT vendors? Retail tech? Manufacturing automation? Pick ONE vertical per week.

5. **Per-candidate verification (parallel APIs as we did today)**. For top 5 candidates from steps 1-4, run Sonar + WebFetch + SN drilldown.

**Wall-time budget**: ~90 min per Week 3 scrape session.
**API cost budget**: ~$0.30 per scrape (mostly Sonar).
**Expected yield**: 2-3 new HOT + 5-8 new WARM (vs today's 1 HOT + 1 WARM).

## Channel attribution dashboard (start tracking now)

For each new lead added to Pipeline.md, tag the source channel:

| Tag | Channel |
|---|---|
| `#src-linkedin-jobs` | LinkedIn Jobs public search |
| `#src-sn-company` | Sales Navigator company-search |
| `#src-sn-people` | Sales Navigator people-search |
| `#src-profession-hu` | Profession.hu |
| `#src-sonar-segment` | Perplexity Sonar segment discovery |
| `#src-ms-partner` | Microsoft Partner directory |
| `#src-conference` | Conference attendee list (specify which) |
| `#src-warm-intro` | Sonrisa team / client network referral |
| `#src-news` | Hungarian business news monitoring |

Track over 4-6 weeks. The channel with highest converted-to-Contacted ratio is the one to over-invest in. Today's discovery: ABRIS came from `#src-linkedin-jobs`, Cardinal Software came from `#src-sonar-segment`.

## Open questions for the user

1. **Profession.hu access**: do you have a recruiter / employer account that lets you see full posting list and download exhibitor data? If yes, you can do the manual scan directly. If not, this becomes a 5-10 min browser visit per scrape session.
2. **HU conferences in 2026 calendar**: do you plan to attend Financial IT 2026 (May 28) or Craft Conference (June 4)? Both have direct ICP overlap. Even if attending solo, the conference attendee list (when public) is gold.
3. **Sonrisa team LinkedIn mining**: are you OK asking Molnár Dániel or the other team members to share their 1st-degree HU IT contacts list? This is the highest-conversion channel but requires team buy-in.
4. **Budget for OPTEN / ZoomInfo subscription**: if HU lead discovery becomes a primary growth driver, a EUR 100-300/mo data subscription would 10x the lead-discovery throughput. Worth considering once we hit Week 4-6.

## Summary

| Channel | Today verdict | Recommend for next scrape? |
|---|---|---|
| Sales Navigator (company + people search) | ✅ Best for HU mid-tier verified leads | YES, primary |
| Profession.hu (manual) | Not yet tried, but likely best for HU coverage | YES, secondary |
| Microsoft Partner directory HU | Not yet tried, structured | YES, segment-specific |
| Sonar Pro segment-discovery | ✅ Great for vertical mapping | YES, one vertical per week |
| LinkedIn Jobs filtered | ⚠️ Thin for niche queries | Only as supplement |
| Perplexity Sonar live-hiring verification | ❌ UNKNOWN-rate too high | Skip for verification, use only for discovery |
| Conference attendee lists | Not yet tried | Tier 2, calendar-driven |
| Sonrisa team network mining | Not yet tried | YES highest-conversion, ABM-style |
| OPTEN / ZoomInfo subscription | Not yet evaluated | Defer until Week 6+ if HU pipeline is the primary growth lever |
