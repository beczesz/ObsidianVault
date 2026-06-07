---
schema: presto.seed.v2
seed_id: seed-20260526-spotify-archive-launch
id: 2c687185-0853-4656-a555-afef6d02d040
index_schema_version: 1
bdos_index: true
title: "Spotify archive launch — 17 missing + 4 date-fix"
short_description: "21 Spotify-publikáció: 17 archív EP heti 1 csütörtökökön (views-priority), 4 date-fix EP a hétvégén. Time-range: 2026-05-28 — 2026-09-17."

runbook_ref: null
campaign_ref: null

area: Navigátor Podcast
source: campaign-launch
source_type: other
source_ref: "[[02_Areas/Navigátor Podcast/Spotify_Master_Plan.md]]"
captured_at: 2026-05-26T00:00+02:00
captured_by: Becze Szabolcs

status: in_prep
exhausted_at: null

channels: [spotify]

prerequisites:
  - id: prereq-001
    description: "MP3 audio fájlok exportálva mind a 17 + 4 EP-hez (YouTube → MP3 vagy eredeti felvétel-fájlból). Forrás-meghatározás user-döntés."
    status: pending
    owner: user
    due_date: 2026-05-28
    notes: "Master Plan §3: 'a felhasználó biztosítja'. Pontos workflow TBD."

distribution_timeline:
  - step: "T+0 (Thu Week 1)"
    date: 2026-05-28
    channels: [spotify]
    pub_type: archive_upload
    notes: "EP36 Both Richárd (18 395 views) — első archív upload"
  - step: "T+3 (Fri date-fix batch)"
    date: 2026-05-29
    channels: [spotify]
    pub_type: date_fix
    notes: "EP38 + EP39 dátum-javítás (Spotify for Creators)"
  - step: "T+4 (Sat date-fix batch)"
    date: 2026-05-30
    channels: [spotify]
    pub_type: date_fix
    notes: "EP41 + EP42 dátum-javítás"
  - step: "Week 2"
    date: 2026-06-04
    channels: [spotify]
    pub_type: archive_upload
    notes: "EP37 Brutbányai-Elekes (6 363 views)"
  - step: "Week 3"
    date: 2026-06-11
    channels: [spotify]
    pub_type: archive_upload
    notes: "EP21 Szakács-Paál István (4 231 views)"
  - step: "Week 4"
    date: 2026-06-18
    channels: [spotify]
    pub_type: archive_upload
    notes: "EP18 Lázár-Szilágyi-Balázs (2 524 views)"
  - step: "Week 5"
    date: 2026-06-25
    channels: [spotify]
    pub_type: archive_upload
    notes: "EP35 Láng Máté (2 491 views)"
  - step: "Week 6"
    date: 2026-07-02
    channels: [spotify]
    pub_type: archive_upload
    notes: "EP15 Szabó W. Péter (1 900 views)"
  - step: "Week 7"
    date: 2026-07-09
    channels: [spotify]
    pub_type: archive_upload
    notes: "EP27 Tamás Barna atya (1 782 views)"
  - step: "Week 8"
    date: 2026-07-16
    channels: [spotify]
    pub_type: archive_upload
    notes: "EP22 Tódor Botond (1 635 views)"
  - step: "Week 9"
    date: 2026-07-23
    channels: [spotify]
    pub_type: archive_upload
    notes: "EP20 Gábor Attila (1 626 views)"
  - step: "Week 10"
    date: 2026-07-30
    channels: [spotify]
    pub_type: archive_upload
    notes: "EP26 Balázs-Zoltáni (1 578 views)"
  - step: "Week 11"
    date: 2026-08-06
    channels: [spotify]
    pub_type: archive_upload
    notes: "EP23 Hátszegi Zsolt (1 440 views)"
  - step: "Week 12"
    date: 2026-08-13
    channels: [spotify]
    pub_type: archive_upload
    notes: "EP40 Gál Ildikó (1 200 views)"
  - step: "Week 13"
    date: 2026-08-20
    channels: [spotify]
    pub_type: archive_upload
    notes: "EP12 Bándi Domokos (889 views)"
  - step: "Week 14"
    date: 2026-08-27
    channels: [spotify]
    pub_type: archive_upload
    notes: "EP13 Józsa Levente (745 views)"
  - step: "Week 15"
    date: 2026-09-03
    channels: [spotify]
    pub_type: archive_upload
    notes: "EP24 Faragó-Fodor (555 views)"
  - step: "Week 16"
    date: 2026-09-10
    channels: [spotify]
    pub_type: archive_upload
    notes: "EP25 Albert Orsolya (495 views)"
  - step: "Week 17"
    date: 2026-09-17
    channels: [spotify]
    pub_type: archive_upload
    notes: "EP34 Süket Csaba (327 views) — utolsó archív upload"

