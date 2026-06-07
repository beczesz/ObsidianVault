---
title: "Adatvédelmi Szabályzat"
description: "A deakhus.ro online platform adatvédelmi szabályozása, amely ismerteti az EXARGROUPS S.R.L. adatkezelési gyakorlatát, a gyűjtött személyes adatokat, Firebase Analytics használatát, cookie-kat és az érintett személyek jogait a GDPR alapján. Üzemeltetőknek és felhasználóknak egyaránt szükséges."
description_source: auto
description_hash: 66522c1a00c7abf0
version: "1.0"
status: DRAFT
created: 2026-04-17
last_modified: 2026-04-21
effective_date: "2026-04-17"
author: EXARGROUPS S.R.L.
applies_to: deakhus.ro
language: hu
changelog:
  - version: "1.0"
    date: 2026-04-21
    summary: "Nyelvspecifikus fájl létrehozva (magyar)"
id: a22aa8b2-77bf-4be5-b2f7-1fbc9f62f90b
index_schema_version: 1
---
# ADATVÉDELMI SZABÁLYZAT

**Deák Húsmíves Online Platform — deakhus.ro**

## 1. Az adatkezelő

A deakhus.ro platform üzemeltetője és kizárólagos adatkezelője:

**EXARGROUPS S.R.L.**
Székhely: Székelyudvarhely (Odorheiu Secuiesc), Orbán Balázs u. 9.
CUI: RO41839221 · J19/789/2019
Képviselő: Becze Szabolcs
Email: contact@exar.ro

A platform megrendelője és partnere, aki szállítási adatokhoz **adatfeldolgozói** minőségben fér hozzá:

**DEAK PROD SRL**
Székhely: Székelyudvarhely, Solymossy u. 9.
CUI: 4845288 · J19/1038/1993

## 2. Milyen adatokat gyűjtünk

Regisztráció és rendelés során az alábbi személyes adatokat kérjük:

- **Teljes név** — fiók azonosítás és szállítási cím feltüntetése
- **Email cím** — Google OAuth vagy email/jelszó alapú belépés
- **Telefonszám** — szállítási kapcsolattartás
- **Szállítási cím** — kézbesítés helyszíne

Különleges személyes adatokat (egészségügyi, biometrikus, vallási stb.) **nem gyűjtünk**. 18 év alatti személyektől tudatosan nem gyűjtünk adatot.

## 3. Az adatgyűjtés célja és jogalapja

| Adatkezelési cél | Jogalap (GDPR) | Érintett adatok |
|---|---|---|
| Fiók létrehozása és kezelése | Szerződés teljesítése — Art. 6(1)(b) | Név, email |
| Rendelés feldolgozása | Szerződés teljesítése — Art. 6(1)(b) | Név, cím, telefon |
| Házhozszállítás | Szerződés teljesítése — Art. 6(1)(b) | Cím, telefon |
| Rendelési előzmények és státusz | Szerződés teljesítése — Art. 6(1)(b) | Rendelési adatok |
| Firebase Analytics (platformhasználat) | Hozzájárulás — Art. 6(1)(a) | Anonim eseményadatok |
| Számviteli kötelezettségek | Jogi kötelezettség — Art. 6(1)(c) | Tranzakciós adatok |

Adatait **marketing célokra nem használjuk**, automatizált döntéshozatalt és profilalkotást **nem végzünk**.

## 4. Adatok megosztása harmadik felekkel

- **DEAK PROD SRL** — a rendelés teljesítéséhez szükséges szállítási adatokat (név, cím, telefon) kapja meg adatfeldolgozói szerződés alapján.
- **Google Firebase / Google LLC** — az alkalmazás infrastruktúráját (autentikáció, analytics) biztosítja. Google adatvédelmi irányelve: https://policies.google.com/privacy
- **Frappe Technologies / EXARGROUPS S.R.L. infrastruktúra** — a backend platformot üzemeltetjük saját szervereinken, harmadik félnek nem adjuk át.

Adatait egyéb harmadik félnek **nem adjuk el és nem adjuk át**, kivéve ha jogszabály kötelez rá.

## 5. Firebase Analytics

A platformon Google Firebase Analytics szolgáltatást használunk a felhasználói élmény javítása érdekében. Ez a rendszer:

- Anonim, aggregált eseményadatokat gyűjt (pl. melyik oldalt nézik, mennyi ideig)
- Nem gyűjt személyes azonosítókat (névtelen session-azonosítót használ)
- QR-kód alapú forgalomkövetést végez (melyik bolt előtt helyezett ki QR-kódot szkennelek)

Az Analytics csak az Ön hozzájárulásával (cookie banner elfogadása) aktiválódik. Hozzájárulása bármikor visszavonható a fiókbeállításokban.

## 6. Cookie-k (sütik)

| Cookie típusa | Célja | Lejárat | Hozzájárulás |
|---|---|---|---|
| Session cookie | Bejelentkezett állapot megőrzése | Böngésző zárásáig | Nem szükséges (működés) |
| Firebase Analytics | Platformhasználat elemzése | 14 hónap | Szükséges |

Harmadik fél marketing cookie-t **nem alkalmazunk**.

## 7. Adatmegőrzési idő

- **Felhasználói fiók adatai** — a fiók aktív időszakára + törlés után 2 évig (visszaélés-megelőzés)
- **Rendelési adatok** — 5 évig (román számviteli jogszabály, Legea 82/1991)
- **Analytics adatok** — 14 hónapig (Firebase alapértelmezett)

Fiókja törlését bármikor kérheti a contact@exar.ro címen. Törlés után a számviteli kötelezettséghez szükséges adatokat kivéve minden adatát töröljük.

## 8. Adatbiztonság

Az adatok védelme érdekében az alábbi intézkedéseket alkalmazzuk:

- Minden adatátvitel HTTPS titkosítással történik
- A jelszavakat titkosított formában (hash) tároljuk — bejelentkezéshez Google OAuth-ot ajánlunk
- A Firebase infrastruktúrát a Google SOC 2 / ISO 27001 tanúsítványokkal üzemelteti
- Az adminisztrációs felülethez csak azonosított munkatársak férnek hozzá

Adatvédelmi incidens esetén az érintetteket és az ANSPDCP hatóságot a GDPR 72 órás határidején belül értesítjük.

## 9. Az Ön jogai

A GDPR alapján Ön jogosult:

- **Hozzáférési jog (Art. 15)** — kérheti az Önről tárolt adatok másolatát
- **Helyesbítési jog (Art. 16)** — kérheti a pontatlan adatok javítását
- **Törlési jog / „elfeledtetéshez való jog" (Art. 17)** — kérheti adatai törlését
- **Adathordozhatóság (Art. 20)** — adatait géppel olvasható formában kérheti
- **Tiltakozási jog (Art. 21)** — jogos érdeken alapuló adatkezelés ellen tiltakozhat
- **Hozzájárulás visszavonása** — az Analytics hozzájárulást bármikor visszavonhatja

Panasszal az **ANSPDCP** (Autoritatea Națională de Supraveghere a Prelucrării Datelor cu Caracter Personal) hatósághoz fordulhat: https://www.dataprotection.ro

## 10. Kapcsolat és panasz

Adatvédelemmel kapcsolatos kérdéseivel és kérelmeivel kérjük forduljon hozzánk:

**EXARGROUPS S.R.L.**
Email: contact@exar.ro
Cím: Székelyudvarhely, Orbán Balázs u. 9.

Kérelmét a beérkezéstől számított **30 napon belül** megválaszoljuk.