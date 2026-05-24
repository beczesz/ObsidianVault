---
title: 00_OPEN_QUESTIONS
generated_by: librarian v0.5
generated_at: 2026-05-22T10:00:00
scope: /Users/becze-mac/My Drive (beczesz.szabolcs@gmail.com)/0. Ideas Vault/01_Projects/Gergely István
mode: index
file_count: 25
id: 77e84704-23b7-4725-b53b-0ec56ba4c952
index_schema_version: 1
---

# 00_OPEN_QUESTIONS — Gergely István projekt

> Forrás: a szintézis fájlokban jelölt nyitott kérdések, "visszaigazolás szükséges" megjegyzések, anomáliák. Prioritás: kritikus (blokkolja az értelmezést) → fontos → alacsony.

---

## LEZÁRT kérdések

### ~~K-01~~ — GERDIT számlák jellege: eladás vagy beszerzés? — MEGOLDVA
- **Megoldás:** A GERDIT **eladási** számlákat tartalmaz. Bizonyíték: Adaos kasszás (4 928 463) + P2025 B2B (696 177) = 5 624 640 ≈ GERDIT 5 623 663; eltérés −977 lej (0,017%).
- **Forrás:** `Szintezisek/06_Tovabbi_felismeresek.md` — "A csatornák összeállnak" szakasz
- **Átvezetve:** `00_DECISIONS_INDEX.md` É-01 (lezárt döntés)

---

## KRITIKUS — visszaigazolás nélkül az értelmezési keret bizonytalan

### K-02 — Gestiune-ok pontos jellege
- **Kérdés:** Melyik gestiune bolt, melyik nagyker, van-e közraktár, online egység vagy más speciális telephely?
- **Miért kritikus:** A kasszás (Adaos) és számlás (ZGY/P2025) csatorna gestiune-szintű szétválasztása ettől függ.
- **Jelenlegi feltételezés:** Névből következtetve: BIRGITA, MUSKATLI, SZEGEDI, VEGYESKE, ZETEKINCSE = boltok; NAGYKERESKEDES = nagyker.
- **Forrás:** `Szintezisek/00_Attekintes.md` — gestiune-táblázat lábj.; `Szintezisek/01_PTOT_keszletmozgas.md`
- **Akció:** Tulajdonosi listát bekérni (gestiune neve → típus → cím).

---

## FONTOS — elemzési mélységet befolyásolja

### F-01 — Intrari tartalmaz-e gestiune-közi áthelyezést?
- **Kérdés:** A PTOT `Intrari` (bevételezés) oszlopa keveri-e a **külső beszerzést** és a **gestiune-ok közti belső áthelyezést**?
- **Következmény:** Ha igen, a hálózati nettó vásárlás kisebb, mint a gestiune-szintű Intrari-összeg — a hálózati készletforgás torzul.
- **Forrás:** `Szintezisek/01_PTOT_keszletmozgas.md` — "Nyitott kérdés" szakasz
- **Akció:** Egy mintavétel: keressünk egy tételt, amelynek az egyik gestiune Iesiri-je megegyezik egy másik Intrari-jával és nincs külső partner.

### F-02 — November B2B mélypontjának oka
- **Kérdés:** Mi magyarázza a november drastikus B2B visszaesését (27 227 RON, a nyári csúcs ~40%-a)?
  - a) Szezonális vége (HoReCa partner inaktív)
  - b) Egy-két nagy vevő kiesése / szüneteltetése
  - c) Adathiány (csonka exportált időszak)
- **Kontextus (06 szintézis):** A teljes árbevételben nincs novemberi összeomlás (405 e lei); a gödör kizárólag a B2B csatornáé — HoReCa/turizmus szezonvég valószínűsíthető.
- **Forrás:** `Szintezisek/04_P2025_szamla_profit.md`; `Szintezisek/06_Tovabbi_felismeresek.md` — "Szezonalitás" szakasz
- **Akció:** A ZGY partner listán november-aktív vs. inaktív vevők szűrése; tulajdonosnál rákérdezni.

### F-03 — NAGYKERESKEDES két számlasorozata
- **Kérdés:** A NAGYKERESKEDES-nél megfigyelt **4-jegyű (F/3xxx, ~118 db)** és **5-jegyű (F/11xxx, ~1 002 db)** sorozat mit jelent? Két kassza? Két dokumentumtípus? Évközben váltott sorozat?
- **Forrás:** `Szintezisek/05_GERDIT_szamlaregiszter.md` — "Két számlasorozat" bekezdés
- **Akció:** A sorozatokat dátum szerint szétválasztani, megnézni hol van a törés.

### F-04 — Besorolatlan "Total..." sor az Adaos-ban
- **Kérdés:** Az első, név nélküli "Total ...»" sor (forgalom: 90 231 RON, árrés: 63 326 RON, **70,2%**) milyen árucsoportot takar?
- **Miért fontos:** A 70,2%-os árrés rendkívüli — valószínűleg gyűjtő vagy számítási artefakt; ha valós, akkor kiemelkedő profittétel.
- **Forrás:** `Szintezisek/03_Adaos_arres.md` — "Az első, név nélküli Total... sor" bekezdés
- **Akció:** Az Excel forrásban szűrővel azonosítani, milyen cikkcsoport kerül ide.

