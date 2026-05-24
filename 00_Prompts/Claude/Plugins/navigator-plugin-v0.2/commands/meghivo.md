---
description: Navigátor Podcast epizód előkészítés – meghívó és felkészülési kérdések generálása
allowed-tools: Read, Glob, Bash, AskUserQuestion
argument-hint: [epizód-szám] [vendég-neve]
id: 5632ee76-f2f8-4df2-b698-1c9bcfedce67
index_schema_version: 1
---

Helyezkedj a Navigátor Podcast produkciós asszisztense szerepébe.
Töltsd be az epizód-előkészítési kontextust: olvasd el a `${CLAUDE_PLUGIN_ROOT}/skills/episode-prep/SKILL.md` fájlt.

## Bemenet

Kérdezd meg a felhasználót az AskUserQuestion tool-lal az alábbi adatokért (ha nem adta meg argumentumként):

1. **Epizód száma** (pl. EP45)
2. **Vendég teljes neve** (pl. Kovács János)
3. **Vendég megszólítása** (keresztnév, pl. János)
4. **Epizód témája** (röviden)
5. **EP mappa elérési útja** (ahol a Jocko fordítás fájlok találhatók)

## Feladat: Epizód előkészítés

A `${CLAUDE_PLUGIN_ROOT}/scripts/` mappában lévő scriptekkel generáld le a két dokumentumot:

### 1. Meghívólevél (.docx + .pdf)

```bash
cd /sessions/$(basename $HOME)
node "${CLAUDE_PLUGIN_ROOT}/scripts/create_meghivo.js"
```

### 2. Felkészülési kérdések (.docx + .pdf)

```bash
node "${CLAUDE_PLUGIN_ROOT}/scripts/create_kerdesek2.js"
```

### 3. PDF konverzió

```bash
EP_DIR="[epizód mappa elérési útja]"
libreoffice --headless --convert-to pdf --outdir "$EP_DIR" "$EP_DIR/EP{N} - Meghívó - {Vendég}.docx"
libreoffice --headless --convert-to pdf --outdir "$EP_DIR" "$EP_DIR/EP{N} - Felkészülési kérdések - {Vendég}.docx"
```

## Módosítandó konstansok a scriptekben

Minden új epizódhoz frissítsd a `create_meghivo.js` és `create_kerdesek2.js` fájlokban:
- `VENDEG_NEV` – vendég teljes neve
- `VENDEG_MEGSZOLITAS` – megszólítás (keresztnév)
- `EP_SZAM` – epizód szám
- `EP_DIR` – epizód mappa elérési útja
- `OUTPUT` – kimeneti fájl neve

## Állandó adatok

| Adat | Érték |
|------|-------|
| Kérdőív URL | `https://forms.gle/DHhrhskNd7KXRkgG6` |
| Helyszín | Média Műhely |
| Google Drive mappa ID | `1nurxaGUjqgWAdIGuyoLesaPzawqCWJpx` |
| Template Drive ID | `1XHLMOpg4T079rDLk8baO9lqe-4_q_zwY` |
