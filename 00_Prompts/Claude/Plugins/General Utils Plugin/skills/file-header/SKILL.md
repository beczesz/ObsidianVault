---
name: file-header
description: >
  This skill should be used when the user asks to add a YAML metadata header
  to a file, or to update an existing header. Trigger phrases: "adj headert
  a filehoz", "tegyél headert", "generálj headert", "frissítsd a headert",
  "updateld a headert", "meta header", "YAML header", "frontmatter hozzáadása",
  "version frissítése a headerben", "írj headert ebbe a fájlba".
version: 0.1.0
id: e8fef22a-81c3-493b-82cb-6c0d5bb26f0a
index_schema_version: 1
---

# File Header Management

Add or update a YAML frontmatter metadata block at the top of any file.

## Header Format

The standard header is a YAML block wrapped in triple-dash delimiters (`---`):

```yaml
---
title: Document Title
version: 0.1
date: 2026-01-26
author: Author Name
description: Brief description of the file's purpose and content
---
```

The header must always be the **very first content** in the file, before any other text.

## Adding a New Header

When the file has no existing header:

1. Read the file with the `Read` tool
2. Confirm the file does not already start with `---`
3. Build the header fields (see Field Rules below)
4. Prepend the header block followed by a blank line before the original content
5. Write the updated content using `Edit` (preferred) or `Write`

## Updating an Existing Header

When the file already starts with `---`:

1. Read the file with the `Read` tool
2. Identify the existing header block (everything between the first `---` and the closing `---`)
3. Parse the current field values
4. Apply only the changes the user requested — preserve all other existing fields unchanged
5. Replace the old header block with the updated one using `Edit`

## Field Rules

| Field | Required | Format | Notes |
|-------|----------|--------|-------|
| `title` | Yes | String | Use the document's main heading if not specified |
| `version` | Yes | `MAJOR.MINOR` (e.g. `0.1`) | Start at `0.1` for new files |
| `date` | Yes | `YYYY-MM-DD` | Use today's date if not specified |
| `author` | Yes | String | Ask the user if unknown |
| `description` | Yes | String | One sentence summarizing purpose and content |

Additional custom fields are allowed — preserve any fields not in the standard set.

## Inferring Missing Fields

If the user does not specify all field values, infer them from context:

- **title**: Use the first `# Heading` in the file
- **date**: Use today's date
- **version**: Use `0.1` for new documents, increment the existing value for updates (e.g. `0.1` → `0.2`)
- **author**: Use the author from the project's CLAUDE.md if available, otherwise ask
- **description**: Summarize the file content in one sentence

Always show the user the complete header before writing and confirm if anything looks wrong.

## Version Increment Rules

When the user says "update the header" without specifying a new version:
- Patch change (minor edit, typo fix): increment third digit if present, or add `.1` (e.g. `0.1` → `0.1.1`)
- Content change (new sections, significant edits): increment second digit (e.g. `0.1` → `0.2`)
- Major revision (complete rewrite): increment first digit (e.g. `0.9` → `1.0`)

When uncertain, ask the user which type of change this represents.

## Multi-file Headers

If the user asks to add headers to multiple files at once, process them sequentially — read, build header, write — one file at a time. Confirm with the user before starting if there are more than 5 files.
