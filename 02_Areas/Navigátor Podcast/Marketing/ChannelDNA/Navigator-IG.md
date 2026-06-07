---
schema: presto.channel-dna.v1
area: Navigátor Podcast
channel: instagram
display_name: Instagram — Navigátor Podcast
status: proposal
version: 0.1.0
date: 2026-05-26
author: Becze Szabolcs
description: Navigátor Podcast Instagram csatorna Channel DNA — presto.channel-dna.v1 séma. Tartalmaz: csatorna-szerepkör és audience-mismatch elemzés, Reels-centrikus format-mix, tone-szabályok (visual-aware, NEM aesthetic-only), hashtag-politika, tartalomstratégia (IG mint Reel-kapu), forbidden patterns, TBD-jelölések. Forrás: episode-launch.md runbook (T+1 Reel step), Navigator-YT.md (YT demográfia cross-platform extrapoláció), instagram.md (channel-profile), MARKETING_ENGINE.md, Alkotmány.
id: 394f9140-677b-4937-ab18-790d404b91ec
index_schema_version: 1
bdos_index: true
audience_data_source: "Becsült — YouTube Analytics demográfiai extrapoláció + instagram.md (fiók-azonosítás: TBD). IG-specifikus Insights adat: TBD."
primary_language: hu
allowed_formats: [reel, story, carousel, single-image]
constraints:
  max_chars:
    caption: 2200
    recommended_visible: 125
  max_hashtags: 15
  link_in_bio: true
  link_in_caption: false
posting_rhythm:
  recommended_cadence: "minden új epizód T+1-én (szerdán) — Reel; Stories: ritka, alkalmi"
  optimal_day: szerda
  optimal_hours_local: TBD
  rationale: "T+1 Reel a runbook Step 3 alapján — episode-launch.md §3.3. IG-specifikus best time: TBD (nincs Insights adat)."
publication_capabilities:
  api_available: false
  mcp_available: false
  manual_required: true
  analytics_api: false
  comment_response_api: false
  fallback_chain: [manual]
  api_note: "Instagram Graph API nincs konfigurálva. Publikálás: manuális — IG mobilapp vagy Creator Studio. IG Insights: manuálisan elérhető az appban."
authentication_state:
  account_handle: TBD
  account_url: TBD
  page_access_token: absent
  oauth_account: TBD
  account_status: "TBD — fiók azonosítása szükséges (lásd instagram.md: 'Navigátor Podcast saját IG fiók azonosítandó')"
---

# Navigator-IG — Channel DNA (proposal)

> **Státusz: proposal.** Ez a fájl Presto-által generált javaslat. Az `active` státuszhoz emberi jóváhagyás szükséges.

> **Figyelmeztetés:** Az IG fiók (handle, URL, followers) azonosítása még nem történt meg — lásd `Channels/instagram.md`. Az alábbi DNA-tartalom a fiók meglétét feltételezi. Ha nincs dedikált Navigátor IG fiók, az első lépés a döntés: külön fiók vs. személyes @beczesz profil.

---

## §1 — Csatorna-identitás és szerepkör

Az Instagram a Navigátor Podcast számára **belépési kapu** — nem önálló tartalom-felület. Szerepe: az epizód legemlékezetesebb 30-60 másodpercét vizuálisan tömöríteni, és azokat elérni, akik a 35-64 éves Navigátor-közönségnél némileg fiatalabb (25-44) digitális térben mozognak.

**A csatorna nem:**
- Nem helyettesíti a YouTube-ot (ott él a mélység és az érvelés)
- Nem aesthetics-brand (nem szép képek, szép idézetek önmagukért)
- Nem trend-gyár (Instagram trendjeit nem követjük tartalom nélkül)

**A csatorna igen:**
- Reel-kapu: az intro-szegmens természetes discovery eszköze
- Audience-híd: a 25-44 éves, IG-aktív szegmens felé nyitott csatorna
- Epizód-amplifikátor: a runbook T+1 hulláma itt csap le először a vertikális térben

**Alkotmány-gyökerek:**
- Megújulás: „Használnunk kell a szociális média által feltárt lehetőségeket, új platformokat, trendeket kell átvegyünk" — az IG-jelenlét az Alkotmány Megújulás-értékének közvetlen alkalmazása
- De a „bölcsesség megmutatja azt, hogy mi az amiben meg kell újuljunk" — az IG-n sem adjuk fel a mélységet a vizualitásért

---

## §2 — Közönség-profil és audience-mismatch

> **Figyelmeztetés:** Minden alábbi adat **becsült** — YouTube Analytics demográfiából extrapolálva, IG-specifikus Insights nélkül.

