---
title: Sales Dashboard Data Contract
version: 2.0
date: 2026-05-14
author: Sonrisa - Cloud Platform Services (CPS)
status: active
description: Format contract between the live HTML dashboard (Sales/dashboard.html) and the markdown source files (per-lead NOTES.md, Pipeline.md, TODAY.md). Read this before structurally editing any of those files or before adding new fields the dashboard should pick up.
audience: AI agents, human collaborators, anyone editing CPS sales markdown
id: 2940c2de-f788-49f1-8107-23af8c1f526e
index_schema_version: 1
---

# Sales Dashboard Data Contract

> **Critical for any session editing CPS Sales markdown.** `Sales/dashboard.html` is a live, read-only dashboard that polls three markdown files every 8 seconds and rebuilds itself from their content. There is no build step, no database, no manual sync. The markdown files are the single source of truth. Break the contract below, the dashboard degrades silently or fails to surface the relevant card / field.

## Shared dashboard conventions (every dashboard in the vault)

These apply to ALL vault dashboards, not just Sales. When building a new dashboard, follow them so the family stays consistent. Encoded in the `vault-dashboards` capability (`00_Prompts/BDOS/capabilities/vault-dashboards/CLAUDE.md`).

0. **Code lives in `_dashboards/`, content lives in the Areas.** All dashboard HTML, the server, and the run scripts live in `_dashboards/` at the vault root (launcher = `_dashboards/index.html`, e.g. `_dashboards/sales.html`, `_dashboards/partnerships.html`, server = `_dashboards/_tools/dash-server.mjs`). The markdown the dashboards read stays in the Areas. Do NOT co-locate `dashboard.html` next to its data anymore (that was the old convention and it scattered code across the vault).

1. **Absolute fetch paths.** Because every dashboard is served from the vault root, read data via absolute paths: `/02_Areas/Sonrisa/CPS/Sales/Pipeline.md`, not relative `../TODAY.md` or `Pipeline.md`. Depth-independent and unaffected by where the HTML file lives.

2. **Home button.** Every dashboard has a back link to the launcher in the top-left of its masthead:
   ```html
   <a class="home-link" href="/_dashboards/index.html" title="Back to the vault home dashboard">
     <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 11l9-8 9 8"/><path d="M5 10v10h14V10"/></svg>
     Ideas Vault
   </a>
   ```
   Absolute path `/_dashboards/index.html`. Do not use relative paths, they are depth-fragile.

3. **Versioning.** Each dashboard HTML carries a version in a top-of-file comment header and a visible `vX.Y.Z` pill. Start new dashboards at `0.1.0`. Bump: `0.0.x` tweak, `0.x.0` structural, `x.0.0` cross-team canonical. Keep a dated audit trail in the comment header.

4. **Design tokens.** Reuse the shared palette (cream `--bg-page: #faf9f5`, accent `--accent: #D97757`, ink scale, line colors), Inter for UI, JetBrains Mono for code/metrics. Do not invent a new palette per dashboard.

5. **Live sync, read-only.** Fetch markdown, rebuild on change, never write back. Include the sync indicator (dot + "Updated Ns ago, next in Ms" + progress bar + click-to-refresh). Add the SSE client so file-watcher pushes update the dashboard sub-second; keep the poll timer (8s, relaxing to 30s while SSE is connected) as a fallback.

6. **Edit markdown, not HTML.** The HTML is the renderer. Content changes happen in the source markdown. Only touch the HTML to add features or fix parsers, and bump the version when you do.

7. **Register in the launcher.** When a new dashboard goes live, add or flip its leaf in `_dashboards/index.html` to an `Open →` button (absolute href `/_dashboards/<name>.html`) and bump the launcher version.

## Serving

Dashboards require an HTTP origin (`file://` blocks `fetch()`). The standard server is `_dashboards/_tools/dash-server.mjs` (pure Node, zero install): serves the vault root, routes `/` to the launcher, and pushes Server-Sent Events on `*.md` changes for instant updates. Run it with `_dashboards/_tools/start.bat` (Windows), `start.ps1` (PowerShell), or `start.sh` (macOS / Linux), then open `http://localhost:4321/`. A plain static server (`npx serve .` from the vault root) also works but without the instant push (the poll timer covers it); with a plain server, open `/_dashboards/`.

