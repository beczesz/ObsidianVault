---
title: "F5.3 — Pályázati form kitöltése (DEMO)"
date: 2026-05-13
author: Becze Szabolcs
status: active
description: "Demonstrációs gyakorlat, ahol az oktató megmutatja, hogyan tölti ki az AI egy 40-60 mezős pályázati form nyomtatványt a már összegyűjtött vállalati adatok felhasználásával, jelölve a hiányzó információkat."
description_source: auto
description_hash: fc548f32b6aeb12e
id: 2086dcca-f204-444f-a324-7ba2b995733b
index_schema_version: 1
bdos_index: true
---
# F5.3 — Pályázati form kitöltése (DEMO)

## Kontextus
A pályázatot online kell beadni — az AFM portálján (MySMIS) van egy hosszú form, amit ki kell tölteni. Mezőnként: cégadatok, beruházás leírása, költségvetés, indikátorok. Egy tipikus pályázati form 40-60 mezőből áll, és egy tanácsadó 1-2 órát tölt el a kitöltésével.

## Feladat (DEMO — az oktató mutatja)
Ez a rész **elsősorban demo**: az oktató bemutatja, hogyan tölti ki a Cowork a form mezőit a már meglévő adatokból.

### A flow:
1. Az oktató megnyit egy pályázati form sablont (HTML vagy markdown)
2. Megkéri a Cowork-öt:

```
Itt a pályázati form mezői. Töltsd ki a TransOffice adataival.
Ahol az adatot az F1-F4 munkából ismered, töltsd ki.
Ahol nem ismered, jelöld meg [HIÁNYZIK]-kal és írd oda honnan szerezhető be.
```

3. A Cowork végigmegy a mezőkön és kitölti — CUI, cég neve, árbevétel, alkalmazotti létszám, beruházás összege, stb.

### Miért demo?
A form kitöltés vizuálisan lenyűgöző (40 mező → 30 mp), de a résztvevők nem tudják reálisan kipróbálni (nincs MySMIS hozzáférésük). Ezért 70% demo, 30% kérdezz-felelek.

## Tanulási pont
- A Cowork az eddigi kontextusból **automatikusan kitölti** a form 80%-át
- A maradék 20% az, amit jelöl: "ezt nem tudom, kérdezd meg X-et"
- Egy tanácsadó 1-2 órás munkája → 2 perc

## Checkpoint
**WOW:** 40 mezős form → szinte teljesen kitöltve 30 mp alatt, a hiányok jelölve
**MICRO HANDS-ON:** "Melyik mezőt nem tudta kitölteni az AI? Miért nem? Honnan szerezhető be?"
