---
description: Alfred LEARNINGS — active/proposed/retired Alfred-learningek listája. Default: active. Megerősítés nélkül fut.
id: a1f10013-0000-4c00-8000-000000000013
index_schema_version: 1
---

A felhasználó Alfred learning-listát kér.

**$ARGUMENTS** — opcionális: üres → active, `--proposed`, `--retired`.

**Tennivaló:**

1. Parsold az opcionális flag-et (default: `active`).
2. Glob: `agents/alfred/learnings/<state>/*.md` (state = `active` | `proposals` | `retired`).
3. Olvasd a frontmattereket: title / slug / type / confidence / evidence-szám / 1-2 mondat description.
4. Rendezd: confidence DESC (active), created_at DESC (proposals), retired_at DESC (retired).
5. Output lista: slug + type + confidence + evidence-szám + rövid leírás.
6. Ha active > 12: figyelmeztess ("Cap közeledik — 15 az active limit").
7. Ha proposals > 0 és active nézet: "Van X pending proposal — `/alf-learning-accept <slug>` a következő lépés."

**Read-only** — nem módosít semmit.

Lásd: `00_Prompts/BDOS/agents/alfred.md` §4 `learn` mód + `agents/alfred/learnings/` struktúra.
