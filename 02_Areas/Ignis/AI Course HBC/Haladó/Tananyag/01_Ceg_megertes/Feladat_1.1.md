# Feladat 1.1 — Káoszból rendszer (egyetlen prompttal)

> **Idő:** 20-25 perc · **Mód:** mindenki saját laptopon, párhuzamosan · **Eredmény:** rendezett mappa + kivonat + a Cowork „memóriája"

---

## Szituáció

Márton, az ügyvezető a második kávéjával odajön hozzád:

> *„Figyelj, csütörtökön lesz egy meeting egy pályázati tanácsadóval — valami AFM-es elektromos járműflotta pályázat, elég sok pénz. De ahhoz hogy értelmes dolgokat mondjak neki, tudnom kéne mi a helyzet a cégnél rendszer-szinten. Te tegnap óta nézegetted a fájlokat ugye? Tudnál nekem egy gyors összefoglalót csinálni? És tegyél valami rendet is benne, mert most ez egy katasztrófa."*

Megnyitod a `TransOffice/` mappát: **30+ fájl** vegyesen. Excel ügyféllisták, Word-szerződések, kéziratos cetlik, Ilona régi mappája 200+ fájllal — valószínűleg sok elavult, néhány felesleges, és minden káoszban.

---

## Cél

Ez a workshop **első tapasztalata**. 1 prompt → és a Cowork mindent elintéz:

- Biztonsági másolat a jelenlegi mappáról (mielőtt bármit elront)
- Egy **Kuka** mappa a szemétnek
- Új, rendezett mappa-struktúra (és tényleg át is rendezi)
- Egy **kivonat** számodra arról mit talált és mit csinált
- Egy **`CLAUDE.md`** — a Cowork hosszútávú memóriája a következő sessionökhöz

**Páros dinamika:** ez a fázis kivétel — **mindketten csináljátok** (mindenki saját gépén, saját TransOffice mappával). A következő fázisokban (F2-F6) felváltva ti vezetitek a Cowork-öt, de ez a setup mindenkié.

---

## Hogyan csináld

### 1. lépés — Nyisd meg a Cowork-öt

- Indítsd el a Claude Cowork desktop alkalmazást
- Hozz létre egy ÚJ projektet (vagy nyisd meg a saját TransOffice projektedet)
- Add hozzá projekt-kontextusként a `TransOffice/` mappát a saját gépedről
- Nyiss egy üres új chat-tabot

### 2. lépés — Másold be az alábbi promptot

A következő szürke kódblokk **a teljes prompt**. Jelöld ki, másold (Cmd+C / Ctrl+C), és illeszd be a Cowork chat-mezőjébe (Cmd+V / Ctrl+V):

```
Az új munkatárs vagyok a TransOffice cégnél, ma az első napom.

A TransOffice mappában találod a cégünk összes dokumentumát. Rendetlenség
van — évek alatt gyűlt össze mindenféle dokumentum, és senki nem nézte át
őket.

Légy szíves, segíts rendbe tenni:

1. Először a jelenlegi mappáról készíts egy biztonsági másolatot, hogy
   bármikor vissza tudjam keresni a fileokat.

2. Kezd el egyenként átnézni a fileokat és kategorizálni.

3. Legyen egy Kuka mappa is — abba másolj minden olyan filet, ami szemét,
   elavult, vagy nem releváns.

4. Gyere egy javaslattal, hogy hogyan rendezzük az anyagot, és rendezd is
   el úgy.

5. Készíts nekem egy kivonatot arról, mit találtál és mit csináltál.

Készíts egy CLAUDE.md fájlt is — ez lesz a hosszútávú memóriád. Minden új
munkamenetben elsőként ezt fogod elolvasni.

Ha bármi nem világos, kérdezz vissza.
```

### 3. lépés — Várd meg a Cowork-et

A Cowork ~3-6 perc alatt végigmegy a fájlokon, létrehozza a backup-ot, a Kuka mappát, átrendezi az anyagot, és megírja a kivonatot + CLAUDE.md-t. Közben **figyeld** mit csinál:

