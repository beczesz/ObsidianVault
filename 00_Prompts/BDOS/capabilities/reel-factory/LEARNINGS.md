---
title: Reel Factory — Learnings
date: 2026-05-27
author: Becze Szabolcs
status: living
description: Iteratív tanulási napló a Reel Factory használatából. Minden nem-triviális próba / hiba / felfedezés után új bejegyzés, hogy a pipeline és a defaults streamline-olódjanak. Ha egy tanulság már beépült a kódba / CLAUDE.md-be, jelöljük "→ kódban" megjegyzéssel.
id: bdd17f96-9c96-46ea-bd81-bdb20a52fa69
index_schema_version: 1
---

# Reel Factory — Learnings

Formátum: minden iteráció kapja meg a saját szekcióját. Cél: a tanulások ne a fejünkben legyenek, hanem itt — és ha visszatérő, akkor be is épüljenek a default-okba (`scripts/reel.py` vagy `CLAUDE.md`).

---

## Iteration template

```markdown
### Iter <N> — <YYYY-MM-DD> — <slug>

**Forrás:** <YT URL> · <epizód címe>
**Cél:** <mire ment ki — milyen platform, milyen üzenet>
**Params:** `--start MM:SS --end MM:SS --aspect 9:16 --music X --music-vol Y --model medium`

**Ami jól ment:**
- ...

**Ami beragadt / rossz lett:**
- ...

**Fix / workaround:**
- ...

**Skill-szintű változtatás:**
- [ ] reel.py — <mit változtassunk?>
- [ ] CLAUDE.md — <új default / open question lezárás?>
- [ ] README.md — <új tipp / hibakeresés sor?>
- [x] csak ezt az iterációt érintette, nincs skill-szintű hatás
```

---

## Iterations

### Iter 5 — 2026-05-28 — Szisztematizálás: methodology + storage + publish

**Trigger:** A v3 reel jóváhagyva mint standard. A felhasználó 5 pontban kérte a folyamat rögzítését:
1. Methodology mentése (reprodukálhatóság)
2. Template-ek a capability-ben, deliverable-ek a területek saját mappáiban
3. Minden reel külön subfolder: videó + PUBLISH.md (cím, leírás, tagek platformonként)
4. Workflow: teljes pontos SRT-ből indul, ha nincs → kérd
5. Deliverable → `előkészített` státusz, ő publikál

**Mit csináltam:**
- [x] [METHODOLOGY.md](METHODOLOGY.md) — kanonikus reprodukálható módszer (alapelvek, pipeline, defaults, tárolás, életciklus, egylapos recept)
- [x] reel.py `publish` subcommand — per-reel deliverable folder az area mappájában + scaffold PUBLISH.md
- [x] [CLAUDE.md §5 Tárolási konvenció](CLAUDE.md) — capability=template+script+scratch, deliverable=area-mappa
- [x] EP43 első deliverable: `02_Areas/Navigátor Podcast/Episodes/EP43 .../Reels/reel-01-anyu-nezd-magadra/` (videó + kitöltött PUBLISH.md, státusz: előkészített)
- [x] Scratch takarítás (debug PNG-k, v1/v2 reel, teszt fájlok törölve)

**Storage modell (kulcs-tanulság):**
A reusable (template, script, outro, zene) a capability-ben él és commit-olható. A **specifikus, legenerált** anyag (reel + metadata) a **TERÜLET** mappájába kerül — minden egységnek saját helye (Navigátor: `Episodes/EP<NN>/Reels/`). Ez a separation of concerns: az agent generikus, a tartalom domain-specifikus.

**Skill-szintű változtatás:**
- [x] reel.py — `publish` subcommand + `PUBLISH_TEMPLATE` (→ kódban)
- [x] METHODOLOGY.md (új kanonikus doksi)
- [x] CLAUDE.md §5 + struktúra-blokk + open questions frissítve

---

### Iter 3 + 4 — 2026-05-27 — STANDARD REEL: full pipeline working

