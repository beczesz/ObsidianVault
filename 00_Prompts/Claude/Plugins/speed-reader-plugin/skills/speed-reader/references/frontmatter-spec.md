---
title: "YAML Front-Matter Specification"
date: 2026-04-21
author: Becze Szabolcs
status: active
description: "Mandatory YAML metadata structure for Speed-Reading Agent markdown notes, specifying required fields like title, type, author, tags, and status to enable Obsidian dataview queries and vault organization. Includes field definitions, conditional requirements, and type-specific examples."
description_source: auto
description_hash: 7a1e0bf6a9c76154
id: b7b698b8-8e52-4e56-b269-41d5005fc10f
index_schema_version: 1
bdos_index: true
---
# YAML Front-Matter Specification

Every Markdown note produced by the Speed-Reading Agent **must** begin with a YAML front-matter block. This ensures consistent metadata for Obsidian Dataview queries, graph views, and vault-wide search.

---

## Full Field Reference

```yaml
---
title: "Full Title"
type: book | podcast | article | atomic | contrast
author: "Name(s)"
year: 2025
source_url: "https://..."
file_refs: ["filename.pdf"]
tags: ["book", "summary", "philosophy"]
status: "triaged"
confidence: "high"
created: "YYYY-MM-DD"
processed_by: "AI Speed-Reading Agent"
---
```

---

## Field Definitions

| Field | Required | Type | Notes |
|-------|----------|------|-------|
| `title` | **Yes** | string | Full title of the work. Wrap in quotes. |
| `type` | **Yes** | enum | One of: `book`, `podcast`, `article`, `atomic`, `contrast` |
| `author` | Conditional | string | Author name(s). **Omit** for contrast notes if N/A. |
| `year` | Conditional | integer | Publication year. **Omit** if unknown. |
| `source_url` | Conditional | string | URL if applicable (web article, podcast page, etc.). |
| `file_refs` | Conditional | list | Filenames of attached source files (PDF, ePub). Omit if none. |
| `tags` | **Yes** | list | 5–10 descriptive tags. Always include the `type` as first tag. |
| `status` | **Yes** | enum | One of: `triaged` (initial pass), `deep-read` (thorough analysis done), `in-progress` (partially complete). Default to `triaged` for title-only, `deep-read` for full-text. |
| `confidence` | **Yes** | enum | `high` — full text was available. `medium` — reliable secondary sources used. `low` — limited or conflicting information. |
| `created` | **Yes** | date | ISO date string `YYYY-MM-DD` of when the note was generated. |
| `processed_by` | **Yes** | string | Always `"AI Speed-Reading Agent"`. |

---

## Examples by Type

### Book (full text available)
```yaml
---
title: "Influence: The Psychology of Persuasion"
type: book
author: "Robert B. Cialdini"
year: 1984
file_refs: ["Influence_Robert_B_Cialdini.pdf"]
tags: ["book", "summary", "psychology", "persuasion", "behavioral-science"]
status: "deep-read"
confidence: "high"
created: "2025-05-20"
processed_by: "AI Speed-Reading Agent"
---
```

### Podcast
```yaml
---
title: "Sleep Toolkit: Tools for Optimizing Sleep"
type: podcast
author: "Andrew Huberman"
year: 2023
source_url: "https://hubermanlab.com/sleep-toolkit"
tags: ["podcast", "summary", "neuroscience", "sleep", "health"]
status: "deep-read"
confidence: "high"
created: "2025-05-20"
processed_by: "AI Speed-Reading Agent"
---
```

### Article (title-only, web-researched)
```yaml
---
title: "Leading Change: Why Transformation Efforts Fail"
type: article
author: "John P. Kotter"
year: 1995
source_url: "https://hbr.org/1995/05/leading-change-why-transformation-efforts-fail-2"
tags: ["article", "summary", "leadership", "change-management", "business"]
status: "triaged"
confidence: "medium"
created: "2025-05-20"
processed_by: "AI Speed-Reading Agent"
---
```

### Atomic Idea
```yaml
---
title: "Scarcity Mindset"
type: atomic
tags: ["atomic", "psychology", "behavioral-economics", "decision-making"]
status: "triaged"
confidence: "high"
created: "2025-05-20"
processed_by: "AI Speed-Reading Agent"
---
```

### Contrast Note
```yaml
---
title: "Peterson vs Dostoevsky on Suffering"
type: contrast
tags: ["contrast", "philosophy", "suffering", "existentialism", "psychology"]
status: "triaged"
confidence: "medium"
created: "2025-05-20"
processed_by: "AI Speed-Reading Agent"
---
```
