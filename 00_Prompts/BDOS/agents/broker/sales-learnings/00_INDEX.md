---
schema: broker.sales-learnings.index.v1
generated_at: null
counts:
  active: 0
  proposed: 0
  retired: 0
description: Broker sales-learnings élő indexe — sales-specifikus cross-project tanulságok (8 típus: objection-pattern, cycle-timing, cohort-signal, outreach-tone, qualification-criteria, competitor-context, loss-pattern, referral-mechanic). Broker `learn` módja frissíti.
id: 5c5b3863-2f40-44a7-b031-1e7c4417ba8f
index_schema_version: 1
---

# Broker — Sales Learnings Index

Sales-specifikus learnings. Presto `audience-learnings` mintára adaptálva.

## Active (0)
*Üres — Broker v0.2 design just done, nincsenek confirmed sales-learnings.*

## Proposed (0)
## Retired (0)

---

## Cap
- Max **15 active learning**, max **2000 token** preamble
- Sorrend: `confidence DESC, last_applied_at DESC`

## 8 sales-learning típus
- `objection-pattern` — milyen kifogásokra mi a jó válasz
- `cycle-timing` — mikor zárul leggyorsabban egy deal-típus
- `cohort-signal` — cohort-ban mi prediktálja a konverziót
- `outreach-tone` — persona-szerinti tone-preference
- `qualification-criteria` — kit érdemes kvalifikálni
- `competitor-context` — versenytárs-mintázatok
- `loss-pattern` — miért veszítünk
- `referral-mechanic` — referral-flow
