---
title: TODAY - CPS Action Queue
description: "Live data source for a sales dashboard tracking daily outreach tasks, decisions, and pipeline actions. Includes task routing rules, date-based section matching, and tag priorities for a 90-day sales campaign."
description_source: auto
description_hash: 2f358a8833b9788c
last-updated: 2026-05-27
purpose: Single source for what needs action today. Read at every session start, update when work is done.
convention: Tasks use 📅 YYYY-MM-DD as due date. Mark done with [x] + ✅ YYYY-MM-DD done date. Each task links to (a) client account NOTES.md, (b) the prepared outreach message.
dashboard_contract: Sales/DASHBOARD_CONTRACT.md
dashboard_note: "Live source for the Today panel in Sales/dashboard.html. Day headers must include a date: `## Today: YYYY-MM-DD (Weekday)`. Subsection containing 'decisions needed' routes tasks to the Decisions column. Bold **CompanyName** in a task links it to the kanban card. Date marker here is the 📅 emoji, NOT @{} (that is Pipeline.md syntax)."
id: f4039d7a-4a98-4a18-8eee-634b6a6e5a4f
index_schema_version: 1
---
<!--
  ===========================================================================
  LIVE DATA SOURCE for Sales/dashboard.html. Polled every 8s.
  ===========================================================================
  This file feeds the "Today" panel at the top of the dashboard.

  DAY SECTION HEADER FORMAT (the date is REQUIRED, parser uses it to match):
      ## Today: 2026-05-13 (Wednesday)
      ## Tomorrow: 2026-05-14 (Thursday)
      ## Friday: 2026-05-16     <-- weekday + date also works

  Dashboard picks the section whose date matches the current system date,
  falls back to the next future date, then renders:
    - That section in the "Today" column
    - The next section in the "Tomorrow" column
    - Subsequent sections in the "Later this week" preview

  SUB-SECTION ROUTING:
      ### User decisions needed before tomorrow's sends
                       ^^^^^^^^^^^^^^^^^
      Any subsection name containing "decisions needed" routes its tasks
      to the Decisions column. Everything else goes to the Outreach column.

  TASK FORMAT:
      - [ ] **CompanyName** Free text 📅 2026-05-13 #tag [[wiki-link]]
  - Bold **CompanyName** links the task to a kanban card (click to open drawer).
  - Date marker in THIS file is 📅. (Pipeline.md uses @{}, do NOT swap.)
  - Tag chip priority: #decision, #followup, #lead, #milestone, #review,
    #drafting. First recognized wins.

  FULL CONTRACT: Sales/DASHBOARD_CONTRACT.md
  ===========================================================================
-->

# TODAY - CPS Action Queue

> Sales Engine clock: Day 9 of 90, reset 2026-05-11. Phase 1 ends 2026-06-07. Week 1 sends: 2 of 5. Week 2 day 1 sends: 2 (SEON Adam Berkecz InMail, CIG Attila Zankai InMail). Week 2 day 2 target: ABRIS InMail in the morning + decisions cleared on Pataki and KBOSS Day-5 nudge. Pipeline cleaned overnight: ABRIS new HOT, Cardinal Software new WARM monitor, 3 WARMs demoted to COLD, 2 COLDs cut to Lost. See `daily-brief-2026-05-18-azure-devops-hu.md` and `alternative-channels-2026-05-18.md`.

## Today: 2026-05-11 (Monday)

### Sales engine warm-up - first touch