### F-05 — Cikkszintű árrés (cikk → kategória megfeleltetés hiányzik)
- **Kérdés:** Melyik egyedi termék mennyit keres? A PTOT cikkszintű mozgásadatokat tartalmaz, de nincs kategória oszlop — így a kategóriánkénti Adaos árrés nem vetíthető rá cikkszinten.
- **Miért fontos:** Konkrét termék-jövedelmezőség csak cikk → kategória mapping után számítható.
- **Jelenlegi állapot:** A kulcsszavas meta-kategorizálás ~74%-ot fed le (data_v2.json); a maradék ~26% besorolatlan.
- **Forrás:** `Szintezisek/07_Dashboard_es_leszallitottak.md` — "Következő lépés"; `Szintezisek/08_Adatkero_lista.md` — #3 pont
- **Akció:** Cikktörzs export bekérése a forrásrendszerből a „grupa/clasa" (árucsoport) oszloppal (adatkérő #3 megoldja).

### F-06 — Telephelyenkénti árrés (gestiune-bontott Adaos hiányzik) — ADATKÉRŐRE VÁR
- **Kérdés:** Melyik bolt mennyire jövedelmező? Az Adaos jelenleg hálózati összesített — gestiune-szintű árrés nem látható.
- **Miért fontos:** Telephely-szintű döntések (fejlesztés, árstratégia, sortiment) ehhez kellenének. A becsült profit szándékosan kikerült a dashboardból (ELV, M-07).
- **Forrás:** `Szintezisek/08_Adatkero_lista.md` — #1 pont (prioritás: legfontosabb); `Szintezisek/07_Dashboard_es_leszallitottak.md` — "Következő lépés"
- **Akció:** "Adaos pe gestiuni" / gestiune-bontott árrés riport bekérése (adatkérő #1 — legmagasabb prioritás).

### F-07 — Partner × idő kereszttábla (számlaszintű export hiányzik) — ADATKÉRŐRE VÁR
- **Kérdés:** Melyik B2B vevő mikor vásárolt, és mennyit profitált a cégnek?
- **Miért fontos:** A ZGY (partner) és P2025 (idő) önmagában nem köthető össze; November-felelős partner nem azonosítható.
- **Forrás:** `Szintezisek/08_Adatkero_lista.md` — #2 pont; `Szintezisek/02_ZGY_partnerek.md`; `Szintezisek/04_P2025_szamla_profit.md`
- **Akció:** Számlaszintű export bekérése (partner + dátum + összeg + önköltség) a forrásrendszerből — „Jurnal de vânzări" (adatkérő #2).

---

## ALACSONY — finomítás, de nem blokkoló

### A-01 — Partnerenkénti profit
- **Kérdés:** Melyik B2B vevő mennyi profitot termel (nem csak forgalmat)?
- **Jelenlegi állapot:** A ZGY fájl csak forgalmat ad; a P2025 csak összesített profitot idő szerint. (Részben átfed F-07-tel — az F-07 megoldása ezt is megoldja.)
- **Forrás:** `Szintezisek/02_ZGY_partnerek.md`; `Szintezisek/04_P2025_szamla_profit.md`

### A-02 — ASOCIATIA SPORTIVA "FEEL GOOD" kerekítési maradék
- **Kérdés:** Az ~1.5e-14 lei értékű sor véletlen kerekítési artefakt, vagy rögzítési hiba?
- **Forrás:** `Szintezisek/02_ZGY_partnerek.md` — "Hosszú farok" bekezdés
- **Akció:** Az Excel forrásban ellenőrizni; ha 0, az exportból kiszűrni.

### A-03 — Operat ≠ DA sorok a GERDIT-ben
- **Kérdés:** Van-e könyveletlen (Operat = NU) számla a regiszterben, és ha igen, melyik gestiune-ban?
- **Forrás:** `Szintezisek/05_GERDIT_szamlaregiszter.md` — "Operat = DA mező" bekezdés
- **Akció:** Szűrés a forrás Excelben; ha van NU sor, összegeik a könyveletlen forgalmat jelzik.

### A-04 — ZETEKINCSE nyitó dátuma
- **Kérdés:** Pontosan mikor nyílt a ZETEKINCSE egység 2025-ben?
- **Forrás:** `Szintezisek/01_PTOT_keszletmozgas.md` + `Szintezisek/00_Attekintes.md`
- **Akció:** GERDIT-ben ZETEKINCSE legkorábbi F/-dátumának meghatározása.

### A-05 — Meta-kategória "Egyéb / technikai" 68,7%-os árrése
- **Kérdés:** Az "Egyéb / technikai" csoport (94 467 RON forgalom, 68,7% árrés) mit tartalmaz — valós kategória vagy a besorolatlan "Total..." sorral azonos artefakt?
- **Forrás:** `Szintezisek/07_Dashboard_es_leszallitottak.md` — "Mire költenek" táblázat; összefügg F-04-gyel
- **Akció:** Cikktörzs érkezésekor (adatkérő #3) tisztázódik.
