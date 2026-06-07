---
title: ExarLabs Szováta meeting 12 jegyzet, 2026-05-30
date: 2026-05-30
author: Becze Szabolcs
status: active
description: A szovátai csapatépítő negyedik felvétele (Sovata 12), a stratégiai nap gyakorlati folytatása: a 6 potenciál-terület összegzése, agrárdigitalizációs szövetség (Miklós Ervin / HAM / DEA értéklánc), a technikai paletta-vita (Frappe vs kisebb eszközök, Expo/Capacitor mobil-template, app-store automatizálás), Aaron Ross "ne csináld tökéletesre" elv, oktatási szintrendszer, és a sales-vállalás + Kanban board.
tags: [exarlabs, csapatepito, szovata, strategia, agrardigitalizacio, technikai-paletta, sales]
id: a6773387-b8ca-4441-b934-3db18464ee7b
index_schema_version: 1
---

# ExarLabs Szováta, meeting 12 (folytatás) — 2026-05-30

> Forrás: `Sovata 12.srt`, gépi (Whisper) feliratból kijegyzetelve, dedup után. Ez a [csapatépítő fő jegyzet](2026-05-30_szovata_csapatepito_jegyzet.md) folytatása: a Sovata 9-10-11 utáni gyakorlati ülés. Nevek/szakkifejezések torzulhatnak a feliratban.

## TL;DR

A csapat összegzi, hogy **6 potenciál-terület** futott egyszerre, és a fókusz a hogyanra terelődik: (1) **kliens előbb, tech utána** ("ne csináld tökéletesre az appot" — Aaron Ross elv), (2) a technikai paletta racionalizálása (a Frappe "ágyú", kellenek kisebb, gyors eszközök microsite / webshop / mobilapp gyártásra template-ekből), (3) az **agrárdigitalizációs szövetség** (Miklós Ervin + HAM + DEA mint kiegészítő értéklánc), és (4) a **sales-vállalás** operacionalizálása egy agent-karbantartott **Kanban board**-dal. Andor önként vállal ~2 céget + Régiokonzultot.

---

## 1. Navigátor-visszajelzés (nyitány)
- "Együtt jobb, mint egyedül": a csapat egymást felfelé húzza (egészség, munka, példamutatás).
- **Konkrét impact-story:** Buda Rász Isti egyik sógora elkezdett minden nap 5-kor kelni, edz, ellátja a ház körüli dolgokat, "felfelé halad az élete" — kiderült, hogy a **Navigátor Podcast fegyelem-epizódja** miatt. (A podcast valódi életet-formáló hatása megerősíti a brand-autoritást.)

## 2. A 6 potenciál-terület összegzése
Egyszerre fut / felmerült:
1. **Digitalizációs pályázat** (a "hullám meglovaglása").
2. **DEAC** (Deák-app), elindítva, még nincs "révben" (nincs igazi traction).
3. **Microsite-ok.**
4. **Oktatás** — főleg marketing-eszköz + "élesen tart minket", másodlagosan bevétel.
5. **Komplex AI-native cég** — Tankvary/Hermes + a többi ötlet összegyúrva, ez maga is eladható.
6. **Helyi termelős** webshop-ötlet (lásd lent; döntés: **később, nem most**).

## 3. Agrárdigitalizációs szövetség (DEA értéklánc)
- **Miklós Ervin** agrárdigitalizációs szakember, Romániában **top 2** (traktorok, termelési statisztikák: mennyi motorina, milyen vegyszer, mikor öntöz stb.). Podcastje 2 hét múlva jön ki. Cége Csíkban.
- **Kulcs-felismerés:** Miklós Ervin a **termelési fázist** viszi végig (visszavezeti a végterméket az alapokig), az ExarLabs/DEA a **termelőtől a sales/kereskedelmi fázist**. Tehát **nem konkurencia, hanem kiegészítés.** A DEA-app kereskedelmi platform; a DEA Romániában top 2 hús-feldolgozó.
- **Kereslet vezérli a kínálatot:** amit fel tudunk mérni mint szükségletet, az megy vissza a termelőhöz (a DEA pont annyit dolgoz fel, amennyire szükség van; nincs nagy raktárkészlet). Itt jön be a digitalizáció mint optimalizáció.
- **DEA beszerzés (részlet):** több helyről, többek között **Petri** (saját disznófarm, ~13 lej/50 ... fél disznóban veszik, nem élősúlyban); csirke heti 2x. Kapacitás: ~5 fél disznó/nap feldolgozva, ~15-öt elbírna → **buffer van növekvő forgalomra.**
- **HAM:** kurier-szolgálat + lefedettség (3 megyében jelen), beszéltek, **nem konkurálnak, szövetkeznek**; ahol kurier kell, velük.
- **Termelői piac-fájdalom:** a termelőknek piac kell; az ügyesebbek zöldségkosár-akciót szerveznek (sok logisztika, nehéz), a kevésbé ügyesek a piacon állnak maguk — **van optimalizálható rész.**
- **Figyelmeztetés:** Orosz Pál Levente szerint a helyi-termelős konkurens cég mögötti személy "borzasztó", nem ajánlja a szövetkezést vele. (A konkurálás viszont indokolt, "sőt kell is".)

