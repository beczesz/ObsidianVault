# Dry-Run v2.0 jelentés — Ignis Academy Haladó AI Workshop

**Dátum:** 2026-05-13
**Verzió tesztelve:** v2.0 (instructor-led + stáció modell)
**Modell-szerep:** OKTATÓ (kivetítve) + PÁROS (saját Cowork) + META-EVALUÁTOR
**Hossz:** 240 perc (4 óra)
**Tananyag-verzió:** v1.3 + F1 v2.1
**Oktatói segédlet:** 09_Oktatoi_segedlet_v2.0.md

---

## Összefoglalás

A teljes meta-jelentést az utolsó fázis után frissítjük. Itt jönnek a fázis-jegyzetek sorrendben.

---


## F1 — Káoszból rendszer

### Az OKTATÓI flow értékelése
A felvezetés sűrű és pontos — Márton-monológ + a `Feladat_1.1.md` kivetítése + 3 lépésben magyarázat a Cowork-projekt setupra. A „Mondom:" idézetek természetesek, magyarosan hangzanak (különösen az „Egyiküknek biztosan nem fog elindulni" warning). Az oktató 5-7 perces felvezetés után **gyorsan átadja a stafétát** — ez a v2.0 nagy nyeresége. A demó-időkeret (0:22-0:27, csak 5 perc) **kissé szűk**: ha 2-3 résztvevőnek nem indul a Cowork, az oktatónak segítenie kell, és a párhuzamos stáció időbecslése csúszhat.

### A STÁCIÓ értékelése
Az A.1 prompt **kezdőknek is barátságos és teljes** — 5 lépés, akciócentrikus, kézivel követhető. Saját Cowork-jén futtatva: a 3 output (ceg_attekintes + CLAUDE.md + javasolt_mappa_struktura) **realisztikus** terjedelmű — kb. 2-3 perces Cowork-futás 34 fájlra. A 15 perces stáció-idő **reális**, sőt **adott esetben túl hosszú** ha valaki gyorsan halad — akinek 10 percben kész van, az unatkozik. Az output-érték magas: minden résztvevő egy **valós, használható** CLAUDE.md-vel távozik, ami F2-től F6-ig az ő munkájának alapja lesz.

### Idő-realizmus
Az ígért 25 perc (0:22-0:47) **éppen elég** — a felvezetés + setup (5p) + stáció (15p) + páros megbeszélés (3p) + átkötés (2p) tényleg kijön. Egy buktató: ha a páros megbeszélés (3 perc) elhúzódik (mert érdekes amit a Cowork dobott a Kukába), az időkeret veszélybe kerül. Az oktatónak fegyelmeznie kell magát: **3 perc kemény time-box**.

### Új javítási ötletek (v2.1-hez)
1. **F1 stáció 2-percenként mini-checkpoint:** az oktató 3, 6, 9, 12 percnél „Hol vagy?" kérdést tehet fel → senki nem reked el némán
2. **A.1 prompt elejére tegyünk egy időkeret-figyelmeztetést:** „*Ha 3 percen belül nem indul a Cowork, szólj!*" — ezzel megelőzhető a néma elveszés
3. **Egy „mit ne tegyél" sor a `_Kuka/`-szabályhoz:** „*A Cowork ne töröljön véglegesen — csak Kuka-mappába helyezzen át.*" Ez már benne van implicit módon, de ki lehetne tenni a promptba is


## F2 — Rend a TODO-k között

