# MVMI Azure DevOps szerzodes -- Targyalasi jegyzet

**Utolso frissites:** 2026-04-29 (v3.1 review -- valtozasok osszegzese + uj ertekeles)
**Szerzodes:** 1001686173_Azure DevOps tamogatasi szerzodes_v3.1.docx
**Felek:** MVMI Zrt. (Megrendelo) vs. Sonrisa Informatikai Kft. (Vallalkozo)
**Sonrisa oldal:** Vallalkozo (service provider)
**Alairo:** Szurdi Miklos (Sonrisa ugyvezeto)
**Review basis:** Iparagi standardok + CPS szolgaltatasi feltetelek (nincs formalis playbook)

---

## 0. V3 -> V3.1 VALTOZASOK OSSZEGZESE

A v3.1 szerzodes lenyeges javitasokat tartalmaz a v3-hoz kepest. Az alabbi tablazat osszefoglalja, melyik korabbi RED/YELLOW kerdes kapott megoldast, es melyik maradt nyitva.

### Megoldott kerdesek (v3.1-ben kezelt)

| Korabbi pont | Mi volt a problema (v3) | Mi valtozott (v3.1) | Ertekeles |
|---|---|---|---|
| **2.1 RED: Korlatatlan karterites** | Nem volt liability cap, "teljes mertekben megteriteni" | **6 honapi tenylegesen kifizetett dij cap bekerult** (14. pont, Karterites). Szandekos karokozas kivetel. Feladatkiadasi lapon elterhetnek, de csak kifejezett hivatkozassal. | **MEGOLDVA** -- elfogadhato, iparagi standard (6 havi) |
| **2.4 RED: SLA response vs resolution** | Nem volt clock stop, munkaidon kivuli bejelentesek kezeletlen | **SLA meres a kovetkezo munkanap elso orajatol indul** munkaidon kivuli ticketeknel. **Clock stop bekerult**: "az SLA meres azon idopontig tart, ameddig a Vallalkozo a hibajegyet kezeli, es az a Megrendelo reszere visszaadasra nem kerul" (1. sz. melleklet) | **NAGYRESZBEN MEGOLDVA** -- lasd megjegyzes lent |
| **Scope definicio** (nem volt korabbi pont, de fontos) | Nem volt reszletes, mely komponensekre terjed ki a tamogatas | **Reszletes scope definicio bekerult** (1. sz. melleklet, 1.b pont): Application Tier (IIS, ADO Windows Services, Search), SQL Server instance szint, reverse proxy, build/deployment agentek, identityintegracioio, monitoring. **Explicit kizaras** (1.c pont): OS szintu adminisztracio, patch management, lemez/kotet kezeles, Windows Firewall, DNS, routing, hardver, hypervisor, cloud infra reteg. | **MEGOLDVA** -- ez nagyon eros vedelem |
| **Kitoltetlen melleekletek** | MTIG alairo, adatkezelesi tajek., adatfeldolgozasi mellekletek uresek | MTIG alairo: **Bajan Gergely** (Sonrisa). Adatkezelesi tajekoztato link: Sonrisa URL. Adatfeldolgozasi 1. sz. almelleklet: **kitoltve** (szerzodeses kapcsolattartok, cegkepviselok, kozremukoedok -- nev, munkalato, munkakort, elerhetoseg). Sonrisa kapcsolattarto: **Miklos Nandor** kitoltve. | **MEGOLDVA** |
| **20 ora/ho explicit rogzites** | Csak az offer.pdf-bol kovetkezoett | **Expliciten bekerult** az 1. sz. mellekletbe: "Havonta 20 ora all rendelkezesre [...] A 20 orat meghalado munkavegzes a 7.2 pontban leirt feltetelek szerint kerul lehivasra." | **MEGOLDVA** |
| **Ponthivatkozas hiba** | 6.1/6.2 pont hivatkozas a szerzodestben helytelen volt | **Javitva** 7.1/7.2 pontra | **MEGOLDVA** |

### Meg NYITOTT kerdesek (v3.1-ben NEM kezelt)

| Pont | Problema | Kockazat | Megjegyzes |
|---|---|---|---|
| **2.2 RED: Alvallalkozo tilalom** | 12. pont: "alvallalkozot nem vesz igenybe" -- valtozatlan | MAGAS | Ha contractor (pl. E9+ Architect) dolgozik, szerzodesszeges. Dontes kell: kizarolag Sonrisa alkalmazottak, vagy targyalni kell. |
| **2.3 RED: ISO 27001 szavatossag** | 5. sz. melleklet 8.8.: "szavatol azert, hogy [...] tanusitvannyal rendelkezik" -- valtozatlan | MAGAS | Ha nincs ISO 27001, szavatossagi nyilatkozat megszegese. Ellenorizni kell. |
| **3.1 YELLOW: Unnepnapok** | Sehol nem kizarva a munkaszuneti napok -- valtozatlan | KOZEPES | 2026-ban 11 munkaszuneti nap. SLA fut-e unnepnapokon? |
| **3.3 YELLOW: Egyoldalu hosszabbitas arazo nelkul** | 10. pont: MVMI egyoldaluan dont +12 honaprol, nincs arazo -- valtozatlan | KOZEPES | 24 honapra rogzitett arak, nincs inflaciokovetes |
| **3.4 YELLOW: Kotber halmozodas** | 14.1.: tobbfele penalty halmozodhat -- valtozatlan | KOZEPES | De a 6 havi cap most mar korlatozza az ossz-kiteteltseeget |
| **3.5 YELLOW: Felmondasi jog aszimmetria** | Sonrisanak nincs rendes felmondasi jog -- valtozatlan | KOZEPES | MVMI-nek van azonnali felmondasi jog tobbfele alapon |
| **3.6 YELLOW: Teljesitesigazolas felfuggesztese** | 4. pont: MVMI felfuggesztheti a penzugyi MTIG-t -- valtozatlan | ALACSONY | Penzaramlas kockazat |
| **3.7 YELLOW: Egyoldalu mellekletmodositas** | 13. pont: MVMI egyoldaluan modosithat sablonokat -- valtozatlan | ALACSONY | IT jogosultsagi lista, Feladatkiadasi lap, MTIG sablon |
| **Hianyzik: Force Majeure** | Sem a szerzodes, sem a mellekletek nem tartalmaznak -- valtozatlan | ALACSONY | ASZF-ben lehet |
| **Hianyzik: IP jogok** | Ki a tulajdonos (scriptek, automatizaciok) -- valtozatlan | ALACSONY | |
| **Hianyzik: Biztositasi kovetelmeny** | Nem szerepel -- valtozatlan | INFORMATIV | |

### Megjegyzes az SLA clock stop-hoz

A v3.1 clock stop megoldasa jo iranyu, de nem teljesen az, amit kertunk. A javaslatunk (v3 review-ban) ez volt: "a resolution time szamlaloja szunetel, amig [...] az Uzemelteto oldali kozremukodesre, jovahagyasra var." A v3.1 szovege viszont igy fogalmaz: "az SLA meres azon idopontig tart, ameddig a Vallalkozo a hibajegyet kezeli, es az a Megrendelo reszere visszaadasra nem kerul." Ez a gyakorlatban hasonlo: ha mi visszaadjuk a ticketet az MVMI-nek (pl. "varunk az Uzemelteto jovahagyasara"), az SLA megall. De a szovegezees nem explicit a "clock stop" iraanyaban -- inkabb a ticket allapotat koveti. Elfogadhato, de az operativ folyamatban pontosan kell dokumentalni, mikor szamit "visszaadottnak" egy ticket.

