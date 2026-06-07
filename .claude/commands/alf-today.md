---
description: Alfred TODAY / briefing — napi read-only briefing: lejárt + mai + soon taskok, naptár-remindek, prioritások. Megerősítés nélkül fut.
id: a1f10003-0000-4c00-8000-000000000003
index_schema_version: 1
---

A felhasználó Alfred napi briefinget kér — mi van ma, mit kell mozdítani.

**$ARGUMENTS** — opcionális: `--date YYYY-MM-DD` (default: ma).

**Tennivaló:**

1. Parsold a dátumot (default: mai nap).
2. Olvasd az összes `02_Areas/Personal Growth/Alfred/todos/<scope>.md` fájlt.
3. Szűrd: **lejárt** (due < ma) + **mai** (due = ma) + **soon** (due <= ma+3 nap) taskok nyitott checkboxok.
4. Olvasd `02_Areas/Personal Growth/Alfred/priorities.md` — személyes/családi prioritások.
5. Olvasd `agents/alfred/state/last_run.md` — utolsó sync/harvest összefoglaló.
6. Output kötelező szekciók:
   - **Lejárt / sürgős** (ha van)
   - **Ma esedékes**
   - **Hamarosan (3 napon belül)**
   - **Aktuális prioritások** (priorities.md-ből)
   - **Rendszer státusz** (utolsó sync/harvest ideje)

**Read-only** — nem módosít semmit. Confirmation nem kell.

Lásd: `00_Prompts/BDOS/agents/alfred.md` §4 `today`/`briefing` mód.
