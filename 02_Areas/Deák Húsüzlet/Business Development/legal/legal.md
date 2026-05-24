---
file: legal.md
version: v1.2
date: 2026-04-20
status: DRAFT — jogi átnézésre vár
owner: Szabolcs
id: 8c3361c8-91ed-424a-b72c-5295ad49ac37
index_schema_version: 1
---

# DH Pilot — Jogi követelmények és teendők

## Összefoglaló

A Deák Húsmíves online rendelési platform (deakhus.ro) és a hozzá tartozó mobil app jogi megfelelőségének biztosítása. A platform élelmiszer rendelést és házhozszállítást tesz lehetővé Székelyudvarhelyen.

---

## 1. Jelenlegi állapot

| Dokumentum | Státusz | Hol van | Jira |
|-----------|---------|---------|------|
| Privacy Policy | ✅ KÉSZ | deakhus.ro/privacy | — |
| ÁSZF (Felhasználási Feltételek) | ❌ HIÁNYZIK | — | DH-130 |
| Impresszum / Legal Notice | ❌ HIÁNYZIK | — | DH-131 |
| GDPR consent (regisztráció) | ⚠️ ELLENŐRIZNI | app regisztrációs flow | DH-132 |
| Push notification opt-in | ❌ NEM RELEVÁNS MÉG | v0.4-ben kell | DH-134 |
| Partnerségi megállapodás (Deák) | ✅ DRAFT KÉSZ | Contract-cadru v1.2 + Comanda nr.1 v1.3 — aláírásra vár | — |
| Jogi szolgáltató tisztázása | ❌ DÖNTÉS KELL | — | DH-133 |
| App Store account | ❌ HIÁNYZIK | v0.4-ben kell | DH-135 |
| ANSVSA szállítási engedély | ⚠️ ELLENŐRIZNI | DH felelőssége | DH-136 |
| Cookie policy | ⚠️ ELLENŐRIZNI | — | DH-137 |

---

## Jira ticketek