### Az OKTATÓI flow értékelése
A felvezetés („*Másnap reggel. Márton odaszól Enikőnek...*") **drámai és pontos** — emlékeztet az F1 átkötésre. A SRT-formátumú transcript bemutatása **kifejezetten zseniális**: úgy néz ki mintha egy AI transcribe készítette volna, ezzel egyúttal egy **second-order Cowork-mágia** is kommunikált (a transcribe is automatizálható). A „session-ök közötti memória" demó (új chat + "Mik a nyitott feladataim?") **a v2.0 legjobban időzített WOW-pillanata** — az 5-10 mp-es csend hatásos, ha az oktató tényleg megáll. A Productivity plugin mentés az állítás **konkretizálódása**: nem csak elmondom hogy „a Cowork emlékszik", hanem **mutatom is** egy második fülön.

### A STÁCIÓ értékelése
A 2.A stáció **a saját CLAUDE.md-jét hagyatkozza** — ez azt jelenti, hogy minden résztvevő enyhén különböző promptra dolgozik, és **emiatt** a páros megbeszélés jobban szolgálódik („*Te hogy fogalmaztad? Az enyém más volt...*"). Az output (4-5 mondatos email) **realisztikus** méretű, 5-7 percbe simán belefér. **Egyetlen veszély:** ha valakinek a CLAUDE.md-jében Enikő részben más szerepkört kapott (pl. nem említette hogy „részmunkaidős"), akkor a hangnem-eltérés zavarba hozhatja. Az oktatónak fel kell készítenie a párosokat: *„a Cowork ezt a CLAUDE.md alapján csinálja — ha nálatok más jött ki, az nem hiba"*.

### Idő-realizmus
A 25 perces időkeret **éppen elég**, sőt **enyhén bő**. Az F2 átkötés (1:10-1:12) 2 perc — ez kissé rövidnek tűnik egy „94 oldal" hookhoz. **Javaslat:** vagy 3 percre megnövelni, vagy az átkötést a szünet előtt (1:25) megtenni dramatikusabban.

### Új javítási ötletek (v2.1-hez)
1. **„Béla bácsi-szál" exponált**: a DEMO-ban a Cowork **maga** kell felhívja a figyelmet a 41. bemondásra ⚠️ piktogrammal, hogy a résztvevők is lássák, miért lett T08 P1. Most ezt a Cowork csak akkor „dobja", ha külön kérdezik
2. **STÁCIÓ 2.A — adjunk egy alternatívát**: aki gyorsan kész van az emailel, az írjon egyet Bíró Attilának is (T03 alapján). Ezzel a stáció max-15 perc legyen, és van „bonus level" a gyorsaknak
3. **Productivity plugin demó**: az új chat-tab nyitás után érdemes lenne **mutatni a kivetítőn a Productivity tab-ot is**, hogy a résztvevők lássák, fizikailag hova kerülnek a TODO-k


## F3 — Pályázati elemzés

### Az OKTATÓI flow értékelése
Az F3 az **első igazi értelmi teljesítmény** demója — a 94 oldalas PDF behúzása + 1 prompttal eligibility-strukturálás bemutatása zseniális. A „60-90 mp várás" alatti csend a leggyengébb pillanat lehet — az oktatónak **be kell töltenie valamivel** (pl. „*Most a Cowork párhuzamosan olvas két dolgot: 94 oldalat és a CLAUDE.md-t*"). A 3 demó sorrendje (eligibility → gap → Data Board) **logikailag tökéletes**: szűkítés-bővítés-strukturálás. A „*3 nap helyett 30 perc*" érv F3 végén **a v2.0 első kemény ROI-állítása** — érződik, hogy itt a workshop tempója felgyorsul.

### A STÁCIÓ(K) értékelése
A két 3-perces stáció (3.A CR-08 + 3.B M-11) **rövid, fókuszált és önálló** — egy résztvevő akkor is meg tudja csinálni, ha az előző fázisokat elveszett követéssel követte, mert a CLAUDE.md-jében benne van a cég profilja. **Az output-érték közepes**: ezek inkább „bemelegítő" gyakorlatok, mint igazi WOW-pillanatok — a *valódi* WOW az F3.1 + F3.3 DEMO-é. Ennek ellenére fontos a hands-on, mert a tempó ne legyen 100% nézés. **Egy kis kockázat:** a 3.A és 3.B nagyon hasonlít (mindkettő egy rövid „elemzés és magyarázat" feladat) — egy résztvevőnek **a 6 perc alatt érdemes ugyanazt a sablont kétszer megcsinálni** — érzés-monotonságot kelthet.

