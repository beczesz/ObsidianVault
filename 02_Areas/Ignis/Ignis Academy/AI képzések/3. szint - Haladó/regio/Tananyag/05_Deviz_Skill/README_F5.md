---
title: "F5: Deviz-templét kitöltő skill (KILLER-DEMO)"
date: 2026-07-01
author: Becze Szabolcs
status: active
description: "Az F5 modul a workshop csúcspontja és a Regio legáltalánosabb fájdalmának megoldása: egy levédett, képletvezérelt deviz general templétet egy SKILL tölt ki a forrás-ajánlatból, kevés inputból. Megtanítja mi a skill / plugin / connector, hogyan írj és hívj skillt (akár Excelből), és hogyan oszd meg a csapattal (Team plan). A killer-demo: üres templét szürke cellái → aggregált Deviz General, összevetve a megoldókulccsal."
id: 3e6bf316-7253-4fb1-8e8c-8d0f6a2e5b4c
index_schema_version: 1
bdos_index: true
tags: [ignis-academy, halado, regio-consult, f5, skill, deviz, killer-demo]
---
# F5: Deviz-templét kitöltő skill (KILLER-DEMO)
**Időkeret:** 45 perc · **Fázis a workshopban:** 5/6 (a csúcspont)

## Modell

🎤 **2 DEMO** + ⏸ **1 stáció**, kontraszt-pillanattal (senior-óra vs. skill-perc).

| # | Fájl | Típus | Idő |
|---|---|---|---|
| **5.1** | `Feladat_5.1_Skill_alapok.md` | 🎤 OKTATÓI DEMO (mi a skill/plugin/connector) | ~15p |
| **5.2** | `Feladat_5.2_Deviz_struktura_felismeres.md` | ⏸ STÁCIÓ (az AI érti-e a templétet) | ~10p |
| **5.3** | `Feladat_5.3_Templet_kitoltes_skill.md` | 🎤 OKTATÓI DEMO (a killer: skill kitölti) | ~15p |

## Narratív összefoglaló

Ez a legáltalánosabb fájdalmatok (a meeting #2 prioritása) és a workshop csúcspontja. A deviz general és az üzleti terv templétek **levédett cellás, képletvezérelt** Excel-ek, amiket ma **csak senior tud kitölteni**, 5-10 év tapasztalattal. Szabolcs saját ötlete adja a megoldást: **üres templét + kitöltött példa + forrás-Excel** hármasból egy **skill**, ami felismeri a templét struktúráját, és kevés inputból kitölti. Pont úgy, ahogy Szabolcs a saját statisztika-skilljét használja.

Ez az a hely, ahol a **Skill / Plugin / Connector** fogalmakat is megtanuljuk, és ahol a **Team plan** kulcs lesz: a skill megosztható és verziózható a csapaton belül, tehát amit egy senior egyszer megír, azt onnantól bárki használja.

## Tanulási célok
1. **Mi a skill, plugin, connector**, a három fogalom tisztán, példákkal.
2. **Hogyan ír és hív az AI skillt**, akár közvetlenül az Excelből (Cowork Excel-plugin).
3. **Levédett cellák kezelése**, csak a szürke input-cellákba írunk, a képletek dolgoznak.
4. **Team-megosztás + verziózás**, a skill közös eszköz, nem egy ember tudása.
5. **A hármas-minta**, üres templét + kitöltött példa + forrás: ebből tanul a skill.

## A killer-demo hármasa (az assetek)

| Fájl | Mi ez | Szerep |
|---|---|---|
| `01_forras_oferta_Napsugar.xlsx` | a kivitelezői ajánlat lapos tételsora | **A FORRÁS** (ezt kapod) |
| `02_deviz_general_URES_templet.xlsx` | üres deviz-templét, szürke input-cellák, levédett képletes lapok (jelszó: `rcm`) | **AZ ÜRES TEMPLÉT** (ezt tölti ki a skill) |
| `03_deviz_general_KITOLTOTT.xlsx` | ugyanaz kitöltve | **A MEGOLDÓKULCS** (ezzel vetjük össze) |

Kontroll-számok: `5_DO1` Construcții 3 190 000 (4.1), Cap. 4 = 5 435 000, TOTAL fără TVA = 6 455 000, cu TVA (19%) = 7 681 450.

## Otthoni bónuszok

| # | Bónusz | Output |
|---|---|---|
| 5.4 | `Feladat_5.4_Bonusz_Sajat_skill.md` | Saját skill írása egy valós templétre |
| 5.5 | `Feladat_5.5_Bonusz_Csapat_megosztas.md` | Skill megosztása + verziózása a csapatnak |
| 5.6 | `Feladat_5.6_Bonusz_AnexaB.md` | Az Anexa B üzleti terv templét kitöltése |

## Átmenet F6-ba

*„A deviz kitöltve, egy skillel, amit a csapatod is használhat. Az utolsó lánc-szem a monitoring: követni a kivitelezést a szerződéshez mérve, és generálni a saját sztenderdetekben egy dokumentumot."*

## Fontos elvárás-kezelés
A képlet-újraszámolás és a levédett cellák a **Cowork Excel-pluginnal (élő Excel)** működnek helyesen. A workshop-út ezt használja. (Egy fejlesztői python/openpyxl script nem számol képletet és nem tartja a lapvédelmet; ez csak háttér-tudnivaló, a workshopon nem játszik.)

**Verzió:** 1.0 (Regio adaptáció)
