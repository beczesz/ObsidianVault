---
description: Presto TODO mode — operational inbox management (list, close, dismiss). Confirmation kell close/dismiss-hez.
id: fa04d6e5-7a8c-9012-def0-123456789012
index_schema_version: 1
---

A felhasználó Presto todo módot kér — TODO inbox kezelés.

**$ARGUMENTS** — kötelező:
- `--op list|close|dismiss` — művelet típusa
- opcionális `--id <todo-id>` — TODO azonosító (close/dismiss-hez)

**Tennivaló:**

1. Parse $ARGUMENTS, validáld az op paramétert
2. Hívd `subagent_type: presto`
3. Paraméterek: `mode: todo`, `op`, `id`
4. Presto:
   - `list`: összes nyitott TODO urgency szerint rendezve
   - `close`: done státuszra állít resolution_note-tal
   - `dismiss`: dismissed státuszra állít reason-nel
5. **Confirmation** — `list`-hez NEM kell; `close`/`dismiss`-hez KÖTELEZŐ

Lásd: `00_Prompts/BDOS/agents/presto.md` §6.19.
