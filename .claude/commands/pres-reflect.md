---
description: Presto REFLECT mode — heti/havi strategic reflection. NEM optimization theater. Csak stabil mintákra reagál. Megerősítés nélkül (info-with-recommendations).
id: c5717ffa-de4d-44de-85ec-28792532c7a3
index_schema_version: 1
---

A felhasználó Presto reflect módot kér — strategic reflection a marketing performance-on.

**$ARGUMENTS** — opcionális:
- `--period weekly|monthly` (default: weekly)
- `--area <name>` szűkítés

**Tennivaló:**

1. Hívd `subagent_type: presto`
2. Paraméterek: `mode: reflect`, `period`, `area`
3. Presto:
   - Olvassa elmúlt időszak `Results-*.md` riportjait
   - Olvassa `audience-learnings/active/*.md`-t
   - Identifikál stabil mintákat (NEM egyetlen outlier)
   - **Auto-hívható** a Thinking Engine Orchestrator ha trend-validáció kell (logoltan)
   - Max 3 stratégiai javaslat (severity + evidence + reversible: true)
   - Új audience-learning-jelölteket `audience-learnings/proposals/`-be
4. Output mentés: `02_Areas/<area>/Marketing/reflections/<YYYY-Www>.md` vagy `agents/presto/reflections/<YYYY-Www>.md`

**Anti-pattern:** ne futtass több mint hetente. NE optimization theater.

Megerősítés NEM kell (info+recommendations only).

Lásd: `00_Prompts/BDOS/agents/presto.md` §6.9.