## Operating model

- **Read-only.** The dashboard never writes to any vault file. All persistent edits happen in Obsidian.
- **Polls every 8 seconds** via `fetch()` against three paths relative to the HTML file.
- **Requires HTTP origin.** Must be served, for example with `npx serve .` or `python -m http.server` in the vault root, then visit `http://localhost:<port>/02_Areas/Sonrisa/CPS/Sales/dashboard.html`. `file://` blocks fetch by browser security and the dashboard falls back to a hardcoded snapshot baked into the HTML at the time of writing.
- **Falls back gracefully.** If `leads.md` is missing or malformed, cards still render from `Pipeline.md` alone, just with sparser drawers.

## Source files

The dashboard fetches the following files. Renaming or moving any of them silently breaks sync until the `VAULT_FILES` constant or the per-lead fetch logic in `dashboard.html` is updated.

| Vault path | Role |
|---|---|
| `02_Areas/Sonrisa/CPS/TODAY.md` | Today panel content, action queue, decisions blocking sends |
| `02_Areas/Sonrisa/CPS/Sales/Pipeline.md` | Discovery + stage tracking (Obsidian Kanban). Lists the leads that exist and which lane they sit in. |
| `02_Areas/Sonrisa/CPS/Accounts/Leads/<Name>/NOTES.md` | **Primary** per-lead source. One file per lead, contains the full data the dashboard needs (frontmatter + sectioned body). |
| `02_Areas/Sonrisa/CPS/Sales/Sales Enablement/leads.md` | Optional fallback enrichment. Used if a lead has no per-lead NOTES.md or the file lacks the `type: lead` frontmatter. |

The dashboard loads in this order, per poll cycle:

1. Fetch `Pipeline.md`, discover the set of leads + their stage.
2. For each lead, derive a folder name (smart normalization, see below) and fetch `Accounts/Leads/<derived>/NOTES.md`.
3. If the NOTES.md exists and starts with `type: lead` frontmatter, parse it as the rich per-lead source. Drawer fully driven from this file.
4. If not, fall back to enrichment from `leads.md` (the legacy multi-lead dossier file).
5. Fetch `TODAY.md` for the today panel.

## Per-lead NOTES.md contract (primary source)

Each lead lives in its own file at `Accounts/Leads/<Name>/NOTES.md`. The folder name is derived from the company name by:

1. Take the side before ` / ` (so `KBOSS / Szamlazz.hu` becomes `KBOSS`).
2. Strip parenthetical suffixes (`Riptides (Labs)` becomes `Riptides`).
3. Replace spaces and dashes with underscores.
4. Keep alphanumerics, dots, underscores. Drop other punctuation.

Example folder names: `KBOSS_Szamlazz`, `NETOPIA_Payments`, `EOS_Faktor`, `SafeFleet_Telematics`, `Allonic`, `CIG_Pannonia`, `Greenergy`, `Chemaxon`, `SEON`, `Colossyan`, `Lensa`, `Loxon_Solutions`, `Barion_Payment`, `Pentech`, `ABZ_Innovation`.

The template is `02_Areas/Sonrisa/CPS/Accounts/_Template/LEAD_NOTES.md`. New leads (manual or scraped) must copy from this template.

### Frontmatter schema

**Required** (lead is skipped if missing):

| Key | Type | Example |
|---|---|---|
| `type` | string, must equal `lead` | `lead` |
| `company` | string | `"KBOSS / Szamlazz.hu"` |
| `stage` | enum string | `hot` (one of: hot, warm, cold, contacted, discovery, proposal, won, lost) |
| `source_url` | URL string | `"https://profession.hu/..."` — **the original opportunity link, prominently rendered in the drawer header** |

**Optional but recommended** (each drives a specific UI slot):