### Uj ertekeles: alairhato-e a v3.1?

**Osszesitett kockazat: ELFOGADHATO, fenntartasokkal.**

A ket legfontosabb RED pont (karteritesi cap + SLA clock stop) megoldast kapott. A reszletes scope definicio (1.b-1.c pont) is nagyon eros vedelem -- pontosan definialta, miert NEM vagyunk uzemeltetok.

**Alaiiras elott meg el kell donteni:**
1. **Alvallalkozo (12. pont):** Contractor dolgozhat-e ezen a projekten? Ha igen, targyalni kell. Ha nem, biztositani kell, hogy kizarolag Sonrisa alkalmazottak legyenek.
2. **ISO 27001 (5. sz. melleklet 8.8.):** Van-e Sonrisanak ISO 27001? Ha nincs, ezt a pontot modositani kell alaiiras elott, mert szavatossagi nyilatkozat.

Ha ez a ket kerdes tisztazott, a szerzodes alairhato. A tobbi YELLOW pont (unnepnapok, arazo, kotber halmozodas, felmondas) kockkazatos, de kezelheto a napi mukodes soran.

---

## Osszefoglalo a felettesnek

Ez a dokumentum osszegyujti a szerzodes minden lenyeges pontjat, amit meg kell beszelni alairras elott. A szerzodes osszessegeben elfogadhato, de van 4 kritikus es tobb fontos pont amit targyalni kell.

---

## 1. PENZUGYI ATTEKINTES

### Szerzodesi ertek (400 Ft/EUR arfolyammal)

| Tetel                  | Ft         | EUR       | Hivatkozas | Megjegyzes |
| ---------------------- | ---------- | --------- | ---------- | ---------- |
| **Fix havidij**        | 745.000/ho | ~1.860/ho | Szerzodes 7.1. pont | Garantalt, havonta szamlazando |
| Fix havidij 12 honap   | 8.940.000  | ~22.350   | Szerzodes 7.1. pont | Minimum garantalt bevetel |
| Fix havidij 24 honap   | 17.880.000 | ~44.700   | Szerzodes 7.1. pont ("a szerzodes hatalya (24 honap) alatt osszesen") | Ha meghosszabbitjak |
| **Opcionalis keret**   | 25.220.000 | ~63.050   | Szerzodes 7.2. pont ("felhasznalasara nem vallal kotelezettsget") | NEM garantalt, teljes 24 honapra |
| **Teljes keret (max)** | 43.100.000 | ~107.750  | Szerzodes 7. pont ("legfeljebb osszesen") | 24 honapra (12+12) |

### Oradijak

| Megnevezes | Ft | EUR | CPS standard | Hivatkozas |
|------------|-----|------|-------------|------------|
| Szakertoi oradij | 14.250 | ~35,6 | 70 EUR/h | Szerzodes 7.2. pont, tablazat |
| Szakertoi napidij | 114.000 | ~285 | ~560 EUR/nap | Szerzodes 7.2. pont, tablazat |

**Fontos:** Az oradij a CPS standard feleertekenel van. A Szakmai Indoklas PDF (2026-02-05, Szurdi Miklos) szerint: Essential csomag alap araihoz kepest 3,2% havidij + 15% napidij kedvezmeny. [Forras: MVM_Sonrisa_Azure_devops_szakmai_Indoklas.pdf]

### Arrogzites es hosszabbitas -- KOCKAZAT

**Szerzodes 7.1. pont** igy fogalmaz: "A szerzodes hatalya (24 honap) alatt osszesen: 17.880.000,- Ft+AFA" -- az arak a teljes 24 honapra rogzitve vannak, valtozatlanul.

**Szerzodes 10. pont** igy fogalmaz: "A szerzodes 12 honap hatarozott idore szol, melyet kovetoen a Megrendelo opcionAlisan rendelkezhet egyoldaluan a szerzodes idotartamanak tovabbi 12 honappal torteno meghosszabbitasarol."

**Sem a tender kiirasban (AZURE DEVOPS tamogatas muszaki melleklet), sem a CPS ajanlatban (offer.pdf), sem a Szakmai Indoklasban NEM szerepel kitejezetten, hogy az arakat a hosszabbitas idoszakara is megtartjuk.** Viszont a szerzodes szovege a 24 honapra egyseges arat alkalmaz, es az MVMI egyoldaluan dont a +12 honaprol -- valtozatlan feltetelek mellett.

**Kockazat:**
- Nincs arfelulvizsgalati, indexalasi vagy inflaciokoveto klauzula a szerzodessben
- Ha a masodik evben koltsegek emelkednek, ugyanazon az aron szallitunk ami mar most a piaci ar fele
- Az MVMI egyoldaluan dont -- ha nekik megeri, meghosszabbitjak; nekunk nincs beleszolasunk

**Javasolt szoveg:**
"A szerzodes meghosszabbitasa eseten a Felek az arakat felulvizsgaljak. Amennyiben a KSH altal publikalt fogyasztoi arindex az elozo 12 honapban meghaladja az 5%-ot, a Vallalkozo jogosult az inflacio mertekenek megfelelo aremelest alkalmazni."

**Alternativ pozicio:** Ha arfelulvizsgalatot nem fogadnak el, legalabb kozos megallapodas a hosszabbitasrol az egyoldalu opcio helyett.

### Szamlazas

- Fix havidij: havonta, utolag, AFA tv. 58.§ szerint [Szerzodes 8. pont, 2. bekezdes]
- Opcionalis feladatok: teljesites utan, AFA tv. 55-56.§ szerint [Szerzodes 8. pont, 3. bekezdes]
- Szamla HUF-ban [Szerzodes 8. pont, 6. bekezdes]
- SAP teljesitesigazolas szukseges, Megrendelo cegszeruen alairt [Szerzodes 8. pont, 4. bekezdes]
- Szamla MVMI Zrt. nevere, MVM Services Zrt. postacimre kuldheto [Szerzodes 8. pont, 4. bekezdes]
- Elso tort honapban idoaranyos szamlazas lehetseges [Szerzodes 8. pont, 3. bekezdes, dolt betus resz]

---

## 2. RED -- KRITIKUS, TARGYALNI KELL

### 2.1 Korlatatlan karteritesi felelosseg

**Hivatkozas:** Szerzodes 14. pont ("Kotber - karterites"), "Karterites" alfejezet

**Szerzodes szovege (14. pont, Karterites, 4. bekezdes):**
"Amennyiben a Megrendelonek a fenti dijengedmenyen felul tovabbi kara keletkezett a Vallalkozo SLA sertesere visszavezethetoen, ugy Vallalkozo koteles a szamara felrohato okokbol szarmazo karokat teljes mertekben megteriteni."

**Szerzodes szovege (14. pont, Karterites, 1-2. bekezdes):**
A Megrendelo az SLA sertesbol eredo dijengedmenyt atharthatja a Sonrisara: "Megrendelo jogosult [...] Vallalkozotol kovet elni az igazoltan, Vallalkozo SLA sertesere visszavezetheto ok miatti elmaradt arbevetelenek (dijengedmeny) megteriteset."

**Mi a problema:**
Havi ~1.860 EUR dijert korlatatlan karteritesi felelosseg. Az MVMI nagy energetikai ceg, az o ugyfeleinek fizetett dijengedmeny akar tobb millio forint is lehet egyetlen SLA sertesbol. Nincs felso korlat (cap).

