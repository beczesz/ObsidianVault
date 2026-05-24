---
title: DH analytics stack és privacy döntés (Firebase Analytics ship)
version: 3.0
date: 2026-04-14
author: Becze Szabolcs
description: Végleges stack döntés: Firebase Analytics ship (DH-104). Consent banner kötelező. Capacitor mobil v0.4-re kompatibilis. RO joghatóság (ANSPDCP).
id: 594e9a66-2b61-4f3e-89e9-141793b4913e
index_schema_version: 1
---

# DH Analytics stack — Firebase Analytics ship (Final)

## 0. Stack döntés (v3.0)
A csapat úgy döntött, hogy DH-104 ship: Firebase Analytics integrálva a Vue PWA-ba, később a Capacitor mobil appba is. A korábbi v2.0 first-party Frappe-only javaslat ELVETVE. Az alábbi dokumentum ezt a valós stack-et elemzi.

## 1. A 7 kérdés rövid válasza

| # | Kérdés | Válasz |
|---|--------|--------|
| 1 | Consent screen kell? | **IGEN, kötelező.** |
| 2 | Miért trigger? | Firebase cookie + localStorage + IndexedDB + FID + USA transzfer + Google joint controller |
| 3 | Consent Mode v2 megoldja? | NEM helyettesíti a bannert. Basic módot használni default denied-del. |
| 4 | USA transzfer? | DPF adekvátsági alap (2023 óta). Firebase DPA SCC backup. PP-ben külön szekció. |
| 5 | iOS ATT? | NEM, ha Google Signals + Google Ads link OFF. App Privacy Labels kötelezőek. |
| 6 | Banner minimum? | EDPB compliant: egyenlő Accept/Reject, no dark pattern, bottom bar, Consent Mode basic |
| 7 | DH-137 lezáró szöveg? | Lent a 7. szekcióban. |

## 2. Jogi triggerek részletesen

### 2.1 506/2004 Art. 4 alin. (5) (RO ePrivacy)
A Firebase Analytics az alábbiakat írja a felhasználó eszközére:
- Web: `_ga` és `_ga_<CONTAINER_ID>` cookie-k (GA4 infra, 2 év)
- Web: localStorage kulcsok `firebase:host:<project>`, `firebase:authUser:<project>`
- Web: IndexedDB `firebase-analytics-database` offline event queue-ra
- Web és mobil: Firebase Installation ID (FID), perzisztens, kb. 1 hónapos rotáció
- iOS: IDFV (default), IDFA csak ha explicit kérve
- Android: AppSet ID / Advertising ID GMS-en

Egyik sem strict-necessary a hús online megrendeléséhez. **Art. 5(3) Directive 2002/58/EC és EDPB Guidelines 2/2023** kifejezetten SDK identifier-ekre is alkalmazza az Art. 4(5) trigger-et.

Következmény: **express, pre-consent, opt-in banner kötelező.**

### 2.2 GDPR Art. 6(1) jogalap
A Firebase Analytics által gyűjtött pszeudonim adat (FID, IP, eseményfolyam, eszközattribútumok) GDPR értelmében személyes adat (Recital 26). Jogalap szükséges.

**Art. 6(1)(a) consent:** ez az egyetlen védhető alap Firebase esetén, mivel
**Art. 6(1)(f) legitimate interest** NEM védhető, mert a Google saját céljaira is felhasználja az adatot (Google Ads modeling, platformfejlesztés, benchmark statisztikák). A Google a Firebase Terms és Google Analytics 4 Terms szerint bizonyos célokra joint controller státuszba lép. A balancing test elbukna az user interest oldalon.

**Art. 6(1)(b) contract:** nem megfelelő, mert az analitika nem szükséges a szerződés teljesítéséhez.

### 2.3 GDPR Art. 26 joint controllership
A Google Analytics 4 / Firebase Analytics feltételei szerint a Google **joint controller** bizonyos célokra (ki-kicsoda-bencmarking, aggregált analytics piac-szinten). Joint controller agreement-et a Google szolgáltatja a Firebase Console-ban. Elfogadás pipa kötelező.

### 2.4 GDPR Art. 28 processor
A Google Cloud Firebase Data Processing Addendum (DPA) elfogadása a Firebase Console-ban kötelező. Ez fedi a processzálási célokat, amelyekben a Google nem joint controller, hanem feldolgozó.

### 2.5 GDPR Art. 13 tájékoztatás
Privacy Policy tartalmi követelmények:
- Google LLC explicit megnevezése mint címzett/feldolgozó
- USA transzfer + DPF adekvátság
- Cookie-k taxonómiája és élettartama
- FID és IDFV használata
- Tiltakozás joga (Art. 21) kiemelt deklarálása
- Retention periods

