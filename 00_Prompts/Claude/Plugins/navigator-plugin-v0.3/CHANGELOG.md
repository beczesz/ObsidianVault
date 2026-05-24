# Navigátor Podcast Plugin — Changelog

## v0.3.0 (2026-04-06) — „Intelligens Motor"

### Új skillek
- **episode-synthesis-v0.3** — Az ENGINE.md automatizált skill-változata. Egy epizód teljes
  elemzését vezérli: SRT → Analytics → Szintézis → Tracking frissítés.

### Új commandok
- `/szintezis [EP-szám]` — Egyetlen epizód Gold Standard szintézisének elkészítése
- `/audit-batch [darabszám]` — Batch feldolgozás: a következő N hiányzó epizód automatikus elemzése
- `/csatorna-intelligencia` — A szintézisekből kinyert minták frissítése a plugin kontextusába

### Frissített skillek
- **navigator-context-v0.3** — Új „Csatorna Intelligencia" szekció: 52 epizód teljesítményadataiból
  kinyert minták (közönség, cím-stratégia, thumbnail, hook, SEO). Új reference fájl:
  `csatorna-intelligencia.md` (~5KB, adat-vezérelt guidance)
- **episode-prep-v0.3** — Cross-referencia képesség: ha a vendég/téma korábban szerepelt,
  automatikusan hivatkozik a korábbi szintézisre a felkészülési kérdésekben

### Frissített commandok
- `/cim-v0.3` — Hatékonyság-pontszám (1-10) csatorna-adatok alapján, mobiloptimalizálás (60 karakter)
- `/hook-v0.3` — Retention-adatokkal alátámasztott hook-típusok, „30mp teszt" mező
- `/thumbnail-v0.3` — Mobiloptimalizálás (70%+ mobil nézettség), kérdőjel-stratégia
- `/leiras-v0.3` — Cross-referencia blokk (sorozat-hatás), SEO ellenőrzőlista
- `/idokod-v0.3` — Hook jelölés (★) a cold open kiválasztáshoz
- `/meghivo-v0.3` — Cross-referencia a korábbi szintézisekből

### Verzió-suffix konvenció
- Minden skill és command neve tartalmazza a verziószámot mint suffix (pl. `-v0.3`)
- Ez biztosítja, hogy a régebbi és újabb verziók egyértelműen megkülönböztethetők

### Architektúrális változás
A v0.3 összeköti a pre-publish (metadata generálás) és post-publish (szintézis/analytics)
workflow-kat. A `/csatorna-intelligencia` command biztosítja, hogy a szintézisekből tanult
minták visszatáplálódjanak a metadata-generáló commandokba.

```
Pre-publish                    Post-publish
/cim ←──────────┐         ┌──→ /szintezis
/hook ←─────────┤         │
/thumbnail ←────┤         │
/leiras ←───────┤         │
/idokod ←───────┘         │
                │         │
        csatorna-intelligencia.md
                │         │
                └─────────┘
            /csatorna-intelligencia (frissítés)
```

---

## v0.2.0 (2026-03-15)

### Új commandok
- `/meghivo` — Meghívólevél és felkészülési kérdések generálása

### Új skillek
- **episode-prep** — Epizód-előkészítési workflow (meghívó + kérdések)

### Változások
- Az `/navigator-metadata` egyetlen command szétbontva 5 önálló commandra:
  `/hook`, `/cim`, `/thumbnail`, `/leiras`, `/idokod`
- Mindegyik command önállóan futtatható

---

## v0.1.0 (2026-02-15)

### Első kiadás
- `/navigator-metadata` — Egyetlen command az összes YouTube metaadat generálásához
- **navigator-context** skill — Brand kontextus és YouTube stratégia
