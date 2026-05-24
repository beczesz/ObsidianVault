---
description: Broker LEARNING REJECT — proposed → retired. Reason kötelező.
id: 54778086-79f9-4618-b352-0ddb23b60e02
index_schema_version: 1
---

A felhasználó sales-learning-proposal elutasítását kéri.

**$ARGUMENTS** — kötelező: slug + `--reason "..."`.

**Tennivaló:**

1. Parse slug + reason
2. Ha reason hiányzik → error
3. Keresd `proposals/<slug>.md`
4. Frontmatter `retired_*`, mozgatás `proposals/` → `retired/`, index update
