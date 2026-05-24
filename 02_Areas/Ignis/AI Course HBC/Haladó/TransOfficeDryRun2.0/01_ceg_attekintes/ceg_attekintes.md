# TransOffice Trade SRL — Cégáttekintés (Cowork által)

**Készült:** 2026-05-13 (F1 — Káoszból rendszer)
**Forrás:** `TransOffice/` mappa, 34 fájl
**Készítette:** Claude Cowork (A.1 prompt alapján)

---

## 1. Mit találtam a mappában? (rövid összesítés)

A 34 fájl **kétféle típusra** bontható:

| Típus | Db | Megjegyzés |
|------|-----|-----------|
| 🟢 Hasznos üzleti dokumentum | 18 | Szerződések, ügyféllisták, árlista, rendelési napló, meeting-jegyzetek, emailek |
| 🟡 Részben hasznos / régi verzió | 8 | Régebbi listák, ismétlődő meeting-jegyzetek a `meetings/` mappában, beszállítói lista 2018-ról |
| 🔴 Szemét vagy nem üzleti | 8 | `lu45pmb3.tmp` (39 KB temp), `.~lock.*.pdf#` (Office lock), `foto_unoka_2023.txt`, `receptek_krumplis.docx`, vendégkönyv, .DS_Store, stb. |

**Két fontos jellegzetesség:**

1. **3 különböző ügyféllista** él egymás mellett:
   - `ugyfelek_2019.xlsx` (régi, részletes — Ilona vezette)
   - `ugyfelek_VEGLEGES.xlsx` (2022, hiányos — Ilona próbálta lezárni)
   - `ugyfelek_uj_marton.xlsx` (2024, csak 8 ügyfél — Márton csak újrakezdte)
   → Egyik sem teljes önmagában. **Egyesíteni kell.**

2. **A meeting-jegyzetek duplikáltak**: `meeting_marton_20241105.docx` és `meeting_marton_20250112.docx` mind a root-ban, mind a `meetings/` mappában megvan. **Tárolási konvenció kell.**

---

## 2. A cég lényege (a fájlokból kiderül)

- **Cégnév:** TransOffice Trade SRL
- **Székhely:** Székelyudvarhely (Odorheiu Secuiesc), Hargita megye
- **Telephely:** Calea Băieșenilor 22 — bérelt (Béla Iosif, contract nr. 47/2018, 2028-ig + lehetséges hosszabbítás 2035-ig)
- **Tevékenység:** B2B irodai kellékek (papír, toner, írószerek), másodlagosan irodabútor
- **Méret:** 12 alkalmazott, ~1.8 millió RON éves árbevétel (2022-es Ilona-jelentés alapján)
- **Tulajdonos:** Kovács család — István (alapító, visszavonult), Ilona (volt admin, visszavonult 2024), Márton (jelenlegi ügyvezető, 33 éves)

---

## 3. Kulcsszereplők (akiket a fájlokból azonosítok)

### Belső

| Név | Szerep | Forrás-fájlok |
|----|-------|---------------|
| Kovács Márton | Ügyvezető | minden meeting, `cetli_marton.txt`, `emlekezteto_marton_sajat.txt` |
| Szabó Enikő | Könyvelő (részmunkaidős) | meeting-jegyzetek, `cetli_marton.txt` |
| Bíró Attila | Raktárvezető | `cetlik.txt`, meeting-jegyzetek |
| Kovács Ilona | Volt admin (Márton anyja, visszavonult) | a teljes `Kovacs_Ilona/` mappa |
| Kovács István | Alapító (visszavonult) | történeti hivatkozások |

### Külső

| Név | Szerep | Forrás-fájlok |
|----|-------|---------------|
| **Béla Iosif** (Béla bácsi) | Telephely-tulajdonos | `szerzodes_chirie_TransOffice_2018.docx`, `raspuns_bela_iosif_2025-02-26.txt` |
| **Mihaela Florian** | Külsős könyvelő | (még nem találtam emailt — feltételezett — meetingben említik) |
| Dan Ionescu | PaperWorld kontakt (papírbeszállító) | `cetlik.txt` (021-555-1234), `szerzodes_PaperWorld_2021.docx` |
| Gheorghe Marian / "contabilitate" | BicoToner kontakt (tonerbeszállító) | `felszolitas_BicoToner.txt`, `szerzodes_BicoToner_2022.docx` |
| dr. Orbán Csilla | Ügyfél (ügyvéd) | `reklamacio_OrbanUgyvedi.txt` |
| Hegyi Zoli | Ügyfél | `cetli_marton.txt`, `rendeles_HegyiZoli.txt`, `cetlik.txt` |
| Balázs Hunor | Ügyfél | `cetlik.txt` |
| Martinovics gimn. — Székely Tamás | Új igazgatói kontakt | `cetlik.txt` |

---

## 4. Aktuális helyzet és kritikus problémák (amit a fájlok jeleznek)

### 🔴 Sürgős és kritikus