| Key | Type | Drives |
|---|---|---|
| `id` | string | stable lead id (defaults to derived from company name) |
| `score` | integer 0 to 15 | score chip on card and drawer header |
| `score_breakdown` | object with `maturity`, `posting`, `aws`, `team_gap`, `geo_fit` | 5-cell score grid in drawer |
| `tags` | string array | tag chips on card (drop stage names) |
| `geo` | string (`HU`, `RO`, `NL`, `INT`, ...) | geo filter |
| `language` | string (`hu`, `en`, `ro`) | language tag |
| `due` | YYYY-MM-DD string | due pill on card |
| `next_action` | string | "next action" verb shown on card |
| `status` | enum | flow status (research / ready_to_send / awaiting_reply / in_conversation / won / lost) |
| `location` | string | HQ field in drawer About |
| `industry` | string | industry field |
| `founded` | integer | About sub-meta |
| `employees` | string | About sub-meta |
| `icp` | string | ICP fit field |
| `package` | object: `tier`, `monthly_eur`, `addons[].name`, `addons[].eur`, `total_eur` | package box on card and drawer |
| `sources` | object: `posting`, `career_page`, `linkedin`, `jira`, `validation_pass` | extra source links in drawer |
| `channels` | string array | sales channel chips |
| `primary_channel` | string | highlighted primary channel chip |
| `case_study_match` | string | reference text in drawer |
| `created`, `validated`, `last_signal_check` | YYYY-MM-DD | timeline metadata |

### Body sections

H2 section headers map to drawer slots. The parser is **case-sensitive** on section names. Use these exact names:

| Section heading | Drawer slot | Format inside |
|---|---|---|
| `## Signal` | Signal source paragraph | Free prose |
| `## What They Want` | Stack / requirement chip list | Bullet list, one item per line |
| `## About the Company` | About paragraph | Free prose. Parser also extracts stack chips from lines starting with `Stack:` |
| `## Why This Is Interesting` | Why paragraph | Free prose |
| `### Pain Hypotheses` (sub-section of "Why This Is Interesting") | Pain bullet list | Bullet list, one item per line |
| `## Value Propositions` | Value props list under package box | Bullet list, one item per line |
| `## Key Contacts` | Contacts table | Markdown table: Name, Role, LinkedIn, Approach, Status |
| `## The Angle` | Strategy angle paragraph | Free prose |
| `## Timing` | Strategy timing paragraph | Free prose |
| `## Red Flags` | Red flags callout | Bullet list, one item per line |
| `## Drafts` | Outreach drafts section | Sub-sections per draft (see below) |
| `### Option A, LinkedIn (HU)` etc. (sub-section of Drafts) | One draft block | Fenced code block (` ```text ` or ` ``` `) containing the draft |
| `## Action Items` | Action items checklist | `- [ ]` / `- [x]` lines |
| `## Next Step` | Next step paragraph | One sentence |

If a section is missing, the corresponding drawer slot is hidden. The dashboard never errors on missing optional content.

### Lead identity for matching to Pipeline.md

A Pipeline.md card with `**KBOSS / Szamlazz.hu**` is matched to the NOTES.md file at `Accounts/Leads/KBOSS_Szamlazz/NOTES.md` via the folder derivation above. The frontmatter `company` field does not need to match Pipeline.md byte-for-byte, but the folder name does need to be derivable.

If a lead exists in Pipeline.md but no per-lead NOTES.md is found, the dashboard renders the card from Pipeline.md data only and the drawer is sparse (just the teaser plus an "Open in Obsidian" link). This is the fallback path.

### Common breaks (per-lead file)

| Mistake | Consequence |
|---|---|
| Missing `type: lead` in frontmatter | Dashboard ignores the file, falls back to Pipeline.md only |
| Missing `source_url` | Drawer header "View original opportunity" button is hidden, big UX regression |
| Section heading typo (e.g. `## Whay They Want`) | Section's drawer slot is hidden |
| Markdown table with wrong column order in Key Contacts | Columns mis-mapped (parser uses position, not header) |
| Multi-line frontmatter string without proper YAML quoting | YAML parse error, dashboard logs warning, falls back |
| Draft outside a fenced code block | Treated as prose, copy-to-clipboard button shows the wrong content |

## Pipeline.md contract

Obsidian Kanban plugin format. **Keep the frontmatter intact** or the file stops being a kanban:

