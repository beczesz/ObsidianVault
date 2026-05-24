---
schema: presto.strategic-prep.v1
date: 2026-05-24
presence: Sonrisa Enterprise AI Presence (CPS-led)
status: assessed
maturity_level: high
smoke_test_readiness: recommended-first
id: b317ce06-309a-428e-9b79-e5b08848705d
index_schema_version: 1
---

# Sonrisa Enterprise AI Presence — Strategic Prep Assessment

> **Scope:** Enterprise AI, AI operations, cloud operations, DevOps transformation, operational intelligence, AI-native company infrastructure — primarily through the **Cloud Platform Services (CPS)** business unit, with Becze Szabolcs as Head of CPS as the public face.

## 1. Vault archaeology — what exists

**Marketing-relevant assets in `02_Areas/Sonrisa/CPS/Marketing/`:**

- `about-szabolcs.md` v1.0 (2026-05-12) — **canonical CPS-scoped bio** (LOCKED headline, LinkedIn About LIVE, 5 skills pinned, 50-word/150-word/300-word variants ready)
- `CPS - Introduction - Short.md` — short corporate intro
- `Sonrisa general description.md` — parent company description
- `Blogs/` — **three published LinkedIn articles already LIVE on sonrisa.hu:**
  1. `#1 [Managed Service] Why One DevOps Engineer Is Never Enough` → article 18
  2. `#2 [Managed Service] Managed DevOps vs Hiring In-House` → article 22
  3. `#3 [Managed Service] The Hidden Costs of Hiring vs Managed Services` → article 23
- `Blogs/COMPETITIVE-BRIEF-2026-03-25.md` — competitor landscape (Palark, SDH Global, OpsWorks Co.) + the strategic finding: **"the hire-vs-outsource content lane is wide open."**
- `Blogs/Ideas/Plan.md` — funnel logic for the trilogy (Article 1 awareness → Main article decision-framework → Article 2 financial close)
- `website/` — extensive landing page work (AWS Health Check v0.2, Azure DevOps landing v0.1→v0.4, llmaas-landing v11, managed-service v0.4, insights page sellvio v0.4, intermediary v0.5→v0.9). Strong velocity here.
- `selvio/` — CMS-rendered pages (about_us, legacy_modernization, full_page)

**Strategic substrate in `Sonrisa/CPS/Strategy/`:**
- `CPS Sales Strategy v2.0.md` — 3-engine model + 90-day plan
- `BMC v1.3.md`, `Roadmap.md`, `AI Ops/`, `FinOps/`, `Competitor Reports/`, `AWS/`, `Managed service/`
- `Strategy Dashboard.canvas`, `dashboard.html`

**Operational depth:** `Sales/SALES_ENGINE.md` is the testbed where the markdown-native engine pattern Presto inherits originated. **This is the most operationally mature unit in the entire vault.**

## 2. Current state assessment

**Maturity: HIGH** — and by a large margin the highest of the three presences.

- Voice is **established and published** (3 LinkedIn articles already in market, consistent tone — honest-broker, decision-framework, pain-led).
- Audience is **named and qualified** (mid-sized enterprises 50-500 employees, CTOs/CFOs in "hiring mode" — explicit ICP).
- Competitive positioning is **researched** (COMPETITIVE-BRIEF identified the open content lane).
- Strategic narrative spine exists: *"team-based delivery, not single-engineer dependency"* — repeatable across surfaces.
- AWS Select Tier partner working toward Advanced — provides external credibility anchor.
- Pricing is **public-ready** and unusually transparent for the space (Safety Net €990 → Scale €6,000), which the COMPETITIVE-BRIEF flags as a weapon.

**Gap:** the "Enterprise AI / AI Ops / operational intelligence" surface is **named in the strategy** (`Strategy/AI Ops/`, `llmaas-landing-page`) but not yet anchored by published content. The trilogy is managed-services-positioned; the AI-ops positioning is one layer deeper but not yet voiced.

## 3. Channel inventory

| Channel | Status | What lives there | Notes |
|---|---|---|---|
| sonrisa.hu/en/our-impact/article/ | LIVE | 3 published articles trilogy | The corporate site is hosting the personal-voice articles |
| LinkedIn (personal — Szabolcs) | LIVE | About section, 5 skills, GreeHill project, trilogy as Featured candidates | Trilogy not yet reposted as LinkedIn articles |
| LinkedIn (Sonrisa company page) | Status not documented in vault | — | Worth a quick verification before campaigning |
| AWS Partner directory | Select Tier listed | Profile exists | Underused as a content surface |
| Conferences | Craft Conference 2026-06-04, AWS Community Day CEE 2026-09-17 | Speaker bio variants ready | Future content multiplier |
| Cloud Health Check (free entry point) | Live offer | Lead-magnet candidate | Unique vs competitors |

