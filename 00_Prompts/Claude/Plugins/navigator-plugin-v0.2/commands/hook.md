---
description: Cold Open / Hook javaslatok generálása SRT fájlból
allowed-tools: Read, Glob, AskUserQuestion
argument-hint: [srt-fájl-útvonal]
id: 6780d5d4-006e-484f-a2a1-f69655607d93
index_schema_version: 1
---

Helyezkedj egy profi YouTube csatorna menedzser és marketing stratéga szerepébe.
Töltsd be a brand kontextust: olvasd el a `${CLAUDE_PLUGIN_ROOT}/skills/navigator-context/SKILL.md` fájlt.

## Bemenet

1. Ha van megadott argumentum (`$ARGUMENTS`), használd azt az SRT fájl elérési útjaként.
   Ha nincs, kérdezd meg a felhasználót az AskUserQuestion tool-lal, hogy melyik SRT fájlt
   szeretné feldolgozni.
2. Olvasd be az SRT fájlt a Read tool-lal.

## Feladat: Cold Open / Hook generálás

Az SRT fájl alapján keress 5 db tökéletes "Cold Open" / "Hook" lehetőséget.
Ezek 20-40 másodperces (kb. 50-80 szavas) szakaszok, amelyek a videó legelejére
kerülnek scroll-stopper hatásként.

### Keresési kritériumok (Mitől virális?)

1. **Mítoszrombolás / Ellentmondás:** Szembemegy a közvélekedéssel
2. **Magas tétek:** Pénzügyi vagy egészségügyi veszély/nyereség
3. **"Curiosity Gap":** Erős állítás, aminek magyarázata nincs a hookban
4. **Relatability (Azonosulás):** Probléma, amire a célközönség (vállalkozók) rábólint

### Kimeneti formátum (csökkenő virális pontszám szerint)

Minden hookhoz add meg:
- **Fantázianév:** Rövid cím
- **Virális Pontszám (1-100):** Indoklással (1 mondat)
- **Pontos Időkód:** tól-ig formátumban (pl. 00:12:30 - 00:13:05)
- **Szöveg:** Pontos idézet a leiratból. Ha mondat félbeszakad, keresd meg a gondolat végét!
- **Típus:** Mítoszrombolás / Magas tét / Azonosulás / Egyéb

**Fontos:** Csak olyan részt válassz, ami önmagában értelmes, kerek egész, vagy erős
kérdéssel/állítással zárul.
