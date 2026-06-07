---
description: "Assessment of maturity rankings and audience overlap across three presences: Sonrisa Enterprise AI (high maturity for outbound campaigns), Navigátor Podcast (high maturity for audience stewardship), and Personal Builder (low maturity, unpackaged)."
description_source: auto
description_hash: 67977fc656007e6c
schema: presto.strategic-prep-synthesis.v1
date: 2026-05-24
phase: strategic-prep-1
presences_assessed: 3
id: 44befc3f-0b7c-4c4d-8811-9b362ca14571
index_schema_version: 1
---
# Strategic Prep Phase 1 — Cross-Presence Synthesis

> User-directed Strategic Preparation Phase. Multi-mode (audience + discover + reflect). Output: assessment only. No campaigns started, no drafts produced. Phase 2.B compliant.

## 1. Maturity ranking (which presence is readiest)

| Rank | Presence | Maturity | One-line rationale |
|---|---|---|---|
| 🥇 1 | **Sonrisa Enterprise AI (CPS)** | HIGH | Voice published, audience named, competitive lane researched, sales funnel downstream, AWS Partner credibility — a campaigning engine in standby state. |
| 🥈 2 | **Navigátor Podcast** | HIGH (different shape) | Mature content engine with 5,780 installed subs, rigorous channel-intelligence, 9-skill operational stack — but the constraint is preservation, not acquisition. |
| 🥉 3 | **Personal Builder (Becze Szabolcs)** | LOW | Substance exists (BDOS) but is unpackaged; no separate builder-voice artifact; current public surface is fused with CPS-Head identity. |

**Key insight:** The two HIGH-maturity presences are mature in opposite directions. Sonrisa is mature for *outbound campaigning*; Navigátor is mature for *audience stewardship*. They require different first moves.

## 2. Audience overlap analysis

**Pairwise overlap:**

| Pair | Overlap level | Identity-confusion risk |
|---|---|---|
| Sonrisa ↔ Personal Builder | **HIGH** (~70-80% audience overlap — both CTO/operator-flavoured, both Szabolcs-fronted, both English) | **HIGH** — same person, same surface (LinkedIn), risk of fragmenting the published trilogy voice |
| Sonrisa ↔ Navigátor | **LOW** (different language EN vs HU, different topic stack, partial CEE geographic overlap only) | LOW — natural separation by language + topic |
| Navigátor ↔ Personal Builder | **MEDIUM** if Personal Builder operates in Hungarian; LOW if in English | DEPENDS on Personal Builder language decision (open question §6) |

