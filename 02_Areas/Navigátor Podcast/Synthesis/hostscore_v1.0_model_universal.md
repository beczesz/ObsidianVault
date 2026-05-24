---
version: 1.0
date: 2026-04-09
type: hostscore-model-universal
origin: "Navigátor Podcast 40 epizód SRT-alapú értékelés"
formula: "HostScore = (Q × 0.30 + S × 0.20 + P × 0.25 + A × 0.15 + C × 0.10) × 20"
scale: "20-100"
dimensions: "Q=Question Quality, S=Space Management, P=Personal Presence, A=Arc & Pacing, C=Chemistry"
id: 1cd2ab0f-0dad-4527-b78b-2d7e77c121f5
index_schema_version: 1
---

# HostScore v1.0 — Universal Podcast Host Performance Model

> Evaluate any podcast host's performance on a per-episode basis.
> Works for interview podcasts, panel shows, and (with adaptation) solo formats.

## Origin & Validation

Developed from scoring 40 episodes of a Hungarian long-form interview podcast across the full SRT transcript of each episode. The five dimensions and their weights reflect what differentiates a *competent* host from an *exceptional* one in the deep-interview format.

The model is format-transferable: the dimensions apply to any conversational podcast. For solo/monologue formats, see the adaptation notes at the end.

## The Formula

```
HostScore = (Q × 0.30 + S × 0.20 + P × 0.25 + A × 0.15 + C × 0.10) × 20
```

Where Q, S, P, A, C are scored 1-5. Output scale: 20-100.

## Why These Weights?

The weights reflect the relative importance of each dimension in the training data:

- **Question Quality (Q) — 30%:** The largest weight because questioning is the host's primary craft. A great question opens the guest up; a poor one closes them down. In the training data, every 90+ HostScore episode had Q ≥ 5.
- **Personal Presence (P) — 25%:** The second largest because it's what separates an interviewer from a *conversational partner*. In the training data, the single strongest predictor of an above-average HostScore was the host sharing a personal vulnerability (score J ≥ 4).
- **Space Management (S) — 20%:** The balance between host and guest talk time. Critical in interview format — too much host talk drowns the guest; too little means the conversation drifts without direction.
- **Arc & Pacing (A) — 15%:** The dramaturgical structure: does the conversation build, reach a peak, and close well? Lower weight because arc is partly guest-dependent.
- **Chemistry (C) — 10%:** The smallest weight because chemistry depends on two people — it's unfair to penalize a host for a closed-off guest. But when it's there, it elevates everything.

## Dimension 1: Question Quality (Q) — 30%

**What it measures:** Does the host ask questions that open the conversation to unexpected depth? Are there follow-ups? Does the guest say things they wouldn't say elsewhere?

| Score | Criteria |
|:-----:|----------|
| **5** | Questions probe beneath the surface, surprise the guest, provoke genuine reflection. Strong follow-ups that don't let surface answers slide. The guest reveals something new — things they haven't said on other podcasts. Questions come from genuine curiosity, not a script. |
| **4** | Good questions with several deep moments. Follow-ups are mostly present. The guest is comfortable but also challenged at times. |
| **3** | Competent questioning but predictable. "Tell me about…" dominates. Rarely digs deeper. The conversation stays at the level the guest sets — no host-driven escalation. |
| **2** | Surface-level or checklist-style. The guest could monologue without interruption. Few follow-ups. Questions don't build on answers. |
| **1** | Questions don't connect to answers. The host follows their own agenda regardless of what the guest says. No listening is evident. |

**Diagnostic test:** After the episode, can you point to a moment where the *host's question* — not the guest's story — created the most interesting moment? If yes, Q ≥ 4.

## Dimension 2: Space Management (S) — 20%

**What it measures:** The allocation of airtime and conversational control. Is the guest given room to develop ideas while the host maintains direction?

| Score | Criteria |
|:-----:|----------|
| **5** | Perfect balance: the guest speaks ~65-75% of the time, but the host's presence is felt throughout. The host knows when to stay silent and when to interject. No unnecessary interruptions, no runaway monologues. |
| **4** | Good ratio with minor imbalances. Generally well-controlled. |
| **3** | Acceptable but noticeable imbalance. Either the host talks too much (50%+) limiting the guest, or is too passive and the conversation drifts. |
| **2** | Significant imbalance. The host dominates OR completely disappears, losing control of the conversation. |
| **1** | The guest barely speaks OR the host is entirely absent and the guest delivers an unstructured monologue. |

