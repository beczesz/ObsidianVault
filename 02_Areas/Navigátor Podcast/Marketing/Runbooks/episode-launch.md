---
schema: presto.runbook.v1
runbook_id: episode-launch
area: Navigátor Podcast
version: 0.3.0
status: active
date_created: 2026-05-26
date_last_updated: 2026-05-26
owner: Becze Szabolcs
id: e1c8cf27-912f-40c6-a73a-d643644c4cec
index_schema_version: 1
bdos_index: true
description: "Navigátor Podcast epizód-launch runbook v0.3 — egy új epizód publikálásának teljes receptje. T+0 YouTube go-live (16:00 Tue, EP43-on validált) + Facebook personal post + Spotify audio upload (paired), T+1 Reels-hullám (Insta+FB+YT Shorts+TikTok), T+7 follow-up activation, plus Patreon teaser a következő epizódra. v0.3.0: §3.1 Post-publish verification (Chrome MCP YT Studio check, published_unverified fallback, EP43 tanulság), §3.5a MP3 export pipeline (yt-dlp default 192k, alternatívák, best practices), §10 Next-episode jumpstart copy-paste checklist (21 lépés, pre-launch/launch/post-launch/monitoring/spotify-archive fázisok)."
trigger: "Új epizód publikálásra kész (recording done + edited + thumbnail done + plugin-generated YT metadata done)"
typical_publish_day: "Kedd 16:00 (EP43 alapján validált — TBD-01 resolved)"
publications_generated_count: 8
tags: [navigator-podcast, runbook, episode-launch, multi-platform]
---

<!-- 2026-05-26 — v0.1.0 — Initial creation, user-driven first draft -->
<!-- 2026-05-26 — v0.2.0 — EP43 launch 8 operatív tapasztalat beépítve. Módosított §-ok: §1, §2, §3.1, §3.5, §4, §5, §6, §7, §8. Új §-ok: §3.5a, §3.7. -->
<!-- 2026-05-26 — v0.3.0 — Presto audit-fix B+C csomag. §3.1 bővítve: "Post-publish verification" alszekció (Chrome MCP YT Studio check, published_unverified státusz + risk-flag, EP43 cross-link). §3.5a bővítve: "MP3 export pipeline — default workflow" alszekció (yt-dlp primary, alternatívák, best practices). Új §10: "Next-episode jumpstart" — 21-lépéses copy-paste checklist 5 fázisra (pre-launch/launch/post-launch/monitoring/spotify-archive). §6 Iteration history bővítve. Frontmatter: version 0.2.0→0.3.0, description frissítve. -->

# Runbook — Episode Launch (v0.2.0)

> **Cél:** egy új Navigátor epizód maximális elérése a magyar audience-en, builder-tone-on belül maradva. Növelni a nézettséget és a feliratkozó-számot epizód-ról epizódra.

---

## 1. Prerekvizitumok (manuálisan, a runbook elindítása ELŐTT)

Az epizódnak `status: ready_to_publish` állapotban kell lennie. Ez azt jelenti:

| # | Prerekvizitum | Ki csinálja | Mivel |
|---|---|---|---|
| 1 | Epizód felvéve + vágva | User (vagy editor) | Manuális |
| 2 | SRT generálva | User | Manuális (külső eszközzel) |
| 3 | Thumbnail kész | User | Canva / Photoshop |
| 4 | YT metadata generálva (cím, leírás, hashtagek, időkód, hook) | User + Navigator Plugin | `/cim`, `/leiras`, `/idokod`, `/thumbnail`, `/hook` skillek |
| 5 | YT publish_date + publish_time kitűzve | User | (tipikusan kedd 16:00 — lásd §7 TBD-01 resolved) |
| 6 | Reel-vágás kész (T+1 wave-hez) | User (vagy editor) | Manuális, intro-szegmensből |
| 7 | **Fact-check pass elvégezve** | User | Minden numerikus és faktikus állítás (kor, dátum, statisztika) cross-check legalább 2 forrásból. EP43 tanulság: "17 évesen" vs "18 évesen" eset — a Spotify-leírásban végig "18 éves" (helyes), a podcast-leírás-draft-ban "17" szerepelt. Publish előtt kötelező ellenőrzés. |

**Workflow gate:** ha a 7 prerekvizitum bármelyike hiányzik, a runbook **NEM indítható**. A Seed `## Prerequisites checklist` szekciójában explicit jelölni kell mindegyiket.

---

## 2. Generált publikációk — overview

A runbook **8 db Publication-t** generál, mind a Navigátor Area `Publications/` vagy `Campaigns/<ep-id>-launch/publications/` mappában.