```
---
kanban-plugin: basic
---
```

### Column headers

Format `## ColumnName`. The parser matches the stage by case-insensitive prefix of the column name:

| Column starts with | Lane in dashboard |
|---|---|
| `HOT` | HOT |
| `WARM` | WARM |
| `COLD` | COLD |
| `Contacted` | Contacted |
| `Discovery` | Discovery |
| `Proposal` | Proposal |
| `Won` | Won |
| `Lost` | Lost |

Anything else, the parser skips. So `## HOT - Outreach This Week` works, `## Outreach This Week` does not.

### Card line format

```
- [ ] **CompanyName** #tag1 #tag2 @{YYYY-MM-DD} optional teaser text [[wiki-link]]
```

Required:
- `- [ ]` or `- [x]` checkbox prefix. The state is ignored by the dashboard, only the column determines the stage.
- `**CompanyName**` bold name at the start. The first `**...**` pair on the line wins.

Optional, all order-independent after the bold name:
- `#hashtags`. Stage tags (`#hot`, `#warm`, `#cold`, `#contacted`, `#discovery`, `#proposal`, `#won`, `#lost`) are filtered out. Everything else (`#fintech`, `#engine-b`, `#lang-hu`, `#romania`) appears as a tag chip on the card.
- `@{YYYY-MM-DD}` due date. Renders as "DUE TODAY", "DUE IN 2D", overdue in red.
- `[[wiki-links]]`. Stripped from the teaser display.
- Free text. Everything else becomes the card teaser (3-line clamp).

### What breaks Pipeline.md

| Mistake | Consequence |
|---|---|
| Missing the `**` around the company name | Card disappears from the dashboard |
| `# HOT` instead of `## HOT` | Lane never populates |
| Card lines above the first `##` heading | Cards ignored |
| `📅 2026-05-13` instead of `@{2026-05-13}` | Due date not parsed (Pipeline uses `@{}`, TODAY uses `📅`, they are not interchangeable) |
| Renaming the file | Dashboard offline until `VAULT_FILES.pipeline` updated |

## leads.md contract

Plain markdown, one dossier per lead.

### Lead header

```
### CompanyName
```

Optional score and label suffix:
```
### CompanyName -- Score: 14/15 -- HOT
```

The company name does not need to match Pipeline.md byte-for-byte. The dashboard uses a smart matching key that:
1. Strips parenthetical suffixes, so `KBOSS.hu Kft. (Szamlazz.hu)` becomes `KBOSS.hu Kft.`
2. Takes the side before `/`, so `KBOSS / Szamlazz.hu` becomes `KBOSS`
3. Splits on whitespace and punctuation, drops corporate suffixes (Kft, Zrt, SRL, GmbH, AG, Inc, Ltd, LLC, BV, NV, hu, com, io, ai)
4. Takes the first token if it is 6+ chars, else the first two tokens, normalized to lowercase alphanumeric

So `KBOSS / Szamlazz.hu` (Pipeline.md) and `KBOSS.hu Kft. (Szamlazz.hu)` (leads.md) both resolve to key `kboss` and are matched. Same applies to other naming variants.

### Field bullets

```
- **Location:** Budapest, Hungary
- **Company:** Hungary's largest online invoicing platform. Founded 2004. ~50 employees.
- **Signal:** ...
- **AWS stack:** Confirmed (AWS, Terraform, Jenkins)
...
```

Field name is enclosed in `**...**` followed by a colon. Field value is everything on the rest of that single line. Multi-line values are **not** parsed (only the first line).

