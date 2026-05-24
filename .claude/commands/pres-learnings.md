---
description: Presto LEARNINGS — active/proposed/retired audience-learnings listája. Default: active. `--proposed` flag = pending review.
id: 6832b9da-5830-467f-af92-2b00738a8cc9
index_schema_version: 1
---

A felhasználó Presto audience-learning listát kér.

**$ARGUMENTS** — opcionális:
- üres → active
- `--proposed`
- `--retired`

**Tennivaló:**

1. Glob: `00_Prompts/BDOS/agents/presto/audience-learnings/<state>/*.md`
2. Olvasd a frontmattereket
3. Rendezd: confidence DESC, last_applied_at DESC (active) / proposed_at DESC (proposed)
4. Adj vissza emberi listát: slug, type, confidence, evidence-szám, last_applied_at + 1-2 mondat
5. Ha üres → "Nincs <state> audience-learning."
6. Proposed esetén: "Review: `/pres-learning-accept <slug>` vagy `/pres-learning-reject <slug>`"

Olvasás-only, NEM hív agent-et.
