---
description: Maestro REFLECT mode — mélyebb minta-analízis a logokon, JAVASLATOKAT generál (NEM hajt végre). Megerősítés nélkül (info+recommendations).
id: c029c2fd-c6b5-4ab4-a4f1-bf5fa8a76c94
index_schema_version: 1
---

A felhasználó Maestro reflect módot kér — pattern-recognition + recommendations.

**$ARGUMENTS** — opcionális:
- üres → minden minta-típus
- `--focus token-efficiency|workflow-bottlenecks|prompt-drift|collaboration|systemic-risk` → szűrés

**Tennivaló:**

1. Hívd `subagent_type: maestro`
2. Paraméterek:
   - `mode: reflect`
   - opcionális: `focus`
3. Maestro olvassa az aggregált logokat (mint observe), keres mintákat:
   - duplicated reasoning, token graveyards, inefficient workflows
   - orchestration bottlenecks, unstable agents, repeated retries
   - collaboration failures, prompt drift, systemic inefficiencies
4. Generál javaslat-táblát: severity (low/medium/high) + agents affected + suggested action + expected impact + related learnings

**FONTOS:** ez a mód CSAK javasol. Nem futtat semmit. Az `optimize` mód feladata egy konkrét javaslat végrehajtása.

Megerősítés NEM kell.

Lásd: `00_Prompts/BDOS/CONSTITUTION_PHASE_2.md` + `00_Prompts/BDOS/agents/maestro.md` §4.C.2.
