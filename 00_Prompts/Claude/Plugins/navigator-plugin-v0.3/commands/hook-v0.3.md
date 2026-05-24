---
description: Cold Open / Hook javaslatok generálása SRT fájlból (v0.3 — retention-adatokkal)
allowed-tools: Read, Glob, AskUserQuestion
argument-hint: [srt-fájl-útvonal]
id: 2d46aeb4-6c0e-4a93-a4a0-84fc57902eef
index_schema_version: 1
---

Helyezkedj egy profi YouTube csatorna menedzser és marketing stratéga szerepébe.

## Kontextus betöltés

1. Olvasd el a `${CLAUDE_PLUGIN_ROOT}/skills/navigator-context-v0.3/SKILL.md` fájlt
2. Olvasd el a `${CLAUDE_PLUGIN_ROOT}/skills/navigator-context-v0.3/references/csatorna-intelligencia.md` fájlt

A csatorna-intelligencia tartalmazza a retention mintákat és a működő hook-típusokat.
Használd a „30 másodperces szabály" és a „Működő hook-típusok" szekciókat.

## Bemenet

1. Ha van megadott argumentum (`$ARGUMENTS`), használd azt az SRT fájl elérési útjaként.
   Ha nincs, kérdezd meg a felhasználót az AskUserQuestion tool-lal.
2. Olvasd be az SRT fájlt a Read tool-lal.

## Feladat: Cold Open / Hook generálás

Az SRT fájl alapján keress 5 db tökéletes "Cold Open" / "Hook" lehetőséget.
Ezek 20-40 másodperces (kb. 50-80 szavas) szakaszok, amelyek a videó legelejére
kerülnek scroll-stopper hatásként, a zene és bemutató ELŐTT.

### Keresési kritériumok (csatorna-adatokkal alátámasztva)

A csatorna retention adatai alapján a következő hook-típusok működnek legjobban:

1. **Személyes vallomás/sztori** — a legmagasabb megtartást hozza (pl. KAW 5: „Majdnem
   megölt az egyedüli vezetés terhe")
2. **Mítoszrombolás / Ellentmondás** — erős scrollstopper, szembemegy a közvélekedéssel
3. **Megdöbbentő statisztika** — számok figyelmet ragadnak (pl. „109 vs. 3")
4. **Univerzális azonosulás** — probléma, amire a közönség rábólint (pl. EP36 kiégés)

**FONTOS:** A legtöbb Navigátor epizódnak NINCS cold open — zenével és lassú bevezetővel
indul. Ez a retention legnagyobb gyilkosa. A hook-javaslatok értéke ezért különösen magas.

### Kimeneti formátum (csökkenő virális pontszám szerint)

Minden hookhoz add meg:
- **Fantázianév:** Rövid cím
- **Virális Pontszám (1-100):** Indoklással (1 mondat), a csatorna korábbi retention-adatai
  alapján: melyik hook-típusba tartozik, és az a típus hogyan teljesített korábban?
- **Pontos Időkód:** tól-ig formátumban (pl. 00:12:30 - 00:13:05)
- **Szöveg:** Pontos idézet a leiratból. Ha mondat félbeszakad, keresd meg a gondolat végét!
- **Típus:** Személyes vallomás / Mítoszrombolás / Megdöbbentő statisztika / Azonosulás / Egyéb
- **30mp teszt:** Belefér-e 30 másodpercbe? (Ha nem, hol vágnád rövidebbre?)

**Fontos:** Csak olyan részt válassz, ami önmagában értelmes, kerek egész, vagy erős
kérdéssel/állítással zárul.
