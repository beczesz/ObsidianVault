# Dry-Run meta-jelentés — Ignis Academy Haladó AI Workshop

> **Készítette:** Claude (Cowork dry-run student + meta-evaluator szerepében)
> **Dátum:** 2026-05-12
> **Verzió:** v1.0
> **Tananyag-verzió:** v1.3
> **Oktatói segédlet-verzió:** v1.0

---

## F0 — Bevezető (0:00 → 0:30)

> Nem futtattam le ténylegesen a bevezetőt (nincs élő közönség), de az oktatói segédlet alapján értékelhető.

### Mi volt WOW (potenciálisan)?
A film-metafora ("A Nap, Amikor A Káosz Rendszerré Vált") szerintem azonnal felemeli a várakozást. A "200.000 EUR pályázat 1 héten belül" pisztolymisszió-ívet ad — nem absztrakt tool-tréning, hanem **konkrét, mérhető tét**. Az "eszterga metafora" (ChatGPT = gőzgép, Cowork = precíziós szerszámgép) Szabolcs személyes hookja remek, csak akkor működik ha tényleg hisz benne.

### Mi nem ment olajosan?
A bemutatkozás-kör ("hány %-ban használod az AI-t") kényes — egy "nullás" résztvevő itt megszégyenülhet. Az oktatói segédlet vigyázza ezt, de **a 30 perces bevezető önmagában feszített** ha többen jönnek 5 percet késve. A pre-workshop checklist nagyon technikailag terhelt (Productivity + Legal plugin aktiválás, 2 Obsidian tab, MySMIS form előre nyitva) — egy átlag oktatónak ez sokk.

### Oktató/tanuló arány
**Oktató 90% / Tanuló 10%** — gyakorlatilag csak a bemutatkozás-kör a tanuló aktivitás.

### Javítási ötlet
1. A bemutatkozást **átfogalmazni:** ne "%-os AI-használat", hanem "**1 dolog amit AI-tól vársz ma**" — pozitív, nem hierarchikus.
2. A 22 perces TransOffice-bemutatást **vágni 12 percre** — a film-narratíva (káosz → rendszer → pályázat) közhelyesen elmondható **3 mondatban**. Időt nyerünk F1 elejére.
3. Pre-workshop checklist legyen **plugin-aktiválás-automatizmus** — ne kelljen 8 ☐-t végigfutni 30 perc alatt.

---

## F1 — Rend a fájlok között (0:30 → 0:55)

### Mi volt WOW?
**Tényleg 5 perc alatt össze lehet rakni egy 9 fejezetes cég-áttekintőt 34 fájlból**, **kereszthivatkozásokkal** (3 különböző ügyfél-Excel összevetése, beszállítói státusz egy mondatban kategorizálva, Kovács Ilona-mappa zaja kiszűrve). Az tényleg "hűha"-élmény hogy a `cetli_marton.txt`, `emlekezteto_marton_sajat.txt` és `cetlik.txt` **mind egyetlen probléma-listába** rendeződik súlyozva (P1-P10). A "BicoToner felmondás márc. elejéig" → ezt **manuálisan kéznél tartani** majdnem lehetetlen, de a Cowork ezt **a beszállítói szintetizált táblába** beilleszti.

A CLAUDE.md generálás a **legmélyebb** — mert ez a TÉNYLEGES "project memory" pillanat, amikor minden további session **már nem null-státuszról indul**. Ez a Cowork-specifikus képesség, amit a ChatGPT nem tud.

### Mi nem ment olajosan?
- A `.docx` fájlok többségét nem tudtam tényleges tartalom-szinten beolvasni (python-docx lassú lett volna, ill. nem volt rá idő). A `lu45pmb3.tmp` valószínűleg duplikátum egy korábbi szerződés-docx-szel, de **csak méret + típus alapján következtettem** — egy igazi tanuló itt valószínűleg megakad.
- A `meeting_marton_20241105.docx` és `meeting_marton_20250112.docx` tartalmát nem dolgoztam fel — pedig ezekben **lehet hogy nyitott TODO van**. Egy szigorúbb F1 elvárás végigolvasná őket.
- A workshop F1 csak 25 perces. **5 perc maradna a HANDS-ON-ra**, és a CLAUDE.md DEMO-ra **összesen 4 perc**. A valóságban a Cowork-válasz 1-2 perc, 1 perc maradna a magyarázatra — **túl szoros**.