**Onellentmondas a szerzodesen belul:**
A 7. sz. melleklet ("Uzemeltetest tamogato szerzodeses kotelezettsegei"), "Felelosseg" alfejezet egyertelmuen kimondja: "Az Uzemeltetest Tamogato tevekenyse NEM minosul uzemeteltelesnek, es nem eredmenyez uzemeltetoi felelosseg- vagy hataskort-atruhaast." Es: "felelossege kizarolag az altala vallalt tamogato feladatok szerzodesszeru es szakszeru ellatasara terjed ki." A 14. pont viszont uzemeltetoi szintu felelossseget rendel hozzank.

**Enyhito tenyezo a szerzodessben (14. pont, Karterites, 3. bekezdes):**
"Vallalkozo felelossege nem terjed ki azokra a karokra, amelyek bekovetkezeseert mas felelos, amelyek kozvetlen ok-okozati viszonyban nem allnak a vallalkozoi tevekenysseggel. Vallalkozo nem felelos tovabba a vele szerzodeses kapcsolatban nem allo harmadik fel altal okozott karokert." -- Ez fontos, de nem elegseges, mert a "teljes mertekben megteriteni" felulirja.

**Javasolt szoveg:**
"A Vallalkozo osszes felelossege (kotber + karterites + dijengedmeny egyuttesen) a szerzodes elozo 12 havi netto fix dijainak osszegere korlatozott (max ~22.350 EUR / ~8.940.000 Ft). A Vallalkozo felelossege nem terjed ki az MVMI es harmadik felek kozotti szerzodeses jogviszonybol eredo kozvetettt karokra."

**Fallback pozicio:**
Ha nem fogadjak el az eves cap-et, legalabb havi cap: az adott havi fix dij 200%-a (1.490.000 Ft / ~3.720 EUR), es kozvetettt karok kizarasa.

### 2.2 Alvallalkozo tilalom

**Hivatkozas:** Szerzodes 12. pont ("Megbizasok es alvallalkozoi szerzodesek")

**Szerzodes szovege:**
"Vallalkozo kijelenti, hogy a jelen szerzodesben rogzitett feladatok elvegzesehez alvallalkozot nem vesz igenybe."

**Mi a problema:**
Ha az E9+ Architect (aki contractor) vagy barki mas nem Sonrisa-alkalmazott dolgozna ezen a projekten, az azonnali szerzodesszeges.

**Vonatkozo szankciok:**
- Szerzodes 13. pont: az alvallalkozoi rendelkezesek modositasa nem minosul szerzodesmodositasnak (MVMI egyoldaluan valtoztathat)
- ASZF (4. sz. melleklet): feltehetoen tovabbi alvallalkozoi korlatozasokat tartalmaz

**Dontes szukseges:**
- OPCIO A: Modositani a 12. pontot, hogy MVMI jovahagyassal bevonhato alvallalkozo
- OPCIO B: Biztositani, hogy kizarolag Sonrisa alkalmazottak dolgoznak (nincs contractor)

**Javasolt szoveg (ha OPCIO A):**
"Vallalkozo alvallalkozot kizarolag a Megrendelo elozetes irasbeli hozzajarulasaval vehet igenybe. Az alvallalkozoval szembeni felelosseg a Vallalkozot terheli."

### 2.3 ISO 27001 szavatossag

**Hivatkozas:** 5. sz. melleklet (Adatfeldolgozasi megallapodas), 8. fejezet ("Az adatkezeles biztonsaga"), 8. pont

**Szerzodes szovege:**
"A Megbizott kijelenti es szavatol azert, hogy az arra jogosult akkreditalt szervezet altal kiallitott (pl. ISO 9001, 27001) tanusitvannyal rendelkezik az informatikai rendszerei mukodtetesi folyamataira. A tanusitasnak tobek kozott ki kell terjednie a Megbizott adatfeldolgozoi tevekenysegere."

**Mi a problema:**
Ha a Sonrisanak nincs ISO 27001 tanusitvaanya, ez szavatossagi nyilatkozat megszegese. GDPR kontextusban sulyos kovetkezmenyei lehetnek. Ez egy konkret, igazolhato teny -- vagy van tanusitvany, vagy nincs.

**Vonatkozo felelosseg:** 5. sz. melleklet, 5. fejezet, 5.1-5.2. pont: "A Megbizott felelos az adatfeldolgozasi tevekenyseg kereteben vegzett valamennyi muvelet szakszeru [...] vegrehajtasaert."

**Dontes szukseges:**
- Van-e Sonrisanak ISO 27001? Ha igen: ok, GREEN
- Ha nincs: ezt a pontot el kell tavolitani vagy modositani ("Vallalkozo vallalja, hogy a szerzodes hateidejen belul megkezdi az ISO 27001 tanusitasi folyamatot" VAGY "Vallalkozo az iparagi best practice-nek megfelelo biztonsagi intezkedeseket alkalmaz")

### 2.4 SLA definicio -- response vs. resolution

**Hivatkozas:** 1. sz. melleklet ("Muszaki tartalom, SLA"), SLA tabla

**Szerzodes szovege (SLA tabla fejlece):**
"Problema elharitas megkezdese es befejezese a bejelentestol szamitva"

**SLA ertekek az 1. sz. melleklet tablazatabol:**

| Prioritas | SLA | Meresi idoszak | Hivatkozas |
|-----------|-----|----------------|------------|
| Kritikus | 8 munkaora | 5x11 (7:00-18:00) | 1. sz. melleklet, SLA tabla, 1. sor |
| Magas | 16 munkaora | 5x11 (7:00-18:00) | 1. sz. melleklet, SLA tabla, 2. sor |
| Normal | 4 munkanap | 5x11 (7:00-18:00) | 1. sz. melleklet, SLA tabla, 3. sor |
| Alacsony | 60 munkanap | 5x11 (7:00-18:00) | 1. sz. melleklet, SLA tabla, 4. sor |

**Mi a problema:**
Az "elharitas megkezdese es befejezese" NEM response time, hanem teljes resolution time. A Kritikus 8 munkaora azt jelenti, hogy 8 oran belul meg kell KEZDENI es BE kell FEJEZNI a javitast. Ez az iparagi standardtol (ITIL) elter, ahol a response time es resolution time kulon metrika.

**Tovabbi SLA kockazatok:**
- Nincs "clock stop" mechanizmus -- az SLA ora nem all meg, ha az Uzemeltetore varunk
- A 7. sz. melleklet, "Onallo intezkedesek tilalma" alfejezet szerint onalloan nem hajthatunk vegre valtoztatast, mindig kell az Uzemelteto
- Ha mi 2 ora alatt diagnosztizalunk, de az Uzemelteto 6 oraig nem reagal, mi sertunk SLA-t
- Az 1. sz. melleklet, "Egyuttmukodes modja" resz: "Az MVMI a munkavegzes soran fenntartja a jogot, hogy barmely feladat elvegzeset sajat eroforrassal valositsa meg" -- tehat az MVMI barmikor atveheti a feladatot, de az SLA orank fut

**Javasolt szoveg -- SLA szetvalasztas:**
"A Kritikus incidensek eseten:
- Response time (a hiba azonositasa, korulhatarolasa, a bejelento tajekoztatasa): 2 munkaora
- Resolution time (a hiba teljes elharitasa): 8 munkaora
A resolution time szamlaloja szunetel, amig a hibaelharitas a Megrendelo vagy az Uzemelteto oldali kozremukodesre, jovahagyasra, vagy informacioszolgaltatasra var (clock stop)."

