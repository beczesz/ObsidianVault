---
schema: presto.channel-dna.v2
area: Fókuszpont
channel: facebook
display_name: Facebook — Fókuszpont
status: proposal
version: 0.1.0
date: 2026-05-28
author: Becze Szabolcs
description: Fókuszpont Facebook Channel DNA — presto.channel-dna.v2 séma. Elsődleges tartalom a Meta vertikális-videó feltöltési szabály (Reel ≠ feed-poszt, 9:16 safe-zone, borítókocka), ami a 2026-05-28-i úrnapi videó "levágott" hibáját okozta. Esemény-promóció, erdélyi magyar keresztény közösség (Székelyudvarhely).
id: a3f1c9d2-6b84-4e57-9a21-7c0e5f8d3b46
index_schema_version: 1
bdos_index: true
primary_language: hu
allowed_formats: [reel, feed-post, event-cover, story]
constraints:
  video_aspect_canonical: "9:16"
  feed_crop_aspect: "4:5"
  reel_safe_zone: "felső ~10%, alsó ~20%, jobb oldal ~10% UI-gombokkal takart"
posting_rhythm:
  recommended_cadence: "esemény-vezérelt (kampány-időzítés szerint)"
  rationale: "Fókuszpont nem evergreen-csatorna — az úrnapi/esemény kampányok kadenciája diktál (lásd urnapja-2026 CAMPAIGN.md)."
publication_capabilities:
  api_available: false
  mcp_available: false
  manual_required: true
  analytics_api: false
  fallback_chain: [manual]
  api_note: "Plébánia FB-oldal — publikálás manuális. Nincs konfigolt Graph API token."
---

# Facebook — Fókuszpont — Channel DNA (proposal)

> **Státusz: proposal.** Presto-generált javaslat (2026-05-28). Az `active` státuszhoz emberi jóváhagyás kell.
>
> **Meta cross-platform:** a §3 vertikális-videó szabályok **azonosan érvényesek Instagram Reels-re** (`Fokuszpont-IG.md`) — közös Meta-viselkedés.

---

## §1 — Csatorna-identitás

A Fókuszpont Facebook-jelenléte **esemény-promóciós csatorna** egy erdélyi (székelyudvarhelyi) katolikus imaközösség számára. Nem evergreen content-gyár: a tartalom az adott eseményhez (pl. Úrnapja 2026, június 3.) kötött meghívó- és tanúságtétel-anyag.

**Brand-line:** *„Jézus a Fókuszpont — és minden szem Rá szegeződik."*

**Közönség:** erdélyi magyar keresztény közösség, Székelyudvarhely és környéke; fiatalok (peer-to-peer reel) + szélesebb plébániai közösség (meghívó, event-cover).

---

## §2 — Publikáció-formátumok és a Meta feltöltési szabály ⚠️

> **Ez a csatorna legfontosabb szekciója — a 2026-05-28-i "levágott videó" eset tanulsága.**

### A vágás gyökere

A reel-videók **9:16 (álló)** formátumúak. A Facebook (és Instagram) kétféleképpen jeleníti meg ugyanazt a videót:

| Feltöltési mód | Mit csinál a kerettel | Eredmény |
|---|---|---|
| **Reel** (Létrehozás → Reel) | Megtartja a teljes **9:16**-ot | ✅ nincs vágás |
| **Feed-poszt** (Létrehozás → Fotó/Videó) | A feed-előnézetben **4:5-re vágja** | ❌ levágja a tetejét/alját (fej teteje, alsó felirat) |

A 2026-05-28-i úrnapi videó feed-posztként ment fel → a feed-crop levágta a fej tetejét és beszorította a "letérdeltünk Jézus elé" feliratot. **A megoldás: Reel-ként kell feltölteni.**

### Kötelező feltöltési szabályok (minden reel-anyaghoz)

1. **Mindig Reel-ként** publikálj vertikális videót, NEM feed-posztként. (FB: *Létrehozás → Reel*. IG: a feltöltőben a *Reel* fül.)
2. **Borítókocka (cover):** kézzel válassz olyan frame-et, ahol a fej/felirat középen van — a feed-thumbnail 4:5 vagy 1:1, ezért a borító akkor is vághat, ha a teljes Reel 9:16.
3. **Safe-zone a vágásnál és a forgatókönyvnél:**
   - felső **~10%** és alsó **~20%** maradjon "üres" a kulcs-tartalomtól (fej, fő alany, felirat),
   - jobb oldalon **~10%** a UI-gombok (like / komment / megosztás) miatt szintén kerülendő,
   - a feliratok és a fő alany a **középső safe-zone-ba** kerüljenek.
4. **Event-cover** kivétel: a Facebook esemény-borító vízszintes/négyzetes — ehhez külön, nem-9:16 vágás kell (lásd Reel #1B event-cover főanyag).

---

## §3 — Operacionalizált insights

| ID | Típus | Tanulság | Evidencia |
|----|-------|----------|-----------|
| INS-FP-FB-001 | format-fit | Vertikális (9:16) videót **mindig Reel-ként** kell feltölteni Meta-n; a feed-poszt 4:5-re vágja és levágja a tetejét/alját. | 2026-05-28 úrnapi videó "levágott" eset; cross-project learning `meta-reel-not-feedpost` |
| INS-FP-FB-002 | format-fit | Reel-borító (cover frame) kézi kiválasztása szükséges — a feed-thumbnail akkor is vághat, ha a teljes Reel 9:16. | ugyanaz az eset |
| INS-FP-FB-003 | format-fit | A reel-feliratok és a fő alany a középső safe-zone-ba (felső 10% / alsó 20% / jobb 10% kerülendő) — különben UI-gombok és feed-crop takarja. | Meta UI-overlay konvenció |

---

## §4 — Publikáció és fallback

- **Publikálás:** manuális (plébánia FB-oldal, nincs API token).
- **Fallback chain:** `manual` — Presto draft-ot és emlékeztetőt készít, az ember tölti fel.
- **Kötelező ellenőrzés publikálás előtt:** "Reel-ként megy fel?" + "borítókocka kiválasztva?" (lásd §2).

---

## §5 — Iteration history és nyitott kérdések

### Iteration history
- 2026-05-28 — v0.1.0 — initial proposal — Presto; trigger: úrnapi videó feed-crop eset.

### Nyitott kérdések
| # | Kérdés | Következő lépés |
|---|--------|-----------------|
| TBD-01 | Stats/analytics — van-e hozzáférés a plébánia FB-oldal Insights-hoz? | Audit a következő kampány előtt |
| TBD-02 | Event-cover pontos méret/safe-zone (FB esemény-borító jelenlegi ratio) | Ellenőrizni a `pub-facebook` event-cover anyagnál |

---

*Generálta: Presto — 2026-05-28 — trigger: úrnapi videó feed-crop eset (Áron/Sámuel chat-jelzés).*
