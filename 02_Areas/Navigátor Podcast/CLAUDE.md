# Memory

## Me
Szabolcs (beczesz.szabolcs@gmail.com) — Navigátor Podcast alkotó és hosztja.
YouTube csatorna Brand Account a beczesz.szabolcs@gmail.com alatt. Podcast email: navigator.podc@gmail.com

## Projektek

| Név | Mi ez? |
|-----|--------|
| **Navigátor Podcast** | Magyar vállalkozói podcast mélyreható beszélgetésekkel. Cél: térképet és alapelveket találni egy változó világban vendégekkel együtt. |

## Értékek (Navigátor Podcast)

- **Éberség:** Jelenlét és figyelem a pillanatban
- **Harmadik út keresése:** Kollektív gondolkodás, új megértés keresése
- **Bátorság és alázat:** Határok elfogadása + merészség az alapelvek alkalmazásában
- **Integritás:** Ígéretek megtartása, következetesség

## Misszió elemei

- **Párbeszéd:** Nyitott, alázatos hozzáállás
- **Keresés:** Kíváncsiság, lelki szegénység vezérli
- **Megújulás:** Folyamatos alkalmazkodás és tanulás

## YouTube Stratégia

**Célközönség:** 35-64 éves magyar nők és férfiak (89.6% 35+, 53% nő), akiket az egészség, pszichológia, család, önfejlesztés és erdélyi/székely témák érdekelnek. Erdély a 2. legnagyobb közönség (16%). Formátum: 60-120+ perces mélyinterjúk.

**Formátumok:**
- Cím: `"Idézet" – Téma | Vendég | EP[szám]`
- Thumbnail: Max 3-4 szó, provokatív/kérdő
- Leírás: Hook → Kontextus → Összefoglaló + Hashtagek
- Időkódok: 10-12 kulcspillanat

**Állandó hashtagek:** #NavigátorPodcast #MagyarPodcast

## Eszközök

**Plugin commands:**
- `/hook` — Cold Open javaslatok SRT-ből
- `/cim` — YouTube címek generálása
- `/thumbnail` — Thumbnail szövegek
- `/leiras` — SEO leírás + hashtagek
- `/idokod` — Időkódok generálása

**YouTube MCP (40 tool — pauling-ai/youtube-mcp-server):**
- Analytics: `youtube_analytics_overview`, `_top_videos`, `_demographics`, `_geography`, `_traffic_sources`, `_retention`, `_daily`, `_day_of_week`, `_content_type_breakdown`
- Videó: `youtube_get_video`, `youtube_list_videos`, `youtube_update_video`, `youtube_get_transcript`
- Csatorna: `youtube_get_channel` (saját + versenytárs)
- SEO: `youtube_search`, `youtube_search_suggestions`, `youtube_trending`
- Kommentek: `youtube_list_comments`, `youtube_post_comment`, `youtube_reply_to_comment`
- Playlist: `youtube_list_playlists`, `youtube_create_playlist`, `youtube_add_to_playlist`
- Publikálás: `youtube_upload_video`, `youtube_set_thumbnail`
- Reporting: `youtube_reporting_*` (bulk CSV riportok)

**Google Cloud projekt:** Navigator YouTube MCP v2 (navigator-youtube-mcp-v2, beczesz.szabolcs@gmail.com)
**OAuth:** Brand Account (Navigátor Podcast) a beczesz.szabolcs@gmail.com fiók alatt

## ⚠️ YouTube API Státusz (2026-04-08)

**YouTube Data API v3:** ❌ NEM MŰKÖDIK — Google 0 kvótát allokál új projekteknek is (audit nélkül)
- A Console 10,000 queries/day-t mutat, de a tényleges allokáció 0
- Érintett tool-ok: `youtube_get_video`, `youtube_list_videos`, `youtube_update_video`, `youtube_get_channel`, `youtube_search`, playlist és komment tool-ok
- Audit form kitöltve, Google screen recording-ot kért → nem reális személyes használatra

**YouTube Analytics API:** ✅ MŰKÖDIK — teljes hozzáférés
- Működő tool-ok: `youtube_analytics_overview`, `_top_videos`, `_demographics`, `_geography`, `_traffic_sources`, `_retention`, `_daily`, `_day_of_week`, `_content_type_breakdown`, `_revenue`, `_video_detail`

**YouTube Reporting API:** ✅ Engedélyezve (bulk CSV)

**Workaround írás műveletekhez:** Chrome MCP → YouTube Studio böngészőautomatizálás

## Linkek

