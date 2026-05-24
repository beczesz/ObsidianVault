# Data Completion Board — AFM Mobilitate Verde IMM 2026
## TransOffice Trade SRL — élő munkatábla

> **Készítette:** Cowork (AI) + Operations Manager
> **Indítás:** 2025.02.25 18:30 (kedd este)
> **Beadási határidő:** 2025.02.28 péntek 16:00 (4 munkanap)
> **Frissítés:** lásd alul versionhistory

---

## 📊 Dashboard

```
📋 PROIECT:        AFM Mobilitate Verde IMM 2026 — Intervenția 1.4.1
🎯 CÉL:            2 vehicul electric N1 + 1 stație AC reîncărcare
🗓️  HATÁRIDŐ:       2025.02.28 péntek 16:00
⏰ HÁTRALÉVŐ:      4 munkanap (KEDD ESTE → PÉNTEK 16:00)

📦 ÖSSZES TODO:    23 (17 melléklet + 6 nyilatkozat)
✅ KÉSZ:           0 / 23
🟡 FOLYAMATBAN:    0 / 23
⏳ HÁTRA:          23 / 23

🔴 KRITIKUS (külső válasz vár):  2 / 23
   → T-05  M-05 Mérleg + EK 2023-2024 (4.A)
   → T-16  M-16 Bérleti szerződés stabilitás (4.B)

📐 ELIGIBILITY pontszám becslés:  64-75 (min. 60 kell) ✓
💰 Külső költség becslés:        850-1.050 RON
👥 Felelős személyek:            6 (Te, Márton, Enikő, Attila, Ilona, könyvelő)
```

---

## 👥 Responsibility Map (felelősök tábla)

| Felelős | Szerep | Hozzárendelt feladatok | Becsült munkaóra |
|---------|--------|-----------------------|------------------|
| **Te (Operations)** | Koordinátor + AI munka | T-01 (UBO koord.), T-11 (flotta-felmérés), T-13 (M-13 üzleti terv), T-14 (dealer-megkeresés), T-16 (M-16 email Béla), N-01..N-06 sablon | **8-12 ó** |
| **Márton (ügyvezető)** | Aláírások, döntések | T-03 (UBO közjegyző), N-03..N-06 aláírás, M-13 jóváhagyás, **közvetlen kapcsolat Béla bácsival** | **2-3 ó** |
| **Enikő (könyvelő/admin)** | Pénzügyi mellékletek koord. | T-01 (M-01), T-05 (M-05 — kapcsolat a külsős könyvelővel), T-06 (M-06), T-07 (M-07), T-08 (M-08), T-09 (M-09), T-10 (M-10), N-02 | **4-6 ó** |
| **Bíró Attila (raktárvezető)** | Flotta-input | T-11 (járműflotta-leltár), T-12 (forgalmi engedélyek begyűjtése sofőröktől) | **3-4 ó** |
| **Ilona (volt admin)** | Régi dokumentum-archeológia | T-02 (act constitutiv keresése a régi mappákban — telefonon) | **1 ó** |
| **Külsős könyvelő** | Mérleg + EBITDA | T-05 válasz (kritikus!) | (külsős) |
| **Notar Andrei Munteanu** | Közjegyzői hitelesítés | T-03 (UBO), opc. Béla bácsi declarație | (külsős) |
| **Béla bácsi (Locator)** | Bérleti stabilitás | T-16 válasz (kritikus!) | (külsős) |

---

## 📝 Akcióterv táblázat (23 sor)

