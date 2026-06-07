---
schema: presto.seed.v2
seed_id: seed-20260526-ep43-gyasz-launch
id: cc4a3bc8-495d-4ff8-9890-c73a512c1273
index_schema_version: 1
bdos_index: true
status: ready
title: "EP43 Gyász (Farkas Kinga) — multi-platform launch"
short_description: "EP43 Farkas Kinga (Gyász/ambiguous loss). 8 publikáció T+0–T+7: YT+Spotify+FB+Patreon + T+1 Reel-hullám (Insta+TT+FB+YT-Shorts) + T+7 follow-up."
runbook_ref: episode-launch
campaign_ref: null
created_date: 2026-05-26
captured_at: 2026-05-26T09:48:50+03:00
captured_by: Becze Szabolcs
area: Navigátor Podcast
source: campaign-launch
source_type: other
source_ref: "[[02_Areas/Navigátor Podcast/Episodes/EP43 - Gyász - Farkas Kinga/EP43_ChatGPT_jegyzet]]"
channels: [youtube, spotify, facebook, patreon, tiktok, instagram]

prerequisites:
  - id: prereq-001
    description: "Felvétel elkészült (hanganyag rögzítve és alapszerkesztés kész)"
    status: done
    done_date: 2026-05-26
    owner: user
    due_date: 2026-05-29
    notes: ""
  - id: prereq-002
    description: "SRT felirat generálva (YouTube feltöltéshez + Shorts burned-in subs)"
    status: done
    done_date: 2026-05-26
    owner: user
    due_date: 2026-05-29
    notes: "SRT-függő: YouTube metadata + TikTok/Instagram Shorts is erre vár"
  - id: prereq-003
    description: "Thumbnail elkészítve (YouTube primary thumbnail — /thumbnail skill)"
    status: done
    done_date: 2026-05-26
    owner: user
    due_date: 2026-05-29
    notes: ""
  - id: prereq-004
    description: "YouTube metadata csomag összeállítva (cím, leírás, időkódok, hashtagek — /cim /leiras /idokod /hook)"
    status: done
    done_date: 2026-05-26
    owner: user
    due_date: 2026-05-29
    notes: "navigator-plugin skill-jei: /cim, /leiras, /idokod, /thumbnail, /hook"
  - id: prereq-005
    description: "Publish date véglegesítve (T+0 konkrét dátum és időpont meghatározva)"
    status: done
    done_date: 2026-05-26
    owner: user
    due_date: 2026-05-29
    notes: ""
  - id: prereq-006
    description: "Reel-clip kivágva (30-60s legerősebb retention-szegmens — T+1 hullámhoz)"
    status: done
    done_date: 2026-05-26
    owner: user
    due_date: 2026-05-29
    notes: "TikTok + Instagram + FB Reels + YT Shorts alap — SRT-függő (burned-in subs)"

distribution_timeline:
  - step: T+0
    date: 2026-05-29
    channels: [youtube, spotify, facebook, patreon]
    pub_type: launch
    notes: "Elsődleges launch: YT teljes videó + Spotify audio + FB személyes cross-post (EP41-mintára) + Patreon intimate backstage + EP44 teaser"
  - step: T+1
    date: 2026-05-30
    channels: [instagram, tiktok, facebook, youtube]
    pub_type: reel
    notes: "Reel-hullám: 30-60s clip — Insta Reels + TikTok + FB Reels + YT Shorts. Legerősebb retention-szegmens, burned-in subs, magyar."
  - step: T+7
    date: 2026-06-05
    channels: [facebook]
    pub_type: followup
    notes: "Follow-up post: első hét statisztikák + tanulságok + közönség bevonása (ha van elég visszajelzés)"

publications_spawned:
  - pub-youtube-2026-05-26-001
  - pub-facebook-2026-05-26-001
  - pub-instagram-2026-05-27-001
  - pub-facebook-2026-05-27-001
  - pub-youtube-shorts-2026-05-27-001
  - pub-tiktok-2026-05-27-001
  - pub-youtube-community-2026-06-02-001
  - pub-facebook-2026-06-02-001
exhausted_at: null
tags: [navigator-podcast, ep43, gyász, farkas-kinga, multi-platform-launch, case-study, ambiguous-loss]
description: "EP43 Farkas Kinga (Gyász) epizód többplatformos publikáció-terve. Launch nap: 2026-05-29 YouTube + Spotify + Facebook + Patreon (Miklós Ervin teaser). T+1: TikTok + Instagram + Facebook Reels + YT Shorts. T+7: follow-up. Case study: első élesbe vitt Presto Marketing Engine v2 seed flow."