### 2.6 GDPR Art. 44-49 nemzetközi transzfer
Részletek a 4. szekcióban.

### 2.7 Különbség az első-fél Frappe stack-hez képest
| | Frappe first-party | Firebase Analytics |
|---|-------------------|--------------------| 
| Device storage | session cookie only (strict nec) | cookies + LS + IndexedDB + FID |
| Harmadik fél | nincs | Google LLC |
| Joint controller | nincs | IGEN (Google) |
| USA transzfer | nincs | IGEN |
| Consent kell? | NEM | IGEN |
| Privacy Policy komplexitás | alacsony | magas (DPF, cookies, transzfer, retention) |
| ATT érintett? | NEM | potenciálisan IGEN |

## 3. Firebase Consent Mode v2

### 3.1 Mi ez
Google 2024-es mechanizmusa a consent állapot SDK-szintű tiszteletben tartására. Négy signal: `ad_storage`, `analytics_storage`, `ad_user_data`, `ad_personalization`. A banner hozza a döntést, a `gtag('consent', 'update', {...})` hívással áttranszferálod az SDK-nak.

### 3.2 Két mód
**Basic:** consent nélkül az SDK nem tüzel. Nulla adat, nulla cookie. A banner függvénye hogy bekapcsoljon.

**Advanced:** consent nélkül is küld cookieless pingeket (nincs `_ga` cookie, nincs FID kiírva). Google consent modeling aggregált adatot ad. Jogi státusza vitatott: technikailag nincs device storage (ePrivacy scope nélkül), de GDPR Art. 6 alapot kér a Google szerverre küldött ping miatt.

### 3.3 Megoldja a bannert?
**Nem.** A Consent Mode a banner döntését implementálja, nem helyettesíti. A banner kötelező marad.

### 3.4 DH javaslat
**Basic mód** + **default denied** minden 4 signal-re. Ha reject → nulla tracking, tiszta. Ha accept → teljes Firebase funkcionalitás. Az Advanced módot csak akkor mérlegelni, ha később Google Ads conversion tracking kerül a képbe, ami jelenleg nincs.

## 4. Nemzetközi transzfer (Art. 44-49)

### 4.1 Adat destination
Firebase Analytics alapértelmezetten Google LLC szervereken processzál (US, aggregáltan globálisan). Opcionálisan EU régió választható az Analytics-nek 2024 óta, de a Firebase Analytics dashboard aggregátumok globálisak maradnak.

