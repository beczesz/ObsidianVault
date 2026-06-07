---
description: Alfred HARVEST — idea-harvest a ChatGPT "Referencia chat"-ból Chrome MCP-vel. Strukturált thought-note-ok az Ideas/ mappába. Csend default, csak hiba vagy 3+ thought esetén notify.
id: a1f10009-0000-4c00-8000-000000000009
index_schema_version: 1
---

A felhasználó Alfred idea-harvest-et kér — az ötlet-csatorna (ChatGPT "Referencia chat") feldolgozása.

**$ARGUMENTS** — opcionális: `--dry-run` (ír helyett csak listázza mit találna).

**Tennivaló:**

1. Olvasd `agents/alfred/state/last_seen.md` — melyik az utolsó már feldolgozott üzenet.
2. Chrome MCP-vel olvasd a ChatGPT "Referencia chat" chat-et: csak a `last_seen`-nél újabb üzenetek.
3. Minden új referencia-üzenetből generálj strukturált thought-note-ot:
   - Cél: `02_Areas/Personal Growth/Ideas/thoughts/<YYYY-MM-DD>_<slug>.md`
   - Frontmatter: title, date, source, description (1-2 mondat tartalom-driven), tags
4. Ha atomi gondolat-javaslat detektálható → írj `Ideas/_inbox/atomic_proposals/` mappába is.
5. Ha `--dry-run`: csak listázd a tervezett fájlokat, ne írj.
6. Confirmation nélkül fut (csend default, automated-friendly mód).
7. Frissítsd `agents/alfred/state/last_seen.md` + `agents/alfred/state/last_run.md`.
8. Notify: csak ha 3+ thought készült, uncertain inbox, vagy hiba.

**Tools:** Chrome MCP, Read, Write, Edit, Glob.

Lásd: `00_Prompts/BDOS/agents/alfred.md` §4 `harvest` mód (v0.3 kognitív, Sage-merged).
