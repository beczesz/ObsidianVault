---
title: "Feladat 1.4 (Bónusz): A standard md-vé alakítása (md-natív rendszer)"
date: 2026-07-02
author: Becze Szabolcs
status: active
description: "F1 otthoni bónusz: a résztvevő a docx-alapú Internal_Standard-et md-natívvá teszi. Létrehoz egy Standard mappát, áthelyezi oda a docx-et, készít belőle egy hű md változatot, és frissíti az összes CLAUDE.md-t (gyökér, Projects index, projektek), hogy mostantól a md-re hivatkozzanak. Így a következő rendrakásnál/auditnál már nem docx-et kell kicsomagolni, hanem egy közvetlenül olvasható és kereshető md-t használunk."
id: 8d5f0e24-6c93-4e74-9b48-2f3e1d5c4a06
index_schema_version: 1
bdos_index: true
tags: [ignis-academy, halado, regio-consult, f1, bonusz, standard, markdown]
---
# Feladat 1.4 (Bónusz): A standard md-vé alakítása

> **Típus:** otthoni gyakorlat · **A rendszer md-natívvá tétele**

## Cél
A standardünk most egy `Internal_Standard.docx`. A docx-et minden alkalommal ki kell csomagolni és beolvastatni; egy **markdown** viszont közvetlenül olvasható, kereshető, verziózható, és az AI anyanyelve. Tegyük a rendszert md-natívvá.

## Feladat
```
A standardünk most egy docx (Internal_Standard.docx). Tegyük md-natívvá:

1. Hozz létre egy Standard mappát a RegioConsult gyökerében, és helyezd át oda
   a Internal_Standard.docx-et.
2. Készíts belőle egy Internal_Standard.md fájlt ugyanabba a mappába: a docx
   tartalmát hűen, markdownban (a docx maradjon meg referenciának/archívnak).
3. Frissítsd az összes CLAUDE.md-t (a gyökér, a Projects index, és minden
   projekté), hogy mostantól a Standard/Internal_Standard.md-re hivatkozzanak
   a docx helyett.

A cél: legközelebb, amikor rendet kell rakni vagy auditálni, már nem a docx-et
kell kicsomagolni, hanem egy md-t olvasunk, ami közvetlenül kereshető.
```

## Elvárt eredmény
Egy `Standard/` mappa a docx-szel és az új `Internal_Standard.md`-vel, és minden CLAUDE.md a md-re mutat. A rendszer mostantól md-natív: a következő audit/rendrakás a md-t olvassa.

## Tanulás
A docx **ember-barát** (formázott, nyomtatható), a md **gép-barát** (közvetlenül olvasható, kereshető, diffelhető). Egy AI-workflow-ban a md a jobb: nincs kicsomagolás, a szabály egyetlen grep-pel megtalálható, és a CLAUDE.md lánc közvetlenül hivatkozhatja. A docx megmarad archívnak, a md lesz a munka-verzió. Kapcsolódik: [[Feladat_1.9_Bonusz_Standard_bovites]].

**Verzió:** 2.0 (Regio adaptáció)