| # | T+ | Channel | Publication-type | Owner | Action | Pub-fájl naming |
|---|---|---|---|---|---|---|
| 1 | T+0 (Tue 16:00) | youtube | episode_full | User | go-live (manuális) | `pub-youtube-<YYYY-MM-DD>-001.md` |
| 2 | T+0 (Tue PM, ~5 min után YT-live) | facebook | personal_post_with_thumbnail | User | manuális post (FB API hiány) | `pub-facebook-<YYYY-MM-DD>-001.md` |
| 3 | T+1 (Wed) | instagram | reel_intro_cut | User | manuális Reel upload | `pub-instagram-<YYYY-MM-DD>-001.md` |
| 4 | T+1 (Wed) | facebook | reel_intro_cut | User | manuális Reel upload | `pub-facebook-<YYYY-MM-DD>-002.md` |
| 5 | T+1 (Wed) | youtube_shorts | shorts_intro_cut | User | manuális Shorts upload | `pub-youtube-<YYYY-MM-DD>-002.md` |
| 6 | T+1 (Wed) | tiktok | tiktok_intro_cut | User | manuális TikTok upload | `pub-tiktok-<YYYY-MM-DD>-001.md` |
| 7 | T+7 (next Tue) | youtube_community | followup_activation | User | manuális Community post | `pub-youtube-community-<YYYY-MM-DD>-001.md` |
| 8 | T+7 (next Tue) | facebook | followup_activation | User | manuális FB post | `pub-facebook-<YYYY-MM-DD>-003.md` |
| (+) | T+0 (paired) | spotify | audio_re_upload | User | manuális Spotify upload | `pub-spotify-<YYYY-MM-DD>-001.md` |
| (+) | T+X | patreon | next_episode_teaser | User | manuális, insider-only | `pub-patreon-<YYYY-MM-DD>-001.md` |
| (+) | T+0…T+30 (daily) | all | stats_check | User | §3.7 monitoring | — |

**Paired action naming-convention (v0.2.0 új):** a Spotify audio upload és a Patreon teaser **külön Publication-fájlt kap**, frontmatterben `runbook_step: T+0 paired` (vagy `T+X paired`) jelöléssel. Ez megkülönbözteti az önálló T+ wave-lépésektől, de biztosítja hogy a publikációk state-je nyomon követhető. Lásd: `pub-spotify-2026-05-26-001.md` mint referencia-példa.

A daily stats check **nem önálló Publication** — §3.7 monitoring cadence-re l. részletesen.

---

## 3. Részletes lépések

### 3.1 T+0 — YouTube go-live (Step 1)

**Channel:** YouTube (primary, Navigator-YT DNA)
**Owner:** User (Becze Szabolcs)
**Publication-id sablon:** `pub-youtube-<YYYY-MM-DD>-001`

**Content-szabályok:**
- Cím: Navigator Plugin `/cim` skill outputja, jóváhagyva
- Leírás: Navigator Plugin `/leiras` skill outputja + állandó link-blokk (lásd `Synthesis/new_video_checklist.md` Fázis 3)
- Időkódok: `/idokod` skill outputja
- Thumbnail: max 4 szó, magas-kontraszt (Navigator-YT DNA §4)
- Hashtagek: `#NavigátorPodcast #MagyarPodcast` + epizód-specifikus 2-3 hashtag

**Időzítés:** **Kedd 16:00** — TBD-01 resolved, EP43-on validálva (lásd §7).

**Presto action:** monitor + log publish_event. Nincs autonóm publikálás.

**Offline-prep alternative workflow (v0.2.0 új — EP43 tapasztalat):**

Ha a user a metaadatokat offline, közvetlenül YouTube Studio-ban készíti el (Navigator Plugin + manuális editálás YT Studio-ban), az alábbi folyamat az érvényes:

1. User a Navigator Plugin skill-jeit (`/cim`, `/leiras`, `/idokod`, `/thumbnail`, `/hook`) futtatja és az outputot YT Studio-ba másolja + manuálisan szerkeszti
2. User ütemezi a videót YT Studio-ban (`scheduled` állapot)
3. Presto **Chrome MCP read-back**-et végez: megnézi a YT Studio-t és a pub-fájl state-jét szinkronizálja a valósággal
4. Stage-átugrás megengedett: `prepared → scheduled` (vagy akár `draft → scheduled`) egyetlen state-sync lépéssel, ha a YT Studio-ban a videó már `scheduled` állapotban van. Az approval-trail-be rögzíteni kell: "user offline-prepared, YT Studio scheduled, Presto state synced via Chrome MCP read-back"

**Anti-pattern:** ne várj explicit Presto-approve lépésre, ha a user YT Studio-ban már elvégezte az összes szerkesztést és ütemezést.

#### Post-publish verification (v0.3.0 új)

A go-live után **5-10 percen belül** Presto Chrome MCP-vel elvégzi a post-launch ellenőrzést:

**Ellenőrzési lépések:**

1. Presto Chrome MCP-vel megnyitja a YT Studio Video Details oldalt az epizód video_id-jával
2. Ellenőrzi: `Visibility: Public` (nem Private, nem Unlisted)
3. Ellenőrzi: a cím és leírás pontosan az approved verzió (nem maradtak draft változatok)
4. Ellenőrzi: thumbnail feltöltve és megjelenik (nem default)
5. Screenshotot ment a publish trail-be: `Marketing/Campaigns/<ep-id>-launch/publish-trail/yt-studio-post-launch-<YYYY-MM-DD-HHmm>.png`

**PASS:** pub-fájl `publication_status: published` státuszba kerül, az `## Analytics` szekció Day 0 snapshot slot nyílik.

**FAIL (nem public / thumbnail hiányzik / cím nem stimmel):**
- Pub-fájl `publication_status: published_unverified` státuszba kerül
- Presto risk-flag-et helyez el a pub-fájl `## Notes` szekciójában: `risk: post-publish-check-failed — <konkrét hiba>`
- Azonnali user-riasztás chatben: "YT go-live verify FAILED — [hiba leírása] — manuális ellenőrzés szükséges"
- A wave (T+0 FB post) csak user manuális jóváhagyásával folytatható