## 4. Audience hypothesis

**Primary (high-confidence):** CTOs and engineering managers at 30-500 person companies running AWS / Azure who feel "one DevOps engineer away from chaos." Hungary + CEE + DACH + select US. Bilingual but **English** is the publishing default for reach.

**Secondary:** CFOs / COOs evaluating in-house build vs managed services — the financial-close angle of Article 3.

**Tertiary (latent):** Enterprise AI / AI-ops buyers — companies asking "what does it mean to run AI workloads in production reliably." Not yet activated; this is the natural next narrative extension.

## 5. Communication risks

- **Trilogy fatigue / topical saturation.** Three articles on the same managed-services thesis are now in market; a fourth in the same lane risks diminishing returns. The narrative needs to either deepen (case study) or laterally extend (AI-ops).
- **NIS2 trap (already flagged in CLAUDE.md).** CPS does not have NIS2 certification — any marketing material must scrub NIS2-readiness claims. **Recurring publish-time validation needed.**
- **AI-ops positioning without proof.** Strategy mentions LLMaaS and AI ops; publishing AI-narrative content without a live AI-ops engagement to point at would weaken the established credibility of the managed-services voice.
- **Sales-marketing decoupling risk.** Sales Engine is operating at high cadence (KPI: 25 first touches/week). If marketing publishes content that doesn't feed that funnel directly, the two engines drift.
- **Verify-before-send rule (2026-05-20).** Already a sales-side discipline; the same gate applies to any campaign referencing a competitor / lead / claim in real time.

## 6. Strategic opportunities

- **The trilogy is already a campaign-in-place.** Reposting the 3 articles as native LinkedIn articles under Szabolcs's personal profile (currently they live on sonrisa.hu) would unlock a second wave of reach without producing new content. **Lowest-cost, highest-leverage move available.**
- **Case-study-as-content.** Three named delivery wins exist (Hungarian national energy billing → OpenShift, 4TB media monitoring → AWS EKS in 3 months, US travel platform). Any one of these as a narrative case study would extend the trilogy into proof.
- **Pricing transparency campaign.** COMPETITIVE-BRIEF identified this as a differentiator (Palark hides pricing, SDH packages aren't public, OpsWorks is hourly). A single post titled "Here's exactly what managed DevOps costs at CPS" would be unusually defensible.
- **AWS Health Check as lead-magnet.** Free entry point, unique vs competitors. Marketing surface for it (the `aws-health-check-v0.2.html` landing) exists; activation is a deliberate distribution problem, not a content problem.
- **Conference content multiplier.** Craft Conference (June) and AWS Community Day CEE (September) — both will produce talk recordings, which extend a single talk into 4-6 derivative content pieces per appearance.

## 7. Smoke test readiness

**RECOMMENDED-FIRST.** Of the three presences, this is the only one where:
- voice is calibrated,
- audience is named,
- content already exists in market,
- competitive position is researched,
- a measurable lead-funnel sits downstream.

A first smoke test from here can produce real signal in days, not months, and the downside is bounded (the corporate brand absorbs experimentation risk).

**Suggested smoke test (handed to synthesis §4):** repost trilogy Article #1 ("Why One DevOps Engineer Is Never Enough") as a native LinkedIn article under Szabolcs's personal profile, with a fresh 200-word framing intro tied to a current observation. Measure: impressions, profile visits, inbound CTA clicks to AWS Health Check. Cadence: one article per 7-10 days, sequenced as published trilogy order.

## 8. Recommended Librarian queries for v2 (optional)

- "All CPS case-study material — Hungarian energy billing / media monitoring / US travel platform — narratable detail."
- "AWS Health Check assets — current landing, what is the funnel currently capturing."
- "AI Ops / LLMaaS strategy material — what is documented vs experienced."

## 9. Thinking Engine research candidates (optional)

- **Discover-mode:** "Is there an emerging AI-ops / LLMOps audience cluster on LinkedIn EN that overlaps with managed-services-curious CTOs?" — Perplexity (market scan) + ChatGPT (audience-cluster hypothesis).
- **Reflect-mode (post-smoke-test only):** if the LinkedIn-native repost smoke test runs, then Thinking Engine can validate whether the engagement pattern is one-off or stable before recommending a second wave.

**Recommendation: skip both for now.** This presence does not need outside research to take its first step — the vault already contains everything required.
