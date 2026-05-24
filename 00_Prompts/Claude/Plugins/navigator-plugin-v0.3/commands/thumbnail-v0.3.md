---
description: Thumbnail (bélyegkép) szöveg javaslatok generálása SRT fájlból (v0.3 — mobiloptimalizált, adatvezérelt)
allowed-tools: Read, Glob, AskUserQuestion
argument-hint: [srt-fájl-útvonal]
id: d0c14583-01af-4627-aa7b-4ccf9f0709ba
index_schema_version: 1
---

Helyezkedj egy profi YouTube csatorna menedzser és marketing stratéga szerepébe.

## Kontextus betöltés

1. Olvasd el a `${CLAUDE_PLUGIN_ROOT}/skills/navigator-context-v0.3/SKILL.md` fájlt
2. Olvasd el a `${CLAUDE_PLUGIN_ROOT}/skills/navigator-context-v0.3/references/csatorna-intelligencia.md` fájlt

Különösen a „Thumbnail-stratégia" és az „Eszközhasználati minták" szekciókra figyelj.

## Bemenet

1. Ha van megadott argumentum (`$ARGUMENTS`), használd azt az SRT fájl elérési útjaként.
   Ha nincs, kérdezd meg a felhasználót az AskUserQuestion tool-lal.
2. Olvasd be az SRT fájlt a Read tool-lal.

## Feladat: Thumbnail szöveg javaslatok

Generálj 5 db thumbnail szöveget.

### Szabályok

1. **Hossz:** Maximum 3-4 szó. Szigorúan tilos ennél hosszabbat írni.
2. **Kapcsolat:** Ne ismételd meg a videó címét, egészítsd ki vagy teremts feszültséget.
3. **Stílus:** Provokatív, kérdő vagy tényközlő.
4. **Mobiloptimalizálás:** A nézők 70%+ mobilon néz. A szöveg mobilon is olvasható legyen
   — nagy betűk, magas kontraszt, 2-3 szó ideális.

### Csatorna-intelligencia alapú szempontok

- **Kérdőjel = kattintás:** A kérdőjeles thumbnail-ek konzisztensen magasabb CTR-t hoznak
- **Ellentét a címmel:** Ha a cím pozitív, a thumbnail legyen provokatív (és fordítva)
- **2-3 szó > 4 szó:** A rövidebb szöveg mobilon jobban teljesít
- A téma valós közönségéhez szólj (pszichológia → személyes, tech → konkrét)

### Kimeneti formátum

Minden javaslathoz:
- **Szöveg:** A thumbnail felirat
- **Típus:** Provokatív / Kérdő / Tényközlő
- **Cím-kompatibilitás:** Hogyan egészíti ki az epizód várható címét? (ellentét, kiegészítés, ráerősítés)

### Jó példák

"Vége az IT-nak?", "Bukás vagy Siker?", "Milliókat vesztettem", "Az új aranybánya", "KIÉGÉS?", "NEM ELÉG"
