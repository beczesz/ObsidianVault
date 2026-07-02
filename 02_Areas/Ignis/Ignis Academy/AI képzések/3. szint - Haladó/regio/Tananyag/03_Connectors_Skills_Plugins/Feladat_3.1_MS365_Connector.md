---
title: "Feladat 3.1: MS365 Connector: érkezett-e új email? (DEMO)"
date: 2026-07-02
author: Becze Szabolcs
status: active
description: "F3 oktatói demó: élőben bekötjük az MS365 (Outlook) connectort, és megkérdezzük az AI-tól, érkezett-e új email. Pont ekkor fut be a kivitelező ajánlata (szkennelt PDF melléklet), amit az AI összefoglal és a projekt mappájába ment. Ezt az oktató élőben, kivetítve mutatja; a résztvevők megfigyelik, és otthon a saját Outlookjukon próbálják. Ez az email-ben befutó ajánlat táplálja az F4 OCR-fázist."
id: b2e4d3c5-4c6f-5d7b-8e9a-2f3c4d5e6a7b
index_schema_version: 1
bdos_index: true
tags: [ignis-academy, halado, regio-consult, f3, feladat, connector, demo]
---
# Feladat 3.1: MS365 Connector: érkezett-e új email? (DEMO)

> **Típus:** 🎤 OKTATÓI DEMO (élő, kivetítve) · **Idő:** ~10 perc

---

## Szituáció

Eddig az AI a lokális fájlokat látta. De a munka nagy része **emailben** jön: a beneficiár, a tervező, a kivitelező mind ír. Mi lenne, ha az AI **közvetlenül a postaládátokból** olvasna? Ezt csinálja egy **connector**: egy híd egy külső rendszerhez (itt: MS365 / Outlook), amin keresztül az AI, a te felhatalmazásoddal, olvashat.

Most élőben bekötjük, és pont jókor: a kivitelező **épp most küldi be** a Napsugár-beruházás ajánlatát.

---

## A demó menete (az oktató élőben, kivetítve)

### 1. lépés: A connector bekötése
Az oktató a Cowork connector-beállításában bekapcsolja az **MS365 (Outlook)** kapcsolatot, és jóváhagyja a hozzáférést. Fontos üzenet a résztvevőknek: a connector **olvasási** hozzáférés, a te engedélyeddel, és bármikor lekapcsolható. Az AI nem küld a nevedben, csak ha külön kéred.

### 2. lépés: „Érkezett-e új email?"
Az oktató bemásolja:

```
Nézd meg az Outlook postaládámban, érkezett-e ma új email a kivitelezőtől
a Napsugár Tejüzem beruházás ajánlatával kapcsolatban. Ha igen, foglald össze
röviden (ki küldte, mi a tárgy, mit tartalmaz), és mentsd le a mellékletét a
THR_Napsugar_Tejuzem projekt 08_Dosare_de_achizitii/04.04_DAL_Lucrari mappájába.
```

### 3. lépés: Az eredmény
Az AI megtalálja a kivitelező emailjét, összefoglalja (feladó, tárgy, hogy egy **szkennelt PDF ajánlat** a melléklet), és a mellékletet a projekt DAL mappájába menti. A résztvevők a saját (statikus) másolatukban ugyanezt a szkennelt PDF-et már a helyén találják, tehát az F4 mindenkinél folytatható.

---

## Amit a résztvevők megfigyelnek
- Hogy az AI **valós postaládából** olvas, nem előre bemásolt fájlból.
- Hogy a beérkező ajánlat egy **szkennelt PDF**, ami rögtön előrevetíti az F4 fájdalmát.
- Hogy a connector **kontrollált**: olvasás, felhatalmazással, nincs önálló küldés.

## Otthoni gyakorlat (opcionális, saját gépen)
Kösd be a saját Outlook / OneDrive connectorodat, és kérdezd meg az AI-tól egy konkrét, ártalmatlan témában, mit lát (pl. „foglald össze a mai leveleimet egy témában"). Csak olvasás, semmi küldés.

---

## Tanulás

A connector az a pont, ahol az AI **kilép a fájl-mappából a rendszereitekbe**. Ez teszi a napi munkát folyamatossá: a levél megérkezik, az AI látja, feldolgozza, elmenti a helyére. A kulcs a **kontroll**: olvasás a te felhatalmazásoddal, a küldés mindig emberi döntés marad.

---

## Mi következik (3.2)

A connector behozta a munkát. De hogyan tanítjuk meg az AI-t a **saját, ismétlődő** munkafolyamataitokra, hogy ne kelljen mindig újramagyarázni? Ez a **skill**.

---

## Időkeret
- A connector bekötése + biztonsági keret: 3 perc
- „Érkezett-e új email?" + az ajánlat behozása: 4 perc
- Kérdések: 3 perc
- **Össze: 10 perc**

**Verzió:** 1.0 (új F3, 2026-07-02)
