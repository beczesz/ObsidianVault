---
schema: presto.channel-dna.v2
area: Navigátor Podcast
channel: youtube
display_name: YouTube — Navigátor Podcast
status: proposal
version: 0.1.0
date: 2026-05-26
author: Becze Szabolcs
description: Navigátor Podcast YouTube csatorna Channel DNA — presto.channel-dna.v2 séma. Tartalmaz: közönségdemográfia (Analytics API), PopScore/CraftScore modellek, forbidden patterns explicit rationale-lal, tone-szabályok, posting rhythm, execution capabilities. Forrás: channel.md (Analytics API 2024-05-01–2026-04-08) + patterns.md (v1.5, 39 epizód szintézis + 24 transzkript-elemzés) + Alkotmány + CLAUDE.md.
id: f9e3b7a1-2c4d-4f5e-8b6a-3d1c9e7f2b4a
index_schema_version: 1
bdos_index: true
audience_data_source: "YouTube Analytics API 2024-05-01 → 2026-04-08 (channel.md v0.1)"
primary_language: hu
allowed_formats: [long-form-video, short, community-post]
constraints:
  max_chars:
    title: 100
    description: 5000
  max_hashtags: 15
  link_in_text: true
posting_rhythm:
  recommended_cadence: "kéthetente"
  optimal_day: kedd
  optimal_hours_local: [10, 18]
  rationale: "Kedd a legerősebb nap views (585 avg) és watch time (9,307 min avg) szerint — channel.md §7."
publication_capabilities:
  api_available: false
  mcp_available: true
  manual_required: true
  analytics_api: true
  comment_response_api: true
  fallback_chain: [mcp, manual]
  api_note: "YouTube Data API v3 kvóta 0 (Google audit blokkolt, 2026-04-08 óta). Analytics API működik. Íráshoz: Chrome MCP → YouTube Studio."
authentication_state:
  analytics_api_token: present
  data_api_token: blocked
  oauth_account: "Brand Account (Navigátor Podcast) — beczesz.szabolcs@gmail.com"
---

# Navigator-YT — Channel DNA (proposal)

> **Státusz: proposal.** Ez a fájl Presto-által generált javaslat. Az `active` státuszhoz emberi jóváhagyás szükséges.

---

## §1 — Csatorna-identitás és brand-pozíció

A Navigátor Podcast YouTube csatornája **mélységre épülő, hosszú formátumú mélyinterjú-csatorna** magyarul. Nem hírcsatorna, nem tipp-lista-gyár, hanem **párbeszéd-alapú felfedezés**: a vendég és a házigazda közösen keres választ nehéz, életközeli kérdésekre.

**Mentális modell a csatornához:** Térképkészítők vagyunk egy változó világban. A néző nem tananyagot kap — hanem egy gondolkodási módszert lát működés közben.

**Brand-pozíció egyetlen mondatban:** Olyan magyar nyelvű YouTube-csatorna, ahol mélyreható párbeszéd segít eligazodni az egészség, pszichológia, család és önfejlesztés területén — 35-64 éves magyar anyanyelvű nézők számára.

**Alkotmány-gyökerek (Navigátor Podcast Alkotmánya):**
- Párbeszéd: mindkét fél nyitott és alázatos, feltételezi, hogy a másik tud valamit, amit ő nem
- Keresés: kíváncsiság és lelki szegénység a közös gondolkodás alapja
- Megújulás: hajlandóság az alázatos változásra

---

## §2 — Közönség-demográfia (forrás: channel.md, Analytics API)

### Nemek
| Nem | Arány |
|-----|-------|
| Nő | 53.1% |
| Férfi | 46.9% |

### Korosztályok
| Korosztály | Összesen | Nő | Férfi |
|------------|----------|----|-------|
| 45-54 | **33.3%** | 18.5% | 14.8% |
| 55-64 | **21.3%** | 12.9% | 8.4% |
| 35-44 | **20.7%** | 9.2% | 11.5% |
| 65+ | **14.3%** | 8.7% | 5.6% |
| 25-34 | 9.5% | 3.6% | 5.9% |
| 18-24 | 0.9% | 0.2% | 0.7% |

