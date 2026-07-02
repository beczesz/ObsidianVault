---
title: "Feladat 6.1: A deviz-kitöltő skill anatómiája (DEMO)"
date: 2026-07-02
author: Becze Szabolcs
status: active
description: "F6 oktatói demó: a Skill/Plugin/Connector fogalmakat már az F3-ban megismertük, itt egy konkrét skill anatómiáját nézzük meg (mi a feladat, milyen lépések, mire figyelj), és hogyan hívható közvetlenül az Excelből. Ez alapozza meg a killer-demót: a deviz-templét kitöltését egy megosztható, verziózható skillel."
id: 4f7cb427-8364-4ac2-9f9d-9e1a7b3f6c5d
index_schema_version: 1
bdos_index: true
tags: [ignis-academy, halado, regio-consult, f6, feladat, skill, demo]
---
# Feladat 6.1: A deviz-kitöltő skill anatómiája (DEMO)

> **Típus:** 🎤 OKTATÓI DEMO · **Idő:** ~15 perc

---

## Szituáció

A **Skill / Plugin / Connector** fogalmakat már az F3-ban megismertük. Most jön a lényeg: hogyan lesz ezekből a **legnehezebb, csak-senior munkátokból** megosztható céges eszköz. A titok egy **skill**, ami kitölti a levédett deviz-templétet. Előbb nézzük meg egy skill anatómiáját, mielőtt élesben lefuttatjuk.

> **Emlékeztető (F3):** a *skill* = amit **te tanítasz** az AI-nak (a ti munkafolyamataitok); a *plugin* = egy **képesség**, amit hozzáadsz (pl. a Cowork Excel-plugin); a *connector* = egy **híd** egy külső rendszerhez (pl. MS365).

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

## Mi következik (6.2 stáció)
Mielőtt a skill kitölti a templétet, a résztvevők leellenőrzik: érti-e egyáltalán az AI a levédett templét szerkezetét? (Ez a kitöltés előfeltétele.)

---

## Időkeret
- A három fogalom: 5 perc
- Skill anatómia + Excel-hívás: 6 perc
- Team plan: 4 perc
- **Össze: 15 perc**

**Verzió:** 1.0 (Regio adaptáció)