- Hány fájlt sorol szemétbe?
- Milyen kategóriákat alkot?
- Hol jelez kérdéses pontot?

### 4. lépés — Nézd át, módosíts

Amikor készen jelez, **nézd át mit csinált**:

- Tényleg ott van a backup? Megnyithatóak a régi fájlok?
- A Kuka mappában nincs-e olyan fájl, amit te megtartanál? (Ha igen, mondd: *„A `[fájlnév]`-et tedd vissza, érdekes lehet."*)
- A kivonat lényegre törő? Olvasd át 1 percre.
- A CLAUDE.md-ben szerepelnek a fontos nevek és prioritások?

Ha valami nem stimmel: **mondd meg neki**. Pl. *„A `Kovacs_Ilona` mappa nagy részét hagyd ott archív szekciónak, ne kerüljön a Kukába."*

---

## Önellenőrzés (a fázis végén)

- [ ] Létrejött a **backup mappa** (`TransOffice_backup/` vagy hasonló)
- [ ] Létrejött a **Kuka mappa** legalább 2-3 fájllal benne
- [ ] A TransOffice/ mappa **új, kategorizált struktúrát** kapott
- [ ] Megvan a **kivonat** (`kivonat.md` vagy hasonló néven)
- [ ] Megvan a **`CLAUDE.md`** — és benne van legalább 4 név (Márton, Enikő, és pár ügyfél/beszállító)

---

## A WOW-pillanat (5 perc bemutatás a párodnak)

Miután mindketten elkészültetek, **5 percig** mutassátok meg egymásnak:

- **Mit dobott a Kukába a Cowork** — egyezett a 2 listátok? Volt valami amit a párod megtartott, te meg dobtál?
- **Hogyan kategorizálta** — másmilyen mappa-fát hozott létre nálatok? Melyik logika tetszik jobban?
- **A CLAUDE.md** — vajon ki került be a „csapat" listába, és kit hagyott ki a Cowork? Megegyeznek a kivonataitok?

Ez a páros-megbeszélés a workshop **első igazi összehasonlítása**.

---

## Tanulás

**Mi történt itt?** Az AI **nem csak válaszolt** egy kérdésre — **átnézett 30+ fájlt, döntéseket hozott, mappákat hozott létre, fájlokat mozgatott**. Ezt egy ember **2 napig** csinálná. És **emlékezni fog** mindenre a következő sessionben is.

**A CLAUDE.md a kulcs.** Ez különbözteti meg a Cowork-öt a ChatGPT-től. A ChatGPT-ben minden chat tiszta lap. A Cowork-ben a `CLAUDE.md` **minden új sessionben automatikusan betöltődik** — emlékszik kik vagytok, mi a céged, mi az aktív küldetés. Ezt **mostantól F2-F6-ig használjuk**.

**A „bízz benne, de ellenőrizd" elv.** A Cowork dönt — de te döntesz a döntéseiről. Ha valami a Kukában van amit megtartanál, **mondd meg**. Az AI a kezed, te vagy a fej.

---

## Mi következik (F2)

A fájlok rendben, a CLAUDE.md megvan. De a napi működésben **nem fájlok a fő probléma** — hanem hogy a meetingekből semmit nem követünk nyomon. Márton közben besüllyed Enikővel egy sürgős meetingre: **vagy ezen a héten beadjuk a pályázatot, vagy lemaradunk**. Az F2-ben a meeting kaotikus transcript-jét alakítjuk át végrehajtható TODO-listává a Productivity plugin-nel.

---

## Időkeret összesen

- A prompt másolása + indítása: **1 perc**
- Cowork dolgozik: **3-6 perc**
- Outputok átolvasása + 1-2 finomítás: **5-7 perc**
- Páros megbeszélés: **3-5 perc**
- Buffer + kérdések: **3 perc**
- **Össze: 20-25 perc**

---

**Verzió:** 2.1 (rövidített, akcióközpontú prompt) · **Korábbi:** v1.0 és v2.0 archiválva a `Műhely/_archivum/01_Ceg_megertes/`-ban