## 4. A fragmentált hálózat összekötése
- Imádságban feljött: **nagyon sok fragmentált potenciál** van a csapat körül, ezeket össze kell kötögetni ("mint a húslevesben a zsírkarikák, hogy nagy karikává álljanak össze").
- **Hálózat-csomópontok:** Ignis, Navigátor Podcast kapcsolati tőke, **Orosz Pál Levente** (CED elnök, mindenkit ismer, a minisztériumban "OP"-ként ismerték), **Gergely István**, Miklós Ervin, HAM.

## 5. Technikai paletta racionalizálása
- **Frappe = "ágyú":** mindent meg lehet vele csinálni, de túl nehéz, külön szerver kell. Kellenek **kisebb, gyorsabb eszközök** is.
- **Cél-sebességek:**
  - **Microsite:** ~20 perc (MyITQ-szerű).
  - **Webshop:** ~1 nap (**Arni** eszközével, kis/közép cégekhez). Arni a webshopra nagyon ügyes; a másik kolléga a microsite-okra.
  - **Mobilapp:** cél, hogy **1-2 nap** alatt — ehhez kell egy template/generikus rész kiextraktálása, amire csak a domain + business-réteget húzzák rá.
- **Mobil-stack vita:** AI-javaslat **React Native → Expo** (a "helyes út" a React Native-hez); jelenlegi megoldás **Capacitor** (Frappe backend-del) — ezt **egyszerűsíteni kell** (egyszerűbb backend, egy kódbázis web+mobil). Flutter is felmerült. (Döntés elhalasztva: "most nem kell technikailag megdumálni".)
- **App-store automatizálás (jelentős időmegtakarítás):**
  - Már megvan: Playwright-tesztek 64 screenshotot gyártanak (HU/RO, telefon/tablet, Android/iOS) + store-feltöltés. (Régen, pl. Epiola: egy hét manuális meló, minden pixel a helyén.)
  - **Még automatizálandó:** az app-regisztráció Google/Facebook/Apple felé (1-2 hetes verifikáció + felkészülés sok óra), **OAuth consent screen / credentials** beállítása (Playwright-kattogtatás), és a **data-collection formok** (privacy: mit gyűjtesz, miért, hogy tárolod) generálása egy **centralizált adat-tárból**, amiből egy agent kitölti.

## 6. Stratégiai elv: kliens előbb, tech utána (Aaron Ross)
- **"Érőn rossz" = Aaron Ross** (Predictable Revenue, a Salesforce sales-gondolkodás megalkotója). Szabolcs gyakori prompt-trükkje: "mit csinálna [Aaron Ross / Salesforce] ebben a helyzetben?".
- **Elv:** **ne csináld tökéletesre az appot.** Legyen egy "kellően ügyes kis template"; az **első kliensnél sokat tanulsz** (alap a "módustság"/modularitás), a másodiknál kevesebbet iterálsz, a **harmadiktól matúr**.
- **Sorrend:** **először legyen kliens, utána építjük a technikai megoldást az első kliensnek.** Ne az eszközöket csiszoljuk előre, hanem a kliens-kapcsolatot.
- **Hiányzó integrációk** a fő tech-fájdalom: courier + payment (a Melindánál is 2 hónapja húzódik).

## 7. Design-guardrailek (anti-AI-look)
- A workflow-ba beépített guardok, hogy ne legyen "AI-hatású" a kimenet:
  - **Tiltott** a top-10 legismertebb font (ne a default-okat használja).
  - **Tilos a szimmetria** — legyen **aszimmetrikus** elrendezés (a szép szájtok nem szimmetrikusak; a túl racionális, egyenlő elrendezés AI-hatású).
  - **Parallax-hatás** (görgetésre eltérő sebességű elemek, 3D-érzet), interaktív animációk — vagány, népszerű.