### 4.2 Jogi alap a transzferre
**EU-US Data Privacy Framework** [Commission Implementing Decision (EU) 2023/1795](https://eur-lex.europa.eu/eli/dec_impl/2023/1795/oj) 2023 július óta adekvátsági alap. Google LLC self-certified a [dataprivacyframework.gov](https://www.dataprivacyframework.gov/list) listán mindhárom vertikumra (GDPR, Swiss DPA, UK extension).

**GDPR Art. 45** → adekvátsági alap
**GDPR Art. 46** → Google Firebase DPA tartalmaz SCC-ket mint másodlagos védelem

### 4.3 Mit kell intézni
1. Firebase Console → Settings → Data processing and privacy: DPA elfogadás checkbox ellenőrzése
2. Firebase Console → Analytics → Data Settings: EU-régiót választani, ahol lehet
3. Privacy Policy szöveg:

> „Adatait továbbítjuk a Google LLC-nek (1600 Amphitheatre Parkway, Mountain View, CA 94043, USA) mint Firebase Analytics szolgáltatás üzemeltetőjének. A Google LLC az EU-US Data Privacy Framework szerint tanúsított adatvédelmi minősítéssel rendelkezik, ami a GDPR 45. cikk szerinti megfelelő védelmi szintet biztosít. Másodlagos védelemként a GDPR 46. cikk szerinti standard szerződéses klauzulákat alkalmazzuk."

4. Belső egyoldalas Transfer Impact Assessment (TIA) dokumentum

### 4.4 DPF kockázati monitoring
A DPF-et a NOYB már támadja (Schrems III). Ha 12-24 hónapon belül megbukik, át kell térni SCC + TIA alapra. DH-138 Legal epic-be tenni mint monitoring feladatot.

## 5. iOS ATT és Google Play Data Safety (Capacitor v0.4)

### 5.1 Apple ATT
Firebase Analytics default **IDFV-t** használ, nem IDFA-t. ATT prompt NEM kötelező.

ATT prompt KÖTELEZŐ lesz, ha bekapcsolsz bármelyiket:
- Google Signals (cross-device)
- Google Ads attribution / conversion tracking
- IDFA explicit request
- AdMob integráció

**DH konfig:** mindegyik OFF a Firebase Console-ban. Nincs ATT prompt.

### 5.2 Apple App Privacy Labels
App Store Connect → App Privacy kötelező kitöltés:
- **Identifiers:** Device ID (Firebase Installation ID, IDFV), Linked to User: IGEN
- **Usage Data:** Product Interaction, Linked to User: IGEN
- **Tracking (cross-app/site):** NEM (Google Signals off)
- **Diagnostics:** kimondható, nem kötelező

### 5.3 Google Play Data Safety Form
Play Console → Policy → App content → Data safety:
- Data types collected: "App interactions," "Device or other IDs"
- Shared with third parties: IGEN (Google)
- Processed ephemerally: NEM (Firebase persists)
- Encryption in transit: IGEN
- User data deletion possible: IGEN (delete account flow implementálni)

### 5.4 Mobil consent implementáció
A native app első indulásakor **consent képernyő kell** a Firebase SDK init ELŐTT. Capacitor Preferences-be menteni a döntést. Visszavonható a Beállítások menüben. Az ATT prompt (ha valaha aktiválódik) **nem helyettesíti** a GDPR consentet. 

## 6. Banner design ami nem tankolja a konverziót

### 6.1 Jogi minimum (EDPB Guidelines 05/2020 + 03/2022)
- Accept és Reject **egyenlő vizuális súly** (méret, szín, pozíció)
- Granularitás első képernyőn (Accept all / Reject all / Customize)
- Withdrawal legalább olyan könnyű mint a consent
- No dark pattern: nincs pre-checked, nincs timer, nincs X mint accept
- Nem cookie wall

### 6.2 Copy javaslat (HU, RO-val párhuzamosan)

**HU:**
```
Cookie-kezelés

A deakhus.ro használati statisztikákat gyűjt a szolgáltatás
fejlesztése céljából. Ehhez Google Firebase Analytics-et
használunk, ami cookie-kat és eszközazonosítókat tárol.

A kötelező működési cookie-k (bejelentkezés, kosár) mindenképp
aktívak maradnak.

[Részletek és beállítások]

[Elutasítom]              [Elfogadom]
```

**RO:**
```
Gestionarea cookie-urilor

deakhus.ro colectează statistici de utilizare pentru
îmbunătățirea serviciului. Folosim Google Firebase Analytics,
care stochează cookie-uri și identificatori de dispozitiv.

Cookie-urile strict necesare (autentificare, coș) rămân active.

[Detalii și setări]

[Refuz]                   [Accept]
```

### 6.3 Implementációs best practices
1. **Bottom bar, NEM modal.** Product browsing nem blokkolt.
2. **Consent Mode v2 basic default denied.** Reject = tiszta nulla tracking.
3. **Banner NE jelenjen meg a checkout flow-ban.** Landing vagy az első 10-15 másodperc browsingban.
4. **Privacy beállítások visszavonhatók** a user fiókban + a Privacy Policy-ban egy kattintás.
5. **Consent state tárolása:** User DocType mezőben authentikált usereknél, httpOnly cookie anonim usereknél, Capacitor Preferences mobilon.

### 6.4 Hibrid alternatíva (konverzió-minimális)
A Firebase Analytics CSAK a bejelentkezett userre fut. A publikus (nem-auth) oldalon nincs Firebase = nincs banner. A registration flow-ban a DH-132 checkbox egy külön Firebase-consent pipát is tartalmaz.

Előny: publikus oldalon nulla consent-eroded konverzió.
Hátrány: a pre-registration funnel (landing → product browse → registration) Firebase-ben nincs tracking-elve. A DH-80 UTM first-touch localStorage-ben működhet továbbra is (ez nem Firebase).

**Javaslat:** kezdjetek a hibrid megoldással. Banner csak akkor kerül elő, amikor a user regisztrálni készül, vagy akkor se, mert a regisztráció amúgy is consent-alkalom.

## 7. DH-137 frissített zárószöveg

```markdown
## Döntés
Cookie consent banner KÖTELEZŐ.

## Jogalap
- 506/2004 Art. 4 alin. (5): Firebase Analytics cookie-k, localStorage,
  IndexedDB, FID nem strict-necessary. EDPB Guidelines 2/2023 Section 3.
- 506/2004 Art. 4 alin. (5^1): express consent kötelező.
- GDPR Art. 6(1)(a) consent az egyetlen védhető jogalap.
- GDPR Art. 13 tájékoztatás: részletes Privacy Policy update.
- GDPR Art. 26 joint controller: Google Firebase joint controller
  agreement elfogadás a Console-ban.
- GDPR Art. 28 processor: Google Cloud Firebase DPA elfogadás.
- GDPR Art. 44-49 transzfer: EU-US Data Privacy Framework adekvátsági
  alap (Google LLC self-certified) + SCC backup.

## Implementációs követelmények (pre-launch, DH-138 Legal epic)
1. Firebase Console: DPA + DPF settings ellenőrzés
2. Firebase Console: Google Signals OFF, Google Ads OFF, IDFA OFF
3. Firebase Consent Mode v2 basic, default denied mind 4 signal
4. Banner: Accept/Reject egyenlő vizuális súly, bottom bar,
   Customize opció a részletekhez
5. Consent state: User DocType + httpOnly cookie + Capacitor Prefs
6. Firebase SDK init CONDITIONAL consent-re
7. Privacy Policy új szekciók: cookie lista, Firebase/Google, USA
   transzfer DPF, Art. 21 objection, 13 hónap retention
8. Cookie Policy oldal: minden cookie táblázatosan

## Capacitor mobil (v0.4)
9. iOS ATT NEM kell (IDFV, Signals off)
10. Apple App Privacy Labels kitöltés
11. Google Play Data Safety Form kitöltés
12. App első indulás: consent screen a Firebase init előtt

## Strict-necessary (consent NEM kell)
- sid auth session
- csrf_token
- cart_state
- lang_preference

## Consent-függő
- _ga és _ga_<CONTAINER_ID>
- firebase:host:<project> és firebase:authUser:<project> LS
- IndexedDB firebase-analytics-database
- Firebase Installation ID (FID)
- Capacitor native IDFV / AppSet ID

## Ügyvéd review
DH-133 után 500 EUR audit fee a teljes setupra + Privacy Policy
szövegre. 2-4 óra ügyvédi munka.

## Hibrid alternatíva
Firebase CSAK bejelentkezett userre → publikus oldalon nincs banner,
nincs konverzió-erózió. Regisztráció amúgy is consent-alkalom,
DH-132 checkbox-ba beépíthető.
```

## 8. KPI Dashboard hatás (DH-82)

A Firebase-váltás (DH-104) egy hibrid metrikamegoldást javasol:

- **Tranzakciós KPI-k** (Second Order Rate, TTFO, Order Failure Rate, Revenue, Fulfillment): **Frappe DB-ből 100 % lefedettséggel**. DH-82 dashboard ezt tartja.
- **Behavior KPI-k** (checkout_duration guardrail, Savings Engine events, product interaction): **Firebase Analytics 30-50 % lefedettséggel** az opt-in rate miatt.

**Javaslat:** A DH-82 dashboard-ot ne bontsátok le. Két külön riport szekció legyen: "Tranzakciós KPI (DB, 100%)" és "Behavior KPI (Firebase, opt-in sample)". Az opt-in arány önmagában is legyen KPI, hogy látszódjon a mintavétel minősége.

## 9. Források
- [Legea 506/2004 actualizată](https://legislatie.just.ro/Public/DetaliiDocument/57364)
- [Legea 190/2018](https://legislatie.just.ro/Public/DetaliiDocument/203151)
- [GDPR EU 2016/679 konszolidált szöveg](https://eur-lex.europa.eu/eli/reg/2016/679/oj)
- [Commission Implementing Decision (EU) 2023/1795 - DPF adequacy](https://eur-lex.europa.eu/eli/dec_impl/2023/1795/oj)
- [EU-US Data Privacy Framework list](https://www.dataprivacyframework.gov/list)
- [EDPB Guidelines 2/2023 on Art. 5(3) ePrivacy](https://www.edpb.europa.eu/our-work-tools/our-documents/guidelines/guidelines-22023-technical-scope-art-53-eprivacy-directive_en)
- [EDPB Guidelines 05/2020 on consent](https://www.edpb.europa.eu/our-work-tools/our-documents/guidelines/guidelines-052020-consent-under-regulation-2016679_en)
- [EDPB Guidelines 03/2022 on deceptive design patterns](https://www.edpb.europa.eu/our-work-tools/our-documents/guidelines/guidelines-032022-deceptive-design-patterns-social-media-platform_en)
- [Google Firebase Data Processing and Security Terms](https://firebase.google.com/terms/data-processing-terms)
- [Google Analytics 4 Terms of Service](https://marketingplatform.google.com/about/analytics/terms/us/)
- [Apple App Tracking Transparency](https://developer.apple.com/documentation/apptrackingtransparency)
- [Apple App Privacy Details](https://developer.apple.com/app-store/app-privacy-details/)
- [Google Play Data Safety Form](https://support.google.com/googleplay/android-developer/answer/10787469)
- [ANSPDCP (RO Data Protection Authority)](https://www.dataprotection.ro/)
- [CNIL Délibération 2020-091](https://www.cnil.fr/fr/cookies-et-autres-traceurs-la-cnil-publie-des-lignes-directrices-modificatives-et-sa-recommandation)