### Navigátor core vs. IG-szegmens

| Dimenzió | Navigátor core (YT adatok) | IG-skew (platform általános) | Overlap |
|---|---|---|---|
| Korosztály | 45-54 domináns (33.3%), 35+ = 89.6% | 25-34 domináns, 18-44 = ~75% | 35-44 sáv — potenciális híd |
| Nem | 53% nő, 47% férfi | ~55-60% nő | nő-skew konzisztens |
| Viselkedés | Mélységre hajlandó, 17-20 perc átlag watch time | Rövidebb figyelmi ablak, scroll-first | Csak ha a Reel eléggé hook-erős |
| Geográfia | HU 61.7% + Erdély 15.8% | Magyar IG-felhasználók — hasonló földrajz | Valószínűleg konzisztens |

**Audience-mismatch kezelése:**
- A Navigátor 45-54 éves magjának csak egy kisebb szegmense IG-aktív — ez elfogadott korlát
- Az IG a fiatalabb (35-44) szegmens elérésére optimalizált, aki 5-10 éven belül belép a core-demográfiába
- NE adjuk fel a brand-mélységet a 25-34 évesek kedvéért: a Reel hook erős legyen, de a tartalom mögöttes értéke a Navigátor-értékrendet tükrözze

---

## §3 — Tone és stílus

### Default tone

`visual-storyteller-builder-hu` — a házigazda röviden, vizuálisan fogalmaz, de NEM aesthetics-only. A Reel caption nem reklám, hanem **meghívás egy gondolkodási pillanatba**.

### Tone-dimenziók

| Dimenzió | Pozíció | Magyarázat |
|---|---|---|
| Formális vs. informális | 3/5 informális | Tegezés, személyes hang — de nem szleng. Az IG közelséget igényel, de a Navigátor-brand nem csúszik könnyed-barátkozásba. |
| Érzelmi vs. analitikus | 4/5 érzelmi | A caption az érzelem-kapu. Az elemzés a YouTube hosszú formátumé — itt a hook-érzelmet kell megütni. |
| Vizuális-poetic vs. builder-tone | 2/5 vizuális-poetic | Engedélyezett, hogy kicsit poétikusabb legyen mint YT vagy FB, de **soha nem vesz el a Builder-tónusból** (Bátorság-alázat, keresés, harmadik út). |
| Inspiráló vs. pragmatikus | 3/5 inspiráló | Cél: kíváncsiságot felkelteni és átkattintani. Nem recept (az a YT-on van), hanem kérdés vagy paradoxon. |
| Humor | ritkán, természetesen | Ha a vendéggel volt autentikus vicces pillanat, az idézhető. Erőltetett humor tiltott. |

### Emoji-politika

Mérsékelt, strukturált célra. Max 3 emoji/caption. Nem díszítés, hanem vizuális tagolás (pl. ▶ a link előtt). Az idézőjeles hook-sorban soha. A 45+ IG-felhasználóknál sem zavaró, ha célzott — de nem szükséges.

---

## §4 — Format-mix és kadencia

### Reels (primer formátum)

**Szerepe:** T+1 epizód-launch hullám — az epizód intro-szegmense (első 30-60 másodperc, vagy a legerősebb hook-pillanat).

**Technikai spec (runbook §3.3 alapján):**
- Vertikális 9:16
- 30-60 másodperc
- Burned-in magyar feliratok (sound-on optimalizált, de sound-off-ra felkészítve)
- Záró frame: „Teljes epizód → link a bio-ban"

**Caption-struktúra:**
1. Hook (1 sor) — az interjú legemlékezetesebb mondata idézőjelben, vagy egy nyitott kérdés
2. Kontextus (1-2 sor) — vendég neve + epizód tétje, egy mondatban
3. CTA (1 sor) — „Teljes epizód: link a bio-ban" vagy hasonló
4. Hashtagek (lásd §4 hashtag-politika)

**Megcélzott reach (runbook success criteria):** kombinált IG+FB+TT+YT Shorts views > 1500 (T+24h)

### Stories (szekunder, ritka)

- Csak epizód-launch napon (T+0) vagy T+1-én, figyelemfelkeltésre
- 24 órás láthatóság — nem tartós tartalom
- Típus: swipe-up link (ha elérhető), vagy egyszerű grafikus emlékeztető az új epizódról
- TBD — nincs tapasztalati adat, stratégia iterálandó

### Carousel (jövő, TBD)