| ID | Melléklet/Nyilatkozat | Felelős | Bemenet | Határidő | Státusz | Megjegyzés |
|----|-----------------------|---------|---------|----------|---------|------------|
| **🔴 KRITIKUS — KÜLSŐ VÁLASZ VÁR** |
| **T-05** | **M-05** Mérleg + EK 2023-2024 | **Enikő → Külsős könyvelő** | — | **SZERDA délig várt válasz** | ⏳ TODO | **MA ESTE email küldés!** A külsős könyvelő nevét csak Márton tudja |
| **T-16** | **M-16** Telephely stabilitás (Béla bácsi) | **Te (email)** | — | **SZERDA-CSÜTÖRTÖK válasz** | ⏳ TODO | **MA ESTE email küldés!** A meeting transcriptben utalás Béla bácsi eladási szándékára → tisztázni kell |
| **🟡 RUTIN — ONLINE BESZERZÉS** |
| T-01 | M-01 Cégkivonat (max 30 napos) | Enikő | — | szerda dél | ⏳ TODO | ONRC online InfoCert, 50 RON |
| T-02 | M-02 Act constitutiv konsolidat | Te + Ilona | telefon Ilonának | szerda este | ⏳ TODO | régi mappákban van valahol; B-terv: ONRC újra |
| T-04 | M-04 CAEN-kód igazolás | — | M-01-vel együtt | szerda dél | ⏳ TODO | a cégkivonat tartalmazza |
| T-06 | M-06 Certificat fiscal ANAF | Enikő | — | csütörtök dél | ⏳ TODO | ANAF SPV online; A 30 napos szabály miatt PÉNTEK reggel megújítjuk! |
| T-07 | M-07 Bankszámlakivonat 3 hó | Enikő | — | szerda | ⏳ TODO | Banca Transilvania internet banking |
| T-08 | M-08 Saját erő igazolás | Enikő | M-07 alapján | szerda | ⏳ TODO | Hivatkozás kiválasztott tételekre |
| T-09 | M-09 REGES kivonat (12 hó) | Enikő | — | csütörtök | ⏳ TODO | REGES online |
| T-10 | M-10 ITM bérügyi igazolás | Enikő | — | csütörtök | ⏳ TODO | ITM Harghita online kérelem |
| **🟡 KÖZJEGYZŐI / KÜLSŐ SZAKEMBER** |
| T-03 | M-03 UBO-nyilatkozat | Márton | időpont notar | csütörtök reggel | ⏳ TODO | Notar Andrei Munteanu — ugyanaz aki a bérleti szerződést hitelesítette |
| T-17 | M-17 Hálózati csatlakozás | Te | — | csütörtök este | ⏳ TODO | 1 punct AC < 11 kW → declarație pe propria răspundere elég, NEM kell aviz tehnic |
| **🟡 BELSŐ ADAT-ÖSSZESZEDÉS** |
| T-11 | M-11 Járműflotta-leltár | Te + Attila | felmérés telephelyen | szerda délután | ⏳ TODO | Márton "3? 4?" — pontosítani kell. Talon-okat előszedjük |
| T-12 | M-12 Forgalmi engedélyek + RCA | Te + sofőrök | M-11-vel együtt | szerda délután | ⏳ TODO | sofőröknél vannak a talon-ok |
| **🟡 GENERÁLT TARTALOM (Cowork)** |
| T-13 | M-13 Üzleti terv (8 kapitulus) | Te + Cowork | M-05 + M-11 alapok | csütörtök este | ⏳ TODO | Anexa 6 sablon alapján; T-05-ra várva |
| T-14 | M-14 Műszaki specifikáció járművek | Te (dealer-megkeresés) | — | szerda-csütörtök | ⏳ TODO | Renault Kangoo E-Tech vagy Citroen e-Berlingo |
| T-15 | M-15 3 dealer-árajánlat | Te | — | csütörtök | ⏳ TODO | Helyi (Brașov) + regionális (Cluj) dealer-ek |
| **🟢 NYILATKOZATOK (sablonok)** |
| T-N1 | N-01 KKV-státusz nyilatkozat | Te + Cowork | — | csütörtök este | ⏳ TODO | Sablon kitöltés |
| T-N2 | N-02 De minimis nyilatkozat | Enikő → Könyvelő | T-05 függvénye | csütörtök este | ⏳ TODO | Cont 7411-7414 mozgások |
| T-N3 | N-03 Foglalkoztatási köt. nyil. | Te + Márton | — | péntek reggel | ⏳ TODO | Sablon |
| T-N4 | N-04 Környezetvédelmi nyil. | Te + Márton | — | péntek reggel | ⏳ TODO | Sablon |
| T-N5 | N-05 GDPR-nyilatkozat | Te + Márton | — | péntek reggel | ⏳ TODO | Sablon |
| T-N6 | N-06 Összeférhetetlenségi nyil. | Márton | — | péntek reggel | ⏳ TODO | Sablon |

