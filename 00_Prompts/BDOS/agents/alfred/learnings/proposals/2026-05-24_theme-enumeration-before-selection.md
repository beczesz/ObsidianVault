---
description: "Mandatory enumeration of all candidate themes before selection in Sage harvest; primary thematic focus is often implicit in chat structure, not literal keywords. Decision trace with justification now required in operational logs."
description_source: auto
description_hash: ee27b33554e7aa4e
schema: sage.learning.v1
slug: theme-enumeration-before-selection
type: prompt-weakness
status: proposed
confidence: high
proposed_at: 2026-05-24T16:00:00+02:00
confirmed_at: null
last_applied_at: null
applications_count: 0
evidence:
  - "2026-05-24 smoke test v1: Sage extracted 'editorial taste modeling' (valid but secondary side-thread) instead of 'middle management layer disappearance + BDOS' (primary central thread). User had to correct."
  - "Root cause: Sage scanned for 'new' themes among the chat's user-input, but did not enumerate ALL candidate themes with primary-focus-ranking before selecting."
  - "Implicit themes (those that emerge from chat's structural conclusion, not literal keywords) were missed entirely — the chat's closing AI/human function-split IS a middle-management-disappearance argument structurally, but never names it that way."
retired_at: null
retired_reason: null
id: eb7121d3-e5a9-405c-9717-9e8dae014f24
index_schema_version: 1
---
## A tanulság

Sage harvest-során **kötelező enumerálni MINDEN candidate témát** a chatben mielőtt választ. Egy "új-de-mellékes" téma soha nem ér többet egy "primary-de-részben-fedett" témánál.

A literal keyword-matching félrevezet — a primary thematic focus gyakran IMPLICIT a chat strukturális zárásában (pl. egy felsorolás, ami valójában argumentum), nem szó szerinti megnevezésben.

## Hatás a Sage-re

`daily_harvest.md` prompt frissítve (v1.1):
- Új `§3.c.1 Decision trace — KÖTELEZŐ` szekció
- Minimum 3 candidate téma enumerálása
- Mindegyiknél `is_primary_focus` + `is_new` + `atomic_readiness` jelölés
- Selected téma justification kötelező
- Teljes `decision_trace` az operational log-ban (schema `bdos.operational.log.v1.1`)

## Hogyan vonom vissza

Ha 4 héten belül egy user-correction esemény ismét bekövetkezik AZONOS okkal (primary focus missed) → ez a learning **NEM működik**, vissza kell vonni és új mechanizmus kell.

Ha 4 hét után 0 user-correction event (vagy van, de más okból) → confirmed.

## Cross-link

- Sage operational log entry: `sage-harvest-2026-05-24-smoke-test-corrected` — első futás amelyik logolja a `decision_trace`-t
- Archived files: `Ideas/_archive/thoughts_replaced/` — audit trail a hibára
