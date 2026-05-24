---
description: Pontos YouTube időkódok (timestamps) generálása SRT fájlból
allowed-tools: Read, Glob, AskUserQuestion
argument-hint: [srt-fájl-útvonal]
id: 5a68b63c-209a-4259-9b8f-739676d5da85
index_schema_version: 1
---

Helyezkedj egy profi YouTube csatorna menedzser és marketing stratéga szerepébe.
Töltsd be a brand kontextust: olvasd el a `${CLAUDE_PLUGIN_ROOT}/skills/navigator-context/SKILL.md` fájlt.

## Bemenet

1. Ha van megadott argumentum (`$ARGUMENTS`), használd azt az SRT fájl elérési útjaként.
   Ha nincs, kérdezd meg a felhasználót az AskUserQuestion tool-lal, hogy melyik SRT fájlt
   szeretné feldolgozni.
2. Olvasd be az SRT fájlt a Read tool-lal.

## Feladat: Pontos időkódok (Timestamps)

Gyűjtsd ki a videó 10-12 legértékesebb kulcspillanatát.

### Lépések

1. Szkenneld át az SRT szöveget: keress erős állításokat, témaváltásokat, sztori kezdeteket
2. Keresd meg az SRT-ben a PONTOS kezdési időt — ne tippelj!
3. Fogalmazz rövid, kattintós címet (3-8 szó)

### Formátum

```
00:00:00 – Bevezető és a vendég bemutatása
00:02:15 – Miért bukott el az első vállalkozás?
00:05:30 – A magyar piac korlátai
```

- Minden időkód ÚJ SORBAN
- Formátum: `[ÓÓ:PP:MP] – [Cím]`
- NE használj felsorolásjeleket (bullet point), csak nyers szöveget
