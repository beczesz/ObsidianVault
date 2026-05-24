---
topic: Lead Validation Scrape - 2026-05-11 Engine Warm-Up
created: 2026-05-11
last_updated: 2026-05-11
status: active
id: e3bee11f-b2b8-4efa-9095-23144385c619
index_schema_version: 1
---

# Brainstorm: Lead Validation Scrape (2026-05-11 Engine Warm-Up)

## Objective

Day 1 of the reset 90-day sales clock. Validate the 5 HOT and 5 WARM leads on the Obsidian Kanban (Sales/Pipeline.md) are still actively hiring DevOps/cloud/platform roles as of today, find the decision maker for each on LinkedIn, and scrape the Hungarian + Romanian market for 5 to 10 new ICP-matching companies we missed in the 2026-04-02 career page scan. Output feeds directly into the sharpened outreach drafts and Pipeline.md card updates.

## Team

| AI | Role | URL |
|----|------|-----|
| Perplexity | Researcher | TBD (session opens 2026-05-11) |
| ChatGPT | Strategist | TBD |
| Gemini | Validator | TBD |
| Claude Cowork | Orchestrator | (this session) |

## Sessions

| Date | Team | Key Outcome |
|------|------|-------------|
| 2026-05-11 | Perplexity (Researcher) + ChatGPT (Strategist) + Gemini (Validator) | Session 1: Lead validation + new lead scrape kickoff |

## AI Session Links

- Perplexity (Researcher): https://www.perplexity.ai/search/i-need-two-things-with-sources-n1MS3ywMSeWayZnLrYau_A (opened 2026-05-11)
- ChatGPT (Strategist): https://chatgpt.com/c/6a01ea53-89ec-8386-8ca7-de98bdf17c77 (opened 2026-05-11, titled "Sales Engine Strategy")
- Gemini (Validator): https://gemini.google.com/app/e9dc0d77f89133ea (opened 2026-05-11, titled "Devil's Advocate: Sales Outreach Plan Critique")

## Context References

- `Sales/SALES_ENGINE.md` -- system documentation (v1.0, 2026-04-27)
- `Sales/Pipeline.md` -- current Kanban with 5 HOT + 5 WARM + 5 COLD
- `Sales/Sales Enablement/leads.md` -- detailed research notes per lead
- `Sales/Sales Enablement/Lead Scanner/career-page-scan-2026-04-02.md` -- 5-week-old career page state
- `Sales/Sales Enablement/Lead Scanner/seen-companies.md` -- dedup tracker
- `Sales/Sales Enablement/profile1.md` -- ICP "The Replacement Hire"
- `Strategy/CPS Sales Strategy v2.0.md` -- 3-engine strategy
- `brainstorm/brainstorm_sales-strategy-agentic-review.md` -- 4-AI strategic review (2026-04-27)

## Pre-Scrape State (snapshot 2026-05-11)

### HOT (need fresh validation + decision-maker identification)
1. KBOSS / Szamlazz.hu (14/15) -- Budapest, ~50 emp, AWS, Visma owner. Persistent DevOps hiring 12+ months as of April. Career page had 5 Java roles + 0 DevOps role posted directly. Need: still hiring? Find CTO.
2. Chemaxon (HOT, two roles April) -- Budapest HQ, pharma/chemistry SaaS, compute-heavy. SRE Cloud Engineer + Senior DevOps Engineer posted. Need: both roles still open? Find VP Eng.
3. Loxon Solutions (HOT) -- Budapest, banking software, 25+ years, AWS/K8s/CI/CD. Senior DevOps role. Need: still open? Find CTO. Note DORA pressure.
4. SEON (HOT) -- Budapest HQ + global team (Americas/EMEA/APAC), 300+ emp, fraud/AML SaaS, SOC 2 + ISO 27001. Lead DevSecOps on Workable. Need: still open? Find VP Eng / Head of Platform / CISO.
5. Colossyan (HOT) -- Budapest 5th district, AI video, GPU workloads. Platform Engineer role. Need: still open? Find CTO.

### WARM (need fresh validation + decision-maker identification)
1. CIG Pannonia (8/15) -- Budapest, insurance, K8s + Azure DevOps + Helm. Two DevOps roles posted April. Previously contacted via career page 2026-03-24, no response. Target: LinkedIn to Zankai Attila.
2. EOS Faktor (9/15) -- Budapest, debt collection, 226 emp, part of EOS Group (Otto Group). Fresh DevOps posting April 1 (was ~3 days old then). Need: still open?
3. Allonic (Profile 2 HOT) -- Budapest, robotics startup, $7.2M pre-seed (largest HU ever), 15 emp growing. No DevOps posting (latent need).
4. Lensa (WARM) -- Budapest eng center, AWS confirmed, no dedicated DevOps. Backend Python + Senior Java openings.
5. Greenergy-Service Kft (was 11/15, now STALE) -- Budapest, energy, AWS+Azure+K8s+Terraform+ISO 27001. December 2025 DevOps posting may still be unfilled. Contact: Gergely Geczi (IT Ops Lead, linkedin.com/in/gergely-geczi-3b308881). Prior LinkedIn connect to Marko Tamas Gabor 2026-03-24, no response.

