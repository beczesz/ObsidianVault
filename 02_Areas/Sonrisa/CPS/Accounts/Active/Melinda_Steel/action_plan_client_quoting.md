---
title: "Akcioterv: Melinda Steel -- Ugyfelfele Ajanlatkero Chatbot"
date: 2026-04-23
author: Becze Szabolcs
status: active
description: "Akcioterv a Melinda Steel acélcég WhatsApp-alapú ajánlatkérő chatbotjához Microsoft Copilot Studio és Power Automate segítségével, négy fázisban: előkészítés, Copilot alapok, backend integráció és tesztelés. Projektmenedzsereknek és Power Platform fejlesztőknek szól."
description_source: auto
description_hash: 93057c33c6081949
id: 0141908f-00bb-4959-a6c8-352a22273113
index_schema_version: 1
bdos_index: true
---
# Akcioterv: Melinda Steel -- Ugyfelfele Ajanlatkero Chatbot

**Projekt:** WhatsApp-alapu ajanlatkero rendszer, ahol ugyfelek termeszetes nyelven kernek arajanlat acel termekekre
**Platform:** Microsoft Copilot Studio + Power Automate + Azure Communication Services
**Datum:** 2026-04-23
**Statusz:** TERVEZES

---

## Architektura

```
Ugyffel (WhatsApp) 
  -> Azure Communication Services 
    -> Copilot Studio (beszelgetes + slot filling)
      -> Power Automate 
        -> Fuzzy Matching API (Render)
        -> Azure Function (pricing logika)
          -> ERP rendszer
      -> Dataverse / SharePoint (ugyffel, ajanlattar)
```

**Dontes alapja:** Harom fuggetlen forras (Perplexity kutatas, ChatGPT strategiai elemzes, Copilot M365 domain expert) egyuttesen validalta, hogy a Copilot Studio nativ WhatsApp csatornaja (GA 2025 julius) megfelelo front-end ehhez a use case-hez. A Copilot Studio feladata: beszelgetes kezeles, nyelv felismeres, adatgyujtes. A Power Automate + Azure Functions feladata: uzleti logika, ERP, matching, ar szamitas.

---

## Phase 0: Elokeszites (1 het)

**Cel:** Minden blokkolo kerdest tisztazni mielott fejlesztes indul.

**Feladatok:**
1. ERP rendszer azonositasa -- melyik rendszert hasznalja Melinda Steel, van-e API/export lehetoseg?
2. Azure Communication Services fiok letrehozasa + WhatsApp Business API regisztracio Meta-nal
3. Copilot Studio licenc / PAYG beallitasa (Azure subscription szukseges)
4. Power Platform environment letrehozasa (Dataverse-szel)
5. Csapat kivalasztasa -- ki dolgozik a projekten? (1-2 fo, Power Platform alapismeretek szuksegesek)
6. Meglevo fuzzy matching API (melinda-matching-gom4.onrender.com) tesztelese -- mukodik-e, milyen valaszidovel?

**Fuggosegek:** ERP azonositasa blokkolo -- enelkul a Phase 2 nem indulhat.

**Sikerkriterium:** Minden nyitott kerdés megvalaszolva, Azure + Meta fiokok aktivan, Copilot Studio elerheto.

**Becsult idotartam:** 1 het (parhuzamositva)

> **Copilot validacios megjegyzes:** A Meta WhatsApp Business jovahagyas 3-10 munkanapot is igenybe vehet. Ezt az 1. napon el kell inditani, es NEM szabad feltetelezni, hogy 5 nap alatt kesz. Licensz tekinteteben is pontositani kell: Copilot Studio tier, Power Automate premium connectorok, Dataverse tarolas.

---

## Phase 1: Copilot Studio Alapok + WhatsApp Csatorna (2 het)

**Cel:** Mukodo chatbot, ami WhatsApp-on beszel az ugyfelekkel es osszegyujti az adatokat, de meg NEM ker arat.

**Feladatok:**

*1. het:*
1. Copilot Studio megismeres -- topicok, valtozok, entitasok, Power Automate integracii (3-5 nap tanulas)
2. Fo topic letrehozasa: "Ajanlat keres" -- slot filling flow:
   - Termek neve / leirasa (szabad szoveg)
   - Mennyiseg + mertek egyseg
   - Szallitasi cim (varos / helyszin)
   - Fizetesi feltetel (keszpenz / atutalas / halasztott)
3. Nyelv detektalas -- roman es magyar nyelvu valaszok konfigurasa
4. Fallback topic -- ha a chatbot nem erti az ugyfel kereset