---

## ⛓️ Kritikus út (heti bontás)

```
KEDD ESTE (ma) ←─── KEZDET
├─ T-05 EMAIL külsős könyvelőnek (4.A) ★★★
└─ T-16 EMAIL Béla bácsinak (4.B) ★★★

SZERDA
├─ Reggel:    T-05 + T-16 válaszra várás (közben más feladatok)
├─ T-01, T-02, T-06, T-07, T-08 — Enikő letölti
├─ T-11, T-12 — Te + Attila a raktárnál
└─ Délután:   T-05 válasz remény → ha igen, T-13 üzleti terv kezdődhet

CSÜTÖRTÖK
├─ Reggel:    T-03 UBO közjegyzői (Márton + notar)
├─ T-13 üzleti terv (Te + Cowork) ←── függ T-05-től
├─ T-14, T-15 dealer-megkeresések (párhuzamos)
├─ T-09, T-10 REGES + ITM
└─ Este:      T-N1..T-N6 nyilatkozatok generálása

PÉNTEK
├─ Reggel:    T-N3..T-N6 Márton aláírja
├─ T-06 megújítás (30 napos szabály!)
├─ T-17 hálózati declarație
├─ 10:00-11:00: PDF konszolidáció (mind 23 dokumentum)
├─ 11:00-12:00: Auditor (opc.) végigfutás
└─ 12:00-16:00: BEADÁS MySMIS-en (4 órás puffer)
```

---

## 🚦 Kockázatok és mitigation

| Kockázat | Valószínűség | Hatás | Mitigation |
|----------|--------------|-------|------------|
| T-05 könyvelő nem válaszol szerdáig | Közepes | Magas | Telefon Mártontól szerda reggel; B-terv: 2022-es Ilona-számokkal becslés |
| T-16 Béla bácsi nem válaszol | Alacsony | Magas | Telefon Mártontól (családi kapcsolat); B-terv: declarație notarială pre-emptív |
| T-11 járműflotta hiányos (papír talon-ok elvesztek) | Közepes | Közepes | Sofőröket előbányászni; Servicii Auto-tól ellenőrzés |
| T-15 dealer-ek nem küldenek árajánlatot időben | Közepes | Közepes | Online listaárakkal becslés, frissítés a contractare-ben |
| Karácsonyi szünet utáni elhagyások (Enikő szabin?) | Alacsony | Magas | Enikő hozzáférhetőségét elsőként ellenőrizni |
| MySMIS portál túlterhelt péntek délután | Magas | Közepes | 12:00-ra kész, 4 órás puffer |

---

## 🔄 Napi sync javaslat

5-perces stand-up Mártonnal és Enikővel **minden reggel 9:00-kor**:
1. Mi készült el tegnap?
2. Min dolgozol ma?
3. Mi blokkol? (különösen: 4.A és 4.B válaszok)

A **Productivity plugin** automatikusan frissíti a TODO-státuszokat. A board egyetlen igazsága ez a fájl + a Cowork TODO-store.

---

## 📜 Frissítési előzmények

| Dátum / Idő | Változás | Frissítette |
|-------------|----------|-------------|
| 2025.02.25 18:30 | Tábla létrehozva, 23 TODO felsorolva, 2 ⛔ kritikus azonosítva | Cowork + Te |
| 2025.02.25 18:45 | Email-ek elküldve T-05-höz (külsős könyvelő) és T-16-hoz (Béla bácsi) | Te |
| ... | (folyamatos frissítés F4-F5-F6 alatt) | |

---

## 🎯 KÖVETKEZŐ LÉPÉS

**MA ESTE 19:00-IG:**
1. ✉️ Email-tervezet a külsős könyvelőnek (T-05) — Cowork generál, Te küldöd
2. ✉️ Email-tervezet Béla bácsinak (T-16) — Cowork generál, Te küldöd

**Holnap reggel várjuk a válaszokat.** Addig elindulhatunk a rutin-feladatokkal (T-01, T-06, T-07, T-08, T-11, T-12).

→ **Folytatás: F4 — Kommunikáció + feldolgozás**
