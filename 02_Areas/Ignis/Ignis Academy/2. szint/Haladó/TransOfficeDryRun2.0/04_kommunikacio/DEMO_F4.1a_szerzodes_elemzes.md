---
title: "DEMO F4.1a — Bérleti szerződés cross-doc elemzés (A.9 prompt)"
date: 2026-05-13
author: Becze Szabolcs
status: active
description: "Bérleti szerződés kockázat-elemzése TransOffice raktárhelyére, amely azonosított 5 kritikus pontot (felmondási jog, díj-indexálás, nincs karte funciară bejegyzés, beruházás-visszatérítés hiánya, karbantartási jog). Cross-dokumentum ellenőrzés után feloldódott a legfontosabb kockázat: tulajdonosváltás nem fenye"
description_source: auto
description_hash: d13b09e5799737a2
id: 7c3c5160-592c-40a8-b3a6-4618c3d799cf
index_schema_version: 1
bdos_index: true
---
# DEMO F4.1a — Bérleti szerződés cross-doc elemzés (A.9 prompt)

> **Prompt:** A.9 — szerzodes_chirie_TransOffice_2018.docx top 5 kockázat + más fájlokkal cross-check + akcióterv
> **Cowork-futás:** ~90 mp

---

## Top 5 kockázati pont (TransOffice mint bérlő szempontjából)

| # | Pont | Részlet | Súly |
|---|------|---------|------|
| 1 | **Art. 8.3 — Egyoldalú felmondás 6 hónapos felmondási idővel** | A locator (Béla bácsi) bármikor felmondhat 6 hó értesítéssel, ami nem fér az AFM 5 éves stabilitás-követelményével | 🔴 magas |
| 2 | **Bérleti díj-indexálás évente CPI szerint** | Art. 4.2: a locator egyoldalúan indexálhatja a bérleti díjat — pályázati cash flow tervezést bizonytalanná teszi | 🟡 közepes |
| 3 | **Nincs karte funciară-bejegyzés** | A szerződés csak ANAF-nál van bejegyezve — eladás esetén az új tulajdonos nem köteles automatikusan tisztelni | 🔴 magas |
| 4 | **Beruházás-vissza-térítés hiánya** | Art. 12: a bérlő által végzett fejlesztések (pl. töltőpont!) bérleti viszony megszűnésekor a locator tulajdonába kerülnek térítés nélkül | 🟡 közepes |
| 5 | **Tervezett karbantartás 30 napos előzetes értesítéssel** | Art. 14.2: a locator 30 nap értesítéssel végezhet 'major repairs' a bérlemény részein — operatív kockázat | 🟢 alacsony |

---

## 🌟 CROSS-DOC FELFEDEZÉS (a WOW pillanat)

A Cowork **NEM CSAK** a szerződést olvasta. Visszanézte a többi fájlt is és **kapcsolódó információt** talált:

📂 **Meeting transcript (`meetings/meeting_transcript_20250224.srt`) — 41. bemondás:**
> *„Béla bácsi szilveszterkor mondott valamit, hogy gondolkodik egy-két ingatlana eladásán — utána kéne nézni nehogy a miénk legyen, ahol a raktár van."*

🚨 **Riasztás:** Ha a Calea Băieșenilor 22 érintett az eladási tervekben, az AFM 5 éves stabilitás-követelménye **közvetlenül sérül**. A bérleti szerződés Art. 8.3 + a karte funciară-bejegyzés hiánya (3. pont fent) miatt az új tulajdonos nem automatikusan kötelezett — **azonnali tisztázás szükséges**.

📂 **Egyébként a `email_exportok/raspuns_bela_iosif_2025-02-26.txt` fájl (Béla bácsi válasza már megérkezett!)** — ezt is felfedeztem:
- ✅ A Calea Băieșenilor 22 **NEM eladó** (családi örökség)
- ✅ Hajlandó **contract prelungire 2035-ig** (act adițional)
- ✅ Felajánl **declarație notarială**: nem ad el 10 évig + Art. 21 + Art. 1811 Cod Civil automatikus utódlás
- ✅ A szilveszteri megjegyzés **más parcellákra** (Sub Cetate-i 4 ha agricol) vonatkozott — nem a TransOffice telephelyre

**Azaz: az 1, 3 kockázat → ✅ megoldódott Béla bácsi proaktív javaslata által.** Csak az act adițional aláírása + declarație notarială beszerzése maradt.

---

## Akcióterv (a pályázat előtti 7 napban)

| Nap | Akció | Felelős |
|-----|-------|---------|
| Kedd (ma) | Tisztázó email Béla bácsinak — **MÁR ELKÜLDVE / VÁLASZ MEGÉRKEZETT** | Op Mgr |
| Szerda reggel | Köszönő-válasz + vételi opció érdeklődés | Márton (Op Mgr fogalmaz) |
| Szerda dél | Notár (BNP Munteanu Andrei) felhívása az act adițional-ra | Béla bácsi (felajánlotta) |
| Csütörtök reggel | Declarație notarială beszerzése + act adițional aláírás | Mindketten |
| Csütörtök este | Másolat csatolása az AFM dossiéba (M-15 acord + M-16 imobil mellékletek) | Op Mgr |
| Péntek 14:00 | Beadás | Márton |

**Bonus:** Béla bácsi vételi opciót is felajánlhat (Márton kérdezhet rá) — ez **hosszú távú stabilitás-növelés** lenne, de a pályázat szempontjából **most nem szükséges**.

---

## Mit jegyez meg a Cowork a CLAUDE.md-be (automatikus)

➕ Hozzáadom a CLAUDE.md-hez:
- Béla bácsi notar: BNP Munteanu Andrei
- Béla bácsi felajánlott declarație szövegtartalma (10 év + Art. 1811)
- Act adițional 2035-ig — folyamatban
