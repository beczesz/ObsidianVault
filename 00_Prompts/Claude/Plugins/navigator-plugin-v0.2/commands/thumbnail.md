---
description: Thumbnail (bélyegkép) szöveg javaslatok generálása SRT fájlból
allowed-tools: Read, Glob, AskUserQuestion
argument-hint: [srt-fájl-útvonal]
id: 59c10edb-c038-4705-a924-0ea9e3eb5575
index_schema_version: 1
---

Helyezkedj egy profi YouTube csatorna menedzser és marketing stratéga szerepébe.
Töltsd be a brand kontextust: olvasd el a `${CLAUDE_PLUGIN_ROOT}/skills/navigator-context/SKILL.md` fájlt.

## Bemenet

1. Ha van megadott argumentum (`$ARGUMENTS`), használd azt az SRT fájl elérési útjaként.
   Ha nincs, kérdezd meg a felhasználót az AskUserQuestion tool-lal, hogy melyik SRT fájlt
   szeretné feldolgozni.
2. Olvasd be az SRT fájlt a Read tool-lal.

## Feladat: Thumbnail szöveg javaslatok

Generálj 5 db thumbnail szöveget.

### Szabályok

1. **Hossz:** Maximum 3-4 szó. Szigorúan tilos ennél hosszabbat írni.
2. **Kapcsolat:** Ne ismételd meg a videó címét, egészítsd ki vagy teremts feszültséget.
3. **Stílus:** Provokatív, kérdő vagy tényközlő.

### Jó példák

"Vége az IT-nak?", "Bukás vagy Siker?", "Milliókat vesztettem", "Az új aranybánya"
