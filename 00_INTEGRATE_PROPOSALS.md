---
title: 00_INTEGRATE_PROPOSALS
description: Librarian integrate mode scan of Downloads/munka/ (7 source groups, ~1.4 GB total). 52 fájl vizsgálva. 6 HIGH confidence javaslat (kliens dokumentumok, workshop transzkriptek, md fájlok), 26 MEDIUM (Benedek Dezso SRT sorozat, Személyes admin), 11 LOW (nagy médiafájlok), 12 SKIP (már a vaultban vagy git repo).
generated_by: librarian v0.8.3
generated_at: 2026-06-07
mode: integrate
external_scope: /Users/becze-mac/Downloads/munka/
id: a3f7c291-5e8b-4d09-b1e4-7c9d20f83a14
index_schema_version: 1
---

# Downloads/munka Integration Proposals
_Generated: 2026-06-07 | Librarian integrate mode v0.8.3_

> Ez a fájl felváltja a korábbi (2026-05-11) IgnisAcedemy-scope javaslatot. Az IgnisAcedemy javaslatok ebben a scan-ben NEM szerepelnek (különböző scope).

---

## Summary

| | |
|---|---|
| Vizsgált forrás | `/Users/becze-mac/Downloads/munka/` |
| Vizsgált fájlok (kb.) | 95 (7 forráscsoport, ~1.4 GB) |
| HIGH confidence javaslat | 8 |
| MEDIUM confidence | 26 |
| LOW confidence (nagy média) | 11 |
| SKIP (már a vaultban / git repo / byte-azonos) | 12 |

---

## Proposals

### CPS/Accounts — kliens dokumentumok

| Confidence | Forrás (relatív) | Javasolt vault cél | Megjegyzés |
|---|---|---|---|
| HIGH | `CPS/Accounts/HLB/Egyedi megrendelőlap_Sonrisa_graylog_fix price_250618.pdf` | `02_Areas/Sonrisa/CPS/Accounts/Active/HLB/` | Sonrisa-HLB megrendelőlap (200 KB). HLB kliensmappa NEM létezik a vaultban; az összes többi Sonrisa kliens (Onriva, Melinda Steel, stb.) megvan. Kliens-szerződés, releváns. |
| MEDIUM | `CPS/Accounts/Onriva/Onriva_myRiva_2026.02_CaseStudy.docx.pdf` | `02_Areas/Sonrisa/CPS/Accounts/Active/Onriva/` | Onriva Case Study (112 KB, 2026-02). A vaultban már van `Cost Optimization Report - Onriva (Final).pdf` + `v1.pdf`, de a Case Study nincs. Érdemes importálni ha az Onriva engagement él. |
| HIGH | `CPS/Accounts/MelindaSteel/Contr. Sonrisa-Melinda Steel_signed.pdf` | `02_Areas/Sonrisa/CPS/Accounts/Active/Melinda_Steel/` | Aláírt Sonrisa-MelindaSteel szerződés (5.2 MB). A vaultban van `n8n Part 1` és `Part 2` megrendelőlap + tech ajánlat, de az aláírt master szerződés NINCS. Elsőbbségi import. |

### CPS/workshop — Strada Luminisului workshop

| Confidence | Forrás (relatív) | Javasolt vault cél | Megjegyzés |
|---|---|---|---|
| HIGH | `CPS/workshop/Strada Luminișului.txt` | `02_Areas/ExarLabs/resources/workshops/strada-luminisului/` | Workshop transzkript szöveg (Plaud). Nincs a vaultban. Célmappa (`workshops/`) nem létezik, létre kell hozni. |
| HIGH | `CPS/workshop/Strada Luminișului 2.txt` | `02_Areas/ExarLabs/resources/workshops/strada-luminisului/` | Workshop transzkript szöveg 2. változat (Plaud). Nincs a vaultban. |
| LOW | `CPS/workshop/Strada Luminișului.m4a` | `02_Areas/ExarLabs/resources/workshops/strada-luminisului/audio/` | Eredeti workshop felvétel (~43-49 MB becsült). Van txt pár, az m4a LOW priority. Csak akkor érdemes, ha az audio archív értékű. |
| LOW | `CPS/workshop/Strada Luminișului 2.m4a` | `02_Areas/ExarLabs/resources/workshops/strada-luminisului/audio/` | Eredeti workshop felvétel 2. változat. Ld. fent. |

### CPS/Webpage — UI design assets

