---
description: YouTube leírás és hashtagek generálása SRT fájlból (v0.3 — SEO-intelligenciával és cross-referenciával)
allowed-tools: Read, Glob, AskUserQuestion
argument-hint: [srt-fájl-útvonal]
id: c0129978-0ec4-404d-8fdb-bfc930e9441f
index_schema_version: 1
---

Helyezkedj egy profi YouTube csatorna menedzser és marketing stratéga szerepébe.

## Kontextus betöltés

1. Olvasd el a `${CLAUDE_PLUGIN_ROOT}/skills/navigator-context-v0.3/SKILL.md` fájlt
2. Olvasd el a `${CLAUDE_PLUGIN_ROOT}/skills/navigator-context-v0.3/references/csatorna-intelligencia.md` fájlt

Különösen a „Leírás és SEO" és a „A sorozat-hatás" szekciókra figyelj.

## Bemenet

1. Ha van megadott argumentum (`$ARGUMENTS`), használd azt az SRT fájl elérési útjaként.
   Ha nincs, kérdezd meg a felhasználót az AskUserQuestion tool-lal.
2. Olvasd be az SRT fájlt a Read tool-lal.
3. Kérdezd meg a felhasználót az AskUserQuestion tool-lal:
   - **A vendég neve**
   - **Az epizód száma** (pl. EP45)
   - **Van-e korábbi epizód ezzel a vendéggel?** (Ha igen, melyik EP szám?)

## Feladat: YouTube leírás és hashtagek

Készíts egy SEO-optimalizált leírást.

### Struktúra

1. **Hook (első 2 sor):** Erős kérdés vagy provokatív állítás — ez látszik a "Több" gomb előtt.
   A csatorna-intelligencia alapján: legalább 1 kereshető kulcsszót tartalmazzon (pl. „nárcizmus",
   „kiégés", „AI" — nem költői, hanem konkrét).
2. **Kontextus:** Vendég és problémafelvetés rövid bemutatása
3. **Tartalmi összefoglaló:** 3-4 mondat, kulcsszavakban gazdag
4. **Cross-referencia blokk (v0.3 újdonság):**
   Ha a vendég korábban szerepelt, vagy a téma kapcsolódik más epizódokhoz:
   ```
   🔗 Kapcsolódó epizódok:
   EP14 — A nárcizmus rejtett arcai | Bencze Edit: https://youtu.be/[ID]
   EP28 — Nárcisztikus kapcsolatokból kiút | Bencze Edit: https://youtu.be/[ID]
   ```
   Ez a sorozat-hatás kihasználása: az end-screen CTR egyetlen bizonyított növelője.
5. **Stílus:** Olvasmányos, tagolt, motiváló

### Hashtagek

Generálj 5-8 releváns hashtaget:
- Vegyítsd a széles körű (#Vállalkozás) és specifikus (#VentureBuilder) címkéket
- **Mindig tartalmazza:** #NavigátorPodcast és #MagyarPodcast
- A csatorna-intelligencia alapján: a YouTube Search forgalom erősen korrelál az
  egyértelmű kulcsszavakkal — használj keresési volumennel rendelkező szavakat

### SEO ellenőrzőlista (v0.3)

A leírás leadása előtt ellenőrizd:
- [ ] Az első 2 sor tartalmaz kereshető kulcsszót?
- [ ] A leírás tartalmaz cross-referenciát (ha releváns)?
- [ ] A hashtagek tartalmazzák a két kötelezőt?
- [ ] A leírás mobilon is jól olvasható (rövid bekezdések)?
