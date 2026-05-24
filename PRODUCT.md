---
title: Ideas Vault, Product Brief
register: product
version: 1.0
date: 2026-05-18
id: 5faf5304-ab97-4cd9-a5ec-5d0e99e1b607
index_schema_version: 1
---

# Ideas Vault, Product Brief

## What this is

An Obsidian-based personal and business operating system. Not a public product. One user, one machine. Used as the coordination layer across several active businesses and life domains.

## Users

Single user: the vault owner. Manager and operator running multiple parallel businesses (Sonrisa CPS, Deák Húsüzlet, Navigátor Podcast, ExarLabs, Mikado, Média Műhely, Ignis Academy, plus org-development practice and personal growth work). Reads in Obsidian, edits in Obsidian, but occasionally needs browser-based dashboards because the dashboards live-poll markdown and render structure that Obsidian alone cannot.

## Purpose

Coordinate work across many parallel domains without losing context. The vault is the source of truth. The dashboards are read-only lenses over the markdown.

## Surfaces

| Surface | Role |
|---|---|
| `index.html` at vault root | Unified navigation hub, today's anchor, jump-off to sub-dashboards |
| Sub-dashboards per active area | Operational views (kanban, pipeline, KPIs) that live-read markdown |
| Markdown indexes (`00_INDEX.md`) | Tier-2 entry points per Area, opened in Obsidian |
| Daily notes | The temporal spine, one per day under `05_DailyNotes/YYYY/Month/` |

Sub-dashboards are served via `python -m http.server 8000` from the vault root, addressed at `http://localhost:8000/02_Areas/<Area>/.../dashboard.html`. The root hub resolves at `http://localhost:8000/` directly because the file is named `index.html`.

## Tone

Calm, professional, restrained. Earned familiarity over novelty. The tool disappears into the task.

## Anti-references

- SaaS gradient hero patterns
- Glassmorphism as decoration
- Identical card grids without rhythm
- Hero-metric template (big number, small label, gradient accent)
- Decorative motion that does not convey state
- Em-dashes anywhere in vault content. Use commas, colons, semicolons, periods, or parentheses. This is a hard rule, not a preference.

## Strategic principles

- **PARA-modified, Areas-dominant.** Businesses are tracked as Areas (long-term responsibilities), not Projects (short-lived tasks). See vault `CLAUDE.md` for the full convention.
- **BDOS (Business Development Operation System).** AI agents are stable cognition roles, not chat replicas. See `00_Prompts/BDOS/CLAUDE.md`.
- **Two-tier indexing.** Vault root holds global indexes. Active areas hold their own scoped indexes when they cross the substantive threshold.
- **Markdown is the source of truth.** Dashboards never write back. All persistent edits happen in Obsidian.

## Language

Mixed Hungarian and English. English is the default for UI chrome and labels. Hungarian brand names and proper nouns are preserved verbatim (Deák Húsüzlet, Média Műhely, Szervezet Fejlesztés). Do not translate brand names.
