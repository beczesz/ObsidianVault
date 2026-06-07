---
schema: presto.channel-dna.v2
area: Fókuszpont
channel: instagram
display_name: Instagram — Fókuszpont (@fokuszpont_)
status: proposal
version: 0.1.0
date: 2026-05-28
author: Becze Szabolcs
description: Fókuszpont Instagram Channel DNA (@fokuszpont_) — presto.channel-dna.v2 séma. A Meta vertikális-videó feltöltési szabály (Reel ≠ feed-poszt, 9:16 safe-zone, borítókocka) azonos a Facebook DNA-val. Account-info és recovery a Channels/instagram.md-ben.
id: b7e4d201-3f95-4a68-8c12-9d6a0e2f1c83
index_schema_version: 1
bdos_index: true
primary_language: hu
allowed_formats: [reel, feed-post, story]
constraints:
  video_aspect_canonical: "9:16"
  feed_crop_aspect: "4:5"
  reel_safe_zone: "felső ~10%, alsó ~20%, jobb oldal ~10% UI-gombokkal takart"
publication_capabilities:
  api_available: false
  mcp_available: false
  manual_required: true
  fallback_chain: [manual]
---

# Instagram — Fókuszpont (@fokuszpont_) — Channel DNA (proposal)

> **Státusz: proposal.** Presto-generált (2026-05-28).
> **Account-info, recovery chain, stats:** lásd [`../../Channels/instagram.md`](../../Channels/instagram.md) (nem duplikáljuk).

---

## §1 — Csatorna-identitás

`@fokuszpont_` — esemény-promóciós Instagram-fiók a székelyudvarhelyi Fókuszpont imaközösségnek. Rövidvideók (Reels) + Stories. Erdélyi magyar keresztény közönség, fiatalok peer-to-peer.

---

## §2 — Meta feltöltési szabály ⚠️ (azonos a Facebook DNA-val)

A vágási és safe-zone szabályok **megegyeznek a Facebook-éval** — közös Meta-viselkedés. Teljes leírás: [`Fokuszpont-FB.md` §2](./Fokuszpont-FB.md).

**Rövid összefoglaló:**
1. Vertikális (9:16) videó **mindig Reel-ként** (a feltöltőben a *Reel* fül), NEM feed-posztként — különben 4:5-re vág.
2. **Borítókocka** kézi kiválasztása (feed-thumbnail vághat).
3. **Safe-zone:** felső ~10% / alsó ~20% / jobb ~10% kerülendő a kulcs-tartalomtól (UI-gombok + feed-crop).

> Megjegyzés: az Instagram a vertikális videókat ma alapból Reels-ként kezeli, de ha mégis feed-posztba kerül, ugyanúgy 4:5-re vág.

---

## §3 — Operacionalizált insights

| ID | Típus | Tanulság | Evidencia |
|----|-------|----------|-----------|
| INS-FP-IG-001 | format-fit | Lásd INS-FP-FB-001/002/003 — közös Meta Reel safe-zone tanulság. | cross-project learning `meta-reel-not-feedpost` |

---

## §4 — Iteration history
- 2026-05-28 — v0.1.0 — initial proposal — Presto; közös Meta Reel-szabály a Facebook DNA-val.

---

*Generálta: Presto — 2026-05-28.*