### Oktató/tanuló munkaaránya
**Oktató 80% / Tanuló 20%** — a tervezett 70/30 arány kicsit lebillen, mert a HANDS-ON (5 perc, "kérdezz egy dolgot") túl rövid és nem termel kézzelfogható outputot.

### Javítási ötlet
1. **A CLAUDE.md-t a HANDS-ON-ba költöztetni** — ne az oktató generálja, hanem a résztvevők ÍRJÁK MEG közösen (3 percben). A tanulási hatás drasztikusan nő.
2. A `lu45pmb3.tmp`-szerű "csali" fájloknak **legyen kifejezett megoldás-szóláma** ("ezt a Cowork felismeri mint duplikátumot — törlésre javasolja").
3. A HANDS-ON kérdéseknek legyen **3 előre megírt példa** a Prompt Library-ben (jelenleg csak ad hoc — egy nullás résztvevő nem tudja mit kérdezzen).

---

## F2 — Rend a TODO-k között (0:55 → 1:20)

### Mi volt WOW?
A meeting transcript SRT-formátum **kifejezetten szerencsés** választás — az AI úgy dolgozza fel, mintha **valódi beszélgetés** lenne, nem szerkesztett anyag. A "3? 4? Nem tudom pontosan" mondatot **konkrét TODO-vá alakítani** (T4: "Márton — pontos járműflotta-lista") **az AI ereje láthatóvá válik**. A 18 TODO felelős+határidő+blokkolóval **2 perc alatt** kész lesz — kézzel ez **1 órás meeting-jegyzet-átírás** lenne.

A románul írt Mihaela-email **3 mondat alatt** átkapcsol nyelvet **és hangnemet** (a magyar Enikő-emailhez képest formálisabb, román üzleti stílus). Ez kézzel **csak kétnyelvű embernek** menne, és nekik is 20-30 percbe telne.

A **Productivity plugin "új session, mégis emlékszik"** pillanat valószínűleg a workshop egyik legnagyobb mentális ugrása — ChatGPT-felhasználó nem érti azonnal mit lát. Az oktatói segédlet 🔑 jól bekódolja: **"Csendben hagyni. Ne magyarázd túl."**

### Mi nem ment olajosan?
- A meeting transcript 41. bemondásában elhangzik a Béla bácsi-megjegyzés ("egy-két ingatlana eladásán"). **A workshop dramaturgiája szerint** ezt **NE** kell most kiemelni — F4-re tartogatjuk. **De**: ha az AI **most azonnal** észreveszi és kiemeli (mint nálam most), **összeomlik a meglepetés-pillanat F4-ben**. Ez nehezen kezelhető.
- A 18 TODO közül legalább 4 (T4, T5, T16, T17) **NEM** a meeting-ből származik, hanem **az F3-F4 narratíva-ívből kikövetkeztetve** kerül be. Egy "valódi" Cowork-output **kevesebb** TODO-t adna a transcript alapján — de a workshop dramaturgia ezt elvárja.
- A T8 ("Mihaela visszaküldi") **fiktív TODO**, valós cégnél nincs garancia hogy időben jön. Az élő workshop ezt **manipulálja** (előre megírt válasz-email a `04_Legal_Szerzodes/emails/mihaela_konyvelo_valasz/`-ban) — **ez kiderül a résztvevőknek hogy meg van rendezve?**
- Az "új session, kérdezz: Mik a nyitott feladataim" demo **erősen függ attól, hogy a Productivity plugin tényleg dolgozik**. Ha kicsit lassú vagy laggol, az **egész WOW elszáll**.

### Oktató/tanuló munkaaránya
**Oktató 75% / Tanuló 25%** — a HANDS-ON (új session-ben kérdezés) **tényleg** ad valódi tanuló-aktivitást, de még mindig kevés. Az e-mail-szerkesztés DEMO csak nézés.

### Javítási ötlet
1. **F2 HANDS-ON 2.0**: ne csak "kérdezz" — hanem **mindenki ÍR EGY SAJÁT TODO-T** kézzel a meeting alapján, aztán **összehasonlítja a Cowork-listával**. Az "ah, ezt is megfogalmazta!" pillanat erősebb.
2. A Béla bácsi szál **drámai erejéért**: a 2. felvonás végén az oktató **direkt mondja** "ne firtassuk most ezt a mondatot, de F4-ben látni fogjátok miért" — előre építjük a feszültséget.
3. **A "session-ök közötti memória" demo** legyen **2 új session** — nem 1. Egy chatben, egy CLAUDE.md-vel, egy plugin-nel. Kontraszt = nagyobb hatás.

