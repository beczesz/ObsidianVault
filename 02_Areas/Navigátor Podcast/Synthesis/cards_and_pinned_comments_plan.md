---
version: 1.1
date: 2026-04-09
type: cards-and-pinned-comments-plan
description: "Cards és Pinned Comment terv az összes Navigátor Podcast videóra"
total_actionable_videos: 62
id: 8c93446e-bc3a-44d3-9733-bffacb440077
index_schema_version: 1
---

# Cards & Pinned Comment Plan — Navigátor Podcast

> **Cél:** Minden publikált videón legyen min. 2 Card (tematikus cross-link) és 1 Pinned Comment (engagement + cross-promote CTA).
> **Miért:** A Cards a videó közepén a nézők 25-30%-át éri el — 2-3x hatékonyabb, mint az End Screen (10-15% long-form videóknál).
> **Végrehajtás:** Chrome MCP → YouTube Studio (Data API v3 nem elérhető, 0 kvóta).

---

## ✅ PINNED COMMENTS STATUS UPDATE (2026-04-09)

**Aktuális helyzet:**
- ✅ **ALL 62 videón:** Cross-link comments posted (100%)
- ✅ **ALL 62 videón:** Comments pinned (100%) — COMPLETED!
  - 40 videó pinned az első körben (EP14 → EP39 + Intro + 7Sz-01 + Köz-01)
  - 21 videó pinned a második körben via YouTube Studio Chrome MCP (7Sz-02→7Sz-08, KAW-01/02/04/05, Köz-02/03, Clip-05/06/07/08/09/10/15)
  - ~~1 videó (KAW-03) nem létezik — skip~~

---

## Tematikus klaszterek (Cards ajánlás logika)

| Klaszter | Videók | Cross-link logika |
|----------|--------|-------------------|
| **Pszichológia** | EP06, EP14, EP28, EP24, EP37 | Bencze Edit trilógia + kiégés + függőség |
| **Egészség** | EP29, EP36, EP37, EP08, EP26 | Vércukor → Fáradtság → Kiégés → Hematológia → Daganat |
| **AI/Tech** | EP17, EP30, EP31, EP32, EP33, EP35, EP15, EP18 | ChatGPT → Iskola → AI 80% → MI-stratégia → BME → IT verseny → MI mindennap → Digitális int. |
| **Közélet/Vezetés** | EP05, EP21, EP04, EP10, EP34 | Polgármester ↔ Audit, Vezetők, Hit+vezetés, Startup |
| **Család/Nevelés** | EP19, EP38, EP39 | Házasság ↔ Örökbefogadás ↔ Szex. nevelés |
| **Hit/Spirituális** | EP10, EP16, EP27 | Hit+vezetés → Izrael → Fókuszpont |
| **Művészet/Kultúra** | EP11, EP22, EP23, EP25 | Stílus → Hangszer → Vizuális → Vers |
| **Személyes/Kaland** | EP01, EP07, EP12, EP13, EP20 | Kávé, Ecuador, Olimpia, Podcast, PUBG |

---

## Cards pozícionálási stratégia

A Cards elhelyezése a retention-görbe alapján:

| Pozíció | Időpont | Cél |
|---------|---------|-----|
| **Card #1** | ~20-25% (retention esés előtt) | Legfontosabb cross-link — ide kerül a legerősebb ajánlás |
| **Card #2** | ~45-55% (videó közepe) | Második tematikus ajánlás |
| **Card #3** | ~70-75% (második félidő) | Playlist link VAGY harmadik ajánlás |

**Gyakorlatban (90 perces videóknál):**
- Card #1: ~18-22. perc
- Card #2: ~40-50. perc
- Card #3: ~65-70. perc

---

## Pinned Comment sablon

```
🎯 Ha ez a beszélgetés megérintett, nézd meg a [AJÁNLOTT VIDEÓ CÍME]-t is → [LINK]

[ENGAGEMENT KÉRDÉS]? 👇

⏰ Időkódok a leírásban!
📌 Iratkozz fel, hogy ne maradj le: https://www.youtube.com/@NavigatorPodcast?sub_confirmation=1
```

