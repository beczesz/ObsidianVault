# Feladat 1.1 — Káoszból rendszer (egyetlen prompttal)

> **Idő:** 20-25 perc · **Mód:** mindenki saját laptopon, párhuzamosan · **Output:** 3 fájl

---

## Szituáció

Márton, az ügyvezető a második kávéjával odajön hozzád:

> *„Figyelj, csütörtökön lesz egy meeting egy pályázati tanácsadóval — valami AFM-es elektromos járműflotta pályázat, elég sok pénz. De ahhoz hogy értelmes dolgokat mondjak neki, tudnom kéne mi a helyzet a cégnél rendszer-szinten. Te tegnap óta nézegetted a fájlokat ugye? Tudnál nekem egy gyors összefoglalót csinálni? És tegyél valami rendet is benne, mert most ez egy katasztrófa."*

Megnyitod a `TransOffice/` mappát: **30+ fájl** vegyesen — Excel ügyféllisták (3 verzió, mind eltér), Word-szerződések románul, kéziratos cetlik Mártontól, Ilona régi mappája 200+ fájllal, az `arak_2023.xlsx` ami nyilvánvalóan elavult, és egy `lu45pmb3.tmp` ami valószínűleg szemét. **Csütörtökön reggel** — kell egy összefoglaló Mártonnak, kell egy átláthatóbb struktúra, és kell egy „memória" amibe a Cowork minden új sessionben bele tud nézni.

---

## Cél

Ez a workshop **első tapasztalata**. 1 prompt → 3 output:

| # | Output | Mi ez |
|---|--------|-------|
| 1 | **`ceg_attekintes.md`** | 1-2 oldalas strukturált összefoglaló Mártonnak (a csütörtöki meetinghez) |
| 2 | **`CLAUDE.md`** | A Cowork „memóriája" — minden új session ezt először olvassa el |
| 3 | **`javasolt_mappa_struktura.md`** | Hogyan rendezzem át a kaotikus fájlokat — új mappa-fa, mit törlök, mit archiválok |

**A pár dinamikája:** ez a fázis kivétel — **mindketten csináljátok** (mindenki saját gépén, saját TransOffice mappával). A következő fázisokban (F2-F6) felváltva ti vezetitek a Cowork-öt, de ez a setup mindenkié.

---

## Hogyan csináld

### 1. lépés — Nyisd meg a Cowork-öt

- Indítsd el a Claude Cowork desktop alkalmazást
- Hozz létre egy ÚJ projektet (vagy nyisd meg a saját TransOffice projektedet)
- Adj hozzá projekt-kontextusként a `TransOffice/` mappát (ott a saját gépeden)
- Nyiss egy üres új chat-tabot

### 2. lépés — Másold be az alábbi promptot

A következő szürke kódblokk **a teljes prompt**. Jelöld ki, másold (Cmd+C / Ctrl+C), és illeszd be a Cowork chat-mezőjébe (Cmd+V / Ctrl+V):

