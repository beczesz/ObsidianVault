---
title: "Output Templates"
date: 2026-04-21
author: Becze Szabolcs
status: active
description: "A standardized collection of markdown templates for capturing book summaries, podcasts, articles, atomic ideas, and contrast notes using the PARA framework. Includes placeholders, required sections, and file organization guidelines for building a structured personal knowledge base."
description_source: auto
description_hash: dbe9f0f4ac01ca69
id: fb488ea3-0a81-45e6-bebf-c21351444297
index_schema_version: 1
bdos_index: true
---
# Output Templates

Use these templates verbatim as the skeleton for each note type. Replace `{{placeholders}}` with actual values. Keep every heading — leave sections empty with "…" only if genuinely not applicable.

---

## Book Summary Template

```markdown
# {{title}} — {{author}} ({{year}})
> Master Prompt v7 (PARA)

**Thesis (1-line):** …

## Context
- **Author bio:** …
- **Historical context:** …
- **Genre & tradition:** …
- **Contrarian signal:** …
- **Reception & influence:** …
- **Comparable works:** …
- **Who should read:** …

## Abstract (≤300 words)
…

## Chapter Outline (Deep Analysis)

### Ch. 1 — {{chapter_title}}
**Guiding Question:** …
**Expanded Answer & Key Ideas:** … (½–2 pages if needed)
**Thesis Statement(s):** …
**Extended Commentary:** …
**Skeptical Challenge:** …
**Applications & Implications:** …

### Ch. 2 — {{chapter_title}}
…

_(repeat for every chapter)_

## Key Quotes
1. "…" — p. XX
2. "…" — p. XX

## Tags
`#book` `#summary` `#{{genre}}` …

## Suggested Atomic Notes
- [[Atomic_Idea_Name]] — 1-line description
- …

## Suggested Contrast Notes
- [[A_vs_B_on_Theme]] — axis of disagreement
- …

## Citations
- …
```

---

## Podcast Summary Template

```markdown
# {{show}} — Ep {{n}}: {{title}} ({{date}})
> Master Prompt v7 (PARA)

**Abstract:** …

## Chapter Timestamps
00:00 — Intro
02:23 — Topic A
…

## Key Insights
- …

## Context
- **Host / Guest bio:** …
- **Historical context:** …
- **Genre & tradition:** …
- **Contrarian signal:** …
- **Comparable episodes / works:** …

## Tags
`#podcast` `#summary` …

## Suggested Atomic Notes
- [[Atomic_Idea_Name]] — 1-line description
- …

## Suggested Contrast Notes
- [[A_vs_B_on_Theme]] — axis of disagreement
- …

## Citations
- …
```

---

## Article Summary Template

```markdown
# {{title}} — {{author}} ({{year}})
> Master Prompt v7 (PARA)

**Abstract:** …

## Section Breakdown (Deep Analysis)

### Section 1 — {{section_title}}
**Guiding Question:** …
**Expanded Answer & Key Ideas:** … (detailed write-up)
**Thesis Statement(s):** …
**Commentary:** …
**Skeptical Challenge:** …
**Applications & Implications:** …

### Section 2 — {{section_title}}
…

_(repeat for every section)_

## Key Quotes
1. "…" — para./location
2. "…" — para./location

## Tags
`#article` `#summary` …

## Suggested Atomic Notes
- [[Atomic_Idea_Name]] — 1-line description
- …

## Suggested Contrast Notes
- [[A_vs_B_on_Theme]] — axis of disagreement
- …

## Citations
- …
```

---

## Atomic Idea Note Stub

Save to: `/03_Resources/02_Books/Atomic_Ideas/`
Filename: `Concept_Name.md` (PascalCase with underscores)

```markdown
# {{Concept Name}}

## Definition
…

## Sources
- [[Book_Summary_Name]] (Ch. …)

## Connections
- Related: [[Related_Concept]]
- Opposed: [[Opposing_Concept]]

## My Reflection
…
```

---

## Contrast Note Stub

Save to: `/03_Resources/02_Books/Contrasts/`
Filename: `A_vs_B_on_Theme.md`

```markdown
# {{Author/Concept A}} vs {{Author/Concept B}} on {{Theme}}

## Author / Concept 1
…

## Author / Concept 2
…

## Overlaps
…

## Differences
…

## My Synthesis
…
```
