---
title: "(Bónusz) Feladat 1.4 — Ügyfélkép egységesítés"
date: 2026-05-14
author: Becze Szabolcs
status: active
description: "Gyakorlati feladat a Claude felhasználásával három ügyféllistát egyesíteni egyetlen master adatbázisba, duplikációk feloldásával, eltérések jelölésével és golden record kialakításával. Adategyesítési és adattisztítási technikákat tanít meg."
description_source: auto
description_hash: ab45fa99920a5cff
id: 5acaeb38-222f-4770-af3b-ac03d359d1b1
index_schema_version: 1
bdos_index: true
---
# (Bónusz) Feladat 1.4 — Ügyfélkép egységesítés

## Szituáció

Márton megkérdezi:

> "Hány ügyfelünk van tulajdonképpen? Anyám listáján 40, a másikon 28, én meg elkezdtem egyet amiben 8 van. Fogalmam sincs ki aktív és ki nem. Össze tudnád rakni egyetlen listába?"

3 különböző Excel, 3 különböző formátum, 3 különböző korszak. Kézzel ez fél nap. AI-val? Nézzük.

## Feladat

Kérd meg a Claude-ot hogy:
1. Olvassa be mindhárom ügyféllistát (`ugyfelek_2019.xlsx`, `ugyfelek_VEGLEGES.xlsx`, `ugyfelek_uj_marton.xlsx`)
2. Egyesítse őket egyetlen, tiszta adatbázisba
3. Jelölje meg ahol eltérés van (pl. névváltozat, hiányzó adat, duplikáció)
4. Javasoljon egy "golden record"-ot minden ügyfélhez (= a legfrissebb/legteljesebb adat)

### Javasolt prompt:

> "Olvasd be mindhárom ügyfél-Excelt. Készíts egy egységes master listát az alábbi oszlopokkal: Cégnév (hivatalos), Kapcsolattartó, Telefon, Email, Település, Kedvezmény %, Státusz (aktív/inaktív/kérdéses), Utolsó rendelés, Forrás (melyik fájlokból jön). Ha egy ügyfél több fájlban is szerepel, egyesítsd a legfrissebb/legteljesebb adattal. Jelöld pirossal ahol eltérés van a források között."

## Elvárt kimenet

Egy `ugyfelek_MASTER.xlsx` ami:
- Tartalmazza az összes egyedi ügyfelet (deduplikálva)
- Oszlopok: Cégnév | Kapcsolattartó | Telefon | Email | Település | Kedvezmény | Státusz | Utolsó rendelés | Forrás | Megjegyzés
- Jelzi melyik forrásból jön az adat
- Megjelöli pirossal a kérdéses tételeket
- Tartalmaz egy "Kérdéses" fület a nem egyértelmű esetekkel

## Extra kihívás

Ha elkészült a master lista, kérdezd meg a Claude-ot:
> "Ebből a listából melyek a top 10 ügyfelek árbevétel szerint? Van-e olyan ügyfél aki régóta nem rendelt (>6 hónap)? Ki az akit érdemes lenne visszahívni?"

## Tanulás

- **Data reconciliation** — több forrás összefésülése → amit kézzel órákig csinálnál
- **Golden record** koncepció — adatbázis-kezelés alapja
- Az AI nem csak összefűz, hanem **értelmez** (névváltozat felismerés, duplikáció detektálás)
- Gyakorlati Excel-generálás: a Cowork képes .xlsx fájlt létrehozni formázással együtt
