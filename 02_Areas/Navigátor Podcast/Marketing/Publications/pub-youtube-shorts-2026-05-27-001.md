---
schema: presto.publication.v2
publication_id: pub-youtube-shorts-2026-05-27-001
id: 84bfb956-4cdb-4a8f-a709-ff6325672393
index_schema_version: 1
bdos_index: true
stage: published
status: monitoring
published_at: 2026-05-28
area: Navigátor Podcast
channel: youtube-shorts
campaign_ref: null
seed_ref: seed-20260526-ep43-gyasz-launch
runbook_ref: episode-launch
runbook_step: T+1
pub_type: shorts_intro_cut
dna_ref: Navigator-YT
planned_publish_date: 2026-05-28
planned_publish_time: null
created_date: 2026-05-26
created_by: presto (auto-spawn from runbook)
prepared_by: presto (2026-05-28 — text package anchored to EP43 launch pub-youtube-2026-05-26-001)
prepared_date: 2026-05-28
intent:
  audience: "YouTube Shorts discovery-réteg — fiatalabb demográfia, más elérési mechanizmus mint a hosszú-formátum. Navigator-YT §4 Shorts-caveat: a Shorts közönsége eltér a long-form-tól, külön baseline-t igényel."
  message: "Az epizód legerősebb hook-pillanata 60 másodpercen belül — a Shorts-logikához igazítva. A cél: discovery (új nézők) és cross-link a teljes epizódra."
  hook_angle: "Shorts: első 3 mp döntő, felirat kötelező (burned-in), vertikális 9:16. Navigator-YT §4 Shorts-caveat szerint: NEM clickbait, NEM brain-rot — a csatorna hangvételével konzisztens, csak rövid formátumban. A Shorts-ra mutató cross-link az epizód leírásában is meg fog jelenni."
  source: suggested-by-presto-then-needs-review
description: "EP43 YouTube Shorts T+1 hullám — 30-60s, 9:16, burned-in felirat. Discovery-célú, a Navigátor hosszú-formátum tölcsérébe vezet. Navigator-YT §4 Shorts-caveat figyelembevételével."
tags: [navigator-podcast, ep43, gyász, youtube-shorts, shorts_intro_cut, farkas-kinga, t1-reel-wave]
---

## Body — final

### Cím (max 100 karakter, #Shorts kötelező)

**Ajánlott:** `Egyik reggel anyám eltűnt – 20 évig kerestem #Shorts`  *(50 karakter)*

Alternatívák (a kivágott klip tartalmától függően):
- `Kiégésnek hittem. 20 év gyász volt. #Shorts`  *(reframe — univerzálisabb, többekhez szól)*
- `A gyász, amit 20 évig nem mertem kimondani #Shorts`

### Leírás

```
Farkas Kinga 18 évesen vesztette el édesanyját — egy reggel kisétált a házból, és soha többé nem került elő. 20 évig azt hitte, kiégett. Valójában gyászolt.

🎙️ Teljes beszélgetés (EP43): https://youtu.be/1A53BXfdpw0

#Shorts #NavigátorPodcast #Gyász #Kiégés #Gyászfeldolgozás #FarkasKinga
```

### Ajánlott klip-szegmens (ha még nincs kivágva)

- **Elsődleges — cold-open sokk:** 0:00–0:55 „Anyu, nézd magadra" / „20 évig az utcákon kerestem őt" — erős misztérium + érzelmi horgony, az első 3 mp önállóan megfog.
- **Alternatíva — reframe:** ~34:00–38:00 „kiégésnek hittem, de gyász volt" — univerzálisabb (a kiégés sokakat érint), illeszkedik a fő thumbnail-hez („NEM KIÉGÉS, HANEM GYÁSZ").

> A cím a kivágott szegmenshez igazodjon: cold-open klip → 1. cím; reframe klip → 2. cím.

### YT Shorts spec (upload-ellenőrzés)
- 9:16 vertikális, max 60 mp · burned-in magyar felirat
- A `#Shorts` a címben VAGY a leírásban kötelező (itt mindkettőben)
- Cross-link a teljes epizódra a leírásban ✓ (Navigator-YT §4: a Shorts a long-form tölcsérébe vezet)

## Body — variations
- v1 (rough draft): [TBD]

## Visual assets
- Videó: T+1 reel clip (azonos alap pub-instagram-2026-05-27-001-gyel)
- Thumbnail: automatikus (YT Shorts nem kér külön thumbnailt)

## Approval trail
- 2026-05-28 — Presto prepare: text package (cím + leírás + hashtag + ajánlott szegmens) generálva, az EP43 launch (pub-youtube-2026-05-26-001) kanonikus metaadatához igazítva. stage: draft → prepared. Várja a user manuális feltöltését + utána a published-jelölést.

## Publish trail
- 2026-05-28 — **PUBLISHED** YouTube Shorts-ként (Chrome MCP-vel előkészítve a cím+leírás, user töltötte fel a klipet + nyomta a Publish-t). Klip: 0:40, 9:16. URL: youtube.com/shorts/i-o… (teljes ID a YT Studio-ból pótlandó).
Execution: YouTube MCP → Chrome MCP (YT Data API kvóta 0). Manuális upload YouTube Studio-n keresztül.

## Analytics (30-day window)
(empty until published)
Megjegyzés: első YT Shorts adatpont — külön baseline szükséges (Navigator-YT §4).

## Notes
Auto-generated from seed:seed-20260526-ep43-gyasz-launch via runbook:episode-launch step T+1.
DNA reference: ../ChannelDNA/Navigator-YT.md (§4 Shorts caveat alkalmazandó)
Shorts ≠ long-form audience: analytics külön kezelendő.
