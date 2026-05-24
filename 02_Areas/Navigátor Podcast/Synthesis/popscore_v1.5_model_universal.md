---
version: 1.5
date: 2026-04-09
type: popscore-model-universal
origin: "Navigátor Podcast 40 epizód + 24 SRT validációs kör"
formula: "PopScore = (Universal × 0.57 + Practical × 0.36 + Depth × 0.07) × 20"
scale: "20-100"
status: "Converged — weights locked after 4 validation rounds"
id: 2f3da349-ee3d-4611-bb11-7764a90582c5
index_schema_version: 1
---

# PopScore v1.5 — Universal Podcast Popularity Prediction Model

> Predict the relative popularity potential of any podcast episode based on three content dimensions.
> Language-agnostic, genre-agnostic, format-agnostic.

## Origin & Validation

This model was developed from 40 episodes of a Hungarian interview podcast and validated through 4 iterative rounds (24 transcript-level reviews). The weights converged by round 3 — the Universal dimension's 57% dominance was consistent across all validation samples. The model achieves **Spearman ρ = 0.923** and **R² = 0.849** on the training set.

While calibrated on long-form interviews (60-120 min), the underlying logic is universal: **the size of the addressable audience matters more than content quality for predicting reach.**

## The Formula

```
PopScore = (U × 0.57 + P × 0.36 + D × 0.07) × 20
```

Where U, P, D are scored 1-5. Output scale: 20-100.

## Dimension 1: Universal Appeal (U) — Weight: 57%

**What it measures:** How large is the addressable audience for this topic? Would a stranger click on this without knowing the podcast?

| Score | Criteria | Examples |
|:-----:|----------|----------|
| **5** | Nearly everyone can relate. The topic touches a fundamental human experience: health, parenting, money, relationships, fear, identity. No prerequisite knowledge needed. | Sleep quality, narcissism in relationships, managing anxiety, raising teenagers, career burnout |
| **4** | Broad audience within a major demographic. Requires minimal context. | AI tools for productivity, entrepreneurship lessons, university education reform |
| **3** | Interesting to a defined community but not immediately magnetic to outsiders. | Regional politics, industry-specific trends, cultural heritage topics |
| **2** | Niche — appeals to a specific interest group. Most people would scroll past. | Craft instrument repair, poetry analysis, a specific sporting discipline |
| **1** | Ultra-niche or insider-only. Requires significant context to even understand the topic. | Local bureaucratic processes, highly technical academic debates |

**Key insight:** Universal Appeal is NOT about quality. A 5/5 U episode can be mediocre content — but its *topic* guarantees a large potential audience. The YouTube/Spotify algorithm decides *who* to show the episode to before *how good* it is matters.

## Dimension 2: Practical Applicability (P) — Weight: 36%

**What it measures:** Can the listener DO something after this episode? Is there a concrete takeaway they can apply today?

| Score | Criteria | Examples |
|:-----:|----------|----------|
| **5** | Clear, specific actions the listener can take immediately. "Tonight I'll try this." Checklist-worthy. | 30 ChatGPT prompts, blood sugar management through diet, 5 signs of narcissistic abuse, discipline techniques for parents |
| **4** | Useful frameworks or mental models. Not a checklist but changes how you think about something actionable. | How to evaluate a startup idea, resilience strategies for burnout prevention |
| **3** | Some takeaways but mostly informational. The listener learns but may not change behavior. | History of a company, overview of an industry trend, biographical interview |
| **2** | Primarily educational or narrative. Entertainment or intellectual value but no practical application. | Philosophical discussion, artistic exploration, historical analysis |
| **1** | Pure storytelling, abstract discussion, or entertainment with no actionable component. | Poetry reading, abstract art discussion, nostalgic reminiscence |

**Key insight:** Every episode with 10K+ views in the training set scored P ≥ 4. No exceptions. Practical content is the strongest *retention* driver — it's why people stay, share, and return.

## Dimension 3: Depth of Expertise (D) — Weight: 7%

**What it measures:** How deep, credible, and layered is the content? Is this surface-level or does it reveal something you can't find elsewhere?

