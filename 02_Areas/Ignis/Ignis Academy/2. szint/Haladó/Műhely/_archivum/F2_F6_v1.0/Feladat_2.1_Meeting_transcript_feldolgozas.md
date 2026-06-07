---
title: "F2.1 — Meeting transcript feldolgozása a Productivity pluginnel"
date: 2026-05-13
author: Becze Szabolcs
status: active
description: "Útmutató a Meeting Productivity pluginnel történő feldolgozásához: kaotikus meeting transcriptet strukturált TODO listává alakít át, amely session-ök között megmarad a rendszerben, ellentétben a ChatGPT-vel amely elfelejtené az információt."
description_source: auto
description_hash: 07c5c8708d08f929
id: d7c54d83-c524-42f2-bde3-327fdd1b64f2
index_schema_version: 1
bdos_index: true
---
# F2.1 — Meeting transcript feldolgozása a Productivity pluginnel

## Kontextus
Az F1-ben rendet raktunk a TransOffice fájljai között. De a fájlok csak a múlt — a napi működésben megbeszélések történnek, döntések születnek, feladatok osztódnak ki. És általában elfelejtődnek.

A csütörtöki pályázati tanácsadói meetingről kiderült: az AFM elektromos járműflotta-pályázat **már 2 hónapja a radarjuk alatt volt** (Márton dec. óta tudott róla), de senkinek nem volt rá ideje rendesen ránézni. Most viszont a forrás kifut: **vagy ezen a héten beadják, vagy lemaradnak**. Márton gyorsan összeült Enikővel — kaotikus meeting, sok kérdés, kevés válasz. Van egy nyers transcript — de abból nem derül ki ki mit csinál.

## A Productivity plugin
A Claude Cowork-ben van egy **Productivity plugin**, ami:
- Meeting jegyzeteket kezel
- TODO elemeket kinyeri és elmenti
- Feladatokat követ (ki, mit, mikorra, státusz)
- Session-ök között is megőrzi az állapotot

## Feladat
1. Aktiváld a Productivity plugint
2. Add be a meeting transcriptet (`meetings/meeting_transcript_20250224.md`)
3. Kérd meg a Claude-ot, hogy dolgozza fel:

```
Olvasd el ezt a meeting transcriptet. Ez egy sürgős megbeszélés volt egy EU pályázatról (elektromos autó flotta).

Kérek:
1. Helyzet összefoglaló (3-5 mondat)
2. TODO lista: Ki → Mit → Mikorra → Prioritás
3. Hiányzó információk (amik nélkül nem lehet pályázni)
4. Blokkolók: melyik TODO függ a másiktól

Mentsd el a TODO-kat a feladatkezelőbe.
```

## Tanulási pont
- A Productivity plugin nem csak listáz — **elmenti** a TODO-kat
- Következő session-ben is ott vannak a feladatok
- Ez a különbség a ChatGPT és a Cowork között: a ChatGPT elfelejti, a Cowork megjegyzi

## Checkpoint
**WOW:** Kaotikus transcript → strukturált TODO lista, ami MEGMARAD a rendszerben
**MICRO HANDS-ON:** Nyiss egy új session-t és kérdezd meg: "mik a nyitott feladataim?" — a Cowork tudni fogja