*2. het:*
5. WhatsApp csatorna bekotes Azure Communication Services-en keresztul
6. Meta Business fiok + WhatsApp Business API konfiguracio
7. WhatsApp message template-ek letrehozasa (24 oras ablak utani ujra-megkereses)
8. Vegig teszteles: valodi telefonrol WhatsApp uzenet -> Copilot Studio valaszol, adatot gyujt

**Fuggosegek:** Phase 0 kesz (Azure fiok, Copilot Studio licenc)

**Sikerkriterium:** Egy valodi telefonrol WhatsApp-on elindithato beszelgetes, a chatbot osszegyujti a termek, mennyiseg, cim, fizetesi feltetelt mindket nyelven.

**Becsult idotartam:** 2 het

> **Copilot validacios megjegyzes:** A "confirmation gate" topic fontos -- ha a fuzzy match confidence < threshold, a chatbot kerjen megerositest az ugyfeltol mielott arazzak. Az MVP-ben NE probaljunk tobb termekes ajanllatot egyszerre kezelni -- egy termek / session.

---

## Phase 2: Backend Integraciok (2-3 het)

**Cel:** A chatbot nem csak gyujt adatot, hanem termeket is talal es arat is ad.

**Feladatok:**

*1. het:*
1. Power Automate flow: Copilot Studio -> HTTP action -> Fuzzy Matching API
   - Input: ugyffel altal megadott termeknev
   - Output: legjobb talalat (ITEMKEY, confidence score, WEIGHT)
   - Ha confidence < 60: kerjen vissza az ugyfeltol pontositast
2. Custom connector letrehozasa a fuzzy matching API-hoz (OpenAPI spec)
3. Ugyffel-azonositas flow: telefon szam -> Dataverse lookup -> CUI (ado szam) mapping
   - Ha uj ugyffel: adatokat kerni (cegnev, CUI, kapcsolattarto)

*2-3. het:*
4. Azure Function letrehozasa az ERP integraciohoz:
   - Bejarato: ITEMKEY + mennyiseg
   - Kijarato: egysegar, keszlet, szallitasi ido
   - Ar szamitas: mennyiseg x egysegar, valuta kezeles (RON/EUR), AFA
   - Kedvezmeny szabalyok (ha vannak)
5. Power Automate flow: Copilot Studio -> Azure Function -> ERP
6. Ajanllat osszeallitas: a Copilot Studio formatalt szoveges ajanlat-ot kuld vissza WhatsApp-on
7. Ajanllat archivalas: Dataverse / SharePoint-ba mentes (ajanllat ID, datum, tetelek, ar, ugyffel)

**Fuggosegek:** Phase 1 kesz + ERP hozzaferes tisztazva (Phase 0-bol)

**Sikerkriterium:** Teljes flow mukodik: ugyffel kerdes -> termek match -> ar lekerdezes -> ajanllat visszakuldes WhatsApp-on. Ajanllat archivalva.

**Becsult idotartam:** 2 het (ha ERP API kesz), 3 het (ha ERP adapter fejlesztes szukseges)

> **Copilot validacios megjegyzes:** ERP scope-ot LIMITALNI kell az MVP-ben: csak read-only pricing. NEM keszletinformacio, NEM szallitasi datum iger. Hianyzo aranyek kezelese: ERP timeout, SKU nem arazdhato, ugyffel blokkolt/hitelkeret. Az ajanllat ervenyessegi idot is rogziteni kell (pl. 24h/72h).

---

## Phase 3: Finomhangolas + Belso Teszteles (1-2 het)

**Cel:** A rendszer megbizhato, kellemes felhasznaloi elmenyt ad, es kezeli a szelso eseteket.

**Feladatok:**
1. Edge case-ek kezelese:
   - Ismeretlen termek (nincs match a katalogusban)
   - Hianyzo ERP ar (termek letezik, de nincs aktualis ar)
   - Ugyffel felbesakitja a beszelgetest es ujra kezdi
   - 24 oras WhatsApp ablak lejarta -- message template kuldese
   - Tobb termek egy beszelgetesben
2. Nyelvi finomhangolas -- roman es magyar valaszok termeszetes hangzasa
3. Valaszido optimalizalas -- a fuzzy matching + ERP lekerdezes osszesen < 10 masodperc legyen
4. Belso teszteles: Sonrisa csapat + Melinda Steel ertekesitok tesztelik
5. Analytics beallitasa: Copilot Studio beepitett analytics + egyedi Power Automate logging
6. Hiba-eszkalacios utvonal: ha a bot nem tud valaszolni, elo ertekesitohöz iranytias (Teams / email ertesites)