---

## 3. YELLOW -- FONTOS, TARGYALANDO

### 3.1 Unnepnapok nem definaltak

**Hivatkozas:** 1. sz. melleklet, SLA tabla, "Meresi idoszak" oszlop: "5x11 (7.00-18.00)"

A szerzodes munkarendet ir elo, de sehol nem emliti a magyar allami unnepnapokat. Az iparagi standard MINDIG kizarja az unnepnapokat a business hours definiciobol.

2026-ban 11 munkaszuneti nap van, ebbol toebb munkanapra esik: Apr 3 (Nagypentek), Apr 6 (Husvet hetfo), Maj 1, Maj 25 (Punkosd), Aug 20, Okt 23, Dec 25, Dec 26.

**Javasolt szoveg:**
"A rendelkezesre allasi idoszak hetfo-pentek munkanapokra vonatkozik (7:00-18:00), a Munka Torvenykonyve szerinti munkaszuneti napok kizarasaval. Az SLA szamlalo munkaszuneti napokon nem fut."

### 3.2 Munkaido szelen erkezo ticketek

**Hivatkozas:** 1. sz. melleklet: "A bejelentesek a het minden napjan 0-24 oraig rogzithetok. A bejelentesek Vallalkozo altali feldolgozasa az alabbi idoszakokban tortenjen meg: 5x11 (7-18.00)"

Ha 17:59-kor erkezik egy Kritikus ticket, az SLA indul de erdemben mar nem lehet elkezdeni. A szerzodes nem szabalyozza.

**Javasolt szoveg:**
"Amennyiben a bejelentes a rendelkezesre allasi idoszak utolso 30 perceben erkezik (17:30 utan), az SLA szamlalo a kovetkezo munkanap 7:00 oratol indul."

### 3.3 Egyoldalu hosszabbitas arazo nelkul

**Hivatkozas:** Szerzodes 10. pont ("A szerzodes hatalya"), 2. bekezdes

**Szerzodes szovege:**
"A szerzodes 12 honap hatarozott idore szol, melyet kovetoen a Megrendelo opcionAlisan rendelkezhet egyoldaluan a szerzodes idotartamanak tovabbi 12 honappal torteno meghosszabbitasarol. Megrendelo hosszabbitasi szandokat legkesobb a szerzodes lejarta elott ket honappal koteles jelezni."

**Mi a problema:**
- MVMI egyoldaluan dont, Sonrisa nem tagadhatja meg
- Nincs arfelulvizsgalat, 24 honapra kotelezodsz a mai arszinten
- A tender (Szakmai Indoklas, 2026-02-05) NEM tartalmazott arrogzitest a hosszabbitasi idoszakra -- csak az Essential csomag kedvezmenyeit rogzitette
- A 7.1. pont a 24 havi osszesitett dijat tartalmazza, tehat az arak implicit rogzulnek

Lasd meg: 1. fejezet, "Arrogzites es hosszabbitas" resz.

**Javasolt szoveg:**
"A szerzodes meghosszabbitasa eseten a Felek az arakat felulvizsgaljak. Amennyiben a KSH altal publikalt fogyasztoi arindex az elozo 12 honapban meghaladja az 5%-ot, a Vallalkozo jogosult az inflacio mertekenek megfelelo aremelest alkalmazni."

### 3.4 Kotber halmozodas

**Hivatkozas:** Szerzodes 14. pont, 14.1. alpont ("Fix havidijas szolgaltatasok eseten")

A szerzodes tobbfele penalty-t definal:

| Penalty tipus | Merteke | Hivatkozas |
|---------------|---------|------------|
| Kozlekedesi lampa piros | havi dij 20%-a (~372 EUR) | 14. pont, 14.1., "SLA sertes szolgaltatasi dijengedmenye" |
| Kritikus/surgos SLA sertes | 10.000 Ft (~25 EUR)/megkezdett ora, max havi fix dij | 14. pont, 14.1., "Kritikus problema es Surgos igeny hibajavitas kotberezese" |
| Hibas teljesites | havi fix dij 30%-a (~558 EUR) | 14. pont, 14.1., "hibas teljesites eseten" |
| Karterites | korlattan (lasd 2.1) | 14. pont, "Karterites" alfejezet |

**Hibas teljesites definicioja (14. pont, 14.1.):** "Megrendelo minden olyan vallalkozoi teljesitiest hibas teljesitesnek tekint, melynek eredmenyekent a rendszer mukodese az elvart funkcionalitastol elteroen mukodik, a hiba nem lett kijavitva vagy a hibajavitas ujabb hibat generalt."

Egy rossz honapban ezek egyutt: 20% + 30% + orankenti kotber + karterites = a havi dijnal joval tobb.

**Javasolt szoveg:**
"Az adott havi osszesitett penalis (kotber + dijengedmeny + karterites egyuttesen) nem haladhatja meg az adott havi netto fix dij 100%-at."

### 3.5 Felmondasi jogok aszimmetriaja

**MVMI azonnali felmondasi jogai:**
- Szerzodes 4. pont: jogosultsagi szabalysertesnel ("a jogosultsagok minden ertesites nelkul, azonnali hatallyal visszavonasra kerulnek, es a Megrendelo a szerzodest azonnali hatallyal felmondhatja")
- 5. sz. melleklet (Adatfeldolgozasi megallapodas), 9.5. pont: adatfeldolgozasi szerzodesszegesnel
- 4. sz. melleklet (ASZF): tovabbi esetek az ASZF szerint

**Sonrisa felmondasi joga:** Nincs rendes felmondasi jog a 12 honapon belul a szerzodes szovege szerint. Meg akkor sem, ha az MVMI nem fizet, nem biztositja a hozzaferest, vagy egyeb modon akadalyozza a teljesiteset.

**Megjegyzes:** Az ASZF (4. sz. melleklet, online elerheteo: informatika.mvm.hu) tartalmazhat tovabbi felmondasi szabalyokat -- ezt kulon ellenorizni kell.

**Javasolt szoveg:**
"Vallalkozo jogosult a szerzodest 60 napos felmondasi idovel felmondani, amennyiben a Megrendelo 30 napot meghalado fizetesi kesedelembe esik, vagy a teljesiteshez szukseges hozzafereseket 15 munkanapot meghaladoan nem biztositja."

### 3.6 Penzugyi teljesitesigazolas felfuggesztese

**Hivatkozas:** Szerzodes 4. pont ("Vallalkozo reszere biztositott jogosultsagok"), 2. bekezdes

**Szerzodes szovege:**
"a szerzodes, illetve a szerzodes valamely terjedelmenek Megrendelo altali penzugyi teljesitesigazolasa felfuggesztesre kerulhet"

Ez azt jelenti, hogy az MVMI megtagadhatja a szamla elfogadasat, ha ugy iteli meg, hogy a Sonrisa a jogosultsagi kereten tul tevekenykedett. Penzaramlas kockazat.

### 3.7 Szerzodesmodositas egyoldalusag

**Hivatkozas:** Szerzodes 13. pont ("Szerzodesmodositas")

**Szerzodes szovege:**
"Nem minosul a szerzodes modositasanak a Megrendelo sablonjait kepezo mellekletek (pl.: Muszaki teljesitesigazolas, IT jogosultsagi lista, Feladatkiadasi lap, valamint az alvallalkozokat erinto rendelkezesek) modositasa."

