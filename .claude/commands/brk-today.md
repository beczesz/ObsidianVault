---
description: Broker TODAY mode — mai napi sales action queue, lead-szinten. Megerősítés nélkül.
id: 04c2238d-e35d-4160-9105-d202aee4ec25
index_schema_version: 1
---

A felhasználó Broker mai napi action queue-t kér — kit kell ma megkeresni.

**$ARGUMENTS** — opcionális `--date YYYY-MM-DD` (default: ma).

**Tennivaló:**

1. Hívd `subagent_type: broker`, mode: `today`
2. Broker olvas: minden Area `Sales/Pipeline.md` + aktív `COHORT.md`-k
3. Output: lead-szintű priorizált lista — kit hívni / emailezni / follow-up-olni, milyen kontextussal

Lásd: `00_Prompts/BDOS/agents/broker.md` §4.2.