### New leads target
5 to 10 NEW ICP-matching companies (30 to 500 emp, AWS or Azure, hiring DevOps/SRE/Platform Engineer, not gov, not IT outsourcing, HU primary + RO/DACH secondary) not already in seen-companies.md.

## Key Insights

### Perplexity (Researcher) -- 2026-05-11, sourced verification

Verdict on each of the 10 leads (May 2026 state):

1. **KBOSS / Szamlazz.hu** -- NO active DevOps posting visible on the company career page in May 2026. Their public Karrier section now highlights full-stack developer roles, not ops. The only DevOps posting (Profession.hu, KBOSS.hu Kft "Uzemelteto / DEVOPS") dates from 10 March 2025. The 14/15 score from April was based on the 2025 posting which appears no longer active. The narrative "devs doing AWS work themselves" may now be stronger, not weaker -- they may have given up trying to hire DevOps externally. CTO not identifiable from public pages. Source: szamlazz.hu, profession.hu.

2. **Chemaxon** -- YES, active. "Senior DevOps Engineer (Budapest)" is currently listed under Technology & Data on chemaxon.com careers. Same careers page also advertises a full-stack engineer role explicitly noting AWS / Terraform / Docker / GitLab CI delivery (posted 10 Nov 2024 on Greenhouse). Posting age for the DevOps role not stated on the page. CTO not named publicly. CONFIRMED HOT. Source: chemaxon.com, boards.eu.greenhouse.io.

3. **Loxon Solutions** -- WEAKENED. Loxon's open Hungary roles on LinkedIn now read Junior Java SWE, Java SWE, Senior SW Quality Engineer, and SysOps. No DevOps/SRE/Cloud/Platform engineer branded posting. SysOps exists but is not the same buyer. CTO not identifiable. Source: linkedin.com.

4. **SEON** -- YES, and now LEADERSHIP-level. Active "Senior Manager, Site Reliability Engineering (EU CET)" role on SEON careers (Budapest hybrid or EU remote). Plus a "Senior Platform Engineer" on Profession.hu. Role description explicitly lists AWS, Kubernetes, Terraform, Prometheus, Grafana, Jenkins. They want someone to lead an SRE team, own incident management, drive SLAs/SLOs and automation. CONFIRMED HOT, potentially higher value. Source: linkedin.com, profession.hu.

5. **Colossyan** -- BORDERLINE. Platform Engineer (Remote Hungary) role posted 4 Nov 2024 on Jobera, still publicly listed but ~6 months old. Stack: AWS (EKS, IAM, S3), Kubernetes, Flux, GitHub Actions. Active openness uncertain. Source: jobera.com.

6. **CIG Pannonia** -- FRESHEST signal of the entire pipeline. "Devops mernok" posted on Profession.hu on 4 May 2026, just 7 days ago. Hybrid Budapest (1097 Konyves Kalman korut 11). Required tech: Git, DevOps, Azure, Docker, Linux, Kubernetes, Azure DevOps CI/CD, Helm charts. Strongly Azure-oriented. THIS LEAD SHOULD MOVE UP. Source: profession.hu.

7. **EOS Faktor / EOS Hungary** -- NO publicly advertised DevOps/SRE/Cloud/Platform roles. The career page focuses on debt collection / business operations roles. The fresh April 1 posting that put them on the list appears gone. Source: eos-solutions.com.

8. **Allonic** -- NO explicit DevOps/SRE/Cloud/Platform role, but actively hiring Robotics Engineer, Mechatronics Engineer, Software Engineer, and an Operations role for their 3D Tissue Braiding robotics platform. Robotics Engineer role actively promoted on LinkedIn from February 2026. Profile 2 (latent need) still applies. Source: allonic.co, linkedin.com.

9. **Lensa** -- NO ops-titled role on career.lensa.com. However, a Mid-Level Data Engineer in Budapest is hiring to work "across our AWS-based ecosystem" on data pipelines and infrastructure. AWS confirmed. Latent need angle holds. Source: career.lensa.com, linkedin.com.

