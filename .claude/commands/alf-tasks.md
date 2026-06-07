---
description: Alfred TASKS — nyitott taskok read-only lekérdezése, scope-szűrve és due szerint rendezve. Megerősítés nélkül fut.
id: a1f10008-0000-4c00-8000-000000000008
index_schema_version: 1
---

A felhasználó a nyitott task-okat kéri le.

**$ARGUMENTS** — opcionális:
- `[scope]` — szűrés adott scope-ra (pl. `personal`, `family`, `navigator`)
- `--due` — csak a due dátummal rendelkező taskok, due szerint rendezve
- `--overdue` — csak a lejárt taskok (due < ma)

Példák:
- (üres) → minden scope összes nyitott taskja
- `navigator` → csak a navigator scope
- `--overdue` → minden lejárt task
- `family --due` → family scope, due szerint rendezve

**Tennivaló:**

1. Parsold scope-szűrőt és flag-eket.
2. Glob: `02_Areas/Personal Growth/Alfred/todos/<scope>.md` (vagy az összes ha nincs scope-szűro).
3. Parse-old a `- [ ]` sorokat minden fájlból.
4. Szűrd/rendezd a flag-ek szerint.
5. Output tábla: scope | feladat | prioritás | due | napok-száma-lejáratig.
6. Ha overdue taskok vannak, emeld ki.

**Read-only** — nem módosít semmit. Confirmation nem kell.

Lásd: `00_Prompts/BDOS/agents/alfred.md` §4 `tasks` mód + §5a TODO store.
