---
schema: presto.channel-dna.v2
area: Navigátor Podcast
channel: facebook
display_name: Facebook — Navigátor Podcast
status: proposal
version: 0.1.0
date: 2026-05-26
author: Becze Szabolcs
description: Navigátor Podcast Facebook oldal Channel DNA — presto.channel-dna.v2 séma. Tartalmaz: csatorna-identitás, közönségdemográfia (becsült, Analytics API FB-specifikus adat nélkül), tone-szabályok, posting rhythm, execution capabilities, forbidden patterns, operacionalizált insights. Forrás: Navigator-YT.md (YouTube Analytics) + channel.md traffic-source-adat (FB external 7.9%) + általános FB best-practice. FB-specifikus retention/reach adat: TBD.
id: b3c7d1e5-f2a4-4b6c-8d9e-1f0a2b4c6d8e
index_schema_version: 1
bdos_index: true
audience_data_source: "Becsült — YouTube Analytics (cross-platform demográfiai extrapoláció) + channel.md FB external traffic 7.9%. FB Page Insights API: TBD."
primary_language: hu
allowed_formats: [video-link-post, text-post, photo-post, reel, story, live]
constraints:
  max_chars:
    post_text: 63206
    recommended_visible: 477
  max_hashtags: 5
  link_in_text: true
  link_preview: true
posting_rhythm:
  recommended_cadence: "minden új epizód megjelenésekor + heti 1 önálló poszt"
  optimal_day: TBD
  optimal_hours_local: TBD
  rationale: "FB posting time: TBD — nincs FB Page Insights adat. YouTube-on kedd 10:00/18:00 a legjobb (channel.md §7); a párhuzamos FB-publikálás (YouTube megjelenéssel egy napon) az eddigi gyakorlat alapján ésszerű, de FB-specifikus adat hiányzik."
publication_capabilities:
  api_available: false
  mcp_available: false
  manual_required: true
  analytics_api: false
  comment_response_api: false
  fallback_chain: [manual]
  api_note: "Facebook Graph API nincs konfigurálva. Publikálás: manuális — facebook.com/navigatorpodcast. FB Page Insights: manuálisan exportálható."
authentication_state:
  page_access_token: absent
  oauth_account: TBD
  page_url: TBD
---

# Navigator-FB — Channel DNA (proposal)

> **Státusz: proposal.** Ez a fájl Presto-által generált javaslat. Az `active` státuszhoz emberi jóváhagyás szükséges.

---

## §1 — Csatorna-identitás és szerepkör

A Navigátor Podcast Facebook oldala **terjesztési és közösségi csatorna**, nem önálló tartalom-gyártó. Elsődleges szerepe: a YouTube-on megjelent epizódokat egy organikusan aktív, elkötelezett FB-közösségnek eljuttatni, és a megosztás révén visszavezető forgalmat generálni YouTube-ra.

A YouTube Analytics adatok szerint a FB external forgalom a csatorna **7.9%-át teszi ki** (channel.md §5 alapján) — ez a harmadik legnagyobb külső forgalmi forrás. Ez bizonyítja, hogy a FB organikus megosztás valóban működik és a csatorna növekedésének érdemi összetevője.

**A FB csatorna nem:**
- Nem helyettesíti a YouTube-ot (ott él a mélység)
- Nem „komment-szinkronizátor" (a FB közösség más, mint a YT közönség)
- Nem reklámfelület (a Navigátor brand-je autenticitásra épül)

**A FB csatorna igen:**
- Kapuőr — a néző itt hall először egy epizódról, mielőtt YT-ra megy
- Amplifikátor — a megosztás organikus terjedést generál az ismerősi hálón
- Visszacsatoló loop — kommentek és reakciók jelzik, melyik téma érinti meg a közönséget

---

## §2 — Közönség-demográfia

> **Figyelmeztetés:** Az alábbi adatok **becsültek** — YouTube Analytics demográfiai adataiból extrapolálva, nem FB Page Insights-ból. FB-specifikus demográfia: **TBD** (manuális Page Insights exportálás szükséges).

### Extrapolált demográfia (YT-alapon)

| Jellemző | Becsült érték | Forrás |
|----------|---------------|--------|
| Nem | ~53% nő, ~47% férfi | YT Analytics (Navigator-YT.md §2) |
| Korosztály | 45-64 domináns | YT Analytics (Navigator-YT.md §2) |
| Geográfia | Magyarország + Erdély fő közönség | YT Analytics (Navigator-YT.md §2) |
| Elsődleges érdeklődési körök | Egészség, pszichológia, párkapcsolat, önfejlesztés | Patterns.md szintézis |

