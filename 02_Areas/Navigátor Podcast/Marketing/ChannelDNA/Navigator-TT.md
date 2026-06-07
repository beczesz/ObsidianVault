---
schema: presto.channel-dna.v1
area: Navigátor Podcast
channel: tiktok
display_name: TikTok — Navigátor Podcast
status: proposal
version: 0.1.0
date: 2026-05-26
author: Becze Szabolcs
description: Navigátor Podcast TikTok csatorna Channel DNA — presto.channel-dna.v1 séma. Kísérleti csatorna, explicit audience-mismatch figyelmeztetéssel (TikTok <35 core vs. Navigátor 35-64 core). Tartalmaz: stratégiai fit analízis, tone-szabályok (punchy-but-substantial, NEM clickbait), format spec (30-60s vertikális, burned-in subs), forbidden patterns (trend-chasing, brain-rot, cross-post automatizmus), és explicit strategic-decision-gate (EP43+EP44+EP45 mérés alapján). Forrás: episode-launch.md (runbook Step 6 T+1 TikTok intro-cut), Navigator-YT.md, Navigator-IG.md, Alkotmány, MARKETING_ENGINE.md.
id: 7a2f4c81-3b5e-4d9f-a1c6-8e0b2d4f6a3c
index_schema_version: 1
bdos_index: true
audience_data_source: "TBD — TikTok Analytics nincs hozzáférve. Demográfia: általános TikTok platform-statisztikákból becsülve. Navigátor core-demográfia: YouTube Analytics (Navigator-YT.md §2)."
primary_language: hu
allowed_formats: [short-video]
constraints:
  max_chars:
    caption: 2200
    recommended_visible: 150
  max_hashtags: 5
  link_in_bio: true
  link_in_caption: false
posting_rhythm:
  recommended_cadence: "T+1 per epizód (szerdán) — és semmi más rendszeres tartalomtípus a kísérleti fázisban"
  optimal_day: szerda
  optimal_hours_local: TBD
  rationale: "Runbook Step 6 (T+1 TikTok intro-cut). Pontos óra TBD — nincs TikTok Analytics adat az audience aktív idejéről."
publication_capabilities:
  api_available: false
  mcp_available: false
  manual_required: true
  analytics_api: false
  comment_response_api: false
  fallback_chain: [manual]
  api_note: "TikTok API nincs konfigurálva. Publikálás: manuális — TikTok mobilapp. Analytics: TikTok Creator-portal manuálisan."
authentication_state:
  account_handle: TBD
  account_url: TBD
  account_status: "TBD — profil handle és URL azonosítása szükséges (lásd Channels/tiktok.md)"
  page_access_token: absent
---

# Navigator-TT — Channel DNA (proposal)

> **Státusz: proposal.** Ez a fájl Presto-által generált javaslat. Az `active` státuszhoz emberi jóváhagyás szükséges.

> **Kísérleti jelölés:** Ez a Channel DNA **kísérleti fázisban** érvényes — EP43, EP44, EP45 TikTok Reel-jei alapján döntünk a csatorna fenntartásáról vagy visszavonásáról. Lásd §10 Strategic decision gate.

---

## §1 — Csatorna-identitás és szerepkör

A TikTok a Navigátor Podcast számára **algoritmus-vezérelt discovery csatorna** — potenciálisan, ha a hipotézis igazolódik. Nem core platform, nem a mélység helye. Egyetlen szerepe: az epizód intro-szegmensét eljuttatni olyan emberekhez, akik még nem ismerik a Navigátort, és akiket az algoritmus a tartalom alapján ide sodor.

**A csatorna nem:**
- Nem helyettesíti a YouTube-ot — ott él a mélység, az érvelés, a 100+ perces párbeszéd
- Nem rendszeres, önálló tartalom-felület
- Nem trend-gyár — a Navigátor brand-je Bátorság-alázat értéken áll, nem trend-hullókon

**A csatorna igen:**
- Discovery-kapu: ha az algoritmus a content-alapú ajánlásokkal eléri a potenciális Navigátor-nézőt
- Reel-terjesztési pont: az epizód intro-szegmensének vertikális változata (ugyanaz az anyag, mint az IG és FB Reel)
- Hipotézis-tesztelő: bizonyítja vagy cáfolja, hogy TikTok algoritmus elér idősebb audience-t releváns tartalommal

