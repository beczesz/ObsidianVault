---
name: navigator-v0.1
description: Navigátor Podcast reggeli email összefoglaló (Gmail) és YouTube stats tracker. Scheduled task or on-demand command.
version: 0.1
date: 2026-04-02
author: Becze Szabolcs
allowed-tools: WebSearch, WebFetch, TodoWrite
id: b8cdde03-1353-4a2a-9a3b-642f4c0a0b3d
index_schema_version: 1
---

Ellenőrizd a Navigátor Podcast Gmail fiókját (navigator.podc@gmail.com) és foglald össze a tegnap érkezett új emaileket.

## Lépések

1. Keresd az elmúlt 24 órában érkezett emaileket a Gmail MCP eszközzel: `gmail_search_messages` tool-lal, query: `newer_than:1d`, a navigator.podc@gmail.com fiókban (ez a 2-es indexű Gmail fiók a rendszerben).

2. Értékeld az emaileket:

- Ha nincs új email: írd, hogy "Ma reggel nincs új email a Navigátor Podcast postaládájában."

- Ha van új email: foglald össze tömören, minden emailnél: feladó, tárgy, és 1-2 mondatos összefoglaló

- Kategorizáld: személyes megkeresés / automatikus értesítés / szponzorációs ajánlat / egyéb

- Ha nincs semmi személyes vagy actionable: egy mondatban foglald össze ("Csak automatikus értesítések érkeztek.")

## Formátum

**Navigátor Podcast – Reggeli Email Összefoglaló**

Dátum: [mai dátum]

[Ha nincs email:]

Nincs új email.

[Ha van email:]

📧 [Feladó] – [Tárgy]

→ [1-2 mondatos összefoglaló + kategória: személyes / automatikus / szponzorációs]

[Ha csak automatikus/irreleváns:]

Összesítve: [X] automatikus értesítés érkezett, nincs személyes megkeresés.

## Fontos szempontok

- A Navigátor Podcast egy magyar vállalkozói podcast (Szabolcs vezeti)

- Személyes megkeresésnek számít: vendégajánlás, hallgatói levél, együttműködési ajánlat egyéni feladótól, partnerségi kérés

- Automatikusnak számít: Patreon értesítők, Google alerts, Spotify processing, platform levelek

- Legyél tömör – ez egy reggeli briefing, nem részletes elemzés

## STEP 2 — YOUTUBE PODCAST STATS

Fetch current stats using YouTube tools. Show a table: Channel/Video | Last Recorded | Today | Δ. Delta as +N or -N, or — if unchanged.

**Channels — subscriber count:**

- @NavigatorPodcast (Navigátor Podcast)

- @csakabaj.podcast (Csakabaj Podcast)

- @Koffer-x1b (Koffer)

- @RMÜE-e9i (RMÜE MásHOGYoszkóp)

**Videos — view count:**

- Video ID: PG8etGmSLtU (Koffer #12 – Emberi felelősség & AI)

**Last recorded values** (updated automatically after each run):

- Navigátor Podcast subs: 5740

- Csakabaj Podcast subs: 5490

- Koffer subs: 208

- RMÜE MásHOGYoszkóp subs: 43

- Koffer #12 views: 929

---

## STEP 3 — SELF-UPDATE (silent, after displaying the briefing)

Call `update_scheduled_task` with taskId `navigator-reggeli-email-osszefoglalas`. In the updated prompt, replace the numeric values in the "Last recorded values" block with today's freshly fetched YouTube numbers. Change nothing else.
