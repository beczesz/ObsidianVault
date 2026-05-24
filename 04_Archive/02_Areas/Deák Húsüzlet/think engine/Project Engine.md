---
title: Project Engine
version: 0.2
date: 2026-03-31
author: Becze Szabolcs
description: Definition, rules, and usage guide for the 01_PROJECT_STATE.md control file used by AI agents in any project.
---

# Project Engine — 01_PROJECT_STATE.md Definition & Usage

## Purpose

`01_PROJECT_STATE.md` is the **canonical snapshot of the project's current reality**.

It serves as:
- the **primary entry point** for any AI agent (Claude, ChatGPT, etc.)
- a **compressed representation** of the most important project information
- a **control surface** for decision-making and execution

This file must always answer:
- Where are we now?
- What matters right now?
- What happens next?

---

## Location Rule

`01_PROJECT_STATE.md` must always be placed in the **root directory** of the workspace.

- Root = the top-level folder the AI agent has access to
- Never place it in a subfolder
- If it exists elsewhere, move it to the root

---

## Versioning Rule

`01_PROJECT_STATE.md` must always carry a YAML frontmatter header with a version number.

- Use the standard header format (see File Header skill)
- Start at `version: 0.1` when first created
- **Increment the version on every update** — no exceptions
- Version increment rules:
  - Minor content update (status, metrics, tasks): increment second digit (`0.1` → `0.2`)
  - Major revision (complete rewrite or structural change): increment first digit (`0.9` → `1.0`)
- The `date` field must reflect the date of the last update
- Never update the file without bumping the version

---

## Core Principles

1. **Single Source of Truth** — must not conflict with or duplicate other files
2. **Compression Over Completeness** — details belong in referenced files
3. **Deterministic Entry Point** — AI agents start here, no vault exploration before reading
4. **Always Up-to-Date** — stale information must be removed or updated

---

## Structure

This file must follow a fixed schema. The structure must NOT be changed.

- Objective
- Current Status
- Key Metrics
- Active Problems
- Current Focus
- Next Actions
- Constraints
- Last Updated
- Project Map (curated)
- Available Context (optional, minimal)

---

## Project Map Rules

- Include only **high-value files or folders**
- Maximum: **5–10 entries**
- Each entry must include: path + short description
- Do NOT list entire directories blindly
- Do NOT include temporary or low-value files

---

## AI Behavior Rules

1. **Read First** — always read `01_PROJECT_STATE.md` before any action
2. **Default Scope** — operate based on this file unless more info is needed
3. **Use Project Map First** — prefer mapped files over arbitrary exploration
4. **Controlled Expansion** — access additional files only if required or instructed
5. **No Unbounded Exploration** — do NOT scan the entire vault

---

## Update Rules

When updating `01_PROJECT_STATE.md`:
- Preserve the structure exactly
- Update only: Current Status, Key Metrics, Active Problems, Current Focus, Next Actions, Last Updated
- Update the Project Map only if new critical files emerge or structure changes significantly
- **Always increment the version and update the date in the header**
- Do NOT rewrite the entire file unnecessarily
- Do NOT introduce new sections
- Do NOT convert this file into a log or narrative

---

## Curation Rules

- Remove completed or irrelevant tasks from Next Actions
- Keep only current and actionable problems
- Keep the Project Map minimal and relevant
- Move detailed content to appropriate files:
  - decisions → `03_DECISIONS.md`
  - logs → `02_ACTIVITY_LOG.md`
  - full tasks → backlog files
- Target size: ideally under **5–15 KB**

---

## How to Generate a New Project State File

1. Place the file in the **root directory** of the workspace
2. Add a YAML header starting at `version: 0.1` with today's date
3. Define a clear **Objective** (short-term, actionable)
4. Record **Current Status** as facts only
5. Add 3–5 **Key Metrics** (if available)
6. List real **Active Problems** (blockers only)
7. Define **Current Focus** (this week's priorities)
8. Create **Next Actions** as atomic tasks
9. Specify **Constraints** (time, budget, dependencies)
10. Set **Last Updated** to today's date
11. Create a **Project Map** with 3–7 key entry points
12. Optionally define minimal **Available Context**

---

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
