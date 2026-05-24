# CPS Working Memory

Avoid em Dashes

## Session Start Convention

On every session start, BEFORE any task work, read `TODAY.md` at the vault root for the current day's action queue. Surface:
- Anything overdue (📅 dates earlier than today)
- Anything due today
- Open user-decisions blocking tomorrow's sends

The TODAY.md file is the single source for what needs to happen today. After completing tasks, mark them done in TODAY.md with `[x]` + `✅ YYYY-MM-DD` and add a line under the "Done log" section.

## Quick Reference

**Vision:** "We are the Backstage Crew who runs the show"
**Mission:** Stabilitás, Innováció, Fejlődés
**#1 Value:** Alázat - "Az lesz a legnagyobbra értékelve, aki a legalázatosabb"

## Sales Engine (start here for sales work)

**Start here:** `Sales/SALES_ENGINE.md` -- complete system overview, agentic flow, KPIs, benchmarks.

Key files (read in this order):
1. `Sales/SALES_ENGINE.md` -- system overview + agentic flow documentation
2. `Sales/Pipeline.md` -- Obsidian Kanban board (single source of truth for leads)
3. `Sales/Dashboard.md` -- KPI dashboard with weekly velocity tracking
4. `Strategy/CPS Sales Strategy v2.0.md` -- 3-engine strategy + 90-day plan
5. `Sales/Sales Enablement/leads.md` -- detailed lead research notes
6. `brainstorm/brainstorm_sales-strategy-agentic-review.md` -- thinking team review

**Pipeline is in Obsidian Kanban** (`Sales/Pipeline.md`). Columns: HOT / WARM / COLD / Contacted / Discovery / Proposal / Won / Lost.

### Live HTML dashboard (read this before editing pipeline data)

There is a live dashboard at `Sales/dashboard.html` that polls source markdown every 8 seconds and renders an interactive kanban + today panel. **It does not need to be regenerated when you edit the source markdown.** It rebuilds itself from the live files.

**Contract:** `Sales/DASHBOARD_CONTRACT.md` is the canonical spec.
**Template for new leads:** `Accounts/_Template/LEAD_NOTES.md`.

**Per-lead is now the primary source.** Each lead lives at `Accounts/Leads/<Name>/NOTES.md` with strict frontmatter (`type: lead`, `company`, `stage`, `source_url`, plus optional `score`, `tags`, `due`, `next_action`, `package`, etc.) and H2 body sections (Signal, What They Want, About the Company, Why This Is Interesting, Pain Hypotheses, Value Propositions, Key Contacts, The Angle, Timing, Red Flags, Drafts, Action Items, Next Step). Copy the template, do not invent new field names.

The user explicitly requires `source_url` on every lead. This is the original opportunity URL (posting / career page / signal), rendered prominently at the top of the drawer.

Hard rules to avoid silent breakage:
- **Per-lead NOTES.md** uses YAML frontmatter (must start with `---` line, `type: lead` required) and H2 section headings exactly as documented in `DASHBOARD_CONTRACT.md`. Section headings are case-sensitive.
- **Pipeline.md** must stay in Obsidian Kanban format, with `## ColumnName` lanes (HOT / WARM / COLD / Contacted / Discovery / Proposal / Won / Lost prefix match) and card lines `- [ ] **CompanyName** #tag @{YYYY-MM-DD} teaser`. Used for discovery + stage tracking, the kanban remains the workflow surface.
- **leads.md** is now legacy fallback. Prefer creating per-lead NOTES.md files for new leads.
- **TODAY.md** uses `## Today: YYYY-MM-DD (Weekday)` day headers, `### subsection` blocks, and `- [ ] task 📅 YYYY-MM-DD` tasks. Pipeline uses `@{}` for dates, TODAY uses `📅`, do not swap them.
- The HTML file (`dashboard.html`) should not be regenerated for content changes. Edit the source markdown instead. Only touch the HTML to add features or fix parsers, and update `DASHBOARD_CONTRACT.md` in the same change.

**Scraper / scanner protocol.** When any scraping skill or agent adds a new lead:
1. Copy `Accounts/_Template/LEAD_NOTES.md` to `Accounts/Leads/<NormalizedName>/NOTES.md`.
2. Fill `source_url` with the actual URL where the opportunity was found (REQUIRED).
3. Fill frontmatter and body sections from research output.
4. Add a kanban card to `Sales/Pipeline.md` in the right stage column.
5. Do not edit `dashboard.html`.

The dashboard must be served over HTTP to live-sync. Open it via `npx serve .` (or `python -m http.server`) from the vault root, then visit `http://localhost:<port>/02_Areas/Sonrisa/CPS/Sales/dashboard.html`. The `file://` protocol blocks fetch and the dashboard falls back to a stale snapshot.

**Thinking Team:** Use `/general-utils:think-agent-orchestrator-v07` for strategic reviews. Team: ChatGPT (Strategist), Perplexity (Researcher), Gemini (Validator), Claude Chat (Domain Expert).

**IMPORTANT:** CPS does NOT have NIS2 certification. Do not advertise NIS2 readiness in any outreach or materials.
**IMPORTANT:** Volume before quality. Primary KPI = first touches sent per week (target 25). Do NOT over-research leads before outreach.
**IMPORTANT (verify-before-send, user rule 2026-05-20):** Before presenting ANY lead to the user or sending outreach, re-validate that the lead is STILL RELEVANT. Lightweight check: confirm the trigger/signal still exists right now (e.g., the job posting is still live and "actively reviewing", the company still hiring, no acquisition/redirect). This is the Chemaxon lesson (stale posting) and the Allonic lesson (no trigger at all). It is NOT over-researching, it is a live-relevance gate. State the validation evidence + timestamp when presenting a lead. Park or drop leads whose trigger has gone stale.