- [Google Drive mappa](https://drive.google.com/drive/u/0/folders/1Ou69cPqw3i8vfDp_Q_jvPjb8F5KjbFeI)
- Social Blade stats összehasonlítás

## Fontos fájlok

> ⚠️ Az alábbi Synthesis/ fájlok egy korábbi session-ben jöttek létre, de nem mindegyik létezik a jelenlegi mappában. Újragenerálhatóak igény szerint.

| Fájl | Leírás | Státusz |
|------|--------|---------|
| `Synthesis/new_video_checklist.md` | Új videó publikálási checklist — 5 fázis | ❌ Újragenerálandó |
| `Synthesis/plan.md` | Master tracking — audit fázisok és haladás | ❌ Újragenerálandó |
| `Synthesis/end_screen_plan.md` | End screen terv minden videóra | ❌ Újragenerálandó |
| `Synthesis/channel.md` | Csatorna-intelligencia, traffic source adatok | ❌ Újragenerálandó |
| `Synthesis/cards_and_pinned_comments_plan.md` | Cards és Pinned Comment terv (62 videó) — ✅ Pinned Comments 100% DONE | ❌ Újragenerálandó |
| `Synthesis/synthesis_map.md` | Összes videó referencia térkép | ❌ Újragenerálandó |
| `Synthesis/Csakabaj/synthesis_map.md` | Csakabaj 51 epizód referencia térkép (PopScore + HostScore) | ✅ Létezik |
| `WP41_Fegyelem_YouTube_Metadata.md` | EP41 teljes metadata csomag (címek, hookek, thumbnailek, leírás) | Session-ben volt |

## Epizód állapot

| EP | Cím/Téma | Vendég | Státusz | Video ID |
|----|----------|--------|---------|----------|
| EP40 | Fegyelmezés | Gál Ildikó | ✅ Publikálva (2026-04-10) | — |
| EP41 | Fegyelem | Gergely István | ✅ Publikálva (2026-04-20) | ncHyEJD6yaM |
| EP42 | MMA | — | 🟡 SRT kész, feldolgozásra vár | — |
| EP43 | AI képzés | — | 🟡 Soron következő | — |
| EP44 | Gyász | — | 📋 Tervezett | — |
| EP45 | Agrárdigitalizáció | — | 📋 Tervezett | — |

## Folyamatban lévő

- ~~Intro az örökbe fogadós résznél~~ (lejárt/elengedve)
- Csatorna audit végrehajtása (Fázis 4a folyamatban)
- YouTube MCP integráció — Analytics működik, Data API kvóta 0
- navigator-v0.1 scheduled task frissítése YouTube MCP tool-okra
- ~~EP számozás korrekció~~ ✅ (EP39=Eberlein Éva, EP40=Fegyelmezés/Gál Ildikó, EP41=Fegyelem/Gergely István, EP42=MMA, EP43=AI képzés, EP44=Gyász [tervezett], EP45=Agrárdigitalizáció [tervezett])
- ~~Fegyelmezés epizód (EP40)~~ ✅ Publikálva (2026-04-10), teljes launch kész (pinned comment, 2 cards, end screen, FB poszt)
- ~~Fegyelem epizód (EP41)~~ ✅ Publikálva (2026-04-20), teljes launch kész (cím, leírás, tagek, end screen, 2 playlist, 1 card @ 30:00)
- **EP42 (MMA):** Következő publikálásra váró epizód — SRT elérhető
- **EP43 (AI képzés):** Soron következő epizód
- **EP44 (Gyász):** Tervezett epizód
- **EP45 (Agrárdigitalizáció):** Tervezett epizód
- 6 tematikus playlist + Created playlists szekció megjelenítve a csatorna főoldalán (2026-04-11)
- **Fázis 4a aktív feladatok:** ✅ 15/15 cím+leírás kész! ✅ 62/62 Pinned Comments kész! Hátra: Cards (TOP 10 → összes). ✅ Channel layout kész (2026-04-11)
- **Pinned Comments (2026-04-09):** ✅ 62/62 videón pinned cross-link komment — 100% COMPLETE! (@NavigatorPodcast Brand Account-ról)
- **End screen audit eredmény (2026-04-08):** TOP 10 mind ✅, de end screenek alacsony hatékonyságúak hosszú videóknál (10-15% retention a végén) → Cards prioritás
- **Új videó checklist kész:** `Synthesis/new_video_checklist.md` — minden új epizód publikálásnál ezt követni
- **Snapshot rendszer aktív:** Heti KPI snapshot, baseline: 2026-04-09. Következő snapshot esedékes. Trigger: "csináld meg a heti snapshot-ot"
