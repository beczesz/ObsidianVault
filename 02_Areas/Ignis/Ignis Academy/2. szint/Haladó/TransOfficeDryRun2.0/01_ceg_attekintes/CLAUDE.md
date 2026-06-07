---
title: "CLAUDE.md — TransOffice Trade SRL"
date: 2026-05-13
author: Becze Szabolcs
status: active
description: "A TransOffice Trade SRL 22 éves B2B irodai kellék kereskedő KKV szervezeti memóriája, tartalmazva a cég alapadatait, csapattagokat, az aktuális AFM Mobilitate Verde pályázati prioritást és az azonosított kockázatokat. Márton ügyvezető és az új Operations Manager számára szól napi munkához."
description_source: auto
description_hash: d096fab06e3a9b01
id: ad867d7a-51b1-4121-8cd2-c18e02eec76c
index_schema_version: 1
bdos_index: true
---
# CLAUDE.md — TransOffice Trade SRL

> Ez a fájl a Cowork hosszútávú memóriája. Minden új munkamenetben ELŐSZÖR ezt olvasd be.
> Frissítve: 2026-05-13 (F1 — Káoszból rendszer)

---

## 🏢 A cég egy mondatban

A TransOffice Trade SRL egy 22 éves, B2B irodai-kellék-kereskedő KKV Székelyudvarhelyen (Hargita megye, Románia), 12 alkalmazottal, ~1.8 millió RON éves árbevétellel — épp generációváltáson megy keresztül (Kovács István → Kovács Márton, 33) miközben a 2025-ös AFM Mobilitate Verde pályázatra készül egy elektromos járműflottára.

## 📍 Alapadatok

| Adat | Érték |
|------|-------|
| Cégnév | TransOffice Trade SRL |
| Székhely | Székelyudvarhely (Odorheiu Secuiesc), Hargita megye |
| Telephely | Calea Băieșenilor 22 — **bérelt** (Béla Iosif, contract nr. 47/2018, 2028-ig + 2035-ig hosszabbítható) |
| CUI | (a fájlokban még nem találtam — beszerezni Mártonnal) |
| Alapítás | 2003 (Kovács István) |
| Alkalmazottak | 12 fő |
| Éves árbevétel | ~1.8 M RON (2022 alapján — 2023-2024-es számok a könyvelőnél) |
| Tevékenység | B2B irodai kellék (papír, toner, írószer), másodlagosan irodabútor |

## 👥 A csapat (a fájlokból azonosítottam)

### Belső
- **Kovács Márton** (33) — ügyvezető, tech-érdeklődő, türelmetlen, eredményorientált
- **Szabó Enikő** (45) — könyvelő, részmunkaidős (heti 3 nap), precíz
- **Bíró Attila** (50) — raktárvezető, megbízható, papíron dolgozik
- **5 raktáros / 2 sofőr / 2 segéd**
- **Kovács Ilona** — volt admin (Márton anyja), visszavonult 2024-ben, telefonon elérhető
- **Operations & Systems Manager — TE** (új pozíció, első nap)

### Külső
- **Béla Iosif** ("Béla bácsi", ~70 éves) — telephely-tulajdonos, családi ismerős, együttműködő. Tel: 0744-291.872. Email: bela.iosif@gmail.com
- **Mihaela Florian** — külsős könyvelő (csak emailen érhető el)
- **Dan Ionescu** — PaperWorld kontakt (papírbeszállító), Tel: 021-555-1234
- **Gheorghe Marian** — BicoToner kontakt (tonerbeszállító)

## 🎯 Aktuális kihívás (prioritás)

**AFM Mobilitate Verde 2025** — 200.000 EUR állami támogatás 5 elektromos járműre + 2 töltőpontra.
- **Sürgető:** a forrás kifut, **péntekig** be kell adni
- **Műhely:** 2025-02-24-i meeting-transcript részletezi (lásd `meetings/meeting_transcript_20250224.srt`)
- **Béla bácsi együttműködik**: contract prelungire 2035-ig + declarație notarială (`email_exportok/raspuns_bela_iosif_2025-02-26.txt`)

## 🚨 Aktív kockázatok (a fájlokból)

