---
description: Presto TEMPLATE mode — template lifecycle management (list, detect-candidates, promote, retire). Confirmation kell promote/retire-hoz.
id: 0b15e7f6-8b9d-0123-ef01-234567890123
index_schema_version: 1
---

A felhasználó Presto template módot kér — template lifecycle kezelés.

**$ARGUMENTS** — kötelező:
- `--op list|detect-candidates|promote|retire` — művelet típusa
- opcionális `--id <template-id>` — template azonosító (promote/retire-hoz)

**Tennivaló:**

1. Parse $ARGUMENTS, validáld az op paramétert
2. Hívd `subagent_type: presto`
3. Paraméterek: `mode: template`, `op`, `id`
4. Presto:
   - `list`: összes template státusz szerint (candidate/reusable/validated/canonical)
   - `detect-candidates`: publikációk scanelése recurring successful structures-re (≥3 pubs, engagement > 2x baseline)
   - `promote`: reusable → validated (≥7 uses + stable multiplier) VAGY validated → canonical (human only)
   - `retire`: template retired státuszra állítása reason-nel
5. **Confirmation** — `list`/`detect-candidates`-hez NEM kell; `promote`/`retire`-hoz KÖTELEZŐ

Lásd: `00_Prompts/BDOS/agents/presto.md` §6.17.