**Cél:** A user-jóváhagyott szabványos reel-formátum első kompletten generált változata. v3 fájl: [`output/navigator-test-01/reel-navigator-test-01-v3.mp4`](output/navigator-test-01/reel-navigator-test-01-v3.mp4) (6.6 MB, 39.93 sec).

**Az alkalmazott pipeline:**
1. `extract-subs` a teljes EP43 SRT-ből (0:00-0:37) → 5 entry
2. **Word-fragment splitter** (max 3 szó / fragment) → 25 fragmens karaoke-style
3. `compose` a reframed.mp4-en + title pill (`„Anyu, nézd magadra"`, 3.5s) + outro concat

**Implementált új funkciók:**
- [x] `split_entry_to_fragments` — proporcionális időzítéssel
- [x] `extract-subs --max-words-per-frag N` (default 3)
- [x] `compose --outro <path>` (default `assets/templates/outro-v0.mp4`)
- [x] `append_outro` — concat demuxer codec-copy (gyors, frame-pontos)

**Hiba & fix — filter_complex concat:**
A koncepcióm szerinti megoldás (`filter_complex "[0:v][0:a][1:v][1:a]concat=n=2:v=1:a=1[v][a]"`) **EINVAL-lal elszállt**, pedig a két stream-spec azonos volt. A "concat demuxer" (`-f concat -safe 0 -i list.txt -c copy`) egyszerűen működött, ráadásul gyorsabb is (~0.6 sec vs ~5 sec re-encode). Always-prefer-demuxer ha a specifikációk megegyeznek.

**Default outro auto-applied:**
A `compose` és `full` is alapból az `assets/templates/outro-v0.mp4`-et fűzi a végéhez. `--outro none` paranccsal kapcsolható ki.

**Verifikáció — frame-ek:**
| t (sec) | Tartalom |
|---|---|
| 0.5-1.5 | Title pill „Anyu, nézd magadra" + subtitle "És bejött hozzám" stb |
| 5 | „hát ilyen nagyon" (3-szavas fragment) — title eltűnt |
| 15 | „lévén, hogy amúgy" |
| 25 | **Wide two-shot** (host + vendég) — a forrásban van kameravágás, mi átengedjük → vizuális változatosság |
| 35 | „nem tudok rajta" — még main video |
| 37.5 | Fehér háttér + kicsi iránytű (outro start) |
| 39 | Full Navigátor logo (outro end) |

**Vesszőparipa: a v3 az új standard.** A `compose` és `full` mostantól default-ban produkál ilyen reel-t — title, fragmens-subs, outro mind benne van. Csak a `--title "..."` és a `--full-srt <path>` flag-ek kellenek a `full`-hoz, az outro auto.

**Skill-szintű változtatás:**
- [x] reel.py — `fragment_entries` + `split_entry_to_fragments` (→ kódban)
- [x] reel.py — `--max-words-per-frag` flag default 3 (→ kódban)
- [x] reel.py — `append_outro` concat demuxer (→ kódban)
- [x] reel.py — `--outro` flag default `assets/templates/outro-v0.mp4` (→ kódban)
- [x] reel.py — `_resolve_outro` helper a 'none' string + nem létező path-okhoz

**Open / further-tuning:**
- [ ] Subtitle font: Segoe UI Black sikertelen volt (libass nem találta?), Arial Bold használunk. Még tesztelni más alternatívákat.
- [ ] Subtitle hátteret próbálni `BorderStyle=4` (semi-transparent box) — Opus-szerűbb lehet
- [ ] Fragment-időzítés: most szigorúan proporcionális szám szerint, de a tényleges szótár-hosszúság szerint pontosabb lehetne ("delíriumos" hosszabb mint "és")
- [ ] Source törlés-prompt aktiválható → epizód kész, reelek mind kimentek?

---

### Iter 2.C — 2026-05-27 — Outro template kivágás + frame-accuracy fix