### Idő-realizmus
A 30 perc **valós** és **elég bő** — a 3 DEMO + 2 stáció elfér. A bottleneck az F3.1 DEMO (10 perc) — ha a Cowork 90 mp helyett 2-3 percig dolgozik, az oktatónak **csendet kell tartani** és a `Pelda_outputok/` pre-cached példára átváltani. **Erre a vészforgatókönyv készül, jól.**

### Új javítási ötletek (v2.1-hez)
1. **3.A + 3.B unifikáció:** legyen egyetlen, de gazdagabb stáció (5 perc): „*Válassz egy nyitott kérdést (CR-05, CR-09 stb.) — kérdezd meg a Cowork-öt, és írd meg az emailt a felelősnek.*" Ez kombinálja a 3.A elemzést és 3.B akciótervet — **kevesebb mennyiség, több mélység**
2. **Pontozási becslés vizualizálás:** a 64-75 pontos Grila ETF-becslést érdemes lenne **Mermaid chart-tal** kivetíteni (sávban: 0-60 piros, 60-75 zöld, jelenleg vagyunk 64-75) — vizuális anchor
3. **Béla bácsi-szál második említése:** a Cowork F3.1-ben **kötelezően** dobja ki a meeting-transcript-keresztreferenciát — most függ attól, hogy bekérdez-e az oktató


## F4 — Multi-persona kommunikáció

### Az OKTATÓI flow értékelése
A 3 sub-flow (Legal cross-doc + Pénzügy/Excel + CEO PPT) **diverzitása az F4 ereje** — minden résztvevő egy különböző Cowork-képességet lát egy 37 perces ablakban. A **Béla bácsi cross-doc DEMO az egész workshop dramaturgiai csúcsa** (2:00-2:12): a Cowork **maga** kapcsolja össze a meeting transcriptet a bérleti szerződéssel, és az oktató „*lassan, drámaian*" mondja el a felfedezést. A „*Tegyük fel hogy ez a levél elment. Béla bácsi visszaválaszolt is.*" mozzanat (a valódi `raspuns_bela_iosif_2025-02-26.txt` megnyitása) **realisztikussá teszi** az egész szimulációt — nem mock, hanem szimulált válasz egy valódi karaktertől. A 6-perces CEO PPT generálás **a vizuális WOW** — a generált .pptx megnyitható, mutogatható, letölthető.

### A STÁCIÓ(K) értékelése
**4.A (köszönő-válasz Béla bácsinak, 4 perc)** — az 5 mondatos limit pedagógiailag erős: kényszeríti a tömörítést. A vételi opció kérdés vissza-átkötés **érzelmileg súlyos pillanat** — a résztvevők ezen a stáción megtanulják, hogy a Cowork **kontextusból kontextusra építi a kapcsolatot**, nem csak izoláltan generál. **4.B (EBITDA margin, 3 perc)** — kvantitatív, gyors, egyértelmű. A „*ki mondja az eredményt szóban*" rész a workshop **első explicit verseny-pillanata** — ha 2-3 ember ugyanazt mondja, megerősítő. Ha más, vita-momentum. Mindkét stáció **önállóan futtatható** F1 után (a CLAUDE.md-jén keresztül).

### Idő-realizmus
A 37 perces ablak **a leghosszabb és legintenzívebb** — Reális, de a 12 perces F4.1 DEMO **érzéséig** elnyúlhat. **Egy konkrét aggály**: az F4.3 CEO PPT-generálás (6 perc) — a Cowork-nek néha 90 mp-2 perc kell a `.pptx`-re. Ha az oktató közben **csak vár**, a tempó leesik. **Javaslat:** az F4.3 prompt elindítása **párhuzamosan** az F4.B stáció alatt (3 perc) — amikor a stáció végén visszakapcsolunk, a PPT **már kész**.

