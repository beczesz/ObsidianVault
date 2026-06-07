---
title: Reel Factory — Methodology
date: 2026-05-28
author: Becze Szabolcs
status: active
version: 1.0
description: A Reel Factory kanonikus, reprodukálható módszertana. Egy YouTube hosszú-formátumú epizódból szabványos reel (title card + karaoke-felirat + Navigátor outro) gyártása, majd publikálásra-előkészített deliverable elhelyezése az adott terület mappájában. Ezt olvassa minden AI/agent, mielőtt reelt készít.
id: 3f13f3a9-e8db-4f05-9bdb-0bf10ce61a36
index_schema_version: 1
---

# Reel Factory — Methodology v1.0

Ez a kanonikus munkamódszer. Az [Iter 3+4 (2026-05-27)](LEARNINGS.md) validálta; a felhasználó jóváhagyta mint standardot. Minden új reel ezt követi.

## 0. Alapelvek (NEM megkerülhető)

1. **A teljes epizód SRT a ground truth.** Mindig abból indulunk ki — soha nem a saját Whisper-generálásból (az hallucinál). Ha nincs SRT → **kérd a felhasználótól**, ad egyet. Részletek: [CLAUDE.md §0](CLAUDE.md).
2. **A capability csak template-eket + scriptet tárol.** A legenerált deliverable-ek az **adott terület saját mappájába** kerülnek (lásd §4 Tárolás).
3. **Minden iterációból tanulunk** → [LEARNINGS.md](LEARNINGS.md). Ami visszatérő, beépül a default-okba.
4. **Felirat-helyesség review a `compose` előtt** kötelező (a fragment-szöveg átolvasása).

## 1. Bemenetek

| Bemenet | Honnan | Kötelező? |
|---|---|---|
| YouTube URL (teljes epizód) | felhasználó | ✅ |
| Teljes epizód SRT | `02_Areas/<terület>/.../EP<NN> .../*.srt` | ✅ (ha nincs, kérd) |
| Klip start/end timestamp | felhasználó vagy AI-javaslat | ✅ |
| Title card szöveg | AI generálja az SRT-ből, user jóváhagy | ✅ |
| Háttérzene | opcionális, `assets/music/` | ❌ |

## 2. Pipeline lépések

A teljes pipeline egyetlen `full` paranccsal lefut, de iteráláshoz külön is futtatható.

### Egyparancsos (standard)

```powershell
python scripts/reel.py full "<YT_URL>" `
    --slug "<projekt>-ep<NN>-<tema>-<sorszam>" `
    --start 00:00:00 --end 00:00:37 `
    --full-srt "<teljes epizód .srt path>" `
    --title "„Idézet a klipből""
# automatikus: word-fragment (3 szó), blurred-bg reframe 9:16, outro concat
```

### Lépésenként (iteráláshoz / finomításhoz)

| # | Parancs | Mit csinál | Default |
|---|---------|------------|---------|
| 1 | `download <URL> --out source.mp4` | yt-dlp best quality | eredeti felbontás |
| 2 | `clip source.mp4 --start --end --out clip.mp4` | frame-pontos trim (output-seek) | re-encode CRF 18 |
| 3 | `reframe clip.mp4 --out reframed.mp4` | 9:16 blurred-bg | aspect 9:16 |
| 4 | `extract-subs <full.srt> --start --end --out subs.srt` | SRT slice + shift + **word-fragment** | max 3 szó/fragment |
| 5 | *(felirat-helyesség review — átolvasod a subs.srt-t)* | — | — |
| 6 | `compose reframed.mp4 --subs subs.srt --title "..." --out reel.mp4` | felirat + title pill + **outro** | outro auto |
| 7 | `publish reel.mp4 --dest <area_reels> --slug <slug>` | deliverable folder + PUBLISH.md | — |

### Whisper fallback (ha nincs teljes SRT)

Ha a felhasználó nem tud SRT-t adni, akkor és csak akkor:
```powershell
python scripts/reel.py transcribe reframed.mp4 --lang Hungarian --model medium --device cpu --out subs.srt
```
**De a kimenetet kötelező átolvasni és javítani** — a Whisper magyarul ~95%, és tartalmilag félrehallhat (lásd Iter 2.B incident).

## 3. Standard defaults (v1.0)

| Paraméter | Érték | Indok |
|---|---|---|
| Reframe | 9:16 blurred-bg | működik bármilyen forrásra |
| Felirat-fragment | max 3 szó | Opus-stílusú karaoke, olvasható scroll közben |
| Felirat font | Arial Bold, Fontsize 18 (~120px) | libass-kompatibilis, vastag |
| Felirat pozíció | MarginV 70 (~lower third) | nem takarja az arcot |
| Felirat outline | Outline 2 + Shadow 2 | olvashatóság bármilyen háttéren |
| Title card | fehér pill, Segoe UI Black, top 6%, 3.5s | Opus-mintára |
| Outro | `assets/templates/outro-v0.mp4` (auto) | Navigátor branding |
| Whisper model | medium, CPU | GPU CUDA inkompatibilis ezen a gépen |