---

## F3 — Pályázati elemzés (1:35 → 2:05)

### Mi volt WOW?
A **94 oldalas pályázati kiírás → 12 kritérium státusz-táblázat 65-73/100 becsléssel** valami olyan, amit kézzel **3 nap olvasással és 2 napos jogi tanácsadói review-val** lehet elérni — és **fél óra alatt** kész. A "kézzel ezt egy tanácsadó 3000 EUR-ért adná" mondás az oktatói segédletben **valós**, és a résztvevők itt **kalkulálnak** a fejükben: "ez az AI ingyen ad nekem 3000 eurós tanácsot."

A **3 minta-output cross-link** is erős: a Cowork észreveszi, hogy a bérleti szerződésben **nincs explicit stabilitás-klauza** (csak időtartam), és **ezért javasolja a declarație notarială-t** mint extra mellékletet. Ez egy "jogásztól tanult mozdulat" — és az AI **maga találja meg** a meeting transcriptből, a szerződésből és a Ghidul-kritériumból.

A Hargita megyei +5 puncte automatikus bonusz **eltalálása** ("zona deficit-ből vagytok, +5 jár") — szintén olyan részlet, amit 94 oldal megemlít **egyszer**, és kézzel könnyű elsiklani fölötte.

### Mi nem ment olajosan?
- **30 perc nagyon szoros** ehhez a fázishoz. A 3 DEMO-t + 2 HANDS-ON-t **realisztikusan 40-45 perc** lefutni; az oktatói segédlet **csúszás-tervet** ad, de a valóságban itt **mindig csúszunk**.
- A workshop F3.1 demo során a **Cowork-válaszra 60-90 mp várakozás** azzal jár, hogy az oktatónak **van mit mondania közben** — egyébként awkward csend. Az oktatói segédlet ad mondatokat ("Egy emberi tanácsadó ezt napokig csinálná..."), de **15 résztvevőnél már nem hipnotizál a hangod**.
- A 6 piros tétel közül **5 Béla bácsi vagy Mihaela kezében van** → a workshop fizikai szempontból **azt mutatja meg**, hogy az AI **az emberi kommunikációt nem helyettesíti, csak előkészíti**. **Ezt a tanulságot a Story Book/oktatói segédlet nem hangsúlyozza** — pedig az egyik legértékesebb tanulság a kkv-vezetőknek.

### Oktató/tanuló munkaaránya
**Oktató 78% / Tanuló 22%** — a 2 HANDS-ON (1 kritérium + 1 melléklet kérdezés) tényleg gyakorlatias, de **rövid**. A 25 résztvevő közül **csak 2-3-an** mutatják meg a sajátjukat — a többi csak figyel.

### Javítási ötlet
1. **A 12 kritériumot 3 csapatra osztani**: 5-5 fős csoportok, mindenki 4 kritériumot kap. **Versenyhelyzet**: "ki tudja gyorsabban kiértékelni?" Az AI-t mind a 3 csapat használja. 5 perc múlva egyesítjük. → tanuló-aktivitás **40%-ra** ugrik.
2. **A Hargita-bonusz felfedezést** ne az oktató mondja ki — **kérdezzen vissza**: "Mit szóltok, van itt valami amit megérdemlünk extra pontként?" A résztvevők egyike észreveszi → **tudásszikra**.
3. A `Pelda_outputok/` mappa **NE legyen alapból elérhető** a résztvevőknek a workshop alatt — a kíváncsi típusok beleskelődnek és csaló-jellegűnek tűnik. **Visszamoderálva, post-workshop emailben kapnák**.

---

## F4 — Multi-persona kommunikáció (2:05 → 2:40)

### Mi volt WOW?
A **Béla bácsi cross-document felfedezés** valóban a workshop egyik **legtisztább varázslat-pillanata**. A Cowork **3 fájlt** (szerződés + meeting transcript + email) **összeköti egyetlen szállá** — egy 70 éves családi ismerős "szilveszteri megjegyzéséből" pályázati red flag, majd a tisztázó email Béla bácsihoz, majd a válasz **plusz BONUSZ** (5 év stabilitás + acord proprietar a töltőpontra) **megformálódik 15 perc alatt**. Ezt **kézzel** csinálni: 1 nap papírmunka + 2 nap várakozás + 1 jogtanácsos.

