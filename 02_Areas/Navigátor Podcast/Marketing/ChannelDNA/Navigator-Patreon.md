---
schema: presto.channel-dna.v1
area: Navigátor Podcast
channel: patreon
display_name: Patreon — Navigátor Podcast
status: proposal
maturity: stub
version: 0.1.0
date: 2026-05-26
author: Becze Szabolcs
description: Navigátor Podcast Patreon csatorna Channel DNA — presto.channel-dna.v1 séma. INSIDER/COMMUNITY csatorna, NEM hagyományos marketing channel. Tartalmaz: loyalty-retention fókusz, patron-profil, intimate-builder-confidant tone, insider-exclusive principle, két runbook-use-case (teaser + reflection), forbidden patterns (public-tartalom ismétlés, marketing-tone, sales-y CTA). Forrás: Patreon Kampányterv 2026 (4→25 tag célkitűzés), MARKETING_ENGINE.md, Alkotmány, episode-launch.md runbook §3.5. Stub-státusz: az első Patreon poszt EP43-szal születik.
id: 559ec8e7-f0cf-43b6-b58f-482477467015
index_schema_version: 1
bdos_index: true
audience_data_source: "Részleges — Patreon Kampányterv 2026 (65 ingyenes tag, 4 fizető tag, 2026-03 baseline). Patron-specifikus demográfia, retention, engagement: TBD."
primary_language: hu
allowed_formats: [long-form-text, image, audio-clip, short-video-message]
constraints:
  max_chars:
    post_text: null
    recommended_visible: null
  max_hashtags: 0
  link_in_text: true
  note: "Patreon nem hashtag-platform. Nincs karakterlimit-kényszer — long-form text természetes."
posting_rhythm:
  recommended_cadence: "Per-epizód paired action (next-episode teaser) + ad-hoc deeper content (heti max 1)"
  optimal_day: TBD
  optimal_hours_local: TBD
  rationale: "Patreon nem algoritmikus, nincs push-notification-verseny — az optimális küldési idő a patronok szokásától függ. TBD első mérési adatokból."
publication_capabilities:
  api_available: false
  mcp_available: false
  manual_required: true
  analytics_api: false
  comment_response_api: false
  fallback_chain: [manual]
  api_note: "Patreon API nincs konfigurálva. Publikálás: manuális — patreon.com/navigatorpodcast. Analytics: Patreon Creator Dashboard manuálisan."
authentication_state:
  account_url: "patreon.com/navigatorpodcast"
  page_access_token: absent
  oauth_account: TBD
  account_status: "ACTIVE — 65 ingyenes tag, 4 fizető tag (2026-03 baseline). Tier-szerkezet: TBD (Kampányterv: Támogató+ $10/hó fókusz)."
---

# Navigator-Patreon — Channel DNA (proposal)

> **Státusz: proposal, maturity: stub.** Ez a fájl Presto-által generált javaslat. Az `active` státuszhoz emberi jóváhagyás szükséges.
>
> **Stub-jelölés:** Ez a Channel DNA a 4 channel közül a leg-stub-szerűbb. A valódi Patreon-specifikus tartalom (hangnem, formátum, frekvencia-preferencia) az első EP43 poszttal kezd kialakulni. Addig ez a fájl stratégiai keretrendszer és explicit TBD-lista.

---

## §1 — Csatorna-identitás: INSIDER/COMMUNITY channel, NEM marketing channel

A Patreon alapvetően különbözik a Navigátor többi 4 csatornájától (YouTube, Facebook, Instagram, TikTok). Ez nem fokozati különbség — ez kategoriális különbség.

| Szempont | YouTube / FB / IG / TT | Patreon |
|---|---|---|
| Közönség | Anonymus, ingyenes | Fizető patronok, nevesített insiderek |
| Lojalitás | Felépítés alatt | Már elkötelezve |
| Cél | Elérés, discovery, konverzió | Retention, mélyebb kapcsolat, érték-viszonzás |
| Dinamika | Algoritmus-vezérelt ajánlás | Közvetlen feliratkozói bázis |
| Tartalom-elvárás | Platform-natív formátum | Exclusive, behind-the-scenes, early-access |

**A Patreon NEM marketing channel.** A patronok nem marketingért fizetnek — hanem azért, hogy közelebb legyenek az alkotóhoz. Ők már döntöttek: velünk vannak. A feladat nem meggyőzni őket, hanem **megtartani és viszonozni a bizalmukat**.

**Presto szempontból:** ez a csatorna a loyalty-retention mérőszáma szerint optimalizált, nem reach vagy konverzió szerint. Egyetlen releváns metrika: **churn-ráta** (hány patron hagyja abba a fizetést).

