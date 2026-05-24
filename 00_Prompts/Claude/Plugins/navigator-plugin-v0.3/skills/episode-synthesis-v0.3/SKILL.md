---
name: episode-synthesis-v0.3
description: >
  A Navigátor Podcast epizód-elemző és szintézis-készítő motorja. Használd, amikor
  "szintézis", "epizód elemzés", "episode synthesis", "deep analysis", "audit",
  "batch feldolgozás", "csatorna audit", "ENGINE", "YouTube analytics kinyerés",
  "SRT feldolgozás", "plan.md frissítés", "szintézis.md frissítés", vagy "hány epizód
  kész" témában kap feladatot a felhasználó. Ez a skill a korábbi ENGINE.md automatizált
  változata — egy epizód teljes elemzését vezérli az SRT olvasástól a szintézis megírásán
  át a tracking fájlok frissítéséig. Aktiválódjon akkor is, ha a felhasználó csak annyit
  mond: "csináld meg a következő epizódot" vagy "folytasd az auditot".
version: 0.3.0
id: 34e23e90-2e18-4b81-9bf0-79ead3845033
index_schema_version: 1
---

# Navigátor Podcast — Epizód Szintézis Motor (v0.3)

> **Mi ez?** Az ENGINE.md skill-változata. Automatizálja egy epizód teljes elemzését:
> SRT olvasás → YouTube Studio analytics → szintézis megírás → tracking frissítés.

---

## Kontextus betöltés (minden futásnál)

Mielőtt szintézist írnál, olvasd be ezeket a fájlokat a Navigátor Podcast mappából:

1. `CLAUDE.md` — csatorna identitás, értékek, formátumok
2. `Synthesis/plan.md` — tracking mátrix (melyik epizód kész, melyik nem)
3. `Synthesis/szintézis.md` — utolsó ~50 sor (legfrissebb megfigyelések)
4. Legalább 1 referencia szintézis a `Synthesis/Podcast/` mappából (a legjobb minőségű)

**NFD/NFC encoding probléma:** A macOS két „Navigátor Podcast" mappát hoz létre.
A valódi fájlokat tartalmazó mappa megtalálása:

```python
import os
base = '/sessions/.../mnt'  # a session working dir + mnt
nfd = None
for d in os.listdir(base):
    if 'Navig' in d and 'Podcast' in d:
        full = os.path.join(base, d)
        if os.path.isdir(full) and len(os.listdir(full)) > 10:
            nfd = full
            break
```

Ezt a mintát MINDIG használd — soha ne hardkódold a Navigátor útvonalat.

---

## Epizód kiválasztása

### Prioritás (ha nincs explicit kérés)

1. A `plan.md`-ból keress placeholder/hiányzó epizódokat
2. Válaszd a legtöbb megtekintéssel rendelkezőt (több tanulság)
3. Ha tematikus csoport van (pl. pszichológia klaszter), csoportban dolgozz

### Sorozat vs. Podcast felismerés

Nézd meg a kérést: ha „7 Szokás", „KAW", „Közösség" szó van benne → sorozat-szintézis.
Ha EP szám → podcast-szintézis. A sablonok különböznek! Részletek: `references/quality-criteria.md`

---

## A szintézis 5 fázisa

### FÁZIS A: SRT olvasás

1. **SRT megkeresése:** A `Downloads--Navigátor/srt/` mappában.
   A fájlnév → EP szám mapping: `references/srt-mapping.md`

2. **SRT feldolgozás szöveggé** (Python):

