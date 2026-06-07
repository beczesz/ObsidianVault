# Vox Humana — Mély Honlap-analízis

**Forrás:** https://voxhumana.ro/  
**Dátum:** 2026-05-03  
**Platform:** Drupal 9 + Bootstrap 3 + Pegazus egyedi téma

---

## 1. Információs architektúra

A jelenlegi oldal 7 menüpontból áll: Címlap, Rólunk, Orgonaépítés és restaurálás, Alkatrészgyártás, Csapatunk, A műhely, Kapcsolat.

A főoldal egyszerre próbálja bemutatni az összes területet, de a tartalom hierarchia elmosódott. Az oldal szekvenciája: carousel → kategória gombok → portfólió grid → csapat → footer. A legnagyobb probléma az, hogy nincs egyértelmű értékajánlat (value proposition) vagy hero szekció szöveggel — a felhasználó 6 db fekete-fehér workshop fotót lát, de nem érti rögtön, mi ez a cég és miért különleges.

A navigáció horizontálisan túl sok elemet tartalmaz (7 menüpont), ami mobilon különösen problémás. Az Orgonaépítés és restaurálás + Alkatrészgyártás két fő szolgáltatási irány jól elkülönül, de a Csapatunk, A műhely és a Rólunk tartalmak átfedhetők lennének.

**Javaslat:** Összevonni a navigációt 4-5 elemre (Főoldal, Szolgáltatások [dropdown], Referenciák, Rólunk, Kapcsolat). Hozzáadni egy egyértelmű hero szekciót szöveggel.

---

## 2. Tartalmi hierarchia

A jelenlegi sorrend problémás:

1. **Header + logó** — rendben, de a logó csak szöveg (VOX HUMANA), nincs vizuális brand jel a navbar-ban
2. **Carousel** (6 slide) — túl sok, lassú, a képek mind hasonló tónusúak (fekete-fehér műhely fotók). Nincs szöveges overlay (csak a logó ikon)
3. **Két kategória kör** — jó koncepció, de a kör alakú thumbnailek nagyon kicsik és nehezen felismerhetők
4. **Portfólió grid** (6 elem) — ez a legerősebb tartalom! Gyönyörű templomfotók, de nincs kontextus, leírás, vagy CTA
5. **Csapatunk** (2 ember) — fontos a bizalomépítéshez, de nincs pozíció, bio, vagy személyes szöveg
6. **Footer** — sok jó info (cím, telefon, e-mail, rövid bemutatkozás), de a navigáció sekciója alig tartalmaz linkeket

**Javaslat:** Erős hero → rövid bemutatkozás → referenciák (ez a legerősebb content!) → szolgáltatások → csapat + műhely → kapcsolat CTA

---

## 3. Vizuális ritmus

Az oldalon a vizuális ritmus egyenetlen. A carousel hatalmas (teljes képernyő), utána hirtelen kis kör ikonok nagy fehér térben, majd egy sűrű 3x2-es grid, végül csapat fotók. A vizuális "levegő" (whitespace) nincs tudatosan kezelve — néhol túl sok, máshol túl kevés.

A szekciók közötti átmenet nincs jelezve — nincs szín- vagy háttérváltás, szeparátor vonal, vagy más vizuális kapocs. Minden fehér háttéren van, kivéve a footer (sötétszürke) és a portfólió szekciót.

**Javaslat:** Váltakozó szekció-hátterek (fehér/világosszürke/krém), konzisztens padding, és szeparátorok vagy gradiens átmenetek.

---

## 4. Képek minősége, méretezése, vágása

**Pozitív:**
- A carousel fotók nagyfelbontásúak (2048x1356px), ami jó quality
- A portfólió (referencia) fotók professzionálisak — gyönyörű templomi orgonaképek
- A csapatfotók természetesek, barátságosak

**Negatív:**
- A carousel képek MIND fekete-fehér/szürke tónusúak — ez monoton hatást kelt
- A kategória ikonok (orgonaépítés, alkatrészgyártás) túl kicsik (kör alakban vágva, ~150px)
- A portfólió grid képek 394x261px-esek, ami rendben van, de nincs hover effektus
- Nincs optimalizálás: a nagy carousel képek ~400KB-osak, ami lassítja a betöltést
- A csapatfotók háttere eltér (sárga vs. sötét) — nem konzisztens

**Javaslat:** 1-2 erős, színes hero kép; képek WebP formátumba konvertálása; konzisztens csapatfotó háttér; a kategória képek növelése és modernizálása.

---

## 5. Tipográfia

A jelenlegi betűtípusok:

- **Raleway** (300, 400, 700) — a navbar menüpontokhoz és fejlécekhez
- **Montserrat** (300, 400, 700) — a footer címekhez, néhány UI elemhez
- **Roboto** (300, 400, 700) — alapértelmezett body szöveghez

Ez 3 font, ami redundáns és lassítja a betöltést. A Raleway all-caps menü betűk rendben vannak, de a spacing túl szűk. A body szöveg Roboto 300-ban (light) nehezen olvasható kis méretben.

A `h1.page-header` ("Orgonaépítés és restaurálás - Alkatrészgyártás") túl hosszú és kényelmetlen elsődleges feliratnak.

**Javaslat:** 2 font max: Raleway (display) + Roboto (body), vagy egyetlen prémium serif font (Playfair Display, Cormorant Garamond) párosítva egy sans-serif body fonttal. Ez jobban illene az orgona/zene/hagyomány témához.

---

## 6. Színek

A jelenlegi színpaletta rendkívül szegényes:

- **Fehér** (#fff) — háttér
- **Szürke** (különböző árnyalatok) — szöveg, navbar
- **Sötétszürke** (#333-#444) — footer háttér
- **Fekete** — szöveges elemek
- **Nincs akcentszín!** — teljesen hiányzik bármilyen márka-szín

A logóban látható egy piros/bordó elem, de ez sehol nem jelenik meg az oldalon.

**Javaslat:** A logó piros/bordó elemét (#8B0000 vagy hasonló) felvenni akcentszínnek CTA gombokhoz, hover effektekhez, szeparátorokhoz. Egy meleg, fás tónust (pl. #8B6914) használni szekció-háttérekhez, ami az orgonák faanyagára utal.

---

## 7. Formák, gombok, kártyák, szekciók

- **Gombok:** Gyakorlatilag nincsenek. A cookie banner gombon kívül nincs CTA gomb az egész oldalon
- **Kártyák:** A portfólió grid elemei nem igazi kártyák — nincs shadow, border, hover effektus. Csak kép + szöveg
- **Szekciók:** Nincs vizuális elválasztás szekciók között
- **Formák:** Minden szögletes, nincs border-radius, nincs modern alakzat
- **Carousel vezérlők:** Láthatatlanok (csak screen-reader szöveg)

**Javaslat:** Modern kártyák enyhe shadow-val és hover-zoom effektussal; világos CTA gombok ("Referenciáink megtekintése", "Kapcsolatfelvétel"); szekciók vizuális elválasztása háttérszínekkel.

---

## 8. Mobil UX

A jelenlegi oldal Bootstrap 3 alapú, így alapszintű reszponzivitás van (col-xs, col-sm, col-lg). Azonban:

- A carousel teljes képernyős, ami mobilon OK, de nincs swipe támogatás
- A kategória körök egymás alá kerülnek, de nagyon kicsik maradnak
- A portfólió grid 1 oszlopossá válik, de a képarány megmarad (szélesen nyújtott)
- A footer 4 oszlopa egymás alá kerül, ami hosszú scrollolást eredményez
- A hamburger menü Bootstrap 3 alapú — működik, de elavult

**Javaslat:** Modern mobil menü (slide-in vagy overlay); touch-barát carousel (swipe); nagyobb kategória gombok mobilon; footer accordion vagy kompaktabb elrendezés.

---

## 9. Konverziós pontok

**Jelenleg NINCSENEK konverziós pontok!** Ez a legnagyobb probléma.

- Nincs "Ajánlatkérés" vagy "Kapcsolatfelvétel" gomb
- Nincs telefon/e-mail a headerben
- Nincs CTA a szekciók végén
- A "Kapcsolat" menüpont az egyetlen konverziós lehetőség, de az is 7 kattintásból a 7.

**Javaslat:** Telefon + e-mail a header tetejére; sticky CTA gomb ("Ajánlatkérés"); minden szekció végére "Tudjon meg többet" vagy "Vegye fel a kapcsolatot" CTA; a footer-ben kiemelni az elérhetőségeket.

---

## 10. Elavult vagy gyenge elemek

- **Bootstrap 3** — a framework 2013-as, már Bootstrap 5 az aktuális
- **Drupal 9** — maga a CMS is régi (Drupal 11 az aktuális)
- **jQuery alapú carousel** — nincs CSS animation, nehézkes
- **EU Cookie Compliance** modul — működik, de elavult design
- **Google Tag Manager** — script betöltve, de valószínűleg nem aktívan monitorozott
- **Copyright 2022** — 4 éve nem frissített jogi szöveg
- **Nincs SSL tanúsítvány hiba, az jó** — HTTPS aktív

---

## 11. Mit érdemes megtartani az eredeti karakterből

- **A logó (VOX HUMANA)** — erős, felismerhető tipográfiai brand
- **A logó ikon** (kör alakú, kereszttel és VH betűkkel) — egyedi, szép
- **A fekete-fehér műhely fotók hangulata** — művészi, kézműves érzetet kelt. De használjuk kiegészítésként, ne fő képekként
- **A portfólió/referencia szekció** — ez a legerősebb tartalom, ezt kell kiemelni
- **A csapat fotók** — személyes, barátságos
- **A cégbemutatkozó szöveg** — rövid, informatív, megtartandó

---

## 12. Modernizálási irányok

### Irány A: Elegáns/Prémium
Serif tipográfia (Playfair Display), meleg fa-tónusok és arany akcentek, teljes szélességű hero kép természetes fényű orgonafotóval, finoman animált szekciók, prémium luxury érzet. Mintha egy tradicionális kézműves műhely high-end bemutatkozó oldala lenne.

### Irány B: Modern/Kreatív
Sans-serif tipográfia, bold kontrasztos layout (nagy képek + minimál szöveg), parallax scroll effektusok, interaktív galéria, videó integráció, hangminta lejátszás lehetőség. Az orgona hangzásvilágát vizuálisan is megjelenítő, immerzív élmény.

### Irány C: Storytelling/Bold
Vegyes tipográfia, narratív scrollozás ("Így épül egy orgona" story), timeline szekció a cég történetéről, előtte-utána galéria restaurálásokról, testimony-k (ajánlások), erős CTA-k. A mesterség és a történet áll középpontban.

---

## Összefoglalás — TOP 5 Prioritás

1. **Hero szekció értékajánlattal** — Az oldal jelenleg nem kommunikálja 3 másodpercen belül, miről szól
2. **CTA és konverziós pontok** — Teljesen hiányoznak
3. **Színpaletta és vizuális identitás** — A logó bordó/piros elemét be kell emelni az egész designba
4. **Referenciák kiemelése** — Ez a legerősebb tartalom, prominensebb helyre kell kerüljön
5. **Mobil optimalizálás** — Modern, touch-barát megoldásokra van szükség