A Mihaela-Excel **élő pénzügyi értelmezése** szintén erős: a Cowork **nem csak kiolvas** számokat, hanem **strukturáltan értelmez** (EBITDA marzs növekedés +0,7 pp **iparági kontextusban kifejezetten konzervatív**). A "2024 lehet hogy negatív, de 2023 elég" Plan B-narratíva **az AI-tól származott** — nem az embertől. Ez egy **jogi-pénzügyi intuíció** ami eddig csak tapasztalt tanácsadótól jött.

A 5-slide CEO PPT **valós, letölthető, prezentálható** dokumentum — nem mock-up, nem "tervezz egy slide-ot" ábránd. **38 KB**, Forest & Moss palettával (a zöld átálláshoz illik), és ténylegesen használható holnap reggel Mártonnal.

### Mi nem ment olajosan?
- **35 perc nagyon kevés** 3 sub-flow-hoz. Az 5-slide PPT generálása **több mint 5 perc** (a python-pptx-szel kb. 30 mp, de a Cowork **lassabb** valódi LLM-eval). Az oktatói segédlet 7 percet ad — **realista 12-15 perc** lenne.
- A pptx skill **több visszacsatolást** vár (extract-text, thumbnail rendering, subagent visual QA) — a 7 percbe ez **nem fér bele**. Az oktató workshop közben **nem QA-zhat** vizuálisan minden slide-on. **Élő helyzetben** valószínűleg **a workshop előtt előgenerált PPT-t** mutat be, **eltitkolva** hogy nem live generálta.
- A "Te töltöd ki ezt az 1 mezőt" MICRO HANDS-ON (slide újrahangolás) elviekben jó, **de** a python-pptx (vagy bármely tool) **nem trivial** kézzel kicsi módosításra. **Egy résztvevőnek** ez **kísértésszerűen elidegenít** — "én ezt soha nem fogom kódból PPT-zni." → **az AI az aki a kódot írja**, de **a HANDS-ON itt elveszti az élt**.
- A Béla bácsi-felfedezés **automatikus megtalálása** a meeting transcript-ből **erősen prompt-érzékeny**. Ha az oktató szólni felejt, hogy "nézd meg az összes fájlt", a Cowork **csak a szerződést olvassa** és nem találja meg a red flag-et. → **az oktatói segédlet ezt megjegyzi** (vészterv: "Cowork, nézd meg a meeting transcript-et is"), de a **drámai pillanat lerontja**, ha az oktató kell hogy "súgjon".

### Oktató/tanuló munkaaránya
**Oktató 85% / Tanuló 15%** — a legrosszabb arány a workshopban. A 3 sub-flow közül **csak a CEO PPT slide-újrahangolás** ad valódi tanuló-tevékenységet, és az is **kísértő**. A Legal + Pénzügy 100%-ban DEMO.

### Javítási ötlet
1. **A Béla bácsi-felfedezést tudatosan kérdezz-vissza** ne mondd ki: "Mit gondoltok, miért emelte ki a Cowork pont ezt a 41. mondatot?" → a résztvevő ráébred a cross-document logikára, és **nem csodálkozik**, hanem **megért**.
2. A 3 sub-flow szétbontása **3 csoportra**: 5-5 fő, ki melyiket csinálja. A 35 perc végén 3 csoport bemutatja egymásnak. **Hands-on érték 50%-ra ugrik**, oktató csak fasilitátor.
3. A CEO PPT-t **előre legenerálni** és csak **élőben módosítást** demózni — **becsületesen** elmondani: "Ezt előre megcsináltam, most csak egy slide-ot fogunk együtt javítani." A "minden élő" illúzió **nem szükséges** — az **élő módosítás** is hatásos.
4. **Eltávolítani** az F4-ből: ha 35 perc kevés és 3 sub-flow van, **vagy bővíteni 45 percre**, **vagy ledobni a CEO PPT-t** és csak emailt + Excelt mutatni.

---

## F5 — Pályázat összeállítás (2:50 → 3:25)

