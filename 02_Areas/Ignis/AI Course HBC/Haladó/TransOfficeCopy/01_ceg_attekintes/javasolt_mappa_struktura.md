# Javasolt mappastruktúra a TransOffice digitális rendnek

> **Cél:** Egy ember nélkül is használható, AI-barát file system. A 200+ kaotikus fájl helyett 6 funkcionális gyökér + kettő közös mappa.

```
TransOffice/
├── 00_CEG/                     ← Cégadatok master (egy helyen)
│   ├── CLAUDE.md
│   ├── ceg_attekintes.md
│   ├── szervezeti_struktura.md
│   └── jogi_keret/             ← Cégkivonat, ANAF, OAUI igazolások
│
├── 01_UGYFELEK/                ← Master CRM
│   ├── ugyfelek_MASTER_2025.xlsx  ← (a 3 régi Excel konszolidálva)
│   ├── ugyfel_megjegyzesek/    ← Egyenként .md file
│   ├── reklamaciok/            ← (Orbán Csilla toner-ügy itt)
│   └── archivum/               ← ugyfelek_2019.xlsx, _VEGLEGES.xlsx, _uj_marton.xlsx
│
├── 02_BESZALLITOK/             ← Szerződés-katalógus
│   ├── szallitok_lista_AKTUALIS.xlsx
│   ├── PaperWorld/             ← szerződés + emailek + felszólítások
│   ├── BicoToner/              ← URGENT: lejár 2025-06-01, dönteni márc. elejéig
│   ├── MegaPrint/, Birotehnic/, EuroMobil/
│   └── archivum_megszunt/      ← Herlitz, Global Copy, Top Office
│
├── 03_TERMEKEK_KESZLET/        ← Árlista + készlet
│   ├── arlista_MASTER_2025.xlsx
│   ├── keszlet_aktualis.xlsx
│   └── rendeles_naplo_MASTER.xlsx
│
├── 04_PENZUGY/                 ← Csak Enikő + Mihaela ide
│   ├── 2020/, 2021/, 2022/, 2023/, 2024/, 2025/
│   ├── eves_jelentesek/
│   └── adoUgyek/
│
├── 05_TELEPHELY_ESZKOZ/        ← Bérlet, járművek, eszközök
│   ├── szerzodes_chirie_Bela_Iosif/
│   ├── jarmuvek/
│   └── eszkoz_leltar/
│
├── 06_KOMMUNIKACIO/            ← Email-archívum + jegyzetek
│   ├── _INBOX_kiosztando/      ← Új email-ek ideiglenesen
│   ├── ugyfelekkel/, beszallitokkal/, hatosagokkal/
│   └── jegyzetek/              ← cetli_marton.txt, cetlik.txt, emlékeztetők
│
├── 07_PROJEKTEK/               ← Élő projektek (időhöz kötött)
│   └── AFM_Mobilitate_Verde_2025/
│       ├── eligibility_check.md
│       ├── mellekletek_gap_analysis.md
│       ├── data_completion_board.md
│       └── outputok/
│
├── 08_HR/                      ← Alkalmazotti adatok (jövő)
│
├── 09_IT_BIZTONSAG/            ← Jelszavak, hozzáférések — KÜLÖN VÉDETT
│   └── jelszavak_FRISSITENDO.md  ← (Vault-ba költöztetni!)
│
├── 99_ARCHIVUM/                ← Régi, de megőrzendő
│   ├── Kovacs_Ilona_personal/  ← receptek_krumplis, foto_unoka — Ilonának visszaadni
│   └── 2012_marketing/         ← honlap_szoveg_2012.docx (történelmi)
│
└── _TMP_torlendo/              ← Tipp: `lu45pmb3.tmp` és társai
```

## Konvenciók

- **Datumozás:** ISO (`2025-02-24`), nem `20250224` és nem `24.02.2025`
- **Verziók:** ne `_VEGLEGES`, `_uj`, `_marton`; használj `_v1`, `_v2` vagy git-et
- **Master / Aktualis:** csak egy létezhet egyszerre minden témából — a többi `archivum/`-ba
- **Nyelv:** a fájlnév lehetőleg ékezet nélküli, alulvonással (`ugyfelek_master_2025.xlsx`)
- **Szenzitív:** `09_IT_BIZTONSAG/` és `04_PENZUGY/` kerüljön külön hozzáférési szintre

## Migrációs sorrend (1 nap alatt megcsinálható)

1. ✅ **F1 (most):** `00_CEG/` létrehozva, CLAUDE.md + ceg_attekintes.md kész
2. Beszállítók szétdarabolása (PaperWorld, BicoToner, MegaPrint, ... 6 mappa)
3. Ügyfél-master konszolidálás (3 Excel → 1 master, scriptelhető)
4. Pénzügy átszervezés (Enikő segítségével)
5. Email-archív címkézés (kb. 6 email-export → kategóriába)
6. `Kovacs_Ilona/personal/` kiszedése + Ilonának visszaadás
7. `_TMP_torlendo/` ellenőrzés + törlés
