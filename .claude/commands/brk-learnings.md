---
description: Broker LEARNINGS — active/proposed/retired sales-learnings listája. Default: active. `--proposed` flag = pending review.
id: a1c5691e-78b3-48af-a40e-16fda36dd14b
index_schema_version: 1
---

A felhasználó sales-learning listát kér.

**$ARGUMENTS** — opcionális: üres → active, `--proposed`, `--retired`.

**Tennivaló:**

1. Glob: `00_Prompts/BDOS/agents/broker/sales-learnings/<state>/*.md`
2. Olvasd frontmatterek, rendezés confidence DESC
3. Output: slug + type + confidence + evidence-szám + 1-2 mondat

8 type: objection-pattern, cycle-timing, cohort-signal, outreach-tone, qualification-criteria, competitor-context, loss-pattern, referral-mechanic.

Olvasás-only.
