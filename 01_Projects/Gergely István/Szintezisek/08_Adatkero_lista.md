---
title: "Adatkérő lista a tulajdonosnak — mit exportáljon és miért"
description: "Adott 5 aggregált riporthoz szükséges 4 adatkérés részletezése: telephelyi árrés-bontás, számlaszintű vevő-önköltség lista, cikk-kategória megfeleltetés és opcionális cikkszintű telephely-bontás, mind meglévő rendszerből exportálható."
description_source: auto
description_hash: 6932923dcdbe8797
type: data-request
project: Gergely István
created: 2026-05-21
tags: [data-request, next-steps]
id: b4125b11-c689-491f-b5fb-0c1fcc4da790
index_schema_version: 1
---
# Adatkérő lista — pontosan mit kérjünk, és miért

A jelenlegi 5 fájl **összegzett (aggregált) riport**. A mélyebb elemzéshez 4 dologra van szükség.
Mindegyiknél leírom: **mi az, miért kell, és milyen formában**.

---

## 1. Telephelyenként (gestiune-onként) bontott árrés / önköltség riport
**Mi ez:** ugyanaz, mint az `Adaos total 2025`, de **nem összevontan az egész cégre, hanem
telephelyenként** (BIRGITA, MUSKATLI, SZEGEDI, VEGYESKE, NAGYKERESKEDES, ZETEKINCSE).
Oszlopok telephelyenként: eladási érték, önköltség (cost), árrés (adaos).

**Miért kell:** most a **profitot üzletenként csak BECSÜLNI tudjuk** a hálózati átlag-árréssel (23,7%).
Ez torzít: a NAGYKERESKEDES (nagyker) árrése biztosan alacsonyabb, egy belvárosi bolté magasabb lehet.
Telephelyi önköltséggel a **valós profit/üzlet** kiszámolható, nem becsült.

**Formátum:** a szoftver „Adaos pe gestiuni" / „árrés raktáranként" riportja, Excelbe.
*Kulcsszó a rendszerben (WinMENTOR-szerű): „Adaos comercial" szűrve gestiune-ra.*

---

## 2. Számlaszintű (tételes) értékesítési lista: dátum + partner + érték + önköltség
**Mi ez:** egy sor = egy számla, oszlopok: **dátum, vevő neve, telephely, nettó érték, önköltség**.
(A `TOTAL GERDIT` már majdnem ez — de **nincs benne a vevő neve és az önköltség**.)

**Miért kell:** ezzel összeköthető a **partner és az idő** (most a `ZGY` csak partnert, a `P2025`
csak időt tud). Megválaszolható: *melyik vevő mikor, mennyit és milyen profittal vásárolt;
ki a növekvő/zsugorodó vevő; van-e szezonális vevő.*

**Formátum:** „Jurnal de vânzări" / értékesítési napló, vevővel és önköltséggel, Excelbe.

---

## 3. Cikktörzs kategória-megfeleltetéssel (cikk → árucsoport)
**Mi ez:** egy lista, ami minden cikkhez megadja, **melyik árucsoportba tartozik**
(pl. „BERE BUCEGI 0.5" → kategória „BERE").

**Miért kell:** a `PTOT` cikkenkénti **mennyiséget** ad, az `Adaos` kategóriánkénti **árrést**.
A kettő összekötésével **cikkszintű jövedelmezőség** számolható: nem csak hogy a sör jó kategória,
hanem *konkrétan melyik sör hozza a legtöbb árréstömeget*. Ez kell a polc-optimalizáláshoz.

**Formátum:** a cikktörzs export (Nomenclator articole) a „grupa/clasa" oszloppal, Excelbe.

---

## 4. (Opcionális, de erős) Cikkszintű eladási érték + önköltség telephelyenként
**Mi ez:** cikkenként + telephelyenként: eladott mennyiség, eladási érték, önköltség.

**Miért kell:** ez a „szent grál" — ezzel **minden** felbontható (cikk × telephely × árrés),
és a dashboard teljes drill-down képességet kap. Ha túl nagy, a 3. pont (kategória-mapping) is
elég a legtöbb elemzéshez.

**Formátum:** „Fișa de magazie valorică" / értékkészlet-karton, vagy értékesítés cikk+gestiune
bontásban, Excelbe.

---

## Prioritási sorrend
1. **#1 (telephelyi árrés)** — azonnal megadja a valós profit/üzletet. *Legnagyobb haszon, kis meló.*
2. **#3 (kategória-mapping)** — cikkszintű árrés, polc-döntésekhez.
3. **#2 (számlaszintű vevő+önköltség)** — B2B vevő-jövedelmezőség és időbeli vevőelemzés.
4. **#4** — ha könnyen exportálható, mindent megnyit; ha nehéz, kihagyható.

> Mind a 4 a meglévő rendszerből kijön (csak más riport-nézet), **nem kell új adatrögzítés.**

Kapcsolódó: [[07_Dashboard_es_leszallitottak]] · [[00_Attekintes]]
