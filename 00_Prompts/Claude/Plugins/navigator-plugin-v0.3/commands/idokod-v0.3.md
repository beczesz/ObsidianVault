---
description: Pontos YouTube időkódok (timestamps) generálása SRT fájlból (v0.3 — hook-integrációval)
allowed-tools: Read, Glob, AskUserQuestion
argument-hint: [srt-fájl-útvonal]
id: bf5fefac-469b-4842-98ac-92b8ebcae3bb
index_schema_version: 1
---

Helyezkedj egy profi YouTube csatorna menedzser és marketing stratéga szerepébe.
Töltsd be a brand kontextust: olvasd el a `${CLAUDE_PLUGIN_ROOT}/skills/navigator-context-v0.3/SKILL.md` fájlt.

## Bemenet

1. Ha van megadott argumentum (`$ARGUMENTS`), használd azt az SRT fájl elérési útjaként.
   Ha nincs, kérdezd meg a felhasználót az AskUserQuestion tool-lal.
2. Olvasd be az SRT fájlt a Read tool-lal.

## Feladat: Pontos időkódok (Timestamps)

Gyűjtsd ki a videó 10-12 legértékesebb kulcspillanatát.

### Lépések

1. Szkenneld át az SRT szöveget: keress erős állításokat, témaváltásokat, sztori kezdeteket
2. Keresd meg az SRT-ben a PONTOS kezdési időt — ne tippelj!
3. Fogalmazz rövid, kattintós címet (3-8 szó)
4. **v0.3 újdonság — Hook jelölés:** Ha valamelyik időkódnál különösen erős hook-anyag van
   (személyes vallomás, mítoszrombolás, megdöbbentő statisztika), jelöld csillaggal (★).
   Ez segít Szabolcsnak a cold open kiválasztásánál.

### Formátum

```
00:00:00 – Bevezető és a vendég bemutatása
00:02:15 – ★ Miért bukott el az első vállalkozás?
00:05:30 – A magyar piac korlátai
00:12:45 – ★ „Mindent elveszítettem" — a fordulópont
```

- Minden időkód ÚJ SORBAN
- Formátum: `[ÓÓ:PP:MP] – [Cím]`
- NE használj felsorolásjeleket (bullet point), csak nyers szöveget
- A ★ jellel jelölt időkódok potenciális cold open anyagok