# Preliminary intent (hint) — végleges intent platformonként a /pres-draft fázisban
intent:
  audience: "35-64 éves keresők, pszichológia/spiritualitás iránt érdeklődők, 53% nő (Navigátor core audience)"
  message: "Az ambiguous loss (lezáratlan veszteség) feldolgozása nem időfüggő — aktív munka. Farkas Kinga története + Grief Recovery Method konkrét, módszertani választ adnak."
  hook_angle: "Builder-tone, evidence-based — NEM provokatív. Személyes sebezhetőség (Kinga édesanyja eltűnt 17 évesen) + módszertani konkrétum kombóban. Patreon-on egyébként betekintés a következő epizódba (Miklós Ervin — Agrár Digitalizáció)."
---

## Raw content (epizód-mag)

**Vendég:** Farkas Kinga (~40 éves nő, Grief Recovery Method magyarországi képviselője — gyaszfeldolgozasmodszer.hu)

**Vezérgondolat:** *Ambiguous loss* — lezáratlan gyász (nem haláleset, hanem eltűnés). Az idő nem gyógyít, csak aktív feldolgozás segít. Hit + strukturált módszer = Kinga válasza.

**Személyes ív:** 17 évesen Kinga édesanyja rejtélyesen eltűnt (se telefon, se ruha, se pénz). Pszichés beteg volt. Máig ismeretlen sors. Kinga hosszú keresési utat járt be (ezoterikus, más irányzatok), végül keresztény hitben találta meg a stabilitást.

**Módszertani mag:** Grief Recovery Method — 5 lépéses strukturált feldolgozás, magyarországi adaptáció.

**Forrás-anyagok:**
- [[02_Areas/Navigátor Podcast/Episodes/EP43 - Gyász - Farkas Kinga/EP43_ChatGPT_jegyzet]] — teljes background, 4-részes interjú-ív, módszer-leírás
- `EP43 - Felkészülési kérdések - Farkas Kinga.pdf` — felvétel előtti kérdéssor
- `EP43 - Meghívó - Farkas Kinga.pdf` — vendég-meghívó + framing

## Distribution plan — multi-platform timeline

### T+0 (Launch day = 2026-05-26)

| Channel | Pub-id sablon | Variáns | Megjegyzés |
|---|---|---|---|
| **YouTube** | `pub-youtube-2026-05-26-001` | **Elsődleges launch.** Teljes metadata (cím + leírás + időkód + thumbnail) a navigator-plugin skill-jeivel: `/cim`, `/leiras`, `/idokod`, `/thumbnail`, `/hook`. | SRT-függő — felvétel/vágás után indítható |
| **Spotify** | `pub-spotify-2026-05-26-001` | **Audio upload.** Spotify-on a Navigátor csatorna már él, ide csak az audio kerül + leírás-link a YouTube videóra. | Spotify-szabványok (channel.md alapján) |
| **Facebook** | `pub-facebook-2026-05-26-001` | **Személyes magyar cross-post.** EP41-mintára (TOP 6 retencióval). Builder-tone, személyes bevezető, YouTube link. | Manual posting (facebook.md channel-DNA: `manual_required: true`) |
| **Patreon** | `pub-patreon-2026-05-28-001` | **Intimate backstage + EP44 teaser.** ÁTHELYEZVE 2026-05-28 csütörtökre (YT-launch + 2 nap). Két részes: (1) miért választottam Kinga történetét, mi érintett meg személyesen; (2) **rövid betekintés a következő epizódba (Miklós Ervin — Agrár Digitalizáció)** mint loyalty-reward a támogatóknak. | Patreon-only insider content (patreon.md: `intimate-backstage`) |

### T+2 (2026-05-28) — Shorts wave

| Channel | Pub-id sablon | Variáns | Megjegyzés |
|---|---|---|---|
| **TikTok** | `pub-tiktok-2026-05-28-001` | **30-60s short clip.** Legerősebb retention-szegmens kivágása (valószínűleg Kinga személyes története + ambiguous loss "aha"-pont). Magyar nyelvű, alulra burned-in subs. | SRT-függő. Hashtag-stratégia: `#NavigátorPodcast #gyász #ambiguousloss` |
| **Instagram** | `pub-instagram-2026-05-28-001` | **Reels — ugyanaz a clip mint TikTok-on, IG-formátumra adaptálva (9:16, sound-on optimalizált).** | IG-channel-DNA per existing |
| **Facebook** | `pub-facebook-2026-05-28-001` | **Facebook Reels / video post — ugyanaz a clip.** Cross-post a már posztolt T+0 lánc alá, second-touch a Magyar audience-ra. | Facebook-channel-DNA: manual |