| Confidence | Forrás (relatív) | Javasolt vault cél | Megjegyzés |
|---|---|---|---|
| MEDIUM | `CPS/Webpage/check icon.png` | `02_Areas/Sonrisa/CPS/Administration/assets/` vagy `02_Areas/ExarLabs/design/` | UI check icon (20 KB). Sonrisa CPS weboldalhoz készült design asset valószínuleg. Vault célterülete nem egyértelmű (nincs `assets/` mappa a CPS-ben). |
| MEDIUM | `CPS/Webpage/check icon 2.png` | Ld. fent | UI check icon variáns (28 KB). |
| MEDIUM | `CPS/Webpage/check_icon.zip` | Ld. fent | Check icon bundle (392 KB). Ha az egyedi PNG-k importálva, a zip skip. |

### ExarLabs — md fájlok + git repók

| Confidence | Forrás (relatív) | Javasolt vault cél | Megjegyzés |
|---|---|---|---|
| SKIP | `ExarLabs/BDOS_vs_marveen_osszehasonlitas.md` | `02_Areas/ExarLabs/resources/` | BYTE-AZONOS másolat: md5 `725133775f...` megegyezik a vaultban lévővel. Törölhető az original. |
| SKIP | `ExarLabs/marveen_tanulsagok_BDOS-nak.md` | `02_Areas/ExarLabs/resources/` | BYTE-AZONOS másolat: md5 `0f7e57a845...` megegyezik a vaultban lévővel. Törölhető az original. |
| SKIP | `ExarLabs/microsite-factory/` | n/a | `.git/` mappa megvan: git repo, NEM importálható. |
| SKIP | `ExarLabs/ExarSharedBrain/` | n/a | `.git/` mappa megvan: git repo, NEM importálható. |
| SKIP | `ExarLabs/marveen/` | n/a | `.git/` mappa megvan: git repo, NEM importálható. |
| MEDIUM | `ExarLabs/sonrisa-partner-header/` (index.html + assets/) | `02_Areas/Sonrisa/sonrisa-partner-header/` | HTML/CSS microsite töredék, NEM git repo. A vaultban `02_Areas/Sonrisa/sonrisa-partner-header` MÁR LÉTEZIK. Ellenőrizni kell hogy azonos-e a tartalom (md5 check ajánlott fájlonként) mielőtt importálnánk. Várható: SKIP vagy frissebb verzió. |

### Navigátor/Benedek Dezső — antropológiai kurzus (EP01-EP19)

A kurzus 19 epizódból áll. Minden epizódhoz MP3 + SRT pár létezik a forrásban. A vaultban Benedek Dezső könyvtár NEM létezik (`03_Resources/03_Podcasts/Benedek-Dezso/` hiányzik).

