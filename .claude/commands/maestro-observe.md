---
description: Maestro OBSERVE mode — aggregálja a 3 family log-streamet (Operational/Learning/Version) és strukturált operacionális riportot generál. Megerősítés nélkül (read-only).
id: 9b2d8d6f-1906-4267-9a11-f96f0d11433d
index_schema_version: 1
---

A felhasználó Maestro observe módot kér — a BDOS organizational observability layer-je.

**$ARGUMENTS** — opcionális:
- üres → utolsó 7 nap, minden agent, minden stream
- `--since YYYY-MM-DD` → ettől az időponttól
- `--agent <name>` → szűrés egy agentre
- `--streams operational,learning,version` → szűrés streamekre

**Tennivaló:**

1. Hívd `subagent_type: maestro`
2. Paraméterek:
   - `mode: observe`
   - opcionális: `since`, `agent`, `streams`
3. Maestro olvassa: `00_Prompts/BDOS/agents/*/logs/<stream>/*.md` glob, parse-olja a YAML-blokkokat, aggregálja
4. **Phase 2.B előtt:** degraded mód — Sage `_journal/` aliasát is használja, többi agentnél placeholder

**Output:** strukturált riport (Activity / Learnings / Evolution / Health Indicators), max 400 szó.

Megerősítés NEM kell. Read-only mód.

Lásd: `00_Prompts/BDOS/CONSTITUTION_PHASE_2.md` + `00_Prompts/BDOS/LOG_SCHEMAS.md` + `00_Prompts/BDOS/agents/maestro.md` §4.C.1.
