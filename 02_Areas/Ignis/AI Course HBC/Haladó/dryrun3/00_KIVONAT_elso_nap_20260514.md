# Kivonat — Szabolcs első napja a TransOffice-nál

**Dátum:** 2026-05-14
**Készítette:** Szabolcs (új Operations Manager)
**Hely:** `dryrun3/00_KIVONAT_elso_nap_20260514.md`

---

## TL;DR (3 mondatban)

A `dryrun3/` mappa rendetlen volt (36 fájl szétszórva, duplikátumokkal és
személyes kacatokkal keverve), most tematikus struktúrába rendeztem
(00–09 sorszámozott mappák + `_Kuka` + `_TransOffice_eredeti_BACKUP_20260514`
biztonsági másolat). Az AFM Mobilitate Verde 2026 pályázathoz tartozó
2026-08-25-i meeting transcriptjét feldolgoztam: van helyzet-összefoglaló,
ki/mit/mikorra TODO lista, blocker-lista a hiányzó adatokról és egy
kollegális follow-up email Enikőnek. A hosszútávú memóriát a `CLAUDE.md`
gyökérfájl tartja: itt van a cég kontextusa, a kulcs-NPC-k és az aktív
küldetés — minden új munkamenet ennek olvasásával kezdődik.

---

## A) RENDRAKÁS — mit találtam, mit csináltam

### Az eredeti állapot (36 fájl, 4 alkönyvtár)

A gyökérben szerződések, ügyféllisták (3 különböző verzió!), készlet és
ár-Excelek, két meeting docx és egy `lu45pmb3.tmp` (kiderült: bit-azonos
duplikátuma a PaperWorld 2021-es PDF-jének — Word/rendszer-tmp).
Alkönyvtárak: `Kovacs_Ilona/` (vegyes — céges + magán: jelszavak,
beszállítói lista, **receptek**, **unoka-fotó**), `email_exportok/` (6
exportált email), `meetings/` (4 fájl, közte 2 db 2025-02-24-es ami a
felhasználó szerint elhagyható, és 2 db 2026-08-25-i ami az AFM kickoff),
`Marketing/` (egyetlen 2012-es honlapszöveg).

### Backup

Mindenből készült `_TransOffice_eredeti_BACKUP_20260514/` — ezzel bármikor
visszaállítható az eredeti állapot. Ehhez a mappához nem nyúlok ezután.

### Az új struktúra logikája

A felépítés **számozott** (00–09), hogy a Drive-ban / Finderben mindig
azonos sorrendben jelenjenek meg, és az aktív küldetés (`00_AFM_Palyazat_2026/`)
mindig elsőként legyen szem előtt:

| Mappa | Mit tartalmaz | Hány fájl |
|-------|---------------|-----------|
| `00_AFM_Palyazat_2026/` | Aktív küldetés — meeting kimenetek, kritikus dokumentumok | 6 (a meeting felvétel, transcript + 4 új md) |
| `01_Szerzodesek/` | beszallitok/ + ingatlan/ — élő szerződések | 4 |
| `02_Ugyfelek/` | aktuális + archív listák, Ilona ügyfél-jegyzetei, nyitott ajánlat | 4 |
| `03_Beszallitok/` | beszállítói lista (jelölve: "regi_2020", aktualizálandó) | 1 |
| `04_Termekek_es_Keszlet/` | árjegyzék, készlet, rendelési napló | 3 |
| `05_Penzugy/` | éves jelentés (jelenleg csak 2020-2022 — friss kell az AFM-hez!) | 1 |
| `06_Marketing_es_IT/` | 2012-es honlapszöveg (jelölve "REGI" — Márton említette: a honlap szét van) | 1 |
| `07_Email_archivum/` | 6 db exportált email, köztük a kritikus Béla bácsi-válasz | 6 |
| `08_Meetings/` | korábbi (2024-11-05, 2025-01-12) meeting jegyzetek | 2 |
| `09_Belso_dokumentumok/` | jelszavak (BIZALMAS!), Márton + Ilona cetli-jegyzetei | 3 |
| `_Kuka/` | duplikátumok, elavult, személyes — visszahozható | 9 |