**Fuggosegek:** Phase 2 kesz

**Sikerkriterium:** 20+ belso teszt beszelgetes hiba nelkul lefut mindket nyelven. Atlagos valaszido < 15 masodperc.

**Becsult idotartam:** 1-2 het

---

## Phase 4: Pilot Valos Ugyfelekkel (2-4 het)

**Cel:** Valos korulmenyek kozott validalni, hogy az ugyfelek hasznaljak es erteket latnak benne.

**Feladatok:**
1. 5-10 valos ugyffel kivelasztasa pilot-ra (meglevo, megbizhato ugyfelek)
2. QR kod / link elkeszitese a WhatsApp szamhoz
3. Pilot inditas -- ugyfelek hasznaljak, Melinda ertekesitok monitorozzak
4. Napi riportok: hany beszelgetes, hany sikeres ajanllat, hany hiba, ugyfel visszajelzes
5. Iteracio: a pilot alatti tanulsagok alapjan finomitas (heti ciklusokban)
6. Monitoring: Copilot Studio credit fogyasztas kovetese (valos PAYG koltseg)

**Fuggosegek:** Phase 3 kesz + Melinda Steel belso jovahagy

**Sikerkriterium:**
- Legalabb 20 valos ugyffel beszelgetes
- Legalabb 10 sikeres ajanllat kiadasa
- Ugyffel elegedettseg pozitiv (informalis visszajelzes)
- Nincs kritikus hiba

**Becsult idotartam:** 2-4 het

---

## Phase 5: Eles Inditas + Skalazas (1 het)

**Cel:** A rendszer mindenki szamara elerheto.

**Feladatok:**
1. WhatsApp szam nyilvanossa tetele (Melinda Steel weboldalon, szamlakon, bolti QR)
2. Melinda ertekesitok kepzese: mikor kell manualis beavatkozas, hogyan nezik az ajanllat-okat
3. Monitoring dashboard beallitasa (credit fogyasztas, beszelgetes szam, hiba rata)
4. SLA meghatarrozasa: valaszido, rendelkezesre allas, eszkalaci
5. Dokumentacio lezarasa

**Fuggosegek:** Phase 4 sikerkriteriumai teljesulnek

**Sikerkriterium:** Rendszer stabilan mukodik, naponta 10+ beszelgetes, Melinda csapat onalloan monitorozza.

**Becsult idotartam:** 1 het

---

## Idovonal Osszefoglalo

| Fazis | Idotartam | Kumulativ |
|-------|-----------|-----------|
| Phase 0: Elokeszites | 1 het | 1. het |
| Phase 1: Copilot Studio + WhatsApp | 2 het | 3. het |
| Phase 2: Backend integraciok | 2-3 het | 5-6. het |
| Phase 3: Finomhangolas + belso teszt | 1-2 het | 6-8. het |
| Phase 4: Pilot valos ugyfelekkel | 2-4 het | 8-12. het |
| Phase 5: Eles inditas | 1 het | 9-13. het |

**Osszesen: 9-13 het (2-3 honap)**

---

## Becsult Koltsegek

| Tetel | Havi koltseg | Megjegyzes |
|-------|-------------|------------|
| Copilot Studio (PAYG) | ~$54-108 | 50-100 conv/nap, ~18 credit/session |
| Azure Communication Services | ~$10-30 | WhatsApp uzenet dijak |
| Azure Functions | ~$5-20 | Consumption plan, pricing logika |
| Fuzzy Matching API (Render) | Mar meglevo | Nincs plusz koltseg |
| Power Platform environment | $0 | Copilot Studio licenccel jar |
| **Osszesen (eredeti becsles)** | **~$70-160/ho** | |
| **Osszesen (Copilot validalt)** | **~$120-250/ho** | Realisabb, volumen-fugg |

---

## Korlatok es Kockazatok

1. **WhatsApp 24 oras ablak** -- Az ajanlatkeres-nek 24 oran belul le kell zarulnia, kulonben Meta-jovahagyott message template kell a folytatashoz. A flow-t ugy kell tervezni, hogy egy session-ben lezaruljon.

2. **Adaptive Cards korlatozas** -- WhatsApp-on max 3 gomb, nincs gazdag tabla. Az ajanllatot szoveges formaban kell kuldeni, nem formatalt dokumentumkent.

3. **ERP integracii a legnagyobb kockazat** -- Ha az ERP-nek nincs modern API-ja, az Azure Function fejlesztese jelentosen tobb idot vehet igenybe.