10. **Greenergy-Service Kft** -- NO public evidence of DevOps/SRE/Cloud/Platform postings or company-specific job pages. Greenergy looks like a fully dead end as a lead. Source: glassdoor and generic searches returned nothing for them. Mark as Lost.

### Quick yes/no summary table (Perplexity)

| Company | Active relevant role (May 2026)? | Notes |
|---------|----------------------------------|-------|
| KBOSS / Szamlazz.hu | No (last DevOps posting Mar 2025) | Narrative still strong, but signal weaker than thought |
| Chemaxon | Yes -- Senior DevOps Engineer live | AWS/Terraform/Docker/GitLab |
| Loxon Solutions | No (only SysOps, not DevOps-titled) | Signal weakened |
| SEON | Yes -- Senior Manager SRE + Sr Platform Engineer | Leadership-level, AWS/K8s/Terraform |
| Colossyan | Uncertain (posting from Nov 2024, still listed) | 6 months old |
| CIG Pannonia | Yes -- Devops mernok posted 4 May 2026 | FRESHEST, Azure/K8s |
| EOS Faktor | No | Posting gone since April |
| Allonic | No DevOps; Robotics + SWE roles only | Profile 2 latent need |
| Lensa | No ops role; Data Engineer on AWS | Latent need angle |
| Greenergy | No public evidence | Mark Lost |

### Task 2 -- New leads (thin, per Perplexity)

Perplexity surfaced only weak new candidates (most fail the exclusion criteria):
- Societe Generale Global Solution Centre (Romania), Cloud DevOps Engineer -- too large (global bank)
- GlobalLogic Romania, Senior DevOps Engineer -- IT outsourcing firm (excluded)
- Arm Budapest, DevOps/Automation Software Engineer posted 16 March 2026 -- already disqualified (semiconductor, 6000+ globally)
- Unnamed Randstad client in Budapest, "cloud-native experts," medior to senior DevOps -- unnamed end-employer (already a known noise source)
- Unnamed isecjobs "Senior Cloud Security DevOps Engineer Budapest" -- unnamed employer

Market signal: Glassdoor shows 354 cloud engineer roles + 22 DevOps roles in Budapest (May 2026) and 1,736 platform engineer roles in Romania. Plenty of demand-side activity, but Perplexity was unable to identify NEW Hungarian/Romanian product or SaaS companies (30 to 500 emp) with explicit active DevOps/SRE postings beyond the ones we already have. This validates the SALES_ENGINE.md thesis that ENGINE B (pain-based outbound, not hiring-signal-based) must be the primary path. Profile 1 (Replacement Hire) job-scanning alone will not fill the pipeline.

Perplexity offered a second-pass option focused only on HU SaaS or only on RO SaaS for a deeper sweep. Worth running.

### ChatGPT (Strategist) -- partial, then session lost

ChatGPT stream truncated at 114 chars on the first attempt ("1. KBOSS / Szamlazz.hu - send first. Best fit for your wedge: mature Hungarian SaaS, likely..."). A "continue" nudge was sent but the session was lost during the conversation pause. Did not produce a strategist synthesis. Recommend re-running ChatGPT in a future session if a second-opinion pass is needed.

### Gemini (Validator) -- never produced output, session lost

Gemini entered extended-thinking ("Tools / Thinking") mode and did not generate visible response text before the session was lost during the pause. Recommend re-running Gemini if a validator pass is needed.

## Synthesis -- final 2026-05-11

Based on Perplexity findings (and Claude/Cowork orchestrator analysis since ChatGPT and Gemini produced no usable output):

### New HOT order for Tuesday 2026-05-12

1. **CIG Pannonia** -- promoted from WARM. Freshest signal in the entire pipeline (Devops mernok posted 2026-05-04, 7 days old). Azure DevOps / K8s / Helm stack. Hybrid Budapest.
2. **Chemaxon** -- holds. Senior DevOps Engineer active on careers page. AWS / Terraform / Docker / GitLab CI confirmed.
3. **SEON** -- value upgraded. Senior Manager SRE leadership role plus Senior Platform Engineer. AWS / K8s / Terraform / Prometheus / Grafana / Jenkins.
4. **KBOSS / Szamlazz.hu** -- holds but icebreaker pivots. No current DevOps posting on career page; full-stack devs only listed. "Absorbed DevOps into dev team" thesis is now stronger than "persistent hiring" thesis.
5. **Colossyan** -- borderline. Platform Engineer (Jobera) from 2024-11-04 still listed but 6 months old. AWS EKS / Flux / GitHub Actions.

### New WARM order for Wed-Fri