**A discovery-funnel:**
```
TikTok Reel (T+1, 30-60s)
    ↓ (hook rezonál)
TikTok bio-link
    ↓
YouTube epizód (teljes hossz)
```

A konverzió (TikTok → YT) várhatóan **hosszabb és alacsonyabb arányú**, mint IG-ről — a TikTok közönsége scroll-reflex-vezérelt, nem mélységre orientált. Ez elfogadott korlát, nem ok a formátum megváltoztatására.

---

## §2 — Audience-mismatch elemzés és stratégiai kockázat

### Demográfiai ütközés

| Dimenzió | Navigátor core (YT adatok) | TikTok platform-átlag | Mismatch fok |
|---|---|---|---|
| Korosztály | 45-54 domináns (33.3%), 35+ = 89.6% | 18-34 domináns (~60-65%) | **MAGAS** |
| Nem | 53% nő, 47% férfi | ~55% nő, ~45% férfi | alacsony |
| Figyelmi ív | 17-20 perc átlag watch time (YT-on) | Scroll-first, rövid figyelem | MAGAS |
| Tartalom-igény | Mélység, érvelés, autentikus keresés | Hook-first, entertainment reflex | MAGAS |

> **Forrás-megjegyzés:** TikTok demográfia általános platform-statisztikákból becsülve — Navigátor-specifikus TikTok Analytics nem áll rendelkezésre.

### Mismatch-kezelési hipotézis

A TikTok algoritmus **nem-demográfiai alapon is ajánl** — a watch time, completion rate és share-viselkedés alapján képez topic-klasztereket. Ez azt jelenti:

- Ha a 30-60 másodperces Reel completion rate-je magas → az algoritmus topic-kompatibilis users-nek ajánlja, függetlenül a korosztálytól
- A pszichológia/egészség/nevelés témák TikTok-on **jelen vannak az idősebb (35-54) szegmensben is** — de ez Navigátor-specifikus adattal nem validált

### Stratégiai kockázat

> **Explicit jelölés: KÍSÉRLETI csatorna, potenciális erőforrás-pazarlás kockázatával.**

| Kockázat | Leírás | Valószínűség |
|---|---|---|
| Erőforrás-pazarlás | Ha a TikTok nem hoz YT-konverziót, a Reel-upload manuális munkája nem térül meg | KÖZEPES — de a T+1 Reel munka IG/FB/YT Shorts-szal párhuzamos (marginális többletköltség) |
| Brand-dilúció | Ha a TikTok-os megjelenés nem illeszkedik a Navigátor-hanghoz, az sértheti a brand-koherenciát | ALACSONY — ha a tone-szabályok (§3) betartva maradnak |
| Túl-investálás | Ha kísérleti fázis után nem mérünk és folytatjuk „inerciaból" | KÖZEPES — §10 decision gate véd ellene |

**Javasolt hozzáállás:** a T+1 Reel-hullám részeként TikTok is kap tartalmat (marginális extra munka az IG/FB Reels mellé), de **semmi egyebet nem fektetünk bele** a mérési fázis lezárásáig.

---

## §3 — Tone és stílus

### Default tone

`punchy-but-substantial-hu` — a TikTok-közönség gyorsabb reflextől vezérelt, mint a YouTube néző, ezért az első 3 másodperc dönt. DE: a tartalom mögöttes értéke a Navigátor-értékrendet tükrözi. A „punchy" a formátumra vonatkozik, nem a mélység feladására.

### Tone-dimenziók

| Dimenzió | Pozíció | Magyarázat |
|---|---|---|
| Formális vs. informális | 3/5 informális | Közelebbi hang mint YT, de nem barátos-szleng. Tegezés természetes. |
| Érzelmi vs. analitikus | 4/5 érzelmi | Az első 3 másodpercnek el kell kapni a scrollolót — érzelmi hook, kérdés vagy paradoxon. |
| Inspiráló vs. pragmatikus | 3/5 inspiráló | Hook: kérdés vagy feszültség. A recept a YouTube-on van — itt a „be akarsz menni?" élmény kell. |
| Humor | ritkán, természetesen | Csak ha az epizódban volt autentikus humor. Erőltetett soha. |