## Folder Structure

```
CPS/
  01_PROJECT_STATE.md        -- single source of truth for project status (versioned)
  CLAUDE.md                  -- THIS FILE, AI working memory
  CPS Constitution.md        -- founding principles and values
  PO_numbers.md              -- purchase order reference
  TASKS.md                   -- detailed task tracker
  memory/                    -- AI persistent knowledge base
  brainstorm/                 -- thinking team session files
  Accounts/
    _Template/NOTES.md       -- NOTES.md template (use when creating new accounts)
    Active/                  -- paying clients (each has NOTES.md)
      Colosseum_Dental/
      Diligentes/
      Direct_Travel/
      Green_Hill_SynLab/
      Jumeon/
      MVMI/                  -- has sub-engagements:
        NOTES.md               -- account-level overview
        AzureDevOps Managed Service/   -- separate team & contract
          NOTES.md
          Tender/
        Omni Support/          -- separate team & contract (OpenShift)
          NOTES.md
      OKFO/
      Observer/
      Onriva/
      ProSharp/
      SocialBud/
    Leads/                   -- prospects being evaluated (each has NOTES.md)
      CIG_Pannonia/
      EOS_Faktor/
      Greenergy/
      KBOSS_Szamlazz/
      NETOPIA_Payments/
      SafeFleet_Telematics/
  Marketing/                 -- blogs, website, selvio CMS
  Sales/
    SALES_ENGINE.md          -- complete sales system documentation (START HERE)
    Pipeline.md              -- Obsidian Kanban board (lead tracking)
    Dashboard.md             -- KPI dashboard with Dataview queries
    Case Studies/            -- published case studies
    Sales Enablement/        -- leads.md, Lead Scanner/, outreach templates
  Services/                  -- service descriptions, cost optimization, ITIL, Inference Farm
  Strategy/                  -- roadmap, BMC, AWS partnership, competitor reports, FinOps
  Team/                      -- units, communication, recruitment, workshops
  Partnership/               -- Ingram Micro, partner tracks
```

## Accounts Convention

Every account (Active or Lead) has a **NOTES.md** as its entry point. Use `Accounts/_Template/NOTES.md` as the starting template. Key sections: Quick Info table, What Is This Account, Current Situation, Key History, People, Open Items, Profitability, Related Files.

When an account has multiple distinct engagements (like MVMI), create sub-folders per engagement, each with its own NOTES.md. Keep one account-level NOTES.md at the root for overview.

When the user says "let's work on account X" or "review client Y", start by reading that account's NOTES.md to orient yourself.

## Team Structure

**Total:** ~13 engineers + 1 E9+ contractor

**Leadership:**
- Ceclan Alexandru (Team Lead, 6h/day, keeps team together)
- Szántó Zoltán (Team Lead, proactive, cloud native, CORE)
- Póda Alexander (Senior, AWS expert, reliable)

**Architect:** E9+ Contractor (AWS, GCP, Oracle) ⭐

**Sales Engineer:** Molnár Dániel (E7-E8, talented, highest salary)

**Experienced:** Kovács Attila, Tornai Zsolt, Török Bálint

**Young Talents:** Vaida Márk-Ádám ⭐, Kovács Marcell, Pap Dávid, Gáll Botond

**Current Status:**
- ❌ Bakonyi Peti TÁVOZOTT (nárcisztikus viselkedés)
- ❌ Jankó-Király Attila TÁVOZOTT (not team fit)
- ✅ E9+ Architect joined (contractor)
- ✅ Molnár Dániel Sales Engineer
- Recruitment: ⏸️ Kulcsár Vencél & Csirak Raymond halasztva -- helyette 2x E1 junior a junior programból

## Services & Pricing

**Support Packages:**
- Safety Net: €990/m (6h, backup support)
- Essential: €2,000/m (40h)
- Growth: €4,000/m (80h)
- Scale: €6,000/m (120h)

**Add-ons:**
- 24/7 On-Call: €2,000/m
- Solution Architect: €1,000/m
- FinOps: €500/m
- DevSecOps: €700/m
- Extra hours: €70/h

## Customer Segments

1. Mid-sized enterprises (50-500 employees)
2. Startups & scale-ups (5-50 employees)
3. Large enterprises (500+)
4. Companies with existing DevOps teams

## Key Values in Action

**Proaktivitás:** Megelőzés, nem reagálás
**Tervezés:** Kétlépcsős teremtés - fejben majd valóságban
**Személyes kapcsolatok:** Bizalom = gyorsaság + alacsonyabb költség
**Nyertes-nyertes:** Mindkét félnek nyernie kell
**Alázat:** Nem tudunk mindent, szükség van egymásra

## Recruitment Context

**Értékelési szempontok:**
1. Alázat & professzionalizmus ⭐
2. Proaktivitás (nem reaktivitás)
3. Team fit & empátia
4. Technikai kompetencia
5. Önreflexió képessége
6. Nincs nárcisztikus jellemvonás

**Red flags (Bakonyi Peti példája):**
- Alapelvek megértésének hiánya
- Empátia hiánya
- Arrogancia ("mindent tud")
- Önreflexió hiánya
- Gázlángozás (realitás tagadása)
- Passzív agresszió
