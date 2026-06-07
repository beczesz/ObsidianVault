---
schema: sage.learning.v1
slug: engine-pull-priority-over-ask-user-question
type: failure-mode
status: proposed
confidence: medium
proposed_at: 2026-05-26T00:00:00+02:00
confirmed_at: null
last_applied_at: null
applications_count: 0
evidence:
  - "EP43 launch session 2026-05-26: 40+ AskUserQuestion a session során. Sok kérdés ('mit szeretnél most?', 'folytatjuk vagy várjunk?', 'auto vagy manuális?') a state-ből triviálisan kiszámítható lett volna. Decision fatigue: a user a 4. órára észrevehetően lassabban válaszolt. Az engine-pull pattern (Broker mintára) elveihez NEM hű volt a megvalósítás."
retired_at: null
retired_reason: null
retire_after_condition: "Ha 5 session consecutively az AskUserQuestion-count átlag <10/session (jelenlegi ~40/session-ről)."
scope: "Minden engine-pull pattern-t használó agent (Presto, Broker, Maestro). NEM scope: kreatív tartalom-döntések (content-direction, voice-tone, hook-pick) ahol valódi user-preference kell."
id: d4a7f165-2bc9-4e10-c640-5f4a9d2e814
index_schema_version: 1
description: Meta-learning arról, hogy state-machine + runbook + jelenlegi pipeline-állapot által egyértelműen meghatározott next-action esetén az agent NE AskUserQuestion-nel kérjen döntést, hanem konkrét next-action-suggestion-t adjon és confirm-ot kérjen (igen/nem). Decision fatigue csökkentése: az EP43 session-ben ~40 kérdés volt, ahol a legtöbb state-alapból kiszámítható lett volna.
bdos_index: true
---

## A tanulság

**Amikor a state machine + runbook + jelenlegi pipeline-állapot egyértelmű next-action-t ad, a parent agent NE használjon AskUserQuestion-t binary "mit szeretnél most?" döntéssel. Adj konkrét next-action-suggestion-t a state-alapján, és KÉRJ confirm-ot (igen/nem), NE menü-választást.**

### 1. szabály — AskUserQuestion csak valódi döntési szituációban

AskUserQuestion CSAK akkor jogos, ha az alábbi feltételek egyike teljesül:

- **(a) State-alapból NEM számítható ki válasz** — hiányzó adat, ambiguous spec, conflicting rules.
- **(b) Valós alternatívák versengő trade-off-fal** — 2-3 opció van, mindegyiknek van értelmes érve, nincs egyértelmű "helyes" irány.

Nem jogos AskUserQuestion:
- "Mit szeretnél most?" — ha a runbook következő lépése egyértelmű.
- "Folytatjuk vagy várjunk?" — ha a state `prepared + approved`, az action `scheduled`.
- "Auto vagy manuális?" — ha a pipeline-config egyértelmű default-ot ad.

### 2. szabály — State-alapú determinisztikus next-action: action + utólagos riport

Ha a next-action state-alapból egyértelmű (pl. `prepared + approved → scheduled`, `publish_time elmúlt → published`, `draft + no_blockers → ready_for_review`):

1. Az agent **azonnal végrehajtja** az akciót (vagy javaslatot tesz egy mondatban + confirm kér: "Következő lépés: X — rendben?").
2. Az akció után **egy mondatos riport**: "EP43 state: scheduled → published. YT link: [URL]."
3. NEM nyit fel döntési menüt: "Szeretnéd hogy (a) ezt, (b) azt, (c) amazt?"

**Cél:** a user fókuszát a valódi döntésekre irányítani (kreatív tartalom, priority-call, resource allokáció), nem triviális state-transition confirmálásokra.

## Mire vonatkozik

Presto (publish-flow, state-machine transitions), Broker (pipeline step execution, follow-up timing), Maestro (brand-spine projekt-navigáció, next-milestone). NEM vonatkozik: kreatív tartalom-döntések ahol valódi user-preference kell (hook-pick, voice-tone, CTA szöveg, képválasztás).

## Hogyan vonom vissza

Ha 5 egymást követő session AskUserQuestion-count átlag <10/session → retire (decision fatigue eliminated). Ha az átlag nem csökken → escalate: Presto runbook state-transition lépéseibe "auto-execute unless blocked" flag beépítendő.

## Kapcsolódó

- `one-session-one-phase` — párhuzamos tanulság: ugyanazt a session-terhelést okozza a kérdés-árasztás és a fáziskeverés.
- Broker engine-pull pattern — kanonikus referencia arra, hogyan kell state-alapú determinisztikus akciót végrehajtani kérdés nélkül.
- Presto state-machine spec: state transition rules — ezekből következik, mikor nem kell kérdezni.