Tehat az MVMI a 2. sz. mellekletet (Muszaki teljesitesigazolas), 3. sz. mellekletet (IT jogosultsagi lista), 6. sz. mellekletet (Feladatkiadasi lap) es az alvallalkozoi rendelkezeseket egyoldaluan modosithatja szerzodesmondositas nelkul.

---

## 4. GREEN -- RENDBEN VAN

### 4.1 Muszaki tartalom
**Hivatkozas:** 1. sz. melleklet ("Muszaki tartalom, SLA")
Megegyezik a tender kiirassal. L3 support, 5x11, SLA tabla azonos a palyazattal. [Ld. Tender mappa: "AZURE DEVOPS tamogatas muszaki.pdf"]

### 4.2 Teljesites modja
**Hivatkozas:** Szerzodes 9. pont ("Teljesites modja")
Havi osszesito es jelentes keszitese, reszletes dokumentalas. Vallalkozoi jelentes alapjan, ahol "reszletesen rogzitesre kerul, hogy az adott idoszak alatt Vallalkozo milyen feladatokat lat el." [Szerzodes 9. pont, 1. bekezdes] Ez vedelem is egyben.

### 4.3 Uzemeltetest Tamogato szerepkor
**Hivatkozas:** 7. sz. melleklet ("Uzemeltetest tamogato szerzodeses kotelezettsegei")
Egyertelmuen definialta, hogy NEM vagyunk uzemeltetok. 6 korlat felsorolva. Ez a legerosebb vedelmunk a felelossegi vitakban. Reszletes elemzes: lasd 11. fejezet.

### 4.4 Kapcsolattartok
**Hivatkozas:** Szerzodes 11. pont ("Felek egyuttmukodese, kapcsolattartas, Felek kepviseloi")
Bozar Anita (MVMI muszaki), Horvath Istvan (szerzodeses), Tumpek Judit (szamlazas), Miklos Nandor (Sonrisa). Tiszta struktura.

### 4.5 Adatfeldolgozasi megallapodas
**Hivatkozas:** 5. sz. melleklet ("Adatfeldolgozasi megallapodas")
GDPR compliant, standard struktura. 4 oras incidensbejelentesi kotelezettseg [5. sz. melleklet, 4.2. fejezet, 2. pont: "4 oran belul ertesiti"]. Mellekletek meg kitoltendok (1-4. sz. almellekletek).

### 4.6 Korrupcioellenes zaradek
**Hivatkozas:** Szerzodes 16. pont ("Korrupcioellenes zaradek")
Standard MVM csoportos kovetelmeny. Uzleti Magatartasi Kodex megismerese szukseges [16. pont, utolso bekezdes].

### 4.7 Jotallas
**Hivatkozas:** Szerzodes 15. pont ("Jotallas")
Csak szallitott szoftver/hardver gyartoi kellekszavatossag/jotallas vonatkozik [15. pont, 1. bekezdes]. ASZF 10-11. pont irányadó. Nem a szolgaltatasra. Elfogadhato.

### 4.8 Karterites enyhito rendelkezesek
**Hivatkozas:** Szerzodes 14. pont, "Karterites" alfejezet, 3. bekezdes
"Vallalkozo felelossege nem terjed ki azokra a karokra, amelyek bekovetkezeseert mas felelos, amelyek kozvetlen ok-okozati viszonyban nem allnak a vallalkozoi tevekenysseggel." Es: "Megrendelo felrohato kozrehatassesetenesetenesetaz elmaradt haszon megteritese iranti igeny a kozrehatasuk aranyaban oszlik meg a felek kozott." Es: "Egy adott esemenyhez kapcsolodo karteritesi igenyt csak egy alkalommal ervenyesithet Megrendelo." [14. pont, Karterites, 2. bekezdes] -- Ezek fontosak, de nem helyettesitik a liability cap-et.

---

## 5. HIANYZO ELEMEK -- amit a szerzodes nem tartalmaz

| Hianyzo elem | Miert fontos | Standard-e? | Megjegyzes |
|--------------|-------------|-------------|------------|
| **Force Majeure** | Mi tortenik vis maior eseten? | Igen, standard | Sem a szerzodes, sem az 1-7. melleklet nem emliti. Az ASZF (4. sz. melleklet) tartalmazhat -- ellenorizni kell |
| **Felelossegi plafon (liability cap)** | Nincs felso hatar a karteritesre | Igen, minden iparagi standard | Lasd 2.1. pont. Szerzodes 14. pont: "teljes mertekben megteriteni" |
| **SLA clock stop** | SLA nem all meg ha az ugyfel blokkol | Igen, ITIL standard | Sem az 1. sz. melleklet SLA szekcio, sem a 7. sz. melleklet nem tartalmaz clock stop mechanizmust |
| **Unnepnapok kizarasa** | Nem definalt | Igen, minden SLA standard | 1. sz. melleklet: "5x11 (7.00-18.00)" -- munkaszuneti napok nem kizarva |
| **Arazo a hosszabbitasnal** | Nincs inflaciokovetes | Gyakori | 10. pont + 7.1. pont: 24 havi rogzitett ar, nincs felulvizsgalat |
| **IP jogok** | Ki a tulajdonos? (scriptek, automatizaciok) | Fontos | A szerzodes nem szabalyozza. Feladatkiadasi lap (6. sz. melleklet) tartalmazhat eredmenytermekelre vonatkozo eloirast |
| **Biztositasi kovetelmeny** | Nincs emlitve | MVMI meretuu cegek altalaban kernek | Nem szerepel sem a szerzodes toerzsszovegben, sem a mellekletekben |

---

## 6. TARGYALASI STRATEGIA

### Prioritasi sorrend

1. **Karteritesi cap** -- Hivatkozz a 7. melleklet "Felelosseg" alfejezetre + 14. pont ellentmondasra. Ez logikailag tamadhatatlaan.
2. **SLA definicio (response vs resolution + clock stop)** -- Hivatkozz az 1. melleklet SLA tabla fejlecere + a 7. melleklet "Onallo intezkedesek tilalma" alfejezetre. Iparagi standard, az MVMI IT csapata ismeri az ITIL-t.
3. **Unnepnapok es munkaido szeli ticketek** -- Hivatkozz az 1. melleklet "5x11" meghatarozasra. Egyertelmu, technikai jellegu, konnyen elfogadhato.
4. **Arfelulvizsgalat a hosszabbitasnal** -- Hivatkozz a 10. pontra es a 7.1. pontra. A Szakmai Indoklas (2026-02-05) nem rogzitett arat a +12 honapra.
5. **Alvallalkozo kerdes** -- Szerzodes 12. pont. Belso dontes kell eloszor: contractor bevonasa szukseges-e?
6. **ISO 27001** -- 5. sz. melleklet, 8. fejezet, 8. pont. Belso dontes: van-e tanusitvany?

### Miben engedhetunk

- Az oradij (35,6 EUR) mar alacsony, de ha a karteritesi cap-et megkapjuk, ez elfogadhato [Szerzodes 7.2. pont]
- Az egyoldalu hosszabbitas elfogadhato, ha kap inflaciomelesi jogot [Szerzodes 10. pont]
- A kotber struktura (kozlekedesi lampa + oradij) elfogadhato, ha halmozodasi tilalommal vedve van [Szerzodes 14. pont, 14.1.]

### Amit NEM szabad elengedni

