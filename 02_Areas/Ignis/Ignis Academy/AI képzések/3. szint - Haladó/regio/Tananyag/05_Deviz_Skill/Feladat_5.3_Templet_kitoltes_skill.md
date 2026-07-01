---
title: "Feladat 5.3: A killer: skill kitölti a deviz-templétet (DEMO)"
date: 2026-07-01
author: Becze Szabolcs
status: active
description: "F5 killer-demó: egy skill a forrás-ajánlatból (01_forras) kitölti az üres deviz-templét (02_URES) szürke input-celláit az 5_DO1 lapon, az 1_DG automatikusan aggregál (kereszthivatkozás, TVA), és az eredményt összevetjük a megoldókulccsal (03_KITOLTOTT). Kontraszt: senior-óra kézzel vs. skill-perc. Kontroll-számokkal validálva."
id: 619ed649-0586-4cd4-9bbf-1a3c9d5b8e7f
index_schema_version: 1
bdos_index: true
tags: [ignis-academy, halado, regio-consult, f5, feladat, killer, demo]
---
# Feladat 5.3: A killer: skill kitölti a deviz-templétet (DEMO)

> **Típus:** 🎤 OKTATÓI DEMO (a workshop csúcspontja) · **Idő:** ~15 perc

---

## Szituáció

Minden együtt van: értjük a skillt (5.1), az AI érti a templét szerkezetét (5.2). Most jön a pillanat, amiért az egész workshop épült: a **skill kitölti a levédett deviz-templétet a forrás-ajánlatból**, kevés inputból. Amit ma egy senior 5-10 év tapasztalattal, órák alatt csinál, azt itt egy skill percek alatt.

---

## A kontraszt-pillanat felállítása

Az oktató először **kimondja a kézi valóságot**: ezt a templétet ma csak Laci vagy egy senior tudja kitölteni. Végig kell venni a forrás-ajánlat minden tételét, a megfelelő objektumhoz és kategóriához rendelni, beírni a szürke cellákba, ügyelve, hogy a levédett képleteket ne rontsa el. Ez **jó félóra-óra** figyelmes munka, és hibázni könnyű.

Aztán jön a skill.

---

## A demó menete

### 1. lépés: A három fájl a képernyőn
- `01_forras_oferta_Napsugar.xlsx`: a lapos tételsor (objektum, kategória, UM, mennyiség, ár, érték).
- `02_deviz_general_URES_templet.xlsx`: az üres templét, szürke input-cellákkal.
- `03_deviz_general_KITOLTOTT.xlsx`: a megoldókulcs (egyelőre nem nézzük).

### 2. lépés: A skill hívása
Az Excel-pluginban, a `02_URES` templéten:

```
Töltsd ki ezt az üres deviz general templétet a forrás-ajánlatból
(01_forras_oferta_Napsugar.xlsx). A forrás tételeit rendeld az 5_DO1 lap
megfelelő objektumaihoz (Hala, Depozit, Centrală, Amenajări) és
kategóriáihoz, és írd be a szürke input-cellákba. A levédett, képletes
cellákat NE módosítsd, azok automatikusan aggregálnak. A montaj, utilaje,
dotări tételek a Cap. 4 megfelelő soraiba kerüljenek. Amikor kész,
mondd meg a Cap. 4 összeget és a TOTAL GENERAL fără TVA + cu TVA értéket.
```

### 3. lépés: Az eredmény (a WOW)
A skill beírja a szürke cellákat az `5_DO1`-en, az `1_DG` **magától aggregál** (kereszthivatkozás + TVA-számítás). Az oktató felolvassa a számokat:
- `5_DO1` Construcții (4.1): **3 190 000** (Hala 2 330 000 + Depozit 380 000 + Centrală 270 000 + Amenajări 210 000)
- Cap. 4 összesen: **5 435 000**
- TOTAL GENERAL fără TVA: **6 455 000** · TVA 19%: 1 226 450 · cu TVA: **7 681 450**

### 4. lépés: Összevetés a megoldókulccsal
Megnyitjuk a `03_KITOLTOTT`-at: **a számok egyeznek.** A skill nem csak beírt, hanem a helyes objektum-kategória logika szerint, és a képletek dolgoztak. Ez a „operál" pillanat.

---

## Amit a résztvevők megfigyelnek
- Hogy a skill a **forrás lapos tételeit** helyesen rendeli a templét struktúrájához.
- Hogy a levédett **képletek maguktól** aggregálnak, ha csak a szürke cellákat töltjük.
- Hogy az eredmény **egyezik a megoldókulccsal**, a végösszegekig.

---

## Tanulás

Ez a workshop tézise egyetlen demóban: a ti legáltalánosabb, legidőigényesebb, legsenior-igényesebb munkátok egy **skillbe önthető**, és onnantól **kevés inputból, percek alatt, megosztva a csapatnak** elvégezhető. Nem az ember helyett, hanem az ember kezeként: a senior tudása egyszer beépül a skillbe, és onnantól a csapat is hozzáfér.

**Fontos:** a levédett cellák és a képlet-aggregáció a **Cowork Excel-pluginnal (élő Excel)** működik. Ezt használjuk a workshopon.

---

## Mi következik (F6)
Az utolsó lánc-szem: a monitoring. A kitöltött deviz / szerződés alapján követjük a kivitelezést egy Centralizatorban, és generálunk egy dokumentumot a saját sztenderdben.

---

## Időkeret
- A kézi valóság felállítása: 3 perc
- Skill hívása + kitöltés: 6 perc
- Aggregátum + megoldókulcs összevetés: 4 perc
- Reakció, kérdések: 2 perc
- **Össze: 15 perc**

**Verzió:** 1.0 (Regio adaptáció)
