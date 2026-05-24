# Javasolt mappastruktúra — TransOffice/

**Készült:** 2026-05-13 (F1 kimenet)
**Mit látsz alább:** a Cowork által javasolt és elvégzett rendezés, amit én MÁR meg is csináltam (lásd `_BACKUP_2026-05-13/`-ban az eredeti állapot).

---

## Rendezett struktúra

```
TransOffice/
│
├── 00_Aktualis/                       ← amit napi szinten használunk
│   ├── keszlet_aktualis.xlsx           [eredetiből áthelyezve]
│   ├── rendeles_naplo.xlsx             [eredetiből áthelyezve — 2024 oktoberben abbamaradt!]
│   └── arak_2023.xlsx                  ⚠️ átnevezésre vár: arak_2025.xlsx (frissítendő)
│
├── 01_Szerzodesek/                    ← jogi dokumentumok
│   ├── Telephely/
│   │   ├── szerzodes_chirie_TransOffice_2018.docx     [eredetiből áthelyezve]
│   │   └── (Béla bácsi 2025-02-26 válasza — emailbe kerül vagy ide is)
│   ├── Beszallitok/
│   │   ├── szerzodes_PaperWorld_2021.docx              [Aláírt verzió: .pdf]
│   │   ├── szerzodes_PaperWorld_2021.pdf
│   │   └── szerzodes_BicoToner_2022.docx               ⚠️ lejár 2025-06-01 — döntés kell márciusig
│   └── Ugyfelek/
│       └── (egyelőre nincs egyedi szerződés — jövőbeli)
│
├── 02_Penzugy/                        ← könyvelői dokumentumok
│   ├── eves_jelentes_2022.xlsx          [Ilona/-ból áthelyezve — utolsó komplett éves]
│   ├── szamlak_2023/                    [Ilona/-ból áthelyezve, README.txt benne]
│   └── (2023-2024-es bilanț — Mihaelától kell kérni)
│
├── 03_Ertekesites/                    ← ajánlatok, ügyfél-adatok
│   ├── ajanlat_InfoTech_2024.docx       [eredetiből áthelyezve]
│   ├── ugyfelek_master.xlsx              ⚠️ később generáljuk — a 3 listából
│   └── _archivum/                       ← régi listák (historikus érték)
│       ├── ugyfelek_2019.xlsx
│       ├── ugyfelek_VEGLEGES.xlsx       (2022-es)
│       └── ugyfelek_uj_marton.xlsx      (2024-es kezdemény)
│
├── 04_Meetings/                       ← minden meeting-jegyzet egy helyen
│   ├── meeting_marton_20241105.docx
│   ├── meeting_marton_20250112.docx
│   └── meeting_transcript_20250224.srt   🌟 F2 kiindulópont — pályázati meeting
│
├── 05_Levelezes/                      ← archív emailek (export TXT-k)
│   ├── beerkezo/
│   │   ├── felszolitas_BicoToner.txt              ⚠️ aktív tartozás
│   │   ├── reklamacio_OrbanUgyvedi.txt            ⚠️ státusz?
│   │   ├── rendeles_HegyiZoli.txt
│   │   ├── rendeles_visszaigazolas_PaperWorld.txt
│   │   └── raspuns_bela_iosif_2025-02-26.txt      🌟 AFM-stabilitás
│   └── kimeno/
│       └── emlekezteto_marton_sajat.txt           (önemlékeztető)
│
├── 06_Marketing_Honlap/               ← weboldal-anyagok
│   └── honlap_szoveg_2012.docx          ⚠️ 13 éves — F6 fázisban dolgozzuk fel
│
├── _archive_Ilona/                    ← Ilona történeti hagyatéka (NE törölni!)
│   ├── cetlik.txt
│   ├── ugyfel_megjegyzesek.docx
│   └── szallitok_lista_regi.xlsx
│
├── _BIZALMAS/                         ← érzékeny adatok (titkosítva tartani)
│   └── jelszavak.txt                    🚨 Mártonnak átvinni jelszókezelőbe (1Password / Bitwarden)
│
├── _Kuka/                             ← töröltek (rollback-re megmaradnak 1 hónapig)
│   ├── lu45pmb3.tmp                    (Office temp, 39 KB)
│   ├── .~lock.szerzodes_PaperWorld_2021.pdf#
│   ├── .DS_Store
│   ├── foto_unoka_2023.txt             (Ilona/-ból)
│   ├── receptek_krumplis.docx           (Ilona/-ból)
│   ├── meeting_marton_20241105.docx_DUP (root-szintű dupla)
│   └── meeting_marton_20250112.docx_DUP (root-szintű dupla)
│
└── _BACKUP_2026-05-13/                ← TELJES EREDETI állapot, érintetlen
    └── (34 fájl változatlanul — bármikor visszanyerhető)
```

---

## Elvi szempontok

1. **`00_` prefix** = "aktuális, ezt használom napi szinten"
2. **`0X_` prefixek** növekvő sorrendben az életciklus szerint (szerződéskötés → pénzügy → értékesítés → meeting → email → marketing)
3. **`_archive_` prefix** = nem napi munka, de NE töröld
4. **`_BIZALMAS/`** = jelszavak, banki adatok, érzékeny személyes adatok
5. **`_Kuka/`** = törölhető 1 hónap múlva (rollback időszak)
6. **`_BACKUP_DATUM/`** = teljes eredeti pillanatkép — ne piszkáld

---

## Mit NEM csináltam (és miért nem)

- **Nem egyesítettem a 3 ügyféllistát** → ez egy érzékeny adatmunkálat, döntést igényel (melyik a legfrissebb mező?). Külön task lesz F2 után, Mártonnal együtt.
- **Nem nyitottam meg az érzékeny pénzügyi adatokat** → a `bilant` típusú információk a könyvelőtől jönnek (Mihaela), F4-ben kérjük.
- **Nem töröltem semmit véglegesen** → minden a `_Kuka/` vagy `_BACKUP_2026-05-13/` alatt megőrződik.
- **A `Marketing/honlap_szoveg_2012.docx`-et nem dobtam a kukába** — F6 fázisban viszont szükséges lesz (a régi szöveg az új weboldal kiindulópontja).

---

## Mit kérdezzek vissza Mártontól?

1. **CUI (adószám)** — a fájlokban sehol nem találtam, de a pályázathoz biztosan kell.
2. **A 3 ügyféllista közül melyik a "vezérlő"?** (vagy mind a 3 kell külön?)
3. **BicoToner-szerződés: meghosszabbítani vagy felmondani?** (március előtt kell dönteni)
4. **dr. Orbán Csilla reklamáció (2024-09-18) — le lett-e zárva?** Ha nem, gyorsan reagálni kell.
5. **Mihaela Florian elérhetősége** — még nem találtam emailcímét. Honnan szerzem be?

---

**A `01_ceg_attekintes/` mappám a Cowork projekt-kontextusába be van állítva**, így minden következő F2-F6 fázis ezekre tud építeni.
