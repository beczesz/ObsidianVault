---
description: Presto LEARNING REJECT — proposed → retired. Reason kötelező.
id: fc5c8491-7b57-4649-9fde-03e310e4d94b
index_schema_version: 1
---

A felhasználó audience-learning-proposal elutasítását kéri.

**$ARGUMENTS** — kötelező: slug + `--reason "..."`

**Tennivaló:**

1. Parse slug + reason
2. Ha reason hiányzik → error
3. Keresd `audience-learnings/proposals/<slug>.md`
4. Frontmatter: `status: retired`, `retired_at`, `retired_reason`
5. Mozgasd: `proposals/` → `retired/`
6. Update index

Nincs külön confirmation — reason-megadás már szándék-jel.
