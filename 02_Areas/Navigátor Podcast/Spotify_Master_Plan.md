# Navigátor Podcast — Spotify Master Plan

> Generálva: 2026-05-21 | Státusz: AKTÍV | Stratégia: Heti 1 archív epizód (17 hét)

---

## Scheduling Rule (2026-05-26 óta érvényes)

**MAX 2 archív Spotify-művelet hetente.**

| Hét típusa | Max archív op |
|---|---|
| Új epizód launch hét (EP43, EP44, ...) | **1** archív op |
| Normál hét (csak archive content) | **2** archív op |

"Archív op" = bármilyen Spotify-action a régi epizódokhoz (archive upload VAGY date-fix).

**Indok:** elkerülni a Spotify-pipeline és az új-EP-launch wave interference-ét. Túl sok Spotify-művelet egy héten cognitive overload (az MP3 export, upload, ellenőrzés mind manuális, mind időigényes).

**Default ütemezés:** Thursday = archive upload (Navigator-FB runbook szerint), Saturday = date-fix (ha kell) — de csak normál heteken.

**Cross-link:** [Marketing/Runbooks/episode-launch.md](Marketing/Runbooks/episode-launch.md) — a launch-week-rule visszahivatkozása.

---

## 1. Meglévő Spotify epizódok — Dátum korrekció

| EP | Vendég | Spotify dátum (HIBÁS) | YouTube dátum (HELYES) | Státusz |
|----|--------|----------------------|----------------------|---------|
| EP08 | Dr. Kurtus Aranka | 2025-07-18 | **2024-09-10** | ✅ OK (2026-05-21) |
| EP09 | Dr. Simon Károly | 2025-07-14 | **2024-09-26** | ✅ OK (2026-05-21) |
| EP10 | Elekes István | 2025-10-29 | **2024-10-08** | ✅ OK (2026-05-21) |
| EP11 | Pálfi Kinga | 2025-10-29 | **2024-10-22** | ✅ OK (2026-05-21) |
| EP14 | Bencze Edit | 2025-10-29 | **2024-12-03** | ✅ OK (2026-05-21) |
| EP16 | Erőss Gáspár | 2025-10-29 | **2024-12-27** | ✅ OK (2026-05-21) |
| EP17 | ChatGPT | 2025-10-29 | **2025-01-14** | ✅ OK (2026-05-21) |
| EP19 | Becze Juliánna és Szabolcs | 2025-10-29 | **2025-02-11** | ✅ OK (2026-05-21) |
| EP28 | Bencze Edit | 2025-10-28 | **2025-06-17** | ✅ OK (2026-05-21) |
| EP29 | Dr. Lőrinczi Kincső | 2025-07-18 | **2025-07-15** | ✅ OK (2026-05-21) |
| EP30 | Dr. Csala Dénes | 2025-09-09 | **2025-09-09** | OK |
| EP31 | Simon Károly & Kolumbán Sándor | 2025-10-28 | **2025-10-15** | ✅ OK (2026-05-21) |
| EP32 | Dr. Palkovics László | 2025-11-24 | **2025-11-11** | ✅ OK (2026-05-21) |
| EP33 | Dr. Charaf Hassan | 2025-11-24 | **2025-11-18** | ✅ OK (2026-05-21) |
| EP38 | Gál Ildikó | 2026-05-20 | **2026-02-17** | JAVÍTANDÓ |
| EP39 | Eberlein Éva | 2026-05-20 | **2026-03-18** | JAVÍTANDÓ |
| EP41 | Gergely István | 2026-05-20 | **2026-04-20** | JAVÍTANDÓ |
| EP42 | MMA | 2026-05-20 | **2026-05-04** | JAVÍTANDÓ |

EP01-EP07: Ellenőrizni kell, valószínűleg korrektek.

---

## 2. Hiányzó 17 epizód — Metadata

### EP12 — Bándi Domokos
- **Cím:** A Konyhai Kisegítőtől az Olimpiáig | Bándi Domokos | Navigátor Podcast EP12
- **YT ID:** e4m3NrK4lDk | **Publish date:** 2024-11-05 | **Hossz:** 1:32:13
- **Leírás:** Bándi Domokos séf a konyhai kisegítői pozícióból indulva eljutott az olimpiai kulináris versenyig Párizsban. Hogyan talált rá a szakácsszakmára, miért lett a zöldség-gyümölcs faragás erdélyi úttörője, és milyen a Taste of Transylvania csapattal a világszínpadon.