```python
import re

def parse_srt(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    blocks = re.split(r'\n\n+', content.strip())
    result, last_marker = [], -1
    current_time = None
    for block in blocks:
        lines = block.strip().split('\n')
        for line in lines:
            ts = re.search(r'(\d{2}):(\d{2}):(\d{2})', line)
            if ts and '-->' in line:
                current_time = int(ts.group(1))*3600 + int(ts.group(2))*60 + int(ts.group(3))
            elif not re.match(r'^\d+$', line.strip()) and '-->' not in line and line.strip():
                if current_time is not None:
                    marker = (current_time // 300) * 300
                    if marker > last_marker:
                        h, m, s = marker//3600, (marker%3600)//60, marker%60
                        result.append(f"\n\n[{h:02d}:{m:02d}:{s:02d}]\n")
                        last_marker = marker
                result.append(f" {line.strip()}")
    return ''.join(result)
```

3. **Olvasd el a TELJES átiratot.** Ne ugorj át részeket. Közben jegyzetelj:
   - Főbb témablokkok + időkódok
   - Legütősebb idézetek
   - Szabolcs saját hozzájárulásai (nem csak kérdez — ez FONTOS)
   - Potenciális cold open anyagok
   - Kontroverzális vagy meglepő kijelentések

### FÁZIS B: YouTube Studio analytics

Ha van Chrome MCP elérés, nyisd meg a YouTube Studio-t:

1. Navigálj a videó analytics oldalára (video ID: `references/srt-mapping.md`)
2. **Overview tab:** Views, Watch time, Subscribers, AVD, AVD%
3. **Reach tab:** Impressions, CTR, Traffic sources (External, Browse, Suggested, Search)
4. **Audience tab:** Device, Age+Gender, Geography, Subscriber ratio
5. **Comments tab:** Minden komment (szűrő eltávolítása!)

Ha NINCS Chrome MCP: jelezd a szintézisben, hogy „analytics hiányzik, félkész szintézis."
A szintézist így is írd meg a tartalom alapján, de ne találj ki számokat.

### FÁZIS C: Szintézis megírása

A sablon és minőségi követelmények: `references/quality-criteria.md`

**Kritikus szabályok:**
- NE használj párhuzamos agent-eket szintézishez — placeholder-eket gyártanak
- NE becsüld a nézettséget — MINDIG YouTube Studio-ból
- NE hagyd ki Szabolcs gondolatait
- NE írj generic témablokkokat
- Egy session-ben max 2-3 epizódot csinálj MÉLYEN

**Fájl írása:** Használj bash heredoc-ot a temp path-ra, majd Python `shutil.copy2`-vel
másold az NFD Synthesis mappába.

### FÁZIS D: szintézis.md frissítése

Ha az új epizód bármilyen ÁLTALÁNOS mintát erősít vagy cáfol:
- Új közönség-adat ami módosítja a demográfiai képet
- Téma-nézettség korreláció megerősítése
- Új hook/intro minta
- Traffic source minta

### FÁZIS E: plan.md frissítése

Az epizód sorát állítsd ✅ KÉSZ-re a tracking mátrixban.

---

## Batch feldolgozás

Ha egyszerre több epizódot kell feldolgozni:

1. **SRT-ket batch-ben** feldolgozhatod szövegfájlokká (mechanikus munka)
2. **Szintéziseket EGYENKÉNT** írd (NEM batch-elhető — mélység kell)
3. A YouTube Studio tab-ot tartsd nyitva — ne zárd be epizódok között
4. A szintézis.md-t a session VÉGÉN frissítsd (ne epizódonként)
5. Minden epizód után progress update: „X/Y kész (Z%)"

---

## Session-folytonosság

A session végén MINDIG frissítsd:
1. `plan.md` — melyik kész, melyik nem
2. `szintézis.md` — session log szekció
3. Ha félbe marad: írd be melyik fázisnál tartottál

Új session elején: olvasd be a plan.md-t és a szintézis.md session log-ját.

---

## Kapcsolódó plugin skill-ök

A szintézis FÁZIS C részeként a metadata-generáló commandokat is futtasd le:
- `/cim` és `/thumbnail` → hasonlítsd össze a jelenlegi címmel/thumbnaillal
- `/hook` → ha nincs cold open, ez ad anyagot
- Ha az AI javaslat jobb → tedd be a szintézisbe mint „Alternatív javaslat"
