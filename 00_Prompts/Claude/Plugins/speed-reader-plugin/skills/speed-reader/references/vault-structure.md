---
title: "Vault Structure, File Naming & Save-To Header"
date: 2026-04-21
author: Becze Szabolcs
status: active
description: "Complete guide to organizing the Idea Vault using PARA structure, file naming conventions for books, podcasts, articles, atomic ideas, and contrast notes, plus the Save-To header format for directing where each file should be stored. Essential reference for maintaining consistent vault structure and automation."
description_source: auto
description_hash: f239b05cb34f464c
id: d716239a-dbec-4ba1-8996-3face9f8d6f0
index_schema_version: 1
bdos_index: true
---
# Vault Structure, File Naming & Save-To Header

## Vault Overview

**Vault name:** `Idea Vault` (Google Drive–synced, PARA structure)

```
Idea Vault/
├── 00_Prompts/                          ← master prompt lives here
├── 01_Projects/
├── 02_Areas/
├── 03_Resources/
│   ├── 02_Books/
│   │   ├── <Author - Title>/            ← one subfolder per book
│   │   │   ├── Title_Author_Year.md     ← summary note
│   │   │   └── Title_Author.pdf         ← source file (if provided)
│   │   ├── Atomic_Ideas/                ← concept-level notes
│   │   └── Contrasts/                   ← comparison notes
│   ├── 03_Podcasts/
│   ├── 04_Articles/
│   └── 05_References/
├── 04_Archive/
└── Templates/
```

---

## Folder Rules

### Books
1. Check if `/03_Resources/02_Books/<Author - Title>/` exists.
2. If not, **create it**.
3. Save both the Markdown summary **and** the source file (PDF/ePub) inside.
4. Example folder: `Robert B. Cialdini - Influence`

### Podcasts
- Save to `/03_Resources/03_Podcasts/`

### Articles
- Save to `/03_Resources/04_Articles/`

### Atomic Ideas
- Save to `/03_Resources/02_Books/Atomic_Ideas/`

### Contrast Notes
- Save to `/03_Resources/02_Books/Contrasts/`

---

## File Naming Conventions

| Type | Pattern | Example |
|------|---------|---------|
| Book summary | `Title_Author_Year.md` | `Influence_Robert_B_Cialdini_1984.md` |
| Book source | keep original, or `Title_Author.pdf` | `Influence_Robert_B_Cialdini.pdf` |
| Podcast | `Show_EpNNN_Title_YYYY-MM-DD.md` | `Huberman_Ep042_Sleep_2023-03-15.md` |
| Article | `Source_Title_Author_Year.md` | `HBR_Leading_Change_Kotter_1995.md` |
| Atomic idea | `Concept_Name.md` (PascalCase + underscores) | `Scarcity_Mindset.md` |
| Contrast note | `A_vs_B_on_Theme.md` | `Peterson_vs_Dostoevsky_on_Suffering.md` |

### Collision Handling
**Never overwrite** existing files. If a filename already exists, append `-v2`, `-v3`, etc.

---

## Save-To Header Format

Place this block at the very top of the response (before the main note) so the user (or automation) knows where each file goes:

```
SAVE-TO: /03_Resources/02_Books/Robert B. Cialdini - Influence/
FILES:
  - Influence_Robert_B_Cialdini_1984.md
  - Influence_Robert_B_Cialdini.pdf   (if provided)
ALSO-CREATE:
  - /03_Resources/02_Books/Atomic_Ideas/Social_Proof.md
  - /03_Resources/02_Books/Contrasts/Cialdini_vs_Ariely_on_Behavior.md
```

### Rules
- `SAVE-TO` is the primary folder for the main summary + source file.
- `FILES` lists every file that goes into that folder.
- `ALSO-CREATE` lists any additional notes (atomic, contrast) with their full paths.
- Always resolve paths relative to the vault root (`Idea Vault/`).
