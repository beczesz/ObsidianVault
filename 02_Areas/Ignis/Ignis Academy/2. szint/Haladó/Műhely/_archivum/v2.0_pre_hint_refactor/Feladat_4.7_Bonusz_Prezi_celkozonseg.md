---
title: "(Bónusz) Feladat 4.7 — Ugyanaz a prezentáció, 3 célközönségnek"
date: 2026-05-14
author: Becze Szabolcs
status: active
description: "Gyakorlat egy CEO-prezentáció átalakítására három különböző célközönségnek: bankár, alkalmazottak és sajtó. A feladat bemutatja, hogyan használható az AI-vel ugyanaz a tartalom másféle fókusszal, hangnemmel és hosszúsággal újraírható néhány perc alatt."
description_source: auto
description_hash: 852a2f260239c4ce
id: 34d3f37f-7056-4543-b63f-23a0ad2775a1
index_schema_version: 1
bdos_index: true
---
# (Bónusz) Feladat 4.7 — Ugyanaz a prezentáció, 3 célközönségnek

## Szituáció

Az F4.3-ban a Cowork generált egy 5-slide CEO prezentációt Mártonnak. De ugyanazt az információt **másképp kell elmondani** a banknak, az alkalmazottaknak, vagy a sajtónak. Más a fókusz, más a hangnem, más a hossz.

A Cowork-kel ez **másodpercek alatt át lehet alakítani** — egy alapprezentációból 4 verzió.

## Feladat

Vedd az F4.3-ban készült CEO prezentációt (vagy ha nincs meg, kérj egy újat), és kérd meg a Cowork-öt, hogy alakítsa át 3 másik célközönségre:

### Verzió A: Bankár / hitelező
- Fókusz: cash flow, biztosítékok, megtérülés
- Hangnem: konzervatív, számokkal alátámasztott
- Hossz: 8-10 slide (banki standard)

### Verzió B: Alkalmazottak (csapatülés)
- Fókusz: mi változik nekünk, mi az új lehetőség
- Hangnem: motiváló, közvetlen, érzelmes
- Hossz: 5-6 slide (rövid, vizuális)

### Verzió C: Helyi sajtó / közösség
- Fókusz: helyi munkahelyteremtés, fenntarthatóság, közösségi érték
- Hangnem: büszke, közösségi, kicsit emelkedett
- Hossz: 4-5 slide (sajtó-anyag stílus)

### Javasolt prompt:

> "Itt a CEO prezentációm (vagy: `presentation_marton_v1.pptx`). Készíts 3 új verziót:
>
> **A) Bankár-verzió:** Az ügyvezetői változatból fókuszálj a pénzügyi adatokra. 8 slide. Konzervatív hangnem.
>
> **B) Alkalmazotti verzió:** Az ügyvezetői változatból fókuszálj arra ami a dolgozóknak fontos: új technológia, képzés, munkakör-változás. 5 slide. Motiváló hangnem.
>
> **C) Sajtó-verzió:** Az ügyvezetői változatból fókuszálj a helyi értékre: zöld átállás, helyi cég, Hargita megye. 4 slide. Kicsit emelkedett hangnem.
>
> Mindegyik kapjon külön .pptx fájlt."

## Elvárt kimenet

3 külön .pptx fájl:
- `presentation_bank_v1.pptx`
- `presentation_team_v1.pptx`
- `presentation_press_v1.pptx`

## Extra kihívás

Miután megvan a 3 verzió, kérdezd meg:
> "Mindegyik verzióhoz adj egy **beszéd-vázlatot** (5-10 mondatos cue card) amit én magamtól is el tudok mondani — kulcsfogalmakkal kiemelve. Hangnemben különbözzön a 3 vázlat."

## Tipp

A "ugyanaz a tartalom, más célközönség" pattern **az AI üzleti kommunikációs szuperereje**. Ami korábban 2-3 nap volt (3 prezentáció előkészítése), most 5 perc.

**Vigyázz:** a Cowork néha túl entuziasztikus a sajtó-verzióval — érdemes lehúznod 1-2 ponttal a felsőbb fokokat ("legnagyobb" → "egyik vezető").

## Tanulás

- Az AI **nemcsak fordít — átalakít hangnemet, fókuszt, hosszt**
- Egy üzleti ember átlagosan 5-6 különböző célközönséggel kommunikál — mindegyikhez más Cowork-prompt sablont érdemes kialakítani
- A beszéd-vázlat (cue card) a prezentáció **emberi része** — ezt az AI nem írhatja meg neked, csak feltérképezi
- A 4-féle verzió (CEO + 3 új) **újrahasználható template** lesz minden következő nagy prezentációdhoz