| Confidence | Forrás (relatív) | Javasolt vault cél | Megjegyzés |
|---|---|---|---|
| MEDIUM | `Navigátor/Benedek Dezső/EP01 - Kurzus bevezető és személyes életút.srt` | `03_Resources/03_Podcasts/Benedek-Dezso/EP01 - Kurzus bevezeto es szemelyes eletat.srt` | 80 KB. SRT = tényleges szöveges tartalom, kereső- és feldolgozható. |
| MEDIUM | `Navigátor/Benedek Dezső/EP02 - Tulajdonviszonyok és melanéziai kultúra.srt` | `03_Resources/03_Podcasts/Benedek-Dezso/` | 36 KB |
| MEDIUM | `Navigátor/Benedek Dezső/EP03 - Antropológiai alapfogalmak és energetika.srt` | `03_Resources/03_Podcasts/Benedek-Dezso/` | 84 KB |
| MEDIUM | `Navigátor/Benedek Dezső/EP04 - Ausztronéziai térség és Tau népcsoport.srt` | `03_Resources/03_Podcasts/Benedek-Dezso/` | 44 KB |
| MEDIUM | `Navigátor/Benedek Dezső/EP05 - Teknonymia és társadalmi szerveződés.srt` | `03_Resources/03_Podcasts/Benedek-Dezso/` | 68 KB |
| MEDIUM | `Navigátor/Benedek Dezső/EP06 - Halászati technikák és nyelvészeti összehasonlítás.srt` | `03_Resources/03_Podcasts/Benedek-Dezso/` | kb. 50-80 KB |
| MEDIUM | `Navigátor/Benedek Dezső/EP07 - Halfajok, gúnynevek és mágia pszichológiája.srt` | `03_Resources/03_Podcasts/Benedek-Dezso/` | kb. 50-80 KB |
| MEDIUM | `Navigátor/Benedek Dezső/EP08 - Tabuk és funkcionalista mitológia.srt` | `03_Resources/03_Podcasts/Benedek-Dezso/` | kb. 50-80 KB |
| MEDIUM | `Navigátor/Benedek Dezső/EP09 - Rituálék és halálsziklák.srt` | `03_Resources/03_Podcasts/Benedek-Dezso/` | kb. 50-80 KB |
| MEDIUM | `Navigátor/Benedek Dezső/EP10 - Polipfogás és kulturális változás.srt` | `03_Resources/03_Podcasts/Benedek-Dezso/` | kb. 50-80 KB |
| MEDIUM | `Navigátor/Benedek Dezső/EP11 - Sámánizmus és orális hagyományok.srt` | `03_Resources/03_Podcasts/Benedek-Dezso/` | kb. 50-80 KB |
| MEDIUM | `Navigátor/Benedek Dezső/EP12 - Betegség, gyógyítás és erkölcsi dilemmák.srt` | `03_Resources/03_Podcasts/Benedek-Dezso/` | kb. 50-80 KB |
| MEDIUM | `Navigátor/Benedek Dezső/EP13 - Marapuná gyöngyök nyomozása.srt` | `03_Resources/03_Podcasts/Benedek-Dezso/` | kb. 50-80 KB |
| MEDIUM | `Navigátor/Benedek Dezső/EP14 - Etnográfiai dokumentáció és revitalizáció.srt` | `03_Resources/03_Podcasts/Benedek-Dezso/` | kb. 50-80 KB |
| MEDIUM | `Navigátor/Benedek Dezső/EP15 - Vietnámi expedíció és ősi civilizációk.srt` | `03_Resources/03_Podcasts/Benedek-Dezso/` | kb. 50-80 KB |
| MEDIUM | `Navigátor/Benedek Dezső/EP16 - Aura látás és spirituális jelenségek.srt` | `03_Resources/03_Podcasts/Benedek-Dezso/` | kb. 50-80 KB |
| MEDIUM | `Navigátor/Benedek Dezső/EP17 - Tudatosság és távoli látás.srt` | `03_Resources/03_Podcasts/Benedek-Dezso/` | kb. 50-80 KB |
| MEDIUM | `Navigátor/Benedek Dezső/EP18 - Civilizációk és filozófiai összegzés.srt` | `03_Resources/03_Podcasts/Benedek-Dezso/` | kb. 50-80 KB |
| MEDIUM | `Navigátor/Benedek Dezső/EP19 - Marapona gyöngyök és záró rituálék.srt` | `03_Resources/03_Podcasts/Benedek-Dezso/` | kb. 50-80 KB |
| MEDIUM | `Navigátor/Benedek Dezső/Jegyzetek.pdf` | `03_Resources/03_Podcasts/Benedek-Dezso/Benedek-Dezso-jegyzetek.pdf` | Kurzusjegyzetfüzet (780 KB). Társ-anyag az SRT-ekhez. Érdemes együtt importálni. |
| MEDIUM | `Navigátor/Benedek Dezső/Documents/Factura-Z1_bwrrayrvrc4gqptfkufzynykmq5q5.pdf` | `02_Areas/Személyes/admin/szamlak/` vagy `02_Areas/ExarLabs/Clients/<kurzus-klienshez>/` | Számla (272 KB). Ha a Benedek Dezső kurzus ExarLabs ügylethez kötődik, az az ExarLabs célterület; ha személyes, `Személyes/admin/`. Döntést igényel. |
| LOW | `Navigátor/Benedek Dezső/EP01 - Kurzus bevezető és személyes életút.mp3` | `03_Resources/03_Podcasts/Benedek-Dezso/audio/` | ~25-40 MB/ep, összesen ~400-600 MB az összes MP3. Van SRT pár minden epizódhoz. LOW confidence (nagy méret, SRT fedezi a tartalmat). |
| LOW | `Navigátor/Benedek Dezső/EP02-EP19 MP3-ok` (18 fájl) | `03_Resources/03_Podcasts/Benedek-Dezso/audio/` | Ld. EP01 megjegyzés. Összesen 18 további MP3 fájl. Ha az audio archív célt szolgál (reel-factory, Presto) érdemes; egyébként SRT elegendő. |