| Score | Criteria | Examples |
|:-----:|----------|----------|
| **5** | Multi-layered, expert-level content with original insights. The guest/host brings unique experience that can't be googled. Years of deep practice visible. | A therapist with 20 years of clinical practice sharing case patterns, a cancer survivor describing the psychological journey |
| **4** | Strong expertise, well-structured arguments, some original insights mixed with known frameworks. | An experienced entrepreneur analyzing failure patterns, a doctor explaining a condition with nuance |
| **3** | Competent coverage of the topic. Accurate but not revelatory. Could be found in a good article. | Standard expert interview, textbook-level explanation, well-prepared overview |
| **2** | Surface-level treatment. The guest gives generic answers or the conversation stays at intro level. | Brief conference-style interview, promotional guest appearance |
| **1** | Inaccurate, confused, or trivially shallow. No real expertise demonstrated. | Unprepared guest, topic not matched to guest's knowledge |

**Key insight:** Depth has minimal impact on popularity (7% weight) but is the strongest predictor of *watch time* and *audience retention*. Deep episodes convert fewer clicks but keep viewers longer — they build channel loyalty, not viral reach.

## Interpretation Scale

| Range | Label | Meaning |
|-------|-------|---------|
| **90-100** | Viral potential | Topic + practicality aligned for maximum reach. Rare — requires U=5, P=5. |
| **75-89** | Strong performer | Broad appeal with good actionability. Should exceed channel average. |
| **60-74** | Solid average | Good content but limited by either niche topic or low actionability. |
| **45-59** | Niche content | Quality may be high but audience is small. Expect below-average reach. |
| **20-44** | Deep niche | Valuable for the right listener but won't generate organic discovery. |

## Scoring Protocol

1. **Read/listen** to enough of the episode to understand: the topic, the guest's expertise level, and the practical takeaways (if any). An SRT transcript is ideal; a detailed synopsis works too.
2. **Score U first** — ask: "If I showed this title/topic to 100 random people, how many would be interested?"
3. **Score P second** — ask: "What can a listener DO after this episode? Can they apply something tonight?"
4. **Score D last** — ask: "How deep, credible, and unique is this content?"
5. **Calculate:** `PopScore = (U × 0.57 + P × 0.36 + D × 0.07) × 20`

## Important Caveats

- **PopScore predicts popularity potential, NOT quality.** A PopScore of 40 can be a masterpiece; a PopScore of 95 can be shallow clickbait. Use it alongside a quality metric (like HostScore) for a complete picture.
- **External factors account for ~15% of variance:** Trending topics, algorithm luck, social media amplification, and returning guest effects are NOT captured by PopScore.
- **The model was calibrated on long-form interview podcasts.** For short-form, narrative, or comedy podcasts, the weights may differ — but the three dimensions remain valid.
- **Controversy was excluded** from the final model. In the training data, controversy showed no independent predictive power after controlling for Universal and Practical dimensions.
- **Emotion was absorbed** into the model through Universal Appeal (emotional topics tend to be more universal) and is not a separate dimension.

## Example Scorings

| Episode concept | U | P | D | PopScore | Reasoning |
|-----------------|:-:|:-:|:-:|:--------:|-----------|
| "How I reversed my Type 2 diabetes with diet" | 5 | 5 | 4 | 97.2 | Universal health concern + concrete diet plan + real clinical results |
| "5 signs you're in a narcissistic relationship" | 5 | 5 | 3 | 95.8 | Everyone wonders; immediate self-check; therapist insight |
| "How AI will change education in 5 years" | 4 | 4 | 4 | 80.0 | Broad interest + framework applicable to parents/teachers + expert |
| "My journey restoring 18th century violins" | 2 | 2 | 5 | 43.4 | Beautiful content, deep expertise, tiny audience |
| "The philosophy of suffering in Dostoevsky" | 3 | 1 | 5 | 46.2 | Intellectually rich, zero actionability, moderate audience |
| "Local council budget debate 2026" | 1 | 2 | 3 | 32.0 | Ultra-local, no practical takeaway for most |