| Field heading (case-sensitive) | Renders in drawer as |
|---|---|
| `Location` | About the company: HQ |
| `Company` | About the company: industry sentence + auto-extracted founded year (`Founded YYYY`) + employees (`~N employees`) |
| `Signal` or `Signal history` | Signal source section |
| `AWS stack` | "What they want" stack chip list, plus stack chips in About |
| `Reverse-engineered cloud setup` | Stack chips fallback if no AWS stack field |
| `Decision-maker` | First row of Key Contacts table |
| `Pain points` | Pain hypotheses bullet list. Format the value as `(1) ... (2) ... (3) ...` for clean splitting; otherwise the dashboard splits on periods |
| `CPS fit` | "Why this is interesting" paragraph |
| `Best outreach angle` | Sales strategy angle, also added as a value prop |
| `Recommended package` | Recommended package box. Parser extracts tier (Safety Net / Essential / Growth / Scale) and add-ons (FinOps / DevSecOps / 24/7 / Solution Architect) with their EUR amounts. Format: `Essential EUR 2,000/mo + FinOps EUR 500/mo` |
| `Scoring` | 5-cell score grid. Format: `Maturity 3/3 \| Posting age 3/3 \| AWS confirmed 2/3 \| Team gap 3/3 \| Geo fit 3/3` |
| `Next step` | Dedicated "Next step" drawer section |
| `Where it lives now` | Strategy timing line |
| `Key Risks` or `Caveats` | Red flags callout |

Any other `- **Field:**` is still captured on the lead object but does not get its own UI slot.

### What breaks leads.md

| Mistake | Consequence |
|---|---|
| Missing `**` around the field name | Field not parsed |
| `**Field name **:` with a stray space | Not parsed |
| Multi-line values, especially sub-bullets | Only the first line captured |
| Changing the heading depth (`##` or `####`) | Lead not detected |
| Using a name that does not share the first significant token with the Pipeline.md card | Dossier not matched, drawer renders sparse |

## TODAY.md contract

### Day section headers

The parser matches two formats:
- Labeled: `## Today: 2026-05-13 (Wednesday)`, `## Tomorrow: 2026-05-14 (Thursday)`
- Weekday: `## Wednesday: 2026-05-13`

The dashboard picks the section whose date matches the current system date, falls back to the next future date if no exact match, then:
- That section renders as "Today" in the panel
- The next section as "Tomorrow"
- Subsequent sections as "Later this week" preview

### Sub-section routing

Within a day, sub-sections are `### Section name`. Two routing rules:
- Sub-section name contains "decisions needed" (case-insensitive) → tasks go to the Decisions column
- Anything else → tasks go to the Outreach column for that day

### Task line format

```
- [ ] **Optional Company** Free-text description 📅 2026-05-13 #tag [[wiki-link]]
```

Recognized markers:
- `- [ ]` open, `- [x]` done. Done tasks are hidden from the Today column.
- `**CompanyName**` bold name. Links the task to a kanban lead card. Click the task in the dashboard to open that lead's drawer.
- `📅 YYYY-MM-DD` due date. Note: TODAY.md uses the emoji form, Pipeline.md uses `@{}`. Do not swap them.
- `✅ YYYY-MM-DD` completion date.
- `#tag` priorities for the task chip: `decision`, `followup`, `lead`, `milestone`, `review`, `drafting`. First recognized one wins.

### What breaks TODAY.md

| Mistake | Consequence |
|---|---|
| Day section heading without a date (e.g., `## Today` alone) | That day is not picked as "today" |
| Tasks above the first `### Subsection` | Not rendered |
| Multi-line task descriptions | Only first line captured |
| `@{2026-05-13}` instead of `📅 2026-05-13` | Due date not parsed |

## Lead identity

A "lead" in the dashboard is **one row in Pipeline.md**. Two Pipeline rows with similar names (e.g., the active `**CIG Pannonia**` in Contacted and the archived `**CIG Pannonia (old outreach attempt)**` in Lost) are two distinct leads. They share the same dossier from leads.md when one exists.

The card id is the full normalized form of the bold name. The dossier match is the smart key described in the leads.md section.

## Adding a new lead, end to end

The new flow makes per-lead NOTES.md the primary source. Steps for any session (human or scraper agent):

1. **Copy the template** to create the lead file:
   ```
   02_Areas/Sonrisa/CPS/Accounts/Leads/<NormalizedName>/NOTES.md
   ```
   based on `02_Areas/Sonrisa/CPS/Accounts/_Template/LEAD_NOTES.md`.

2. **Fill in the frontmatter.** Required: `type: lead`, `company`, `stage`, `source_url`. Highly recommended: `score`, `tags`, `due`, `next_action`, `package`, `location`, `industry`. The richer the frontmatter, the richer the card.