### EP13 — Józsa Levente
- **Cím:** A Podcast az Új Mainstream? | Józsa Levente | Navigátor Podcast EP13
- **YT ID:** CEBAnmXFlr8 | **Publish date:** 2024-11-19 | **Hossz:** 1:38:45
- **Leírás:** Józsa Levente a Csakabaj podcast megalkotója. Hogyan született meg a Csakabaj, miért lehet a podcast az új mainstream Erdélyben, és mit jelent hiteles tartalmat gyártani egy kis piacon. Média, közösség, hitelesség.

### EP15 — Szabó W. Péter
- **Cím:** Mit hoz az AI a mindennapjainkba? | Szabó W. Péter | Navigátor Podcast EP15
- **YT ID:** KYR2-VI3U3M | **Publish date:** 2024-12-17 | **Hossz:** 1:32:21
- **Leírás:** Szabó W. Péter (Tengr.ai alapító, ex-Flutter/PokerStars UX igazgató) a mesterséges intelligencia gyakorlati oldaláról mesél. Neurális hálók, deepfake, képgenerálás — nem sci-fi, hanem valóság.

### EP18 — Lázár Csilla & Szilágyi-Balázs Brigitta
- **Cím:** Digitális intelligencia: Az új kulcskompetencia | Lázár Csilla & Szilágyi-Balázs Brigitta | Navigátor Podcast EP18
- **YT ID:** JhquTzM8dfU | **Publish date:** 2025-01-28 | **Hossz:** 1:34:14
- **Leírás:** Nem az a kérdés, mikor adjak telefont a gyerekemnek — hanem hogy készen áll-e rá. Két szakértő 24 digitális kompetenciáról, szülői felelősségről és online biztonságról. Konkrét eszközök Székelyföldről.

### EP20 — Gábor Attila
- **Cím:** Játékból Szenvedély — Hogyan Formál a PUBG? | Gábor Attila | Navigátor Podcast EP20
- **YT ID:** 34K4pwugxLc | **Publish date:** 2025-02-25 | **Hossz:** 1:08:57
- **Leírás:** 19 éves PUBG e-sport játékos Sun Tzu stratégiai alapelveit alkalmazza a virtuális csatatéren. Hogyan fejlesztenek valós kompetenciákat a videojátékok? A Navigátor Podcast legrendhagyóbb epizódja.

### EP21 — Szakács-Paál István
- **Cím:** Indul az Audit? — Az első 4 hónap a városházán | Szakács-Paál István | Navigátor Podcast EP21
- **YT ID:** ymSgaBRwN4k | **Publish date:** 2025-03-11 | **Hossz:** 1:15:19
- **Leírás:** Székelyudvarhely polgármestere az első négy hónapjáról mesél: deficit, átvilágítás, hitelfelvétel, hivatali kultúraváltás. Milyen valójában belülről a városháza — a politikán túl.

### EP22 — Tódor Botond
- **Cím:** Hangszerjavítás vagy művészet? | Tódor Botond | Navigátor Podcast EP22
- **YT ID:** yc50GxmlMNg | **Publish date:** 2025-03-25 | **Hossz:** 1:11:51
- **Leírás:** Erdély egyetlen professzionális fúvós hangszerjavítója. Kézműves mesterség, mester-tanítvány kapcsolat, anyagismeret — és milyen az, amikor egy hiányszakma az életed munkája.

### EP23 — Hátszegi Zsolt
- **Cím:** A szavakon túl — Mit mesél rólunk a vizuális művészet? | Hátszegi Zsolt | Navigátor Podcast EP23
- **YT ID:** XrvpAIs4I3U | **Publish date:** 2025-04-08 | **Hossz:** 1:46:34
- **Leírás:** Székelyföldi animátor és egyetemi oktató a vizuális művészet dimenzióiról. Hogyan formálja az ADHD a kreativitást? Milyen az animációgyártás Kelet-Európában? Művészetek, amik szavak nélkül tanítanak.

### EP24 — Faragó Zénó & Fodor Alain Leonard
- **Cím:** A valóság színpadra állítva — A függőségről őszintén | Faragó Zénó & Fodor Alain Leonard | Navigátor Podcast EP24
- **YT ID:** X3Rhtpal5tA | **Publish date:** 2025-04-22 | **Hossz:** 1:34:30
- **Leírás:** Rendező és színész a Figurastúdióból: függőség, drogprevenció, monodráma. Az apa-hiányról, személyiség fragmentációjáról és transzcendenciáról — mélyen emberi párbeszédben.

### EP25 — Albert Orsolya
- **Cím:** Versben élni — Színpad, anyaság és költészet | Albert Orsolya | Navigátor Podcast EP25
- **YT ID:** -CBBMeGz6bI | **Publish date:** 2025-05-06 | **Hossz:** 1:44:15
- **Leírás:** Költészet, kortárs irodalom, anyaság — hogyan fér meg a színpad és a család. Fodor Ákos versei, AI és kreativitás, kulturális szervezés Székelyudvarhelyen.