**Kampányterv-kontextus (2026-03):** az induláskor 65 ingyenes + 4 fizető patron — a cél 25 fizető patron. A fájl ezért egyszerre írja le a fenntartandó "insidership" hangot és az azt megelőző "konverziós fázis" utáni státuszt.

---

## §2 — Patron-profil (részleges — TBD egészíti ki)

A tipikus patron a Navigátor YT-közönség legaktívabb szegmenséből kerül ki — ő már 10-20+ epizódot megnézett, visszatérő néző, és valamilyen érzelmi rezonancia (egy epizód-téma, egy vendég, vagy a házigazda hangja) arra vezette, hogy anyagilag is elköteleződjön.

| Dimenzió | Becsült profil | Forrás |
|---|---|---|
| Korosztály | 35-55 (YT core-demográfia belső aktív szegmense) | YT Analytics extrapoláció |
| Motiváció | Tartja a Navigátort életben — "belső kör" érzet | Kampányterv §3 szegmens-leírások |
| Lojalitás | Magas — tudatos döntés volt a fizetős tagság | Patreon mechanizmus |
| Churn-kockázat | Alacsony ha az exclusive érték valóban exclusive | Általános Patreon benchmark |

**Patron-portré:** Az a 45-50 éves magyar nő vagy férfi, aki a YT-on rendszeresen nézett, és egy epizód után úgy érezte: "ezt az embert meg kell tartani." Nem szükségszerűen a leggazdagabb néző — hanem a leginkább értékelő. Azt várja: Szabolcs megszólítja őt, nem a "közönségét".

> **TBD:** Patron-specifikus demográfia, átlagos patron-kor, retention baseline, upgrade-ráta (ingyenes → fizető). Forrás: Patreon Creator Dashboard.

---

## §3 — Tone: `intimate-builder-confidant`

Ez a tone radikálisan különbözik a többi csatornától. A YouTube-on `podcast-host-authoritative` — a házigazda vezet. A Patreonon a házigazda **megnyílik**.

### Default tone
`intimate-builder-confidant-hu` — az alkotó a patronokkal mint a belső körébe tartozókkal kommunikál. Első személy szigorúan. Vulnerable-honest ahol releváns. A patron nem befizető — hanem társ.

### Tone-dimenziók

| Dimenzió | Pozíció | Magyarázat |
|---|---|---|
| Formális vs. informális | 5/5 informális | Tegezés kötelező. Nincs "közönség" — csak "ti". |
| Érzelmi vs. analitikus | 4.5/5 érzelmi | A Patreonon az érzelem az elsődleges — az elemzés máshol van. A patronok a kapcsolatért fizetnek, nem az infóért. |
| Sebezhetőség | magas (ahol autentikus) | "Ezt most érzem", "nem tudom még a választ", "ezt a felvétel után gondoltam végig" — ezek a Patreon-specifikus tartalom lényege. Az Alkotmány Bátorság-alázat értéke itt a legdirektebb. |
| Tanári vs. kereső | 1/5 tanári | A Patreonon Szabolcs NEM tanít — ő oszt meg. A patron beavatott, nem tanítvány. |
| Marketing-hang | TILTOTT | A legfontosabb tone-szabály. Ha bármilyen mondat "marketing-szagú" (FOMO, CTA, subscriber-language), az disqualifying a Patreon kontextusban. |
| Humor | természetes, otthonosabb | A belső körben a humor természetesebb — de csak ha autentikus. |

### Az Alkotmány-kapcsolat

A Patreon-tartalom az Alkotmány **Bátorság-alázat** értékének legtisztább kifejeződési tere:
- Bátorság: megosztani azt, ami még nincs kész, ami bizonytalan, ami személyes
- Alázat: nem előadást tartani a patronoknak, hanem velük gondolkodni

---

## §4 — Formátum és kadencia

### Formátum-mix

| Formátum | Prioritás | Mikor |
|---|---|---|
| Long-form text | Primer | Per-epizód reflection, behind-the-scenes gondolat |
| Kép (behind-scenes fotó) | Szekunder, opcionális | Felvétel előtt/után, ha vizuálisan érdekes |
| Audio-clip | Opcionális | Vágott szegmens, amit nem kerülhet ki a publikus epizódban |
| Rövid videóüzenet | Ritka | Különleges pillanathoz (mérföldkő, köszönet, személyes szó) |