1. **BicoToner-tartozás 4.750 RON** lejárt (2024-11-05 felszólítás) — szállítás-felfüggesztési veszély
2. **BicoToner-szerződés lejár 2025-06-01** — 90 napos felmondási idő → **2025. március előtt** kell dönteni
3. **dr. Orbán Csilla reklamáció** (2024-09-18, hibás HP 26A) — státusz ismeretlen → ügyfél-elveszítési kockázat
4. **3 inkonzisztens ügyféllista** — döntéshozatali bizonytalanság
5. **Árlista (`arak_2023.xlsx`) nem aktuális** — kalkuláció-hiba kockázat
6. **Weboldal 2012-es** — branding-probléma

## 📁 Mappastruktúra (rendezett — F1 outputja)

```
TransOffice/
├── 00_Aktualis/             ← élő, gyakran használt
│   ├── ugyfelek_master.xlsx  (a 3-ból egyesítve — később)
│   ├── arak_2025.xlsx        (frissítendő)
│   └── keszlet_aktualis.xlsx
├── 01_Szerzodesek/
│   ├── Telephely/           szerzodes_chirie_TransOffice_2018.docx + Béla bácsi válasz
│   ├── Beszallitok/         PaperWorld 2021, BicoToner 2022
│   └── Ugyfelek/            (üres egyelőre — egyedi szerződések ha lesznek)
├── 02_Penzugy/
│   ├── eves_jelentes_2022.xlsx (Ilona)
│   ├── szamlak_2023/        (Ilona mappája)
│   └── rendeles_naplo.xlsx
├── 03_Ertekesites/
│   ├── ajanlat_InfoTech_2024.docx
│   └── ugyfelek_archivum/   (régi listák — historikus)
├── 04_Meetings/
│   ├── meeting_marton_20241105.docx
│   ├── meeting_marton_20250112.docx
│   └── meeting_transcript_20250224.srt  ← AFM pályázat (F2 kiindulópont)
├── 05_Levelezes/             (a 6 archív email)
├── 06_Marketing_Honlap/      honlap_szoveg_2012.docx (régi)
├── _archive_Ilona/           cetlik, megjegyzések, régi listák — historikus
├── _BIZALMAS/                jelszavak (eljuttatva Mártonnak jelszókezelőbe)
└── _Kuka/                    8 fájl (lock, tmp, recept, foto, .DS_Store, dupla meetingek)
```

## 🗂 Konvenciók (jövőbeli munkához)

- Új fájlnév: `kategoria_temaja_dátum.kiterjesztés` (pl. `szerzodes_chirie_2025.docx`)
- `_archive_*` és `_Kuka` mappa-prefix jelzi: NEM napi munka
- `_BIZALMAS/` mappába jelszó, banki adat, személyes adatok
- Meeting-jegyzetek mindig SRT vagy MD formátumban, dátummal a fájlnévben

## 🎬 Hol tart a workshop-narratíva

✅ **F1 — kész**: ez a CLAUDE.md a Cowork rendrakásának eredménye
🚧 **F2 — következő**: meeting_transcript_20250224.srt → TODO-k a Productivity pluginbe
⏳ F3 — pályázati kiírás eligibility check
⏳ F4 — multi-persona kommunikáció (Béla bácsi, Mihaela, Márton CEO PPT)
⏳ F5 — Plan de afaceri + csomag + form-kitöltés
⏳ F6 — weboldal redesign

## 🔑 Fontos linkek és hivatkozások

- **Pályázati kiírás:** `Tananyag/03_Dontes_Elemzes/Palyazat_kiiras/Ghidul-solicitantului-Mobilitate-Verde-IMM-2025.md` (94 oldal RO)
- **Béla bácsi telefon:** 0744-291.872
- **Notariát Béla bácsi:** BNP Munteanu (cégalapításnál és bérleti szerződésnél is)
- **Béla bácsi notarája:** Andrei Munteanu (felajánlott act adițional és declarație notarială)

---

**Megjegyzés:** Ha új információ jön (új email, új szerződés, új TODO), én MAGAM frissítem ezt a fájlt minden új sessionkor — szóljatok ha valamit észrevettek, ami nincs itt.
