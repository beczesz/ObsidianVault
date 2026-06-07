---
title: "Amodei vs Sutton on Learning Algorithms"
description: "Comparison of Amodei and Sutton's positions on whether current LLM scaling represents the path to AGI. Both agree compute beats human priors, but diverge on whether LLMs optimize the correct objective or merely a proxy for intelligence."
description_source: auto
description_hash: 7e28a89d71f3eaab
type: contrast
tags: ["contrast", "AI", "scaling", "bitter-lesson", "learning", "sample-efficiency"]
status: "triaged"
confidence: "medium"
created: "2026-02-24"
processed_by: "AI Speed-Reading Agent"
id: 1b8e97c0-ad35-4b25-ac69-e7764fdf3891
index_schema_version: 1
---
# Amodei vs Sutton on Learning Algorithms

## Dario Amodei (Anthropic)

Agrees deeply with Sutton's "Bitter Lesson" that general compute/data beat human-designed inductive biases. The Big Blob of Compute hypothesis is essentially a seven-factor formalisation of that insight. Pre-training and RL are the current exemplars of scalable objective functions, and both are now confirmed to follow log-linear improvement curves. Current LLMs *are* on the right path to AGI — the exponential is nearly complete.

## Rich Sutton (Alberta / DeepMind)

The Bitter Lesson holds: compute and search beat human-designed priors consistently. However, Sutton (as paraphrased by Dwarkesh in the episode) is notably *non-LLM-pilled*. His objection: a system with "the true core of human learning" would not require billions of dollars of data and bespoke RL environments to learn how to use everyday tools. The sheer resource requirement hints that LLMs are scaling a *proxy* for intelligence, not the real algorithm. The Bitter Lesson applies, but we may be bitter-lessoning the wrong objective.

## Overlaps

Both believe compute is the primary driver of progress. Both reject the idea that human-designed architectural tricks are the key. Both accept that general learning algorithms beat specialised ones.

## Differences

| Axis | Amodei | Sutton |
|---|---|---|
| Are LLMs on the right path? | Yes | Uncertain / skeptical |
| Sample efficiency | Explained by evolution analogy | Suggests wrong learning algorithm |
| Current scaling targets | Pre-training + RL objectives | May need genuinely different objective |
| AGI proximity | 1–3 years via current path | Open / skeptical |

## My Synthesis

…

## Sources

- [[Dwarkesh_DarioAmodei_EndOfExponential_2026-02-13]]
- Rich Sutton, "The Bitter Lesson" (2019)