- Karteritesi cap -- ez existencialis kockazat [Szerzodes 14. pont]
- Clock stop az SLA-ban -- enelkul nem tudjuk teljesiteni az SLA-t [1. sz. melleklet + 7. sz. melleklet, "Onallo intezkedesek tilalma"]
- Alvallalkozoi kerdes tisztazasa -- szerzodesszeges kockazata [Szerzodes 12. pont]

---

## 7. OPERATIV FELKESZULES (ha alairjak)

- [ ] Csapat kivalasztasa (kizarolag Sonrisa alkalmazottak, ha alvallalkozo tiltva marad) [Szerzodes 12. pont]
- [ ] TAM kijelolese
- [ ] MVMI ticketrendszer hozzaferes igenylese [Szerzodes 4. pont, IT jogosultsagi lista: 3. sz. melleklet]
- [ ] Havi riport sablon keszitese [Szerzodes 9. pont: "havonta osszesitest es osszefoglalot keszit"]
- [ ] SLA szamlalo beallitasa (response + resolution kulon, clock stop logika) [1. sz. melleklet, SLA tabla]
- [ ] Belso eszkalacios utvonal definialasa (MVMI Uzemelteto nem reagal -> Bozar Anita) [Szerzodes 11. pont]
- [ ] Titoktartasi nyilatkozat alairatasa a csapattagokkal [5. sz. melleklet, 1. sz. almelleklet: "Titoktartasi nyilatkozat"]
- [ ] Adatfeldolgozasi mellekletek kitoltese (2-4. sz. almellekletek) [5. sz. melleklet]
- [ ] Kibertorvenyi megfeleloseg ellenorzese [Szerzodes 3. pont: "2024. evi LXIX. torveny", ASZF 18. pont]
- [ ] MTIG alairo szemely kijelolese [Szerzodes 11. pont: "Muszaki teljesitesigazolas alairas jogosult: ....."]

---

## 8. KAPCSOLATTARTOK

### MVMI oldalrol

| Nev | Szerep | Telefon | Email | Hivatkozas |
|-----|--------|---------|-------|------------|
| Bozar Anita | Frontend uzemeltetesi osztalyvezeto (muszaki) | +36 20 216 31 73 | bozara@mvmi.hu | Szerzodes 11. pont |
| Horvath Istvan | Medior strategiai beszerzo (szerzodeses) | +36 20 849 97 59 | horvath.istvan1@mvm.hu | Szerzodes 11. pont |
| Tumpek Judit | Szamviteli osztalyvezeto (szamlazas) | +36 70 381 54 56 | tumpekj@mvmi.hu | Szerzodes 11. pont |
| Kur Jozsef | Adatfeldolgozasi kapcsolattarto | +36 20 851 79 49 | kjozsef@mvmi.hu | 5. sz. melleklet, 2.1. pont |

### MVMI alairoi

| Nev | Szerep | Hivatkozas |
|-----|--------|------------|
| Kadar Zsolt | Uzleti alkalmazasok uzemeltetesi igazgato | Szerzodes, alairas blokk |
| Magyar Beatrix | Vezerigazgato | Szerzodes, alairas blokk |

### Sonrisa oldalrol

| Nev | Szerep | Telefon | Email | Hivatkozas |
|-----|--------|---------|-------|------------|
| Miklos Nandor | Szerzodeses kapcsolattarto | 06703767979 | miklosn@sonrisa.hu | Szerzodes 11. pont |
| Szurdi Miklos | Alairo (ugyvezeto) | | | Szerzodes, alairas blokk |
| MTIG alairasra jogosult | **MEG KITOLTENDO** | | | Szerzodes 11. pont: "Muszaki teljesitesigazolas (MTIG) kialliatasara jogosult: ....." |

---

## 9. MELLEKLETEK ALLAPOTA

| Melleklet | Tartalma | Allapot | Megjegyzes |
|-----------|----------|---------|------------|
| 1. sz. | Muszaki tartalom, SLA | Kitoltve, rendben | SLA tabla + feladatleiras megegyezik a tender kiirassal |
| 2. sz. | Muszaki teljesitesigazolas sablon | Sablon, kitoltendo havonta | Szerzodes 9. pont szerint |
| 3. sz. | IT jogosultsagi lista | Kitoltendo (nevek, felhasznalok) | Szerzodes 4. pont: jogosultsag validalas szukseges |
| 4. sz. | ASZF (online hivatkozas) | Nem csatolt, link: informatika.mvm.hu/Tevekenysegunk/ASZF | Szerzodes 1. pont: "2025. marcius 15. naptol hatalyes" |
| 5. sz. | Adatfeldolgozasi megallapodas | Torzsszoveg kesz, almellekletek (1-4) kitoltendok | Fontos: 8.8. pont ISO 27001 szavatossag! |
| 6. sz. | Feladatkiadasi lap sablon | Sablon, kitoltendo eseti feladatoknal | Szerzodes 2. pont: "Feladatkiadasi lapon [...] rogzitik az elvegzendo konkret munkat" |
| 7. sz. | Uzemeltetest tamogato kotelezettsgei | Kitoltve, rendben | **EZ A LEGFONTOSABB MELLEKLET** -- 6 explicit korlat, lasd 11. fejezet |

---

## 10. STRATEGIAI ERTEKELES (Szabolcs meglaatasai)

### ITIL fejlodesi lehetoseg

Ez a szerzodes az elso strict SLA vallalasunk formalis keretben. Ezt hasznaljuk arra, hogy a csapattal kidolgozzuk az ITIL-alapu incidenskezelesi folyamatot. Fontos, hogy pontosan meghatarozzuk a hataridokat, a belso eszkalacios utvonalat, es a dokumentacios standardot. Ez a tudas utana az osszes tobbi accountra is alkalmazhato lesz.

### Junior program

Az opcionalis keret (~63.050 EUR, Szerzodes 7.2. pont) lehivhato feladatokra juniorokat is be tudunk vonni. Elonyok:
- Az alacsony oradij (35,6 EUR, Szerzodes 7.2. pont tablazat) mellett a junior koltseggel meg mindig van marzs
- A juniorok MVMI kornyezetben tanulnak (Azure DevOps, enterprise workflow, ticketkezeles)
- Valodi ugyfelkornyezetben szerzett tapasztalat, ami a CPS junior program fontos eleme

### Upsell lehetosegek

- Proaktiv javaslatok: pipeline modernizalas, kontenerizalas, security hardening [1. sz. melleklet: "Kontenerizalassal kapcsolatos technologiai tanacsadas" mar a scope-ban]
- Minden Feladatkiadasi lap (6. sz. melleklet) uj bevetel a keretbol
- Ha a ticket mennyiseg no, atalhatas Growth csomagra (+80h/ho) [CPS standard: Managed Service csomag leirasok.pdf]
- Mas MVMI rendszerek tamogatasa (nem csak Azure DevOps)
- FinOps / cost optimization az Azure kornyezetben

### SLA feletti munka kulon szamlazasa

**FONTOS:** Ha egy hibaelharitas pl. 8 munkaora SLA-n belul elharithato lenne, de a valos raforditas 15 ora, akkor a kulonbozet (7 ora) az opcionalis keretbol szamlazando [Szerzodes 7.2. pont, Feladatkiadasi lap: 6. sz. melleklet]. Ezt expliciten rogziteni kell az operativ folyamatban:
- Minden ticketnel rogziteni a tenyleges raforditast [Szerzodes 9. pont: "reszletesen rogzitesre kerul"]
- Az SLA-n beluli reszt a fix havidij fedezi [Szerzodes 7.1. pont]
- Az azon feluli reszt Feladatkiadasi lapon keresztul szamlazzuk (14.250 Ft/ora) [Szerzodes 7.2. pont]

