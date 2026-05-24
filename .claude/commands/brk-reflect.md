---
description: Broker REFLECT mode — heti/havi sales strategic reflection. NEM optimization theater. Megerősítés nélkül (info-with-recommendations).
id: 000bd52e-e649-45e8-8fae-7606185ac66f
index_schema_version: 1
---

A felhasználó Broker strategic reflection-t kér.

**$ARGUMENTS** — opcionális: `--period weekly|monthly`, `--area <name>`.

**Tennivaló:**

1. Hívd `subagent_type: broker`, mode: `reflect`
2. Broker olvas: `Cohorts/*/COHORT.md` iteration history, `Results-*.md`, `sales-learnings/active/`
3. Identifikál stabil mintákat (NEM egyetlen outlier)
4. Max 3 strategic javaslat (severity + evidence + reversible: true)
5. Output mentés: `02_Areas/<area>/Sales/reflections/<YYYY-Www>.md` vagy `agents/broker/reflections/<YYYY-Www>.md`

**Anti-pattern:** ne futtass többet hetente. NE optimization theater.