### Közönség-portré (becsült)

Tipikus FB-követő: 45-60 éves magyar nő, aki az epizódokra ismerősei megosztásán vagy a csatorna oldalán talál rá. A YT-os nézőnél kissé kevésbé „deep-dive" orientált — a FB poszt alapján dönti el, hogy megnézi-e a teljes epizódot. Az első 2-3 sorból kell meggyőzni.

---

## §3 — Tone és stílus

### Default tone
`podcast-host-warm-personal-hu` — A házigazda szól a közösséghez, nem egy szerkesztőség. Az első személy természetes. A poszt nem reklám, hanem meghívás: „ezt ma gondoltuk át, gyere te is velünk."

### Tone-dimenziók

| Dimenzió | Pozíció | Magyarázat |
|----------|---------|------------|
| Formális vs. informális | 3/5 informális | Tegezés vagy magázás — a YT-os megszólítási konvencióval konzisztens. Nem barátos-szleng, de közel áll. |
| Érzelmi vs. analitikus | 4/5 érzelmi | A FB-poszt az érzelem-kapu. Az elemzés a videóban van — itt csak a belépési szándékot kell felkelteni. |
| Tanári vs. kereső | 2/5 tanári | Kereső, meghívó tone — „kíváncsiak voltunk arra, hogy..." |
| Inspiráló vs. pragmatikus | 3.5/5 inspiráló | A cél érzelmi trigger + kíváncsiság, nem utasítás. |
| Humor | ritkán, természetesen | Ha a vendéggel volt vicces pillanat, az idézhető. Forced humor tiltott. |

### Emoji-politika
Mérsékelt. Max 3-4 emoji/poszt, kizárólag vizuális tagolásra (pl. ▶ link előtt). Soha ne legyen az egyetlen tartalom. A 45-64 éves közönség nem igényel emojit, de nem is zavaró ha célzottan van.

---

## §4 — Poszt-formátumok és struktúra

### Epizód-launch poszt (primer formátum)

**Célja:** Minden új YouTube-epizód megjelenésekor — a nézők Facebook-on értesülnek és rákattintanak.

**Struktúra:**
1. **Hook (1-2 sor)** — a videó legemlékezetesebb mondata, kérdése vagy paradoxona. Idézet formátum: `„Idézet" – Vendég neve`. Vagy kérdés-formátum: `Mi a különbség a fegyelem és az erőszak között a nevelésben?`
2. **Kontextus (2-4 sor)** — miért fontos most, ki a vendég, mi a tét. Nem szinopszis — hanem **miért érdemes megnézni**.
3. **Link** — YouTube epizód URL, rövid CTA (pl. `▶ Az epizód itt:`)
4. **1-2 hashtag** — #NavigátorPodcast + téma-tag (pl. #nevelés, #pszichológia)

**Hossz:** Látható (kattintás nélküli) rész max 4-5 sor. A FB 477 karakter után „Bővebben" linket tesz — ez elé a legfontosabb kerüljön.

### Önálló tartalom-poszt (szekunder formátum)

**Célja:** Heti 1 alkalommal a közösség megszólítása epizód nélkül is — gondolat, kérdés, idézet, kulisszák mögé betekintés.