```
Szia! Az új Operations & Systems Manager vagyok a TransOffice Trade
SRL-nél. Ma az 1. munkanapom. A főnököm (Kovács Márton, ügyvezető)
kávéval az asztalra tette a laptopomat és átadott egy mappát — a
`TransOffice/` projekt-mappa, amit projekt-kontextusként már látsz.

Ez a mappa az anyja (Kovács Ilona, korábbi adminisztrátor) hagyatéka
+ Márton saját jegyzetei. 30+ vegyes fájl van benne (Excel, Word,
PDF, txt), és valószínűleg káosz: 3 különböző ügyféllista, elavult
árak, kéziratos cetlik, duplikált szerződések, egy-két szemét fájl
is (pl. lock/.tmp).

A háttérben sürgető küldetés: csütörtökön egy pályázati tanácsadói
meeting (AFM Mobilitate Verde 2025 — elektromos járműflotta), és
péntekig kell beadni. Márton tudja, hogy nem ismeri saját cégét
rendszerszinten.

Kérlek olvasd át a `TransOffice/` mappa ÖSSZES fájlját (Excel, docx,
PDF, txt — mindent, beleértve az alfápákat is mint Kovacs_Ilona/,
Marketing/, email_exportok/, meetings/), és készíts NEKEM 3 különálló
markdown fájlt:

────────────────────────────────────────────────────────────────
1) ceg_attekintes.md — Strukturált cég-összefoglaló Mártonnak
────────────────────────────────────────────────────────────────

1-2 oldalas, fejezetekre tagolt MD dokumentum az alábbi szekciókkal:

- Cég alapadatok (név, CUI, székhely, vezető, alkalmazottak, profil)
- Pénzügyi helyzet (utolsó 2-3 év árbevétel, eredmény, trend)
- Ügyfélkör (hány aktív, kik a top 5-7, szegmensek, kérdéses pontok)
- Beszállítók (kik, milyen feltételekkel, lejáró/problémás szerződések)
- Jelenlegi rendszerek és technológia (vagy ennek hiánya)
- Azonosított problémák és inkonzisztenciák (eltérő számok, duplikációk,
  elavult adatok — minden tételhez add meg melyik fájl mit mond)
- 3-5 prioritás a csütörtöki meetinghez

Minden állításhoz add meg a forrás-fájl nevét. Ami homályos vagy
kérdéses, jelöld ⚠️-vel.

────────────────────────────────────────────────────────────────
2) CLAUDE.md — A Cowork hosszútávú memóriája
────────────────────────────────────────────────────────────────

Egy ~1 oldalas markdown fájl, amit minden következő Cowork-session
automatikusan elolvas. Tartalmazza:

- Rólam: új Operations & Systems Manager, 1. nap
- A cég: 1 paragrafus a TransOffice-ról
- Csapat: név + szerep + 1 mondat tudnivaló — legalább Kovács Márton,
  Szabó Enikő, Mihaela (külsős könyvelő, románul ír), Béla bácsi
  (telephely-tulajdonos), Bíró Attila (raktárvezető)
- Top ügyfelek (5-7 név)
- Aktív küldetés: AFM Mobilitate Verde pályázat — péntekig beadni
- Szabályok: mire kell mindig figyelnie a Cowork-nek (pl. „az
  arak_2023.xlsx ELAVULT, ne hivatkozz rá aktuálisként", „a
  BicoToner szerződés problémás", stb.)
- Hivatkozott fájlok: 5-8 legfontosabb fájl, melyik mit tartalmaz

────────────────────────────────────────────────────────────────
3) javasolt_mappa_struktura.md — Új mappa-fa
────────────────────────────────────────────────────────────────

A jelenlegi TransOffice/ mappa kaotikus. Javasolj egy ÚJ, tisztább
struktúrát egy markdown fájlban:

- Új mappa-fa (pl. 01_Penzugy/, 02_Ugyfelek/, 03_Beszallitok/,
  04_Szerzodesek/, 05_Marketing/, 06_Meetings/, _Archiv/, ...)
- Melyik létező fájl HOVA kerülne (táblázat: régi fájl → új helye)
- Mit JAVASOLOK TÖRÖLNI (pl. lock fájlok, .tmp, duplikátumok)
- Mit ARCHIVÁLNI (régi de fontos — 2019-es ügyféllista, stb.)
- Mit AZONNAL FRISSÍTENI (pl. árlista)

NE mozgasd ténylegesen a fájlokat — csak javasold a struktúrát egy
MD-ben.

────────────────────────────────────────────────────────────────

Mindhárom fájlt mentsd külön egy új mappába:
TransOffice/01_ceg_attekintes/

Ha valamit nem tudsz egyértelműen, KÉRDEZZ vissza — ne találj ki.
Munkára!
```

### 3. lépés — Várd meg a Cowork-et

A Cowork ~1-3 perc alatt átolvassa a fájlokat és legenerálja a 3 outputot. Közben **figyeld** mit csinál:

- Melyik fájlokat nyitja meg?
- Hogyan rendszerezi az információt?
- Hol jelez ⚠️ kérdéses pontot?

### 4. lépés — Nézd át, módosíts

