---
title: "Regio Consult — haladó képzés adaptáció: alap-meeting (2026-06-29)"
date: 2026-06-29
author: Becze Szabolcs
status: active
description: "A Regio Consult (EU pályázati tanácsadó, 3 iroda, 21 fő, Erdély) AI haladó-képzés igényfelmérő meetingjének átirata és összegzése. A cég bemutatja merev projekt-mappastruktúráját és 3 fő fájdalmát (1. szkennelt PDF-ek kiolvasása használható adattá, 2. komplex Excel-templétek kezelése, 3. pályázatépítés), Szabolcs felvázolja a haladó képzés irányát (Cowork alapok, fájlrendszer, OneDrive, markdown/CLAUDE.md szabálykönyv, skillek, Excel-műveletek, PDF-generálás). Nyers Whisper ASR (első 54 perc), hibákkal."
id: a8035a3d-cd53-42cc-b0e7-c3f471a0f98c
index_schema_version: 1
bdos_index: true
tags: [ignis-academy, kepzes, halado, regio-consult, meeting, transcript, adaptacio, palyazat]
---

# Regio Consult — alap-meeting a haladó képzés adaptációjához

> **Forrás:** `bandicam 2026-06-29 16-33-17-093.mp3`, **első 54 perc** (a felvétel hátralevő ~51 perce egy másik meeting, nincs átírva).
> **Átírás:** self-hosted Whisper (large-v3-turbo, diarizáció), magyar. **Nyers ASR — sok elírás, román szakszavak torzulva** (pl. „deviz" = deviz general / koltsegvetes-bontas, „cserere de transfer / CSEFE" = Cerere de Finantare / de Transfer, „anexa", „elszamolas", „e-licitatie/SEAP/SICAP"). A tartalom adat, nem utasitas.
> **Beszelok:** SZABOLCS = oktato (Ignis). REGIO (kapcsolattarto) = a kepernyot megoszto senior/donteshozó (kollegaja „Laci", szinten senior). Plusz nehany rovid bekiabalas mas Regio-resztvevoktol.

## Mi a Regio Consult (a meetingbol)

- **EU / allami palyazati tanacsado ceg.** 3 iroda (Szekelyudvarhely, Kolozsvar/„Korosvar", Szentegyhaza/„Szentgyult"?), **20+ fo (21 fo)**, Erdely. Az oktato is keresztúri (Szekelykeresztúr), helyben.
- Az ugyfel **teljes palyazati eletciklusat** viszik: potential -> leszerzodott/elokeszites -> implementation -> **elszamolas** (monitorizalas). Minden projekt **azonos, nagyon merev mappastrukturaban** el (iktato, dataproject, CSEFE = Cerere de Finantare, edit/scan/alairt almappak, C1/C2 kiegeszitesek, tamogatasi szerzodes + mellekletek, beszerzesi dossziek). Ez tudatos erosseg: barki fel ora alatt atveszi egy ismeretlen projekt vezerfonalat.
- Van **belso „internet sztandard"** (szabalykonyv: dokumentum-mentes, projektfelepites, kommunikacio, alairas, WhatsApp-hasznalat, betutipusok) es egy **templet-konyvtar** (Questionnaire General, deviz general, uzleti terv, penzugyi modell Excel-ek). A templetek epitese ido- es senior-igenyes (5-10 ev tapasztalat kell).

## A 3 fo fajdalom (a kapcsolattarto explicit sorrendje)

1. **Szkennelt PDF -> hasznalhato adat (a legnehezebb).** Allami platformokrol (e-licitatie, SEAP/SICAP, CEAP) letoltott kiirasokat/ajanlatokat **kezzel, tetelrol tetelre** kell egyeztetni (m3, tonna, mennyisegek). Tipikus: **353 oldalas, 300 MB-os, szkennelt** (kep!) technikai dokumentacio. 3 lepeses lanc: ajanlatkeres -> ajanlat -> elszamolas, mindenhol konzisztencia-ellenorzes. Ma 100% kezi. Szabolcs elesen jelzi: a **szkennelt (kep) PDF** draga/nehez az AI-nak, a **vektoros / Excel-export** viheto. Kert 2 minta-PDF-et.
2. **Templet-kezeles (a legaltalanosabb).** Komplex, levedett-cellas, kepletezett Excel-ek (deviz general, uzleti terv, penzugyi modell). Cel: uj kiiras „okos PDF"-jebol az AI a meglevo templet alapjan **jobb templetet** generaljon (hibak kiszurve, jobb kepletek/instrukciok). Ma csak senior tudja.
3. **Palyazatepites (a legkevesbe surgos).** A palyazatleadas az aktivitasuk **~10%-a**, ebben mar profik; jol promptolva chatben is sokat kihoznak. Felmerult: kulon agent / nagy palyazatiro agent kerdese.

## Kulcsdontesek es keretek

- **Ez a HALADO kepzes, NEM a Mester.** Agenteket **nem epitunk** (tul komplex). A kapcsolattarto **a Mester kepzesen jart, a haladon nem** — a Regio-csapat a haladot kapja.
- A cel: **alapok + eszkozok atadasa**, hogy **maguk tudjak automatizalni magukat**, nem kesz megoldas epitese. Szabolcs „atomizalja a feladatokat", mintazatokat keres a kuldott anyagbol.
- **Halado kepzes tananyag-gerince (Szabolcs felsorolasa):** mi a Claude Cowork; munka a lokalis fajlrendszeren; osszekotes Microsoft 365 / OneDrive-val; mi a markdown fajl; navigacio; **CLAUDE.md mint szabalykonyv** (egymasba agyazott, „kalandkonyv"-szeru, **parhuzamos** mappa a meglevo merev struktura melle, azt nem bolygatva); szabalyok felismertetese es kovetese (belso sztandard -> markdown); **mi a skill, hogyan irj/hasznalj skillt, Excelbol skill-hivas**; bizonyos Excel-muveletek; PDF-generalas.
- **Konkret demo-otlet (Szabolcs):** Excel-skill — ures templet + kitoltott pelda + forras-Excel harmasabol megmutatni, hogyan tolt ki az AI komplex Excel-t keves inputbol (ahogy o a sajat statisztikajat tolti). Plusz: szamla-generalas ledolgozott orakbol.
- **Team plan** (~**534 EUR/ho, 20-21 seat, ~18 EUR/seat**) — meg nincs meg, holnap reggel veszik; egyben, hogy a **skillek/agentek megoszthatok** legyenek a csapatban.

## Logisztika

- **Nap: csutortok.** Kezdes 11:00 (mindenki 10:30-11:00 erkezik), **12:30 brunch-szunet**, utana tovabb; Szabolcs **17:00-ig** maradni tud. Helyben van (keresztúri), biciklivel megy.

## Follow-up (a Regio kuldi, Szabolcs feldolgozza)

- [ ] **2 minta-PDF** (egy ajanlatkeres + egy ajanlat, szkennelt) — a PDF-kiolvasasi kiserlethez.
- [ ] A **belso „internet sztandard"** dokumentum (szabalykonyv).
- [ ] **Templet-harmas:** ures templet-Excel + kitoltott Excel + a forras-Excel, amibol kitoltottek (osszetartozo deviz/uzleti terv).
- [ ] Szabolcs: holnap visszahiv otletekkel; videobol mintazatokat nyer ki, atomizalt feladatokat epit.

---

## Teljes atirat (nyers, beszelonkent osszevonva)

**REGIO (kapcsolattartó, képernyőt oszt):** Transcribe. Start recording. Engliszt adjak, vagy magyart?

**SZABOLCS (oktató):** Vagy autót. De igazából mindegy kinyerem a hangfájt belőles.

**REGIO (kapcsolattartó, képernyőt oszt):** Oké. És ezt majd én kell elküldjem neked?

**SZABOLCS (oktató):** Vagy jogot adj hozzá, hogy le tudjam tölteni. Igen. De meglátjuk majd a végén, hogy hogy csináljuk ezt.

**REGIO (kapcsolattartó, képernyőt oszt):** Jó, oké. Figyelj, nem tudom, látod a képernyőmet?

**SZABOLCS (oktató):** Igen.

**REGIO (kapcsolattartó, képernyőt oszt):** Doksan. És akkor most elmegyek arra, hogy hogy néz ki a még struktúránk. Ez a Région Consult, van egy ilyen struktúránk. És akkor gyakorlatilag a projektek között, tehát hogy végigmondom, ez a pénzügy, ez csak limitált hozzáfér, és grand scheme-oká be vannak mentve mindenféle kírásaink. Marketing info, ez annyira nem érdekes. Projectsbe megyek be ezek a projektek, és akkor van egy ilyenünk, hogy mindenünkben van kategorizálva, vagy actual projects, amikre leszerződtünk, de előkészítés alatt van. Leszerződtünk, de még nem egy, mondjuk egy támogatott pályázat, de már van rá szerződésünk, vagy egy olyan típusú projekt, ami nem feltétlenül pályázat, hanem más típusú projekt, de van rá szerződésünk. Van egy ilyenünk, hogy potential, ez, ide belakunk mindenfélét az elmúlt időszakból, amikor a potential, ez az alap. Potential project, amikor már elkezdtünk valakivel tárgyalni, és az adatokat gyűjtjük, és akkor van egy ilyen, hogy implementation, ami azt jelenti, hogy már a megvalósítás alatt levő projektek. És akkor ebből fogod látni a teljes struktúrát, a teljes megvalósítási struktúrát. Most például bemegyek a peneszebe, és akkor minden projektnek van adva egy kód, és akkor tudjuk azt, hogy az illető projekt, hogy van, most bemegyek mondjuk a Terézia sajgyárhoz, és akkor mindenhol ugyanezt a struktúrát látjuk. Itt van kint egy iktató, mert mi vezetjük teljesen a projektjét az ügyfélnek, tehát a regiszterünket, az ő regiszterét. Van egy dátaprojekt, amiben bevezetjük a legfontosabb adatokat. Megmutatom ezt is, csak egy picit lassú a gépem. Miért ennyire lassú? Itt van. Ide így bevezetjük a legfontosabb adatokat, és akkor innen tudjuk, hogy milyen projekt, ki az, milyen támogatás, stb. stb. stb. Ez egy egyszerűen bízik fáj. és akkor, na most, mit csináljunk? Jó. És akkor amúgy minden projektünk ugyanebben a struktúrában van. Van egy CSEFE, ami a Cserere de Financsárem, és akkor itt van egy edit dokumentációval megszámozva, és akkor tudjuk, hogy a THR, az Terézia, és akkor itt vannak az adatok, pályázati szinten, és akkor ez a scannelt folder, ami már a végleges, tehát ami csak a pályázathoz kell, és ez az aláírt folder. És akkor az első kiegészítés kérésnél ugyanúgy, második kiegészítés, hogy C1 edit, C1 scan, C1 aláírt. És akkor ez így van végigvezetve. És akkor utána ez egy támogatási szerződés, és az ahhoz levő mellékletek, meg ezek a beszerzési dossziék, és az is ugyanebben a struktúrában. Tehát minden projektünk ugyanígy néz ki. Teljesen mindegy, hogy a Penesze Teréziába megyek, vagy a, mint tudom én, Penere-re, és akkor itt azt mondom, hogy itt van a Kánoki kastély, ott is ugyanezt a struktúrát látod. Ott annyi különbséggel, hogy a dáteprojekt mellett még kint van egy-két dokumentum, pluszba egy ekipedeprojekt, vagyis a projektcsapat is kint van így, hogy hívjál meg az oldalság, hogy mit, hogy címkézik a dosszárakat, meg ilyen-olyan dolgok. De hogy gyakorlatilag minden projektünk ugyanezzel a struktúrával működik. És akkor én, hogyha visszamegyek a Peneszehez, akkor például nekem, és visszamegyek a Teréziához, hogyha már ezt kezdtem el, ez egy tejgyár építése, és akkor nekünk van egy ilyen technikai tervünk mondjuk, és a technikai tervet, amikor láttuk, akkor lesz egy ilyen dokumentációk. És akkor mondok én neked a végén egy ilyen dolgot, hogy dokumentácia, technikai, ekonomika. És ez egy klasszikus probléma, ezt megnyittom, ez egy elég nagy dokumentum, és ez az egyik típikus, klasszikus problémánk, csak sokféleképpen megjelenik. Hát ez egy picit nagy, de mindegy. Ez egy nagy beluházás, elég komoly csomag van.

**SZABOLCS (oktató):** Általában ilyen nagy szokott lenni?

**REGIO (kapcsolattartó, képernyőt oszt):** Igen, ennyi, egy technikai terv, egy több millió eóos projektek, ekkora technikai terv. Mármint ez az összes fájl a technikai terv, ez maga fogod látni, hogy ez a borlap, de ez egy ilyen dokumentáció, ami 353 oldal.

**SZABOLCS (oktató):** De azért 300 megabájt, mert szkennelve van hatalmas felvontáció.

**REGIO (kapcsolattartó, képernyőt oszt):** Igen, de hát sajnos ezt így kell látni. És ez egy ilyen dokumentáció, és most belemegyek a dokumentációba, és akkor itt azt mondja, hogy itt van. Ez maga azt jelenti, hogy ezt kell megajánlja a kivitelező. Azt mondja, hogy az ámenazsárját elnudulja, az transportúrúti ará betonulói, mortálulói, és ez 2090 tonna lesz. Majd szepetúramekánika, az 100, mit tudom, metrupetrát. Tehát, hogy van egy ilyen, ez a struktúrája, minden építkezési beruházásnál, ez a struktúrája. Tudod, ez így néz ki, minden. És most menjek egy picit egy ilyen fejezet kezdéshez, és itt kezdődik egy fejezetem, itt látszik, hogy unitáter vendem el, szóra, kantitáter.

**SZABOLCS (oktató):** Igen.

**REGIO (kapcsolattartó, képernyőt oszt):** És akkor itt látjuk, hogy kömimbrán sem ment, és akkor kapák, sír rá, mert tudom. Az egyik legunalmasabb dolog, még tudsz követni, ugye, vagy követető vagyok, hogy itt van a diá, a doszárdia kizicil, és a dál, a doszárdia kizicilukránél, kapok egy ajánlatot a kivitelezőtől.

**REGIO résztvevő:** És itt van az ajánlatom.

**REGIO (kapcsolattartó, képernyőt oszt):** És akkor ez egy jobb dokumentum, mert ez nem vissza van szkendelve, egyre jobban haladunk ebbe az irányba, és itt a dokumentációban, ellenben itt van a technikai ajánlatom. Látod, ugyanaz a struktúra. És akkor a kollégáim, képzeld el, nekik elfogjanak, és le kell előrizzék, hogy ugyanannyi bukátat, és ugyanannyi mennyi, tehát hogy ugyanannyi 19 bukát, de support her, Tiemontáret rendelte meg, tehát ajánlotta meg, mint amennyi volt a a kiírásban.

**SZABOLCS (oktató):** Igen.

**REGIO (kapcsolattartó, képernyőt oszt):** De hallgatni,

**SZABOLCS (oktató):** ez nem képformátumban?

**REGIO (kapcsolattartó, képernyőt oszt):** Hogy?

**SZABOLCS (oktató):** Ez nem képformátumban? Megvan? Mert a képformátumban az a baj, hogy nagyon költséges processzálni a képeket, és...

**REGIO (kapcsolattartó, képernyőt oszt):** Már még mi nincs meg képformátumban? Ez? Maga az ajánlat?

**SZABOLCS (oktató):** Egy Excel, vagy egy táblázat, vagy valami, ami nem képformátumban?

**REGIO (kapcsolattartó, képernyőt oszt):** Ezek... Ez... Ez... Hát ez e-scanert, látod, ez még talán megvan nekünk ilyen... Tehát, hogy ez még talán megvan nekünk egyszerűen importált PDF formátumban, és az ajánlat, az meg ilyen szintén az is egy importált. Miért? Mert az e-devize programból szedi ki, és gyakorlatilag mindenki olyan devizprogramban dolgozik, amilyen devizprogramban akar. És akkor nekem bármelyik kollégám, aki ezzel dolgozik, neki kell ugorjon, és el kell kezdeni ezt nézni, hogy egyenként tudod, vagy... És nem tudom, nincs te magarok rámenni, hogy ez a dekopert álleteremben csetál több méter, és kantitáter.

**SZABOLCS (oktató):** Igen, tehát oda mennék vissza.

**REGIO (kapcsolattartó, képernyőt oszt):** És végig kell pipálja az egészet, hogy ez így van, vagy nincs így.

**SZABOLCS (oktató):** Igen, igen. Tehát oda mennék vissza, hogy az exportálásnál nincs olyan opció, hogy ne képként szkennelt változatba.

**REGIO (kapcsolattartó, képernyőt oszt):** Nem mi exportáljuk. Mi egy beszerzést elenőrzünk. Mi ezt letöltjük az elektronikusan aláírt, mi nem is ismerjük a kivitelezőt, a kiaján, hanem mi letöltjük ezt az elicsitáciéről, vagy a száfírnak, vagy valamelyik állami intézménynek a platformjáról, és utána összenézzük és ellenőrizzük.

**SZABOLCS (oktató):** Jó, figyelj, hát el tudsz küldeni nekem két ilyen PDF-et, hogy játszatozzak egy kettőt.

**REGIO (kapcsolattartó, képernyőt oszt):** Én ezt a kettőt is el tudom akár, vagy mit tudom két ilyen.

**SZABOLCS (oktató):** Két olyat.

**REGIO (kapcsolattartó, képernyőt oszt):** Na ez az egyik klasszikus problémánk, de nem fejeztem be, mondom tovább, és akkor nekem ez úgy néz ki, hogy ezt a projektet, akkor el fogom kezdeni az elszámolásokat. Hát, menek egy másik projektről, ami egy picivel előre haladottabb fázisban van, szintén egy ilyen, itt is megvolt, és akkor itt, nem, várj egy picit, bocsánat, hogy úgy keressem, akkor én itt az elszámolásba ugyanúgy le kell tegyem a dokumentációt, igen. Nem, nem az a jó, de igen, ezt így megcsinálja, és ugyanúgy, tehát én az elszámolásba ugyanezt le kell tegyem, de mondom mindjárt, mert de szerintem ez lesz az, csak én nem tartok az elejét,

**REGIO résztvevő:** de ez a centralizatorok, bocsánat,

**REGIO (kapcsolattartó, képernyőt oszt):** minél ezek a jegyzőkönyvek, ezt nem tudom megszabadítani, akkor megyek egy másikra, a cipi háromra, és itt azt mondom úgy, a lényeg az, amit akarok mondani, csak vére nem találom meg a dokumentációt, de magát a devizt, amit leadja valamiért, nem tudom, melyik dokumentuma van bennem, de a lényeg az, hogy gyakorlatilag az ajánlat és a megvalósítás gyakorlatilag amit itt mutattam neked, tehát ez volt az ajánlatkérés, ez az ajánlat, és a végén lesz egy olyan, hogy ebből a 67,310 köbméterből már megvalósult 47,25 köbméter, és mi ezt vezetjük egy nagy Excel-be egyszerűen hogy hívják formájában, egyszerűen tehát az ideális esetben mi ezt vezetjük, mondjuk menjek el egy telekihez, amely már a végén van, kicsit kapkodok még, de és akkor van ebből mi legyártjuk ezt, a nagy centralizátorunkat, és akkor levezetjük az egészet egy ilyen formába, ez is mondják megnyílik, egyszerűen sok minden van nyitva a gépemen, jó, és akkor itt van egy nagy centralizátorunk, ahol azt mondjuk, hogy ez volt az eredeti költségvetésünk, fejezetekről lebontva, ezek a szerződéseim, hogy kinek mennyi pénze volt, ez így még látható, követhető, ugye? És akkor ez a centralizátor, a cserere de transferek, hogy az egyesbe ennyit kértem, kettesbe annyit kértem, eddig kértem, összesen 19 millió, tehát kértem 19 millió lejt, eddig kivizettek 18 millió lejt, mennyit vágtak vissza, és akkor ezt így cseretetranszferekként lebontja, és akkor ilyen szinten, tehát, hogy én csinálok ebből ilyen kivezetéseket, de ideális esetben, csak most nem akarom azt úgy, ja igen, ezek a a munkálatok, ideális esetben nekem, én az egészet, amit itt megcsinálnék, tehát, hogyha azt szeretném, hogy ideális esetben ez, viszbe legyen vezetve egy nagy összes szintő táblázatba, hogy akkor ebből mennyit kértünk, ebből mennyit kértünk, ebből mennyit kértünk. Tehát ez az egyik legjelentősebb problémám, aminek a megoldása jelen pillanatban csak és kizárólag kézi erővel megy.

**SZABOLCS (oktató):** Akkor gyere megismétlem, hogy lássam, hogy jól értettem-e a problémát, és lássuk, hogy mit kezdünk a képzés szempontjából vele. Szóval, van egy platforma, honnan letöltitek konkrétan azt, hogy mi az a kérés, tehát mire kérnek árajánlatot?

**REGIO (kapcsolattartó, képernyőt oszt):** Nem, az, hogy a kérést, azt mi adjuk ki, de azt is egy tervezőtől kapjuk be.

**SZABOLCS (oktató):** Megkapjátok, és ez egy pdf, amit egy skennel dokumentum valójában, ez nagyon fontos. Mert ha valami 300 megabajtos és skennelve van, az AI azzal küzdeni fog, ha egyáltalán meg tudja csinálni. Ha nincs skennelve, mármint hogy a tartalma az egy vektor, valami, amit ki lehet nyerni gyorsan, programmatikusan, akkor 300 oldal vihető. Ez a kettő között a különbség. Az egyik egy kép sorozat, és a másik bené.

**REGIO (kapcsolattartó, képernyőt oszt):** Alapvetően, mivel minden tervező és minden bevizes más programba dolgozik, így, legjobb esetben, ezt tudom, egy Excel-be kiexportálva talán megkapom.

**REGIO résztvevő:** Te az Excel az jó. Az Excel az jó.

**REGIO (kapcsolattartó, képernyőt oszt):** De már magát, az ajánlatot, ugye az első fázis az, hogy ajánlatkérés, aztán jön rá egy ajánlat. Magát, az ajánlatot, vagyis a választ, hát azt nem biztos, hogy megkapom. Vagy szinte biztos, hogy nem kapom meg, mert valószínűleg nem ismerem a kivitelezőt, azt sem tudom, most mit tudom, hogy hívják valamok, most van egy korosvári onkológiánál, bírálunk el egy ajánlatot, van tíz ajánlat, tíz ajánlatból, tíz ajánlattelőből véletlenszerűen ismerünk bárkit, de jogunk sincs, mert törvénytelen megkeresni valakit.

**SZABOLCS (oktató):** Hát egyszerűen csak kaptak egy PDF dokumentumot, amivel élnetek.

**REGIO (kapcsolattartó, képernyőt oszt):** Így van. Így van. És abból én a végén kell egy ehhez hasonló lekövetetően.

**SZABOLCS (oktató):** Egy ilyen monitorizálást csinálni.

**REGIO (kapcsolattartó, képernyőt oszt):** Így van, megcsináljam, amikor már eljutok az elszámoláshoz. Először azt csinálom meg, hogy le kell ellenőrizzem, hogy az ajánlatnak megfelelően, az ajánlatkérésnek megfelelően az ajánlat, aztán hogy hívják egy... Bocsánat, ezeket lelövöm, mert itt ugranak fel mindenféle ablakok. És aztán azt mondom, hogy amikor elkezdek elszámolni, az elszámolás az ajánlatnak megfelelően. Tehát ilyen háromlépéses dologról van szó. Ez az egyik... Igazán a legnehezebb problémával kezdtem, mert tudom, hogy egy PDF-ből, egy skennel PDF-ből borzasztóan nehéz.

**SZABOLCS (oktató):** Igen.

**REGIO (kapcsolattartó, képernyőt oszt):** De ez az egyik legnyűgösebb problémánk. Igazából ezt fizikailag szokta mindenki csinálni, mert másképp állatotjuk. Az ajánlatelenőrzéseket.

**SZABOLCS (oktató):** Jó, hát itt sok minden megmutattás, hogyha ezt a videót le fogom tudni tölteni, akkor egy kicsit fogom tudni ezt a struktúrát nézni. Az egyik az, hogy... Tehát a képzésnek a célja az az, hogy vannak alapelemek, amit a Cloud Cover-ben be tudok mutatni. Mi egy plugin, mit hogyan lehet használni. Mit jelent az, hogy a háttérben a lokális fájrendszeren fut? Hogyan fogjátok tudni ezt használni közösen a OneDrive-val? Van egy saját struktúrátok? Mit tudunk kezdeni azzal, hogy egy ilyen szuper merev struktúrátok van? Mert jó az, hogyha merev a struktúra. Igazából az program...

**REGIO (kapcsolattartó, képernyőt oszt):** Nagyon merev a struktúránk, és ez a másik, amit akartam mondani, mihez ragaszkodók. Mert... És mutatok egy másik dokumentumot neked, ami talán egy hasznos dolog lesz. Pocsárát, csak a másik céget nézem, a Régio Consultant, igen. És nekem innen kezdődik, van egy ilyen internet sztandádom. És az én internet sztandárdjaim az megmondja, hogy hogyan mentek el egy dokumentumot, hogyan építek fel egy projektet, és ezt így teljesen struktúrálta, és mindenik így van felépítve.

**REGIO résztvevő:** Jó. Figyelj, ezt nem tudom, hogy ezt az internet sztandárdot.

**REGIO (kapcsolattartó, képernyőt oszt):** meg kell használjon, hogy használjuk a kommunikációt, Verdánál kilencesen írunk, tehát minden ilyen hülyeség benne van, érte?

**REGIO résztvevő:** Jó. Ezt eltunáljuk...

**REGIO (kapcsolattartó, képernyőt oszt):** Hogy néz ki az aláírásunk, mikor használunk a WhatsApp-ot, mindenféle ilyen dolog benne van ebben. Jó. Na most nekünk ez, ezt nem akarom, tehát ez azért merev, struktúrálisan, mert gyakorlatilag háromiroda, húsz plusz fővel, hasonló típus, valamilyen szinten át kell lássuk ezt az egészet.

**REGIO résztvevő:** Abszolút.

**REGIO (kapcsolattartó, képernyőt oszt):** És nem tudok én, és így ellenben, hogyha ugyanúgy ment mindenki, ugyanabban a struktúrában, akkor gyakorlatilag tök mindegy, vagy elviegve tök mindegy, hogy a Szentgyűlt hírodából valaki besegít egy tök ismeretlen projektbe a Korosvári hírodában, mert fel tudja venni a vezérfogalat fél óra alatt.

**SZABOLCS (oktató):** Pontosan. Ezt a dokumentumot el tudnád különni, kérlek? Ezt a standardot? Persze. Persze. Tehát akkor kéne ez a dokumentum, és akkor a két PDF-es egy Excel, ami összetartozik, hogy lássam, hogy hogyan tudom ezt az egészet összekötni, hogyha egyáltalán összetudom kötni.

**REGIO (kapcsolattartó, képernyőt oszt):** Ja, persze ezeket elküldöm, valamelyik projektből kiveszem. Ez az egyik tibigus standardodok. A másik az, amit viszonylag jól ráérez, vagy ami van, és amit mondtál, hogy hogyan építünk fel egy pályázatot, amiben ellenben az van nekünk, és akkor most jövök ismét, hogy mi ezzel úgy fogunk neki, hogy azt mondom, hogy van egy ilyen templétkönyvtárunk. Penederem, vagy nem, Penederem, mert ez trisszebb, és itt akkor azt mondjuk, hogy ilyen szinten le van templétezve minden, hogy tudjuk, hogy milyen dokumentumot küld ki, milyen, tehát Questionnaire General, egy csomó mindent letemplétezünk. Most ez egy ilyen standard templét, és akkor mindenki ezt küldi ki az ügyfélnek. És akkor, ide vissza vagyok, és akkor igazából mondjuk az állattenyésztésbe, megfogtuk a dokumentációt, és mármint a pályázati dokumentációt, és mindent, ahogy elkezdtünk letemplétezni. Ez kurvasok időben megy el, és csak és kizárólag szenyorok tudják megcsinálni. Most mondok egy ilyen példát, megmutatok egy ilyen bonyolgultabb Excel-t, megfog nyílni, ez egy bonyolgultabb Excel, azt mondja nekem, van, adok instrukciókat, hogy mit, hogy kell csinálni, adok egy device general struktúrát, templétetet, amit ki kell töltsön, egy esú számolást, amit szintén egy nagyon bonyolgult Excel-ből vettem ki, állap, stb., stb., stb., hogy kapja ezt a dolgot, és úgy építi fel az üzleti tervet, hogy gyakorlatilag a pályázatóhatóság már csak ezt látja. Mert ez az ő stondoltja. És akkor nekem egy projektemben, most elmegyek egy, szintén egy peneszeből, és azt mondom, hogy master-t, ez egy disznófár. És akkor, amikor adunk le a pályázatot, akkor nekem van egy ilyen cuccom, ez az edit, amiben minden bekerül. Az editbe itt van az anexabém, amit az előbb megnyitottam feltöltve. Tehát, hogy ez a dokumentáció. ez itt már fel van töltve adatokkal, és kijön ez az Excel-be, és itt ki kell hozzá, hogy minden rendben van. És akkor, amikor ez teljes mértékben megvan, akkor én ezt átkelvezess, nem én, de utána egy meló az, hogy megfogjuk, és ezt átvezetjük, abba a formátumban, amit már a pályázatotú hadonság kér. És az az 1, 2, az a szefe, bocsánat. Ja igen, akkor már a szefebe beraktam, és akkor a pályázatotú hadonságnak megvan az anexabéje, ez az, ami ugyanaz, mint amit az előbb láttál, csak az már egy általáltott formátum, és az én excelemet bevezeti. És az már így néz ki, de az ugyanaz, mint az én excelem, csak... Na, ez meg úgy néz ki rául, hogy ebből az excelelből veszi valaki a számokat, és lépésről lépésre ezt a biláncot ide bevezeti a biláncba, mondom, hogy hová, itt fogjuk látni, itt van, ebbe. És akkor ez, itt ez a V1-47-30-9-8-8-3-9-71, ez, jó, ez valószínűleg, hogy a V1-47-30-9, és ezeket lépésről lépésre átvesztetni ebbe az okos PDF-ben. Na, ez a másik, amitől általában megbolondol mindenki.

**SZABOLCS (oktató):** Tehát meg ez egy olyan PDF-on, amiben bele lehet írni, vagy pedig így Excel, amit a PDF-ben.

**REGIO (kapcsolattartó, képernyőt oszt):** Igen, ez egy olyan PDF-on, amiben bele lehet írni, ebbe a PDF-be én bele tudok írni. Tehát én ezt itt meg tudnám csinálni, érted? Ez egy okos PDF. Na most, nekem itt kettő problémám van. Az egyik problémám az, hogy mi megcsináltuk ezt az Excel-t, tudod, ezt a doksit, ami a mi templétük. De ezt gyakorlatilag Laci vagy én, vagy valamelyik szenior kollégánk képletezte be egyenként. És azért nem van a legegyszerűbb képletek. És mi ezt a képletet, és utána játszunk vele, csináljuk, mi honnan jön. És persze, mi ezt úgy csináljuk meg ezeket az Excel-eket, hogy ezekkel levédjük a sorokat, még mutatok neked egy másik Excel-emet. Mondjuk, ugyanúgy bemegyek, és azt mondom, hogy devizem. És nekem ilyen szinten van levédve az Excel-em. 2025-es, azt nézom, hogy van-e frissebb. De mindig legyek ezzel is boldog. És most megmondok egy dokumentumot neked. Az a deviz generál, amit a tervezők használnak, és a tervezőknek a 99 százaléka Romániában egy nagyon buta deviz generált használ, amit kinyert egy törvényből, ami azt szépen beképleteztük, ahogy érnék. És ez ilyen szinten be van képletezve, hogy mit tudom, egy öt objektív, egy öt elemes beruházás, és csak a szürkébe tudok írni, ide már nem is tudok írni, mert be van zárva. Ide tudom, és akkor ez megvan csinálva a struktúrája szépen, és mindent ide átvesz. és ez az a demiz generált struktúra, amit, hogyha a román állami így adna ki ezen a szinten, mindahogy mi megcsináltuk, tehát adna egy mellékletet a törvénytervezethez, akkor sokkal kevesebb hiba lenne a beruházásokban, és az önkormányzatok tudnának élni. Tehát, hogy mondjam, körülbelül a hatékonyságon nőne a román állami beruházásoknak kurvasokat. De hát ők nem így adják ki, mert ezt senki nem csinálja meg. Na, de nekünk ez a templétezésünk, nagyon-nagyon sok mindenünk megvan, és megvan egy olyan logikával, de hogyha én itt valahol egyszer elcseszek valamit, és egy képletet rosszul húzok le, vagy szól a telefonon, vagy valami, és itt egyszer elcsesztem, és valamelyik kollégám nem veszi résztre, akkor persze valamelyen plusz egy ilyen verification sor, meg minden beépítve, de hát az Excel gurúság, az magis dolog, de már kezdem úgyni. És nem is vagyok igazi Excel gurú, én csak ilyen fake Excel gurú vagyok. Volt egy igazi Excel gurú koréganőm, de ő már nincs itt. Na, de azért sok mindent megtanultunk tőlük, úgyhogy rendben. De most az a bajom ezzel, hogy most újra nekiugrunk egy ilyen nagy pályázati, bármikor ősz mondjuk, hogy le akarunk adni tömegesen pályázatot, 10-20 projektet, mi ezt mindig letemplétezzük. De ezt mondom, csak és kizáról valóan valaki tudja csinálni, akinek van egy 5-10 éves tapasztalata ebben a szakmában, és tudja, hogy mit kell csinálni. Ezt hiába adomod, hogy egy kezdők eszen nem fogja megérteni. Na, nekem ez a templéttesítés lenne még egy rohadt nagy segítség, hogy megmondom neki, hogy figyelj, így néz ki egy devész, és kérlek szépen az általa megadott költségvetésre csinálj egy ilyen templétet.

**SZABOLCS (oktató):** Mármint, hogy tölts ki ezt a templétet. Nem.

**REGIO (kapcsolattartó, képernyőt oszt):** Csinálj egy templétet egy új kiírással. Mit mutattam neked? Mutattam neked ezt pillanat. Mutattam neked ezt. Ezzel régebb színvilágában is ugyanilyen volt, mint ez. Csak igazából csak a színvilágot cserélte ki a támogatóhatóság. Úgyhogy mi a régi templétet, ami 2010-en valamikor felépítettünk, azt már nem cseréltük ki színvilágba is, mert jó volt. Na, de én azt szeretném, hogyha ad ő egy ilyet, egy ilyen opos PDF-ed, akkor ennek alapján az én templétemből csináljon egy akár jobb, egy jobb templétet, kiszűrve az esetleges hibáimat, bevezetve esetleg egy-két jobb képletet, egy-két instrukciót, hogy én hogy tudom kihozni a beruházás pluszosra, mit tudok ezzel kezdeni. Tudom, hogy erre már meg kell találni egy agentet, csak így dobom neked a problémákat, hogy mi mivel küzdünk. A legalapabb probléma, a dokumentumot kiolvasni, és egy éppkézláb Excel-be, vagy valamilyen formával áttenni, hogy az használható legyen. Az volt a legelsően mondhatatlan. A második probléma, amit mondtam neked, az az, hogy és talán ez a legáltalánosabb. A második problémám, ez a templétek, megfelelő kezelése.

**REGIO résztvevő:** Jó, figyelj fel!

**REGIO (kapcsolattartó, képernyőt oszt):** A harmadik problémám, és akkor el is engedem itt a mondandómat, az, amit te is mondták, hogy hogy építünk fel egy pályázatot, csak ugye mi elviekben ebben, hogy egy pályázat, hogy építünk fel. A pályázat az a, mit evékenységben mondtam, 10%-a a pályázatleadás. Mi elviekben abban, hogy még a Visby profik vagyunk, de kibázunk azért nincs. És igazából ott nem is az a kérdés, hogy a pályázatot meg tudja írni, mert adom a kiírást, adom a feladatot, és akkor azt, hogyha jól promptolom, még akár egy csetformátumban is sokat ki tudok hozni belőlem.

**REGIO résztvevő:** Igen.

**REGIO (kapcsolattartó, képernyőt oszt):** az is fontos, de hogy én például külön, például az egy jó kérdés, hogy minden egyes pályázat kírása érdemes, hogy külön agentot építeném, vagy egy nagy pályázatíró agent hozza össze a tudást, vagy hogy kezelni.

**SZABOLCS (oktató):** Te figyelj, ez a haladó képzés lesz, nem a mester képzés. Tehát az agenteket nem fogunk írni, mert az egy túl komplex valami. Viszont neked azt lehet tudom mondani, hogy érdemes agentot írni, mert van egy merev struktúrátok, amitre meg lehet tanítani egy agentot. Én például simán csinálnék egy agentot, amelyik írsz indexel, tehát lokálisan azt a file tömeget, amit tud lehoz, az gyorsan beindexeli egy agentot, gyorsan tudjon benne keresni. Ez az egyik. A másik pedig, hogy egy agentot be lehet tanítani, mi a struktúrája. Tehát úgy, ahogy ti is a szenyorjaitokat betanítjátok meg a juniorjait, van gyakorlatilag egy ilyen szabálykönyv, hogy hogyan kell kinézzen egy struktúra, és milyen betűtípust használsz meg minden, akkor legyen egy agent, amelyik lektorál például, és meggyőződik róla, hogy minden ugyanabban a struktúrában van-e, vagy minden egyes dokumentum, amit generáltok, az megfelelője. Tehát például egy ilyen lehetőbe fogok hozni, akkor generálunk egy dokumentumot, azok alapján, a szabályok alapján, amit te megosztasz velem. Ezen kívül pedig egyáltalán szabályokat követni, hogy hogyan lehet szabályokat felismertetni és követni. Ez a haladó képzésen is rendben lesz, tehát itt fognak bejönni a markdown file-ok, ha elküldöd nekem ezt a szabálykönyvet, egy markdown file-t fogok bele lecsinálni, meg a meglévő struktúrátokat valamilyen szempontból letükrözöm, és megmutatom, hogy én hogyan használnám azon a struktúrán azt. Tehát akkor itt az Excel-lel látom, hogy itt jól lenne valamiket behozzak, amit az Excel-be lehet csinálni. Tehát amit ti a mesterképzésen láttatok, hogy én miket csinálok az Excel-be, valamit így behozni a haladóba is, hogy hogyan lehetne esetleg valamit. Csak nagyon komplex volt, amit mutattál. Tehát ez egy olyan valami, hogy az én statisztikáimat ahhoz, hogy komplexül megcsinálja, ahhoz kellett dolgozok egy olyan napot kb. Vagy másfél napot úgy, hogy én a mestere voltam annak a statisztikának. Tehát most a kérdés az, hogy mit tudok nektek mutatni, hogy négy óra alatt átmenjen, vagy eszközöket kell mutassak nektek, amiből ti majd összerakjátok azt, hogy ti hogyan fogjátok tudni az eszközöket használva saját magatokat oktatomatizálni.

**REGIO (kapcsolattartó, képernyőt oszt):** Szerintem is, illetve úgy kellene az egészet megcsináljuk, hogy legyen, tehát nem csak ledarálod, most érsz jól, hanem legyen egy olyan lehetőség, hogy az egyszerűbb, butább kérdéseketre is legyen egy ilyen tényleg szabadabb, kérdezfeleleg dolog. Illetve úgy kellene elinduljunk, hogy milyen, én holnap reggel nekik elfogjak, és meg kell vegyem a csapatnak a CloudPro-t, mert még nem vettük meg. Még mindenkinek csehlt jvd. És akkor milyen usert vegyünk?

**SZABOLCS (oktató):** Tehát kell az Enterprise, most nem tudom mi a neve, de hogyha is le megosztod a képernyőjét, megnézhetjük. Mindenkinek kell egy hozdolláros.

**REGIO (kapcsolattartó, képernyőt oszt):** Én megosztottam.

**SZABOLCS (oktató):** Bocsánat, a Cloud oldalára menjünk fel, és hogy milyen plánek vannak.

**REGIO (kapcsolattartó, képernyőt oszt):** Mindenkinek a Cloud-omba? Csak én most mihol is vagyok.

**SZABOLCS (oktató):** Ott a három csík a jobb felsősorokban. Jaj, jó, oké. Oké, és akkor ott van egy olyan, hogy a profilodnál.

**REGIO résztvevő:** Van egy olyan.

**SZABOLCS (oktató):** Ott alul a profilodnál írja, hogy Pro. Kattints rá. Igen. És akkor van egy upgrade plán. Jó, itt lássuk csak a Max. az, igen, és Team and Enterprise. Van felül egy olyan tab. Jó, és akkor a Team. Predictable usage per seat. Igen, gyanítom, hogy itt a Team ke. All cloud features plus more usage than Pro. Tehát ez a 18 eurós lesz nektek a tiétek, és azt mondja, hogy get Team plan.

**REGIO (kapcsolattartó, képernyőt oszt):** Csinálhatom, vagy csinálom?

**SZABOLCS (oktató):** Hát akár még csinálhatjuk is, lássuk csak. És akkor azt mondjuk, hogy van, ha öt standard seat-et veszel, akkor az adjust seat-nél be tudod állítani, hányat akarsz venni? itt felhúszik, vagy hányat akartok venni?

**REGIO (kapcsolattartó, képernyőt oszt):** Húszat. Hát igazán 20-an vagyunk, 21-en vagyunk.

**SZABOLCS (oktató):** Jó. Azt jelenti, hogy 500 euró lesz, 534 euró lesz, havonta. És akkor...

**REGIO (kapcsolattartó, képernyőt oszt):** És éreztem, bármikor leállíthatod. Downgrade-jelhetem?

**SZABOLCS (oktató):** Igen. Igen, igen.

**REGIO (kapcsolattartó, képernyőt oszt):** És érdemes, hogy legyen mondjuk 18 és Laci-nak, és nekem legyen egy...

**SZABOLCS (oktató):** Az van, hogy a... én azért csinálnám egybe az egészet, mert én még nem használtam így, de valószínűleg így van, hogy a skill-eket meg lehet osztani. Tehát, hogyha az enter... Tehát ebbe a... Írtok egy saját skill-t tegyük fel, ami a deviznél valamit csinál. Például az egyik dolog, amit szerintem érdemes lenne megtanítani, az az, hogy az Excel-be, tehát hogyha most visszaugrasz gyorsan az Excel-file-odra, valamelyik... Ott az Excel-e nyitva, nézd csak meg az alsósában. Jó. Oké. És ott van a Cloud plugin. Nézd csak meg ott a... Igen. Kattints csak meg. Lássuk, hogy... Mi csinálj? Jó. Most itt beloginol. Jó. Mehetsz next. Most ez mindegy, bármit kiválasz. Hadsz itt itt egy ilyen... kérdőívet akarja, hogy kitöltsd. Van egy skip is. Skip elheted szerintem. Ne töltsük fel az vizet. Jó. Jó. Skip. Meg work across your apps. Jó. Turn on. Kíváncsi vagyok, mit csinál. Jó. Oké. Maybe later. Jó. Na oké. Szóval gyakorlatilag itt most tudsz beszélgetni az Excel-eddel. Itt kellene valami olyasmit tanítsak szerintem, hogy hogyan töltesz ki egy Excel-t úgy, hogy komplex információval, de kevés. Tehát, hogy egy skillt kell építeni valójában, ami felismerteti az Excel-nek a struktúráját, és valami egyszerűen hogyan lehet kommunikálni azzal az Excel, ez a kérdés. Na most, ha megnyomod a slash gombot, tehát, hogyha ott, ahol írja a reply, és csináld ezt a visszaper-t, vagy per-t.

**REGIO résztvevő:** Erre gondolsz?

**SZABOLCS (oktató):** Nem, a másik. Per. Jó. Akkor itt kiugrik egy lista. És az jelenti, hogy itt már vannak dolgok, amiket tudsz csinálni itt belül. Itt a kérdés az, hogy hogyan tudsz egy régió konszáltos skillt csinálni, amelyik elmagyarázza, hogy a 0-1 dap dali az milyen dap, mi az értelme annak. Mert ha tudja az értelmét, akkor könnyebben tudja kitölteni adatokkal. Úgyhogy én például ezt csináltam, hogy az én saját Excel-emet úgy töltöm ki a statisztikámat, hogy elmagyarázom egy skill-be, hogy milyen lépések vannak, hogyan kell kitölteni, és akkor egy fájt csatolok hozzám, mivel mindenféle nyers adat benne van, és automatikusan meg is kitölti. Például egy ilyesmit hasznos lehetne nektek, mit szólsz hozzá?

**REGIO (kapcsolattartó, képernyőt oszt):** Szerintem abszolút igen. Abszolút.

**SZABOLCS (oktató):** Ilyen skill-eket meg tudsz osztani. Tehát, hogyha egy ilyen Enterprise-on belül vagy, akkor az egész csapattal megírtok egy skill, és mindenki ugyanaz a skill tudja használni, és tudjátok verziózni. Úgyhogy ahhoz, hogy egy ilyet meg tudjak mutatni nektek, vagy az van, hogy okozom, vagy hogy csináljuk. Mert az is lehet, hogy nekem is érdemes lenne most egy ilyen licenszet vásárolni egy hónapra, és után aztán kiraktok, hogy írjak én nektek egy skillt, és akkor meg tudom osztani veletek. De az annyi egyeztetést igényel őszintén szóval, nem vagy benne biztos, hogy lesz időm erre az egész csütörtökig. De minden esetem ez a lényege. Ez a lényege, hogy meg tudsz osztani skill-eket nektek. Csapaton belül az a fontos, hogy meg lehessen osztani skill-eket.

**REGIO (kapcsolattartó, képernyőt oszt):** Abszolút. Meg, hogy az agentek a csapaton belül dolgozol a többiekkel is.

**(azonosítatlan):** Igen.

**REGIO (kapcsolattartó, képernyőt oszt):** De én építek egy agentet, mondjuk egy... olyan agentet, aki üzleti termeket ír a percse típusú pályázatokra, akkor azt az agentet tudja használni a többi kollégát is.

**SZABOLCS (oktató):** Igen. Ezt úgy fogjuk tudni megcsinálni, szerintem, amúgy az én javaslatom, hogyha visszamész a 5 browser-edhez, ahol a harmadik ikon, vagy a negyedik ikon, ott az a sárga ikon.

**REGIO (kapcsolattartó, képernyőt oszt):** Jaj, hogy írják a rózban, ugye?

**SZABOLCS (oktató):** Nem, nem. Alulról az a sárga ikon, a negyedik balról. Alulról. Tehát a File Explorer.

**REGIO (kapcsolattartó, képernyőt oszt):** Ja, időm.

**SZABOLCS (oktató):** Igen, igen. Jó. Igen. Szóval, struktúrátokban van egy olyan, hogy 00 general info például. És el tudnék képzelni például, vagy akármelyiknél, ha... Tehát oda akarok kijutni, hogy egy olyan foldert kellene csináljunk, ami ugyancsak beépül a tiv hierarhiátokba, de párhuzamosan létezik a mostani hierarhiába, tehát nem módosít rajta, és ebben lennének a markdown file-ok, amelyek a szabályokat tartalmaznák. Tehát az AI gyakorlatilag ezt menne is, és identifikálná, automatikusan menne is, keresne benne, és tanulna meg újabb és újabb feladatokat, ott annak függvényében, hogy éppen milyen feladatot adtunk ki neki. Tehát itt kellene most valami okos dolgot kitaláljunk, hogy ez mi is legyen pontosan. Kb. úgy képzeld el, hogy amikor megosztjuk majd ezt a foldert az AI-jal, akkor van ez a cloud.md file, amit mindig először elolvas. Ez a markdown file, ez gyakorlatilag általános instrukciók, hogy hogyan kell értelmezni ezt az egész folder struktúrát, vagy nem tudom, hogyan kell értelmezni bármit is. És gyakorlatilag egy szabálykönyv, amit röviden, tegyifel 150 sorba leírom. De kb. úgy képzeld el, mint a régi kalandkönyvekben, hogy ilyent is lehet csinálni, hogy figyelj, itt van a struktúra. Ha ezzel a projekttel akar zolgozni, ide menj, ha azzal a projekttel ide menj, ha azzal a projekttel ide menj, ha bemész abba a foldertbe, akkor egy újabb cloud.md várja, amit megint, hogyha elolvas, akkor megint kap plusz információt, és gyakorlatilag automatikusan az agent tud ugrálni a bármilyen komplexitású folder hierarhiába, és újabb és újabb dolgokat tanulhat meg majd a projektekről. Tehát a végén már oda fogunk eljutni, hogy amikor a Terézia projekthez érkezünk, akkor abban a pillanatban várja majd ott is egy cloud.md, és akkor is ott várja egy leírás, amit elolvasva egyből tudja, hogy mit is csinálunk a Terézia projekten. Például, és akkor itt lehet szabályokat meghatározni, hogy általános szabályokat is, és specifikus szabályokat is a projektre. Úgyhogy most kell egy kicsit gondolkozzak, hogy mit lehetne esetleg, hagyalok rajta, hogy holnap megcsengetlek, hogy például milyen ötletein vannak.

**REGIO (kapcsolattartó, képernyőt oszt):** Jó, persze.

**SZABOLCS (oktató):** De ha ennek a mesterévé váltok, tehát ha megértitek, hogy hogyan lehet a markdown fájlokat használni, úgyhogy ne zavarja a jelenlegi struktúrát meg egyáltalán, hanem mondjam úgy, hogy mellé párhuzamosan bekerül, akkor az agenteket lehet tanítani mindenféle komplexzologra. És ha most elküldöz nekem ezeket a fájlokat, például maga az a fájl, ahol leírtad a kollégáknak, hogy mit szabad és mit nem szabad, hogy hogyan kell kinézni egy dokumentum, és milyen folder struktúrát kötelezően kell követni. Ez tipikusan egy valami, amit egy agentnek kell elmagyarázni. Hogy ő tudja, hogy milyen is egy ilyen folder struktúra. Úgyhogy, és ehhez hasonló szabályotok van még gondolom sok.

**REGIO (kapcsolattartó, képernyőt oszt):** Azt van.

**SZABOLCS (oktató):** Úgyhogy ezeket a szabályokat kell átvinni markdown formátumban, mert az agentek ezek pillanatok alatt meg fogják érteni. Miközben navigálnak, egyből olvassák, teszik, veszik, tehát gyakorlatilag egy ilyesmit kéne felépíteni. És most gyakorlatilag arra kéne valahogy megtanítsalak titeket, hogy ti, akik a mesterei vagyotok ennek, hogyan tudjátok alkalmazni ezt a saját világotokba. Nem pedig konkrétan megépítsek valamit.

**REGIO (kapcsolattartó, képernyőt oszt):** Szerintem is az van, hogy tényleg, hogy mi hogy alkalmazzunk. Mert nagyon színes és többféle projekt, amivel foglalkozunk. Illetve tudod, mivel esik gondolom, hogy azért nem tudok mindent dátteni Magdan fájban, mert megvannak ezek a külső hatások, és hogy letöltem az e-licitáciával és a CEAP oldaláról a dokumentumot, nem tudok így kezdeni. De nem tudom így felhívni az in-service-t, hogyha jöttet ajánlatot, meg a viaduttot, hogy tudod, mint adjátok ide a dokumentumokat, mert elvisz a DNA holnap.

**SZABOLCS (oktató):** Persze, persze, persze. Nem, nem, ezek a dokumentumokat kb. úgy kell elképzelni, tehát, hogy olyan, mintha a belső szabályaitok min-mardámban lennének, és minden, ami kívülről érkezik, az olyan formátumban, amilyenben van. És akkor, hogy akaratlag az agenten, amikor nyitsz egy új session-t, azt mondod, hogy a mai nap a Terizia projekten szeretnék dolgozni. És ő automatikusan megy, pak-pak-pak, megy a folderbe ahhoz, ahol a Terizia projekt van, elolvassa a cloud.md-t, elolvassa a szabályokat, stb. és akkor megkérdezi, mit szeretnél csinálni. És azt mondod, hogy szeretném, hogyha kicsit a devizekkel dolgoznák. Ő automatikusan tudja, hogy melyik a deviz oda megy, és azt mondja, mit szeretnél a devizekkel kapcsolatban. És akkor, mert tudja editálni az Excel, tudja értelmezni, statisztikát tud belőle számolni. Itt egy kicsit problémás az, hogy a scannel dokumentumok, azok mivel képek ezért problémás. De megnézem, kíváncsi vagyok, mit fogok tudni kiszedni belőle. És tipikusan olyan repetitív feladatok a statisztika számolás, vagy frissítése egy dokumentumnak, vagy olyan dolgok, amik ilyen elmagyarázhatóak, és megtaníthatóak, aztán meg is lehet tanítani. Hogyha valami ilyesmit kéne, megtanítsak nektek, hogy hogyan navigáljatok gyorsan, hogyan hozzatok új szabályokat, hogyan lehet automatikusan a repetitív Excel-eket kitölteni. Például én számlát generálok vele, és hány órát dolgozott rajta egy pár személy, és pák, így generál nekem egy új számlakísérővel egy Excel-t, aminek megvan a templétje, hogy hogy néz ki. Tehát, hogy ilyesmiket fogok akkor, úgyhogy én akkor nem bánnám, hogyha még, és mennem kell sajnos, de hogy rászánnál erre egy kicsi időt. Végig gondolnád, hogy egy kicsi szűk-kicsi, mert tényleg nagyon sok minden volt. Igen, ezt a videót is majd meg fogom nézni, és megpróbálok, megpróbálok mintázatokat kinyerni belőle, de hogy próbáljuk meg atomizálni a feladatokat, hogy olyan feladatot kapjunk, amit, hogyha bemutatok nektek, hogy hogy kell, akkor egyből bekattan. A szkilleket mindenképpen meg kell tanítsam, hogy hogyan lehet szkilt írni, mi is egy szkill pontosan, és hogyan lehet ezt használni, hogyan lehet excelekbe szkilleket meghívni, és mi is az előnye ennek. És esetleg, például egy template Excel-t, és egy kitöltött Excel-t, és amivel kitöltött. Tehát például egy ilyent, hogyha bemutatnék nektek, tehát küldesz egy template-et, ami üres, egy kitöltött változatot, ilyen, amikor tele van, és egy másik Excel-t, hogy miből töltötted ki ezt például. Egy ilyet meg tudok csinálni szerintem, ha lenne.

**REGIO résztvevő:** Oké. Jó.

**REGIO (kapcsolattartó, képernyőt oszt):** Jó. Azt mondokatom, hogy valószínűleg most el kell mennem egy picit, de azt mondokatom, hogyha ezzel reggel korán foglalkozunk, és akkor küldöm az jó.

**SZABOLCS (oktató):** Akkor is elég. Ma este már nem fogok vele foglalkozni. Holnap fogok.

**REGIO (kapcsolattartó, képernyőt oszt):** Jó, ezért kérdeztem, hogy most szervezzem át a programomat, hogy inkább...

**SZABOLCS (oktató):** Nem, nem, ráír holnap. Tehát, hogyha ilyeneket küldesz nekem, akkor megpróbálok kiszedni mintázatokat, és összerakni egy specializáltan anyagot nektek, ami... Jó, de alapvetően...

**REGIO (kapcsolattartó, képernyőt oszt):** Alapvetően ne gondolt, tehát, hogy szerintem az alapvetően a haladó képzésen, vagy a bíziktől haladóig tartó képzésen, én nem voltam haladó képzéset, de így próbálom visszavezetni, hogy mi lehet. De a bíziktől haladó képzéseden, ami van, az biztosan nagyon hasznos.

**SZABOLCS (oktató):** Igen, abszolút, abszolút.

**REGIO (kapcsolattartó, képernyőt oszt):** Biztosan nagyon hasznos. Csak azt akartam elkerülni, hogy ne azzal induljon, tudod, hogy egy pályázatot hogy kell megírni, mert nem biztos, hogy ez a mi alap problémánk, hanem... Persze.

**SZABOLCS (oktató):** Persze, tehát a haladónak is a célja az volt, hogy legyen egy történet, de arra a történetre egy csomó minden ilyen eszközt felfűztem, mert sokkal könnyebben figyel valaki, hogyha valamit elindul, és valahova megérkezik egy történet által.

**REGIO (kapcsolattartó, képernyőt oszt):** Persze, persze, persze, persze, persze. Abszolút. Abszolút csak, hogy azért nagyon-nagyon sok régen, tényleg csak cseppként használja és kész.

**REGIO résztvevő:** Jó, jó, oké.

**REGIO (kapcsolattartó, képernyőt oszt):** Ugyanúgy, hogy én is csak cseppként használtam, maximum jobban promkoltam, mint Mari néni ennyi.

**SZABOLCS (oktató):** Ja, pont, pont. Szuper. Jó, figyelj, akkor a haladóba azt fogjuk megtanulni az alapokat, mi is a cloud cover-k, mi is a... hogyan dolgozunk a fájrendszeren, hogyan kötjük össze ezt a Microsoft 300, vagy a OneDrive-val, mi is egy markdown file, hogyan tudunk navigálni, mi is egy skill, és akkor bizonyos műveleteket Excel-be végzünk, PDF-eket generálunk. Megnézem, mi fér még vele, kb. ilyesmiket.

**REGIO (kapcsolattartó, képernyőt oszt):** Jó, és egy utolsó dolog a struktúra kapcsán, úgyhogy mármint az egész képzésünk kapcsán, mi elvilegben úgy lettük be, hogy 11-re, vagy fél 11-re mindenki érkezik, tehát 11-től el tudjuk kezdeni.

**REGIO résztvevő:** Jó.

**REGIO (kapcsolattartó, képernyőt oszt):** ellenben be kellene itt tassunk, szerintem, mert megérkezik mindenki, elkezdjük, be kellene itt tassunk 12-től 30-tól egy rövid bráncs szünetet, és utána folytassuk.

**SZABOLCS (oktató):** Jó.

**REGIO (kapcsolattartó, képernyőt oszt):** Mert ez így működőképes neked?

**SZABOLCS (oktató):** Persze, persze tudok. Én azt a napot arra szántam, tehát már mint, hogy nyilván reggel még valamit fogok csinálni, ilyen-olyan dolgot, de utána már nem hiszem, tehát ötig simán ott tudok maradni, pláne, hogy én is keresztúron vagyok, tehát ez a vicces, hogy pont itt vagytok, úgyhogy betpontbiciklivel fogok menni.

**REGIO (kapcsolattartó, képernyőt oszt):** Helyes. Oké, köszi nagyon szépen. Szia. Szia, szia.

