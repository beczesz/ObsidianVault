---
title: "Meeting Prep -- Bozar Anita (MVMI)"
date: 2026-04-02
author: Becze Szabolcs
status: active
description: "Szabolcs és Bozar Anita (MVMI frontend üzemeltetési vezetője) közötti meetingtervezett áprilisban az Azure DevOps támogatási szerződés nyitott kérdéseinek tisztázásáról, különösen az SLA működésről, üzemeltetői kooperációról, hozzáférésekről és riportingról."
description_source: auto
description_hash: bdb7d6a350fef902
id: 1f9cda5c-bf1b-43fe-ae7e-b7073ce51b03
index_schema_version: 1
bdos_index: true
---
# Meeting Prep -- Bozar Anita (MVMI)

**Datum:** 2026 aprilis (jovo het, pontos datum kitoltendo)
**Resztvevok:** Szabolcs (CPS) + Bozar Anita (MVMI, frontend uzemeltetesi osztalyvezeto)
**Tema:** Azure DevOps tamogatasi szerzodes -- nyitott kerdesek alairras elott
**Szerzodes hivatkozas:** 1001686173_Azure DevOps tamogatasi szerzodes_v3.docx

---

## Kerdesek Bozar Anitanak

### 1. SLA mukodes a gyakorlatban

**1.1.** Az SLA tablaban (1. sz. melleklet) a "Problema elharitas megkezdese es befejezese a bejelentestol szamitva" -- ez a gyakorlatban mit jelent? Pelda: ha 2 ora alatt diagnosztizaljuk a hibat, de a javitashoz az Uzemelteto csapat jovahagyasa kell es ok csak masnapra ernek ra -- az SLA orat ki futja?
> *Hatter: a szerzodes nem tartalmaz "clock stop" mechanizmust. Ha az Uzemelteto oldali varakozas belesszamit, nem tudjuk tartani az SLA-t.*
> *Hivatkozas: 1. sz. melleklet, SLA tabla + 7. sz. melleklet, "Onallo intezkedesek tilalma"*

**1.2.** Ki donti el a bejelentes prioritasat (Kritikus / Magas / Normal / Alacsony)? Mi tortenik, ha nem ertunk egyet a prioritassal?
> *Hatter: a prioritas kozvetlenul befolyasolja az SLA idot (8 ora vs. 60 munkanap) es a kotber merteket.*
> *Hivatkozas: 1. sz. melleklet, SLA tabla + Szerzodes 14. pont, 14.1.*

**1.3.** Mi tortenik ha 17:30 utan erkezik egy Kritikus ticket? Masnap reggel 7:00-tol indul az SLA, vagy mar az erkezeskortol szamit?
> *Hatter: a szerzodes nem szabalyozza. 17:59-kor erkezo Kritikus ticketnel erdemben mar nem tudjuk megkezdeni a munkat.*
> *Hivatkozas: 1. sz. melleklet: "5x11 (7-18.00)" + "bejelentesek a het minden napjan 0-24 oraig rogzithetok"*

**1.4.** Magyar allami unnepnapokon (pl. Apr 3 Nagypentek, Maj 1, Aug 20) fut-e az SLA? Erkezhetnek ticketek amiket abban az idoszakban kell kezelni?
> *Hatter: a szerzodes "5x11 (7:00-18:00)"-t ir, de nem zarjaki explicit az unnepnapokat.*
> *Hivatkozas: 1. sz. melleklet, SLA tabla, "Meresi idoszak" oszlop*

---

### 2. Uzemeltetoi egyuttmukodes

**2.1.** Ki az Uzemelteto csapat akivel egyutt dolgozunk? Hany fo, milyen elerheteoseg? Van dedikalt kontaktszemely az Uzemelteto oldalon akit kerdesekkel megkereshetunk?
> *Hatter: a 7. sz. melleklet szerint mi "Uzemeltetest Tamogato" vagyunk, az "Uzemelteto" kulon csapat. A napi munka fugg attol, hogyan mukodunk veluk egyutt.*

**2.2.** Mi a folyamat, ha a mi javitasi javaslatunkhoz Uzemeltetoi jovahagyas kell? Van erre formalis workflow (pl. change management), vagy informalis egyeztetes?
> *Hatter: a 7. sz. melleklet, "Onallo intezkedesek tilalma" szerint "minden ilyen jellegu tevekenysseget kizarolag az Uzemelteto kozremukodesevel es az MVMI Zrt. jovahagyasi rendje szerint vegezhet."*

**2.3.** Mekkora a jelenlegi ticket mennyiseg havonta? Milyen tipusu hibak a leggyakoribbak?
> *Hatter: a Szakmai Indoklas (2026-02-05) "alacsony varhato ticket szam"-ot emlitett, ezert valasztottuk az Essential csomagot. Fontos tudni a valos szamokat a kapacitastervezeshez.*

**2.4.** Van mar kialakult ticketkezeles / ITSM rendszer (pl. ServiceNow, Jira Service Management)? Ebbe kapunk hozzaferest?
> *Hivatkozas: 1. sz. melleklet: "online hibabejelento felulet"*

---

### 3. Hozzaferesek es onboarding

**3.1.** Milyen hozzafereseket kapunk a kezdeskor? A 3. sz. melleklet (IT jogosultsagi lista) meg ures -- mikor toltjuk ki?
> *Hivatkozas: Szerzodes 4. pont + 3. sz. melleklet*

**3.2.** A VPN / tavoli hozzaferes hogyan mukodik? Van valami MVMI-specifikus security requirement (pl. MDM, dedikalt gep)?
> *Hivatkozas: 1. sz. melleklet, "Egyuttmukodes modja": "biztonsagos tavoli hozzaferes a rendszerek eleresere"*