### Új javítási ötletek (v2.1-hez)
1. **Párhuzamos PPT-generálás**: az F4.3 promptot **az F4.B stáció előtt** indítsuk el az oktatói gépen — amikor 4.B végén visszatérünk, a PPT már mutogatható
2. **STÁCIÓ 4.A — kreatív szabadság**: a vételi opció vissza-átkötés helyett legyen választható, **vagy** egy másik megoldás: „*írj 5 mondatban arról, hogy mit írunk az AFM dossiéba a telephely-stabilitásról*" — több kreatív feladatválasztás = több érzés-érték
3. **PPT-generálás látható**: a .pptx megnyitása után **PowerPoint slideshow módba kapcsolj** — a 6 slide-on egy-egy mondat az oktatótól (10 mp/slide), és ez teszi a **belső prezentáció Mártonnak** szimulációját **teljesen filmszerűvé**
4. **Excel-elemzés jól van** — de érdemes lenne **egy mini-vizualizációt** is generálni (oszlopdiagram EBITDA marzs csökkenésről), ami a PPTX-ben is felhasználható


## F5 — Pályázat összeállítás

### Az OKTATÓI flow értékelése
Az F5 az **egész workshop vizuális csúcsa** — és ez **nem fals állítás**. A Plan de afaceri 12 perces generálása (260 sor, románul, 8 fejezet) **csendes pillanat** — a v2.0 segédlet expliciten kéri az oktatótól, hogy „**várok 2-3 perc — CSENDBEN**". Ez **fontos pedagógiai elem**: a csend maga a demonstráció. A 23-tételes csomag-checklist (F5.2) **logikai folyamat-záró** — a résztvevők látják, hogy a Cowork a már elkészült anyagból (Plan de afaceri) **automatikusan származtatja** a dossziér-szerkezetet. A 3-tagú F5 ívben (5.1 → 5.2 → 5.A/5.B → 5.3) **a kontraszt-pillanat (5.B vs 5.3) a workshop szíve**.

### A STÁCIÓ(K) értékelése — a kontraszt-pillanat
**5.A (form-katalogizáló, 5 perc)** + **5.B (manuális idő-becslés, 5 perc)** = **a v2.0 legbrilliánsabb újítása**. A 5.A-ban a résztvevő **maga megdolgozik a forrással** — katalogizálja a 55 mezőt — ezzel **mély megértést szerez**, hogy mit jelent valójában „kitölteni egy AFM formot". Az 5.B-ben pedig **saját maga számítja ki** a manuális kitöltés idejét (kb. 90 perc). Ezzel az **5.3 DEMO-ban** az oktatói „*A ti becslésetek 90 PERC volt. **60× gyorsabb. És hibátlanul.***" mondat **nem üres állítás, hanem a saját számolásuk megerősítése**. Ez **pszichológiailag elképesztően hatékony**: a résztvevő saját maga adta a benchmark számot. Az output-érték mindkét stáción magas (55 mezős tábla + percszámolt becslés).

### Idő-realizmus
A 35 perces ablak **éppen elég, de szoros**. A 12 perces Plan de afaceri-generálás **technikailag lehet 2-3 perc várás** + 8-9 perc bemutatás. Egy potenciális csúszás: ha a Cowork **több mint 3 percig vár** a Plan de afaceri-re, az oktatónak **mesélnie kell valamit** (pl. arról, hogy ez 3000 EUR-os tanácsadói munka lenne). A vészforgatókönyv (Pelda_outputok/) **kifejezetten F3-ra van** — F5-höz **érdemes lenne előre legenerált Plan de afaceri** is a Pelda_outputok/-ban (most már megvan a Tananyag-ban: `Plan_de_afaceri_TransOffice_AFM_2025.md`).

