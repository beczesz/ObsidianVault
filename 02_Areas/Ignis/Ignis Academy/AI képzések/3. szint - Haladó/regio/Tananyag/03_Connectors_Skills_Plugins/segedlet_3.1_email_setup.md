---
title: "Segédlet 3.1: A connector-demó email + csatolmány beállítása (OKTATÓI)"
date: 2026-07-02
author: Becze Szabolcs
status: active
description: "Oktatói segédlet a 3.1 MS365 connector-demóhoz: a kivitelező kísérő emailje (tárgy + feladó + törzs, copy-paste), a csatolandó PDF pontos helye, és a T-5 perces beállítási lépések, hogy amikor a connectoron át megkérdezed 'jött-e új email?', látványosan befusson a várt Napsugár-ajánlat. A csatolmány UGYANAZ a szkennelt PDF, amit az F4-ben OCR-ezünk, így a lánc folytonos."
id: e5b7a6c8-7f9d-4a1b-9c2e-5d6f7a8b9c0d
index_schema_version: 1
bdos_index: true
tags: [ignis-academy, halado, regio-consult, f3, segedlet, connector, oktatoi]
---
# Segédlet 3.1: A connector-demó email + csatolmány (OKTATÓI)

> Ez **csak neked (oktató)** szól. A cél: mielőtt a workshopon a connectoron át megkérdezed „jött-e új email?", tényleg fusson be egy **hiteles ajánlat-email** a bekötött postaládádba. A csatolmány ugyanaz a szkennelt PDF, amit az F4-ben OCR-ezünk.

---

## 1. lépés (T-5 perc): küldd el magadnak az emailt

Küldj egy emailt a **bekötött MS365 (Outlook) postaládád címére**. A feladót állítsd be a kivitelezőre (ha van rá mód: egy másodlagos fiók megjelenített neve „Construct Transilvania SRL"; ha nincs, bármelyik címről mehet, a tárgy és a törzs adja a hitelt).

**Tárgy:**
```
Ofertă financiară – Napsugár Tejüzem, extindere fabrică (Construct Transilvania SRL)
```

**Feladó (megjelenített név, ajánlott):**
```
Construct Transilvania SRL <office@constructtransilvania.ro>
```

**Törzs (copy-paste):**
```
Tisztelt Regio Consult csapata!

Mellékelten küldjük a Napsugár Tejüzem SRL tejfeldolgozó-bővítési
beruházására kért pénzügyi árajánlatunkat (Extindere fabrică de
procesare lapte, Odorheiu Secuiesc).

Az ajánlat objektumonként tartalmazza a tételeket (feldolgozó csarnok,
hűtőraktár, hőközpont, külső rendezés, gépsor, dotációk). A pénzügyi
végösszeg 5.375.000 lej + TVA.

A részletes, tételes ajánlatot aláírva és lepecsételve, szkennelt PDF
formátumban csatoljuk. Kérdés esetén szívesen állunk rendelkezésre.

Tisztelettel,
ing. Kovács Attila
projektvezető, SC Construct Transilvania SRL
Odorheiu Secuiesc, jud. Harghita · CUI RO98765432
```

**Csatolmány (KÖTELEZŐ):** a szkennelt ajánlat PDF-je:
```
.../regio/Tananyag/04_Szkennelt_PDF/oferta_szkennelt_Napsugar.pdf
```
> Ez a fájl **kép-only** (nincs szövegrétege), pont ezért lesz szükség rá az F4-ben az OCR-re. A törzs csak a végösszeget árulja el, a **tételes bontást** (a 12 sor) csak a szkennelt PDF-ből lehet kinyerni.

---

## 2. lépés (a workshopon, élőben): kérdezd meg a connectort

Miután befutott az email, a résztvevők előtt kivetítve futtasd a 3.1 promptot:
```
Nézd meg az Outlook postaládámban, érkezett-e ma új email a kivitelezőtől
a Napsugár Tejüzem beruházás ajánlatával kapcsolatban. Ha igen, foglald össze
röviden (ki küldte, mi a tárgy, mit tartalmaz), és mentsd le a mellékletét a
THR_Napsugar_Tejuzem projekt 08_Dosare_de_achizitii/04.04_DAL_Lucrari mappájába.
```

**Amit látni fognak:** az AI megtalálja Kovács Attila (Construct Transilvania) emailjét, összefoglalja (feladó, tárgy, hogy egy szkennelt PDF-ajánlat a melléklet, végösszeg 5.375.000 lej + TVA), és lementi a PDF-et a projekt DAL-mappájába. „Megjött a várt ajánlat, és az AI egyből behozta."

---

## 3. lépés: átvezetés az F4-be

*„Megvan az ajánlat, le is töltöttük. De ez egy 200 oldal körüli szkennelt PDF, csak kép. A tételes tartalmat, a 12 sort, ebből kézzel kellene kimásolni. Vagy mégsem? Jöjjön az F4: OCR-rel kinyerjük a lényeget."*

---

## Tippek a látványhoz
- Küldd az emailt **közvetlenül a demó előtt** (T-5 perc), hogy tényleg „ma érkezett" legyen, és az AI a legfrissebb levelek közt találja.
- Ha van rá mód, a feladó megjelenített neve legyen a kivitelező, ez erősíti a hatást.
- Ha a wifi/az MS365 bizonytalan a helyszínen: legyen egy **B-terv** screenshot vagy előre lementett válasz, hogy a demó akkor is menjen.

**Verzió:** 1.0 (2026-07-02)