- [x] **CIG Pannónia** -- send LinkedIn connect note to [Attila Zankai](https://www.linkedin.com/in/attila-zankai-358b9517) (Head of Information Technology). Hungarian, 150 chars. → [[Accounts/Leads/CIG_Pannonia/NOTES|account]] · [[Sales/Sales Enablement/outreach-batch-1-hot-leads|prepared connect note + post-accept DM (v2 #1 section)]] #lead #engine-warm-up 📅 2026-05-11 ✅ 2026-05-12

### User decisions needed before tomorrow's sends

- [ ] **Chemaxon language** -- HU (Hungarian HQ rule) or EN (international team, global pharma customers)? Affects v2 #2 outreach draft. → [[Sales/Sales Enablement/outreach-batch-1-hot-leads|v2 #2 context]] #decision 📅 2026-05-11
- [ ] **5th WARM slot** -- Perplexity HU SaaS deep-pass for fresh candidate, or promote one of Barion / Pentech / ABZ Innovation from COLD? → [[Sales/Pipeline|Pipeline]] 📅 2026-05-11 #decision

## Tomorrow: 2026-05-12 (Tuesday)

### HOT batch send (cohort 1)

- [ ] **Chemaxon** -- find VP Engineering / Head of Platform on LinkedIn, send LinkedIn connect (+email when known). → [[Sales/Sales Enablement/outreach-batch-1-hot-leads|prepared message v2 #2]] 📅 2026-05-12 #lead
- [ ] **SEON** -- find VP Engineering / Head of Platform / Director of Engineering on LinkedIn, send connect (EN). → [[Sales/Sales Enablement/outreach-batch-1-hot-leads|prepared message v2 #3]] 📅 2026-05-12 #lead
- [ ] **CIG Pannónia follow-up** -- if connect was accepted overnight, send LinkedIn DM with the full pitch. → [[Accounts/Leads/CIG_Pannonia/NOTES|account]] · [[Sales/Sales Enablement/outreach-batch-1-hot-leads|post-accept DM in v2 #1 section]] 📅 2026-05-12 #lead #followup

## Wednesday: 2026-05-13

### HOT batch send (cohort 2)

- [x] **KBOSS / Szamlazz.hu** -- find CTO / Head of Engineering on LinkedIn, send connect (HU). → [[Accounts/Leads/KBOSS_Szamlazz/NOTES|account]] · [[Sales/Sales Enablement/outreach-batch-1-hot-leads|prepared message v2 #4]] #lead 📅 2026-05-13 ✅ 2026-05-13
- [ ] **Colossyan** -- find CTO / VP Engineering on LinkedIn, send connect (EN). → [[Sales/Sales Enablement/outreach-batch-1-hot-leads|prepared message v2 #5]] 📅 2026-05-13 #lead
- [ ] **CIG Pannónia email fallback** -- if no LinkedIn acceptance by AM, send full email to attila.zankai@cig.eu. → [[Accounts/Leads/CIG_Pannonia/NOTES|account]] · [[Sales/Sales Enablement/outreach-batch-1-hot-leads|v2 #1 message body]] 📅 2026-05-13 #lead #followup

## Thursday: 2026-05-14

### WARM batch send (cohort 1) -- requires v2 drafts first

- [ ] **Draft 5 WARM messages** in `Sales/Sales Enablement/` before sending. Allonic (EN Profile 2 pitch), Lensa (HU latent need), Loxon (HU banking DORA), EOS Faktor (HU Otto Group gateway), 5th TBD. 📅 2026-05-14 #drafting
- [ ] **Allonic** -- find founder/CTO on LinkedIn, send connect (EN). Profile 2 scaling-company pitch. → [[Accounts/Leads/Allonic/NOTES|account]] 📅 2026-05-14 #lead
- [ ] **Lensa** -- find engineering lead on LinkedIn, send connect (HU). → [[Sales/Pipeline|Pipeline entry]] 📅 2026-05-14 #lead

## Friday: 2026-05-15

- [ ] **Loxon Solutions** -- LinkedIn connect (HU), banking + DORA angle. → [[Sales/Pipeline|Pipeline entry]] 📅 2026-05-15 #lead
- [ ] **EOS Faktor** -- LinkedIn connect (HU), Otto Group gateway angle. → [[Accounts/Leads/EOS_Faktor/NOTES|account]] 📅 2026-05-15 #lead
- [ ] **5th WARM** -- send once slot decision is made (see Monday decision queue). 📅 2026-05-15 #lead
- [ ] **CIG Day-5 nudge** -- if neither LinkedIn nor email reply, send short follow-up. → [[Accounts/Leads/CIG_Pannonia/NOTES|account]] 📅 2026-05-15 #followup
- [ ] **Milestone** -- all 9 viable HOT+WARM leads contacted by EOD. Update [[Sales/Pipeline|Pipeline]] (move cards to Contacted) and [[Sales/Dashboard|Dashboard]] W1 row. 📅 2026-05-15 #milestone

## Past: 2026-05-18 (Monday) -- Week 2 day 1 [CLOSED]

> **Honest state, revised 2026-05-18 AM.** Week 1 sent 2 of 5 target. Chemaxon WebFetch verification today found that chemaxon.com/careers 301-redirects to certara.com (acquired by Certara 2022) and the Budapest filter returns zero open roles. Chemaxon demoted from HOT to WARM. The 2026-05-11 Perplexity pass missed this redirect; the lead's Profile #1 thesis is broken until Budapest-team-autonomy is re-validated. SEON now occupies today's HOT slot.

### Backlog priority order (do in this sequence)

| # | Item | Cost | What it unblocks |
|---|------|------|------------------|
| 1 | Check CIG Pannonia LinkedIn status (Day 6 since send) | 2 min | Day-5 nudge vs Pataki secondary decision |
| 2 | Pick 5th WARM slot (Barion recommended) | 5 min | Friday WARM batch |
| 3 | Find SEON VP Eng / Head of Platform on LinkedIn, send v2 #3 (EN) | 15 min | First Week 2 send |
| 4 | Find Colossyan CTO / VP Eng on LinkedIn, send v2 #5 (EN) | 15 min | Second Week 2 send |
| 5 | Sales Navigator: build "Current campaign" Lead List with all 10 pipeline leads + enable job-change / post / news alerts | 20 min | Ongoing follow-up automation, parallel-threads problem solved |

If you complete #1 to #4 today, Week 2 is at 4 sends total (2 W1 + 2 W2) with three days still to run. Item #5 is SN onboarding, do AFTER the sends so it doesn't swallow the morning.

### Chemaxon postmortem (do NOT send today)

The original 2026-05-18 send to Chemaxon is cancelled. Pipeline card moved to WARM, NOTES.md updated with full WebFetch evidence. Action items for Chemaxon re-research are scheduled for 2026-05-22. The v2 #2 message in `outreach-batch-1-hot-leads.md` is now INVALID, do not send as-is.

### User decisions needed before tomorrow's sends

- [ ] **5th WARM slot** -- Perplexity HU SaaS deep-pass for a fresh candidate, OR promote Barion / Pentech / ABZ Innovation? **Recommendation: Barion.** Highest brand recognition among the COLDs, fintech aligns with SEON narrative, fastest path to a real conversation. Defer the deep-pass to Week 3. -> [[Sales/Pipeline|Pipeline]] #decision 📅 2026-05-18

### CIG Pannonia follow-up tree

- [x] **Check Attila Zankai LinkedIn status** -- Chrome MCP verified 2026-05-18: still 3rd-degree, connect not accepted, no reply, no pending indicator. 📅 2026-05-18 #check ✅ 2026-05-18
- [x] **Sales Navigator InMail to Attila Zankai** -- Option G HU sent direct with full pitch (DevOps mérnök pozíció: áthidaló javaslat). SN credit used. -> [[Accounts/Leads/CIG_Pannonia/NOTES]] 📅 2026-05-18 #lead ✅ 2026-05-18
- [x] **Verify Pataki current role at CIG** -- confirmed Head of IT Operations, 137 connections, low LinkedIn activity. 📅 2026-05-18 #check ✅ 2026-05-18
- [ ] **Decide Pataki Connect note (A/B/C) and send** -- 200-char HU connect note, options in [[Accounts/Leads/CIG_Pannonia/NOTES]]. 📅 2026-05-18 #decision #lead

### HOT batch carryover (target: send both by Tuesday)

- [x] **SEON** -- InMail (HU, Option F) sent to **Adam Berkecz** (VP Architecture, 2nd-degree, no warm path). SN-verified Senior SRE role + multi-stack match. Cold InMail. -> [[Accounts/Leads/SEON/NOTES]] 📅 2026-05-18 #lead ✅ 2026-05-18
- [ ] **Colossyan** -- find CTO / VP Engineering on LinkedIn, send v2 #5 (EN). -> [[Sales/Sales Enablement/outreach-batch-1-hot-leads|v2 #5]] 📅 2026-05-19 #lead
- [ ] **Chemaxon re-research** -- moved to 2026-05-22 (Thu) for Sales Navigator-driven Budapest-team-autonomy validation. See [[Accounts/Leads/Chemaxon/NOTES|Chemaxon NOTES]] action items. 📅 2026-05-22 #research

### Week 1 retrospective

What worked: KBOSS got sent on 2026-05-13 despite the cleanup work. Two real touches on the board. What missed: Chemaxon, SEON, Colossyan, and the entire WARM batch. Why: mid-week was dominated by sales-engine cleanup (leads.md, SCANNER_SCRIPT, dashboard contract, account NOTES). Cleanup was overdue and valuable, but it competed with sending and sending lost. **The 2026-04-27 review's exact diagnosis.**

**Rule for Week 2:** mornings = sending, afternoons = tooling. If no send is out by 11:00, the day's target slips. Cleanup work goes after the first send of the day, not before.

## Today: 2026-05-19 (Tuesday) -- Morning send: ABRIS

> **Reggeli prioritás: ABRIS.** Új HOT lead 2026-05-18 estéről. Banking IT vendor (Temenos T24), 142 emp, Budapest, fresh DevOps Fejlesztő posting (20+ órás), 4 applicant. Sonrisa MVMI + OKFO Azure DevOps references direkt matchelnek. Magyar nyelvű InMail.
>
> **15 perc protokoll**: read full JD (5 min) → SN search for ABRIS CTO / Head of Engineering (5 min) → finalize Option A draft (3 min) → send (2 min). Részletek és Option A draft: [[Accounts/Leads/ABRIS/NOTES]].

### Morning send (Week 2 day 2)

- [x] **ABRIS Kft.** -- Read full DevOps Fejlesztő JD (CRITICAL FINDING: AWS stack not Azure DevOps), SN search identified Zsolt Godry (Managing Director, 2nd-degree, 15+ yrs), warm intro path via Miklos Komjathi (Sonrisa colleague, 1 mutual connection). Teams request sent to Miklos 2026-05-19 for warm intro. Awaiting response. Option C forward-blurb (HU, AWS-anchored) ready in NOTES. -> [[Accounts/Leads/ABRIS/NOTES]] 📅 2026-05-19 #lead #morning ✅ 2026-05-19

### Stale decisions to clear (5 min total, blocks downstream)

- [x] **Pataki Connect note (Option B + value-prop close, 10-min CTA)** -- Sent 2026-05-19. As-sent text lifted as template T01 in `Sales/Sales Enablement/outreach-templates.md`. -> [[Accounts/Leads/CIG_Pannonia/NOTES]] 📅 2026-05-19 #decision #lead ✅ 2026-05-19
- [ ] **KBOSS Day-5 nudge decision** -- KBOSS connect 2026-05-13 küldve, 6 nap, nincs reply. Day-5 nudge typically ma esedékes. Opciók: (a) nudge most rövid HU InMail-lel ("nincs nyomás"), (b) várj Day-7-ig (2026-05-20). Ajánlás: (b), KBOSS-nál a tüzelést jól időzítenie kell mert nincs friss aktív DevOps posting (csak a thesis). 📅 2026-05-19 #decision #followup

### Sales Navigator setup (afternoon, 15-20 min)

- [ ] **Banking IT Vendor Cluster Lead List in SN** -- add 7 companies: ABRIS, Cardinal Software, Servera, AB-Soft, CompuTec, Pannon Business Solutions, Cinnamon, BANIF Investment. Enable alerts: new engineering hires, currently-hiring filter, leadership change, funding/M&A news. 📅 2026-05-19 #monitoring
- [ ] **Read alternative-channels research doc** -- [[Sales/Sales Enablement/Lead Scanner/alternative-channels-2026-05-18]]. Decide on Week 3 scrape strategy direction. 📅 2026-05-19 #strategy

### WARM drafting (afternoon if morning sends done, OR Wednesday morning)

- [ ] **Draft 2 WARM messages** in `Sales/Sales Enablement/` -- Allonic (EN Profile #2 scaling pitch) + Loxon (HU banking + DORA, depends on SN-verify the SysOps role still open). Lensa, EOS Faktor, Barion demoted to COLD overnight, not drafting these now. 📅 2026-05-19 #drafting

### Carryover from Monday

- [x] **SEON + CIG-Attila InMails** sent 2026-05-18 (both via SN InMail HU). ✅
- [ ] **Colossyan** -- PARKED (London-based CEO, wrong persona, no warm path). Skip outreach. SN Lead List monitor only. See [[Accounts/Leads/Colossyan/NOTES]].
- [ ] **Chemaxon re-research** -- moved to 2026-05-22 (Thu). See [[Accounts/Leads/Chemaxon/NOTES]] action items. 📅 2026-05-22 #research

## Wednesday: 2026-05-20

### Active WARM send (slimmer batch after overnight cleanup)

- [ ] **ABRIS / Miklos reminder** -- if Miklos has not reported back by EOD, send a friendly nudge on Teams to ask if intro to Zsolt happened. -> [[Accounts/Leads/ABRIS/NOTES]] 📅 2026-05-20 #followup
- [ ] **Allonic** -- LinkedIn connect (EN), Profile #2 scaling-startup pitch. -> [[Accounts/Leads/Allonic/NOTES|account]] 📅 2026-05-20 #lead
- [ ] **Loxon Solutions** -- LinkedIn connect (HU), banking + DORA angle (only if SN confirms SysOps role still open). 📅 2026-05-20 #lead
- [ ] **ABRIS Day-1 follow-up profile view** -- if InMail not replied, view ABRIS CTO profile to trigger notification. 📅 2026-05-20 #followup
- [ ] **Run Week 3 scrape preparation** -- read alternative-channels doc, decide between Sales Navigator deep dive (Tier 1) or Profession.hu scan (Tier 1) for the next discovery session. 📅 2026-05-20 #strategy

## Thursday: 2026-05-21

### Follow-ups + Chemaxon re-research

- [ ] **Chemaxon re-research** -- Sales Navigator validation of Budapest team autonomy post-Certara integration. See [[Accounts/Leads/Chemaxon/NOTES]] action items. 📅 2026-05-22 #research
- [ ] **SEON / CIG / ABRIS Day-3 profile-views** -- view CTO profiles to trigger notification. 📅 2026-05-21 #followup
- [ ] **Cardinal Software SN drilldown** -- save Cardinal Key People (CTO, COO) to "Banking IT Vendor Cluster" SN Lead List with alerts. 📅 2026-05-21 #monitoring

## Friday: 2026-05-22

### Week 2 close + first follow-up nudges + Week 3 scrape

- [ ] **SEON Day-4 / CIG Day-10 / KBOSS Day-9 follow-up nudges** if no replies. 📅 2026-05-22 #followup
- [ ] **Week 3 scrape run** -- per alternative-channels-2026-05-18.md recommended sequence: SN deep search (30 min) → Profession.hu manual scan (15 min) → MS Partner directory (10 min) → one new vertical Sonar query (~$0.025) → per-candidate parallel validation. Target: 2-3 new HOT + 5-8 new WARM. Budget: 90 min wall-time, ~$0.30 API cost. 📅 2026-05-22 #scrape
- [ ] **Week 2 review** -- count touches sent (target 10, realistic 5-7), replies, calls booked. Update [[Sales/Dashboard|Dashboard]] W2 row. 📅 2026-05-22 #review #milestone

## Today: 2026-05-27 (Wednesday) -- URGENT: Merkantil AID infra pricing call

> **Engine clock:** Day 17 of 90, Week 3. **NEW ACTIVE LEAD added today: Merkantil Bank Zrt.** -- multi-workstream Sonrisa engagement (active since 2026-04-27), CPS just plugged in for the AID infrastructure deployment pricing workstream. Email router + AI Enablement training proposals already SENT to Merkantil 2026-05-21 (by non-CPS Sonrisa units, validity 2026-05-31). CPS scope today: provide a defensible infra number for Miklós Nándor to send to Merkantil by EOD.
>
> Pre-call read order (15 min): [[Accounts/Leads/Merkantil/NOTES]] -> [[Accounts/Leads/Merkantil/source-docs/03-further-opportunities-outline|further-opportunities outline §6 AI-assisted SDLC]] -> [[Accounts/Leads/Merkantil/source-docs/04-teams-transcript-202604-202605|Teams transcript 2026-05-27 fragment]].

### URGENT (today, in this order)

- [ ] **Merkantil — pre-call prep** -- read NOTES.md, the AID workstream context, and the 2026-05-27 Teams transcript fragment. 15 min. -> [[Accounts/Leads/Merkantil/NOTES]] 📅 2026-05-27 #prep #urgent
- [ ] **Merkantil — Discovery call 12:00** -- with Bán József + Miklós Nándor + Becze Szabolcs (+ Ceclan Sanyi if joinable). Output: agreed CPS infrastructure deployment number (one-time setup + monthly managed service). Decision in-call, no "elvonulunk 1-2 napra" iteration (Miklós explicit constraint). 📅 2026-05-27 #meeting #urgent
- [ ] **Merkantil — number to Miklós** -- post-call, immediately, send the agreed figure(s) to Miklós Nándor so he can dispatch the offer to Merkantil by EOD. 📅 2026-05-27 #followup #urgent

### Post-call (this week)

- [ ] **Merkantil — formal CPS proposal section drafting** -- within 48h, write up the CPS infra scope formally for inclusion in the next Merkantil proposal iteration (or as a standalone CPS exec summary). -> [[Accounts/Leads/Merkantil/NOTES]] 📅 2026-05-29 #drafting
- [ ] **Merkantil — clarify Gábor's role/title** -- currently only first name + phone (+36 70 394 1260) known. Get last name and Merkantil-side role from Szacsúri László when he's back from OOO. 📅 2026-05-28 #research

### Carryover from earlier weeks (review only, decide which to action)

- [ ] **Loxon Solutions** -- live SysOps Engineer AWS Cloud posting (1 wk, actively reviewing) verified 2026-05-20. CTO Gábor Bicskei (25-yr veteran, 3rd-degree, cold, low LI activity). HU InMail draft ready in [[Accounts/Leads/Loxon_Solutions/NOTES]]. Decision (InMail vs free Connect) was paused for verify-before-send standing rule and Merkantil takes priority today. 📅 2026-05-27 #decision #lead
- [ ] **Allonic** -- PARKED 2026-05-20: zero active postings, no trigger. SN monitor only. No action. [[Accounts/Leads/Allonic/NOTES]]
- [ ] **ABRIS / Miklos warm intro** -- pending Miklos Komjathi response on the warm intro to Zsolt Godry. Check status. [[Accounts/Leads/ABRIS/NOTES]] 📅 2026-05-27 #followup
- [ ] **CIG Pannonia (Attila + Pataki)** -- Day-5 nudges due 2026-05-23 / 2026-05-24, those windows passed. Decide nudge vs. let-lie. [[Accounts/Leads/CIG_Pannonia/NOTES]] 📅 2026-05-27 #followup
- [ ] **SEON (Adam Berkecz)** -- Day-5 nudge due 2026-05-23, window passed. [[Accounts/Leads/SEON/NOTES]] 📅 2026-05-27 #followup
- [ ] **KBOSS** -- Day-7 nudge target was 2026-05-20, window passed. [[Accounts/Leads/KBOSS_Szamlazz/NOTES]] 📅 2026-05-27 #followup

## Active lead index (quick links)

| Lead | Stage | Lang | Send date | Account | Prepared message |
|------|-------|------|-----------|---------|------------------|
| **Merkantil Bank Zrt.** (TODAY 12:00) | Discovery | HU | 2026-05-27 | [[Accounts/Leads/Merkantil/NOTES]] | NOT outbound. Internal CPS infra-pricing call. Output: number to Miklós by EOD. |
| **ABRIS Kft.** (TUESDAY MORNING) | HOT | HU | 2026-05-19 | [[Accounts/Leads/ABRIS/NOTES]] | Option A v1 in NOTES, finalize after JD read |
| CIG Pannónia | Contacted | HU | 2026-05-12 ✅ | [[Accounts/Leads/CIG_Pannonia/NOTES]] | v2 #1 in [[Sales/Sales Enablement/outreach-batch-1-hot-leads]] |
| KBOSS / Szamlazz.hu | Contacted | HU | 2026-05-13 ✅ | [[Accounts/Leads/KBOSS_Szamlazz/NOTES]] | v2 #4 in [[Sales/Sales Enablement/outreach-batch-1-hot-leads]] |
| SEON | Contacted | HU | 2026-05-18 ✅ | [[Accounts/Leads/SEON/NOTES]] | Option F (HU) sent to Adam Berkecz via SN InMail |
| Chemaxon | WARM | TBD | re-research 2026-05-22 | [[Accounts/Leads/Chemaxon/NOTES]] | v2 #2 invalidated (Certara acquisition), Option B TBD |
| Colossyan | HOT | EN | 2026-05-19 | (NOTES TBD) | v2 #5 in [[Sales/Sales Enablement/outreach-batch-1-hot-leads]] |
| Allonic | WARM | EN | 2026-05-20 | [[Accounts/Leads/Allonic/NOTES]] | TBD (draft Tue) |
| Lensa | WARM | HU | 2026-05-20 | (NOTES TBD) | TBD |
| Loxon | WARM | HU | 2026-05-20 | (NOTES TBD) | TBD |
| EOS Faktor | WARM | HU | 2026-05-21 | [[Accounts/Leads/EOS_Faktor/NOTES]] | TBD |
| Barion (5th WARM) | WARM (proposed) | HU | 2026-05-21 | (NOTES TBD) | TBD |

## Live cross-vault query: open tasks with due dates

The Dataview query below pulls every open checkbox task across the whole CPS vault that carries a 📅 date marker, sorted alphabetically (which is also chronologically when dates are YYYY-MM-DD). Overdue tasks appear at the top.

```dataview
TASK
FROM ""
WHERE !completed AND contains(text, "📅")
SORT text ASC
```

## Conventions

- **Adding a task anywhere in the vault**: include `📅 YYYY-MM-DD` somewhere in the task line, and it will appear in the query above on or after that date.
- **Completing a task**: change `[ ]` to `[x]` and append `✅ YYYY-MM-DD` at the end of the line.
- **Linking the client**: use `[[Accounts/Leads/<Name>/NOTES|<Display>]]`.
- **Linking the prepared message**: use `[[Sales/Sales Enablement/outreach-batch-1-hot-leads|<section label>]]` since the v2 messages live in one file with `## v2 #N. <Company>` headings.

## Done log (latest first)

- 2026-05-19 morning: **Pataki Connect Request sent** (László Pataki, Head of IT Operations at CIG Pannónia, secondary contact). 252/300 char HU note: Option B + value-prop close ("Rendszerint olcsóbb...") + 10-min CTA. Free Connect (no SN credit, 3rd-degree via the "More" menu). Awaiting acceptance. As-sent text lifted as template **T01** in new `Sales/Sales Enablement/outreach-templates.md`. ✅
- 2026-05-19 morning: **ABRIS warm intro request** sent to Miklos Komjathi via Teams. Decision-maker target identified: Zsolt Godry (Managing Director, 2nd-degree, 15+ years at company = founder-level). JD verified: AWS stack (RDS/MSK/Lambda/PrivateLink/Databricks), not Azure DevOps as originally inferred. Option C forward-blurb prepared (HU, AWS-anchored). Awaiting Miklos response, then Miklos forwards to Zsolt. Cost so far: $0 (no SN credit used). ✅
- 2026-05-18 (evening, overnight session): **v0.9 scrape run** HU + Azure DevOps + mid-tier enterprise focus. Output: 1 verified HOT (ABRIS Kft, ~142 emp banking IT vendor, Temenos T24, Budapest, fresh DevOps Fejlesztő posting), 1 verified WARM (Cardinal Software, banking IT vendor 30 yrs, monitor-only), 6 banking-vendor cluster siblings parked for SN Lead List monitoring. Pipeline cleanup: 3 WARMs demoted to COLD (Lensa, EOS Faktor, Barion), 2 COLDs cut to Lost (Pentech, ABZ Innovation), 2 Romania COLDs marked off-scope. Daily brief + alternative-channels research docs written. Total API cost ~$0.15. ✅
- 2026-05-18: **CIG Pannonia** Sales Navigator InMail sent to Attila Zankai (Head of IT). Hungarian, ~140 words, Option G. Direct path after the 2026-05-12 connect note was not accepted in 6 days. Pataki current role verified pre-send, Konya parallel-role note added to NOTES.md. Dashboard W2 = 2, total = 4. ✅
- 2026-05-18: **SEON** Sales Navigator InMail sent to Adam Berkecz (VP Architecture). Hungarian, ~95 words, Option F. Senior SRE role verified live in SN before send (Budapest hybrid / Remote EU, reposted 2 days, 68 clicks, promoted). Cold path, no TeamLink overlap. First Week 2 touch. Dashboard W2 = 1, total = 3. ✅
- 2026-05-13: **KBOSS / Szamlazz.hu** LinkedIn connect sent (HU, v2 #4). Pipeline card moved to Contacted. Dashboard W1 = 2. Awaiting acceptance. ✅
- 2026-05-12: **CIG Pannónia** LinkedIn connect note sent to Attila Zankai (Head of IT). 150-char Hungarian teaser. First outreach of the new 90-day clock. Pipeline card moved to Contacted. Dashboard W1 = 1. Awaiting acceptance. ✅
