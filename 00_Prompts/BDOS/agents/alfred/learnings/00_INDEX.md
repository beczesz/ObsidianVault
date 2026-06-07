---
schema: alfred.learnings.index.v1
generated_at: 2026-05-28
counts:
  active: 0
  proposed: 6
  retired: 0
description: Alfred meta-kognicíós learnings élő indexe. Tartalmazza a Sage-tol migralt 6 proposalt (2026-05-28 Sage-Alfred merge). User-reviewable, retirable tanulságok a harvest/curate/chat/learn módokhoz. Heti curate (Alfred) frissiti.
id: 7e2a1b4c-9d3f-4e8a-b2c1-6f5d7e9a0c3b
index_schema_version: 1
---

# Alfred — Learnings Index

Alfred meta-kognicíós tanulságainak élő indexe. Ezek a learningek Alfred harvest, curate, chat és learn módjaira vonatkoznak.

> **2026-05-28 migrációs megjegyzés:** Ez az index a Sage-Alfred merge részeként jött létre. A 6 proposed learning átkerült ide a `00_Prompts/BDOS/agents/sage/learnings/proposals/` mappábol — azok az ott felhalmozódott meta-learningek, amelyek a harvest/curate/chat ciklusok tanulságait tartalmazzák. A source-of-truth mostantól Alfred itt.

## Active (0)

*Üres — nincsenek confirmed learningek még.*

## Proposed (6) — migrálva Sage-tol 2026-05-28

- [`proposals/2026-05-24_theme-enumeration-before-selection.md`](proposals/2026-05-24_theme-enumeration-before-selection.md) — `prompt-weakness` / high — Harvest-kor kötelező enumerálni MINDEN candidate témát kiválasztás elott
- [`proposals/2026-05-26_capability-script-restart-and-smoke-test.md`](proposals/2026-05-26_capability-script-restart-and-smoke-test.md) — `failure-mode` / high — Python daemon módosítás után kötelező restart + smoke-test
- [`proposals/2026-05-26_engine-pull-priority-over-ask-user-question.md`](proposals/2026-05-26_engine-pull-priority-over-ask-user-question.md) — `failure-mode` / medium — State-alapú next-action ajánlás, nem AskUserQuestion
- [`proposals/2026-05-26_one-session-one-phase.md`](proposals/2026-05-26_one-session-one-phase.md) — `failure-mode` / medium — Substrate-evolúció és operational launch keverése tilos egy sessionben
- [`proposals/2026-05-26_sub-agent-output-smoke-test.md`](proposals/2026-05-26_sub-agent-output-smoke-test.md) — `failure-mode` / medium — Parent agent kötelezoen ellenorzi sub-agent outputját
- [`proposals/2026-05-26_verify-before-trust-after-publish.md`](proposals/2026-05-26_verify-before-trust-after-publish.md) — `failure-mode` / medium — Publish akció után kötelező Chrome MCP read-back verifikáció

## Retired (0)

*Üres — még semmit sem archiváltunk.*

---

## Hogyan él egy learning

```
proposed  ──/alf-learning-accept──>  active  ──unused 4 weeks──>  retired
   |                                    |
   |                                    +──contradicts new──>  retired (auto)
   |
   +──/alf-learning-reject──>  retired (with reason)
```

## Learning fájlok helye

- Active: [`active/`](active/) — bekerül a következo Alfred-futás promptjába
- Proposed: [`proposals/`](proposals/) — user-review vár
- Retired: [`retired/`](retired/) — archive, audit miatt megorizve

## Cap

- Max **15 active learning** loadolódik egyidejuleg
- Max **2000 token** preamble méret
- Sorrend: `confidence DESC, last_applied_at DESC`