6. **Allonic** -- Profile 2 scaling-company pitch holds. Active robotics hiring.
7. **Lensa** -- AWS confirmed via Mid-Level Data Engineer on AWS-based ecosystem.
8. **Loxon Solutions** -- demoted from HOT. Only SysOps role, no DevOps/SRE-titled posting. Banking/DORA pitch valid but signal weaker.
9. **EOS Faktor** -- demoted. Posting gone since April. Otto Group gateway angle is the only remaining reason to approach.
10. **TBD** -- open slot. Run Perplexity HU SaaS deep-pass to find candidate, or promote one of Barion / Pentech / ABZ Innovation from COLD.

### Lost / Parked changes

- **Greenergy** -- remove from WARM. Mark Lost. No public DevOps signal, prior failed touch.

### Strategic implication

Perplexity's empty TASK 2 (no meaningful new ICP product-company DevOps postings found in HU/RO) validates the 4-AI thinking team's thesis from 2026-04-27: ENGINE B (pain-based outbound on cloud cost waste and operational fragility) must be the primary path, not hiring-signal-based ENGINE A. The hiring-signal market in Hungary is genuinely thin for ICP companies (30 to 500 emp, product, not outsourcing, not government). This should be carried forward as a fact in `SALES_ENGINE.md`.

## Decisions Made

- [2026-05-11] DECISION: Reshuffle HOT to lead with CIG Pannonia (freshest posting). Input: Perplexity. Confidence: HIGH.
- [2026-05-11] DECISION: Demote Loxon and Colossyan signals (Loxon SysOps-only, Colossyan posting 6mo old). Keep both in pipeline but Loxon moves to WARM. Input: Perplexity. Confidence: MEDIUM-HIGH.
- [2026-05-11] DECISION: Mark Greenergy Lost. Input: Perplexity (no public signal) + prior failed touch on record. Confidence: HIGH.
- [2026-05-11] DECISION: Pivot KBOSS icebreaker from "persistent hiring" to "career page shows full-stack devs but no DevOps = devs absorbed it." Input: Perplexity (career page state). Confidence: HIGH.
- [2026-05-11] DECISION: ENGINE B (pain-based outbound) confirmed as primary path. Input: Perplexity TASK 2 empty results. Confidence: HIGH.
- [2026-05-11] DECISION: Do not block on missing ChatGPT/Gemini output. Proceed to outreach send Tuesday based on Perplexity + Claude/Cowork synthesis. Re-run validator pass post-batch if needed. Input: schedule pressure (90-day clock Day 1). Confidence: MEDIUM.
- [2026-05-11] DECISION: CIG Pannonia decision-maker locked. Primary = Attila Zankai (Head Of IT, since April 2021, LinkedIn URL verified). Secondary = László Pataki (Head of IT Operations, since January 2019). Channel = LinkedIn direct message, NOT Profession.hu (wrong channel for B2B vendor pitch). Email backup pattern @cig.eu confirmed. Input: Perplexity deep-research follow-up pass. Confidence: HIGH.
- [2026-05-11] DECISION: CIG Pannonia outreach hook expanded to include DORA + NIS2 regulatory context (verified Hungary applicability), with explicit caveat that CPS does NOT claim NIS2 certification ourselves. Input: Perplexity sourced from Deloitte / OECD / CMS / Aoshearman. Confidence: HIGH.

## Decisions Made

_(empty)_

## Open Questions

- [ ] Chemaxon outreach language: HU (Hungarian HQ per user rule) or EN (international team, global pharma customers)? -- for: Human
- [ ] Is the Free Cloud Health Check CTA still the right ask for first 10 touches, or should we test a paid micro-assessment in parallel? -- for: ChatGPT (Strategist)
- [ ] Should Greenergy be re-engaged via Gergely Geczi after the failed Marko Tamas connect, or marked Lost? -- for: Gemini (Validator)

## Raw Notes

### Session 1: 2026-05-11 -- Engine Warm-Up

**Context loaded:**
- Sales Engine v1.0 built 2026-04-27 (14 days ago)
- Zero outreach sent in those 14 days
- 90-day clock reset today to Day 1
- Phase 1 milestone: 5 HOT outreach by 2026-05-12, all 15 contacted by 2026-05-15
- The 4-AI strategic review (2026-04-27) concluded "execution failure, not strategy failure"
- This scrape is the LAST validation step before outreach goes out tomorrow

**Prompts being sent:**

Perplexity (Researcher) -- factual validation + new lead scrape with sourced data.
ChatGPT (Strategist) -- given the validated list, prioritization and sharpest icebreaker per lead.
Gemini (Validator) -- devil's advocate, false-positive flagging, what we are missing.

**To be filled after sessions run.**