### Mi volt WOW?
A **konszolidáció**. A Plan de afaceri **NEM ÚJ adatokból épül** — minden szám, minden tény, minden név **az előző 4 fázisban már a kontextusban van** (F1 cégadat, F3 eligibility-score, F4 EBITDA, F4 Béla bácsi-stabilitás). A Cowork **30 mp alatt** összerakja a 8 fejezetes románul írt Plan de afaceri-t, és **a számok stimmelnek minden korábbi outputtal**. Ez az igazi "rendszerszintű AI-munka" — nem egy promptban egy fájl, hanem **5 órás munkamenet összegzése egy dokumentummá**.

A **MySMIS form-kitöltés CSV** (79 mező közül 74-et kitöltött **automatikusan**, a fent maradó 5 pedig pontosan azonosítható: CNP, CI szám, banki igazolás, és 2 olyan amit hatóságtól kérünk) — ez a "**WOW blokk**", ahogy az oktatói segédlet ígéri. Egy ember kézzel 2-3 óra alatt töltené ki — **a Cowork az F1-F4 munkából 3 perc alatt**.

A **23 tételes Dosar checklist** + a kockázat-jelölésekkel ("3. ofertă még várólistán, kompromisszum") **operatív szintű menedzsment-eszköz**, nem csak az pályázathoz, hanem **a beadás napjának vezényléséhez**. Ez ami **átvihető** a résztvevők saját munkájába (nem TransOffice-szerű cég, hanem **bármilyen pályázati / pitch / RFP beadás**).

### Mi nem ment olajosan?
- A 35 perc **megint nagyon szoros**. A Plan de afaceri élő generálása **3 perc tényleges Cowork-idő** + **5 perc bemutatás** = 8 perc minimum. A 23 tételes csomag-DEMO + Form-DEMO + 2 MICRO HANDS-ON-ra **27 perc** marad — ez ténylegesen **40 perc lenne** valós tempóban.
- A "Spot the error" MICRO HANDS-ON jó ötlet pedagógiailag, **de** előzetes hibák elhelyezése a Form-ban **akkor hatásos**, ha a tanulóknak **igazi a fókuszuk**. F5 a 3:13 → 3:23 sávban van — **a workshop 70%-án túl**, már fáradtak. Egy 25 fős csoportból **valószínűleg csak 3-4-en találják meg** a CUI elgépelést — ez **nem versenymű**, hanem inkább **frusztráció**.
- A Form-mockup HTML **nem MySMIS** — egy valós MySMIS-ben **15-20 menü-réteg** van, a CSV-import **nem natív funkció**, és **session-timeout 30 perc**. **A workshopban demózott "AI tölti ki a formot magától"** illúzió a valódi MySMIS-szel **nem reprodukálható** — kérdés, **mit közöl ez a résztvevőkkel** mikor másnap saját pályázatba próbálják.
- **A Plan B (elutasítás)** szekció **a Plan de afaceri-ban van**, **de** a workshop élményében **NEM hangsúlyozott**. Egy KKV-vezető **első kérdése** lenne: "Mi van ha elutasítanak?" A Cowork erre **most már** jó választ ad (F5.1 MICRO), de **az oktatói segédlet alig említi**.

### Oktató/tanuló munkaaránya
**Oktató 75% / Tanuló 25%** — a 2 MICRO HANDS-ON (B-terv bekezdés + Spot the error) **több** mint az előző fázisokban, **de** a "Te töltöd ki ezt az 1 mezőt" **gyenge**: valójában csak **1 mező diktálása** a Cowork-nek, a rendszer pedig kitölti — **nem az emberé a munka**.

### Javítási ötlet
1. **A "Spot the error" MICRO-t cseréld** "Hidd hogy ott vagy" gyakorlatra: minden résztvevő **saját cégnevét, saját CUI-ját, saját címét** írja át a CSV-ben, és nézi meg hogyan változik a Plan de afaceri említés-szintje. **Identitás-élmény** — sokkal erősebb, mint hibavadászat.
2. **F5 ne 35 perc, hanem 45 perc** legyen — ha kell, F6 csökkenjen 15 percre (az úgyis vizuális gyorsulhat).
3. **A Plan B (elutasítás) szekcióhoz egy külön DEMO**: "Mit csinálnánk ha most azt mondaná az AFM hogy nem? A Cowork újratervez 5 perc alatt." → mély üzleti üzenet: **az AI-támogatott munkamenet rugalmas** — nem egy adott projekthez kötődik.