**EP43 tanulság (cross-link: Sage learning `verify-before-trust-after-publish`):** EP43 launch-nál a go-live után egy apró szerkesztési hiba maradt a leírásban ("17 évesen" vs "18 évesen"). A post-publish verify lépés bevezetésének célja, hogy az ilyen csúszások a launch utáni 10 percen belül kiderüljenek — amikor még nincs tömeg a videón, és a javítás fájdalommentes.

**Success criteria (24h):**
- Views > csatorna átlag első 24h
- CTR > 5% (channel.md baseline)
- Retention > 35% első 30 perc

---

### 3.2 T+0 — Facebook personal post (Step 2)

**Channel:** Facebook (Navigator-FB DNA — TBD, még nincs)
**Owner:** User
**Publication-id sablon:** `pub-facebook-<YYYY-MM-DD>-001`

**Időzítés:** YT go-live után ~5 percen belül.

**Content-szabályok:**
- Egy mondatos **személyes** leírás (builder-tone, NEM clickbait)
- Thumbnail-kép csatolva
- Link a YT videóra
- Magyar nyelven
- Hashtag: 1-2 max (FB-on nem fontosak)

**Példa sablon (placeholder, epizódonként testreszabva):**
> *"Új epizód: [Vendég neve]-val beszélgettem [téma]-ról. Számomra a legfontosabb pillanat az volt, amikor [1 mondat hook]. Belenézel? 👇"*
> [thumbnail] [link]

**Presto action:** `/pres-draft pub:pub-facebook-<date>-001` → user iterál + approve → user manuálisan posztol.

**Success criteria (48h):**
- Reach > 500 organic
- Click-through > 3%

---

### 3.3 T+1 — Reels hullám (Steps 3-6)

**Másnap (szerdán reggel/délelőtt).** 4 platformra ugyanaz a Reel: az epizód **intro szegmense** (első 30-60 másodperc, vagy a legerősebb hook-pillanat).

**Content-szabályok mindegyikre:**
- 9:16 vertikális (vagy 1:1 IG-specifikusra adaptálható)
- 30-60 másodperc
- Burned-in subs (magyar)
- Sound-on optimalizált
- Záró frame: "Teljes epizód a Navigátor csatornán → link a bio-ban / leírásban"

**Platform-specifikus eltérések:**