### Mi került a Kukába és miért

| Fájl (új neve a Kukában) | Miért |
|--------------------------|-------|
| `lu45pmb3.tmp_DUPLIKATUM_PaperWorld_PDF` | bit-azonos a PaperWorld 2021 PDF-fel (md5 egyezik) — Word/system tmp |
| `meeting_marton_20241105_DUPLIKATUM_root.docx` | a `meetings/` mappában is megvolt, md5 azonos |
| `meeting_marton_20250112_DUPLIKATUM_root.docx` | ugyanaz mint fent |
| `ugyfelek_2019_ELAVULT.xlsx` | 2019-es ügyféllista — az `ugyfelek_aktualis_2025_marton.xlsx` váltja |
| `meeting_recording_20250224_REGI.m4a` | felhasználó instrukciója szerint elhagyható |
| `meeting_transcript_20250224_REGI.srt` | ugyanaz |
| `foto_unoka_2023_SZEMELYES.txt` | Ilona unoka-fotója — nem cégadat |
| `receptek_krumplis_SZEMELYES.docx` | Ilona receptjei (krumplis tészta, kürtőskalács) — nem cégadat |
| `szamlak_2023_URES_csak_README/` | csak egy README volt benne, valódi számlák nincsenek itt |
| `.~lock.szerzodes_PaperWorld_2021.pdf#` | LibreOffice lock fájl |

### Megjegyzés a régi mappákról (`Kovacs_Ilona`, `Marketing`, `email_exportok`,
### `meetings`)

Üres mappákká váltak az átszervezés után, de a Drive-mount nem engedi a
`rmdir`-t. Mindegyikbe tettem egy `_ATKOLTOZTUNK.txt` szöveges fájlt, ami
megmondja hova került az anyag — a felhasználó kézzel törölheti a Drive
felületén ha akarja.

### Kritikus megfigyelések (amik kibuktak az átnézés közben)

1. **BicoToner árvita**: Ilona cetlije szerint "a számlán 15%, a szerződésben
   12%". Ellenőriztem a 2022-es szerződést: ott valójában **15% szerepel**
   (ha >3000 RON). Tehát Ilona valószínűleg téved, vagy egy másik
   referenciára gondol — de a cetli arra utal hogy érdemes a könyvelésben
   visszanézni a tényleges levonásokat.
2. **BicoToner szerződés lejárati csapdája**: a 2022-es szerződés 3 évre
   szólt 2022-06-01-től, tehát **2025-06-01-én lejárt**, és a 6.2 pont
   szerint **automatikusan +2 évre meghosszabbodik**, ha 90 nap előtt nem
   szólnak. Mártonnak 2024-12-02-i jegyzetében ez fel volt írva
   ("MÁRCIUS ELEJÉIG dönteni kell") — **lényeges kérdés: szóltak-e?**
3. **InfoTech ajánlat (2024-08)**: nyitott állapotban, Márton kézzel írta
   rá hogy "nem válaszoltak, hagyjuk?" — átneveztem `_NYITOTT.docx`-ra.
4. **Béla bácsi 2025-02-26-i emailje** szempontból kritikus pozitív hír:
   a telephely **NEM eladó**, és Béla felajánlotta a 2035-ig hosszabbítást
   az AFM-hez. A 2026-08-25-i meetingen Márton aggódott emiatt (úgy tűnt
   nem emlékszik az emailre) — ezt szóvá kell tenni neki.
5. **Cégadat-ellentmondás**: a 2018-as bérleti szerződésben a cég CUI
   `RO15847291`, a 2022-es BicoToner-szerződésben `RO18765432`. Tisztázni!

---

## B) MEETING FELDOLGOZÁS — `00_AFM_Palyazat_2026/meeting_20260825/`

A 2026-08-25-i meeting (Márton + Enikő, ~7 perc, AFM kickoff) transcriptje
alapján 4 dokumentum készült:

1. **`01_helyzet_osszefoglalo.md`** — 5 mondatos helyzetkép.
   Lényeg: 70-80% AFM támogatás 2 elektromos autóra; a cég 2 hónapja
   parkolópályán hagyta; péntekre kéne minden összeállni; a 100 oldalas
   kiírás senki nem olvasta végig; az alapadatok szétszórtan élnek;
   Márton átadta a koordinációt nekem.

2. **`02_TODO_lista.md`** — 15 feladat, P0-P3 prioritással, ki/mit/mikorra
   bontásban. Engem (Szabolcs) 8 feladat érint, Enikőt 4, Mártont 2,
   1 közös review. A blocker (P0) feladatok: kiírás végigolvasása,
   pályázhatóság eldöntése, céges alapadatok összeszedése, Mihaela
   megkeresése.

3. **`03_hianyzo_informaciok.md`** — strukturált blocker-lista 7 részben
   (A: pályázati alapfeltételek; B: cégadatok; C: járműpark;
   D: telephely — itt jó hír, hogy Béla bácsi része már részben rendezett;
   E: a pályázat tartalma; F: kit kell megkeresni; G: belső kérdések
   tisztázásra).

4. **`04_followup_email_eniko.md`** — kollegális, magyar, tegező email
   Enikőnek a következő 3 napra eső konkrét feladatairól (kedd-csütörtök).
   5 mondat, dátumokkal, a lezárásban "ha bármi blocker, írj rám" mondat.

---

## C) CLAUDE.md — hosszútávú memória

A `dryrun3/CLAUDE.md` fájl a **kanonikus indító-pont** minden új munkamenethez.
Tartalma:
1. Ki vagyok én (Szabolcs, OM, első nap 2026-05-14)
2. A cég dióhéjban (TransOffice Trade SRL, 2003 óta, Hargita, ~12 fő, ~1.75M RON)
3. Kulcs-NPC-k: belső (Márton, István, Ilona, Enikő, Attila) és külső
   (Mihaela, Béla bácsi, Andrei Munteanu közjegyző, Dan Ionescu PaperWorld,
   Gheorghe Marian BicoToner, Hegyi Zoltán, Orbán Csilla)
4. AKTÍV KÜLDETÉS: AFM 2026, deadline 2026-08-31
5. Mappa-térkép
6. Munka-elvek (backup-first, ne nyúlj a backup-hoz, Kuka nem törlés)
7. **Nyitott kérdések Mártonnak** (CUI ellentmondás, ügyvezető személye,
   BicoToner árvita, BicoToner lejárat, a 2026-08-25-i meeting státusza)

---

## D) Időmérleg (becsült, az átszervezésre)

- Backup létrehozása: 5 perc
- Fájlok átnézése + tartalomkivonat: 25 perc
- Mappastruktúra terv + áthelyezés: 15 perc
- Meeting transcript feldolgozás (4 dokumentum): 30 perc
- CLAUDE.md megírása: 15 perc
- Verifikáció + ez a kivonat: 10 perc

**Összesen: ~100 perc** — egy első nap reggelére ráfér.

---

## E) Mi maradt holnapra (kérlek nézz rá Márton/Szabolcs)

1. **A 100 oldalas AFM kiírás megnyitása** (Mártontól kell, az ő gépén van)
   — ez a P0-as blocker
2. **Mártonnal átbeszélni a CLAUDE.md "Nyitott kérdések" szakaszát** (7 kérdés)
3. **Enikővel egyeztetni** a 04_followup_email tartalmát mielőtt elküldjük
4. **A `00_AFM_Palyazat_2026/kritikus_dokumentumok/` mappába bemásolni**
   a fontosabb releváns fájlokat (bérleti szerződés, Béla email, éves
   jelentés) — szándékosan üresen hagytam, hogy te döntsd el mit emelünk át
5. A régi üres mappákat (`Kovacs_Ilona/`, `Marketing/`, `email_exportok/`,
   `meetings/`) **a Drive felületén kézzel törölni**, ha már nem kellenek

---

**Végeredmény:** a mappa most átlátható, a backup biztonsági háló, a
küldetés priorizált. Holnap reggel a CLAUDE.md-vel kezdek és átveszem
veled (Márton) a nyitott kérdéseket.
