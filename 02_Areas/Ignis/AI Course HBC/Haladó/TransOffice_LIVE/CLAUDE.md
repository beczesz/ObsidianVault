---
project: TransOffice
type: hosszú-távú-memória
owner: Szabolcs (operations manager — új munkatárs 2026-05-15-től)
last_updated: 2026-05-15
read_first: true
id: dfa76ab0-f00c-4ef8-b6ea-3f0f2354efda
index_schema_version: 1
---

# CLAUDE.md — Hosszú távú memória

> **Minden új munkamenetben ELSŐKÉNT ezt olvasd el.**
> Ez tartalmazza a cég kontextusát, a mappa-struktúrát, a konvenciókat
> és a folyamatban lévő kritikus ügyeket. Frissítsd, ha új információt
> tudsz meg, vagy ha változik a struktúra.

---

## 1. Cég kontextus

**TransOffice** — kis-közepes irodaszer- és nyomtatókellék-kereskedés.

- **Profil:** papír, toner, irodaszer (HP utángyártott tonerek, A3/A4 papír stb.)
- **Helyszín:** Románia (RON-ban számláznak, román beszállítók is)
- **Nyelv:** belső kommunikáció magyar, szerződések / külső kapcsolat néha román (pl. `chirie` = bérlet)
- **Tulajdonos / vezetés:** családi cég
  - **Kovács Ilona** — anya, sok éve viszi az adminisztrációt (most részben átadja)
  - **Kovács Márton** — fia, operatív vezető, váltani akar (új ember = én)
- **Belső kollégák:**
  - **Enikő** — könyvelő (vagy könyvelői kapcsolat); kéri a PDF számlákat
  - **Attila** — operatív/raktár (papírral kapcsolatos kérdés ment hozzá)
- **Beszállítók:**
  - **PaperWorld** — papír; kapcsolat: **Dan Ionescu**, új tel: **021-555-1234**
    (Ilona cetlije szerint a régi szám nem él)
  - **BicoToner** — toner; szerződés **2022**, lejárat: **2026 jún 1** (lásd lent ⚠️)
- **Fontosabb ügyfelek (eddig azonosított):**
  - **Hegyi Zoli** — visszatérő ügyfél, A3 papírt kér; névnap: okt 15
  - **Martinovics Gimnázium** — Kiss igazgató nyugdíjba megy, új ember: **Székely Tamás**
  - **Balázs Hunor** — A4 papír + HP83 toner x10 csomag jellegű rendelő
  - **Orbán Ügyvédi Iroda** — reklamáció a múltban (lásd 05_Email_archivum)
  - **Béla / Iosif** — román nyelvű email-váltás (2025-02-26)

---

## 2. Mappa struktúra (érvényes 2026-05-15-től)

A struktúra **PARA-szerű, számozott**. A számok rögzítettek, ne változtass rajtuk.

```
TransOffice_LIVE/
├── CLAUDE.md                           ← ez a fájl (memória)
├── KIVONAT_2026-05-15.md               ← első napi rendrakás összefoglaló
│
├── 00_TODO_es_notesz/                  ← élő TODO-k, cetlik, jegyzetek
├── 01_Ugyfelek/                        ← aktív ügyféladatok
├── 02_Szerzodesek/                     ← élő szerződések + ajánlatok
├── 03_Penzugy/                         ← árlisták, készlet, rendelések, számlák
│   └── Szamlak_2023/
├── 04_Meetingek/                       ← meeting jegyzetek, hangfelvételek, átiratok
├── 05_Email_archivum/                  ← exportált fontos emailek
├── 06_Marketing/                       ← marketing anyagok
│
├── 99_Archiv/                          ← régi, de potenciálisan releváns
│
├── Ilona_szemelyes/                    ← Ilona magán fájljai (ide nem nyúlunk)
├── Kuka/                               ← törlésre váró fájlok (lock, duplikáció, tmp)
└── _BACKUP_2026-05-15/                 ← első napi backup (mozgasd egy szinttel feljebb!)
```

### Mire való melyik?

| Mappa | Mi kerül ide |
|---|---|
| `00_TODO_es_notesz/` | Bármi, ami élő feladat, jegyzet, cetli. Pl. `Marton_TODO_2024-12.txt`. |
| `01_Ugyfelek/` | Aktuális ügyféllista, ügyfél-megjegyzések, kapcsolattartók. |
| `02_Szerzodesek/` | Élő szerződések (beszállítói, ügyfél, iroda-bérlet) + kimenő ajánlatok. |
| `03_Penzugy/` | Árak, készlet, rendelési napló, kimenő/bejövő számlák évenkénti almappákban. |
| `04_Meetingek/` | `meeting_*` dokumentumok, hangfelvételek, transcriptek. |
| `05_Email_archivum/` | Fontos email-export (reklamáció, felszólítás, visszaigazolás stb.). |
| `06_Marketing/` | Honlap szövegek, kampány anyagok, social media. |
| `99_Archiv/` | Régi verziók (pl. `ugyfelek_2019`), elavult listák, kontextusként megőrzendő. |
| `Ilona_szemelyes/` | **Ne nyúlj hozzá engedély nélkül.** Magán anyag + a `jelszavak.txt` (lásd ⚠️). |
| `Kuka/` | Lock fájlok (`~$*`, `.~lock*`), tmp fájlok, igazolt duplikációk. Időközönként véglegesíthető a törlés. |
| `_BACKUP_2026-05-15/` | A 2026-05-15-i rendrakás előtti teljes állapot snapshotja. |

---

## 3. Fájlnév-konvenciók