### Emoji-politika

Minimális. Max 1-2 emoji a caption-ben, kizárólag ha vizuálisan tagol. Soha ne helyettesítse a szöveget. A TikTok fiatal audience-hez megszokott emoji-töménység NEM illeszkedik a Navigátor-brandhez.

### Ami SOHA nem szabad (tone-szinten)

- **Brain-rot szókincs tiltott** — „rizz", „based", „slay", „no cap", „bussin", „lowkey/highkey" és hasonlók. Az Alkotmány Integritás-értéke azt mondja: szavaink a valóságot tükrözzék. Ezek a szavak nem a Navigátor-valóságát tükrözik.
- **Clickbait drama tiltott** — „ez megváltoztatta az életemet", „ezt nem hitted volna", „SOKKOLT amit mondott". A title-expectation gap rombolja a bizalmat — ugyanúgy, mint YT-on (Navigator-YT.md §6/1).
- **Trend-hangzás tiltott** — ha a caption-ben lévő hang TikTok-trend-szlengre hajaz, az ütközik az Alkotmány Bátorság-alázat értékével.

---

## §4 — Format és kadencia

### TikTok Reel (egyetlen engedélyezett formátum a kísérleti fázisban)

**Technikai spec (runbook §3.3 alapján, TikTok-specifikus kiegészítéssel):**

| Paraméter | Érték |
|---|---|
| Orientáció | Vertikális (9:16) |
| Hossz | 30-60 másodperc |
| Burned-in feliratok | Kötelező — magyar, olvasható kontraszttal |
| Hang | Sound-on optimalizált (de a burned-in subs miatt sound-off-on is értelmes) |
| Záró frame | „Teljes epizód → link a bio-ban" |
| Forrásanyag | Intro-szegmens, vagy az epizód legerősebb hook-pillanata |

**A „hook in 3 seconds" szabály:**
A TikTok algoritmus az első 3 másodpercben méri a scroll-stop arányt. Az intro-szegmensnek vizuálisan vagy verbálisan azonnal kapnia kell — ez az egyetlen TikTok-specifikus szerkesztési elvárás a többi Reel-formátumhoz képest.

### Kadencia

- **Rendszeres:** T+1 epizód-Reel (szerdán) — a runbook Step 6
- **Rendkívüli:** nincs — a kísérleti fázisban semmilyen egyéb TikTok tartalmat nem gyártunk

### Hashtag-mix

**3-5 hashtag per videó** (TikTok-on a hashtag discovery-értéke alacsonyabb mint IG-n, de a branded tag kötelező):

| Kategória | Hashtag | Kötelező? |
|---|---|---|
| Branded | `#NavigátorPodcast` | Igen |
| Magyar discovery | `#magyarpodcast` vagy `#podcast` | Igen (1 db) |
| Téma-specifikus | `#pszichológia` / `#nevelés` / `#egészség` — epizódonként | 1-3 db |

**Max 5 hashtag.** A 10+ hashtag-halmozás az Alkotmány-értékekkel ütköző spam-viselkedés és visszaesik a reach-re.

---

## §5 — Tartalomstratégia (TikTok → YT funnel)

### A funnel realitása

A TikTok-ról YT-ra mutató konverzió az összes short-form platform közül **a leghosszabb és legbizonytalanabb**:

```
TikTok scroll (passzív felfedezés)
    ↓ (completion rate + like/share)
Algoritmikus amplifikáció (ha a tartalom teljesít)
    ↓ (profil-látogatás)
Bio-link kattintás (aktív döntés)
    ↓
YouTube epizód
```

A IG-funnel (Navigator-IG.md §5) rövidebb és aktívabb közönséggel dolgozik. A TikTok-funnel passzívabb discovery-csatorna — ez nem baj, de a várakozások belőle következnek: alacsonyabb konverziós ráta, magasabb view-count potenciál.

### Témahierarchia

A YouTube-on bizonyított PopScore-modell (Navigator-YT.md §5) iránymutató — TikTok-specifikus validáció hiányzik, de az S-tier témák (pszichológia/nárcizmus, egészség, AI-praktikus) valószínűleg a legjobb TikTok completion rate-et hozzák, mert ezek a leguniverzálisabb hookkal rendelkeznek.