## 8. Oktatás mint fő húzóerő (körkérdés)
- **Konszenzus:** a **minél több képzés** működne a legjobban (személyes, bizalomépítő, upsell).
- **Szintrendszer:** jelentkezési forma + **szintfelmérés** (pár kérdés), leírás alapján. Az emberek megijednek a "Claude Code / Obsidian" szavaktól → inkább **kezdő** szint elöl; aki elvégzi, annak ajánljuk a **haladót**.
- **"Szél/szöveg segédlet" (sales sheet):** ki kell generálni egy segédletet, amiből a csapattag (és a cégvezető) látja, **mit nyer a vállalkozása** a képzéssel — hogy meg tudja keresni és ajánlani a cégeknek.
- **Csatorna-ötlet:** **Simó Réka** (a csíki inkubátorház volt vezetője, Kinga barátnője, Szentegyháza-körök) megkeresése, hogy **Szentegyházán is** szervezzenek céges AI-képzést.
- Ha megvan a kezdő + haladó tananyag, az a mostani cégek ~90-99%-ának bőven elég.

## 9. Sales-vállalás operacionalizálása + Kanban
- **Őszinte felismerés:** a sales (target-ek, X kliens/hó hajtás) **senkinek sem a komfortzónája**, stresszes. **DE:** ha valakiben van rá vállalás, azt ki kell mondani és **elköteleződni** rá egy időablakra.
- **Andor vállal:** a következő 1-2 hétben felkeresi ~2 kontaktját + esetleg a **Régiokonzultot**, beszél velük (szöveg-segédlettel).
- **Kanban board:** Szabolcs generált egy **agent (Hermes) által karbantartott** Kanban boardot a sales-outreach követésére: ki melyik céggel vette fel a kapcsolatot, milyen státuszban van; a bot **statisztikát számol**. ("A kifejlesztés 3 perc, Trello-connector is van, de nem kell külsős — saját, ahogy mi akarjuk; mi húzogatjuk a kártyákat.")

---

## Döntések és nyitott szálak (meeting 12)

### Megerősített
- **Kliens előbb, tech utána** (Aaron Ross). Ne perfekcionizmus, hanem template + iteráció (matúr a 3. kliensre).
- **Agrárdigitalizáció:** szövetség Miklós Ervinnel (termelési oldal) + HAM (kurier) — kiegészítjük a DEA-t, nem konkurálunk.
- **Helyi termelős webshop:** jó ötlet, de **később, nem most.**
- **Technikai paletta:** Frappe mellé kisebb eszközök (Arni-webshop, microsite-tool); mobilra template-cél 1-2 nap, backend-egyszerűsítés.
- **Sales:** önkéntes-alapú vállalás + Kanban board a követésre.

### Új teendők (meeting 12-ből)
- [ ] Mobilapp-template kiextraktálása (Expo vagy egyszerűsített Capacitor), cél: 1-2 nap/app.
- [ ] App-store pipeline továbbfejlesztése: OAuth consent screen / credentials + verifikáció automatizálása (Playwright), centralizált data-form generátor.
- [ ] Capacitor mobil-stack backend egyszerűsítése (Frappe-leválasztás vizsgálata).
- [ ] Oktatás: kezdő/haladó szintrendszer + jelentkezési forma szintfelméréssel.
- [ ] "Szöveg/sales segédlet" generálása, amivel a cégvezető látja, mit nyer a képzéssel.
- [ ] Simó Réka megkeresése: AI-képzés szervezése Szentegyházán (csíki inkubátorház-körök).
- [ ] Miklós Ervin + HAM szövetség konkretizálása a DEA értékláncra.
- [ ] Fragmentált hálózat összekötése (Ignis, Navigátor, Orosz Pál Levente / CED, Gergely István).
- [ ] Sales Kanban board véglegesítése (Hermes agent-karbantartott, státusz + statisztika).
- [ ] Andor: ~2 kontakt + Régiokonzult felkeresése a következő 1-2 hétben (sales-vállalás).

### Nyitott kérdések
- Mobil-stack végső döntése: Expo (React Native) vs. egyszerűsített Capacitor vs. Flutter?
- Hogyan oldjuk meg a hiányzó courier + payment integrációkat (a fő tech-szűk keresztmetszet)?
- Ki vállal még sales-vállalást Andoron kívül?

## Új szereplők/entitások (meeting 12)
- **Miklós Ervin** — agrárdigitalizáció, top 2 Románia, Csík; podcast 2 hét múlva.
- **HAM** — kurier-szolgálat, 3 megyés lefedettség, szövetséges.
- **Orosz Pál Levente** — CED elnök, széles hálózat ("OP" a minisztériumban).
- **Gergely István** — hálózati csomópont.
- **Simó Réka** — csíki inkubátorház volt vezetője, Szentegyháza-képzés kontakt.
- **Arni** — webshop-eszköz fejlesztője/szakértője.
- **Aaron Ross ("Érőn rossz")** — Predictable Revenue / Salesforce sales-gondolkodás, prompt-referencia.
- **Buda Rász Isti** — akinek a sógora a Navigátor-impact story alanya.
- Tech: **Frappe, Expo/React Native, Capacitor, Flutter, Playwright, Hermes (agent), Trello-connector.**
