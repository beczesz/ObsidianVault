---
description: Egyetlen epizód Gold Standard szintézisének elkészítése (SRT → Analytics → Synthesis → Tracking)
allowed-tools: Read, Write, Edit, Bash, Glob, AskUserQuestion
argument-hint: [EP-szám, pl. EP27]
id: 08981ec1-d590-427a-a204-d0d932cebaa1
index_schema_version: 1
---

Töltsd be az epizód-szintézis kontextust: olvasd el a
`${CLAUDE_PLUGIN_ROOT}/skills/episode-synthesis-v0.3/SKILL.md` fájlt.

## Bemenet

1. Ha van megadott argumentum (`$ARGUMENTS`), használd azt az epizód azonosítójaként.
   Ha nincs, kérdezd meg a felhasználót az AskUserQuestion tool-lal:
   - **Melyik epizódot dolgozzuk fel?** (EP szám vagy sorozat + EP szám)
2. Olvasd be a `Synthesis/plan.md`-t a Navigátor Podcast mappából — állapítsd meg,
   hogy az adott epizód kész-e már.

## Feladat

Kövesd az `episode-synthesis-v0.3` SKILL.md 5 fázisát:

### A. SRT olvasás
- SRT megkeresése: `references/srt-mapping.md` alapján
- SRT feldolgozás a SKILL.md Python scriptjével
- TELJES átirat elolvasása (ne ugorj át részeket!)

### B. YouTube Studio analytics (ha elérhető)
- Chrome MCP-vel navigálj a videó analytics oldalára
- Overview, Reach, Audience, Comments adatok kinyerése
- Ha nincs Chrome MCP: jelezd és folytasd tartalom-alapú szintézissel

### C. Szintézis megírása
- Sablon: `references/quality-criteria.md`
- Minőségi cél: >4000 bytes (Deep), ideálisan >10000 (Benchmark/Gold Standard)
- Fájl mentése: Navigátor Podcast/Synthesis/Podcast/ (vagy Series/ ha sorozat)

### D. szintézis.md frissítése
- Ha van általános mintát erősítő/cáfoló adat: írd be

### E. plan.md frissítése
- Epizód sor → ✅ KÉSZ

### F. Progress update
Az elkészülés után írd ki:
```
✅ EPXX szintézis kész (XXXX bytes, [minőségi szint])
Összesen: XX/62 epizód feldolgozva
```
