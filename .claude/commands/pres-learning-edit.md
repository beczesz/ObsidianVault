---
description: Presto LEARNING EDIT — aktív audience-learning szövegének módosítása. Confirmation kötelező.
id: 0dd31c54-ee2a-451f-a065-6473b0f616f6
index_schema_version: 1
---

A felhasználó aktív audience-learning editálását kéri.

**$ARGUMENTS** — kötelező: slug

**Tennivaló:**

1. Keresd `audience-learnings/active/<slug>.md`
2. Olvasd be a teljes tartalmat
3. Hívd `subagent_type: presto`, mode: `learn`, op: `edit`
4. Presto javasol diffet, NEM ír
5. **Confirmation kötelező**
6. Csak akkor írj
7. Frontmatter: `note_revision++` vagy `last_edited_at`