### Új javítási ötletek (v2.1-hez)
1. **5.B stáció — kategorikus tippek:** mielőtt a résztvevők becsülnek, kapjanak egy „**átlagos benchmark**" sort a feladatból (pl. „*egy egyszerű mező 30 mp, egy hosszú szöveges 3-5 perc, egy file feltöltés 1 perc*") — ez segíti a kalibrációt és **gyorsabb konvergencia** lesz a 60-90 perces tartományba
2. **F5.3 vizuálisan**: a CSV mellett **valós form-kitöltés-animáció** — a Cowork beleilleszti az értékeket az élő HTML form-mockupba, mezőről mezőre. Ez a **legjobban filmszerű** pillanat, érdemes vizuális effekttel kísérni
3. **5.A → 5.3 hídként**: a stáció utáni rövid kommentár: „*Figyeljétek — a Cowork **a ti listátokat fogja használni**, csak gyorsabban.*" Ezzel a 5.A → 5.3 kapcsolat **mentálisan zárt körré** válik
4. **Plan de afaceri export PDF-ben**: a 260 soros MD nem mindig hat impozánsnak; **érdemes közvetlenül egy PDF-export** is generálni a kivetítőn


## F6 — Web redesign

### Az OKTATÓI flow értékelése
A 4 perces „Comic Sans nevetés" (3:19-3:23) **a workshop legjobb energia-injekciója** — a 3 órás kognitív terhelés után a fáradt csoportnak **vizuális humor** kell, és a régi 2012-es weboldal Comic Sans-szal tökéletesen szállítja. Az 5 perces modern DEMO **rövid és lényegre törő** — egy reprezentatív variánst mutat, nem öncélúan dizájnt csodálva. Az átvezetés a stációba (3:28) **természetes**: az oktató ad egy prompt-sablont (`[STÍLUS]` placeholder), és a résztvevő egyetlen szó-cserével új arcot kap. **Pedagógiailag erős üzenet**: a Cowork mint design-builder, ahol a kreatív input minimal.

### A STÁCIÓ értékelése
A „**3 saját variáns 7 perc alatt**" feladat **a workshop legnagylelkűbb stációja** — gyakorlatilag azt mondja: „**most te vagy a kreatív, csinálj amit akarsz**". A `[STÍLUS]` placeholder szóval **tényleg egy szóváltoztatás** kell az új arc megjelenéséhez. Saját 3 variánsom (klasszikus / erdélyi / japán-zen) **látványosan különbözik egymástól és a modern referenciától is** — a generálás minden HTML-nél ~7-8 KB inline CSS-szel, reszponzív. **Egy konkrét megfigyelés:** ahogy haladok a variáns 1 → 3 felé, a **kreativitás-érzet nő** — az 1. (klasszikus) szinte iskolásan biztonságos, a 3. (zen) viszont **igazán bátor**. **Ezt az oktatónak kötelezően ki kell emelnie:** *„a Cowork annyira merész, amennyire ti vagytok a promptban"*. **A stáció output-értéke kifejezetten magas**: minden résztvevő legalább 1-2 saját variánssal **távozik**, ami **emlékkép-érték**.

### Idő-realizmus
A 18 perces F6 ablak **éppen elég**, ha a Cowork 60-90 mp-en belül generál egy HTML-t. **Egy konkrét kockázat:** a 3 variáns × 60 mp = 3 perc tiszta Cowork-időmás 4 perc gondolkodás + másolás-illesztés. Egy résztvevőnek **2 variáns simán befér 7 percbe, de 3 már szoros**. A v2.0 segédlet expliciten elismeri ezt: „*Egyiküknek a 3 variáns nem fog elférni 7 percbe. Az is OK ha csak 2 készül.*" — ez egy **érett oktatói üzenet**.