### teambuildin Sovata 2026 — workshop felvételek

A vault Sovata SRT gyűjteménye részben kész: `02_Areas/ExarLabs/events/2026 május 30 Szováta/`.

| Confidence | Forrás (relatív) | Javasolt vault cél | Megjegyzés |
|---|---|---|---|
| HIGH | `teambuildin Sovata 2026/Sovata 11.srt` | `02_Areas/ExarLabs/events/2026 május 30 Szováta/whisper/Sovata 11.srt` | HIÁNYZIK a vaultból. A whisper mappában van: 9, 10, 12, 13 — de 11 hiányzik. Ez a single legfontosabb missing file. |
| SKIP | `teambuildin Sovata 2026/Sovata 9.srt` | `02_Areas/ExarLabs/events/2026 május 30 Szováta/whisper/` | MÁR a vaultban van (whisper/Sovata 9.srt). |
| SKIP | `teambuildin Sovata 2026/Sovata 10.srt` | `02_Areas/ExarLabs/events/2026 május 30 Szováta/whisper/` | MÁR a vaultban van (whisper/Sovata 10.srt). |
| SKIP | `teambuildin Sovata 2026/Sovata 12.srt` | `02_Areas/ExarLabs/events/2026 május 30 Szováta/whisper/` | MÁR a vaultban van (whisper/Sovata 12.srt). |
| SKIP | `teambuildin Sovata 2026/Sovata 13.srt` | `02_Areas/ExarLabs/events/2026 május 30 Szováta/whisper/` | MÁR a vaultban van (whisper/Sovata 13.srt). |
| SKIP | `teambuildin Sovata 2026/Sovata 9-transcript-plud.srt` | `02_Areas/ExarLabs/events/2026 május 30 Szováta/plaud/` | MÁR a vaultban van (plaud/Sovata 9-transcript-plud.srt). |
| SKIP | `teambuildin Sovata 2026/Sovata 10-transcript-plaud.srt` | `02_Areas/ExarLabs/events/2026 május 30 Szováta/plaud/` | MÁR a vaultban van (plaud/Sovata 10-transcript-plaud.srt). |
| SKIP | `teambuildin Sovata 2026/Sovata 11-transcript-plaud.srt` | `02_Areas/ExarLabs/events/2026 május 30 Szováta/plaud/` | MÁR a vaultban van (plaud/Sovata 11-transcript-plaud.srt). |
| SKIP | `teambuildin Sovata 2026/Sovata 13-transcript-Plaud.srt` | `02_Areas/ExarLabs/events/2026 május 30 Szováta/plaud/` | MÁR a vaultban van (plaud/Sovata 13-transcript-Plaud.srt). |
| LOW | `teambuildin Sovata 2026/Sovata 9.m4a` | `02_Areas/ExarLabs/events/2026 május 30 Szováta/audio/` | 59 MB. Van SRT pár (whisper + plaud). LOW confidence. |
| LOW | `teambuildin Sovata 2026/Sovata 10.m4a` | `02_Areas/ExarLabs/events/2026 május 30 Szováta/audio/` | 43 MB. Van SRT pár. |
| LOW | `teambuildin Sovata 2026/Sovata 11.m4a` | `02_Areas/ExarLabs/events/2026 május 30 Szováta/audio/` | 49 MB. Van SRT pár (plaud). |
| LOW | `teambuildin Sovata 2026/Sovata 12.m4a` | `02_Areas/ExarLabs/events/2026 május 30 Szováta/audio/` | 43 MB. Van SRT pár (whisper). |
| LOW | `teambuildin Sovata 2026/Sovata 13.m4a` | `02_Areas/ExarLabs/events/2026 május 30 Szováta/audio/` | 49 MB. Van SRT pár. |

### Navigátor/KAW — részben integrálva