**Diagnostic test:** Did you ever feel the host was "in the way" (over-talking) or "missing" (under-steering)? If neither, S ≥ 4.

**Multi-guest note:** With 2+ guests, space management becomes harder. The host must also manage guest-to-guest dynamics. The baseline tends to drop by 1 point relative to single-guest episodes.

## Dimension 3: Personal Presence (P) — 25%

**What it measures:** Is the host a real person in the conversation — or just a question-delivery mechanism? Do they share their own experiences, vulnerabilities, and reactions?

| Score | Criteria |
|:-----:|----------|
| **5** | The host shares personal stories and vulnerabilities relevant to the topic. They react emotionally and authentically to the guest's words. They bring their own experience into the conversation — not to compete with the guest, but to deepen the dialogue. The listener feels they know the host better after this episode. |
| **4** | Some personal sharing and authentic reactions. The host is present as a person, not just a role. |
| **3** | Professional but distant. The host stays in "interviewer mode." Few personal disclosures. Competent but anonymous — you could replace them with another competent host and the episode would feel the same. |
| **2** | Almost no personal presence. The conversation is purely transactional: question → answer → next question. |
| **1** | Completely detached. Robotic questioning. No human connection is detectable from the transcript. |

**Diagnostic test:** Remove the host's name — could you tell *who* the host is just from how they speak and what they share? If yes, P ≥ 4.

**This is the differentiating dimension.** In the training data, 17 of 40 episodes (42.5%) clustered at the 60.0 baseline (all dimensions = 3). Every episode that scored above 70 had P ≥ 4. Personal presence is what elevates a competent host to a memorable one.

## Dimension 4: Arc & Pacing (A) — 15%

**What it measures:** Does the conversation have a dramaturgical structure? Is there a build, a climax (emotional or intellectual), and a satisfying close?

| Score | Criteria |
|:-----:|----------|
| **5** | Clear arc: relaxed opening → progressive deepening → emotional/intellectual peak → powerful closing synthesis. Tempo varies appropriately — breathing room after intense moments. The episode feels like a *journey*, not a list of topics. |
| **4** | Discernible arc with a mostly strong close. One section may drag but overall momentum is good. |
| **3** | Linear progression without a clear peak. Steady tempo but not dynamic. The close is adequate but not memorable. |
| **2** | Fragmented or sluggish. No peaks. The conversation wanders or suddenly ends without closure. |
| **1** | Chaotic — the listener can't tell where they are in the conversation. No structure, no direction. |

**Diagnostic test:** Can you identify the single best moment of the episode — and does it occur in the second half? If yes, A ≥ 4 (good episodes build toward their peak).

## Dimension 5: Chemistry with Guest (C) — 10%

**What it measures:** The interpersonal dynamic between host and guest. Do they enjoy the conversation? Is there genuine rapport?

| Score | Criteria |
|:-----:|----------|
| **5** | Visible mutual enjoyment. Natural laughter, finishing each other's thoughts, spontaneous moments of co-discovery. The conversation feels like a dialogue between friends exploring an idea together. |
| **4** | Good dynamic, natural back-and-forth. Chemistry flashes at moments. |
| **3** | Respectful but formal. Functional but no spark. Professional distance maintained throughout. |
| **2** | Tense or awkward dynamic. Either the host or guest seems uncomfortable. Visible mismatches in energy or communication style. |
| **1** | The dynamic clearly doesn't work. Awkward silences, misunderstandings, visible discomfort. |

**Diagnostic test:** Would these two people have coffee together after the recording? If obviously yes, C ≥ 4.

**Important:** Chemistry is weighted lowest (10%) because it depends on *both* people. A host shouldn't be penalized for a reserved guest. But when chemistry is high, it amplifies everything else.

## Interpretation Scale