**3.3.** Kell-e MVMI informacioibiztonsagi kepzes a csapattagjainknak az indulas elott?
> *Hivatkozas: Szerzodes 3. pont + 7. sz. melleklet, "Szemelyzettel kapcsolatos eloirasok": "uzemeltetesi szerepkorre optimalizalt informaciobiztonssag-tudatossagi kepzesben reszesuljenek"*

---

### 4. Teljesitesmerees es riporting

**4.1.** A "kozlekedesi lampa" modszer (Szerzodes 14. pont, 14.1.) -- ki szamolja ki? Mi adunk riportot es az MVMI ellenorzi, vagy az MVMI szamolja a sajat rendszerebol?
> *Hatter: fontos tudni, mert a piros lampa automatikus 20% dijengedmenyt jelent.*
> *Hivatkozas: Szerzodes 14. pont, 14.1.: "a bejelentesek legalabb 80%-a a zold (teljesult) savba esik"*

**4.2.** A havi teljesitesigazolas (2. sz. melleklet, MTIG) -- mi a folyamat? Ki irja ala az MVMI oldalon? Meddig kell benyujtani?
> *Hivatkozas: Szerzodes 9. pont + 2. sz. melleklet*

**4.3.** A "hibas teljesites" defnicioja (14. pont, 14.1.): "a rendszer mukodese az elvart funkcionalitastol elteroen mukodik, a hiba nem lett kijavitva vagy a hibajavitas ujabb hibat generalt" -- ez azt jelenti, hogy ha EGY ticket utan a rendszer nem mukodik tokelletesen, az automatikusan hibas teljesites? Vagy van turesmero?
> *Hivatkozas: Szerzodes 14. pont, 14.1., "Hibas teljesites meghatarozasa"*

---

### 5. Opcionalis keret es Feladatkiadasi lap

**5.1.** Az opcionalis keretbol (Szerzodes 7.2. pont, 25.220.000 Ft) milyen tipusu munkakat kepzeltek el? Van mar konkret feladat ami varakozik?
> *Hivatkozas: Szerzodes 7.2. pont + 2. pont ("Feladatkiadasi lapot vesznek fel")*

**5.2.** A Feladatkiadasi lap (6. sz. melleklet) kiadasa hogyan mukodik? Ki inditvanyozza, mi a jovahagyasi folyamat, mennyi az atfutasi ido?
> *Hivatkozas: Szerzodes 9. pont, 2. resz: "Megrendelo [...] a feladat megrendeleset megelozo 2 nappal korabban, irasban (e-mailen) [...] rendeli meg. [...] kizarolag a szakmai kapcsolattarto jogosult."*

---

### 6. Indulasi kerdesek

**6.1.** Mi a tervezett indulasi datum? Van-e valamilyen atmeneti idoszak / pilot, vagy az SLA azonnall az alairas naptol eles?
> *Hivatkozas: Szerzodes 10. pont: "a mindket fel altali alairas naptari napjan lep hatalyba"*

**6.2.** Van-e meglevo dokumentacio az Azure DevOps kornyezetrol (architektura diagram, deployment guide, ismert hibak listaja)?
> *Hatter: az onboarding gyorsitasahoz fontos lenne megismerni a kornyezetet.*

**6.3.** Hany Azure DevOps instance-rol / projektrol van szo? Server es Services (cloud) egyarant?
> *Hivatkozas: 1. sz. melleklet: "Azure DevOps platform (Server & Services)"*

---

## NEM Anitanak szolo kerdesek (Horvath Istvannak / szerzodeses ugyek)

Az alabbi temakat NE Anitaval targyald -- ezek szerzodeses/jogi kerdesek, Horvath Istvan (medior strategiai beszerzo) illetekessegebe tartoznak:

- Karteritesi felso korlat (liability cap) bevezetese [Szerzodes 14. pont]
- Alvallalkozoi tilalom modositasa [Szerzodes 12. pont]
- ISO 27001 szavatossag modositasa [5. sz. melleklet, 8.8. pont]
- Arfelulvizsgalat a +12 honapos hosszabbitasnal [Szerzodes 10. pont + 7.1. pont]
- Felmondasi jogok egyensulya [Szerzodes 4. pont + 10. pont]
- Kotber halmozodasi tilalom [Szerzodes 14. pont, 14.1.]

Ezeket kulon meetingben, Horvath Istvannal (es Miklos bevonasaval) kell targyalni.

---

## Jegyzeteles a meetingen

| # | Kerdes | Anita valasza | Kovetkezo lepes |
|---|--------|---------------|-----------------|
| 1.1 | SLA clock stop | | |
| 1.2 | Prioritas dontes | | |
| 1.3 | 17:30 utani ticket | | |
| 1.4 | Unnepnapok | | |
| 2.1 | Uzemelteto csapat | | |
| 2.2 | Jovahagyasi folyamat | | |
| 2.3 | Ticket mennyiseg | | |
| 2.4 | ITSM rendszer | | |
| 3.1 | Hozzaferesek | | |
| 3.2 | VPN / security | | |
| 3.3 | Biztonsagi kepzes | | |
| 4.1 | Kozlekedesi lampa szamitas | | |
| 4.2 | MTIG folyamat | | |
| 4.3 | Hibas teljesites definicio | | |
| 5.1 | Opcionalis keret tervek | | |
| 5.2 | Feladatkiadasi lap folyamat | | |
| 6.1 | Indulasi datum | | |
| 6.2 | Meglevo dokumentacio | | |
| 6.3 | Azure DevOps scope | | |