A 3 fájl elkészül a `TransOffice/01_ceg_attekintes/` mappában. Nyisd meg mindegyiket:

- A `ceg_attekintes.md` Mártonnak szól — ha valami zavaró, mondd: *„Ez a szekció túl hosszú, vágd le felére."*
- A `CLAUDE.md` a Cowork memóriája — ha hiányzik valaki/valami, mondd: *„Hozzá kell adni X-et a csapathoz."*
- A `javasolt_mappa_struktura.md` egy javaslat — nem kell megvalósítani, csak jó-e

---

## Önellenőrzés (a fázis végén)

- [ ] Létrejött mindhárom fájl: `ceg_attekintes.md`, `CLAUDE.md`, `javasolt_mappa_struktura.md`
- [ ] A `ceg_attekintes.md` említi az AFM Mobilitate Verde pályázatot
- [ ] A `CLAUDE.md` tartalmazza legalább **4 nevet** (Márton, Enikő, Mihaela, Béla bácsi)
- [ ] A mappa-struktúra javaslat legalább **5 új kategóriát** ajánl
- [ ] A `ceg_attekintes.md`-ben legalább **2 ⚠️ inkonzisztenciát** azonosítottál

---

## A WOW-pillanat (5 perc bemutatás a párodnak)

Miután mindketten elkészültetek, **5 percig** mutassátok meg egymásnak:

- **Mi volt különböző** a 2 outputban? (kis variancia normális — az LLM nem 100% determinisztikus)
- **Mit írt a Cowork a CLAUDE.md-be amit te is fontosnak tartottad volna?** Vagy mit hagyott ki?
- **Melyik output volt a leghasznosabb?** A `ceg_attekintes.md` (üzleti)? A `CLAUDE.md` (memória)? A mappa-javaslat (struktúra)?

Ez a páros-megbeszélés **1-2 perc** önmagában — de a workshop első igazi „összehasonlítás" pillanata.

---

## Tanulás

**Mi történt itt?** Az AI **nem csak válaszolt** egy kérdésre — **párhuzamosan átnézett 30+ fájlt**, **összevetett 3 különböző ügyféllistát**, **azonosított inkonzisztenciákat**, **strukturált jelentést írt**, és **emlékezni fog erre** a következő sessionben is. Ezt egy ember **2 napig** csinálná — és a végén nem lenne CLAUDE.md memória se.

**A CLAUDE.md a kulcs.** Ez az ami megkülönbözteti a Cowork-öt a ChatGPT-től. A ChatGPT-ben minden chat tiszta lap. A Cowork-ben a `CLAUDE.md` **minden új sessionben** elsőként betöltődik — a Cowork **emlékszik kik vagytok, mi a céged, mi az aktív küldetés**. Ezt **mostantól végig használjuk** F2-F6-ig.

**A mappa-struktúra javaslat.** Nem feltétlen kell megvalósítani — egy AI-jal **bármikor újra-rendezhető** a fájlrendszer. De a *javaslat látása* megérezteti veled, hogy mi szervezett és mi szervezetlen.

---

## Mi következik (F2)

A fájlok rendben vannak. De a napi működésben **nem fájlok a fő probléma** — hanem hogy a meetingekből semmit nem követünk nyomon. Ezután Márton összerándul Enikővel egy sürgős meetingre, és belerobban a kétségbe: **vagy ezen a héten beadjuk a pályázatot, vagy lemaradunk**. Az F2-ben a meeting **kaotikus transcript-jét** alakítjuk át végrehajtható TODO-listává a Productivity plugin-nel.

---

## Időkeret összesen

- A prompt másolása + indítása: **1 perc**
- Cowork dolgozik: **2-3 perc**
- Outputok átolvasása + 1-2 finomítás: **5-7 perc**
- Páros megbeszélés: **3-5 perc**
- Buffer + kérdések: **5 perc**
- **Össze: 20-25 perc**

---

**Verzió:** 2.0 (páros-mód, copy-paste prompt) · **Korábbi:** v1.0 archiválva a `Műhely/_archivum/01_Ceg_megertes/`-ban
