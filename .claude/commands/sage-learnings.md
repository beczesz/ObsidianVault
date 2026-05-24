---
description: Sage LEARNINGS — active vagy proposed learnings listája emberi formában. Default: active. `--proposed` flag = pending javaslatok.
id: bf33cee3-bf83-421a-97cb-943f03540b37
index_schema_version: 1
---

A felhasználó Sage tanulság-listát kér.

**$ARGUMENTS** — opcionális:
- üres → active learnings
- `--proposed` → pending javaslatok review-hoz
- `--retired` → archived (csak audit)

**Tennivaló:**

1. Glob: `00_Prompts/BDOS/agents/sage/learnings/<active|proposals|retired>/*.md`
2. Olvasd be a frontmattereket
3. Rendezd: `confidence DESC, last_applied_at DESC` (active) vagy `proposed_at DESC` (proposed)
4. Adj vissza emberi listát:
   - slug, type, confidence, evidence-szám, last_applied_at
   - 1-2 mondatos "A tanulság" body-ból
5. Ha üres → mondd ki: "Nincs <state> learning."
6. Proposed esetén: emlékeztess: "Review: `/sage-learning-accept <slug>` vagy `/sage-learning-reject <slug>`"

Olvasás-only, NEM hív Sage agentet.