4. **Copilot Studio debugging** -- Korlatozott debugging eszkozok, a beszelgetes logika verziokezelse nehezebb mint kod-alapu rendszereknel.

5. **Credit fogyasztas kiszamithatatlansaga** -- A tenyleges koltseg fugg a beszelgetesek hosszatol es komplexitasatol. Az elso honapban szorosan monitorozni kell.

---

## Nyitott Kerdesek

### Blokkolo (Phase 0-ban megvalaszolandao)
1. **Melyik ERP rendszert hasznalja Melinda Steel?** Es milyen hozzaferesi mod letezik (REST API, SOAP, direct DB, export feed)?
2. **Ki a projekt megbizott a Melinda Steel oldalrol?** Ki dontt technikai es uzleti kerdesekben?
3. **Van-e mar Azure subscription?** Ha nincs, ki hozza letre es ki fizeti?
4. **A Meta Business fiok (WhatsApp Business API) kinek a nevere legyen?** Melinda Steel vagy Sonrisa?

### Fontos (Phase 1-2-ben megvalaszolandao)
5. **Ugyffel-azonositas:** Eleg a telefonszam, vagy a chatbot-nak CUI-t (ado szamot) is be kell gyujtenie a ceg azonositasahoz?
6. **Kedvezmeny policy:** A chatbot fix listaarat ad, vagy ugyffel-specifikus kedvezmenyt is alkalmazhat? Ki engedelyezi az elterest?
7. **Ajanllat szamozas:** Van-e meglevo ajanllat-szamozasi rendszer az ERP-ben, amihez igazodni kell?
8. **Tobb termek egy ajanllatban:** Egy beszelgetesben hany termekre kerhet ajanllatot az ugyffel?

### Strategiai (Phase 4-5-ben megvalaszolandao)
9. **Mekkora a vart napi beszelgetes szam?** Ez hatarozza meg a PAYG vs capacity pack dontest.
10. **Az eles rendszernek 24/7 kell-e mukodnie?** Vagy csak munkaido alatt?
11. **A legacy n8n workflow (versenytars arak) tovabbra is kulon marad?** Vagy kesobb integralodik a Copilot Studio-ba?
12. **Nyelvek:** Csak roman es magyar, vagy kesobbb angol is szukseges?
13. **Ajanllat ervenyessegi ablak:** Meddig ervenyes egy kiadott ajanllat? (24h / 72h / egyedi?)
14. **AFA kezeles:** Belfoldi vs EU ertekesites -- mas AFA szabalyok?
15. **Valuta:** RON, EUR, vagy mindketto?
16. **Emberi eszkalacio SLA:** Ha a bot nem tud valaszolni, mennyi idon belul kell elo ertekesitonek reagalnia?

---

---

## Validacio

**Copilot M365 (Domain Expert) osszesitett velemenye:**
> "This is a strong, realistic plan overall. Nothing in it is fundamentally wrong. I would approve this plan with minor adjustments."

**Fo korrekciak a Copilot-tol:**
1. Meta Business jovahagyas: 3-10 munkanap, nem 1 het -- inditsd az 1. napon
2. Koltseg becsles realisabb: $120-250/ho (nem $70-160)
3. MVP scope: egy termek / session, csak read-only ERP pricing, nincs keszlet/szallitas
4. Confirmation gate topic: fuzzy match eredmeny megerositese az ugyfellel
5. Plusz nyitott kerdesek: ajanllat ervenyesseg, AFA, valuta, eszkalacio SLA

---

## Forrasok

- [Perplexity kutatas](https://www.perplexity.ai/search/microsoft-copilot-studio-2025-Y0pLldmMS2CqngfafTFfKQ) -- Copilot Studio kepessegek, WhatsApp, pricing
- [ChatGPT strategiai elemzes](https://chatgpt.com/c/69e9e50b-9e00-8395-84e3-2ff527668f5d) -- Platform osszehasonlitas, kockazatok
- [Copilot M365 validacio](https://m365.cloud.microsoft/chat/conversation/23ad3c15-3463-4e35-8e42-501072480c1e) -- Copilot Studio nativ WhatsApp, architektura, koraltok
- [MS Learn: Billing rates](https://learn.microsoft.com/en-us/microsoft-copilot-studio/requirements-messages-management)
- [MS Learn: WhatsApp channel](https://learn.microsoft.com/en-us/microsoft-copilot-studio/publication-add-bot-to-whatsapp)
- [Projekt dokumentacio](./Melinda%20steel%20n8n%20project%20documentaion.md) -- Section 7
