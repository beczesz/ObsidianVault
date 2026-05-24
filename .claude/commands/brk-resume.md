---
description: Broker RESUME mode — stalled lead reaktiválása, follow-up draft. Confirmation kötelező.
id: 450ea957-b460-42c8-b056-a707de2ba2d4
index_schema_version: 1
---

A felhasználó stalled lead reaktiválást kér.

**$ARGUMENTS** — kötelező: `--lead <area/cohort/lead-id>`.

**Tennivaló:**

1. Hívd `subagent_type: broker`, mode: `resume`
2. Broker read-context (lead history, last touch, stall reason)
3. **Confirmation KÖTELEZŐ**
4. Follow-up draft generálás

**Megjegyzés:** ha lead > 30 napos és nincs friss signal, Broker relevancia-gate-en megy át — javasolhatja a lead retire-ját helyett.