3. **Fill in body sections** that have content. Skip sections where information is not yet known, the dashboard hides empty slots. Common minimum: Signal, About the Company, Why This Is Interesting (with Pain Hypotheses), and at least one Draft block.

4. **Add a kanban card to Pipeline.md** in the correct stage column:
   ```
   - [ ] **CompanyName** #tag1 #tag2 @{2026-05-15} short 1-line teaser
   ```
   The bold company name must match what is derivable to the folder name above.

5. Wait up to 8 seconds. Dashboard auto-fetches the new lead, renders the card and drawer.

## Scraper / agent protocol for new opportunities

Any scraping skill (lead-scanner, librarian, integrate mode, etc.) that creates new leads MUST follow this protocol so the dashboard receives them in the right shape:

1. Read the template at `Accounts/_Template/LEAD_NOTES.md`.
2. Generate the new lead file at `Accounts/Leads/<NormalizedName>/NOTES.md` using the template as a starting point. Do not invent new top-level frontmatter keys, the dashboard only knows the documented set.
3. Fill `source_url` with the actual URL where the opportunity was found. **This is mandatory**, the user explicitly needs to see this link.
4. Set `created` to today's date.
5. Set `stage` matching the Pipeline.md column you will add the card to.
6. Add the kanban card to `Sales/Pipeline.md` per the Pipeline.md contract section above.
7. If you have a draft outreach, place it inside a fenced code block under `## Drafts` with a sub-heading like `### Option A, LinkedIn (HU)`.
8. If you have action items, write them as `- [ ]` lines under `## Action Items`.
9. Do not edit `dashboard.html`. The dashboard reads what you wrote.

## Reformatting an existing lead

To migrate an existing lead that lives only in `leads.md` (legacy) or `Pipeline.md` (lightweight) to the new schema:

1. Create the folder `Accounts/Leads/<NormalizedName>/`.
2. Copy `Accounts/_Template/LEAD_NOTES.md` into it as `NOTES.md`.
3. Fill in frontmatter from whatever fields exist in `leads.md` (Location, Company, Signal, AWS stack, Pain points, Recommended package, Scoring, etc.). Map field names per the legacy-to-new mapping in the leads.md section below.
4. Fill body sections from the same source.
5. Optional: remove the lead's section from `leads.md` after the migration. The dashboard prefers the per-lead file when both exist.
6. Verify the dashboard renders the lead correctly within 8 seconds.

## Removing a lead

1. Delete or move the card line in Pipeline.md.
2. Wait up to 8 seconds. The lead disappears.

The leads.md dossier and any NOTES.md file are NOT auto-removed. They become orphaned but unrendered. Decide separately whether to archive them.

## Debugging a missing card or field

1. Open browser DevTools (F12) on the dashboard.
2. Console logs fetch errors, parser exceptions.
3. Hover the green / gray dot in the Today panel sync indicator. The tooltip names which files loaded and how many leads got built.
4. The single most common issue: missing `**` around the company name, or a typo in the Pipeline.md column name.

## Operating procedure summary, for sales-engine agents

When you are working on Sales material in any session:

- Edit Pipeline.md, leads.md, TODAY.md freely. The dashboard auto-syncs.
- Preserve the formats described above. If you find yourself wanting to add a new structural pattern (e.g. a new field, a new column, a multi-line value), update the dashboard parser first or coordinate with a session that can.
- Do not generate a new `dashboard.html` per session. The HTML is built once, then driven by the markdown.
- Do not write to `dashboard.html` to change displayed data. Write to the source markdown.

## Reference implementation

`Sales/dashboard.html`. Relevant functions:

- `parsePipelineMd(md)` → stages of cards
- `parseLeadsMd(md)` → dossiers keyed by `leadDossierKey`
- `parseTodayMd(md)` + `buildViewFromParsed(parsed)` → today panel view
- `buildLeadsFromMd(pipelineMd, leadsMd)` → final LEADS array
- `pollVault()` → 8-second sync loop
- `VAULT_FILES` constant → the three file paths

## Version history

- v1.0 (2026-05-13): Initial contract. Pipeline.md + leads.md + TODAY.md.