**Összesen:** 7 publikáció születik majd ebből a seedből.

## Channel-specifikus megjegyzések

### YouTube (elsődleges launch)
- A Navigátor Channel DNA priority #1 (lásd MARKETING_ENGINE.md §4)
- SRT-függő, a felvétel/vágás után kell indítani
- A navigator-plugin teljes metadata-csomagja: cím / leírás / hashtagek / időkód / thumbnail-szöveg / hook
- Channel intelligence: pszichológia-téma **S-tier** (patterns.md alapján), univerzalitás magas
- Forecast: a "lezáratlan veszteség" angle önmagában erős hook — várható nézési teljesítmény legalább a csatorna-átlag

### Patreon (különleges variant)
- A user explicit kérése: a Patreon-poszt **TARTALMAZZON utalást a következő epizódra** (EP44 Miklós Ervin — Agrár Digitalizáció)
- Ez loyalty-reward a támogatóknak — "te tudod meg először mi jön"
- Patreon-on először állunk bele ebbe a "next-episode tease" pattern-be → ha működik, később template lesz belőle

### Facebook (T+0 personal + T+2 Reels)
- Két touch ugyanazon a hét: T+0 long-form launch + T+2 short clip
- EP41 success mintája: személyes bevezető, nem clickbait, magyar nyelvű
- Channel-DNA: `manual_required: true` — nincs API-integráció

### TikTok / Instagram (T+2 Shorts)
- Még nincs külön Channel DNA fájl Navigátorra (TikTok/Instagram channel-dna stub-ok hiányoznak)
- A T+2 wave-re kell készíteni vagy legalább a Navigator Area Channels/ alá per-Area definíciókat
- A `csatorna-intelligencia.md` patterns nem közvetlenül vonatkoznak Shorts-tartalomra — saját mérés indul

## Suggested next steps (engine-pull)

1. **MOST nincs SRT** → nem lehet `/pres-draft`-olni a YouTube launch metadat-cumost. Azt akkor csináljuk, amikor a felvétel megvan és a SRT generálódott.
2. **Patreon-poszt** és **Facebook személyes-cross-post** részben függetlenek az SRT-től — a vendég-háttér + epizód-mag már elég kontextust ad. Ha akarja, a user **most akár Facebook-draft-ot is generálhat** (EP41-mintára).
3. **Channel DNA gap-ek**: TikTok és Instagram channel-dna stub létrehozása a T+2 hullám előtt szükséges. Lehet más seed/külön ülés.
4. **Campaign-esernyő érdemes?** — Mivel 7 publication tartozik egyazon seedből, egy `CAMPAIGN.md` esernyő (`campaign_id: ep43-gyasz-launch`) hasznos lehet a tracking-hez. Megfontolandó.

## Case study tanulság (élő dokumentáció)

Ez az **első Presto Marketing Engine élesbe vitt flow**. Ahogy végigmegyünk a 6 stage-en, minden tapasztalat itt log-olódik (vagy egy parallel `case-study-ep43-launch.md` doc-ban):

- ✅ Seed létrehozás működik (2026-05-26 — most)
- ⏳ Felvétel/vágás várása
- ⏳ SRT-generálás
- ⏳ Per-platform draft generálás
- ⏳ Prepare (brand-review + Impeccable visual)
- ⏳ Approval gate
- ⏳ Scheduled
- ⏳ Published (per-platform timing)
- ⏳ Measuring (30-day window)
- ⏳ Lessons learned doc

## Notes

A user explicit megerősítette a publikálási tervet:
- Patreon-on legyen utalás Miklós Ervin (EP44) epizódra
- Spotify upload kell
- TikTok + Instagram + Facebook Shorts 2 nappal a launch után
- LinkedIn-t most NEM csináljuk (későbbi seed lehet)

Channel-mix justification: Navigátor MARKETING_ENGINE.md §4 alapján YouTube=P1, Facebook=P1, Patreon=P3. TikTok/Instagram kísérleti — eredménytől függ a folytatás.