**Trigger:** A felhasználó megadta a Navigátor YT Shorts [XJXbaFW0HJ0](https://www.youtube.com/shorts/XJXbaFW0HJ0) videót outro-forrásnak, "51 másodperctől" — de a videó csak 39.6s hosszú volt.

**Megoldás:** A teljes videót letöltöttem (1080×1920 / 25 fps / 39.6s / 11 MB), frame-szondázással azonosítottam a beszélő → fehér-háttér átmenetet, és pontosan onnan vágtam. A találgatott "51" valószínűleg "36" volt (transposition).

**Atmenet-detektálás:** Az első próbáknál a frame-szondázáshoz `-ss N -i SRC` (input seek) kombinációt használtam, ami **keyframe-snap**-pelt — pontatlan eredményeket adott. Pontos frame-szintű detektáláshoz a `select='eq(n,N)'` filter szükséges, ami minden frame-et megnéz és csak az N-ediket írja ki.

**Frame-szintű eredmény:**
| Frame | t (sec) | Tartalom |
|---|---|---|
| 917 | 36.68 | speaker még |
| **918** | **36.72** | **white-bg + logo (átmenet)** |

**Hiba 1 — `clip` subcommand input-seek:**
A `cmd_clip` `-ss BEFORE -i` használt → keyframe-snap, nem frame-pontos. Outro vágásnál a 36.65-os kérés egy korábbi keyframe-hez snap-pelt, és az első frame a beszélőt mutatta, nem az outro-t.

**Fix:** `-ss` áthelyezése `-i` UTÁN → output-seek, ami frame-pontos (de lassabb).
→ kódban: `cmd_clip` átírva, kommenttel a tradeoff dokumentálva.

**Hiba 2 — Frame-szondázásnál is keyframe-snap:**
`ffmpeg -ss N -i SRC -frames:v 1` szintén keyframe-snap-pel. Pontos szondázáshoz `-vf "select='eq(n,N)'"`.

**Új output:** [`assets/templates/outro-v0.mp4`](assets/templates/outro-v0.mp4) (184 KB, 2.89 sec, fehér bg + Navigátor logo animáció). [`TEMPLATES.md`](assets/templates/TEMPLATES.md) dokumentálva.

**Iter 4 javaslat:** új `compose --outro <path>` flag a Reel Factory-ba — minden reel végéhez automatikusan concat-olja az outro-t. Vagy új `append-outro` subcommand.

**Skill-szintű változtatás:**
- [x] reel.py `cmd_clip` — output-seek frame-pontossághoz (→ kódban)
- [x] `assets/templates/outro-v0.mp4` + `TEMPLATES.md` (új template)
- [ ] reel.py `compose` — új `--outro` flag (Iter 4)
- [ ] Frame-szondázás helper subcommand? `reel.py probe-frame N` (talán overkill, kézzel is megy)

---

### Iter 2.B — 2026-05-27 — Teljes-SRT ground truth (workflow expansion)

**Trigger:** A felhasználó feltöltötte a teljes EP43 SRT-t a Navigátor Podcast / Episodes mappába, és kérte hogy ezt mindig használjuk forrásként. Ezzel **két komoly hibát is felfedeztünk**:

**Hiba 1 — Opus AI-cím faktuálisan rossz:**
- Opus: `Évekig kereste az eltűnt férjét`
- Valóság (SRT + ChatGPT jegyzet): Farkas Kinga 18 évesen az **édesanyját** vesztette el. Sem férj, sem apa — **anya**.

**Hiba 2 — A saját v0.1 reel beégetett felirata HALLUCINÁLT:**
- A mi Whisper output-ja: `"…és ennek korláttam utoljára"` (≈ "I scolded him for the last time")
- Teljes SRT (ground truth): `"…És én ekkor láttam utoljára."` (= "And I last saw her then")
- **Más jelentés**, más érzelmi súly, más rejtett szereplő. Ez **kerülhetett volna ki publikálva is** — egész más üzenettel mint amit valójában mond.

**Új workflow rule (CLAUDE.md §0):** A teljes epizód SRT MINDIG required input. Forrás:
- Felirat ground truth
- Cím-generálás kontextusa
- Leírás forrása
- Burned-in subtitle nyersanyaga (a saját Whisper helyett)

**Skill-szintű változtatás:**
- [x] CLAUDE.md §0 — Új workflow rule (Teljes SRT mindig required input)
- [ ] reel.py — új subcommand: `extract-subs <full_srt> --start --end --out <clipped_srt>` (Iter 3)
- [ ] reel.py compose — ha `--full-srt` + `--start` + `--end` flag, automatikusan kihúzza és időzíti a klip-relatív SRT-t
- [ ] reel.py — új subcommand vagy compose-flag: `--title "..."` — title-card overlay (Iter 3, Opus elemzésből)

**Tanulság:**
A retrieval-based cognition elve (BDOS alapelv: agentek **nem emlékeznek, visszakeresnek**) **éppen erre való**: a teljes SRT a "vault-szintű igazság", a Whisper-output meg "ad-hoc generálás" amit *ellenőriztetni kell*. A workflow most explicit lett.

**Ezzel az iter 1 reel-ünk hibás** — a beégetett szöveg nem felel meg a tényleges szavaknak. A javítás:
- Iter 3 implementáció után **újrageneráljuk** a `navigator-test-01` reel-t a helyes SRT-vel
- A régi `reel-navigator-test-01.mp4` **NEM mehet publikálásra** (deprecated)

**Új cím-javaslat (verifikált, v2):** [`compare/opus-z-2026-05-27/TITLE_AND_DESCRIPTION_v2.md`](compare/opus-z-2026-05-27/TITLE_AND_DESCRIPTION_v2.md)

Ajánlott: **„Anyu, nézd magadra"** — a saját autentikus idézet a klipben, provokatív/kíváncsiság-keltő, Navigátor brand-konform (max 4 szó), és valódi (nem Opus-fantázia).

---

### Iter 2 — 2026-05-27 — Opus reel referencia-elemzés (`compare/opus-z-2026-05-27/`)

**Forrás:** `C:/Users/EvoComputers/Downloads/z.mp4` — Opus Clip output ugyanabból a Navigátor epizódból, ahonnan iter 1-et csináltuk (44.5s, 1080×1920, 8 Mbps)
**Cél:** Opus reel vizuális + szöveges elemzése, hogy a Reel Factory default-jait közelítsük az ipari minőséghez.
**Output:** [`OPUS_REFERENCE.md`](compare/opus-z-2026-05-27/OPUS_REFERENCE.md) + [`TITLE_AND_DESCRIPTION_DRAFTS.md`](compare/opus-z-2026-05-27/TITLE_AND_DESCRIPTION_DRAFTS.md) + 12 referencia-frame

**Workflow szabály aktiválva:** felirat-helyesség ellenőrzés (CLAUDE.md §1) — átolvastam a Whisper SRT-t, és listáztam a hibákat (`korlágtam`→`korholtam`, `mézsz`→`mész`, `kéltem`→`keltem`, `eképzelni`→`-e képzelni`).

**Megfigyelések (kulcsponti):**

| Dimenzió | Opus | Saját v0.1 | Iter 2+ teendő |
|---|---|---|---|
| Subtitle szótördelés | **1-3 szó / fragment, karaoke-style** | Teljes Whisper-szegmensek (5-10 szó) | Word-level timestamp + saját ASS-generálás |
| Subtitle font | Modern bold sans-serif (Inter/Montserrat-szerű) | Arial | Próbáld: Montserrat / Segoe UI Black / Inter |
| Subtitle outline | Nincs heavy outline, csak finom drop shadow | `Outline=2` heavy fekete | `BorderStyle=1, Outline=1, Shadow=1` |
| Subtitle méret | ~14-16% canvas (nagy) | `Fontsize=14` (kis) | 18-22 |
| Subtitle pozíció | Lower third (~25-30% a fenékről) | `MarginV=180` (~17%) | 350-400 |
| Title card (tetején) | Fehér rounded pill, sötét bold sans, 3-4s láthatóság | nincs | Új `--title` feature |
| Reframe | Dynamic crop + zoom-in a klimaxnál, NEM blurred-bg | Blurred-bg | v0.3: face-detection zoom (komplex) |
| Bitrate | 8 Mbps | 1.3 Mbps | 2-3 Mbps elég, IG/TikTok újra-tömörít |

**A LEGNAGYOBB látható különbség:** a szótördelés. Opus 1-3 szavas fragmenseket csinál, mi mondatokat. Ez a v0.1→v0.2 ugrás legnagyobb hatású változtatása.

**Új tanulság — Opus AI-cím-generálása megbízhatatlan magyarra:**
Opus a klip tetejére beégetett `Évekig kereste az eltűnt férjét` — DE a transcript-ben sehol nem hangzik el a `férj` szó, és az iter 1 kontextusból kiderül hogy 18 évesen történt → valószínűbb hogy szülő/apa. Tehát:

- ❌ NEM másoljuk Opus címét naivan
- ✅ Saját címet generálunk a saját Whisper-transcriptből + (ha kell) a felhasználó visszaigazolásával

→ **Workflow következmény:** a `compose` előtt **a Title is külön szabad-szem reviewt kap**, nem csak a subtitle.

**Skill-szintű változtatás (Iter 3 plan):**

1. [ ] `reel.py transcribe` — `--word-level` flag, `--word_timestamps True` Whisper-nek, output `.ass` is a `.srt` mellé
2. [ ] `reel.py compose` — accept `.ass` (Advanced SubStation) input, így natív word-level subs lehet
3. [ ] `SUBTITLE_STYLE` default: font Montserrat/Inter (rendszertől függ), Fontsize=20, BorderStyle=1, Outline=1, Shadow=1, MarginV=380
4. [ ] Új subcommand vagy `compose` flag: `--title "..." --title-duration 3.5` — overlay a top 8%-on white pill bg-vel
5. [ ] Új subcommand: `analyze-clip <video>` — bemenetből kihúzza a Whisper transcript-et + 3-5 cím-javaslatot generál + leírás-template platform szerint. Vault-szintű (`02_Areas/Navigátor Podcast/Marketing/Publications/`-be lehet exportálni)

Iter 3 indítása user-jóváhagyás után. A current iter csak elemzés volt, nem code-változtatás.

---

### Iter 1 — 2026-05-27 — `navigator-test-01` (első end-to-end próba)

**Forrás:** https://youtu.be/1A53BXfdpw0 · Navigátor podcast epizód (azonosító nincs benne a fájlnévben)
**Cél:** end-to-end működik-e a pipeline. 9:16 reel, magyar felirat, zene nélkül.
**Params:** `--start 00:00:00 --end 00:00:37 --aspect 9:16 --model medium --device cpu`
**Output:** `output/navigator-test-01/reel-navigator-test-01.mp4` (6.78 MB, 1080×1920, 36.92 sec)

**Forrás-meta:**
- 1.32 GB · AV1 codec · 3840×2160 (4K) · 25 fps · 1:44 óra hossz · AAC audio

**Timing (sub-stage):**
| Stage | Time | Note |
|---|---|---|
| download | ~2-3 perc | net-függő, 1.32 GB |
| clip | 30 sec | AV1→H264 4K re-encode |
| reframe 4K→1080×1920 | 43 sec | blurred-bg filter |
| transcribe (medium, CPU) | **162 sec** | leglassabb lépés |
| compose (burn subs, no music) | 9 sec | |
| **Total (download nélkül)** | **~4 perc** | |

**Ami jól ment:**
- Pipeline ELSŐ próbára végigfutott (a 2 Windows-quirk-fix után). yt-dlp letöltötte 4K AV1-ben.
- A blurred-bg reframe vizuálisan rendben van — a 9:16 vásznon a forrás 16:9 felül-alul blurred sávként, középen az eredeti 1080p szélességben. Profis hatás.
- Whisper magyar `medium` model CPU-n ~95% pontosság, az ékezetek (ő, ű, á, é, í, ó, ú) helyesen renderelődnek a beégetett feliratba.
- A `compose` lépés Windows path-colon escape problémát elkerüli a `cwd`-be-stage-eléssel — működik.

**Ami beragadt / rossz lett:**

1. **Whisper CUDA error.** `medium` model betöltése elhasal: `CUDA error: no kernel image is available for execution on the device`. A telepített PyTorch CUDA build nem kompatibilis ezzel a GPU-val.
2. **Whisper stdout cp1252 crash.** CPU módban a model fut, de Whisper saját `print()`-je elhasal a magyar `ű` karakteren, és emiatt a `.srt` sem íródik ki. `Skipping ... due to UnicodeEncodeError`.
3. **Felirat túl nagy.** `Fontsize=14`-gyel a 8-15 szavas mondatok 3-4 sorba tördelődnek a vásznon — túl sok területet foglal.
4. **Felirat a beszélő arcán.** `MarginV=180` (=180px az alsó éltől) a beszélő arcán landol — feljebb / lejjebb kéne tolni.
5. **Whisper magyar hibák.** Felismert: `eszközterem` (helyesen: `tehetetlen`), `korláttam` (helyesen: `korholtam`). Tulajdonneveknél vagy ritkább szavaknál várható.

**Fix / workaround:**

1. → **kódban**: `cmd_transcribe` default `device=cpu`. CLI: `--device cpu|cuda|auto`, default `cpu`.
2. → **kódban**: `run()` `env_extra` paraméter, `cmd_transcribe` átadja `PYTHONIOENCODING=utf-8`-at a whisper subprocessnek.
3. → **JAVASLAT**: `SUBTITLE_STYLE`-ban `Fontsize=14`→`Fontsize=11` (Iter 2-ben kipróbálni).
4. → **JAVASLAT**: `MarginV=180`→`MarginV=300` (Iter 2-ben kipróbálni).
5. → **workaround**: A `transcribe` és `compose` között *kézzel* át kell olvasni a `subs.srt`-t és javítani a hibákat. README-ben már említve. Hosszú távon: word-prompt initial_prompt (`--initial_prompt "navigátor podcast..."`) javíthatja a context-et.

**Skill-szintű változtatás:**
- [x] reel.py — `device` flag + default `cpu` + `PYTHONIOENCODING=utf-8` env_extra (→ kódban)
- [ ] reel.py — `Fontsize` 14→11 default megfontolás (Iter 2 dönti el)
- [ ] reel.py — `MarginV` 180→300 default megfontolás (Iter 2 dönti el)
- [ ] reel.py — `--initial_prompt` támogatás Whisper-hez (későbbi iteráció)
- [x] README — Whisper CUDA / utf-8 hibakeresés sor hozzáadása (TODO most)

**Tanulság a folyamatra:**

A pipeline iteratív tesztelése **lépésenként** sokkal hasznosabb volt mint a `full` mód lett volna: a download-clip-reframe sikeresen lefutott mire a transcribe elhasalt, és **csak a transcribe-ot kellett újra-és-újra próbálni** a fixek után — nem az egész pipeline-t. Ez konfirmálja a subcommand-os design fő motivációját.

**Teljes 5-7 perces feldolgozási idő epizódonként** acceptable — egy podcast epizódból 3-5 reel kihozható kb. 30 percnyi gépi időben (download share-elve). A `large` model nagyobb pontosságú lenne magyarra, de a 162 sec valószínűleg 4-5x szorzóval nőne — nem éri meg ha a kézi `subs.srt` javítás amúgy is szükséges.

---

### Iter 0 — 2026-05-27 — smoke-test (script `--help`)

**Forrás:** —
**Cél:** csak megnézni, hogy a script egyáltalán elindul-e.
**Params:** `python reel.py --help`

**Ami beragadt:**
- `UnicodeEncodeError: 'charmap' codec can't encode character '→'` — a docstringben volt egy `→`, és Windows Python console default cp1252-vel boot-ol, nem utf-8-cal. Bárhol ASCII feletti karakter (`→`, magyar ékezetek `print()`-ben) bukik.

**Fix:**
- A script tetején `sys.stdout.reconfigure(encoding="utf-8")` (és stderr is). Lásd `scripts/reel.py` 12–16. sor.
- Try/except, mert `reconfigure` régebbi Python-on / nem-tty stream-en hiányozhat.

**Skill-szintű változtatás:**
- [x] reel.py — utf-8 reconfigure beépítve (→ kódban)
- [ ] CLAUDE.md — érintetlen, az `index_schema_version` és `bdos_index` mező sem kell változtatni
- [x] README — már a "Hibakeresés" táblázathoz hozzáadom, hogy ha valaki saját script-et ír mellé, ne lepődjön meg

**Tanulság a folyamatra:**
Windows + Python + non-ASCII output: minden új script tetejére `sys.stdout.reconfigure("utf-8")`. Ez egy general convention, érdemes BDOS-szintű "minden új Python CLI" sablonba is beépíteni — most még nincs sablon, ha lesz, ez legyen benne.

---

## Cross-cutting megfigyelések

*(Ide kerülnek a több iterációt átívelő megfigyelések — pl. "magyarban a `medium` Whisper model rendre rontja a tulajdonneveket, érdemes word-list-tel javítani".)*

### Shorts/Reel hook + retention szabályok (claude-youtube + claude-video skill-értékelésből, 2026-05-28)

Forrás: `~/.claude/skills/youtube/references/shorts-playbook.md` + `repurpose`/`shorts` sub-skillek. Megtartott, reel-factory-ra adaptált szabályok:

- **Hook-quality 3-pillér** (clip-választáskor):
  1. **Scroll-stop 1-3s** — az első 1-3 mp önmagában megállítja a görgetést (pattern-interrupt / kíváncsiság-gap)
  2. **Standalone-worthy** — a klip a teljes epizód nélkül is értelmes (NE igényeljen kontextust)
  3. **Loop setup** — az utolsó 1-2s visszacsatol a nyitásra (zökkenőmentes újrajátszás → magasabb replay-rate)
- **Viewed-vs-Swiped >60% threshold** — ha a várható "viewed" arány <60%, újra kell vágni (gyenge hook / lassú nyitás).
- **Hossz sweet-spot:** 13s (punchy reveal) VAGY 60s (módszertan/storytelling). A **30-45s holt-zóna** kerülendő.
- **Visual change min. 3 mp-enként** — vágás/zoom/felirat-hangsúly. Statikus blurred-bg beszélő-fej önmagában gyenge retention.
- **Reel-cadence:** a legerősebb hook-ú klip MEGY ELSŐRE, a többi 2-3 nap eltartással (Presto runbook §T+1 reel-wave-vel összhangban).

> Megjegyzés: magyar long-form podcast-ra adaptált verziók. A sweet-spot + viewed-threshold átvihető; a US-monetizáció-rész nem.

### `/watch` skill — focused-mode audio bug (2026-05-28)

A `claude-video` (`/watch`) skill `--start/--end` flag-je eredetileg **csak a frame-extraction-t** szűkíti, a Whisper-t NEM — a teljes videó audióját transcribe-olja. Egy 1:44h epizódon lokális CPU-val ez ~24+ perc. **Fix:** az audiót is a range-re vágni transcribe előtt, majd a segment-időket abszolútra tolni. Patch őrizve: [`patches/watch-local-whisper.patch`](patches/watch-local-whisper.patch). Tanulság minden saját yt-dlp+whisper pipeline-ra: **a focused-range-et a transcribe-szakaszra is alkalmazd, ne csak a frame/clip lépésre.**

---

## Beépített tanulások (→ kódban)

*(Ide rövid változás-naplót írunk, ha egy tanulság beépült a default-okba.)*

- 2026-05-27: kezdeti default-ok (Arial 14, fehér/fekete outline, MarginV=180, music-vol=0.15, model=medium, blurred-bg reframe) — alapfeltevés, az első iteráción finomítjuk.
