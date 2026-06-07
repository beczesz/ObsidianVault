---
description: Presto CHANNEL mode — Channel DNA management (list, view, update-tone). Confirmation kell edit-hez.
id: e9a3c5d4-6f7b-8901-cdef-012345678901
index_schema_version: 1
---

A felhasználó Presto channel módot kér — Channel DNA kezelés.

**$ARGUMENTS** — kötelező:
- `--op list|view|update-tone` — művelet típusa
- opcionális `--channel <slug>` — channel azonosító (view/update-tone-hoz)
- opcionális `--area <name>` — Area szűrés (update-tone-hoz)

**Tennivaló:**

1. Parse $ARGUMENTS, validáld az op paramétert
2. Hívd `subagent_type: presto`
3. Paraméterek: `mode: channel`, `op`, `channel`, `area`
4. Presto:
   - `list`: összes channel status + capabilities táblázat
   - `view`: egy channel teljes CHANNEL_DNA.md tartalma
   - `update-tone`: per-Area tone_overrides módosítása
5. **Confirmation** — `list`/`view`-hoz NEM kell; `update-tone`-hoz KÖTELEZŐ

Lásd: `00_Prompts/BDOS/agents/presto.md` §6.18.