> **Figyelmeztetés:** Ez YT-adatokon alapuló extrapoláció — TikTok-specifikus engagement adat TBD.

### Mire NE optimalizáljunk TikTok-on

- NE optimalizáljuk a tartalmat TikTok virális trendjeire — ez a brand-t hígítja
- NE gyártsunk TikTok-natív formátumot (duet, stitch, trending audio) — nincs erre kapacitás és az Alkotmány Bátorság-alázat értékével ütközne
- NE tegyük a TikTok-elérést KPI-vá önmagában — a cél a YT-funnel-conversion, nem a TikTok view-count

---

## §6 — Forbidden patterns

### 1. Trend-chasing
**Tiltott:** Trending audio átvétele, challenge-ek részvétele, vizuális TikTok-trendek utánzása pusztán azért, mert „most menő".

**Rationale:** Az Alkotmány Megújulás-értéke explicit: „a bölcsesség megmutatja azt, hogy mi az amiben meg kell újuljunk." A trend átvétele csak akkor indokolt, ha erősíti a tartalmat — nem ha helyettesíti. A Navigátor-közönség (35-64, akik esetleg TikTok-on is megtalálhatók) azonnal érzi a hiteltelen trendet. Ezenkívül a YT core-közönség egy jövőbeli TikTok-trendre épülő tartalomtól elidegenedne.

### 2. Brain-rot szókincs
**Tiltott:** „rizz", „based", „slay", „no cap", „bussin", „it's giving", „lowkey/highkey" (TikTok-specifikus szleng).

**Rationale:** Az Alkotmány Integritás-értéke: szavaink a valóságot tükrözzék. A Navigátor brand-je komoly, alázatos keresésre épül. A brain-rot szókincs idegen testek a Navigátor-hangban, és a 35-64 éves YT-közönségnél hiteltelenséget szignalizálna.

### 3. Clickbait drama
**Tiltott:** „ez megváltoztatta az életemet", „sokkolt amit mondott", „ezt biztosan nem tudtad", hamis feszültség.

**Rationale:** Azonos a YT és IG tiltással (Navigator-YT.md §6/1, Navigator-IG.md §6/3). A title-expectation gap azonnal rombolja a bizalmat, a completion rate-et lecsökkenti, és az algoritmus bünteti.

### 4. Hashtag-spam
**Tiltott:** 10+ hashtag, irreleváns discovery-tagek halmozása.

**Rationale:** A TikTok 2023 óta pontosan méri a hashtag-relevancia-arányt. A spam visszaesik a reach-re. Max 5, releváns hashtag hatékonyabb. A Navigátor-brand autenticitásával összeférhetetlen a „mindenre rádobni" taktika.

### 5. Kontextus nélküli kivágás
**Tiltott:** Az epizódból kivágott jelenet a vendég személyének vagy szavainak torzításával, kontextus nélküli dramatizálással.

**Rationale:** A Navigátor-brand a párbeszéd mélyítésére épül, nem sensational sound-bite-okra. Ha egy idézet kiszakítva félrevezető, nem posztolható — még ha TikTok-on virális lenne is.

### 6. Cross-post automatizmus IG-ről TikTok-ra
**Tiltott:** Ugyanaz a Reel-fájl minden szerkesztés nélkül IG → TikTok cross-post (Meta-TikTok direkt cross-posting).

**Rationale:** Az IG-algoritmus és a TikTok-algoritmus különböző viselkedést jutalmaz. Az IG Reel caption-struktúrája (bio-link utalás, hashtag-mix 5-12) nem optimális TikTok-ra. A burned-in subs ugyan mindkét platformon segít, de a caption és a hook-struktúra minimálisan eltérhet. A mechanikus cross-post suboptimális mindkét platformon.

---

## §7 — Validated examples (TBD)

> **Nincs validált TikTok-specifikus adat.** A fiók azonosítása (lásd Channels/tiktok.md) és az első Reel-hullám végrehajtása (EP43 T+1) szükséges az első mintákhoz.

| Epizód | TikTok views | Completion rate | YT-konverzió (bio-link) | Forrás |
|---|---|---|---|---|
| — | TBD | TBD | TBD | TikTok Creator Analytics (első audit után) |

---

## §8 — Anti-examples (TBD)