| Confidence | Forrás (relatív) | Javasolt vault cél | Megjegyzés |
|---|---|---|---|
| SKIP | `Navigátor/KAW/Episodes/KAW 01.mp4` | `02_Areas/Navigátor Podcast/KAW/Episodes/` | MÁR a vaultban van. |
| SKIP | `Navigátor/KAW/Episodes/KAW 02.mp4` | `02_Areas/Navigátor Podcast/KAW/Episodes/` | MÁR a vaultban van. |
| SKIP | `Navigátor/KAW/Episodes/KAW 03.mp4` | `02_Areas/Navigátor Podcast/KAW/Episodes/` | MÁR a vaultban van. |
| SKIP | `Navigátor/KAW/Episodes/KAW 04.mp4` | `02_Areas/Navigátor Podcast/KAW/Episodes/` | MÁR a vaultban van. |
| SKIP | `Navigátor/KAW/mp3/Betenbough SG_1-6.mp3` (6 fájl) | `02_Areas/Navigátor Podcast/KAW/mp3/` | MIND a 6 Betenbough MP3 MÁR a vaultban van. |
| LOW | `Navigátor/KAW/Episodes/Red and Black Mysterious Audio Wave Video.mp4` | `02_Areas/Navigátor Podcast/KAW/Episodes/` | Már a vaultban VAN. |
| LOW | `Navigátor/KAW/Podcast/EP30 Thumb.png` | `02_Areas/Navigátor Podcast/KAW/Podcast/` | Thumbnail kép, ellenőrizni kell vault-ban van-e. |
| MEDIUM | `Navigátor/KAW/EP30 Podcast-Csala Dénes [...].srt` | `02_Areas/Navigátor Podcast/KAW/` | SRT (Csala Dénes epizód). Ellenőrizni kell a vaultban. Valószínuleg SKIP (az EP30 SRT megvan a vault KAW gyökerében is). |

**Megjegyzés KAW videókhoz:** `KAW 01-04.mp4` mind a vaultban van. A letöltési forrásban is ugyanaz a 4 — nincs KAW 05.mp4 a forrás-mappában (az `Episodes/` alatt). A `KAW 05.mp4` a VAULT-ban van a `Thumbs/` almappában, de a downloads-ban nincs.

### Személyes — román admin dokumentumok

A vaultban `02_Areas/Személyes/` nem rendelkezik `admin/` almappával. Ezek az admin dokumentumok személyes/üzleti adminisztrációs anyagok.

| Confidence | Forrás (relatív) | Javasolt vault cél | Megjegyzés |
|---|---|---|---|
| MEDIUM | `Személyes/Ghidul-IMM-2026.pdf` | `02_Areas/Személyes/admin/roman-admin/` | Román KKV útmutató 2026. Referencia dokumentum. |
| MEDIUM | `Személyes/Ghidul-solicitantului-–-consultare-publica-1.pdf` | `02_Areas/Személyes/admin/roman-admin/` | Pályázati kérelmező útmutató. |
| MEDIUM | `Személyes/formular_D212_2870618194051_2026.pdf` | `02_Areas/Személyes/admin/roman-admin/` | D212 formulár (adóbevallás-jellegű). |
| MEDIUM | `Személyes/activityreport_2026_05.xlsx` | `02_Areas/Személyes/admin/activity-reports/` | Havi activity report (május 2026). |
| MEDIUM | `Személyes/BAYER-BRRA_20260505.xlsx` | `02_Areas/Személyes/admin/` | Bayer-BRRA kapcsolatos tábla. |
| MEDIUM | `Személyes/Referencia_minta sablon ARIBA 1.docx` | `02_Areas/Személyes/admin/` vagy `02_Areas/ExarLabs/resources/` | ARIBA referencia sablon — ha ExarLabs tenderhez kell, az ExarLabs célterület logikusabb. |
| MEDIUM | `Személyes/COMPAS_alapozo_kepzes.docx` | `02_Areas/Személyes/admin/` vagy `03_Resources/` | Alapozó képzés dokumentum. Ha személyes fejlődés, `Személyes`; ha referencia, `03_Resources/`. |
| SKIP | `Személyes/2025_05_29 Fókuszpont/Fókuszpont - 2025 összefoglaló.md` | `02_Areas/Fókuszpont/` | BYTE-AZONOS: md5 `6a17fa8cb6...` megegyezik a vaultban lévővel. |
| MEDIUM | `Személyes/2025_05_29 Fókuszpont/Fókuszpont - 2025 összefoglaló.docx` | `02_Areas/Fókuszpont/` | A `.md` verzió a vaultban van, de a `.docx` nincs. Ha az eredeti Word formátum szükséges (külső megosztáshoz), érdemes importálni. |

---

## Döntést igénylő tételek (LOW confidence)

### Benedek Dezső MP3-ok (EP01-EP19, ~600 MB összesen)
- **Kérdés:** Az audio archív értékű-e (reel-factory, Presto anyaghoz), vagy az SRT transzkripcióval lefedett?
- **Javaslat:** Ha a Navigátor Podcast reel-factory pipeline (BDOS capability) aktív, az MP3-ok értékesek. Egyébként az SRT importja elegendő.
- **Döntés szükséges:** igen/nem + cél.