**Text-first:** A Patreon szöveg-alapú platform. A patronok olvasni jönnek, nem nézegetni. Egy jól megírt, 200-400 szavas szöveg (első személyben, konkrét részletekkel) többet ér mint bármilyen produkált tartalom.

### Kadencia

**Rendszeres:**
- Per-epizód paired action (next-episode teaser) — az episode-launch.md runbook §3.5 alapján
- Post-launch host-reflection — az epizód megjelenése után, a házigazda visszapillantása

**Ad-hoc:**
- Heti maximum 1 poszt (ennél több spam-érzetet kelt)
- Minimum: minden epizódhoz legalább 1 Patreon-poszt

**NEM szükséges:**
- Napi jelenlét — ez nem social media
- Automatizált ütemezés — minden poszt emberi döntés

---

## §5 — Tartalomstratégia és az insider-exclusive principle

### Az alap-elv (KÖTELEZŐ betartani)

**Patreonon SOHA ne legyen olyan tartalom, ami a publikus csatornákon is megvan.** Ha valami "public-able" — az nem Patreon-tartalom.

Ez nem szűkösség — hanem tisztelet. A patron azért fizet, hogy olyat kapjon, amit más nem kap. Ha ugyanazt adod, mint amit ingyen is megkap, a tagság értelme megszűnik.

### Use-case 1 — Next-episode teaser (runbook paired action)

**Mikor:** T+0 (epizód megjelenése) és a következő epizód launch-a között, valahol a középen.

**Mit tartalmaz:**
- Ki a következő vendég, és miért választottam — személyes indoklás, nem marketing
- Mit várok a felvételtől — honnan jövök bele, mi izgat
- Egy konkrét kérdés, amit fel fogok tenni, és miért fontos nekem

**Forma:** 150-300 szó, első személyben, NEM reklám. Nem "EP43 hamarosan!" — hanem "holnap reggel leülök Farkas Kingával, és ez jár a fejemben előtte..."

**Loyalty-dinamika:** A patron tudja meg először. Ez nem FOMO — ez valódi előnye a tagságnak.

### Use-case 2 — Post-launch host-reflection

**Mikor:** Az epizód megjelenése utáni 1-3 napon belül.

**Mit tartalmaz:**
- Mi maradt ki a vágásból, ami pedig fontos volt
- Amit a felvétel UTÁN gondoltam végig
- Egy pillanat a felvételből, ami engem megmozgatott — és miért

**Forma:** 200-500 szó, első személyben, személyes. Nem összefoglaló — hanem belső nézőpont.

**Miért értékes:** A publikus csatornákon a végtermék látható. A Patreonon a folyamat látható. Ez a különbség.

### Egyéb lehetséges tartalmak (TBD — iterálandó)

- Patron-visszajelzés beépítése: ha egy patron kérdést tesz fel, megválaszolni Patreon-posztban
- Epizód-előkészítési megosztás: vendég-kutató fázis, miért esett rá a választás
- Mérföldkő-köszönet: 10, 25, 50 fizető tag alkalmával — nem marketing, hanem valódi köszönet

---

## §6 — Forbidden patterns

### 1. Public-tartalom ismétlés (NEVER)
**Tiltott:** Ugyanaz a tartalom, ami YouTube-on, Facebookon vagy Instagramon megjelent — változtatás nélkül Patreonra másolva.

**Rationale:** Ez az insider-exclusive principle közvetlen megsértése. A patron azért fizet, hogy ne ugyanazt kapja. Ha igen, a churn azonnal megindulhat.

### 2. Marketing-tone
**Tiltott:** "Iratkozz fel!", "Oszd meg!", "Hagyd megjegyzésben!", "Ne maradj le!" típusú CTA-k.

**Rationale:** A patron már fizet — nincs mit konvertálni. A marketing-hang arra utal, hogy az alkotó nem érti, kivel kommunikál. Ez a bizalom rombolója.

### 3. Sales-y tartalom
**Tiltott:** Termék- vagy szolgáltatás-promóció Patreon-posztban; más platform-ra irányítás kereskedelmi szándékkal; tier-upgrade nyomás.

**Rationale:** A Patreon nem értékesítési csatorna. A patronok a kapcsolatért és az exclusive tartalomért fizetnek — nem azért, hogy hirdetési felületet kapjanak.

### 4. Cross-post automatizmus
**Tiltott:** Automatikus cross-posting más csatornáról Patreonra (pl. FB poszt → Patreon).

**Rationale:** Minden Patreon-poszt szándékos emberi döntés. Az automatizmus épp a "te szólsz hozzám" érzetet öli meg, ami a Patreon értékének alapja.

### 5. Túl gyakori posting
**Tiltott:** Napi vagy heti több poszt rendszeres ritmusban.