| Channel | Pub-id | Caption hossz | Hashtagek | DNA file |
|---|---|---|---|---|
| Instagram Reels | `pub-instagram-<date>-001` | rövid (1-2 mondat) | 5-10 (mix branded + topic) | Navigator-IG (TBD) |
| Facebook Reels | `pub-facebook-<date>-002` | személyes (2-3 mondat) | 1-2 | Navigator-FB (TBD) |
| YouTube Shorts | `pub-youtube-<date>-002` | rövid cím + 1 mondat description | 2-3 | Navigator-YT §4 Shorts caveat |
| TikTok | `pub-tiktok-<date>-001` | rövid + emoji-erős | 3-5 (#NavigátorPodcast + topic) | Navigator-TT (TBD) |

**Presto action:** `/pres-draft` minden 4-re, párhuzamosan. User iterál + approve. **Manuális upload mind a 4-en.**

**Success criteria (24h):**
- IG/FB/TT: kombinált views > 1500
- YT Shorts: views > 500 (channel.md baseline: 17.8% views, 0.4% watch time)

---

### 3.4 T+7 — Follow-up activation (Steps 7-8)

**A következő kedden** (1 héttel a launch után). Cél: aktivizálni azokat, akik még nem nézték meg.

**Step 7 — YouTube Community post:**
- Channel: YouTube Community tab
- Content: kérdés a közönségnek az epizód témájáról (pl. "Te találkoztál már ambiguous loss-szal? Mi segített?")
- Link a videóra
- Pub-id: `pub-youtube-community-<date>-001`

**Step 8 — Facebook follow-up post:**
- Channel: Facebook
- Content: rövid emlékeztető + 1-2 kulcs-gondolat az epizódból (idézet vagy insight)
- Link a YT videóra
- Pub-id: `pub-facebook-<date>-003`

**Presto action:** `/pres-draft` mindkettőre, T+5 napon (előrejelzéssel). User approve T+6 → publish T+7.

**Success criteria (48h):**
- YT Community: 50+ reakció
- FB: reach > 300 organic
- Trafic-bump: a YT epizód-videóra +10% view T+7 és T+10 között

---

### 3.5 Patreon — Next-episode teaser (paired action)

**Időzítés:** T+0 és a következő epizód launch-a között valamikor (TBD: optimum még nincs).

**Channel:** Patreon (Navigator-Patreon DNA — TBD)
**Audience:** Insiders only
**Content:**
- Rövid betekintés a következő epizódba: ki a vendég, miért választottam, mit várok
- Loyalty-reward: "te tudod meg először"

**Pub-id:** `pub-patreon-<date>-001`

**Paired action:** ezzel egyidejűleg a következő epizód Seed-jét is el kell készíteni (lásd MARKETING_OS_FLOW_v2.md Seed lifecycle).

**Presto action:** `/pres-draft pub:pub-patreon-<date>-001` — user iterál + approve → manuális Patreon-post.

---

### 3.5a Spotify — Audio upload (T+0 paired action)

**Időzítés:** T+0 napon, YT go-live közelében (± 30 perc). Pub-fájl: `pub-spotify-<YYYY-MM-DD>-001.md`, frontmatterben `runbook_step: T+0 paired`.

**Channel:** Spotify / Spotify for Podcasters (podcasters.spotify.com)
**Owner:** User (manuális — Spotify API nincs konfigurálva)
**Pub-type:** `audio_re_upload` — az YT-videó audio extractje MP3-ban

**Előkészítés:**
- MP3 export az YT-fájlból (192 kbps+) — lásd részletesen alább
- Spotify leírás = YT-leírás adaptált verziója (YT-specifikus linkek cserélve, `runbook_step: T+0 paired` jelölve)
- Időkódok Spotify Chapters formátumban (`HH:MM:SS Cím` — Spotify 2023 óta natívan támogat)

#### Default workflow — HD-videó letöltés (v0.4.0, EP36 tapasztalat) ⭐

> **Tanulság az EP36 archív-feltöltésből (2026-05-28):** A Spotify for Creators **videó-podcastot is fogad** — nem kell MP3-at extraktálni. A legegyszerűbb és bevált folyamat:

1. **Presto letölti a YT-videót HD (1080p) minőségben** yt-dlp-vel, NEM Drive-synced mappába (a vault Google Drive-on van — egy 300+ MB-os tranziens fájl ott felesleges nagy szinkront indít):
   ```bash
   mkdir -p ~/Downloads/navigator-ep<NN>
   cd ~/Downloads/navigator-ep<NN> && yt-dlp \
     -f "bestvideo[height<=1080]+bestaudio/best[height<=1080]" \
     --merge-output-format mp4 \
     -o "EP<NN>-<vendeg>-%(id)s.%(ext)s" \
     "https://youtu.be/<VIDEO_ID>"
   ```
   - Méret-benchmark: ~2 órás epizód 1080p ≈ 340 MB
   - `~/Downloads/` Finder-ből elérhető a feltöltéshez, NEM Drive-synced, könnyen törölhető
2. **A USER tölti fel** manuálisan a creators.spotify.com-ra (a fájl behúzása + végső Submit/Schedule mindig emberi kéz — publish = explicit user-action).
3. **A művelet végén Presto törli** a `~/Downloads/navigator-ep<NN>/` mappát.

**Cím + leírás beillesztése — clipboard-bridge (EP36-on ez működött, EGYSZERŰBB mint a JS-injection):**
A rich-text editor a `type`/billentyű-bevitelre **összekutyulja a magyar ékezeteket** (megerősítve EP43 + EP36). A bevált fix:
```bash
# UTF-8 vágólapra tesz (Python — a bash locale ronthatja az ékezetet)
python3 -c "import subprocess; t=open('/tmp/desc.txt',encoding='utf-8').read(); p=subprocess.Popen(['pbcopy'],stdin=subprocess.PIPE); p.communicate(t.encode('utf-8'))"
```
Majd a leírás-mezőbe: kattintás → `cmd+a` → `cmd+v`. A cím (egyszerű input) általában `type`-ra is jó, de hosszú/ékezetes leírásnál mindig clipboard-bridge. (A §lentebbi JS-injection a fallback, ha a paste sem megy.)

**Backdate:** a Schedule date-picker **elfogadja a múltbeli dátumot** (EP36: 2026-01-15) — archív-sorrendhez. Verify-before-trust: a Spotify show-oldalon érdemes vizuálisan ellenőrizni a megjelenített dátumot.

---

#### Alternatíva — MP3 export pipeline (ha audio-only kell)

**Primary (ajánlott): yt-dlp a már feltöltött, de még nem public YT videóból**

Ha a YT videó már fel van töltve (akár `scheduled` vagy `unlisted` állapotban), a legegyszerűbb forrás maga a YT:

```bash
# 192k MP3 export yt-dlp-vel (a publikálás előtt, unlisted/scheduled videóból)
yt-dlp -x --audio-format mp3 --audio-quality 192K \
  -o "EP<NN>_<vendeg>_<YYYY-MM-DD>.mp3" \
  "https://www.youtube.com/watch?v=<VIDEO_ID>"
```

Megjegyzés: ha a videó még `scheduled` (nem public), a yt-dlp a saját fiókkal hozzáfér ha cookie-t ad át:
```bash
yt-dlp --cookies-from-browser chrome -x --audio-format mp3 --audio-quality 192K \
  -o "EP<NN>_<vendeg>_<YYYY-MM-DD>.mp3" \
  "https://www.youtube.com/watch?v=<VIDEO_ID>"
```

**Alternatíva 1: Original recording fájlból**

Ha a nyers felvétel elérhető (pl. `.mp4` vagy `.m4a` a szerkesztőtől / saját gépről):
```bash
ffmpeg -i "EP<NN>_master.mp4" -vn -acodec libmp3lame -ab 192k \
  "EP<NN>_<vendeg>_<YYYY-MM-DD>.mp3"
```
Előny: nincs re-encoding veszteség a YT re-upload miatt. Hátrány: a nyers fájl elérhetőségétől függ.

**Alternatíva 2: Drive backup**

Ha sem a YT videó, sem az original recording nem elérhető, a Drive-on archivált vágott verziót (`MP4` vagy `WAV`) lehet MP3-ra konvertálni (ugyanaz az ffmpeg parancs).

**Best practices:**

- **Fájlnév-konvenció:** `EP<NN>_<vendegnev_kebab>_<YYYY-MM-DD>.mp3` (pl. `EP43_farkas-kinga_2026-05-26.mp3`)
- **Minőség:** minimum 192 kbps MP3 — Spotify nem fogad el 128 kbps alatti feltöltést Podcasters-en keresztül
- **ID3 tagek:** a yt-dlp automatikusan kitölti a cím és előadó mezőket; ffmpeg-nél manuálisan add hozzá:
  ```bash
  -metadata title="EP<NN> — <cím>" -metadata artist="Navigátor Podcast"
  ```
- **Fájlméret benchmark:** 60 perces epizód 192k MP3 ≈ 85-90 MB — elfér egy standard Drive mappában
- **Mentési hely:** `02_Areas/Navigátor Podcast/Episodes/EP<NN>/audio/`

**Spotify wizard quirks — ismert probléma és megoldás (EP43 tapasztalat):**

A Spotify for Podcasters leírás-szerkesztő rich-text editor **megszakad hosszú Unicode szövegnél** (különösen bővített latin karakterek + bullet point kombóknál). Tünet: a beírt szöveg az editor-ban vágódik, a mentés sikertelen vagy hibás szöveget ment.

**Megoldás: HTML toggle + JavaScript injection**

1. Nyisd meg a leírás-szerkesztőt Spotify for Podcasters-ben (Chrome böngészőben)
2. Ha elérhető, kapcsold **HTML toggle ON**-ra az editorban (a rich-text editor HTML-módba vált)
3. Ha a HTML toggle sem segít vagy nem elérhető, használd az alábbi JavaScript injekciót a Chrome DevTools Console-ból:

```javascript
// Spotify for Podcasters — leírás textarea native setter injection
// Chrome DevTools Console-ba futtatni (F12 → Console)
const textarea = document.querySelector('textarea[name="description"]');
if (!textarea) {
  console.error('Textarea not found — check selector');
} else {
  const nativeSetter = Object.getOwnPropertyDescriptor(
    window.HTMLTextAreaElement.prototype, 'value'
  ).set;
  nativeSetter.call(textarea, 'IDE_ILLESZD_BE_A_TELJES_LEIRAS_SZOVEGET');
  textarea.dispatchEvent(new Event('input', { bubbles: true }));
  textarea.dispatchEvent(new Event('change', { bubbles: true }));
  console.log('Leírás beillesztve. Ellenőrizd az editort, majd mentsd!');
}
```

**Miért kell a nativeSetter:** a Spotify editor React-alapú, a React saját virtuális DOM-ot tart fenn. Közvetlen `textarea.value = 'szöveg'` nem triggeri a React state-frissítést, ezért az editor nem látja a változást. A `Object.getOwnPropertyDescriptor` + `nativeSetter.call` a natív HTMLTextAreaElement setter-t hívja, amelyre a React event-listener reagál.

**Chrome MCP read-back:** injection után a Presto Chrome MCP read-back-kel ellenőrzi, hogy a leírás megjelent-e az editorban (screenshot + DOM query). Ha sikeres, Presto szinkronizálja a pub-fájl state-jét (`publication_status: scheduled`).

**Scheduling Rule:** lásd `Spotify_Master_Plan.md §Scheduling Rule` — launch-héten egynél több Spotify archive-upload tiltott. Cross-link: §5 anti-patterns utolsó sora.

---

### 3.6 Daily stats check (paired action, T+0 — T+30)

**Időzítés:** napi, minden platformon, a 30-napos measure window alatt. Részletes cadence és sablon lásd §3.7.

**Mit nézünk:**
- YouTube: views, watch time, retention, CTR, subs gained
- Facebook: reach, reactions, click-through
- Instagram: views, saves, shares
- TikTok: views, completion rate
- Spotify: plays, completion rate
- Patreon: post views, new patrons

**Most:** manuális ellenőrzés.

**Cél (jövőbeli):** automatizált daily sweep — Sage harvest-mintára, statisztikákat napi pull-lal, és anomália-jelzéssel.

**Tracking helye:** `02_Areas/Navigátor Podcast/Marketing/Dashboard.md` heti KPI rollup.

---

### 3.7 Post-launch monitoring (T+0 → T+30) — új §

**Cél:** a 30-napos measure window alatt 4 milestone-on szisztematikus snapshot, a runbook következő iterációjának adatalapja.

#### Snapshot cadence (4 milestone)

| # | Nap | Időpont | Fókusz | Döntési pont |
|---|---|---|---|---|
| **Day 0** | publish napja +1 (Wed) | ~16:00 (24h a go-live után) | Első 24h pulse: views, CTR, retention, subs gained, A/B test status, kommentek száma | Ha CTR < 3%: thumbnail A/B teszt megfontolása |
| **Day 7** | T+7 (következő Sze) | ~16:00 | Mid-window: kumulatív + retention görbe + traffic sources mix | **Decision point** a T+7 follow-up wave timing-ra és a YT Community post tartalmára |
| **Day 14** | T+14 | ~16:00 | Stability check: views-ramp, komment-thread érettség, anomalia-ellenőrzés | Ha views-ramp leáll: evergreen boost megfontolása |
| **Day 30** | T+30 | ~16:00 | **Final snapshot**: teljes 30 napos window, patterns.md PopScore validáció, lessons learned | Runbook iteráció döntés (mi kerüljön a következő verzióba?) |

#### 10-pontos snapshot template (kitöltés minden milestone-nál)

A snapshot a pub-youtube fájl `## Analytics` szekciójába kerül (append):

```
#### Day N Snapshot (YYYY-MM-DD ~HH:MM)
1. Views: <szám>
2. Unique viewers: <szám>
3. CTR (impressions click-through): <%>
4. Avg view duration: <perc:mp>
5. Retention first 30 min: <%>
6. Retention curve key drops: <timestamps ahol >5% esés>
7. Subs gained: <szám>
8. Comments count + kvalitatív megjegyzés: <szám + 1 mondat>
9. Top traffic sources: <lista, top 3>
10. A/B test status (ha aktív): <thumbnail/title nyerő variáns>
11. Anomáliák / notable: <szabad szöveg>
```

#### Tooling

- **Primary:** YouTube Analytics API MCP tool-ok:
  - `youtube_analytics_video_detail` (video_id: adott epizód ID)
  - `youtube_analytics_retention` — első 30 perces görbe
  - `youtube_analytics_traffic_sources`
- **Fallback:** YouTube Studio web UI manuális ellenőrzés (ha API quota issues)
- **Kommentek (kvalitatív):** YT comment thread manuális olvasás

#### Snapshot helye a pub-fájlban

A snapshot a vonatkozó `pub-youtube-<YYYY-MM-DD>-001.md` fájl `## Analytics` szekciójába kerül. Ha a pub-fájl nem tartalmaz `## Analytics` szekciót, Presto hozzáadja (append-only, nem módosít meglévő tartalmat).

---

## 3.8 — External-skill cherry-picks (pre-publish SEO + repurpose model)

> Forrás: `~/.claude/skills/youtube/` (claude-youtube) `metadata` + `repurpose` sub-skillek értékelése — [`youtube-skill-integration-candidates.md`](../../../../00_Prompts/BDOS/_inbox/youtube-skill-integration-candidates.md). Navigator-re adaptálva.

### 3.8.1 — Pre-publish SEO checklist (14 pont, T+0 go-live ELŐTT)

A YouTube go-live (§3.1) előtt ellenőrizendő. Magyar-adaptált (US-specifikus pontok kihagyva):

- [ ] Elsődleges kulcsszó a cím első 40 karakterében
- [ ] Elsődleges kulcsszó a leírás első 25 szavában (ez a search-preview)
- [ ] Leírás < 5000 karakter
- [ ] Időkódok 0:00-tól, min. 3 fejezet (Navigator: 10-12 kulcspillanat)
- [ ] Hashtagek a leírás-blokkban (NEM címben), max 15 — állandó: #NavigátorPodcast #MagyarPodcast
- [ ] Custom thumbnail feltöltve, §10.1 synergy + §10.2 mobile-test átment (Navigator-YT DNA)
- [ ] Cards ~20% és ~70%-nál (end-screen helyett — channel.md: end-screen 0.07% forgalom)
- [ ] End screen az utolsó 20 mp-en (videó-javaslat + subscribe)
- [ ] Felirat/SRT feltöltve vagy auto-caption ellenőrizve (magyar)
- [ ] Audience: "Not made for kids"
- [ ] Kategória kiválasztva
- [ ] Nyelv: magyar
- [ ] 2 playlist hozzáadva (Navigator standard)
- [ ] Pinned first-comment előkészítve (cross-link / vendég-elérhetőség — vö. EP43: Kinga FB-link)

### 3.8.2 — Repurpose Hub/Hero/Help + reel-cadence

| Réteg | Mi | Navigator-példa |
|-------|-----|-----------------|
| **Hero** | A teljes long-form epizód | YouTube EP (60-130 perc) |
| **Hub** | Rendszeres közepes klipek | 2-3 reel/epizód (YT Shorts + IG + TikTok) |
| **Help** | Belépő, kereshető pillanatok | Pinned comment, FB-poszt, idézet-kártya |

**Reel-wave cadence (§3.3 kiegészítés):** a legerősebb hook-ú klip MEGY ELSŐRE (T+1), a többi 2-3 nap eltartással. Clip-választás a reel-factory LEARNINGS Shorts-hook 3-pillér szerint (scroll-stop / standalone / loop). Viewed-vs-Swiped <60% → újravágás.

---

## 4. Kapcsolat a többi entitással

### Seed → Runbook

A Seed `intent.runbook_ref: episode-launch` mezővel hivatkozik erre a runbookra. A `/pres-plan` mód az utolsó argumentumát olvasva tudja milyen N db Publication-t generáljon.

### Runbook → Publications

A runbook futtatása **N db Publication-t** generál (most 8 db) a Navigator Area `Marketing/Publications/` vagy `Marketing/Campaigns/<ep-id>-launch/publications/` mappában.

### Runbook → Campaign (esernyő)

Egy epizód-launch tipikusan **egy Campaign esernyő** (`campaign_id: ep-<NN>-launch`). A Campaign aggregálja a 8 Publication-t, és a runbook-template-et hivatkozza.

### State machine flexibility — offline-prep override (v0.2.0 új)

A standard stage-átmenet sorrend: `Seed → Draft → Prepared → Approval → Scheduled → Published`.

**Ez a sorrend NEM rigid kötelező**, ha offline-prep történt. EP43 tapasztalat alapján:

- Ha a user közvetlenül YouTube Studio-ban ütemezi az epizódot (Navigator Plugin + manuális editálás), a state `draft → prepared → approval → scheduled` 4 lépése **egyetlen Presto state-sync-kel** leváltható
- Feltétel: az approval-trail-be rögzíteni kell hogy "user offline-prepared, YT Studio scheduled, Presto state synced via Chrome MCP read-back"
- A pub-fájlban a `Notes` szekció dokumentálja a stage-ugrást és a valódi execution-trail-t
- Az `Iteration history` append-only marad — a stage-ugrás az ott rögzített, nem kihagyott

**Stage-ugrás megengedett:** `prepared → scheduled` (vagy `draft → scheduled`) offline-prep után, ha YT Studio already scheduled állapotban van.

**Stage-ugrás NEM megengedett:** `scheduled → published` — ez mindig emberi akció (YT go-live) és soha nem auto-skip.

---

## 5. Anti-patterns (mit SOHA ne csinálj)

- ❌ NE indítsd a runbookot, ha a 7 prerekvizitum nem teljes — a hiányzó asset-ek miatt a wave megtörik (pl. Reel-vágás nélkül a T+1 hullám teljesen kiesik)
- ❌ NE generálj autonóm módon Publication-t — minden draft confirmation-gate-tel
- ❌ NE publikálj autonóm módon — minden upload manuális (most még), később lépésről-lépésre semi-auto / auto
- ❌ NE iterálj a runbookon mid-epizód — egy runbook 1 epizódra fix. Iteráció a következő epizód előtt
- ❌ NE ignoráld a stats check-eket — a runbook iterációja ezen alapul
- ❌ NE indíts Spotify-archive-uploadot a launch-héten egynél több op-pal — lásd `Spotify_Master_Plan.md §Scheduling Rule`. Ez az anti-pattern explicit cross-link-et kap: ha párhuzamos Spotify-op van folyamatban, a launch-heti upload-ot halasztani kell
- ❌ NE bízz egyetlen forrásban faktikus állításokra — minden numerikus claim (kor, dátum, statisztika) cross-check legalább 2 forrásból publish előtt. EP43 tanulság: "17 vs 18 évesen" eset
- ❌ NE skip-eld a §1 prereq #7 fact-check pass-t, ha a leírásban vendégről szóló adat szerepel — ez a leggyakoribb factual slip forrása

---

## 6. Iteration history

| Date | Version | Mit változott | Miért | Eredmény |
|---|---|---|---|---|
| 2026-05-26 | 0.1.0 | Initial creation | User-driven first draft | TBD (first run pending) |
| 2026-05-26 | 0.2.0 | EP43 launch tapasztalatok beépítve (8 operational learning) | EP43 gyász-epizód launch első teljes runbook-futás, 8 tanulság kinyerve | v0.2.0 aktív, EP44-re alkalmazandó |
| 2026-05-26 | 0.3.0 | Presto audit-fix: §3.1 Post-publish verification, §3.5a MP3 export pipeline, §10 Next-episode jumpstart checklist | Presto B+C csomag GO — operatív gap-ek zárása EP44 előtt | v0.3.0 aktív, EP44-re alkalmazandó |

---

## 7. TBD — kísérlet alatt álló paraméterek

| TBD | Mit | Hogyan dől el | Státusz |
|---|---|---|---|
| TBD-01 | Pontos kedd-délutáni óra | 3-4 epizód A/B tesztelés | **RESOLVED — 16:00 Tue**, EP43-on bizonyítva (2026-05-26 16:00) |
| TBD-02 | Reel-hullám pontos óra T+1-en (reggel? délelőtt? délután?) | EP43 + EP44 alapján mérünk | Nyitott |
| TBD-03 | Follow-up T+7 vs T+10 vs T+14 — melyik a optimum? | 3 epizód külön-külön | Nyitott |
| TBD-04 | Patreon teaser optimum időzítés | Patreon analytics ramp | Nyitott |
| TBD-05 | YouTube Shorts T+1 vs T+0 — Shorts ugyanazon napon ütheti a long-form-ot? | A/B teszt 2 epizódon | Nyitott |

Mindegyik TBD egy **mérési hipotézis** — a runbook iterációja ezeken keresztül történik.

---

## 8. Hivatkozott dokumentumok

- [MARKETING_ENGINE.md](../MARKETING_ENGINE.md) — Navigátor brand, voice, KPI
- [ChannelDNA/Navigator-YT.md](../ChannelDNA/Navigator-YT.md) — YouTube DNA
- ChannelDNA/Navigator-FB.md — Facebook DNA (TBD, még nincs)
- ChannelDNA/Navigator-IG.md — Instagram DNA (TBD)
- ChannelDNA/Navigator-TT.md — TikTok DNA (TBD)
- ChannelDNA/Navigator-Patreon.md — Patreon DNA (TBD)
- [../../Synthesis/new_video_checklist.md](../../Synthesis/new_video_checklist.md) — 5-fázisos operatív checklist
- [../../Synthesis/channel.md](../../Synthesis/channel.md) — channel intelligence baseline
- [../../patterns.md](../../patterns.md) — popularity score modell
- Navigator Plugin: `00_Prompts/Claude/Plugins/navigator-plugin-v0.3/skills/navigator-context-v0.3/SKILL.md`
- **[Spotify_Master_Plan.md](../../Spotify_Master_Plan.md)** — Spotify scheduling rule, archívum-upload tiltás launch-héten. Lásd §5 anti-pattern cross-link és §3.5a.
- **`_dashboards/_design/DESIGN_SYSTEM.md §11`** — promote-candidates: Calendar 3-tier pattern + meta-prefix naming-konvenciók. Releváns a runbook pub-fájl naming-convention fejlesztésekor.

---

## 9. Schema (`presto.runbook.v1`)

Egyelőre inline. Amikor 2+ runbook él, kanonizáljuk `MARKETING_OS_SCHEMAS_v2.md`-be.

**Kötelező mezők:**
- `schema`, `runbook_id`, `area`, `version`, `status`, `description`, `id`, `index_schema_version`, `bdos_index`
- `trigger` — szöveges leírás mi triggereli
- `publications_generated_count` — hány Pub szülik

**Opcionális:**
- `typical_publish_day`, `prerequisites`, `paired_actions`

**Lifecycle:** `draft → proposal → active → deprecated`

---

## 10. Next-episode jumpstart — copy-paste checklist

> **Cél:** EP44+ minden launch előtt ezt a listát nyisd meg és pipáld végig. Copy-paste-elhető, minden lépésnél konkrét parancs vagy helyszín.

### Pre-launch (T-7 → T-1)

- [ ] **1. Prereq audit** — §1 táblázat mind a 7 sorát jelöld meg `done`-ként a Seed `## Prerequisites checklist`-ben
- [ ] **2. Fact-check pass** — minden numerikus állítás (kor, dátum, statisztika) cross-check 2 forrásból. Különösen: vendég életkora, projekt-dátumok, statisztikai idézetek
- [ ] **3. YT metadata generálás** — futtatd: `/cim`, `/leiras`, `/idokod`, `/thumbnail`, `/hook` — output YT Studio-ba másolva és manuálisan ellenőrizve
- [ ] **4. Thumbnail feltöltve** a YT Studio-ban (max 4 szó, magas kontraszt)
- [ ] **5. YT scheduled** — kedd 16:00 UTC+2 (EP43 baseline) — YT Studio `Scheduled` státusz
- [ ] **6. MP3 export kész** — `EP<NN>_<vendegnev>_<YYYY-MM-DD>.mp3`, 192k, mentve: `Episodes/EP<NN>/audio/`
  ```bash
  yt-dlp --cookies-from-browser chrome -x --audio-format mp3 --audio-quality 192K \
    -o "EP<NN>_<vendeg>_<YYYY-MM-DD>.mp3" "https://youtu.be/<VIDEO_ID>"
  ```
- [ ] **7. Pub-fájlok létrehozva** Presto-val: `/pres-seed` → `/pres-draft` mind a 8+2 pub-ra (`pub-*-<YYYY-MM-DD>-001` pattern)
- [ ] **8. Reel-vágás kész** (intro-szegmens 30-60 mp, 9:16, burned-in subs)

### Launch nap (T+0, kedd)

- [ ] **9. YT go-live** — 16:00 YT Studio-ban manuálisan `Publish now` (vagy scheduled automatikusan él)
- [ ] **10. Post-publish verify** — Presto Chrome MCP check: Visibility=Public, cím/leírás/thumbnail OK. Screenshottot ment: `publish-trail/yt-studio-post-launch-<YYYY-MM-DD-HHmm>.png`
  - Ha FAIL → pub-fájl `published_unverified`, user riasztás, FB post halasztva
- [ ] **11. FB personal post** — YT go-live +5 perc: személyes 1 mondatos hook + thumbnail + YT link. Pub-id: `pub-facebook-<YYYY-MM-DD>-001`
- [ ] **12. Spotify upload** — podcasters.spotify.com, MP3 feltöltés, leírás YT-adaptált verzió, Chapters formátum. Ha leírás-szerkesztő hibás: §3.5a JS injection
  - Spotify Scheduling Rule: launch-héten max 1 upload

### Post-launch (T+1, szerda)

- [ ] **13. Reels hullám** — 4 platform párhuzamosan:
  - `pub-instagram-<YYYY-MM-DD>-001` — IG Reels, 5-10 hashtag
  - `pub-facebook-<YYYY-MM-DD>-002` — FB Reels, 1-2 hashtag
  - `pub-youtube-<YYYY-MM-DD>-002` — YT Shorts, 2-3 hashtag
  - `pub-tiktok-<YYYY-MM-DD>-001` — TikTok, 3-5 hashtag + emoji

### Monitoring (T+0 → T+30)

- [ ] **14. Day 0 snapshot** (T+1, ~16:00) — 10-pontos template (§3.7) a pub-youtube fájl `## Analytics` szekciójába
- [ ] **15. Day 7 snapshot** (T+7) — döntési pont: T+7 follow-up wave timing
- [ ] **16. T+7 follow-up draftek** — Presto `/pres-draft` T+5-én:
  - `pub-youtube-community-<YYYY-MM-DD>-001` — Community tab kérdés
  - `pub-facebook-<YYYY-MM-DD>-003` — emlékeztető + 1-2 kulcs-gondolat
- [ ] **17. T+7 publish** — user manuálisan posztolja mindkettőt
- [ ] **18. Day 14 snapshot** (T+14) — stability check
- [ ] **19. Day 30 snapshot** (T+30) — final snapshot, lessons learned, runbook iteráció döntés

### Spotify archive + következő epizód

- [ ] **20. Patreon teaser** (T+X) — Presto `/pres-draft pub:pub-patreon-<YYYY-MM-DD>-001`, insider-only betekintő a következő epizódba
- [ ] **21. Következő epizód Seed** — `/pres-seed` a következő epizód első raw input-jával (Patreon-teaserrel párhuzamosan)

---

*Ez egy ÉLŐ dokumentum. Minden epizód-launch után review és iteráció.*
