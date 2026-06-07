---
schema: presto.audience-learnings.index.v1
generated_at: 2026-05-28
counts:
  active: 1
  proposed: 0
  retired: 0
description: Presto audience-learnings élő indexe — marketing-specifikus cross-project tanulságok (platform patterns, content performance, audience signals). Sage learnings/ mintára adaptálva. Presto `audience` és `learn` módjai frissítik.
id: 1cc93182-7f2d-48f7-b2f6-09c481584ebe
index_schema_version: 1
---

# Presto — Audience Learnings Index

Marketing-specifikus audience-learnings. Sage `learnings/` mintára adaptálva.

## Active (1)

| ID | Típus | Tanulság | Confidence | Applied |
|----|-------|----------|------------|---------|
| [`meta-reel-not-feedpost`](active/meta-reel-not-feedpost.md) | format-fit | Meta vertikális videót Reel-ként kell feltölteni (nem feed-poszt) + borítókocka + safe-zone — különben 4:5-re vág. Cross-project (FB+IG). | high | 2026-05-28 |

## Proposed (0)
*Üres — nincs pending javaslat.*

## Retired (0)
*Üres.*

---

## Cap
- Max **15 active learning**, max **2000 token** preamble (Sage konvenció)
- Sorrend: `confidence DESC, last_applied_at DESC`

## Lifecycle
```
proposed  ──/pres-learning-accept──>  active  ──unused 4 weeks──>  retired
   │                                    │
   │                                    └──contradicts new──>  retired (auto)
   │
   └──/pres-learning-reject──>  retired (reason kötelező)
```
