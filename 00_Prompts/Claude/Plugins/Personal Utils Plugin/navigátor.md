---
title: "navigátor"
date: 2026-05-07
author: Becze Szabolcs
status: active
description: "Reggeli emailkezelési feladat a Navigátor Podcast Gmail fiókjához: olvasatlan levelek átnézése, kategorizálása és sürgős üzenetek kiemelése. Szponzorációs ajánlatok, vendégajánlások és egyéb megkeresések azonosítása."
description_source: auto
description_hash: 32e450dc85f449c1
id: 5610966a-f511-4752-a41f-ab52a430d07f
index_schema_version: 1
bdos_index: true
---
Ellenőrizd a Navigátor Podcast Gmail fiókját (navigator.podc@gmail.com) és foglald össze az összes olvasatlan emailt, kiemelve a figyelmet igénylőket.

## Lépések

1. Nézd át az ÖSSZES olvasatlan emailt, amire még nem válaszoltam: `gmail_search_messages` tool, query: `is:unread`, a navigator.podc@gmail.com fiókban (ez a 2-es indexű Gmail fiók a rendszerben). Minden emailről foglalj össze EGY MONDATBAN. **Bold-dal emeld ki**, ha valami sürgős vagy figyelmet igényel.

2. Értékeld az emaileket:

- Ha nincs olvasatlan email: írd, hogy "Ma reggel nincs olvasatlan email a Navigátor Podcast postaládájában."

- Ha van olvasatlan email: foglald össze tömören, minden emailnél: feladó, tárgy, és **egy mondatos** összefoglaló (bold-dal kiemelve, ha sürgős/actionable)

- Kategorizáld: személyes megkeresés / automatikus értesítés / szponzorációs ajánlat / egyéb

- Ha nincs semmi személyes vagy actionable: egy mondatban foglald össze ("Csak automatikus értesítések érkeztek.")

## Formátum

**Navigátor Podcast – Reggeli Email Összefoglaló**

Dátum: [mai dátum]

[Ha nincs olvasatlan email:]

Nincs olvasatlan email.

[Ha van olvasatlan email:]

📧 [Feladó] – [Tárgy]

→ [Egy mondatos összefoglaló + kategória: személyes / automatikus / szponzorációs] — **bold-olva, ha figyelmet igényel/sürgős**

[Ha csak automatikus/irreleváns:]

Összesítve: [X] automatikus értesítés érkezett, nincs személyes megkeresés.

[Mindig az alján egy soros összegzés:]

Összesen [X] olvasatlan · [N] figyelmet igényel · [Y] automatikus.

## Fontos szempontok

- A Navigátor Podcast egy magyar vállalkozói podcast (Szabolcs vezeti)

- Személyes megkeresésnek számít: vendégajánlás, hallgatói levél, együttműködési ajánlat egyéni feladótól, partnerségi kérés

- Automatikusnak számít: Patreon értesítők, Google alerts, Spotify processing, platform levelek

- **Bold-olt kiemelés**: sürgős vagy actionable üzenet (vendégajánlás, határidős kérdés, együttműködés, szponzorációs ajánlat, személyes válaszra váró megkeresés)

- Legyél tömör – ez egy reggeli briefing, nem részletes elemzés

## STEP 2 — YOUTUBE PODCAST STATS (Analytics MCP only)

A YouTube Data API kvótakorlát miatt CSAK az Analytics MCP-t használjuk. **Ne használj WebSearch-öt**, és **ne hívd a `youtube_get_channel` vagy `youtube_get_video` tool-okat** (ezek Data API kvótát fogyasztanak) — kizárólag Analytics tool-okat.

### Saját csatorna — Analytics összefoglaló

Hívd meg a `youtube_analytics_overview` tool-t (utolsó 7 nap). Jelenítsd meg:

- Views, Watch time, Átl. nézési idő, Új feliratkozók (nettó), Like-ok, Kommentek, Megosztások

### Top videók (utolsó 7 nap)

Hívd meg a `youtube_analytics_top_videos` tool-t az utolsó 7 napra, top 3 megtekintés szerint. Egy soros highlight mindegyikről (cím + megtekintés szám).
