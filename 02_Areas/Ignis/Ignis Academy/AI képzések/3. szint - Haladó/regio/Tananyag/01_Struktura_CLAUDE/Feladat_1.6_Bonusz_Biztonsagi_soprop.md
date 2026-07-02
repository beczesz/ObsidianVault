---
title: "Feladat 1.6 (Bónusz): Biztonsági söprés, érzékeny adat minden projektben"
date: 2026-07-02
author: Becze Szabolcs
status: active
description: "F1 otthoni bónusz: a résztvevő az AI-val átsöpörteti mind a három RegioConsult projektet érzékeny, rosszul tárolt adat után (jelszavak, PIN, banki vagy platform-hozzáférés), és kap egy biztonsági riportot: hol, mi, és mi a teendő. A jelszavak.txt a Napsugárban a fő találat. Az AI nem törli, csak jelez, mert az érzékeny adattal ember dönt."
id: a071e246-8e15-4f96-9d6a-4c5f3e7d2b08
index_schema_version: 1
bdos_index: true
tags: [ignis-academy, halado, regio-consult, f1, bonusz, biztonsag]
---
# Feladat 1.6 (Bónusz): Biztonsági söprés

> **Típus:** otthoni gyakorlat · **Minőségbiztosítás a biztonságra**

## Cél
Az 1.1 auditban felbukkant a `jelszavak.txt`. De vajon csak ott van érzékeny adat? Amikor 3 iroda, 21 ember dolgozik, könnyen becsúszik egy jelszó egy sima szöveges fájlba. Söpörjük át az egészet.

## Feladat
```
Söpörd át mind a három RegioConsult projektet érzékeny, rosszul tárolt adat után:
jelszó, PIN, banki vagy platform-hozzáférés (e-licitatie, SEAP, email), személyes
azonosító. Adj egy biztonsági riportot: melyik projektben, melyik fájlban, milyen
típusú érzékeny adat, és mi a javasolt teendő.
NE töröld és NE oszd meg a talált adatokat, csak jelezd a helyüket és a kockázatot.
Az érzékeny adattal ember dönt.
```

## Elvárt eredmény
Egy biztonsági riport, aminek a fő találata a Napsugár `jelszavak.txt`-je (e-licitatie / SEAP / email / banki PIN). A javaslat: átvinni jelszókezelőbe, és a sima szöveges fájlt biztonságosan megsemmisíteni. A két rendezett projekt tiszta.

## Miért fontos
A rendrakás nem csak esztétika. Egy projektmappában heverő jelszó valódi kockázat (a beérkező állami dokumentumok amúgy is DNA-érzékenyek). Az AI itt nem töröl vakon (az adatvesztés lenne), hanem **jelez**, és rád bízza a döntést. Ez a helyes minta minden érzékeny adatnál: az AI a szem, az ember a kéz.

## Hova vezet ez (Mester előretekintés)
Ez egy jövőbeli **lektor / biztonsági agent** magja: folyamatosan figyeli, hogy sehol ne heverjen érzékeny adat rossz helyen. Agentet a Haladón nem építünk, de látod az irányt.

**Verzió:** 2.0 (Regio adaptáció)