> Az első 3 TikTok Reel tapasztalata után kitöltendő. Javasolt: EP43-EP45 launch-ok után retrospektív.

---

## §9 — Iterations history és nyitott kérdések

### Iteration history

- 2026-05-26 — v0.1.0 — initial proposal — Presto v0.8.0, Navigator-IG.md és Navigator-YT.md mintájára, episode-launch.md Step 6 alapján

### TBD / Nyitott kérdések

| # | Kérdés | Forrás hiánya | Következő lépés |
|---|---|---|---|
| TBD-01 | Strategic-fit validáció — elér-e a TikTok algoritmus 35-54 éves audience-t releváns tartalommal? | Nincs TikTok Analytics adat | §10 decision gate: EP43+EP44+EP45 mérés |
| TBD-02 | TikTok fiók handle és URL azonosítása | tiktok.md: TBD | Ellenőrizni a fiókot; ha nincs, döntés: létrehozunk-e |
| TBD-03 | Optimális TikTok posztolási idő | Nincs Creator Analytics adat | EP43 után TikTok Creator Portal → Analytics → Followers → Activity |
| TBD-04 | Sound-on vs sound-off completion rate | Nincs adat | EP43 + EP44 Reel-eken mérni — az audió befolyásolja-e a completion rate-et (burned-in subs véd, de sound-on optimalizált) |
| TBD-05 | TikTok → YT funnel-conversion mérés | Bio-link click nincs tracking | UTM-link a TikTok bio-ban (pl. `?utm_source=tiktok`) vs. FB bio-link → összevetés |
| TBD-06 | Hook-szerkesztés szükséges-e az IG Reel-től eltérően? | Nincs A/B adat | EP43: azonos Reel mindkét platformon; EP44-től lehet tesztelni különböző hook-vágást |

---

## §10 — Strategic decision gate

> **Ez a szekció dönt a TikTok fenntartásáról vagy leállításáról.** Kötelező visszatérni ide EP45 után.

### Decision-point

**3 epizód mérés után** (EP43, EP44, EP45 TikTok Reel-jei) Presto `measure` módban összefoglalja az eredményeket, és az alábbi thresholdok alapján javaslatot tesz.

### Mérési metrikák (T+0 → T+7 ablak per epizód)

| Metrika | Mérési módszer | Miért fontos |
|---|---|---|
| Views per Reel | TikTok Creator Analytics | Alapelérés — megtalálja-e az algoritmus |
| Completion rate | TikTok Creator Analytics | Tartja-e a tartalom a figyelmet |
| YT bio-link click | UTM-tracking (TBD-05) | A funnel valóban konvertál-e |
| Profile visits | TikTok Creator Analytics | Érdeklődés az alkotó iránt |

### Döntési threshold (TBD — konkrét számok az első mérésnél beállítandók)

> **Megjegyzés:** konkrét view és konverziós számok TBD, mert nincs baseline adat. Az első mérés (EP43) után ezt a szekciót felül kell írni.

| Scenario | Threshold | Döntés |
|---|---|---|
| **Folytatás** | Átlag views per Reel > TBD VAGY átlag YT bio-link click > TBD | TikTok marad a runbookban aktív csatornaként |
| **Megfigyelés** | Views megvan, de YT-konverzió < TBD | 2 további epizód mérés, döntés halasztása |
| **Leállítás** | Views < TBD ÉS YT-konverzió < TBD (3 epizód átlaga) | TikTok kivesszük a runbook Step 6-ból; channel DNA `status: deprecated` |

### Kik vesznek részt a döntésben

A döntés **emberi döntés**, Presto csak az adatot hozza és a javaslatot teszi. Döntéshozó: Becze Szabolcs.

### Mikor reviewoljuk

Legkésőbb: EP45 launch utáni héten. Trigger: `/pres-measure scope:area:Navigátor Podcast` — TikTok szekció.

---

*Generálta: Presto v0.8.0 — 2026-05-26 — forrás: episode-launch.md (runbook Step 6), Navigator-YT.md, Navigator-IG.md, Navigator-FB.md, Channels/tiktok.md, A Navigátor Podcast Alkotmánya.md, MARKETING_ENGINE.md. TikTok-specifikus metrikák: TBD — első audit az EP43 launch után.*
