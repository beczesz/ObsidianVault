---
title: "Personal Utils Plugin"
date: 2026-04-21
author: Becze Szabolcs
status: active
description: "Szabolcs' automation plugin for daily routines: morning briefing aggregating calendar and news, podcast monitoring with email categorization and YouTube stats tracking, and systematic Yahoo Mail cleanup with unsubscribe automation and state persistence."
description_source: auto
description_hash: 95c7c7b303ce1b71
id: bed95a60-3275-4bff-98f4-fc910a83db8d
index_schema_version: 1
bdos_index: true
---
# Personal Utils Plugin

Szabolcs személyes automatizmusai — napi rutinok, inbox kezelés, podcast monitoring.

## Commands

### 1. `/morning-v0.2` — Reggeli Briefing

Napi összefoglaló három lépésben:
1. Google Calendar események (Personal / Family / Work)
2. Hírösszefoglaló — prioritás témák (Irán, AI, Jordan Peterson) + általános (politika, piacok, Magyarország, Románia)
3. Wrap-up: nap sztorija + reflekciós kérdés

### 2. `/navigator-v0.1` — Navigátor Podcast Monitor

Két feladatot hajt végre:
1. Gmail inbox ellenőrzés (navigator.podc@gmail.com) — új emailek kategorizálása (személyes / automatikus / szponzorációs)
2. YouTube stats tracker — feliratkozók és nézettség követése konkurens csatornákkal együtt, delta-számítással

### 3. `/yahoo-v0.2` — Yahoo Mail Fésülés (Comb-through Cleanup)

Szisztematikus inbox takarítás a múlt felé haladva:
1. State fájlból betölti az utolsó feldolgozott dátumot
2. Napról napra visszafelé haladva átnézi az emaileket
3. Promóciós emaileknél: leíratkozás (unsubscribe link keresés + Chrome), majd az összes email törlése a küldőtől
4. Állapot mentése `yahoo-cleanup-state.md` fájlba — következő futás onnan folytatja
5. Briefing riport a futás végén

## State fájl

A Yahoo cleanup a haladási állapotot a plugin gyökerében tárolja:
`yahoo-cleanup-state.md` — markdown formátumban: haladás táblázat, ismert promóciós és biztonságos küldők listája, futási napló.

## Telepítés

Importáld a `personal-utils.plugin` fájlt a Cowork app Plugins menüjéből.

## Verziótörténet

- `0.2.0` — 2026-04-02: Yahoo cleanup v0.2 — teljes újraírás: dátum-alapú fésülés, unsubscribe link keresés, state file, lifetime stats
- `0.1.0` — 2026-04-02: Első kiadás (morning-v0.2, navigator-v0.1, yahoo-v0.1)
