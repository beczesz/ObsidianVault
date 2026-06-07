---
description: Presto INSIGHT mode — insight lifecycle management (list, approve, operationalize, retire). Confirmation kell action módhoz.
id: 1c26f8a7-9c0e-1234-f012-345678901234
index_schema_version: 1
---

A felhasználó Presto insight módot kér — insight lifecycle kezelés.

**$ARGUMENTS** — kötelező:
- `--op list|approve|operationalize|retire` — művelet típusa
- opcionális `--id <insight-id>` — insight azonosító (approve/operationalize/retire-hoz)

**Tennivaló:**

1. Parse $ARGUMENTS, validáld az op paramétert
2. Hívd `subagent_type: presto`
3. Paraméterek: `mode: insight`, `op`, `id`
4. Presto:
   - `list`: összes insight státusz szerint (candidate/approved/operational/retired)
   - `approve`: candidate → approved (requires sample_size ≥ 3, evidence_strength ≥ medium)
   - `operationalize`: approved insight alkalmazása channel DNA-ra vagy campaign defaults-ra
   - `retire`: insight retired státuszra állítása reason-nel
5. **Confirmation** — `list`-hez NEM kell; `approve`/`operationalize`/`retire`-hoz KÖTELEZŐ

Lásd: `00_Prompts/BDOS/agents/presto.md` §6.16.
