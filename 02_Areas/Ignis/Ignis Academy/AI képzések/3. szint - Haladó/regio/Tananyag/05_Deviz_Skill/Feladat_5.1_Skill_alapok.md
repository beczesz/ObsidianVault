---
title: "Feladat 5.1: Mi a skill, plugin, connector (DEMO)"
date: 2026-07-01
author: Becze Szabolcs
status: active
description: "F5 oktatói demó: a három alapfogalom (Skill = megtanított munkafolyamat, Plugin = képesség-csomag, Connector = külső rendszer-kapcsolat) tisztázása Regio-példákkal, plusz hogyan hívható egy skill közvetlenül az Excelből, és miért kulcs a Team plan a skill-megosztáshoz. Ez alapozza meg a killer-demót."
id: 4f7cb427-8364-4ac2-9f9d-9e1a7b3f6c5d
index_schema_version: 1
bdos_index: true
tags: [ignis-academy, halado, regio-consult, f5, feladat, skill, demo]
---
# Feladat 5.1: Mi a skill, plugin, connector (DEMO)

> **Típus:** 🎤 OKTATÓI DEMO · **Idő:** ~15 perc

---

## Szituáció

Mielőtt az AI kitölti a deviz-templétet, meg kell értenünk **hogyan**. A titok egy **skill**. De előbb tisztázzuk a három fogalmat, amit sokan összekevernek.

---

## A három fogalom (Regio-példákkal)

| Fogalom | Mi ez | Regio-példa |
|---|---|---|
| **Skill** | Egy megtanított, ismételhető munkafolyamat. Egyszer leírod, hogyan kell csinálni valamit, és onnantól egy paranccsal hívod. | A deviz-kitöltő skill: „töltsd ki a deviz templétet a forrás-ajánlatból". |
| **Plugin** | Egy nagyobb képesség-csomag, ami új dolgokra teszi képessé a Cowork-öt (pl. az Excel-plugin, ami élő Excellel dolgozik; egy Legal plugin szerződésekhez). | A Cowork Excel-plugin, amivel a levédett templéten dolgozunk. |
| **Connector** | Kapcsolat egy külső rendszerhez, hogy az AI onnan olvasson (pl. Outlook, OneDrive/SharePoint). | Az Outlook connector: a tervező emailjéből kiolvasni az ajánlatot. |

**A legrövidebben:** a *skill* = amit **te tanítasz** az AI-nak (a ti munkafolyamataitok); a *plugin* = egy **képesség**, amit hozzáadsz; a *connector* = egy **híd** egy külső rendszerhez.

---

## A demó menete

### 1. lépés: Egy skill anatómiája
Az oktató megmutat egy egyszerű skillt (pl. a deviz-kitöltő magját): ez lényegében egy leírás arról, **mi a feladat, milyen lépések vannak, mire figyelj**. Nem kód, hanem érthető utasítás-csomag, amit az AI követ. Aki tud egy jó promptot írni, az tud skillt írni. Élőben egy prompttal meg is íratható a skill magja:

```
Itt a fiktív Napsugár deviz-templét (02_deviz_general_URES_templet.xlsx), a
kitöltött példa (03_deviz_general_KITOLTOTT.xlsx) és a forrás-ajánlat
(01_forras_oferta_Napsugar.xlsx).

Írd le sima nyelven, lépésről lépésre, hogyan kell egy ilyen deviz-templétet
forrásból kitölteni: melyik forrás-tétel melyik lapra és cellába kerül (5_DO1
objektumok, Cap. 4 sorok), mire kell figyelni (csak a szürke input-cellák,
levédett képletek, kereszthivatkozás, TVA a 0_IG-ből). Ez lesz a deviz-kitöltő
skill magja (skill-seed), amit a csapat megoszthat.
```

### 2. lépés: Skill-hívás az Excelből
Az oktató megnyitja a Cowork Excel-plugint egy Excel-fájlon, és a `/` (perjel) gombbal előhozza az elérhető skilleket. Megmutatja: innentől az Excelen belül, egyetlen hívással indul a munkafolyamat. Nem kell kimásolni az adatot; a skill ott dolgozik, ahol a fájl van.

### 3. lépés: A Team plan ereje
Az oktató kimondja a kulcsot: egy Team plan-en a **skillek megoszthatók és verziózhatók**. Amit egy senior egyszer megír (a deviz-kitöltő skillt), azt onnantól **a 21 fős csapat bárki** használja, ugyanúgy, frissítve. Ez a különbség egy személyes trükk és egy céges képesség között.

---

## Amit a résztvevők megfigyelnek
- Hogy a skill nem varázslat, hanem **leírt munkafolyamat** (te is meg tudod írni).
- Hogy a skill közvetlenül az **Excelből** hívható.
- Hogy a Team plan miatt a skill a **csapat közös tudása** lesz.

---

## Tanulás

A skill az, ami az AI-t az egyszeri segítségből **skálázható céges eszközzé** teszi. A ti erősségetek (strukturált, ismétlődő, sztenderd munka) pont az, amit skillbe lehet önteni: minél sztenderdebb egy feladat, annál jobban automatizálható egy skillel. És a Team plan miatt ez nem egy ember tudása marad.

---

## Mi következik (5.2 stáció)
Mielőtt a skill kitölti a templétet, a résztvevők leellenőrzik: érti-e egyáltalán az AI a levédett templét szerkezetét? (Ez a kitöltés előfeltétele.)

---

## Időkeret
- A három fogalom: 5 perc
- Skill anatómia + Excel-hívás: 6 perc
- Team plan: 4 perc
- **Össze: 15 perc**

**Verzió:** 1.0 (Regio adaptáció)