---

## 11. ERVGYUJTEMENY: MIERT NEM VAGYUNK UZEMELTETOK

Ez a szerzodes legfontosabb targyalasi ervrendszere. Ha a feletteseddel beszelitek, ez az alap.

### A szerzodes MAGA mondja ki, hogy nem uzemeltetunk

**Forras: 7. sz. melleklet ("Uzemeltetest tamogato szerzodeses kotelezettsegei")**

**1. Definicio [7. sz. melleklet, "Az Uzemeltetest Tamogato szerepe" alfejezet]:**
"Az Uzemeltetest Tamogato tevekenyse NEM minosul uzemeteltelesnek, es nem eredmenyez uzemeltetoi felelosseg- vagy hataskort-atruhaast."

**2. Feladatok [7. sz. melleklet, "Feladatkor" alfejezet]:**
Kizarolag "szakmai tamogatas", "eszeeles, rogzites es tovabbitas az Uzemelteto fele", "elemzesek, javaslatok es szakmai velemenyek", "riportalas es adatszolgaltatas". Egyik sem dontest jelent, mindegyik a tamogatas fogalomkorebetartozik.

**3. Hozzaferesi tilalom [7. sz. melleklet, "Hozzaferesi korlatozasok" alfejezet]:**
"Nem kaphat hozzaferest a rendszer hozzaferes-kezelesehez, jogosultsagi modelljehez vagy alapveto mukodeset befolyasolo beallitasokhoz." Ha nem ferunk hozza, nem is uzemeltethetunk.

**4. Jogosultsag-kezelesi tilalom [7. sz. melleklet, "Hozzaferesi korlatozasok" alfejezet]:**
"Nem jogosult felhasznaloi, adminisztrativ vagy technikai jogosultsagok letrehozasara, modositasara vagy megszuntetesere."

**5. Vegrehajtas tilalom [7. sz. melleklet, "Onallo intezkedesek tilalma" alfejezet]:**
"Onalloan nem hajthat vegre az informatikai rendszer mukodeset, konfiguraciojat vagy biztonsagi allapotat erinto valtoztatast." Es: "minden ilyen jellegu tevekenysseget kizarolag az Uzemelteto kozremukodesevel es az MVMI Zrt. jovahagyasi rendje szerint vegezhet."

**6. Felelossegi korlat [7. sz. melleklet, "Felelosseg" alfejezet]:**
"Felelossege kizarolag az altala vallalt tamogato feladatok szerzodeszeru es szakszeru ellatasara terjed ki. Az Uzemeltetest Tamogato kozremukodesee nem erinti az Uzemelteto es az MVMI Zrt. jogszabalybol es szerzodesbol eredo felelossseget."

### Az eredeti tender kiiras (MVMI altal irt!) is tamogatast ker

**Forras: "AZURE DEVOPS tamogatas muszaki melleklet -- ajanlati felhivas" [Tender mappa: AZURE DEVOPS tamogatas muszaki.pdf]**

**1. Cim:** "Azure DevOps TAMOGATAS" -- nem uzemeltetes, tamogatas [PDF cim, 1. oldal]

**2. Targy [PDF 1. oldal, 1. bekezdes]:**
"szoftvertamogatasi (support), hibaelharitasi, tanacsadasi feladatokra TAMOGATASI szerzodest" -- haromszor szerepel a tamogatas szo

**3. Feladatok [PDF 1. oldal, "Felsoroltak"]:**
- "uzemeltetes TAMOGATAS" (nem: uzemeltetes)
- "hibaelharitasban KOZREMUKODES" (nem: hibaelharitas)
- "IT szakertoi TAMOGATAS"
- "technologiai TANACSADAS"

**4. Tamogatasi tipusok [PDF 2. oldal, "Kulcs felhasznaloi tamogatas" / "Rendszermenedzsment tamogatas" / "Fejlesztoi tamogatas"]:**
Mindharom "rendelkezesre allas biztositasa"-kent van definalva, NEM vegrehajtaskent. Mindegyik "online, vagy telefonos elerheteoseg biztositasat jelenti."

**5. MVMI fenntartja a jogot [PDF 2. oldal, "Egyuttmukodes modja", utolso mondat]:**
"barmely feladat elvegzeset sajat eroforrassal valositsa meg" -- az uzemeltetesi dontes es vegrehajtas az MVMI-e

**6. Rendelkezesre allasi dijstruktura [PDF 3. oldal, "Palyazatban megadando tamogatasi dijak"]:**
A "Rendelkezesre allas biztositasa" es "Szakertoi tamogatas (opcionalis)" ketto feladatkor -- mindketto tamogatasi jellegu

### A Sonrisa ajanlatban (offer.pdf) is tamogataskent szerepel

**Forras: offer.pdf (2026-01-12, CPS szakmai ajanlat) [Tender mappa: offer.pdf]**

**1. "Essential Support csomag" [offer.pdf, 2.1.2. fejezet]** -- a "support" szo egyertelmuen tamogato jelleget jelent

**2. "L3 szintu tamogatas" [offer.pdf, 2.1. fejezet, 2. bekezdes]** -- "L3 szintu tamogatast nyujtunk, amely magaban foglalja a rendszer- es alkalmazasszintu hibak melyrehato elemzeset, reprodukalasat, a gyokerproblemaak azonositasat, valamint a megoldashoz szukseges technikai lepesek meghatarozasat es vegrehajtatat"

**3. "20 ora beepitett orakeret" [offer.pdf, 2.1.2. fejezet, "Essential" resz]** -- ez rendelkezesre allas, nem dedikalt uzemeltetesi kapacitas

### Mi kovetkezik ebbol

| Amit mi csinalunk | Amit az Uzemelteto csinal | Forras |
|-------------------|--------------------------|--------|
| Ticket fogadas, elemzes | Dontes a prioritasrol | 7. melleklet, "Feladatkor" + 1. melleklet 1.d. pont |
| Hiba azonositasa, reprodukalas | Jovahagyas a javitasra | 7. melleklet, "Onallo intezkedesek tilalma" |
| Megoldasi javaslat keszitese | Valtozas vegrehajtasa vagy jovahagyasa | 7. melleklet, "Onallo intezkedesek tilalma" |
| Kozos hibakereses, best practice | Jogosultsag-kezeles | 7. melleklet, "Hozzaferesi korlatozasok" |
| Patch-management tamogatas | Patch telepites jovahagyasa/vegrehajtasa | 1. melleklet, "Rendszermenedzsment tamogatas" |
| Riport keszites | Uzemeltetesi dontes | 7. melleklet, "Feladatkor" + Szerzodes 9. pont |

### Kulso bizonyitekok: iparagi keretrendszerek es joggyakorlat

Az alabbi forrasok tamasztjak ala, hogy az L3 uzemeltetesi tamogatas NEM egyenlo az uzemelestettel.

#### A) ITIL keretrendszer -- Service Operation

**Forras: ITIL v3 Service Operation, 6. fejezet ("Organizing for Service Operation")**

Az ITIL v3/v4 Service Operation fazisaban a support szintek:

- **L1 (Service Desk):** Elso kapcsolatfelvetel, ticket rogzites, egyszeru megoldasok [ITIL SO 6.2.]
- **L2 (Technical Support):** Reszletesebb technikai elemzes, ismert hibak alkalmazasa [ITIL SO 6.2.]
- **L3 (Specialist Support):** Mely technikai elemzes, bug fixing, performance tuning, eszkalacios szint [ITIL SO 6.1.]