---

## F6 — Web redesign (3:25 → 3:50)

### Mi volt WOW?
**A 4 variáns 4 perces egymás után produkálása** valóban **látványos** csúcspont — különösen mert **mindegyik tartalmazza a teljes AFM-narratívát**, **automatikusan integrálva** az előző fázisokból (a 2 e-vehicul, az 5,2 t CO₂/év, a 22 kW AC, a 638 000 RON költségvetés — mind ott vannak, mind helyén). Egy designer csapat **3 hetet kérne** és **8-18 000 RON-t**; itt 1 délután, < 500 RON Claude Pro előfizetés.

A Comic Sans 2012-es kontraszt **dramaturgiailag erős** — az oktatói segédlet helyesen utasítja az oktatót, hogy "hagyd hogy nevessenek". A nevetés **energiát ad a 3:25-ös fáradt csoportnak**, és a 4 modern variáns után **automatikus a "wow, ez tényleg lehetséges?" reflex**.

A saját variáns (variant_4) **a HANDS-ON szempontjából** kiemelkedő: 4-5 mondatos diktálással **drasztikusan megváltozik a hangulat** (lila-sárga energikus startup-szerű = totál más, mint az erdélyi téglavörös konzervatív). Ez a "**diktálsz, az AI értelmezi**" pillanat **mélyebb** mint az F3-as form-kitöltés.

### Mi nem ment olajosan?
- A **3 variáns 8 perc** az oktatói segédlet szerint, de **a Cowork-nek** egy 250 soros HTML generálása **30-90 mp** — 3 darab tehát **2-5 perc**, plus a magyarázat, plus a megnyitás 3 új tabban. A 8 perc **realisztikus**, de **0 ráhagyás**.
- A 4 variáns mind **inline CSS** — egy résztvevő számára aki **nem programozó**, kérdés: **hogyan szerkesztené tovább?** A workshop **csak generálást** mutat, **nem karbantartást**. → "az AI-t mindig hívnod kell ha módosítani akarsz" érzés bonyolult lehet.
- A "Modern / Klasszikus / Erdélyi" hármas **angolszász-szemüveges**, és **nem reflektál arra**, hogy a TransOffice-nek **B2B**-ben van **3 különböző tipikus ügyfele** (online-vevő startup / önkormányzat / helyi vállalkozó) — a 3 stílus elvileg ezekre szabható, de **a workshop ezt explicit nem mondja ki**.
- A 4 variánsban **mind ugyanazok az adatok** (28 ügyfél, 22 év, 5,2 t CO₂) — **ami ezekből a régi 2012-es oldalon NEM volt**. A résztvevő talán nem érzi, hogy **a Cowork az F1-F5 munkából vette ezt** — csak látja a kész oldalt. Az **integráció bemutatása** elveszhet.

### Oktató/tanuló munkaaránya
**Oktató 65% / Tanuló 35%** — a HANDS-ON itt **8 percig** tart és **mindenki saját variánst készít**. Egy résztvevő tényleg **kezdeményez**, diktál, lát. A workshop **legjobb hands-on aránya** ez a fázis.

### Javítási ötlet
1. **A 3 variánsból 2 legyen "alap"** (Modern + Erdélyi), és **az 1 (Klasszikus) a HANDS-ON**: az oktató magyarázza el a brief-et ("konzervatív B2B-iroda, intézményi ügyfelek"), és **a résztvevő-csoport** diktálja a Cowork-nek élőben. A 3. variáns így **közösen** születik, és **mindenki látja** a brief-from-spec-folyamatot.
2. **A 4 variáns után 1 perces "Melyiket választanád?"** szavazás (kézfelhúzás vagy Mentimeter) — **azonnali csoportos döntés**, ami a workshop végén "tanulság-elem" lesz.
3. **A régi Comic Sans szövegnek** legyen **explicit pointer** ("a Cowork ezt a szöveget elolvasta és a 4 új oldalon kerüli mindenhol") — ezzel kiemeled hogy az AI **nemcsak generál, hanem korrigál**.

---

## Zárás (3:50 → 4:00)

### Mi volt WOW?
A **6 fázis 1-mondatos visszatekintése** (a film mint film) **pszichológiailag erős** — a résztvevő érzi hogy "én ezt **élem át**, nem csak néztem". A **"1 mondat amit ma elviszek"** körkérdés **dialóg-momentum**: mindenki válaszol, az oktató bólint, és **a vélemények nem cserélhetőek**.

