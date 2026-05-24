---
description: YouTube cím javaslatok generálása SRT fájlból
allowed-tools: Read, Glob, AskUserQuestion
argument-hint: [srt-fájl-útvonal]
id: f78c27d1-76e5-4331-a7ee-8479f57a186c
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

## Feladat: YouTube cím generálás

Írj 5 db figyelemfelkeltő (High-CTR) YouTube címet.

### Formátum

`„Idézet vagy erős állítás" – Téma/Kontextus | Vendég neve | EP[szám]`

### Kritériumok

1. Használj erős érzelmi hívószavakat (félelem a lemaradástól, ellentmondásos vélemény,
   pénzügyi siker/bukás, jövőkép)
2. Variációk:
   - Legyen egy negatív/figyelmeztető hangvételű (pl. "Vége az aranykornak")
   - Legyen egy inspiráló/sikersztori jellegű
   - Legyen egy szakmai/edukációs jellegű
3. Kerüld a közhelyeket (pl. "Beszélgetés arról, hogy...")

### Példa

`„Nem vagyunk összeszerelő üzem" – Magyarország új MI-stratégiája | Dr. Palkovics László | EP32`
