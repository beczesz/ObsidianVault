---
name: project-engine
description: >
  This skill should be used when the user asks to create, update, review, or
  manage a 01_PROJECT_STATE.md file -- or when starting work on any project
  that needs a structured state snapshot. Trigger phrases: "project state",
  "create project state", "update project state", "01_PROJECT_STATE",
  "where are we", "project status", "initialize project", "project engine".
version: 0.2.0
id: 529ee0fc-9840-4902-85ef-8774f5fe7875
index_schema_version: 1
---

# Project Engine -- 01_PROJECT_STATE.md Management

Create, update, and maintain the canonical `01_PROJECT_STATE.md` project state file.

## What Is 01_PROJECT_STATE.md

It is the **single source of truth** for any project. It answers three questions:

1. Where are we now?
2. What matters right now?
3. What happens next?

It serves as the primary entry point for any AI agent, a compressed representation of the most important project information, and a control surface for decision-making and execution.

## Location Rule

`01_PROJECT_STATE.md` must always be placed in the **root directory** of the workspace (the top-level folder the AI agent has access to). Never place it in a subfolder. If it exists elsewhere, move it to the root.

## Versioning Rule

The file must always carry a YAML frontmatter header with a version number (use the File Header skill format).

- Start at `version: 0.1` when first created
- **Increment the version on every update** -- no exceptions
- Minor content update (status, metrics, tasks): increment second digit (`0.1` -> `0.2`)
- Major revision (complete rewrite or structural change): increment first digit (`0.9` -> `1.0`)
- The `date` field must reflect the date of the last update

## Required Structure (Fixed Schema)

The file must follow this exact structure. Do NOT change, reorder, or add new sections:

1. **Objective** -- what is the project trying to achieve (short, actionable)
2. **Current Status** -- factual description of where things stand
3. **Key Metrics** -- 3-5 quantifiable indicators
4. **Active Problems** -- current blockers only (not historical)
5. **Current Focus** -- this week's priorities
6. **Next Actions** -- atomic, actionable tasks
7. **Constraints** -- time, budget, dependencies
8. **Last Updated** -- date of the last edit
9. **Project Map** -- curated list of 5-10 high-value files/folders with descriptions
10. **Available Context** -- optional, minimal references to additional info

## Creating a New Project State

When the user asks to create or initialize a project state:

1. Read the workspace to understand the project structure
2. Create the file at the workspace root
3. Add YAML header starting at `version: 0.1` with today's date
4. Fill in all sections based on available context
5. Keep the Project Map to 3-7 key entry points
6. Ask the user to validate before finalizing

## Updating an Existing Project State

When the user asks to update the project state:

1. Read the current `01_PROJECT_STATE.md`
2. Update only: Current Status, Key Metrics, Active Problems, Current Focus, Next Actions, Last Updated
3. Update the Project Map only if new critical files emerged or structure changed
4. **Always increment the version and update the date**
5. Do NOT rewrite the entire file unnecessarily
6. Do NOT introduce new sections or convert it into a log

## Curation Rules

- Remove completed or irrelevant tasks from Next Actions
- Keep only current and actionable problems
- Keep the Project Map minimal and relevant
- Move detailed content to appropriate files (decisions to `03_DECISIONS.md`, logs to `02_ACTIVITY_LOG.md`, full tasks to backlog files)
- Target size: under **5-15 KB**

## Project Map Rules

- Include only **high-value files or folders**
- Maximum: **5-10 entries**
- Each entry: path + short description
- Do NOT list entire directories blindly
- Do NOT include temporary or low-value files

## AI Behavior Rules

1. **Read First** -- always read `01_PROJECT_STATE.md` before any action
2. **Default Scope** -- operate based on this file unless more info is needed
3. **Use Project Map First** -- prefer mapped files over arbitrary exploration
4. **Controlled Expansion** -- access additional files only if required or instructed
5. **No Unbounded Exploration** -- do NOT scan the entire vault

## Anti-Patterns (Must Be Avoided)

- File not in the root directory
- Missing or unversioned YAML header
- Version not incremented after an update
- Turning this file into a long document
- Mixing strategy discussions into status
- Keeping historical data here
- Duplicating content from other files
- Listing entire folders in the Project Map
- Allowing uncontrolled file exploration