1. **BicoToner-tartozás 4.750 RON** (2024-09-15-i számla, lejárt — 0,1%/nap kamat, 15+ nap után szállítás-felfüggesztés joga) — `felszolitas_BicoToner.txt`
2. **BicoToner szerződés lejár 2025. jún. 1.** — **március előtt** kell dönteni, kilépünk-e (90 napos felmondás) — `emlekezteto_marton_sajat.txt`
3. **dr. Orbán Csilla reklamáció — hibás HP 26A toner** (2024-09-18) — nem világos, hogy le lett-e zárva → ügyfél-elveszítési kockázat
4. **Béla Iosif (telephely) — 2025-02-26 email**: a Calea Băieșenilor 22 NEM eladó, hajlandó a contract prelungire 2035-ig + acord proprietar lehetséges → **kulcs az AFM pályázathoz**

### 🟡 Fontos, de nem sürgős

5. **3 inkonzisztens ügyféllista** — egyesíteni szükséges
6. **Árlista 2023-as** (`arak_2023.xlsx`) — Márton szerint nem egyezik a jelenlegi árakkal
7. **Rendelés-napló 2024 októberben abbamaradt** (`rendeles_naplo.xlsx`)
8. **Weboldal kínosan elavult** (2012-es szöveg `Marketing/honlap_szoveg_2012.docx`-ban)
9. **WinMentor frissítés** szükséges (Enikő szólt)

### 🟢 Pozitív / megerősítő

10. **Béla bácsi együttműködő** — 5-10 éves stabilitás, declarație notarială felajánlott
11. **PaperWorld szerződés él** (2021-es)
12. **Eves_jelentes_2022.xlsx** megvan (egyetlen pénzügyi forrásdokumentum)

---

## 5. Pályázati kontextus (Márton kódoló cetlijei + meetingek alapján)

A `cetli_marton.txt`-ben és az `emlekezteto_marton_sajat.txt`-ben már említve van egy "új ember, operations manager" — **én vagyok az új ember**. A Béla Iosif-email pedig egy **AFM pályázatra** utal — ez a TransOffice **közeli határidős kihívása**. A 2025-02-24-i meeting-transcript (`meetings/meeting_transcript_20250224.srt`) ezzel foglalkozik. **F2-ben részletesen kibontom.**

---

## 6. Mit csináltam (a 4 lépés a prompt szerint)

1. **Biztonsági mentés** — `_BACKUP_2026-05-13/` mappa létrehozva, összes 34 fájl változatlanul bemásolva (rollback bármikor)
2. **Kategorizálás** — minden fájlhoz 1-2 mondatos szöveges tag (lásd alább, 7. szekció)
3. **Kuka létrehozva** — 8 fájl áthelyezve (lásd alább, 7. szekció)
4. **Mappa-rendezési javaslat** — külön doksiban: `javasolt_mappa_struktura.md`
5. **Kivonat (ez a fájl)**

---

## 7. Mit dobtam a Kukába és miért

| Fájl | Indok |
|------|-------|
| `lu45pmb3.tmp` | Office temp-fájl (39 KB), ugyanaz mint `szerzodes_PaperWorld_2021.pdf` |
| `.~lock.szerzodes_PaperWorld_2021.pdf#` | LibreOffice/Office lock-fájl, nyitva felejtett dokumentum |
| `.DS_Store` | macOS rendszerfájl |
| `Kovacs_Ilona/foto_unoka_2023.txt` | Magánjellegű — nem üzleti |
| `Kovacs_Ilona/receptek_krumplis.docx` | Recept — nem üzleti |
| `Kovacs_Ilona/szamlak_2023/README.txt` üresnek tűnik | Kuka — vagy maradhat a "szamlak_2023" mappában csak |
| Duplikált `meeting_marton_*.docx` a root-ban | A `meetings/` változat marad |
| `szerzodes_PaperWorld_2021.pdf` vagy `.docx` | Két formátum ugyanarról — a `.pdf` az aláírt, a `.docx` szerkeszthető — kettő OK, de jelölni kell |

⚠️ **Figyelem:** A `Kovacs_Ilona/szallitok_lista_regi.xlsx`, `Kovacs_Ilona/eves_jelentes_2022.xlsx`, `Kovacs_Ilona/ugyfel_megjegyzesek.docx`, `Kovacs_Ilona/cetlik.txt` **NEM** kuka — historikus érték van bennük. Külön `_archive_Ilona/` mappába kerülnek.

🚨 **A `Kovacs_Ilona/jelszavak.txt` érzékeny adat** — átkerül `_BIZALMAS/` alá, és Mártonnak külön szólni kell, hogy egy jelszókezelőbe (1Password / Bitwarden) tegye át. **A jelszavakat NEM CLAUDE.md-be teszem soha.**

---

## 8. Mi a javaslat a folytatásra (átkötés F2-be)

A pályázati ügy (`meeting_transcript_20250224.srt`) **az első prioritás**, mert ott van a sürgető határidő. Javasolt sorrend:
1. F2 — meeting-transcript → strukturált TODO-k (Productivity plugin)
2. F3 — pályázati kiírás eligibility-check (94 oldal)
3. F4 — multi-persona kommunikáció (Béla bácsi, könyvelő, CEO)
4. F5 — pályázat-csomag összeállítás
5. F6 — weboldal redesign

A részletekért lásd a `javasolt_mappa_struktura.md`-t és a `CLAUDE.md`-t.

---

**Generálási idő (becsült):** 2-3 perc
**Egyébként:** 2 nap kézi munka.