Kulcsfontossagu: az ITIL kulon kezeli az **IT Operations Management** (uzemeltetes) [ITIL SO 6.3.] es a **Technical Management** (technikai tamogatas) [ITIL SO 6.1.] funkciokat. Az L3 support a Technical Management ala tartozik, NEM az IT Operations Management ala.

Az IT Operations Management feladatai [ITIL SO 6.3.]: Console Management, Job Scheduling, Backup & Restore, Print & Output Management. Ezek egyike sem szerepel a Sonrisa scope-jaban (1. sz. melleklet).

#### B) IT outsourcing joggyakorlat -- tamogatas vs. uzemeltetes

**Forras: Iparagi joggyakorlat, IT outsourcing szerzodesi jog**

| | Tamogatasi szolgaltatas | Uzemeltetesi szolgaltatas |
|---|---|---|
| **Felelosseg** | Eszkozjelleg: best effort, szakertoi tanacs | Eredmenykotelem: rendelkezesre allas, SLA |
| **Donthozatal** | Javaslatot tesz, de nem dont | Dont es vegrehajt |
| **Karterites** | Kozvetlen karokra korlat, altalaban cap-pel | Kozvetlen + kozvetettt karok, magasabb limit |
| **Tipikus cap** | 6-12 havi dij | 12-24 havi dij vagy korlatan |
| **Peldak** | Helpdesk, L3 support, consulting | Managed hosting, full IT operations, SaaS |

A tamogatasi szerzodes tipikusan "best effort" jelleget kepvisel: a szolgaltato mindent megtesz a szakmai szinvonalnak megfeleloen, de nem garantalja az eredmenyt (pl. rendszer mukodeset), mert az nem az o hataskoreben van.

#### C) Karteritesi cap iparagi standard

**Forras: Gartner / IACCM (International Association for Contract & Commercial Management) kutatasok**

- Az IT szerzodések **51%-aban** a karteritesi plafon 12 havi dij
- A tamogatasi szerzodések eseten ez jellemzoen **6-12 havi dij**
- A **korlatan karterites** kivetelesen ritka, es jellemzoen csak ott elfogadott, ahol a szolgaltato teljes operativ kontrollt gyakorol

A jelen szerzodesben a Sonrisa felelossege korlatan [Szerzodes 14. pont, Karterites, 4. bekezdes], mikozben:
- Nincs operativ kontroll [7. melleklet, "Onallo intezkedesek tilalma"]
- Nincs donthozatali jogosutsag [7. melleklet, "Feladatkor"]
- 20 ora/ho kapacitas, nem dedikalt team [offer.pdf, 2.1.2. fejezet]

Ez az aranytalansag a targyalas legerosebb erve.

#### D) Magyar kiberbiztonsagi torveny (NIS2 / 2024. evi LXIX. tv.)

**Forras: 2024. evi LXIX. torveny a kiberbiztonsagi tanusitasrol es a kiberbiztonsagi felugyeletrol**

A szerzodes maga is hivatkozik ra: **Szerzodes 3. pont**: "Felek rogzitik, hogy jelen szerzodes olyan elektronikus informacios rendszerre vonatkozik, amely A Magyarorszag kiberbiztonssagarol szolo 2024. evi LXIX. torveny (a tovabbiakban: Kibertorveny) hatalya ala tartozik."

A torveny alapjan:
- A **kiberbiztonsagi felelosseg** az **uzemeltetot** terheli, nem a tamogato szolgaltatot [2024. evi LXIX. tv. 7-8. §: szervezeti kiberbiztonsagi kovetelmernyek]
- Az uzemelteto koteles a kockazatkezelesi intezkedeseket meghozni es fenntartani
- A tamogato szolgaltato (mint alvallalkozo/beszallito) a sajat szerzodeses kotelezettsegeiig felel [2024. evi LXIX. tv. 30. §: beszallitoi lancra vonatkozo eloirasok]

Ez megerositi, hogy az MVMI mint uzemelteto viseli a platform biztonsagi feleloseget, a Sonrisa mint L3 tamogato csak a tamogatasi feladatok szerzodeszeru ellatasaert felel.

---

### Ervosszefoglalo egy oldalon

| # | Erv | Forras (pontos hivatkozas) | Ero |
|---|-----|---------------------------|-----|
| 1 | A 7. melleklet explicit mondja: "uzemeltetest tamogato", 6 korlat felsorolva | Szerzodes 7. sz. melleklet, "Szerepe" + "Feladatkor" + "Hozzaferesi korlatozasok" + "Onallo intezkedesek tilalma" + "Felelosseg" alfejezetek | ⭐⭐⭐ |
| 2 | A tender kiiras "L3 tamogatas"-t ker, nem "uzemeltetest" | AZURE DEVOPS tamogatas muszaki.pdf, 1. oldal (cim + targy) + 3. oldal (dijstruktura) | ⭐⭐⭐ |
| 3 | A Sonrisa ajanlat "Essential Support"-ot kinal | offer.pdf, 2.1.2. fejezet + MVM_Sonrisa_Azure_devops_szakmai_Indoklas.pdf (2026-02-05) | ⭐⭐ |
| 4 | ITIL: L3 = Technical Management, nem IT Operations Management | ITIL v3 Service Operation, 6.1. vs 6.3. fejezet | ⭐⭐⭐ |
| 5 | IT outsourcing jog: tamogatas = eszkozjelleg, uzemeltetes = eredmenykotelem | IT outsourcing szerzodesi joggyakorlat | ⭐⭐ |
| 6 | Karteritesi cap standard: 51% IT szerzodes 12 havi dijban maximalizal | Gartner / IACCM kutatas | ⭐⭐ |
| 7 | NIS2/Kibertorveny: uzemelteto felelos a kiberbiztonsagert, nem a tamogato | 2024. evi LXIX. tv. 7-8. § + 30. §; Szerzodes 3. pont hivatkozik ra | ⭐⭐⭐ |
| 8 | Scope: 20 ora/ho, nincs donthozatal, nincs jogosultsag-kezeles | Szerzodes 7. melleklet + 1. melleklet + offer.pdf 2.1.2. | ⭐⭐ |

**Targyalasi hasznalat:** Az 1-es es 4-es ervek a legerosebbek. A 7. mellekletet az MVMI maga irta -- ez azt jelenti, hogy ok maguk hataroltak el a szerepkorunket. Az ITIL hivatkozas iparagi standardot ad a hatterbe. A 7-es erv (NIS2) kulonosen eros, mert a szerzodes maga hivatkozik a Kibertorvenyre (3. pont), ami az uzemeltetot terheli a felelossseggel. Egyutt ezek az ervek megalapozzak a karteritesi cap bevezeteset es a felelosseg korlatozasat.

**Kovetkeztetes targyalasra:** A karteritesi (14. pont) es kotber (14.1.) felelosseg NEM lehet uzemeltetoi szintu, mert a szerepkorunk sem az. A 7. melleklet a Sonrisa legerosebb vedoerve. Ha az MVMI vitatna a karteritesi cap-et, a valasz: "a 7. melleklet, amit Ti irtatok, egyertelmuen kimondja, hogy a felelossegunk kizarolag a tamogato feladatok szerzodeszeru ellatasara terjed ki -- nem az uzemeltetesi donthozatalra, nem a rendszer rendelkezesre allasara, es nem a harmadik feleknek okozott karokra."
