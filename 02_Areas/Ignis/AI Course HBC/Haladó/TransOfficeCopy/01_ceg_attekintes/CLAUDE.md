# CLAUDE.md — TransOffice Trade SRL projekt-memória

> Ez a fájl a Cowork project-memory belépőpontja. Minden további sessionban először ezt olvasd be.

## Cég

- **Név:** TransOffice Trade SRL
- **Székhely + telephely:** Calea Băieșenilor 22, Odorheiu Secuiesc (Székelyudvarhely), Hargita megye, Románia
- **Alapítva:** 2003 (Kovács István)
- **Ügyvezető:** Kovács Márton (33, az alapító fia, 2024-ben átvette)
- **Méret:** 12 alkalmazott, ~1,75 millió RON árbevétel (2022, az utolsó megbízható adat)
- **Tevékenység:** B2B irodai eszközök és fogyóanyagok kereskedelme (papír, toner, írószer, kis bútor)
- **Ügyfélkör:** ~25-30 aktív B2B vevő Hargita és Kovászna megyében — önkormányzatok, iskolák, könyvelőirodák, kórház, helyi KKV-k

## Az én szerepem

- **Pozíció:** Operations & Systems Manager (új, 1. munkanap)
- **Feladat:** rendszert építeni a Kovács Ilona (volt admin, Márton anyja) után maradt káoszból, és segíteni az AFM pályázat beadásában
- **Jelentés:** közvetlenül Mártonnak

## Aktuális küldetés

- **AFM Mobilitate Verde 2025** pályázat beadása 2 elektromos szolgálati járműre (70-80% támogatás, ~200 000 EUR)
- **Határidő:** ezen a héten (péntekig); a 94 oldalas pályázati kiírás románul rendelkezésre áll
- **Forrás-fájl:** `Tananyag/03_Dontes_Elemzes/Palyazat_kiiras/Ghidul-solicitantului-Mobilitate-Verde-IMM-2025.md`

## Kulcs-személyek

| Név | Szerep | Kapcsolat | Megjegyzés |
|---|---|---|---|
| Kovács Márton | Ügyvezető | `kovacs.marton.to@gmail.com` | Türelmetlen, eredményorientált; AFM-mániás |
| Szabó Enikő | Belső könyvelő (részmunkaidős) | iroda | Csak a számlákat kezeli, heti 3 nap |
| Mihaela Florian | Külsős könyvelő | `mihaela.f.expert@gmail.com` | Csak emailen elérhető — EBITDA-számításhoz kell |
| Bíró Attila | Raktárvezető | iroda | Papíron dolgozik, megbízható |
| Kovács Ilona | Volt admin (Márton anyja) | telefon | Visszavonult 2024-ben; "azt hiszem abban a zöld mappában volt..." |
| Béla Iosif ("Béla bácsi") | Telephely-tulajdonos | `bela.iosif@gmail.com` | 1998 óta tulajdonos; Calea Băieșenilor 22 nem eladó (családi örökség); contract prelungire 2035-ig felajánlva |

## A workspace struktúrája

```
TransOfficeCopy/                            ← Nyers, kaotikus örökség (34 fájl)
├── *.xlsx, *.docx, *.txt                   ← Ügyfél-, ár-, készlet-, rendelés-fájlok
├── Kovacs_Ilona/                           ← Régi admin mappa (vegyes — recept, fotó, jelszó is)
├── Marketing/                              ← 2012-es honlap-szöveg
├── email_exportok/                         ← 6 export, köztük Béla bácsi válasz + BicoToner felszólítás
├── meetings/                               ← Márton-meetingek + meeting_transcript_20250224.srt
│
├── 01_ceg_attekintes/                      ← F1 outputjai (ez a CLAUDE.md is itt)
├── 02_meeting_TODO/                        ← F2 outputjai
├── 03_palyazati_elemzes/                   ← F3 outputjai
├── 04_kommunikacio/                        ← F4 outputjai (3 email + 1 PPT + DCB-frissítés)
├── 05_palyazat_csomag/                     ← F5 outputjai (Plan de afaceri + dosar + form CSV)
├── 06_weboldal/                            ← F6 outputjai (3 design-variáns + saját)
└── _DryRun_jelentés/                       ← Meta-jegyzetek és pontozás
```

## Fontos kontextus-rétegek

1. **Béla bácsi szál** — a `meetings/meeting_transcript_20250224.srt`-ben Márton elejt egy mondatot Béla bácsi eladási szándékáról ("Béla bácsi szilveszterkor mondott valamit, hogy gondolkodik egy-két ingatlana eladásán — utána kéne nézni nehogy a miénk legyen"). **A 2025-02-26-i Béla bácsi-email tisztázza:** NEM a Calea Băieșenilor 22, hanem agrárparcellák a Sub Cetate-ben → telephely-stabilitás zöld.

2. **EBITDA szál** — a `Kovacs_Ilona/eves_jelentes_2022.xlsx` az utolsó belső adat 2022-ig. 2023-2024 csak Mihaela külsős könyvelőtől szerezhető be. **A 2024-es üzleti év eredménye lehet negatív** (Márton említi a meetingen), de a 2023-as biztosan pozitív → **egy pozitív év elég** az AFM-eligibilityhez.

3. **BicoToner szál** — szerződés 2025-06-01-én lejár, 90 napos felmondás (márc. elejéig dönteni); fennáll 4 750 RON tartozás + árvita (15% vs. szerződéses 12%). **Pályázattól független ügy**, de **márciusban kezelni kell** mert ütközhet a pályázat-csomag fókuszával.

4. **Adatkonzisztencia-figyelmeztetés** — 3 ügyféllista (40 / 28 / 8 sor) eltér; egyetlen Excel sem master. **Mindig kereszthivatkozz** a `rendeles_naplo.xlsx`-vel és az `email_exportok/`-kal.