A defaults a `scripts/reel.py` tetején (`SUBTITLE_STYLE`, `TITLE_*`, `DEFAULT_OUTRO`) módosíthatók.

## 4. Tárolás — HOL él mi

> **Kulcs-elv:** A capability `reel-factory/` mappa **template + script + scratch**. A kész deliverable a **TERÜLET saját mappájába** kerül.

```
00_Prompts/BDOS/capabilities/reel-factory/   ← AGENT (capability)
├── scripts/reel.py                          — a pipeline
├── assets/templates/outro-v0.mp4            — reusable brand template
├── assets/music/                            — zene library
├── METHODOLOGY.md, CLAUDE.md, LEARNINGS.md  — doksi
└── output/<slug>/                           — SCRATCH (intermediates, törölhető)
      ├── source.mp4   (1+ GB — reel(ek) kész után törlés-prompt)
      ├── clip.mp4, reframed.mp4, subs.srt
      └── reel-<slug>.mp4  (a kész reel — innen publish-eljük)

02_Areas/<terület>/.../                      ← DELIVERABLE (a terület mappája)
   pl. Navigátor Podcast/Episodes/EP43 .../Reels/
       └── reel-01-<slug>/
           ├── reel-01-<slug>.mp4            — a publikálandó videó
           └── PUBLISH.md                    — cím + platform-leírások + tagek + checklist
```

**Más területnek** (DH, Sonrisa, stb.) ugyanígy: a reel a **saját** mappájába kerül, nem az agent folderbe.

A `publish` subcommand automatizálja: `--dest <area>/Reels --slug reel-NN-<tema>`.

## 5. PUBLISH.md tartalom

A `publish` scaffold-ol egy `PUBLISH.md`-t, amit az AI kitölt:
- **Forrás:** epizód, klip-tartomány, title card szöveg, tartalmi összefoglaló
- **Platformonként:** Instagram/FB Reels, TikTok, YouTube Shorts — caption/cím + leírás + hashtagek
- **Állandó hashtagek:** `#navigátorpodcast #magyarpodcast` (Navigátor brand)
- **Checklist:** melyik platformra ment ki
- **Státusz:** `előkészített` → (publikálás után) a mappa törölhető / archiválható

## 6. Életciklus + törlés-promptok (workflow rules)

A [CLAUDE.md Munkamódszer](CLAUDE.md) szekció részletezi. Röviden:
1. **`source.mp4` törlés-prompt** — amikor kész a reel(ek) egy epizódból, az AI rákérdez (1+ GB).
2. **Reel-mappa törlés** — amikor minden platformra kiment, az AI rákérdez (a videó a platformokon él).
3. **Felirat-helyesség review** — minden `compose` előtt.
4. **Teljes SRT mindig input** — ha nincs, kérd.

## 7. Új epizód — teljes recept egy lapon

```powershell
$cap = "00_Prompts/BDOS/capabilities/reel-factory"
$srt = "02_Areas/Navigátor Podcast/Episodes/EP<NN> .../*.srt"
$reels = "02_Areas/Navigátor Podcast/Episodes/EP<NN> .../Reels"

# 1. Egyparancsos reel-gyártás (working dir: output/<slug>/)
python $cap/scripts/reel.py full "<YT_URL>" `
    --slug "navigator-ep<NN>-<tema>-01" `
    --start <MM:SS> --end <MM:SS> `
    --full-srt $srt `
    --title "„<idézet>""

# 2. Felirat-review (átolvasod a output/<slug>/subs.srt-t)

# 3. Publish a Navigátor episode mappába
python $cap/scripts/reel.py publish `
    "$cap/output/navigator-ep<NN>-<tema>-01/reel-navigator-ep<NN>-<tema>-01.mp4" `
    --dest $reels --slug "reel-01-<tema>" `
    --title "„<idézet>"" --episode "EP<NN> ..." --clip-range "<MM:SS>-<MM:SS>"

# 4. PUBLISH.md kitöltése (AI a teljes SRT kontextusból)
# 5. source.mp4 törlés-prompt
```

## Hivatkozott

- Belépő: [CLAUDE.md](CLAUDE.md)
- Tanulási napló: [LEARNINGS.md](LEARNINGS.md)
- Opus referencia-elemzés: [compare/opus-z-2026-05-27/OPUS_REFERENCE.md](compare/opus-z-2026-05-27/OPUS_REFERENCE.md)
- Template index: [assets/templates/TEMPLATES.md](assets/templates/TEMPLATES.md)