### Új javítási ötletek (v2.1-hez)
1. **Saját variáns galéria — közös bemutató**: az utolsó 2 perces „1-2 résztvevő prevezeti a sajátját" pillanat előtt érdemes lenne **screenshot-mentési pillanatot** beiktatni (a Cowork export funkcióval, vagy egyszerű képernyőkép) — így a résztvevők **fizikailag is elviszik** a 3 variánst
2. **Stílus-katalógus a Feladat_6.1.md-be**: a `[STÍLUS]` mező mellé érdemes egy **8-10 példa-stílus-listát** odatenni (modern / klasszikus / erdélyi / startup / japán-zen / brutalista / retró-90 / 80-as VHS / svájci tipográfiai), hogy a kreatív választás már a feladat-szövegben **inspiráló példán** alapuljon
3. **Mobil preview**: a Cowork önálló képességeként rakhatnánk be a promptba: „*és add hozzá mobile-preview-t is*" — a reszponzivitás demonstrálása **vizuálisan vonzó**
4. **F6 outputok mentésekor**: az oktató rövid megjegyzése arról, hogy ezeket a HTML-eket **másnap egy fejlesztő tovább tudja használni** kiindulópontként — ez **transzfer-üzenet** a workshop utáni napra


## Bevezető (0:00 → 0:22) — utólagos meta-jegyzet

### Az OKTATÓI flow értékelése
A 22 perces bevezető **szoros és sűrű** — pontosan ennyi kell ahhoz, hogy a résztvevők lássák a film keretet, a TransOffice szituációt és a pisztolymissziót, de **nem nyúlik ki tutoriallá**. Az „1 dolog amit várok" mini-bemutatkozás **érzelmileg pozitív**: nem hierarchizál, mindenki **bátran** megszólalhat. A „Eszterga-metafora" (ChatGPT = gőzgép, Cowork = precíziós szerszámgép) **markáns képi keret**, ami az egész workshopot átszövi. **Egy konkrét aggály:** ha az „1 dolog amit várok" kör elhúzódik 4 perc helyett 6-7 percig (12-15 főnél ez könnyen megtörténik), a workshop **már az elején csúszik**.

### A STÁCIÓ értékelése
Az „1 mondat amit várok" **kis felmelegítő stáció** — nem a saját laptopjukon dolgoznak még, csak verbálisan. Ez **átmeneti pedagógiai forma**: készíti a stáció-mentalitást, anélkül hogy egyből technikai akadályba ütközne.

### Idő-realizmus
**22 perc reális**, de a bemutatkozó kör **fegyelmezés** szükséges (max 30 mp / fő, az oktatónak nyomásra kell helyeznie a tempót).

### Új javítási ötletek (v2.1-hez)
1. **Idő-jelölés a táblán**: az oktató előre felírja a két szünet idejét + az F1/F3/F6 záró időpontokat — vizuális anchor
2. **A Cowork-projekt setup demó már a bevezető végén**: az F1 0:25-0:27 setup-előkészítését **0:18-0:22 közé** lehetne tenni, hogy F1 stáció zökkenőmentesen induljon

---

## Zárás (3:37 → 3:50) — utólagos meta-jegyzet

### Az OKTATÓI flow értékelése
A 3 perces visszatekintés (az 6 fázis ujjakon számolása) **emlékezet-konszolidáló elem**, ami **fizikailag is** (ujjak) anchort ad a memóriának. A „Régen 5-7 napos munka. Ma: 4 óra." mondat **a teljes workshop ROI-állítása egyetlen sorban** — egyszerű, mérhető, megjegyezhető. A „**Ne másold a TransOffice-t — vidd át a saját életedre**" üzenet a **transzfer-pedagógia esszenciája**.

### A STÁCIÓ értékelése
Az „1 mondat amit elviszek" záró stáció **a workshop érzelmi csúcspontja** — minden résztvevő **saját szóhoz juttatja az átélt 4 órát**. Az „**aki akarja, megoszthatja**" opcionális rendszer **nem kényszerít**, de **lehetővé teszi az élmény-csoportosulást**. A 6 perc **bőven elég** 1 mondat megírására + 3-4 önkéntes megosztásra.