**35+ összesen: 89.6%** — a csatorna döntően érett felnőtt közönséget vonz.

### Geográfia
| Ország | Arány |
|--------|-------|
| Magyarország | 61.7% |
| Románia (Erdély) | 15.8% |
| Németország | 1.5% |
| Szlovákia | 1.4% |
| Ausztria | 0.8% |
| Magyar nyelvterület összesen | 81.8% |

**Erdély 15.8% — a második legnagyobb közönség.** Közéleti tartalomnál (pl. Szakács-Paál epizódok) megugrik a romániai nézettség.

### Közönség-portré (szintetizált)

A tipikus néző: 45-54 éves magyar nő, Magyarországon vagy Erdélyben él, érdekli az egészség (vércukor, fáradtság, hormonok), pszichológia (nárcizmus, kötődés, párkapcsolat), szülőség és önfejlesztés. Személyes, mély, autentikus tartalmakat keres — nem clickbait-et, nem rövid tipplistát. Hajlandó 60-120+ percet nézni, ha a tartalom megtartja.

---

## §3 — Tone és stílus

### Default tone
`podcast-host-authoritative-hu` — a házigazda vezeti a párbeszédet, határozott kérdéseket tesz fel, de nem prédikál. Szintetizál, újrafogalmaz, és hangosan gondolkodik a vendéggel együtt. Magyar köznyelv, erdélyi-magyar anyanyelvűek számára is érthető és vonzó.

### Tone-dimenziók

| Dimenzió | Pozíció | Magyarázat |
|----------|---------|------------|
| Formális vs. informális | 4/5 informális | Személyes hangnem, de nem lezser. Megszólítás: tegezés ha a vendég kéri, egyébként magázás. |
| Érzelmi vs. analitikus | 3.5/5 — mindkettő | Az érzelem kapuőr (sebezhetőség az elején), az analízis adja a mélységet. Sosem csak az egyik. |
| Tanári vs. kereső | 2/5 tanári | A házigazda kereső, nem tanár. „Nem tudom a választ" legitim állapot. |
| Inspiráló vs. pragmatikus | 3/5 — vége pragmatikus | Lezárás: mindig recept, nem tanulság. „Holnap reggel ezt csináld." |
| Humor | ritka és természetes | Nem keresett, nem forced. Ha megjön, maradhat. |

### Emoji-politika
Minimális. Leírásban: max 2-3, kizárólag struktúra-jelölésre (pl. ▶ fejezetek jelzése). Címben: SOHA.

---

## §4 — Publikáció-formátumok és struktúra

### Long-form videó (primer formátum)
- **Hossz:** 60-130 perc — a csatorna leghosszabb epizódjai a legnézettebb (patterns.md §7.2: EP14 124 perc, EP36 118 perc)
- **Cím-séma:** `"Idézet vagy tézis" – Téma | Vendég neve | EP[szám]`
- **Thumbnail:** Max 3-4 szó, provokatív vagy kérdő. Nincs shocked-face, nincs hamis feszültség.
- **Leírás:** Hook (1-2 mondat, néző problémájára mutat rá) → Kontextus (vendég, miért most) → Fejezetek/időkódok → Állandó hashtagek
- **Időkódok:** 10-12 kulcspillanat, nem mechanikus 5 perces bontás
- **Állandó hashtagek:** #NavigátorPodcast #MagyarPodcast