**Rationale:** A Patreon nem social media. Ha az alkotó naponta posztol, a patron "notification fatigue"-ot érez — és leiratkozik. Heti maximum 1 ad-hoc poszt + az epizód-paired actionök az egészséges ritmus.

### 6. Public-able tartalom
**Tiltott:** Olyan tartalom Patreonon, ami valójában nyilvánosan is közölhető lenne (pl. epizód-összefoglaló, általános gondolat, ami semmiben nem belső kör-specifikus).

**Rationale:** Ha a patron megnyitja a posztot és ugyanolyan típusú tartalmat lát, mint a nyilvános csatornákon, az exclusive tagság elveszíti az értelmét.

---

## §7 — Validated examples (TBD)

> Nincs validált Patreon-poszt-adat. Az első poszt EP43-szal születik. Ez a szekció EP43-EP45 után kitöltendő.

| Epizód | Poszt-típus | Views | Patron-reakció | Forrás |
|---|---|---|---|---|
| — | TBD | TBD | TBD | Patreon Creator Dashboard (első audit után) |

---

## §8 — Anti-examples (TBD)

> Az első 3 Patreon-poszt tapasztalata után kitöltendő. Javasolt: EP43-EP45 után retrospektív.

---

## §9 — Iteráció-history és TBD-lista

### Iteration history
- 2026-05-26 — v0.1.0 — initial stub-proposal — Presto v0.8.0, forrás: Patreon Kampányterv 2026, episode-launch.md §3.5, MARKETING_ENGINE.md, Alkotmány

### TBD / Nyitott kérdések

| # | Kérdés | Forrás hiánya | Következő lépés |
|---|---|---|---|
| TBD-01 | Jelenlegi patron-szám (2026-05 frissített állapot) | Kampányterv 2026-03-as: 4 fizető tag. Azóta változhatott. | Ellenőrizni: Patreon Creator Dashboard → Patron Manager |
| TBD-02 | Tier-szerkezet (jelenlegi Patreon tier-ek neve, ára, juttatásai) | Kampányterv csak Támogató+ $10-t említ — más tier-ek TBD | Patreon Dashboard → Membership tiers megtekintése |
| TBD-03 | Optimális posting-időpont | Nincs Patreon analytics patron-aktivitásról | Patreon Creator Dashboard → Post Insights első 3 poszt után |
| TBD-04 | Patron-retention baseline | Nincs churn-adat | Dashboard → Patron Manager → New vs. lapsed patrons |
| TBD-05 | Poszt-formátum preferencia (text vs. image vs. audio) | Nincs korábbi poszt-adat | EP43 után: text + image és text-only összehasonlítása |
| TBD-06 | Ingyenes → fizető konverziós ráta az első kampány után | 2026-03 kampány lezárult — eredmény nincs archiválva | Patreon Dashboard: ingyenes tagok száma + fizető tagok szám 2026-05-26-án |
| TBD-07 | Patron-kommunikáció csatornái (Patreon DM vs. poszt vs. email) | Nincs kialakított protokoll | Döntés: mi a preferált patron-interakciós csatorna? |

---

## §10 — Érettségi állapot és következő lépés

**Ez a Channel DNA a 4 Navigator-csatorna közül a leg-stub-szerűbb** — és ez szándékos. A Patreon insider-channel: amíg nincs valódi Patreon-poszt tapasztalat, minden "tartalom-rule" becslés.

**Az első valódi Patreon-poszt EP43 (Gyász / Farkas Kinga) indításával születik.** Addig ez a fájl a következő funkciókat tölti be:
1. Stratégiai keretrendszer: mi a Patreon szerepe a Navigátor csatorna-mixben
2. Tone-útmutató: hogyan szólj a patronokhoz (intimate-builder-confidant)
3. Forbidden patterns: mi az, ami biztosan nem működik
4. TBD-lista: mit kell mérni az első 3 poszt után

**Következő iteráció trigger:** EP43 Patreon-poszt publikálása után 7 nappal. Presto `channel view channel:patreon` + manuális Patreon Dashboard export → TBD-01–TBD-07 kitöltése.

---

*Generálta: Presto v0.8.0 — 2026-05-26 — forrás: Patreon Kampányterv 2026 (patreon.com/navigatorpodcast), episode-launch.md §3.5, MARKETING_ENGINE.md §4, A Navigátor Podcast Alkotmánya (CLAUDE.md), Navigator-YT.md §2 (demográfiai baseline). Patreon-specifikus metrikák: TBD — első audit EP43 launch után.*