publications_spawned:
  - pub_id: pub-spotify-2026-05-28-001
    date: 2026-05-28
    ep: EP36
  - pub_id: pub-spotify-2026-05-29-001
    date: 2026-05-29
    ep: EP38
  - pub_id: pub-spotify-2026-05-29-002
    date: 2026-05-29
    ep: EP39
  - pub_id: pub-spotify-2026-05-30-001
    date: 2026-05-30
    ep: EP41
  - pub_id: pub-spotify-2026-05-30-002
    date: 2026-05-30
    ep: EP42
  - pub_id: pub-spotify-2026-06-04-001
    date: 2026-06-04
    ep: EP37
  - pub_id: pub-spotify-2026-06-11-001
    date: 2026-06-11
    ep: EP21
  - pub_id: pub-spotify-2026-06-18-001
    date: 2026-06-18
    ep: EP18
  - pub_id: pub-spotify-2026-06-25-001
    date: 2026-06-25
    ep: EP35
  - pub_id: pub-spotify-2026-07-02-001
    date: 2026-07-02
    ep: EP15
  - pub_id: pub-spotify-2026-07-09-001
    date: 2026-07-09
    ep: EP27
  - pub_id: pub-spotify-2026-07-16-001
    date: 2026-07-16
    ep: EP22
  - pub_id: pub-spotify-2026-07-23-001
    date: 2026-07-23
    ep: EP20
  - pub_id: pub-spotify-2026-07-30-001
    date: 2026-07-30
    ep: EP26
  - pub_id: pub-spotify-2026-08-06-001
    date: 2026-08-06
    ep: EP23
  - pub_id: pub-spotify-2026-08-13-001
    date: 2026-08-13
    ep: EP40
  - pub_id: pub-spotify-2026-08-20-001
    date: 2026-08-20
    ep: EP12
  - pub_id: pub-spotify-2026-08-27-001
    date: 2026-08-27
    ep: EP13
  - pub_id: pub-spotify-2026-09-03-001
    date: 2026-09-03
    ep: EP24
  - pub_id: pub-spotify-2026-09-10-001
    date: 2026-09-10
    ep: EP25
  - pub_id: pub-spotify-2026-09-17-001
    date: 2026-09-17
    ep: EP34

tags: [navigator-podcast, spotify, archive, heti-1, campaign-launch, multi-week]
description: "Spotify archív launch seed: 17 hiányzó EP heti 1 csütörtökönként (views-priority sorrend), + 4 date-fix EP a hétvégén (2026-05-29–30). Teljes időtartam: 2026-05-28 — 2026-09-17. Prereq: MP3 exportok."
---

## Raw content

Forrás: [[02_Areas/Navigátor Podcast/Spotify_Master_Plan.md]]

A Navigátor Podcast Spotify-on 17 archív epizód hiányzik (EP12, EP13, EP15, EP18, EP20, EP21, EP22, EP23, EP24, EP25, EP26, EP27, EP34, EP35, EP36, EP37, EP40). Ezeket heti 1 csütörtöki ütemezéssel, views-priority sorrendben kell feltölteni — a legnézettebb EP kerül először Spotify-ra.

Emellett 4 meglévő EP dátuma hibás (EP38, EP39, EP41, EP42 — mind 2026-05-20-ra van beállítva, holott a helyes YouTube-dátumok 2026-02-17 és 2026-05-04 között szóródnak). Ezeket az első hétvégén (2026-05-29 péntek + 2026-05-30 szombat) kell javítani.

**Sorrend-logika (views-priority):**
A Spotify legelső archiválásoknál a legnézettebb epizódok adnak legnagyobb esélyt a discovery-re, hiszen egy visszadatált epizód nem küld push-notifikációt — csak a teljes katalógus completeness és az organikus keresés hozza a hallgatókat.

