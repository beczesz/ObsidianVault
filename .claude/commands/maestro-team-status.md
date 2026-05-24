---
description: Maestro TEAM-STATUS mode — meta-riport az agent-családról. Hány agent LIVE, mikor frissültek utoljára, canonical↔registration sync, slash-command-szám.
id: a4c05e62-5e71-4e86-a5af-19f76fe5ace0
index_schema_version: 1
---

A felhasználó az agent-csapat státuszát kéri.

**$ARGUMENTS** — opcionális. Példák:
- (üres) → minden agent
- `--agent=curator` → csak egy agent
- `--stale` → csak a > 90 napja nem frissítetteket

**Tennivaló:**

1. Parsold az `--agent=` és `--stale` paramétereket.
2. Hívd meg a Maestro-t **`subagent_type: maestro`** **team-status módban**:
   - Olvas: `00_Prompts/BDOS/00_AGENTS_INDEX.md` + minden `00_Prompts/BDOS/agents/*.md` frontmatter + `.claude/agents/*.md` frontmatter
   - Számolja: `.claude/commands/<prefix>-*.md` darabszámot agentenként
3. Output: tábla — agent × verzió × status × last_updated × modes × slash_commands × sync_OK.
4. Confirmation NEM kell (info-mód).

**Kontextus-védelem:** a tábla az output. Ne ismételd prózában, csak rövid összefoglalót adj (pl. „4 agent LIVE, mind sync-ben, 1 stale").