### Struktúra-sablonok (patterns.md §4 alapján)
1. **Mélyinterjú:** Hook → Vendég személyes sebezhetősége → Mélyülő párbeszéd → Többszintű kibontás → Gyakorlati lezárás (recept)
2. **Könyv-alapú:** Bestseller-könyv bevezetése → Szerző/vendég saját tapasztalata → Kulcsfogalmak a néző életére vetítve → „Holnap reggel kipróbálható" összefoglaló
3. **Szóló:** Házigazda → Lista-alapú struktúra (pl. „5 dolog amit megtanultam") → Közvetlen nézői megszólítás
4. **Panel (B-opció):** Két vendég → Ütköző nézőpontok → Szintézis a házigazdától

### Short (szekunder, awareness-csatorna)
- Hossz: max 60 mp
- Cél: long-form felfedezés, nem önálló tartalom
- Arány a csatornán: max 30% — a long-form marad az alap
- Megjegyzés: Shorts 17.8% views de 0.4% watch time (channel.md §6) — forgalmat hoz, de nem mélységet

### Community post
- TBD — nincs forrásadat a Navigator community-post aktivitásról

---

## §5 — Tartalomstratégia és topic-szelekcióo

### PopScore-modell (patterns.md §13 — statisztikailag validált, n=18 epizód, R²=0.947)

```
Popularity Score = (Univerzális × 0.57) + (Praktikus × 0.33) + (Mélység × 0.10)
```

**Téma-tier-ek (bizonyított teljesítmény alapján):**

| Tier | Témák | Átlag views |
|------|-------|-------------|
| S (10K+) | Pszichológia/nárcizmus, Egészség (vércukor, fáradtság), AI ha PRAKTIKUS | 23,000+ |
| A (3-10K) | Párkapcsolat/házasság, Szülőség/nevelés, Visszatérő vendég | 4,000-10,000 |
| B (1-3K) | Politika/közélet, Hit/spiritualitás, Panel formátum | 1,000-3,000 |
| C (<1K) | IT/startup (ha nem praktikus), Niche témák | <1,000 |

**Évente kötelező témák (patterns.md §2.5, §4.1):**
- Legalább 1 nárcizmus/toxikus kapcsolat epizód (Bencze Edit-effektus: EP14=72K, EP28=12.5K)
- Legalább 2-3 könyv-alapú epizód (bestseller + egészség/pszichológia kategória)

### CraftScore-modell (patterns.md §13 — R²=0.775)

```
Craft Score = (Többszintű × 0.41) + (Gyakorlati lezárás × 0.25) + (Valós adat × 0.11) + (Sebezhetőség × 0.08) + (Mélység × 0.05) + (Közös gondolkodás × 0.05) + (Érzelmi ív × 0.05)
```

**A sweet spot:** PopScore ≥ 4.0 + CraftScore ≥ 4.0 = csúcsteljesítmény (EP14, EP29, EP36).

### Forgalmi forrás-stratégia (channel.md §5 alapján)

| Forrás | Jelenlegi arány | Stratégia |
|--------|-----------------|-----------|
| Suggested/Related | 23.7% (legtöbb watch time: 2.35M perc) | Tartani — algoritmust a témaselekció táplálja |
| Subscribers/Browse | 29.8% | Tartani — push notification + kedd publikálás |
| YouTube Search | 5.1% | Növelni — SEO: cím, leírás, kulcsszavak |
| End Screen | 0.07% (252 views) | Kritikusan alacsony — Cards prioritás |
| External (Facebook) | 7.9% | Tartani — FB organic megosztás fontos |

---

## §6 — Forbidden patterns (explicit rationale-lal)

### 1. Clickbait cím
**Tiltott:** „Ezt NEM fogod elhinni!", „MINDEN megváltozott!", „Sokkolta az egész Magyarországot"

**Rationale:** A title-expectation gap azonnal roncsol. Ha a cím 10x nagyobbat ígér, mint amit a videó ad, a néző `dislike`-ol és nem tér vissza. A Navigátor közönsége 35-64 éves, tapasztalt — azonnal felismerik a manipulációt. A csatorna értéke az akkumulált bizalom, amelyet egyetlen clickbait cím hónapoknyi munkával lerombol. A hosszú-távú algoritmikus siker (Suggested Video: 2.35M perc watch time) az elégedettségi jelzőkön múlik, nem a CTR-en.

### 2. Misleading thumbnail
**Tiltott:** Fake-shocked arc, hamis kontroverzitás, vendég kimondott szavainak vizuálisan félrevezető kontextusban való megjelenítése, olyasmi szerepeltetése a thumbnail-en ami nincs a videóban.

**Rationale:** A YouTube algoritmus egyre jobban méri a satisfaction signals-t (watch time, return rate, like/dislike arány). A misleading thumbnail CTR-t optimalizál, de watch time-ot ront — ami pontosan az a metrika, amit a Navigátor csatorna maximalizál (17-26 perces átlagos nézési idő). A csatorna hosszú-távú monetizációs és növekedési alapja az algoritmikus amplifikáció (23.7% Suggested Video forgalom) — ezt misleading thumbnail közvetlen kockáztatja.

### 3. Engagement begging
**Tiltott:** „Nyomj like-ot ha egyetértesz!", „Ne felejtsd el feliratkozni!" (többszörös ismétlés), „Kapcsold be az értesítést!" (több mint egyszer per videó), bell icon emlegetése

**Rationale:** A csatorna közönsége (89.6% 35+) különösen érzékeny a nézői idő tiszteletlelenségére. A patterns.md-ben egyértelműen látszik: a legjobb epizódok (EP14, EP29, EP36) magas like/share arányukat nem CTA-val, hanem tartalom-értékkel generálják. Egy, a szabad tartalomhoz közel elhelyezett, értékmomentumhoz kötött subscribe CTA elegendő és hatékonyabb mint hat generikus megszakítás.

### 4. Kontroverzitás erőltetése
**Tiltott:** Szándékosan polarizáló framing, politikai oldalválasztás, háborús/geopolitikai heccelés, „ők vs. mi" struktúra

**Rationale:** A patterns.md §7.3 statisztikai bizonyítékkal mutatja: a kontroverzitás 5/5 score (EP16, Izrael/háború) a csatorna egyik legrosszabb teljesítményű epizódja (19% retention @30s). A Navigátor közönsége megoldásokat keres, nem konfliktust. A 4/5 kontroverzitású sikeresnek tűnő epizódok (Bencze Edit nárcizmus) valójában nem a kontroverzitásból, hanem az univerzalitásból és praktikusságból teljesítenek.

### 5. Tematikai scope-drift
**Tiltott:** Gaming, gasztronómia (önállóan), IT startup (ha nem praktikus), geopolitika (ha nem kapcsolódik 35-64 éves élethelyzethez)

**Rationale:** A patterns.md §2.4 C-tier (<1K) témái bizonyítottan nem hozzák a csatorna célközönségét. Ezek az epizódok nem csak alacsony nézettségűek — az algoritmusnál is „kártékonyak", mert összezavarják a csatorna topic-profilját, és csökkentik a Suggested Video ajánlások pontosságát.

### 6. Rövidítés a hossz rovására
**Tiltott:** Mesterséges vágás 60 perc alá „több nézőért", sebes tempó az érzelmi mélység rovására

**Rationale:** A patterns.md §7.2 megcáfolja az intuíciót: a rövid (<60 perc) epizódok átlaga 1,227 views, míg a 120+ perces epizódoké 72,238 views (n=1, de a 90-120 perces kategória is 5,806 views átlaggal vezet). A csatorna közönsége a mélységet jutalmazza — az AVD (17-20 perc) egy 100 perces epizódnál is kiemelkedő.

---

## §7 — Operacionalizált insights (channel.md + patterns.md alapján)

Ezek a tanulságok aktív állapotban vannak, hacsak a `learn retire` mód másképp nem jelöli.

| ID | Típus | Tanulság | Evidencia |
|----|-------|----------|-----------|
| INS-NAV-YT-001 | narrative-resonance | A nárcizmus/toxikus kapcsolat témakör folyamatos keresési igényt generál, visszatérő vendéggel 4x szorzó. Évente minimum egy ilyen epizód szükséges. | EP14: 72K, EP28: 12.5K — patterns.md §2.5 |
| INS-NAV-YT-002 | format-fit | A 90-130 perces hosszúság korrelál a legnagyobb nézettséggel. Rövidítés nem növeli az elérést. | patterns.md §7.2, §10 szabály 6 |
| INS-NAV-YT-003 | timing-pattern | Kedd 10:00 vagy 18:00 publikálás optimális. | channel.md §7 — kedd 585 avg views |
| INS-NAV-YT-004 | platform-amplification | Suggested Video adja a legtöbb watch time-ot (2.35M perc). Ezt az algoritmikus témaselekció (univerzalitás) táplálja, nem a thumbnail. | channel.md §5 |
| INS-NAV-YT-005 | audience-rejection | Geopolitikai/háborús tartalom 19% retention @30s → algoritmikusan bünteti a csatornát. | channel.md + patterns.md §7.3 |
| INS-NAV-YT-006 | narrative-resonance | Könyv-alapú epizód saját keresési forgalmat hoz a könyv kulcsszaváról. Csak bestseller + egészség/pszichológia kombinációval működik. | EP29 (Glükózforradalom): 62.8K — patterns.md §4.1 |
| INS-NAV-YT-007 | tone-success | Személyes sebezhetőség az első 5 percben + gyakorlati lezárás az utolsó 10 percben = legjobb craft-to-views arány. | patterns.md §11.2 |
| INS-NAV-YT-008 | cross-project-pattern | End screen-ek kritikusan alacsony hatékonyságúak (0.07% forgalom, 252 views). Cards prioritás a keresztlinkeléshez. | channel.md §5 |

---

## §8 — Plugin-skill integráció (Navigátor-specifikus)

A `/cim`, `/hook`, `/thumbnail`, `/leiras`, `/idokod` parancsok a `Navigátor Podcast` Area-specifikus promptjait hívják. Ezek nem generikus marketing skill-ek — a PopScore-modell és a csatorna-specifikus tone-szabályok alapján működnek.

| Skill/Plugin | Mire jó | Mikor hívd |
|--------------|---------|------------|
| `/hook` | Cold Open javaslatok SRT-ből | Új epizód feldolgozásakor — `draft` mód előtt |
| `/cim` | YouTube cím-variációk (cím-séma betartásával) | `draft` módban, publikáció-szintű |
| `/thumbnail` | Max 3-4 szó, provokatív, forbidden-patterns-szűrve | `prepare` módban |
| `/leiras` | SEO leírás + hashtagek a leírás-sémával | `prepare` módban |
| `/idokod` | 10-12 kulcspillanat időkódolása | `prepare` módban, SRT alapján |

**YouTube MCP integráció (pauling-ai/youtube-mcp-server):**
- Analytics: teljes hozzáférés (40+ tool Analytics API-n keresztül)
- Írás: Chrome MCP → YouTube Studio (Data API kvóta 0, 2026-04-08 óta)
- Publikálás fallback: manual → YouTube Studio böngésző-automatizálás Chrome MCP-vel

---

## §9 — Iterations history és nyitott kérdések

### Iteration history
- 2026-05-26 — v0.1.0 — initial proposal — Presto v0.8.0, per-Area Channel DNA migráció alapján

### TBD / Nyitott kérdések

| # | Kérdés | Forrás hiánya | Következő lépés |
|---|--------|---------------|-----------------|
| TBD-01 | Community post stratégia | Nincs analytics adat a Navigator community aktivitásról | Ellenőrizni YouTube Studio Community tab forgalmi adatait |
| TBD-02 | Shorts tone-szabályok | Nincs specifikus Shorts-szintű AB-teszt a csatornán | 3+ Shorts publikálás után patterns.md-stílusú elemzés |
| TBD-03 | Pontos thumbnail A/B metrikák | CTR-adatok rendelkezésre állnak, de thumbnail-variáció tesztelés nem zajlott | `youtube_analytics_overview` hívás CTR-dimenzióban, ha Data API kvóta megoldódik |
| TBD-04 | Párbeszéd-moderáció tone kommentekre | Nincs comment-reply guideline a csatornán | `comment-scan` mód első futtatása után generálni |
| TBD-05 | Erdélyi közönség-specifikus tone override | 15.8% Románia, de nincs külön elemzés a romániai nézői viselkedésről | YouTube Analytics geográfia × retention keresztelemzés |

---

## §10 — Külső skill-tudás integráció (claude-youtube cherry-picks)

> Forrás: `~/.claude/skills/youtube/` (Agrici Daniel, 14 sub-skill + 9 reference) értékelése — lásd [`youtube-skill-integration-candidates.md`](../../../../00_Prompts/BDOS/_inbox/youtube-skill-integration-candidates.md). A reference fájlok **a helyükön maradnak**; ez a szekció a Navigator-re adaptált, megtartott szabályokat rögzíti.

### §10.1 — Title ↔ Thumbnail synergy (5 szabály)

A cím és a thumbnail **NE ismételje egymást** — más-más információt hordozzanak, együtt több kíváncsiságot keltsenek, mint külön-külön:

| # | Szabály | Navigator-alkalmazás |
|---|---------|----------------------|
| 1 | **Info-split** — a cím mondja X-et, a thumbnail mutasson Y-t, átfedés nélkül | Cím = idézet/tézis + vendég + EP-szám; thumbnail = az érzelmi/tematikus mag 3-4 szóban |
| 2 | **Emotional alignment** — a cím tónusa illeszkedjen a thumbnail érzelméhez | Gyász-epizód: nem mosolygós arc; komoly, jelenlét-fókuszú portré |
| 3 | **Curiosity amplification** — együtt nagyobb gap, mint külön | „NEM KIÉGÉS, HANEM GYÁSZ" + cím-idézet = reframe-feszültség |
| 4 | **Text-overlap check** — a thumbnail-szöveg NE ismételje a cím szavait | Ha a cím tartalmazza „gyász", a thumbnail más szót emeljen ki |
| 5 | **Mobile readability** — cím + thumbnail is működjön mobil méretben | lásd §10.2 |

### §10.2 — Mobile-legibility test (168×94 px)

A thumbnail-t **168×94 px-en** (mobil feed méret) is ellenőrizni: a fókuszpont + a max 3-4 szó **kar-távolságból olvasható-e**. Ami ezen a méreten zaj, azt el kell hagyni. A Navigator közönsége 89.6% 35+ — a mobil-olvashatóság kiemelten fontos (kisebb effektív látásélesség, gyakori mobil-nézés).

### §10.3 — Reference-pointerek (on-demand olvasásra)

| Reference fájl | Mire jó | Mikor olvasd |
|---|---|---|
| `~/.claude/skills/youtube/references/thumbnail-ctr-guide.md` | CTR niche-benchmark, face psychology, A/B | thumbnail-döntés előtt |
| `~/.claude/skills/youtube/references/seo-playbook.md` | title/desc/tags/chapters + VideoObject schema | `/leiras` finomításhoz |
| `~/.claude/skills/youtube/references/algorithm-guide.md` | 3-system architecture, CTR/AVD benchmark | stratégiai döntéshez |
| `~/.claude/skills/youtube/references/analytics-guide.md` | metrics hierarchy, funnel ratios | snapshot-értelmezéshez |

### §10.4 — Plugin-skill upgrade TODO-k (v0.4, NEM aktív)

A Navigator-plugin skill-ek külön munkamenetben frissítendők (nem ebben a session-ben):
- **`/hook` v0.4** — 5-mechanizmus taxonómia (Shock/Contradiction, Problem-Agitation, Story-Open, Curiosity-Gap, Social Proof) a cold-open-generáláshoz
- **`/leiras` v0.4** — JSON-LD VideoObject schema generálás a leírás mellé
- **`/cim` v0.4** — 10-15 prioritizált tag + tag-karakterbüdzsé validátor
- **`/thumbnail` v0.4** — §10.1 synergy-check + §10.2 mobile-test beépítve

---

*Generálta: Presto v0.8.0 — 2026-05-26 — forrás: channel.md (Analytics API), patterns.md (v1.5), Alkotmány, CLAUDE.md*
*§10 hozzáadva: 2026-05-28 — claude-youtube skill-értékelés cherry-pick integráció*