A **18 bónusz feladat** a tananyag-csomagban **post-workshop érték**: a résztvevő hazamegy egy **konkrét gyakorló-listával**, nem **általános biztatással**.

### Mi nem ment olajosan?
- A 10 perc **kevés** 25 fős csoportban — körkérdéssel 25 × 15 mp = 6,5 perc + 3,5 perc visszatekintés. Ez **mehet 12-14 percig**, ami **eltolja a 4 órás keretet**.
- A "ne kommentáld a mondatokat" instrukció **erős fegyelem** kell — egy lelkes oktató **ösztönösen** reflektálna. **A workshopban gyakorlat** szükséges hozzá.

### Oktató/tanuló munkaaránya
**Oktató 30% / Tanuló 70%** — **a legjobb arány az egész workshopban**. A zárás **a résztvevőé**, az oktató csak figyel és bólint.

### Javítási ötlet
1. A "1 mondat" **legyen anonim és írásos** (vagy Mentimeter live) → még a csendesebb résztvevők is megszólalnak.
2. A **bónusz feladatok bemutatása** legyen **2 perc, nem 1** → mindegyik fázishoz 1 mondat ("F2 bónusz: a saját meeting-jegyzeted feldolgozása"), így a résztvevő **azonnal hozzá tudja kapcsolni** az életéhez.

---


---

## Záró összefoglaló — dry-run általános benyomás

A 4 órás workshop egy **kiválóan megírt forgatókönyv**, amely **mérhető Cowork-előnyöket** mutat be **konkrét, átvihető üzleti környezetben**. A 6 fázis íve **narratíva-szintű katarzist** ad — különösen a Béla bácsi-szál cross-document felfedezése (F4) és a 4 perces 3 weboldal-variáns parádé (F6).

**A workshop legnagyobb erőssége**, hogy **NEM tool-tréning**. A résztvevő nem azt tanulja meg, hogy "hogyan kell egy promptot megírni" — hanem **megtapasztalja egy 5 napos pályázat-beadási munkamenet 4 órás kontekstusban élve**, ahol az AI **mellette dolgozik**.

**A workshop legnagyobb fejlesztendő része** a **hands-on aktivitás aránya**. Az ígért 70/20/10 valóban inkább 80/15/5, és **az 5 MUST HAVE hands-on pillanat** közül 3 (F1, F3, F5) **kérdés-szintű, nem produkciós**. **Egyszerű csoportmunka-átalakítások** (3 fős kiscsoportok, párhuzamos próbálkozások, közös output-építés) **dramatikusan emelnék** a tanulói energia-szintet és a workshop-utáni "tegnap én csináltam" érzést.

**Ár-érték:** 30 000 RON / HBC-csoport (~10-15 fő) → **5-6 fő × 1 napos pályázati tanácsadói díj** (egy ember ~3 000 EUR-t számláz egy ilyen anyagért) **kontextusában versenyképes**. A 4 órás "élmény + 18 bónusz feladat + tananyag-csomag" csomag **kreatív értéke** magas.

**Mit változtatnék mostantól?**

1. v1.1 mihamarabb (post-dry-run frissítés) — F1 HANDS-ON: közös CLAUDE.md-írás; F4: 3 csoport / 3 sub-flow; F5: identitás-élmény hibavadászat helyett; F6 megtartani modellként.
2. **Becsületes átláthatóság**: a bevezetőben mondja ki az oktató hogy "egyes válaszok és emailek a film miatt fiktívek, de a Cowork-képességek valódiak".
3. **F6 lerövidítése 15 percre**, **F4+F5-be áttéve a felszabaduló 10 percet** — egyenletesebb tempó.

**Üzletileg kész? Igen.** **Pedagógiailag kész? V1.1 után — jelenleg 80%-on.**

---

**Készült:** 2026-05-12 (dry-run szimuláció során)
**Készítette:** Claude (Cowork, student + meta-evaluator dual-role)
**Output-fájlok elérhetőek:** `TransOfficeCopy/01_ceg_attekintes/` ... `TransOfficeCopy/06_weboldal/`
**Meta-jegyzetek:** ez a fájl (jelentes.md) + pontozas.md