### Sovata m4a felvételek (5 db, ~240 MB összesen)
- **Kérdés:** A Szováta workshop felvételek archiválandók-e a vaultban (közvetlen audio), vagy elég a transzkripció (SRT)?
- **Javaslat:** Workflow: SRT importálva, m4a maradjon a Downloads-ban, töröljük 30 nap után.
- **Döntés szükséges:** igen/nem.

### CPS Webpage check ikonok
- **Kérdés:** Melyik Sonrisa/ExarLabs projekt használja (vagy fogja használni) ezeket? Nincs egyértelmű célmappa.
- **Javaslat:** Ha aktív design asset, importálandó az érintett projekt design/ mappájába. Ha egyszer volt, skip.

### Benedek Dezső Factura (számla)
- **Kérdés:** ExarLabs-hoz vagy személyes számlához tartozik?
- **Javaslat:** ExarLabs-os számlázásnál: `02_Areas/ExarLabs/Clients/Benedek-Dezso-kurzus/docs/`. Személyes: `02_Areas/Személyes/admin/szamlak/`.

---

## Azonosított vault hiányok (gap-ek)

1. `02_Areas/ExarLabs/Clients/` hiányzó kliensek: **HLB** nem létezik mint kliensmappa (csak Sonrisa-ügylethez van megrendelőlap).
2. `02_Areas/ExarLabs/resources/workshops/` mappa NEM létezik — a Strada Luminisului + esetleg Sovata anyagok célterülete.
3. `03_Resources/03_Podcasts/Benedek-Dezso/` NEM létezik — 19 epizódos kurzus a Navigátor-tól teljesen hiányzik a vaultból.
4. `02_Areas/Személyes/admin/` NEM létezik — admin dokumentumoknak nincs dedikált helye.
5. Sovata 11 whisper SRT HIÁNYZIK a vaultból (plaud megvan, whisper nem).

---

## Ajánlott következő lépések (prioritás sorrendben)

1. **AZONNALI (1 fájl, HIGH, kritikus):** `Sovata 11.srt` (whisper) másolása `02_Areas/ExarLabs/events/2026 május 30 Szováta/whisper/` alá. Ez a sorozat egyetlen hiányzó darabja.

2. **RÖVID TÁVU (3 fájl, HIGH, üzleti):** CPS kliens dokumentumok importja:
   - `Egyedi megrendelőlap_Sonrisa_graylog_fix price_250618.pdf` → új `Sonrisa/CPS/Accounts/Active/HLB/` mappa létrehozásával
   - `Contr. Sonrisa-Melinda Steel_signed.pdf` → `Sonrisa/CPS/Accounts/Active/Melinda_Steel/`
   - `Onriva_myRiva_2026.02_CaseStudy.docx.pdf` → `Sonrisa/CPS/Accounts/Active/Onriva/`

3. **KÖZEPES TÁVU (2 fájl, HIGH, workshop):** Strada Luminisului workshop transzkriptek (`Strada Luminișului.txt` + `Strada Luminișului 2.txt`) — új `02_Areas/ExarLabs/resources/workshops/strada-luminisului/` mappa létrehozásával.

4. **BATCH döntés (19 SRT, MEDIUM):** Benedek Dezső SRT sorozat (EP01-EP19) + `Jegyzetek.pdf` — ha jóváhagyott, egyetlen batch cp parancs elegendő, a célmappa (`03_Resources/03_Podcasts/Benedek-Dezso/`) létrehozásával.

5. **SZEMÉLYES ADMIN (7 fájl, MEDIUM):** `02_Areas/Személyes/admin/` mappa létrehozása + a roman-admin PDF-ek + activity report importja.

6. **TÖRLÉSI JAVASLAT:** `ExarLabs/BDOS_vs_marveen_osszehasonlitas.md` + `ExarLabs/marveen_tanulsagok_BDOS-nak.md` a Downloads-ból byte-azonosan megvan a vaultban — törölhető a forrás.

7. **LOW confidence döntés (embernek):** Benedek Dezső MP3-ok, Sovata m4a-k, CPS check ikonok — lásd "Döntést igénylő tételek" szekció.

---

_Librarian integrate mode — csak javasol, nem mozgat. Az elfogadott javaslatokat tidy mód vagy manuális cp parancsok hajtják végre._