- Potenciális formátum: epizód kulcs-gondolatok vizualizálva (3-7 slide)
- Magasabb produkciós igény — nem prioritás a jelenlegi fázisban
- Csak ha Reels-stratégia stabilizálódott és van kapacitás

### Single-image post (alkalmi)

- Vendég-fotó + idézat overlay
- Csak ha vizuálisan erős anyag van (nem kötelező per epizód)
- TBD — produkciós workflow még nem definiált

### Hashtag-politika

IG-n a hashtag-elérés (discovery) még számít — de a spam-szintű hashtag-halmozás visszafelé süt.

**Javasolt mix (5-15 összesen):**

| Kategória | Példák | Darab |
|---|---|---|
| Branded | `#NavigátorPodcast` `#NavigatorPodcast` | 2 (mindig) |
| Téma-specifikus | `#pszichológia` `#nevelés` `#egészség` `#önfejlesztés` | 3-5 (epizódonként változó) |
| Discovery (általános) | `#magyarpodcast` `#podcast` `#mélyinterjú` | 2-3 |
| Niche | vendégnév-tag, pl. `#gergelyistvan` — csak ha releváns | 0-2 |

**Max 12 hashtag/poszt** (15 technikai max, de 12 a praktikus határ a spam-jelzés elkerüléséhez).

---

## §5 — Tartalomstratégia (Reel → IG → YT funnel)

### A funnel logikája

```
YT hosszú epizód (T+0)
    ↓
IG Reel — intro-szegmens (T+1)
    ↓
IG bio-link / caption CTA
    ↓
YouTube epizód (teljes hossz)
```

Az IG **nem önálló tartalom-felület** — minden IG tartalom visszavezet a YouTube-ra. A konverzió mértéke (IG → YT click) egyelőre nem mérhető (nincs Insights adat), de a funnel-logika a runbook §3.3-ból és a FB-analógiából következik.

### Témahierarchia (YT PopScore-modell IG-re alkalmazva)

A YouTube-on bizonyított témahierarchia (Navigator-YT.md §5) iránymutató — de IG-specifikus validáció hiányzik.

| Tier | Témák | IG-relevancia hipotézis |
|---|---|---|
| S | Pszichológia/nárcizmus, Egészség, AI-praktikus | Valószínűleg magas megoszthatóság a 35-44 IG-szegmensben |
| A | Párkapcsolat, szülőség/nevelés | Erős érzelmi rezonancia, shares-re hajlamos |
| B | Hit/spiritualitás, közélet | Alacsonyabb — de hiteles követők esetén értékes |
| C | IT/startup (nem praktikus), niche | Gyenge IG-elérés várható |

> **Fontos:** Ez extrapoláció — IG-specifikus engagement adat TBD.

### IG mint fiatalabb közönség híd

Az IG a 35-44 sávba tartozó „középgeneráció" elérésére alkalmas, akik a Navigátor core-közönségénél 10-15 évvel fiatalabbak, de értékileg kompatibilisek. Céltudatosan nem próbálunk 25-34 éveseket tömegesen megszólítani (ehhez más tartalom kellene) — de a 35-44 éves, IG-aktív szegmens természetes táguló kör.

---

## §6 — Forbidden patterns

### 1. Aesthetic-only tartalom
**Tiltott:** Szép idézet + szép háttér + semmi más. „Inspiráló" slide-ok a podcast valódi tartalmától elszakadva.

**Rationale:** Az IG-n való vizuális megjelenés NEM jelenti azt, hogy a tartalom felszínesedhet. A Navigátor brand-je mélységre és keresésre épül (Alkotmány). Egy önmagában szép idézet-poszt más podcastoktól megkülönbözhetetlen — és a Navigátor differenciátora pontosan az, hogy nem ilyen. Ha nincs mit mondani, inkább ne posztoljunk.

### 2. Hashtag-spam
**Tiltott:** 20-30 hashtag/poszt, irreleváns discovery-tagek halmozása (pl. `#love #instagood #viral` egy podcast-poszthoz).

**Rationale:** Az IG algoritmus 2023 óta pontosan felismeri a hashtag-spamot, és csökkenti az organikus elérést. A Navigátor brand autenticitásával összeférhetetlen a „mindenre rádobni" taktika. Max 12, releváns hashtag hatékonyabb.

### 3. Trend-chasing tartalom nélkül
**Tiltott:** IG audio-trendek, challenge-ek, vagy vizuális trendek átvétele pusztán azért, mert „most menő" — ha a tartalom nem illeszkedik a Navigátor-hanghoz.