| Ticket | Összefoglaló | Verzió | Label |
|--------|-------------|--------|-------|
| [DH-130](https://exarlabs.atlassian.net/browse/DH-130) | ÁSZF draft készítése | v0.3-beta | legal |
| [DH-131](https://exarlabs.atlassian.net/browse/DH-131) | Impresszum oldal létrehozása | v0.3-beta | legal |
| [DH-132](https://exarlabs.atlassian.net/browse/DH-132) | GDPR consent checkbox a regisztrációban | v0.3-beta | legal, GDPR |
| [DH-133](https://exarlabs.atlassian.net/browse/DH-133) | Jogi szolgáltató tisztázása (BLOCKER) | v0.3-beta | legal, blocker |
| [DH-134](https://exarlabs.atlassian.net/browse/DH-134) | Privacy Policy frissítés (push + device) | v0.4 | legal, GDPR |
| [DH-135](https://exarlabs.atlassian.net/browse/DH-135) | App Store developer account + compliance | v0.4 | legal, blocker |
| [DH-136](https://exarlabs.atlassian.net/browse/DH-136) | DH szállítási engedély (ANSVSA) ellenőrzés | v0.3-beta | legal |
| [DH-137](https://exarlabs.atlassian.net/browse/DH-137) | Cookie policy ellenőrzés | v0.3-beta | legal, GDPR |

---

## 2. Mikor kell mi?

### v0.3 Beta (ápr. 14-17) — AJÁNLOTT

- **ÁSZF draft** a webapp-on (láblécben link) — a beta userek is elfogadják a feltételeket
- **Impresszum** oldal a cégadatokkal
- **GDPR consent checkbox** a regisztrációnál ("Elfogadom az ÁSZF-et és az Adatvédelmi tájékoztatót")

> Megjegyzés: A beta alatt a kockázat alacsony (30 ismerős user), de jó ha a flow-ba már be van építve, mert utána nehezebb változtatni.

### v0.4 Mobil App — KÖTELEZŐ (launch-blocker)

- **ÁSZF végleges verzió** — az app store-ok megkövetelik
- **Privacy Policy frissítés** — ki kell egészíteni: push notification adatkezelés, device ID, app analytics
- **Push notification opt-in** — GDPR-kompatibilis hozzájárulás-kérés
- **Apple App Store specifikus:**
  - App Privacy "nutrition labels" (milyen adatot gyűjt az app)
  - Age rating (élelmiszer app → 4+)
  - App Store Review Guidelines megfelelés (4.2 — Minimum Functionality)
- **Google Play specifikus:**
  - Data Safety section kitöltése
  - Target audience and content declaration
  - Families Policy compliance (ha 13 év alattiak is használhatják — valószínűleg nem releváns)

### v0.5 Online fizetés — HA ELJUTUNK IDE

- **Fizetési feltételek** az ÁSZF-ben (visszatérítés, reklamáció)
- **PCI DSS** — a fizetési szolgáltató (Stripe/etc.) kezeli, de az ÁSZF-ben hivatkozni kell
- **Számlázási kötelezettség** — elektronikus számla kiállítása
- **Fogyasztói jogok** frissítés (elállási jog, reklamáció kezelése online fizetésnél)

---

## 3. ÁSZF — mit kell tartalmaznia

### Kötelező elemek (Legea 365/2002 + EU e-commerce direktíva):

1. **Szolgáltató azonosítása**
   - Cég neve (EXARGROUPS S.R.L. / vagy a Deák Húsmíves jogi entitása?)
   - CUI/CIF szám
   - Székhely címe
   - Kapcsolattartási email és telefon

2. **Szolgáltatás leírása**
   - Online húsrendelés és házhozszállítás
   - Működési terület: Székelyudvarhely
   - Szállítási idősáv és feltételek

3. **Rendelési folyamat**
   - Hogyan jön létre a szerződés (rendelés leadása → visszaigazolás)
   - Rendelés módosítása/lemondása (meddig lehetséges?)
   - Minimum rendelési érték (ha van)

4. **Árak és fizetés**
   - Árak ÁFA-val (bruttó)
   - Fizetési mód: készpénz szállításkor (pilot fázis)
   - Szállítási díj szabályok (150 RON felett ingyenes, alatta 10 RON)

5. **Szállítás**
   - Szállítási terület
   - Szállítási idő (rendelés leadása → kézbesítés)
   - Mi történik ha a vásárló nincs otthon?

6. **Elállási jog és reklamáció**
   - Romlandó élelmiszer → 14 napos elállási jog NEM vonatkozik (EU 2011/83 irányelv, 16. cikk, d pont)
   - DE: minőségi reklamáció kezelése (rossz termék, hiányos szállítás)
   - Reklamációs határidő és eljárás

7. **Felelősségkorlátozás**
   - Az app "as-is" a pilot fázisban
   - Élelmiszer minőségért a Deák Húsmíves felel
   - Platform üzemeltetésért az EXARGROUPS S.R.L. felel

8. **Adatvédelem**
   - Hivatkozás a Privacy Policy-ra
   - GDPR jogok összefoglalása

9. **Panaszkezelés**
   - ANPC (Autoritatea Națională pentru Protecția Consumatorilor) elérhetősége
   - OPC Harghita elérhetősége
   - Online vitarendezés: https://ec.europa.eu/consumers/odr

10. **Módosítások**
    - Az ÁSZF módosításának joga fenntartva
    - Értesítés módosítás esetén

---

## 4. Impresszum — kötelező tartalom

```
Szolgáltató: [EXARGROUPS S.R.L. / Deák Húsmíves entitás — TISZTÁZNI]
CUI: [...]
Székhely: Székelyudvarhely, [cím]
Email: [...]
Telefon: [...]

Tárhelyszolgáltató: [hosting provider adatai]

Az oldal a Legea 365/2002 és az EU 2000/31/EK irányelv hatálya alá tartozik.
```

---

## 5. Nyitott jogi kérdések (TISZTÁZNI)

| # | Kérdés | Miért fontos | Határidő |
|---|--------|-------------|----------|
| 1 | **Ki a jogi szolgáltató?** EXARGROUPS S.R.L. vagy a Deák Húsmíves? | Az ÁSZF és az Impresszum ettől függ. Ha EXARGROUPS S.R.L. üzemelteti a platformot és a DH szállít, mindkettőt meg kell nevezni. | v0.3 beta előtt |
| 2 | **Van-e a Deák Húsmívesnek élelmiszer-szállítási engedélye?** | Házhozszállításhoz speciális ANSVSA (élelmiszer-biztonsági hatóság) engedély kellhet. A hűtőlánc fenntartása dokumentálandó. | v0.3 beta előtt |
| 3 | **Partnerségi megállapodás** | ✅ Contract-cadru v1.2 + Comanda nr.1 v1.3 elkészült (6,8% platformdíj). Aláírásra vár. | Aláírás |
| 4 | **App store fejlesztői fiók** | Apple Developer Program (99 USD/év) + Google Play Console (25 USD egyszeri). Kinek a nevére? | v0.4 előtt |
| 5 | **Cookie policy kell-e?** | A webapp használ-e cookie-t? Ha igen (analytics, session), kell banner. | v0.3 beta előtt ellenőrizni |
| 6 | **Élelmiszer allergia tájékoztatás** | EU 1169/2011 rendelet — allergén információ kötelező. Az app-ban ezt kezelni kell? Vagy elég ha a bolt biztosítja? | v0.4 |

---

## 6. Költségbecslés

| Tétel | Becsült költség | Megjegyzés |
|-------|----------------|------------|
| Ügyvédi ÁSZF készítés/ellenőrzés | 500-1500 RON | Ajánlott, de draft házon belül is készíthető |
| Apple Developer Program | ~99 USD/év | v0.4-hez kell |
| Google Play Console | ~25 USD (egyszeri) | v0.4-hez kell |
| GDPR audit (opcionális) | 1000-3000 RON | Pilot-hoz nem feltétlenül szükséges |

---

## 7. Javaslat

### Minimum viable legal (v0.3 beta):

1. ÁSZF draft (akár AI-generált, majd ügyvéd ellenőrzi)
2. Impresszum oldal
3. GDPR consent checkbox a regisztrációnál
4. Cookie policy (ha releváns)

### App store ready (v0.4):

1. ÁSZF végleges (ügyvéd által ellenőrzött)
2. Privacy Policy frissítés (push, device data)
3. Apple/Google developer account + policy compliance
4. ANSVSA szállítási engedély ellenőrzés

### Szabolcs döntésre vár:

- [ ] Ki a jogi szolgáltató? (EXARGROUPS S.R.L. / DH / mindkettő)
- [ ] Van-e DH-nak szállítási engedélye?
- [ ] Ügyvédet bevonunk-e az ÁSZF-hez?
- [ ] App store fiók kinek a nevére?