---

## Részletes terv — Podcast epizódok

### TOP Performers (70K+ views)

| # | EP | Views | Card #1 (20-25%) | Card #2 (45-55%) | Card #3 (70%) | Pinned Comment | Státusz |
|---|-----|------:|-----------------|-----------------|---------------|----------------|---------|
| 1 | EP14 | 72,244 | EP28 (nárc. megerősödés) | EP06 (identitáskrízis) | 🧠 Pszichológia playlist | "Ha Te is átélted ezt, nézd meg az EP28-at, ahol arról beszéltünk Edittel, hogyan gyógyulhatsz → [link]. Felismered ezeket a jeleket a környezetedben?" | ✅ Pinned |
| 2 | EP29 | 62,861 | EP36 (fáradtság) | EP37 (kiégés) | ❤️ Egészség playlist | "A 3 legfontosabb tanács ebből: 1) Étel sorrend számít 2) Reggeli szokások 3) Mozgás időzítése. Melyiket próbálsz ki először? Nézd meg az EP36-ot is → [link]" | ✅ Pinned |

### HIGH Performers (10K-25K views)

| # | EP | Views | Card #1 (20-25%) | Card #2 (45-55%) | Card #3 (70%) | Pinned Comment | Státusz |
|---|-----|------:|-----------------|-----------------|---------------|----------------|---------|
| 3 | EP17 | 20,470 | EP30 (AI + iskola) | EP31 (AI 80%) | 🤖 AI playlist | "UPDATE: Ez a beszélgetés 2024/2025 elején készült. Azóta az AI világa sokat változott! Nézd meg az EP31-et a folytatásért → [link]. Te használsz AI-t a munkádban?" | ✅ Pinned |
| 4 | EP36 | 18,394 | EP29 (vércukor) | EP37 (kiégés) | ❤️ Egészség playlist | "Ha gyakran vagy fáradt, nézd meg az EP29-et is, ahol a vércukor-szabályozásról beszéltünk → [link]. A fáradtságod melyik típusba esik?" | ✅ Pinned |
| 5 | EP28 | 12,507 | EP14 (nárcizmus felismerés) | EP06 (identitáskrízis) | 🧠 Pszichológia playlist | "Ez Bencze Edittel a 3. beszélgetésünk. Ha most láttad először, kezdd az EP14-gyel (felismerés) → [link], aztán EP06 (identitás) → [link]. Melyik rész segített a legtöbbet?" | ✅ Pinned |
| 6 | EP30 | 12,359 | EP17 (ChatGPT) | EP31 (AI 80%) | 🤖 AI playlist | "Ha érdekel az AI a gyakorlatban, nézd meg az EP17-et (ChatGPT tippek) → [link]. Szerinted az AI javítja vagy rontja az oktatást?" | ✅ Pinned |

### MID Performers (2K-10K views)