- **Nyelv:** elsősorban **magyar**, ékezet nélkül (Drive/Mac kompatibilitás miatt).
  Pl. `szerzodes_iroda_berlet_2018.docx`, nem `szerződés_iroda_bérlet_2018.docx`.
- **Dátum:** `YYYY-MM-DD` vagy `YYYY` év végén — pl. `meeting_marton_2025-01-12.docx`.
- **Verziók:** **ne legyen** `_VEGLEGES`, `_v2`, `_uj`, `_FINAL`. Vagy a fájl az aktuális,
  vagy archív (`99_Archiv/`). A Drive verziótörténetét használjuk élesben.
- **Idegen szavakat kerüljük a fájlnévben:** `chirie` → `iroda_berlet`.
- **Snake_case:** szóköz helyett `_`. Felsőbb-/kisbetű elsősorban kisbetű, kivéve ha tulajdonnév.

---

## 4. ⚠️ Kritikus — időérzékeny ügyek

Ezeket szem előtt kell tartani **most**:

1. **BicoToner szerződés lejárat: 2026-06-01.**
   - 90 napos felmondási kötelezettség. Márton emlékeztetője szerint
     "MÁRCIUS ELEJÉIG dönteni kell" → **az időablak már szűk vagy lejárt**.
   - Számlázási eltérés: szerződés 12%, de 15%-ot számolnak (Ilona cetlije + reklamáció email).
   - Fájl: `02_Szerzodesek/szerzodes_BicoToner_2022.docx`, `05_Email_archivum/felszolitas_BicoToner.txt`

2. **`Ilona_szemelyes/jelszavak.txt` — KRITIKUS biztonsági kockázat.**
   - Plain text fájl céges + magán jelszavakkal: email, weboldal admin, számlázó (WinMentor),
     PaperWorld portál, BicoToner rendelés, iroda WiFi.
   - **Át kell rakni jelszókezelőbe** (1Password / Bitwarden) és törölni innen.
   - Külön ügy: a fájlban benne van Márton kezdeti jelszava is — váltani kell.

3. **Ügyféllista bizonytalanság.**
   - Három verzió volt: `ugyfelek_2019.xlsx`, `ugyfelek_VEGLEGES.xlsx`, `ugyfelek_uj_marton.xlsx`.
   - **Élesnek a `VEGLEGES`-t választottam** (legkisebb, név alapján a legutolsó), de
     ezt kollégákkal kell verifikálni — lehet hogy Márton verziója a frissebb.
   - Aktív: `01_Ugyfelek/ugyfelek_VEGLEGES.xlsx`
   - Archív (verifikáláshoz): `99_Archiv/ugyfelek_2019.xlsx`, `99_Archiv/ugyfelek_uj_marton.xlsx`

4. **WinMentor frissítés.** Márton emlékeztetője szerint Enikő jelezte. Új könyvelőprogram kell.

5. **Weboldal projekt.** Infoprog nem szállította le. Új ajánlatkérés szükséges
   (Márton TODO + Ilona cetli).

6. **PaperWorld új telefonszám.** A régi szám nem él (Ilona cetlije).
   Frissíteni az ügyféladatbázisban.

---

## 5. A `Kovacs_Ilona` mappa kontextusa (történelmi)

A `Kovacs_Ilona/` mappa eredetileg Ilona "saját" mappája volt a céges drive-on.
Ott vegyesen voltak: éves jelentés, szállítók listája, ügyfél-megjegyzések
(céges) ÉS receptek, unoka-fotó, jelszavak (magán).

A rendrakáskor:
- A **munkaanyagokat szétosztottam** a 01-99 mappákba.
- A **magán fájlokat** a `Ilona_szemelyes/` mappába raktam.
- A `jelszavak.txt`-re külön figyelmeztetés vonatkozik (lásd fent).
- Az **eredeti, üres `Kovacs_Ilona/`** a `Kuka/_ures_Kovacs_Ilona/` alatt van —
  a Google Drive sandbox nem engedte törölni; Finder-rel lehet véglegesen kidobni.

---

## 6. Munka-protokoll

- **Új session elején:** olvasd el ezt a fájlt + a `KIVONAT_*.md` legutóbbi verzióját.
- **Fájl-mozgatás előtt:** mindig készíts backupot a régi struktúrából,
  ha a változtatás nem triviális.
- **Naplózz minden átszervezést** a `KIVONAT_YYYY-MM-DD.md` fájlba ugyanúgy,
  ahogy 2026-05-15-én is.
- **Soha ne nyúlj** `Ilona_szemelyes/`-hez engedély nélkül.
- **Lock fájlok (`~$*`, `.~lock*`):** ezek élő nyitott Office fájlokat jeleznek.
  Ha látsz ilyet, valaki épp dolgozik vele — várd meg, vagy szólj.
- **Frissítsd ezt a fájlt**, ha:
  - Új mappa-szabály születik
  - Új beszállító/ügyfél kerül elő, akit érdemes itt is rögzíteni
  - Lezárul egy "Kritikus ügy" a 4. pontból

---

## 7. Forrás-fájlok, amik ezt a memóriát megalapozzák

- `00_TODO_es_notesz/Marton_TODO_2024-12.txt` — Márton aktuális TODO listája
- `00_TODO_es_notesz/Ilona_cetlik.txt` — Ilona vegyes jegyzetei (kontakt, ügyfél, ár-eltérés)
- `05_Email_archivum/emlekezteto_marton_sajat.txt` — Márton sajátmagának küldött emlékeztetője
- `05_Email_archivum/felszolitas_BicoToner.txt` — BicoToner ügy
- `KIVONAT_2026-05-15.md` — első napi rendrakás részletei
