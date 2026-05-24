---
description: Batch szintézis feldolgozás — a következő N hiányzó epizód automatikus elemzése
allowed-tools: Read, Write, Edit, Bash, Glob, AskUserQuestion
argument-hint: [darabszám, pl. 5]
id: 76879bc3-10fb-4411-8b39-c921ff431318
index_schema_version: 1
---

Töltsd be az epizód-szintézis kontextust: olvasd el a
`${CLAUDE_PLUGIN_ROOT}/skills/episode-synthesis-v0.3/SKILL.md` fájlt.

## Bemenet

1. Ha van megadott argumentum (`$ARGUMENTS`), használd darabszámként.
   Ha nincs, kérdezd meg: **Hány epizódot dolgozzunk fel?** (ajánlott: 2-3 per session)
2. Olvasd be a `Synthesis/plan.md`-t — azonosítsd a hiányzó/placeholder epizódokat.

## Feladat

### 1. Prioritási sorrend felállítása

A plan.md hiányzó epizódjaiból válaszd ki a kért számút:
- Először: legtöbb megtekintéssel rendelkezők (legtöbb tanulság)
- Másodszor: tematikus csoportok (hatékonyabb cross-referencia)
- Kérdezd meg a felhasználót: „Ezeket az epizódokat tervezem: EP_X, EP_Y, EP_Z. Jó így?"

### 2. Szekvenciális feldolgozás

**KRITIKUS SZABÁLY: NE indíts párhuzamos agent-eket szintézishez!**
A párhuzamos feldolgozás bizonyítottan placeholder-minőségű eredményt ad.

Minden epizódot egyenként, mélyen dolgozz fel a `/szintezis` command logikája szerint:
1. SRT olvasás + feldolgozás
2. YouTube Studio analytics (ha elérhető)
3. Szintézis megírás (>4000 bytes minimum)
4. Fájl mentése

### 3. Batch-elhető lépések

Az SRT-k szöveggé alakítása batch-ben futtatható (mechanikus munka):
```python
# Először feldolgozni az összes SRT-t szövegfájlokká
for ep in missing_episodes:
    srt = find_srt(ep)
    text = parse_srt(srt)
    save(text, f'EP{ep}_transcript.txt')
```

Utána EGYENKÉNT olvasni és szintetizálni.

### 4. Hatékonysági tippek

- YouTube Studio tab-ot tartsd nyitva — ne zárd be epizódok között
- A szintézis.md-t a session VÉGÉN frissítsd (ne epizódonként)
- A plan.md-t epizódonként frissítsd (tracking)

### 5. Progress tracking

Minden epizód után:
```
📊 Progress: X/Y kész (Z%)
✅ EPXX — Vendég Neve — XXXX bytes
⏭️ Következő: EPYY — Vendég Neve
```

A session végén összesítés:
```
🏁 Session összesítő:
- Feldolgozva: X epizód
- Összesen kész: XX/62
- Következő session-ben javasolt: EPAA, EPBB, EPCC
```
