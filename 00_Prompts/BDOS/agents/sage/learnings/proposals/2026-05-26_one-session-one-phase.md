---
schema: sage.learning.v1
slug: one-session-one-phase
type: failure-mode
status: proposed
confidence: medium
proposed_at: 2026-05-26T00:00:00+02:00
confirmed_at: null
last_applied_at: null
applications_count: 0
evidence:
  - "EP43 launch session 2026-05-26: ~6 órás session kevert substrate-evolúciót (per-Area DNA, runbook scaffold, schema v2, scheduling rule kanonizálás) + dashboard polish (3-tier visual, meta-prefix, calendar click, opacity, 4 panel removal, area+channel codes) + maga az EP43 launch (state-transitions, content review, manuális Spotify upload, FB post). Eredmény: high cognitive load, multiple agent restart, sub-agent bugok — reálisan 3 különböző session lett volna."
retired_at: null
retired_reason: null
retire_after_condition: "Ha 5 launch consecutively diszciplinált (egy session = egy phase)."
scope: "Marketing engine launch session-ök (Presto-driven publish-flow). Brand-spine sprint-ek. Bármely session ahol substrate-evolúció és operationális akció keveredik."
id: c3f6e054-1ab8-4d0f-b529-4f39b8c1d703
index_schema_version: 1
description: Meta-learning arról, hogy egy session NE keverjen substrate-evolúciót (schema-bővítés, runbook-create, DNA-írás) operacionális launch-folyamattal (state-transitions, publish-flow, content-review). A két aktivitás más kognitív módot igényel — keverve mindkettő minősége romlik, session-hossz és sub-agent hibák nőnek.
bdos_index: true
---

## A tanulság

**Egy session NE keverjen substrate-evolúciót (schema-bővítés, runbook-create, DNA-írás) operational-launch-folyamatba (state-transitions, publish-flow, content-review). A két aktivitás más kognitív módot igényel; keverve mindkettő minősége romlik.**

### 1. szabály — Schema/substrate freeze 24h launch előtt

Tervezett launch nap előtt **minimum 24 órával** lezárul minden schema- és substrate-módosítás. A launch nap munkamenetben csak operacionális akciók engedélyeztek:

- Engedélyezett: state-transition, content review, platform upload, post draft, pub-fájl frissítés.
- Tiltott: új schema mező, runbook scaffold, DNA fájl írás, dashboard strukturális változtatás, capability script módosítás.

Ha a launch napon mégis szükséges egy substrate-módosítás (kritikus bug, blocking issue): az agent expliciten jelzi, hogy "ez substrate-evolúció, nem operational akció — javasolt: gyors hotfix most, refactor post-launch".

### 2. szabály — Mid-launch felmerült ötletek Notes szekcióba mennek

Ha launch közben felmerül "ezt is jó lenne dokumentálni / kódolni" gondolat:

1. A gondolat **NEM kerül azonnal implementálásra** — ez megszakítja a launch-flow-t és növeli a cognitive load-ot.
2. A releváns pub-fájl `## Notes` szekciójába kerül egy sor: `TODO post-launch: <ötlet>`.
3. A post-launch retro session-ben (vagy következő curate-ban) dolgozza fel Sage.

Az agent erre aktívan figyelmeztet ha user menet közben substrate-módosítást kér: "Ez post-launch retro anyag — most Notes-ba teszem, nem implementálom."

## Mire vonatkozik

Presto-driven marketing engine launch session-ök (EP rendszeres launch: Navigátor Podcast, jövőben más contentek). Brand-spine sprint-ek szintén hasonló diszciplinát igényelnek. Bármely session ahol a user egyszerre akarja a "house in order" érzetet ÉS a launch-et elvégezni.

## Hogyan vonom vissza

Ha 5 egymást követő launch session diszciplinált (egy session = egy phase, <3 óra, <1 agent restart) → retire. Ha a pattern ismétlődik → escalate: session-típus pre-check legyen a Presto `plan` módban (javasolt session-fókusz explicitté tétele).

## Kapcsolódó

- `engine-pull-priority-over-ask-user-question` — párhuzamos tanulság: kognitív terhelés csökkentése az AskUserQuestion minimalizálásával.
- Presto runbook: launch day checklist — "D-1 substrate freeze" szabály beépítendő.
- Sage curate mód: post-launch retro a Notes szekció feldolgozásának természetes helye.