## Distribution plan

| # | Pub-id | Dátum | EP | Típus | Vendég |
|---|---|---|---|---|---|
| 1 | pub-spotify-2026-05-28-001 | 2026-05-28 (csüt) | EP36 | archive_upload | Both Richárd |
| 2 | pub-spotify-2026-05-29-001 | 2026-05-29 (pén) | EP38 | date_fix | Gál Ildikó |
| 3 | pub-spotify-2026-05-29-002 | 2026-05-29 (pén) | EP39 | date_fix | Eberlein Éva |
| 4 | pub-spotify-2026-05-30-001 | 2026-05-30 (szo) | EP41 | date_fix | Gergely István |
| 5 | pub-spotify-2026-05-30-002 | 2026-05-30 (szo) | EP42 | date_fix | Yda Gabi & Kovács |
| 6 | pub-spotify-2026-06-04-001 | 2026-06-04 (csüt) | EP37 | archive_upload | Brutbányai-Elekes |
| 7 | pub-spotify-2026-06-11-001 | 2026-06-11 (csüt) | EP21 | archive_upload | Szakács-Paál István |
| 8 | pub-spotify-2026-06-18-001 | 2026-06-18 (csüt) | EP18 | archive_upload | Lázár-Szilágyi-Balázs |
| 9 | pub-spotify-2026-06-25-001 | 2026-06-25 (csüt) | EP35 | archive_upload | Láng Máté |
| 10 | pub-spotify-2026-07-02-001 | 2026-07-02 (csüt) | EP15 | archive_upload | Szabó W. Péter |
| 11 | pub-spotify-2026-07-09-001 | 2026-07-09 (csüt) | EP27 | archive_upload | Tamás Barna atya |
| 12 | pub-spotify-2026-07-16-001 | 2026-07-16 (csüt) | EP22 | archive_upload | Tódor Botond |
| 13 | pub-spotify-2026-07-23-001 | 2026-07-23 (csüt) | EP20 | archive_upload | Gábor Attila |
| 14 | pub-spotify-2026-07-30-001 | 2026-07-30 (csüt) | EP26 | archive_upload | Balázs-Zoltáni |
| 15 | pub-spotify-2026-08-06-001 | 2026-08-06 (csüt) | EP23 | archive_upload | Hátszegi Zsolt |
| 16 | pub-spotify-2026-08-13-001 | 2026-08-13 (csüt) | EP40 | archive_upload | Gál Ildikó |
| 17 | pub-spotify-2026-08-20-001 | 2026-08-20 (csüt) | EP12 | archive_upload | Bándi Domokos |
| 18 | pub-spotify-2026-08-27-001 | 2026-08-27 (csüt) | EP13 | archive_upload | Józsa Levente |
| 19 | pub-spotify-2026-09-03-001 | 2026-09-03 (csüt) | EP24 | archive_upload | Faragó-Fodor |
| 20 | pub-spotify-2026-09-10-001 | 2026-09-10 (csüt) | EP25 | archive_upload | Albert Orsolya |
| 21 | pub-spotify-2026-09-17-001 | 2026-09-17 (csüt) | EP34 | archive_upload | Süket Csaba |

## Suggested next steps

Első Spotify upload előkészítéséhez:
`/pres-prepare pub:pub-spotify-2026-05-28-001`

MP3 export workflow eldöntése (prereq-001 lezárásához) — user-döntés szükséges:
- YouTube videóból → MP3 letöltő eszköz
- Eredeti felvétel-fájlból (ha elérhető)

## Notes

**Navigator-Spotify DNA:** TBD — az első upload tapasztalatai (audio minőség, leírás-format, thumbnail megjelenés Spotify-on) után érdemes elkészíteni a `ChannelDNA/spotify.md` fájlt a Navigátor Podcast Marketing-ben.

**Backdating viselkedés:** visszadatált Spotify epizód NEM küld push-notifikációt. Ez az archív feltöltések inherens korlátja — csak a katalógus teljessége és az organikus kereshetőség a cél.

**Spotify show ID:** 6ONULNIDrswuqNitEAApwO