**Típusok:**
- Epizódból kimetszett idézet + rövid kontextus
- Házigazda saját gondolata egy aktuális témáról
- Kérdés a közösségnek (engagement-driven, de autentikus — nem „nyomj like-ot")
- Forgatás előtti/utáni köszönet, visszajelzés

**Hossz:** 3-8 sor. Nincs kötelező link.

### Reel (opcionális, kísérletként)

**Célja:** Short-form awareness — csak ha az epizódból kivágható egy 60-90 mp-es, önmagában érthető jelenet.
**Megjegyzés:** A YT Shorts tapasztalat (17.8% views, 0.4% watch time — Navigator-YT.md §4) óvatosságra int: a rövid formátum forgalmat hoz, de nem mélységet. FB Reels hasonlóan kezelendő: kísérlet, nem primér csatorna.

### Story (opcionális, alacsony prioritás)
Csak promóciós időszakban (epizód launch napján). 24 órás láthatóság. TBD — nincs tapasztalati adat.

---

## §5 — Tartalomstratégia és témaválasztás

### A YT PopScore-modell alkalmazása FB-re

A YouTube-on bizonyított témahierarchia (Navigator-YT.md §5) a FB-posztokra is érvényes iránymutató:

| Tier | Témák | Várható organikus elérés |
|------|-------|--------------------------|
| S | Pszichológia/nárcizmus, Egészség (vércukor, fáradtság), AI ha praktikus | Magas — megosztásra hajlamos témák |
| A | Párkapcsolat/házasság, Szülőség/nevelés, Visszatérő vendég | Közepes — erős érzelmi rezonancia |
| B | Politika/közélet, Hit/spiritualitás | Alacsony — polarizál, ritkábban megosztott |
| C | IT/startup (ha nem praktikus), Niche | Nagyon alacsony |

> **Figyelmeztetés:** Ez YT adatokon alapul — FB-specifikus reach/engagement adatok: **TBD.**

### Megosztás-amplifikáció logika

Az EP41 (Fegyelem / Gergely István) YouTube-on **12,359 views** — a csatorna **TOP 6** epizódja nézettség szerint. Ez YouTube-metrika, nem FB-specifikus. A FB-posztjának hatása (reach, megosztások, link clicks) nincs archiválva — **TBD.**

A Bencze Edit-effektus (EP14: 72K, EP28: 12.5K YT) valószínűleg FB-n is érvényes: a nárcizmus/toxikus kapcsolat témák az organikus megosztás csúcsát hozzák — de ez FB-specifikus adattal nem validált.

---

## §6 — Forbidden patterns (explicit rationale-lal)

### 1. Clickbait hook
**Tiltott:** „SOKKOLT amit hallottam!", „Ezt el sem hitted volna!", „Mindenki erről beszél"

**Rationale:** Azonos a YT-os indoklással (Navigator-YT.md §6/1) — a 45-64 éves közönség azonnal felismeri a manipulációt, és ez a bizalom-akkumuláció ellen hat. FB-n ráadásul az algoritmus aktívan bünteti a clickbait-et 2019 óta (reach csökkentés).

### 2. Engagement begging
**Tiltott:** „Nyomj like-ot!", „Oszd meg ha egyetértesz!", „Tag-eld azt, akit ez érint!" (ismétlőn)

**Rationale:** A Navigátor-brand autenticitásra épül. Az organikus megosztás (7.9% YT forgalom) azt mutatja, hogy a közönség megosztja, ha megérinti — CTA nélkül is. Az egyszeri, természetes CTA (pl. „Ha ismerős, oszd meg") nem tiltott, de az ismétlő, gépies begging az.

### 3. Kontroverzitás erőltetése FB-algoritmikus okokból
**Tiltott:** Polarizáló frame, „ők vs. mi", politikai oldalválasztás

**Rationale:** A YT-os tanulság (Navigator-YT.md §6/4) mellett FB-on külön kockázat: a FB-algoritmus 2021 óta aktívan visszaszorítja a politikai tartalmakat és a polarizáló interakciókat (Meta Content Policy frissítések). Ez a reach-re közvetlen negatív hatással van, nem csak a brand-re.

### 4. Automatikus cross-post (copy-paste YT leírás FB-re)
**Tiltott:** A YouTube leírás (5000 karakteres, fejezetes, hashtagelt) változtatás nélkül FB-re másolva.

**Rationale:** A FB-poszt más kommunikációs kontextus — rövidebb figyelem-ablak, erősebb érzelmi trigger szükséges. A YT leírás informatív de nem konverzáló. A két formátum különböző célra optimalizált, egymás helyettesítése minőségromlás.

### 5. Ütemezett poszt az epizód-kontextus nélkül
**Tiltott:** Random idézet/gondolat posztolása anélkül, hogy az epizód-összefüggést jeleznénk.

**Rationale:** A FB-oldal a podcast ernyője alatt él — minden poszt építsen a Navigátor-brandre és vezessen vissza az epizódhoz (ha releváns). Az összefüggés nélküli tartalom megzavarja a brand-identitást.

---

## §7 — Validated examples (forrás-tisztázással)

> **Fontos forrás-korrekció:** Az alábbiakban hivatkozott EP41 teljesítménymetrikák **YouTube-adatok**, NEM FB-specifikus mérések. Ez az explicit jelölés szándékos.

| Epizód | YT views | YT-rang | FB poszt hatása | Forrás |
|--------|----------|---------|-----------------|--------|
| EP41 Fegyelem / Gergely István | 12,359 | **TOP 6** a csatornán | **TBD** — FB Page Insights hiányzik | YT Analytics (youtube-analytics API) |
| EP14 Bencze Edit (nárcizmus) | 72,000+ | TOP 1 | **TBD** — archivált FB poszt szöveg nem elérhető | YT Analytics |
| EP29 Glükózforradalom | 62,800 | TOP 2 | **TBD** | YT Analytics |
| EP40 Fegyelmezés / Gál Ildikó | ≈ 4,000-6,000 | A-tier | **TBD** | YT Analytics |

**EP41 FB poszt-szöveg:** Nincs archiválva — a poszt mintaszöveg (Navigator-YT.md + CLAUDE.md alapján) a runbook Step 2 sablonjából és a fenti tone-szabályokból vezethető le, de az eredeti szöveg nem áll rendelkezésre.

**Pattern-szabályok (YT teljesítményből extrapolált, nem FB-specifikus):**
- Pszichológia/nevelés témájú epizódok (S/A-tier YT) valószínűleg a legjobb FB-amplifikációt hozzák — de ez FB adattal nem validált
- A nárcizmus/toxikus kapcsolat témák megosztási hajlandósága az ismerősi hálón feltehetőleg magasabb, mint a niche IT/startup epizódoké

---

## §8 — Operacionalizált insights

| ID | Típus | Tanulság | Evidencia | Státusz |
|----|-------|----------|-----------|---------|
| INS-NAV-FB-001 | platform-amplification | FB external traffic a YT nézettség 7.9%-át teszi ki — ez a csatorna harmadik legnagyobb külső forgalmi forrása. Az organikus FB-megosztás érdemi szerepet játszik. | channel.md §5 (YT external traffic sources) | active |
| INS-NAV-FB-002 | narrative-resonance | YT S-tier témák (nárcizmus, egészség, AI-praktikus) valószínűleg a legnagyobb FB-megosztási hajlandósággal bírnak a 45-64 éves közönségnél. | YT Analytics extrapoláció — FB-validáció TBD | candidate |
| INS-NAV-FB-003 | timing-pattern | Optimális FB posztolási idő: TBD. Hipotézis: YouTube megjelenéssel egy napon, délelőtt (10:00-12:00) vagy kora este (18:00-20:00). | Nincs FB-specifikus adat | candidate |
| INS-NAV-FB-004 | format-fit | Az epizód-launch poszt (YT link + hook + kontextus) valószínűleg erősebb mint az önálló gondolat-poszt, mert a 7.9% FB→YT traffic mögött konkrét link-kattintás áll. | channel.md §5 inference | candidate |

---

## §9 — Iterations history és nyitott kérdések

### Iteration history
- 2026-05-26 — v0.1.0 — initial proposal — Presto v0.8.0, Navigator-YT.md mintájára generált FB Channel DNA

### TBD / Nyitott kérdések

| # | Kérdés | Forrás hiánya | Következő lépés |
|---|--------|---------------|-----------------|
| TBD-01 | FB-specifikus reach és engagement adatok | FB Page Insights nincs exportálva/archiválva | Manuálisan exportálni FB Page Insights-ból (last 90 days): elérés, like/komment/megosztás per poszt |
| TBD-02 | Optimális FB posztolási idő | Nincs FB Page Insights audience activity adat | Insights → Audience → When Your Fans Are Online → exportálni |
| TBD-03 | EP41 eredeti FB poszt szövege és hatása | Nincs archiválva | Visszakeresni a FB oldal timeline-ján (2026-04-20 körül), archiválni |
| TBD-04 | FB-specifikus demográfia | FB Page Insights nem olvasható API nélkül | Manuális export + összevetés a YT Analytics adatokkal |
| TBD-05 | FB Graph API konfigurálása | Nincs Page Access Token | Döntés: szükséges-e automatizálás, vagy marad manuális workflow |
| TBD-06 | Reel formátum tesztelése | Nincs FB Reels kísérlet a csatornán | Első Reel: EP42 vagy EP43 megjelenésekor, 60-90 mp jelenet kivágva |
| TBD-07 | Párhuzamos YT+FB launch-protocol | Nincs dokumentált SOP | Írni: új epizód launch-napon mi a FB poszt workflow-ja (mikor, ki, milyen sablon alapján) |

---

*Generálta: Presto v0.8.0 — 2026-05-26 — forrás: Navigator-YT.md (channel.md + patterns.md alapján), CLAUDE.md (Navigátor Podcast Area), általános FB best-practice. FB-specifikus metrikák: TBD.*
