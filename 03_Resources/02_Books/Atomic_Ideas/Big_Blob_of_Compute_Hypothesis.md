---
title: "Big Blob of Compute Hypothesis"
description: "Dario Amodei's framework proposing that AI progress depends primarily on seven stable factors, compute, data, duration, objective functions, and engineering stability, rather than algorithmic breakthroughs. Relevant to researchers studying scaling laws and AI development trajectories."
description_source: auto
description_hash: 9b40ce49d7fa7003
type: atomic
tags: ["atomic", "AI", "scaling", "compute", "machine-learning", "AGI"]
status: "triaged"
confidence: "high"
created: "2026-02-24"
processed_by: "AI Speed-Reading Agent"
id: 6d420fbf-64b6-4106-8f0b-ff5c5e59c1ce
index_schema_version: 1
---
# Big Blob of Compute Hypothesis

## Definition

Coined by Dario Amodei in a 2017 internal document (before GPT-1's release), this framework claims that AI progress is governed by seven stable factors rather than clever algorithmic innovations:

1. **Raw compute** — total computational power available for training
2. **Data quantity** — amount of training data
3. **Data quality and breadth of distribution** — data must represent a *wide* range of tasks and domains
4. **Training duration** — how long you iterate over the data
5. **Scalable objective functions** — loss functions that improve indefinitely with more compute (pre-training cross-entropy and RL goal-reward objectives both qualify; narrow objectives do not)
6–7. **Numerical stability and conditioning** — engineering techniques ensuring compute flows in a stable "laminar" way rather than hitting instabilities

The central claim: all the cleverness, bespoke techniques, and "we need a new method" thinking matters far less than these seven levers. This echoes Rich Sutton's "Bitter Lesson" published two years later.

**Key update (2026):** RL training now follows the same log-linear scaling curves as pre-training, when applied to broad task distributions — confirming the hypothesis extends beyond language modelling to the post-training phase.

## Sources

- [[Dwarkesh_DarioAmodei_EndOfExponential_2026-02-13]] (Sections 1–2)
- Rich Sutton, "The Bitter Lesson" (2019)

## Connections

- Related: [[End_of_the_Exponential]], [[Pre_Training_as_Artificial_Evolution]], [[RL_and_InContext_Learning_Complementarity]]
- Opposed: [[Amodei_vs_LeCun_on_Scaling]] — LeCun argues scaling is insufficient without architectural innovations for world-modelling

## My Reflection

…