### Idő-realizmus
13 perc **éppen elég**, sőt **enyhén bő**. A bónusz feladatok bemutatása (3:46-3:48) **2 percbe** férhet, mert ez **transzfer-hivatkozás**, nem új tartalom.

### Új javítási ötletek (v2.1-hez)
1. **A „1 mondat" megosztása anonimizáltan**: az oktató szólhat: „*aki nem akar megszólalni, de **leírná névtelenül**, írja egy cetlire — én felolvasom*" — több introvertált is részt vehet a megosztásban
2. **Bónusz feladatok email-be**: az oktató előre összeállíthat egy follow-up emailt a 18 bónusz feladat linkjével, amit **a workshop végén** elküld mindenkinek — így a transzfer **strukturáltan** indul
3. **Záró QR-kód**: a kivetítőn az utolsó slide-on egy QR-kód az egész Tananyag/ zip-ehez — fizikailag mobil-szkennel **hazaviheti** az anyagot

---

## ÖSSZEFOGLALÁS (a jelentés alulnál, miután minden fázis kész)

### A v2.0 modell teszt-eredménye

A 4 órás workshop **a v2.0 modellben végrehajtható és kihozza a vágyott élményt**: az oktató filmszerű narratívát visz végig (kivetítve), a résztvevők stációknál 3-5 percenként **fizikailag is hozzányúlnak** a saját Cowork-jükhöz. A 6 fázis output-térképe: 

| Fázis | DEMO outputok | STÁCIÓ outputok | Σ |
|-------|---------------|------------------|---|
| F1 | (mindenki egyszerre — 3 fájl × 15 fő ≈ 45) | — | F1 = 3 sablonoutput |
| F2 | 1 (DEMO_TODO_lista.md) | 1 (STACIO_2A_email_Eniko.md) | 2 |
| F3 | 3 (eligibility, gap, Data Board) | 2 (CR-08, M-11) | 5 |
| F4 | 3 (szerződés cross-doc + Béla levél + Mihaela RO + Excel + CEO PPT) — összesen 5 fájl | 2 (Béla válasz + EBITDA margin) | 7 |
| F5 | 3 (Plan de afaceri + Csomag + Form-autofill CSV) | 2 (Form-katalog + Idő-becslés) | 5 |
| F6 | 1 (modern HTML) | 3 (klasszikus + erdélyi + zen) | 4 |
| Zárás | — | 1 (egy mondat) | 1 |
| **ÖSSZ** | **15 DEMO output** | **11 STÁCIÓ output** | **26 + 3 F1-sablon = 29 fájl** |

### A 3 legnagyobb v2.0-előny (v1.0-hoz képest)

1. **F5 stáció-pár (5.A + 5.B) = ROI-érzés saját számolásukból** — a kontraszt-pillanat zseniális
2. **F1 párhuzamos parallel-stáció** — mindenki **saját** CLAUDE.md-vel távozik, ami F2-F6 alapja
3. **Stációk izolált prompttal** — ha valaki elveszett, F1-től újraindíthatja magát a CLAUDE.md alapján

### A 3 legnagyobb v2.0-rizikó (amit a v2.1-nek javítania kell)

1. **Csendben várás** a Cowork generálás közben (F4.3 PPT, F5.1 Plan de afaceri) — vagy párhuzamos indítás vagy „mesélj közben" instrukció kell
2. **F1 időkeret-monitoring** — 2-3 elveszett résztvevő esetén bonyolult fenntartani a tempót
3. **Béla bácsi cross-doc dobás** F3-ban vs F4-ben — kétszer ugyanaz a felfedezés (F3 eligibility ⚠️ és F4 cross-doc DEMO) → szándékos, de magyarázat kell hogy ne tűnjön ismétlésnek