| # | EP | Views | Card #1 (20-25%) | Card #2 (45-55%) | Card #3 (70%) | Pinned Comment | Státusz |
|---|-----|------:|-----------------|-----------------|---------------|----------------|---------|
| 7 | EP19 | 6,493 | EP38 (örökbefogadás) | EP39 (szex. nevelés) | 🏠 Család playlist | "A házasságról és családról több beszélgetésünk is volt. Nézd meg az EP38-at (örökbefogadás) → [link]. Nektek mi tartja össze a házasságotokat?" | ✅ Pinned |
| 8 | EP37 | 6,367 | EP36 (fáradtság) | EP29 (vércukor) | ❤️ Egészség playlist | "Ha kiégésben vagy, a testeddel is foglalkoznod kell. Nézd meg az EP29-et (vércukor) → [link] és EP36-ot (fáradtság) → [link]. Te hogyan kezeled a kiégést?" | ✅ Pinned |
| 9 | EP06 | 4,836 | EP14 (nárcizmus) | EP28 (nárc. megerősödés) | 🧠 Pszichológia playlist | "Bencze Edittel 3 beszélgetést készítettünk. Ha tetszett, nézd meg az EP14-et (nárcizmus) → [link] — ez lett a csatornánk legnézettebb videója! Miért? Mert sokan felismerték benne magukat." | ✅ Pinned |
| 10 | EP21 | 4,231 | EP05 (polgármester) | EP34 (startup) | 💼 Vállalkozás playlist | "Ez a második beszélgetésünk Istvánnal. Az elsőt itt nézheted → [link]. Ti mit gondoltok az audit eredményéről?" | ✅ Pinned |
| 11 | EP05 | 2,758 | EP21 (audit) | EP04 (vezetők) | 💼 Vállalkozás playlist | "Szakács-Paál Istvánnal 2 beszélgetést készítettünk. A folytatás (Audit) itt → [link]. Szerintetek milyen a jó polgármester?" | ✅ Pinned |
| 12 | EP31 | 2,875 | EP17 (ChatGPT) | EP30 (AI iskola) | 🤖 AI playlist | "Ha érdekel az AI, ez a 'nagy hármas': EP17 (ChatGPT) → [link], EP30 (oktatás) → [link], és ez. Szerinted hol van az AI határa?" | ✅ Pinned |
| 13 | EP18 | 2,524 | EP17 (ChatGPT) | EP39 (szex. nevelés, fejlődő agy) | 🤖 AI playlist | "A digitális világ hatása a gyerekekre — nézd meg az EP39-et is (szexuális nevelés, fejlődő agy) → [link]. Hogyan véded a gyerekedet a digitális veszélyektől?" | ✅ Pinned |
| 14 | EP35 | 2,491 | EP17 (ChatGPT) | EP33 (BME) | 🤖 AI playlist | "Az IT versenyképességről és AI-ról többet is beszéltünk: EP17 (ChatGPT) → [link], EP33 (BME jövője) → [link]. Szerinted Magyarország lemarad?" | ✅ Pinned |
| 15 | EP39 | 2,103 | EP19 (házasság) | EP38 (örökbefogadás) | 🏠 Család playlist | "A család témája többször visszatér a csatornánkon. Nézd meg az EP19-et (házasság) → [link]. Hogyan beszéltek a gyerekeitekkel ezekről a témákról?" | ✅ Pinned |
| 16 | EP11 | 1,911 | EP14 (nárcizmus — önismeret) | EP22 (hangszer — kreativitás) | 🎨 Kultúra playlist | "A stílus nem csak a ruhákról szól, hanem az önkifejezésről. Nézd meg az EP22-t (hangszerjavítás — kreativitás) → [link]. Neked mi fejezi ki legjobban a személyiségedet?" | ✅ Pinned |
| 17 | EP15 | 1,900 | EP17 (ChatGPT) | EP31 (AI 80%) | 🤖 AI playlist | "Az MI témáról azóta többet is beszéltünk. Nézd meg az EP17-et (ChatGPT) → [link]. Te használsz AI-t a mindennapjaidban?" | ✅ Pinned |
| 18 | EP16 | 1,889 | EP10 (hit és vezetés) | EP27 (Fókuszpont) | — | "Az Izrael-élmény mélyen összefügg a hittel. Nézd meg az EP27-et (Fókuszpont, Tamás Barna atya) → [link] és EP10-et (hit és vezetés) → [link]. Jártál már Izraelben?" | ✅ Pinned |
| 19 | EP33 | 1,854 | EP35 (IT versenyképesség) | EP32 (MI-stratégia) | 🤖 AI playlist | "A BME jövőjéről és az MI-stratégiáról nézd meg az EP32-t is (Palkovics László) → [link]. Szerinted milyen irányba kellene mennie a magyar felsőoktatásnak?" | ✅ Pinned |
| 20 | EP27 | 1,797 | EP16 (Izrael) | EP10 (hit és vezetés) | — | "Tamás Barna atya gondolatai mélyen rezonáltak. Nézd meg az EP16-ot (Izrael élmény) → [link] és EP10-et (hit és vezetés) → [link]. Mi a Te fókuszpontod?" | ✅ Pinned |
| 21 | EP01 | 1,693 | EP14 (nárcizmus — #1 videó) | EP07 (Ecuador — kaland) | ☕ Személyes playlist | "Ez volt az első Navigátor epizód! Azóta 39+ beszélgetés készült. A legnépszerűbb az EP14 (nárcizmus) → [link]. Te melyik epizódot szereted a legjobban?" | ✅ Pinned |
| 22 | EP22 | 1,635 | EP23 (vizuális művészet) | EP25 (vers) | 🎨 Kultúra playlist | "A kreativitásról több beszélgetésünk is van: EP23 (vizuális művészet) → [link] és EP25 (vers) → [link]. Neked mi a kedvenc kreatív tevékenységed?" | ✅ Pinned |
| 23 | EP20 | 1,626 | EP34 (startup) | EP17 (ChatGPT) | — | "Attila története a játék szenvedélyéről szól. Ha a vállalkozás is érdekel, nézd meg az EP34-et (startup bukás) → [link]. Te mit gondolsz, lehet-e a gaming karriert építeni?" | ✅ Pinned |
| 24 | EP26 | 1,578 | EP29 (vércukor) | EP36 (fáradtság) | ❤️ Egészség playlist | "Egy rendkívül bátor beszélgetés. Ha az egészség témája érdekel, nézd meg az EP29-et (vércukor) → [link]. Mi adott erőt neked egy nehéz időszakban?" | ✅ Pinned |
| 25 | EP23 | 1,440 | EP22 (hangszer) | EP25 (vers) | 🎨 Kultúra playlist | "A vizuális művészetről és kreativitásról nézd meg az EP22-t (hangszerjavítás) → [link] is. Szerinted a művészet luxus vagy szükséglet?" | ✅ Pinned |
| 26 | EP38 | 1,258 | EP39 (szex. nevelés) | EP19 (házasság) | 🏠 Család playlist | "Ildikó története rendkívül megérintő. Ha a család témája fontos neked, nézd meg az EP19-et (házasság) → [link]. Van a környezetedben örökbefogadó család?" | ✅ Pinned |
| 27 | EP02 | 1,423 | EP14 (nárcizmus — #1 videó) | EP04 (vezetők) | — | "A törvény tudásáról és szabadságról beszéltünk. Ha az önismeret is érdekel, a legnépszerűbb videónk az EP14 (nárcizmus) → [link]. Te hogyan tanulsz a jogaidról?" | ✅ Pinned |
| 28 | EP10 | 1,144 | EP27 (Fókuszpont) | EP16 (Izrael) | — | "A hit és vezetés összekapcsolásáról nézd meg az EP27-et (Fókuszpont) → [link] is. Mi a Te hitvallásod a vezetésben?" | ✅ Pinned |
| 29 | EP03 | 1,061 | EP14 (nárcizmus — #1 videó) | EP05 (polgármester) | — | "A Hamm egy különleges történet. Ha a vállalkozás is érdekel, nézd meg az EP05-öt (polgármester) → [link]. Ismered a Hamm márkát?" | ✅ Pinned |
| 30 | EP04 | 861 | EP05 (polgármester) | EP10 (hit és vezetés) | 💼 Vállalkozás playlist | "A vezetőképzésről és felelősségről nézd meg az EP05-öt (polgármester) → [link] is. Szerinted mi kell egy jó vezetőhöz?" | ✅ Pinned |
| 31 | EP32 | 862 | EP33 (BME) | EP17 (ChatGPT) | 🤖 AI playlist | "Az MI-stratégiáról és felsőoktatásról nézd meg az EP33-at (Dr. Charaf Hassan) → [link] is. Szerinted jó irányba halad Magyarország az MI-ben?" | ✅ Pinned |
| 32 | EP12 | 889 | EP14 (nárcizmus — #1 videó) | EP07 (Ecuador) | ☕ Személyes playlist | "Az olimpiai út és a kitartás hihetetlen története. Ha a személyes történetek érdekelnek, nézd meg az EP07-et (Ecuador) → [link]. Mi volt a Te legnagyobb kihívásod?" | ✅ Pinned |
| 33 | EP08 | 778 | EP29 (vércukor) | EP26 (daganat) | ❤️ Egészség playlist | "Az orvosi hivatás és az élet törékenysége — nézd meg az EP29-et (vércukor) → [link] is. Hogyan vigyázol a saját egészségedre?" | ✅ Pinned |
| 34 | EP07 | 755 | EP12 (olimpia) | EP01 (kávé) | ☕ Személyes playlist | "Ecuador és a kaland szelleme — nézd meg az EP12-t (Olimpiai út) → [link] is. Te hol szeretnél még eljutni?" | ✅ Pinned |
| 35 | EP13 | 745 | EP17 (ChatGPT) | EP14 (nárcizmus — #1) | — | "A podcast mint médium — nézd meg az EP17-et (ChatGPT) → [link], az egyik legnépszerűbb videónkat. Szerinted a podcast mainstreamé válik?" | ✅ Pinned |
| 36 | EP09 | 612 | EP17 (ChatGPT) | EP31 (AI 80%) | 🤖 AI playlist | "Az információs korszakról nézd meg az EP17-et (ChatGPT) → [link] is, ahol a gyakorlatban mutatjuk be az AI-t. Készen állsz az info-korszakra?" | ✅ Pinned |
| 37 | EP24 | 555 | EP14 (nárcizmus) | EP37 (kiégés) | 🧠 Pszichológia playlist | "Rendkívül bátor és őszinte vallomás a függőségről. Ha az önismeret is érdekel, nézd meg az EP14-et → [link]. Ha Te vagy valakid érintett, nem vagy egyedül." | ✅ Pinned |
| 38 | EP25 | 495 | EP22 (hangszer) | EP23 (vizuális művészet) | 🎨 Kultúra playlist | "A vers és az írás ereje — nézd meg az EP22-t (hangszerjavítás) → [link] is. Neked van kedvenc versed?" | ✅ Pinned |
| 39 | EP34 | 327 | EP21 (audit) | EP05 (polgármester) | 💼 Vállalkozás playlist | "A kudarc a legjobb tanítómester — nézd meg az EP21-et (audit) → [link] is. Te hogyan kezeled a kudarcot?" | ✅ Pinned |
| 40 | Intro | 1,363 | EP14 (nárcizmus — #1) | EP01 (első epizód) | — | "Üdv a Navigátor Podcast csatornáján! Kezdd a legnépszerűbb videónkkal: EP14 (nárcizmus) → [link], vagy az első epizóddal: EP01 → [link]. Jó navigálást!" | ✅ Pinned |

---

## Részletes terv — Sorozatok

### 7 Szokás sorozat

| # | EP | Views | Card #1 | Card #2 | Card #3 | Pinned Comment | Státusz |
|---|-----|------:|---------|---------|---------|----------------|---------|
| 41 | 7Sz-01 | 1,554 | 7Sz-02 (következő rész) | EP14 (nárcizmus — csatorna #1) | — | "Ez a sorozat Stephen Covey '7 szokás' könyvét dolgozza fel. Következő rész: 7Sz-02 (Légy proaktív) → [link]. Melyik szokást tartod a legfontosabbnak?" | ✅ Pinned |
| 42 | 7Sz-02 | 960 | 7Sz-03 (következő rész) | 7Sz-01 (ha lemaradtál) | — | "Következő rész: 7Sz-03 (Tudd előre hova akarsz eljutni) → [link]. Te mennyire vagy proaktív a mindennapjaidban?" | ✅ Pinned |
| 43 | 7Sz-03 | 721 | 7Sz-04 (következő rész) | 7Sz-01 (ha lemaradtál) | — | "Következő rész: 7Sz-04 (Először a fontosat) → [link]. Neked mi a végső célod?" | ✅ Pinned |
| 44 | 7Sz-04 | 1,076 | 7Sz-05 (következő rész) | 7Sz-01 (ha lemaradtál) | — | "Következő rész: 7Sz-05 (Gondolkodj nyer-nyer) → [link]. Hogyan priorizálsz a mindennapjaidban?" | ✅ Pinned |
| 45 | 7Sz-05 | 557 | 7Sz-06 (következő rész) | 7Sz-01 (ha lemaradtál) | — | "Következő rész: 7Sz-06 (Előbb érts) → [link]. Neked sikerül nyer-nyer helyzeteket teremteni?" | ✅ Pinned |
| 46 | 7Sz-06 | 351 | 7Sz-07 (következő rész) | 7Sz-01 (ha lemaradtál) | — | "Következő rész: 7Sz-07 (Szinergia) → [link]. Mennyire hallgatod meg a másikat mielőtt válaszolsz?" | ✅ Pinned |
| 47 | 7Sz-07 | 219 | 7Sz-08 (következő rész) | 7Sz-01 (ha lemaradtál) | — | "Utolsó rész: 7Sz-08 (Élezd meg a fűrészt) → [link]. Hogyan teremtesz szinergiát a csapatodban?" | ✅ Pinned |
| 48 | 7Sz-08 | 324 | 7Sz-01 (vissza az elejére) | EP14 (nárcizmus — csatorna #1) | — | "Ez volt a sorozat utolsó része! Kezdd újra az elejéről: 7Sz-01 → [link]. Ha tetszett, a csatorna legnépszerűbb videója az EP14 → [link]. Melyik szokás változtatta meg a legjobban az életed?" | ✅ Pinned |

### KAW sorozat

| # | EP | Views | Card #1 | Card #2 | Card #3 | Pinned Comment | Státusz |
|---|-----|------:|---------|---------|---------|----------------|---------|
| 49 | KAW-01 | 326 | KAW-02 (következő) | EP10 (hit és vezetés) | — | "Következő rész: KAW-02 → [link]. Ha a hit és munka témája érdekel, nézd meg az EP10-et is → [link]." | ✅ Pinned |
| 50 | KAW-02 | 140 | KAW-04 (következő) | KAW-01 (ha lemaradtál) | — | "Következő rész: KAW-04 → [link]. Hogy kapcsolódik a hited a munkádhoz?" | ✅ Pinned |
| 51 | KAW-04 | 145 | KAW-05 (következő) | KAW-01 (ha lemaradtál) | — | "Következő rész: KAW-05 → [link]. Mit jelent számodra a munka teológiája?" | ✅ Pinned |
| 52 | KAW-05 | 84 | KAW-01 (vissza az elejére) | EP10 (hit és vezetés) | — | "Ez volt a sorozat utolsó része! Kezdd újra: KAW-01 → [link]. A spirituális vezetésről nézd meg az EP10-et is → [link]." | ✅ Pinned |

### Közösség sorozat

| # | EP | Views | Card #1 | Card #2 | Card #3 | Pinned Comment | Státusz |
|---|-----|------:|---------|---------|---------|----------------|---------|
| 53 | Köz-01 | 3,661 | Köz-02 (következő) | EP21 (audit — vezetés) | — | "Következő rész: Köz-02 (80/20 szabály) → [link]. Ha a vezetés is érdekel, nézd meg az EP21-et → [link]. Hogyan építesz közösséget?" | ✅ Pinned |
| 54 | Köz-02 | 730 | Köz-03 (következő) | Köz-01 (ha lemaradtál) | — | "Következő rész: Köz-03 (Bizalom sebessége) → [link]. Hol alkalmazod a 80/20 szabályt?" | ✅ Pinned |
| 55 | Köz-03 | 296 | Köz-01 (vissza az elejére) | EP14 (csatorna #1) | — | "Ez volt a sorozat utolsó része! Kezdd újra: Köz-01 → [link]. A csatorna legnépszerűbb videója az EP14 → [link]. Kiben bízol a legjobban?" | ✅ Pinned |

---

## Részletes terv — Clips

| # | Clip | Views | Card #1 | Pinned Comment | Státusz |
|---|------|------:|---------|----------------|---------|
| 56 | Clip-05 (Városháza) | 790 | EP05 (teljes epizód) | "Ez egy részlet! A teljes beszélgetés itt → [EP05 link]. Iratkozz fel!" | ✅ Pinned |
| 57 | Clip-06 (Identitás) | 371 | EP06 (teljes epizód) | "Ez egy részlet! A teljes beszélgetés itt → [EP06 link]. A legjobbat is nézd meg: EP14 → [link]" | ✅ Pinned |
| 58 | Clip-09 (Info korszak) | 222 | EP09 (teljes epizód) | "Ez egy részlet! A teljes beszélgetés itt → [EP09 link]." | ✅ Pinned |
| 59 | Clip-08 (Tragédia) | 92 | EP08 (teljes epizód) | "Ez egy részlet! A teljes beszélgetés itt → [EP08 link]." | ✅ Pinned |
| 60 | Clip-10 (Hit) | 88 | EP10 (teljes epizód) | "Ez egy részlet! A teljes beszélgetés itt → [EP10 link]." | ✅ Pinned |
| 61 | Clip-07 (Ecuador) | 56 | EP07 (teljes epizód) | "Ez egy részlet! A teljes beszélgetés itt → [EP07 link]." | ✅ Pinned |
| 62 | Clip-15 (MI) | 21 | EP15 (teljes epizód) | "Ez egy részlet! A teljes beszélgetés itt → [EP15 link]." | ✅ Pinned |

---

## Összesítő

| Kategória | Videók | Comments Posted | Pinned | Pin Pending | % Pinned |
|-----------|--------|-----------------|--------|------------|----------|
| TOP Performers (70K+) | 2 | 2 | 2 | 0 | 100% |
| HIGH Performers (10K+) | 4 | 4 | 4 | 0 | 100% |
| MID Performers (2K-10K) | 10 | 10 | 10 | 0 | 100% |
| Podcast (többi) | 24 | 24 | 24 | 0 | 100% |
| 7 Szokás | 8 | 8 | 8 | 0 | 100% |
| KAW | 4 | 4 | 4 | 0 | 100% |
| Közösség | 3 | 3 | 3 | 0 | 100% |
| Clips | 7 | 7 | 7 | 0 | 100% |
| **Összesen** | **62** | **62** | **62** | **0** | **100%** |

---

## Végrehajtási sorrend (prioritás)

**COMPLETED:**
1. ✅ **EP14** (72K) → EP28 + EP06 cards + pinned comment
2. ✅ **EP29** (62K) → EP36 + EP37 cards + pinned comment
3. ✅ **EP17** (20K) → EP30 + EP31 cards + pinned comment
4. ✅ **EP36** (18K) → EP29 + EP37 cards + pinned comment
5. ✅ **EP28** (12K) → EP14 + EP06 cards + pinned comment
6. ✅ **EP30** (12K) → EP17 + EP31 cards + pinned comment
[... all 40 previously pinned videos ...]

**ALL PINNED — NO PENDING ITEMS** ✅

---

## Haladás napló

| Dátum | Videók frissítve | Megjegyzés |
|-------|-----------------|------------|
| 2026-04-09 | 40/62 comments pinned | Terv elkészítve, cross-link comments posted az összes 62 videón. |
| 2026-04-09 | 62/62 comments pinned | ✅ Összes maradék 21 videó pinned via YouTube Studio Chrome MCP (7Sz-02→08, KAW-01/02/04/05, Köz-01/02/03, Clip-05/06/07/08/09/10/15). 100% COMPLETE! |