### EP26 — Balázs Anna & Zoltáni Kinga
- **Cím:** Életfonal — Daganatos betegség és újjászületés | Balázs Anna & Zoltáni Kinga | Navigátor Podcast EP26
- **YT ID:** yhUxLJO5OWY | **Publish date:** 2025-05-20 | **Hossz:** 1:48:30
- **Leírás:** Két mellrák-túlélő nő a diagnózistól a gyógyulásig. Szenvedés mint ébresztő, hit mint tartóoszlop, önszeretet mint előfeltétel. A podcast egyik legmélyebb epizódja.

### EP27 — Tamás Barna atya
- **Cím:** Hit a 21. században — Ferenc pápa, XIV. Leó és Carlo Acutis | Tamás Barna atya | Navigátor Podcast EP27
- **YT ID:** RY14eU8NPU0 | **Publish date:** 2025-06-03 | **Hossz:** 1:16:29
- **Leírás:** Ferenc pápa hagyatéka, XIV. Leó pápa, Carlo Acutis szentté avatása, Fókuszpont imaest. Hit, eukarisztia, és mit jelent különlegesnek lenni egy fénymásolat-világban.

### EP34 — Süket Csaba
- **Cím:** Miért bukik el a startupok 75%-a? | Süket Csaba | Navigátor Podcast EP34
- **YT ID:** vS0SK2x1NQI | **Publish date:** 2025-12-02 | **Hossz:** 0:52:46
- **Leírás:** A kudarc a legerősebb tanítómester. Startup bukás, MVP validálás, IT vállalkozás Székelyföldön. Őszinte beszélgetés a kitartásról és a befektetés-szerzésről.

### EP35 — Láng Máté
- **Cím:** Miért veszíti el versenyképességét a helyi IT? | Láng Máté | Navigátor Podcast EP35
- **YT ID:** X1EF52Eez4o | **Publish date:** 2025-12-16 | **Hossz:** 57:45
- **Leírás:** Már nem elég olcsóbbnak lenni. IT outsourcing vészharang: értéklánc, AI szorzó, Dubai tech ökoszisztéma. Binatch Agency alapítója a startup kultúráról.

### EP36 — Both Richárd
- **Cím:** A fáradtság nem normális! | Both Richárd | Navigátor Podcast EP36
- **YT ID:** rEKsEvsYMHA | **Publish date:** 2026-01-15 | **Hossz:** 1:58:07
- **Leírás:** A csatorna legsikeresebb epizódja (18,000+ nézés). Energiaszint maximalizálás: alvás, mozgás, étrend, étrendkiegészítők. Ha folyamatosan fáradt vagy, ez neked szól.

### EP37 — Brutbányai Melinda & Elekes István
- **Cím:** Hogyan indul el a kiégés? | Brutbányai Melinda & Elekes István | Navigátor Podcast EP37
- **YT ID:** DhXUnXn3p4U | **Publish date:** 2026-02-04 | **Hossz:** 1:18:22
- **Leírás:** Évekig lehet így élni — csak nem érdemes. Kiégés felismerése, megelőzése, egyéni és szervezeti szint. 6,300+ nézés — sokakat érint.

### EP40 — Gál Ildikó
- **Cím:** A fegyelmezés nem büntetés | Gál Ildikó | Navigátor Podcast EP40
- **YT ID:** (ellenőrizni) | **Publish date:** 2026-04-10 | **Hossz:** ~1:30:00
- **Leírás:** Fegyelmezés: miért nem egyenlő a büntetéssel, hogyan neveljünk tudatosan. Gyakorlati tanácsok szülőknek az autoritárius és megengedő stílus közötti harmadik útról.

---

## 3. Instrukciók

### Dátumjavítás (Spotify for Creators)
1. https://creators.spotify.com/pod/show/navigatorpodcast/episodes
2. Epizód → Szerkesztés → Publish date → YouTube dátumra átírni → Mentés
3. Backdated epizód NEM küld push notifikációt

### Új epizód feltöltés
1. https://creators.spotify.com/pod/show/navigatorpodcast/episodes/new
2. Audio (MP3) → Title → Description → EP szám → Season 1 → Publish date (=YouTube dátum) → Publish

### Spotify show adatok
- **Show ID:** 6ONULNIDrswuqNitEAApwO
- **Dashboard:** https://creators.spotify.com/pod/show/navigatorpodcast
- **Fiók:** navigator.podc@gmail.com