**Critical finding:** the Sonrisa ↔ Personal Builder boundary is the single biggest identity-coherence question. They share the same physical channel (Szabolcs's LinkedIn). Without a deliberate split rule, every builder post competes with the CPS narrative for the same slot.

**Recommendation:** treat Personal Builder as **deliberately downstream of Sonrisa** — earn the right to a separate builder voice by first stabilising the CPS voice. Premature parallel activation will dilute both.

## 3. Narrative coherence map — emerging atomics across presences

Recurring conceptual threads visible across all three:

| Emerging atomic | Sonrisa evidence | Navigátor evidence | Personal evidence |
|---|---|---|---|
| **Team-based / collective > single-hero** | "Team-based delivery, not single-engineer dependency" (the trilogy thesis) | "Harmadik út" value, recurring-guest pattern (Bencze Edit, Dr. Lőrinczi) | Communal / spiritual framing in Gondolatok.md |
| **Honest-broker / alázat as differentiator** | "We'll tell you if in-house is better" (honest-broker headline variant) | "Alázat + bátorság" value pillar | Manager-who-externalises-thinking (BDOS) |
| **Externalised cognition / systems-as-substrate** | Sales Engine (markdown-native), CPS Sales Strategy v2.0 | `Synthesis/` archive, channel-intelligence loop, 9-skill family | BDOS itself (the most original artifact) |
| **Hungarian-rooted / CEE-credible** | Hungary + Romania + CEE focus, sonrisa.hu, Erdély values | HU + Erdély 81.8% combined audience | User location, Hungarian-language reflection |

**Sage signal candidate (NOT WRITTEN — flagged for synthesis §6):** the *"externalised cognition / systems-as-substrate"* row is the most original atomic in the cross-presence map and could become a unifying narrative spine across all three voices — if and when packaged.

## 4. First smoke test recommendation

**Where:** Sonrisa Enterprise AI presence.
**What:** repost trilogy Article #1 ("Why One DevOps Engineer Is Never Enough") — currently hosted on sonrisa.hu — as a **native LinkedIn article under Szabolcs's personal profile**, with a fresh 150-200 word framing intro tied to one current 2026 observation.
**Channel:** LinkedIn (personal profile).
**Narrative:** existing, validated thesis. No new content invention.
**Why:** uses already-published voice, established competitive lane (validated by COMPETITIVE-BRIEF-2026-03-25), audience already named (CTO/CFO in hiring mode), downstream funnel exists (AWS Health Check landing live). Lowest invention cost, highest signal-yield-per-effort, fully reversible (a post can be unpublished).
**What it would prove:** whether LinkedIn-native reposting of trilogy content meaningfully outperforms the sonrisa.hu hosted version on impressions, profile visits, and AWS Health Check CTA clicks. **Validates or invalidates the "trilogy has a second wave on LinkedIn" hypothesis.**
**Cadence:** **one article per 7-10 days**, sequenced in original publication order (Article #1 → Article #2 → Article #3). Measure each before scheduling the next. **NOT a posting schedule — a controlled experiment.**
**Stop conditions:** if Article #1 underperforms its sonrisa.hu baseline, pause and reflect before #2. If it overperforms, the cadence is justified.

**Why NOT Navigátor first:** content already publishes at episode cadence; the audience is invested in a specific voice; downside of a clumsy experiment is higher than the upside. Run Sonrisa smoke test first, then transfer learning to a smaller Navigátor experiment (e.g. EP14 / EP29 evergreen re-promotion on Facebook with a quote-card derivative — measurable, on-brand, addresses documented FB-strategy gap).

**Why NOT Personal Builder first:** builder-identity statement and first declassified public artifact do not yet exist. Premature smoke test would generate misleading signal.

## 5. Cross-cutting risks (top 3)

1. **Identity collision on Szabolcs's LinkedIn surface (Sonrisa ↔ Personal Builder).** Without a stated post-mix rule, builder-content will erode the CPS trilogy's coherence. Highest-priority cross-cutting risk.
2. **NIS2 / claim-validation discipline across all three presences.** Already a documented Sonrisa rule (CPS does not have NIS2 certification); the same publish-time validation gate must apply across Personal and Navigátor as the multi-presence operation scales — otherwise the gate erodes by inattention.
3. **Voice-amplification damaging Navigátor's established trust.** The most valuable asset across all three presences is the 5,780-subscriber Navigátor audience. Any cross-presence campaigning that pushes Navigátor-listeners into Sonrisa / Personal funnels without earning the bridge risks audience trust loss — and trust is the only thing that scales for a long-form podcast.

## 6. Open questions for Sage (audience-gap candidates)

> **NOT WRITTEN to `Ideas/_inbox/sage-signals/`.** Flagged here per task constraint (Sage permitted-flow respect: assessment phase only).

- **Sage-candidate 1:** is there an atomic for *"manager externalises cognition into markdown + agents"* in `Ideas/atomic/`? If yes, it is the natural Personal Builder narrative spine. If no, it is an audience-gap (`presto.sage-signal.v1` type `audience-gap` candidate).
- **Sage-candidate 2:** is there an atomic for *"AI-ops / operational intelligence as managed service"* — the natural Sonrisa narrative extension beyond the trilogy? If no, this is the second audience-gap candidate.
- **Sage-candidate 3:** is there an atomic for *"recurring-guest interview as audience-loyalty mechanic"* — distilling the Bencze Edit / Dr. Lőrinczi Navigátor pattern? Useful for Navigátor cross-episode packaging.

## 7. Phase 2 roadmap

**Phase 2 (next session, user-directed):**

1. **Sage atomic-gap resolution.** Run `sage-find` on the three Sage-candidates in §6. Any audience-gap that surfaces → proper `Ideas/_inbox/sage-signals/<date>_audience-gap-<slug>.md` write.
2. **Sonrisa smoke test setup.** Create `02_Areas/Sonrisa/Marketing/Campaigns/trilogy-linkedin-native-wave/CAMPAIGN.md` with first task = Article #1 repost. Confirmation-gate per Presto §7. **No draft writing yet** — only campaign-state scaffolding.
3. **Personal Builder identity statement.** One paragraph: what does Becze Szabolcs publish under his own name distinct from "Head of CPS"? User-authored, Presto facilitates. **Blocker for any Personal Builder smoke test.**
4. **Navigátor Facebook archaeology.** Targeted Librarian retrieve on "Facebook references in Navigátor scope" to close the documented FB-strategy gap. Read-only.
5. **Cross-presence post-mix rule for LinkedIn.** A simple stated discipline: what fraction of Szabolcs's LinkedIn posts are CPS-positioned vs builder-positioned, and what triggers a builder-positioned post. Defends against risk #1 (§5).

**Phase 3 (after smoke-test signal):**

- Sonrisa smoke test → if positive, sequence trilogy Article #2 + #3, then plan AI-ops narrative extension.
- Navigátor smoke test → EP14 / EP29 evergreen re-promotion experiment (Facebook) — only after Sonrisa signal is in.
- Personal Builder → first declassified BDOS public artifact (one capability page, one diagram) — only after identity statement exists.
- **Thinking Engine activation candidates** (deferred from §9 of each per-presence assessment) — invoke selectively based on actual smoke-test signal, never speculatively.
