---
description: Presto LEARNING RETIRE — active audience-learning visszavonása manuálisan. Confirmation kötelező.
id: affbd227-e41d-4bd2-b6b9-290bfcda811d
index_schema_version: 1
---

A felhasználó aktív audience-learning visszavonását kéri.

**$ARGUMENTS** — kötelező: slug + opcionális `--reason "..."`

**Tennivaló:**

1. Parse slug + reason (opcionális, default "manual_retire")
2. Keresd `audience-learnings/active/<slug>.md`
3. Mutasd a tartalmát + kérdezz: "Visszavonod?"
4. Confirmation után: frontmatter `retired_*`, mozgatás `active/` → `retired/`, index update
