---
description: Csatorna-intelligencia frissítése — a szintézisekből kinyert minták aktualizálása
allowed-tools: Read, Write, Edit, Bash, Glob
argument-hint: (nincs argumentum)
id: 5cf67e79-642a-4718-a49c-4b66a6d3281b
index_schema_version: 1
---

Ez a command a pre-publish (metadata) és post-publish (szintézis) világ összekötése.
A szintézisekből kinyert mintákat visszatáplálja a plugin kontextusába, hogy a
`/cim`, `/hook`, `/thumbnail`, `/leiras` commandok a legfrissebb adatokból dolgozhassanak.

## Kontextus betöltés

1. Olvasd be a teljes `Synthesis/szintézis.md` fájlt (a nagy, 70KB+ fájl a Navigátor Podcast mappában)
2. Olvasd be a `Synthesis/plan.md`-t (tracking állapot)
3. Olvasd be a jelenlegi csatorna-intelligencia fájlt:
   `${CLAUDE_PLUGIN_ROOT}/skills/navigator-context-v0.3/references/csatorna-intelligencia.md`

## Feladat: Intelligencia frissítése

### 1. Új minták azonosítása

Hasonlítsd össze a szintézis.md tartalmát a jelenlegi csatorna-intelligencia fájllal:
- Van-e új demográfiai minta? (pl. új téma → más közönség)
- Változott-e a top 10 rangsor?
- Van-e új cím/hook/thumbnail minta, ami működött vagy nem?
- Van-e új traffic source minta?
- Van-e új retention insight?

### 2. Csatorna-intelligencia fájl frissítése

Írd át a `references/csatorna-intelligencia.md` fájlt a legfrissebb adatokkal.
A fájl struktúráját tartsd meg, de a számokat és mintákat frissítsd.

### 3. navigator-context SKILL.md szinkronizálás

A SKILL.md „Csatorna Intelligencia" szekciójában az összefoglaló 3-3 pontot (top működő +
top kerülendő) frissítsd ha szükséges.

### 4. Jelentés

Készíts egy rövid összefoglalót:
```
📊 Csatorna Intelligencia frissítve
- Elemzett szintézisek: XX/62
- Új minták: [lista]
- Változások a top 10-ben: [igen/nem]
- Frissített fájlok: csatorna-intelligencia.md, SKILL.md
```

## Mikor futtasd?

- Minden 5-10 új szintézis után
- Ha a felhasználó azt mondja: „frissítsd az intelligenciát" vagy „mi változott?"
- Automatikusan az `/audit-batch` végén (a szintézis.md frissítése után)