**Rationale:** Az Alkotmány Megújulás-értéke explicit: „a bölcsesség megmutatja azt, hogy mi az amiben meg kell újuljunk." A trend átvétele csak akkor indokolt, ha erősíti a tartalmat — nem ha helyettesíti. A Navigátor 35-64 éves magtörzse azonnal érzi a hiteltelen trendet.

### 4. Engagement begging
**Tiltott:** „Ments el ha hasznos!", „Tag-eld azt, aki ezt hallgatja!", „Nyomj szívet ha te is így érzed!" (ismétlőn, mechanikusan).

**Rationale:** Azonos a YT (Navigator-YT.md §6/3) és FB (Navigator-FB.md §6/2) indoklással. Az organikus mentés/megosztás értékesebb, mint a kierőszakolt. Egy természetes, epizódhoz kötött CTA (pl. „Ha ismerős, oszd meg") nem tiltott.

### 5. Önálló IG-tartalom a podcast-kontextus nélkül
**Tiltott:** Általános motivációs idézetek, önállóan lebegő gondolatok amelyek semmilyen Navigátor-epizódhoz nem köthetők.

**Rationale:** Az IG a podcast ernyője alatt él. Minden poszt erősítse a Navigátor-identitást és vezessen vissza az epizódhoz (ahol releváns). A kontextus nélküli tartalom elbizonytalanítja a követőket, mit is képvisel ez a fiók.

---

## §7 — Validated examples (TBD)

> **Nincs validált IG-specifikus adat.** A fiók azonosítása (lásd instagram.md) és az első Reel-hullám végrehajtása (EP43 vagy EP44 launch) szükséges az első mintákhoz.

| Epizód | IG Reel views | Saves | Shares | Forrás |
|---|---|---|---|---|
| — | TBD | TBD | TBD | IG Insights (első audit után) |

**Hipotézis (YT-adatokból extrapolálva, nem validált):**
- Pszichológia/nevelés témájú epizódok (S/A-tier YT) valószínűleg a legjobb IG Reel-teljesítményt hozzák
- A Bencze Edit-effektus (EP14, EP28 nárcizmus) valószínűleg IG-n is erős megosztási hajlandóságot generál — de ez IG adattal nem validált

---

## §8 — Anti-examples (TBD)

> Az első 3-5 Reel tapasztalata után kitöltendő. Javasolt: EP43-EP45 launch-ok után retrospektív.

---

## §9 — Iterations history és nyitott kérdések

### Iteration history

- 2026-05-26 — v0.1.0 — initial proposal — Presto v0.8.0, Navigator-FB.md és Navigator-YT.md mintájára

### TBD / Nyitott kérdések

| # | Kérdés | Forrás hiánya | Következő lépés |
|---|---|---|---|
| TBD-01 | Navigátor Podcast saját IG fiók létezik-e? | instagram.md: fiók azonosítása TBD | Ellenőrizni: van-e @navigatorpodcast vagy hasonló handle; ha nincs, döntés személyes @beczesz profil vs. külön fiók |
| TBD-02 | IG Insights demográfia | Nincs IG fiók azonosítva | Első audit az appban (followers, age, gender, top locations) |
| TBD-03 | Optimális IG posztolási idő | Nincs Insights adat | IG app → Insights → Audience → Most aktív → exportálni |
| TBD-04 | Reel completion rate és engagement | Nincs korábbi Reel adat | EP43 Reel első 48h után mérni: views, plays, saves, shares |
| TBD-05 | Audience-overlap (YT vs IG) | Nincs cross-platform analytics | IG Insights korosztály vs. YT Analytics demográfia összevetés |
| TBD-06 | Story stratégia | Nincs kísérlet | EP43 launch-on teszt: story T+0 vs. T+1, engagement mérése |
| TBD-07 | Carousel formátum feasibility | Produkciós workflow nincs definiálva | Döntés: van-e kapacitás vizuális slide-ok készítésére epizódonként |
| TBD-08 | IG Reels vs. YT Shorts — melyik teljesít jobban? | Nincs összehasonlítható adat | EP43 + EP44 A/B: azonos Reel, mindkét platformon mérve |
| TBD-09 | Comment-moderáció tone | Nincs IG comment-reply guideline | `comment-scan` mód első futtatása után generálni |

---

*Generálta: Presto v0.8.0 — 2026-05-26 — forrás: episode-launch.md (runbook), Navigator-YT.md, Navigator-FB.md, instagram.md (channel-profile), MARKETING_ENGINE.md, A Navigátor Podcast Alkotmánya.md. IG-specifikus metrikák: TBD — első audit az EP43/44 launch után.*
