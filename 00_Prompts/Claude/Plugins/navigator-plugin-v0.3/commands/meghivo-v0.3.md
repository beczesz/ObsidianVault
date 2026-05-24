---
description: Meghívólevél és felkészülési kérdések generálása egy podcast epizódhoz (v0.3 — cross-referenciával)
allowed-tools: Read, Write, Edit, Bash, Glob, AskUserQuestion
argument-hint: [epizód-szám]
id: 3c7bfbc5-4ca8-45dd-aba8-a5ce8237cc2d
index_schema_version: 1
---

Töltsd be az epizód-előkészítési kontextust: olvasd el a
`${CLAUDE_PLUGIN_ROOT}/skills/episode-prep-v0.3/SKILL.md` fájlt.

## Bemenet

Kérdezd meg a felhasználót az AskUserQuestion tool-lal:

- **Epizód száma** (pl. 47)
- **Vendég neve** (pl. Kovács János)
- **Vendég megszólítása** (pl. János)
- **Epizód témája** (pl. Szorongás a munkahelyen)
- **Epizód mappa elérési útja** (pl. /path/to/EP47/)

## Feladat

### 1. Cross-referencia ellenőrzés (v0.3 újdonság)

Mielőtt a dokumentumokat generálnád, nézd meg a `Synthesis/Podcast/` és `Synthesis/Series/`
mappákat:
- **Szerepelt-e korábban ez a vendég?** Ha igen, olvasd be a korábbi szintézist.
- **Van-e tematikusan kapcsolódó epizód?** Ha igen, jegyzetelj belőle.

Ezeket az információkat használd a felkészülési kérdések gazdagítására
(lásd az episode-prep SKILL.md „Cross-referencia képesség" szekcióját).

### 2. Meghívólevél generálása

Futtasd a `create_meghivo.js` scriptet az episode-prep SKILL.md technikai követelményei szerint.

### 3. Felkészülési kérdések generálása

Futtasd a `create_kerdesek2.js` scriptet. Ha van cross-referencia adat, add hozzá
a kérdésekhez a korábbi epizódokra való hivatkozásokat.

### 4. PDF konverzió

```bash
libreoffice --headless --convert-to pdf meghivo.docx
libreoffice --headless --convert-to pdf kerdesek.docx
```

### 5. Output

Helyezd a fájlokat az epizód mappába:
- `meghivo.docx` + `meghivo.pdf`
- `kerdesek.docx` + `kerdesek.pdf`
