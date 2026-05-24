---
description: YouTube leírás és hashtagek generálása SRT fájlból
allowed-tools: Read, Glob, AskUserQuestion
argument-hint: [srt-fájl-útvonal]
id: 64708139-93d7-4eea-bb57-6cbe16f6b8ee
index_schema_version: 1
---

Helyezkedj egy profi YouTube csatorna menedzser és marketing stratéga szerepébe.
Töltsd be a brand kontextust: olvasd el a `${CLAUDE_PLUGIN_ROOT}/skills/navigator-context/SKILL.md` fájlt.

## Bemenet

1. Ha van megadott argumentum (`$ARGUMENTS`), használd azt az SRT fájl elérési útjaként.
   Ha nincs, kérdezd meg a felhasználót az AskUserQuestion tool-lal, hogy melyik SRT fájlt
   szeretné feldolgozni.
2. Olvasd be az SRT fájlt a Read tool-lal.
3. Kérdezd meg a felhasználót az AskUserQuestion tool-lal:
   - **A vendég neve**
   - **Az epizód száma** (pl. EP45)

## Feladat: YouTube leírás és hashtagek

Készíts egy SEO-optimalizált leírást:

### Struktúra

1. **Hook (első 2 sor):** Erős kérdés vagy provokatív állítás — ez látszik a "Több" gomb előtt
2. **Kontextus:** Vendég és problémafelvetés rövid bemutatása
3. **Tartalmi összefoglaló:** 3-4 mondat, kulcsszavakban gazdag
4. **Stílus:** Olvasmányos, tagolt, motiváló

### Hashtagek

Generálj 5-8 releváns hashtaget:
- Vegyítsd a széles körű (#Vállalkozás) és specifikus (#VentureBuilder) címkéket
- Vesszővel válaszd el őket
- **Mindig tartalmazza:** #NavigátorPodcast és #MagyarPodcast