| Range | Label | What it means |
|-------|-------|---------------|
| **90-100** | Outstanding | Rare — requires near-maximum scores across dimensions. The host was fully present, asked transformative questions, and the conversation had a clear arc. These episodes become the podcast's signature moments. |
| **75-89** | Strong | Above-average performance. Notable personal presence and/or exceptional questioning. These episodes build the host's reputation. |
| **60-74** | Competent average | Solid hosting — professional, prepared, no major issues. This is the baseline for a good host. Most episodes of most good podcasts live here. |
| **45-59** | Below average | Noticeable weaknesses — often caused by overly formal guests, host passivity, or poor topic-host fit. Identifiable improvement areas. |
| **20-44** | Problematic | Significant issues in multiple dimensions. Rare for an experienced host unless dealing with extreme circumstances. |

## Scoring Protocol

1. **Read/listen** to the full episode (or representative sections: opening 10 min, a middle section, closing 10 min). SRT transcript is ideal.
2. **Score Q first** — focus on the host's questions and follow-ups.
3. **Score S second** — estimate the talk-time ratio and conversational control.
4. **Score P third** — identify moments of personal sharing, vulnerability, or authentic reaction.
5. **Score A fourth** — assess the overall arc from opening to close.
6. **Score C last** — evaluate the interpersonal dynamic.
7. **Calculate:** `HostScore = (Q × 0.30 + S × 0.20 + P × 0.25 + A × 0.15 + C × 0.10) × 20`

## Patterns from Training Data (40 episodes)

These patterns emerged from scoring 40 episodes and may help calibrate scoring for other podcasts:

1. **The "Baseline Cluster":** 42.5% of episodes scored exactly 60.0 (all dimensions = 3). This is the natural resting state of a competent, prepared host. It's not bad — it's the professional standard.

2. **Personal Presence (P) is the breakout dimension.** Every episode above 70.0 had P ≥ 4. The host's willingness to be vulnerable is what separates good from great.

3. **Two guests lower the score.** Multi-guest episodes averaged 60.6 vs 67.8 for single-guest. The host becomes a moderator, reducing space for personal presence.

4. **Formal guests suppress the host.** Politicians, executives, and high-status guests correlated with lower P and C scores. The host tends to be more cautious, less personal.

5. **Returning guests elevate performance.** When a guest returns, trust is pre-established — the host can go deeper from minute one. Average HostScore for return guests: 89.0 vs 64.1 for first-timers.

6. **HostScore and PopScore are moderately correlated but NOT equivalent.** Good hosting helps popularity but doesn't guarantee it. An episode with HostScore 60 and PopScore 98 (strong topic, weak hosting) will outperform HostScore 96 and PopScore 50 (brilliant hosting, niche topic) in views.

## Format Adaptations

### Solo/Monologue Format
For solo episodes, adapt the dimensions:
- **Q → Conceptual Depth:** Does the host pose interesting questions to the audience/themselves?
- **S → Information Density:** Is the content well-paced — neither too dense nor too sparse?
- **P → Personal Presence:** Same — does the host share themselves?
- **A → Arc & Pacing:** Same — is there structure and build?
- **C → Audience Connection:** Does the host acknowledge/anticipate the listener's reactions?

### Panel/Debate Format
- **Q → Facilitation Quality:** Does the host draw out all panelists equally and ask probing questions?
- **S → Balance Management:** Does each panelist get fair time? Does the host prevent domination?
- **P, A, C:** Same as standard model.

### Narrative/Storytelling Format
- **Q → Editorial Choices:** Are the right questions asked at the right moments in the story?
- **S → Host vs. Story Balance:** Does the host stay out of the way when the story speaks for itself?
- **P, A, C:** Same as standard model.

## Important Caveats

- **HostScore measures host performance, NOT episode quality.** A mediocre host can be saved by a brilliant guest; a brilliant host can be limited by a closed-off guest.
- **Transcript-only scoring is limited.** Tone of voice, body language, facial expressions, and editing are invisible in text. A score based on audio/video may differ by ±5-10 points.
- **Cultural calibration may be needed.** "Personal presence" means different things in different cultures. In some cultures, a 3/5 P (professional distance) is the expected norm, not a deficit.
- **Sample size:** The weights were derived from 40 episodes of one podcast. Larger datasets may refine the weights — but the five dimensions are robust across formats.
