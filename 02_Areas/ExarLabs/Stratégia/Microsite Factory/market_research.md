---
title: Piackutatás — Microsite Factory
source: Perplexity (Researcher role)
url: https://www.perplexity.ai/search/0d9fb6f7-26ba-43c9-9ad5-cfd8242fba05
imported: 2026-05-16
status: v1 — első kör
id: 3f4b08d9-a80c-4367-b2cd-79cbb5059194
index_schema_version: 1
---

# Piackutatás — Microsite Factory

> Perplexity-vel végzett első kutatási kör. 30 forrást használt. A részletes kérdés-listára adott válasz tematikusan, nem pontról-pontra — alább a kiemelt insightok és a saját értelmezés.

---

## 🇭🇺 Magyar piaci kontextus

### AI adopció — fontos benchmark
- **Magyar vállalati AI adopció: 3,7%** (2024-es EU Digital Decade országjelentés) — szemben a **8%-os EU átlaggal**.
- Cloud használat: **37,1%**, data analytics: **53,2%** — a digitalizációs nyitottság létezik, csak az AI réteg még gyenge.
- Deloitte 2025 felmérés (100+ magyar szervezet): a "résztvevők 80%+ használ valamilyen AI-megoldást" — de ez az érettebb cégek köre.
- **Következtetés:** a piac kettészakadt. Az érettebbek mozdulnak, a többieknek a "mi mindent elkészítünk helyetted" ajánlat híd lehet. → **Done-for-you framing megerősítve.**

---

## 🦷 Miért fogászat — megerősítés

### A vertikum erőssége
- Magyar fogászati piac: erős verseny, sok privát szereplő, magas betegbizalom-igény.
- Webes jelenlét közvetlen konverziós eszköz (nem névjegy) — ajánlások, kezelések bemutatása, könnyű kapcsolatfelvétel.
- Nemzetközi platformok (Bookimed, Dental Departures, Booking.dentist) **benchmarkként** szolgálnak: ár, kezelési oldalak, review-k, gyors egyeztetés, konzultáció elvárása.

### 🌍 Dental tourism extra opportunity
**Budapest kifejezetten erős a dental tourism-ban.**
- Több magyar szereplő külföldi páciensekre optimalizál: utazásszervezés, konzultáció, treatment page-ek, lead capture.
- **Strategic implikáció:** 2 csomag induljon a fogászati vertikumon belül:
  1. **Local patient acquisition** (magyar páciensek)
  2. **Dental tourism lead** (külföldi páciensek, többnyelvű, utazási kontextus, "treatment journey" landing)

### Validációs lépések (Perplexity javasolja)
- **20 fogászat manuális auditja:** modern mobil, egyértelmű CTA, ár/kezelés oldal, többnyelvűség, review, foglalás.
- **8-10 praxisvezetői interjú:** mi a fő fájdalompont — új beteg, visszahívás, konzultáció vagy időpontfoglalás?
- **Landing teszt 2 ajánlattal:** "microsite 10 nap alatt" vs. "új páciensekre optimalizált fogászati weboldal".

---

## 🥊 Verseny és pozícionálás

### A versenytárs-halmaz típusai
1. **Általános webügynökségek** (drága, lassú)
2. **Vertical website szereplők** (specializált, de kevés HU-ban)
3. **Booking platformok** (Bookimed, Dental Departures — leadforrás + benchmark)
4. **Marketplace közvetítők**

### A nyerő pozícionálás
> ❌ NEM: "AI weboldalt készítünk"
> ✅ IGEN: **"2 hét alatt kész, fogászatra optimalizált, többnyelvű, konverzióra épített microsite, amit később online időpontfoglalással bővíthetsz."**

**Kulcs:** az AI a háttérben értékes, de a vevőnek a **kimenet** számít — gyors indulás, jobb szöveg, több lead, strukturált szolgáltatásoldalak.

### GTM üzenet (Perplexity-javaslat)
> "Nem weboldalt adunk, hanem kész fogászati online jelenlétet, amit később foglalással és lead automatizálással bővíthetsz."

---

## 💶 Árazás — realitás-check

### A €25-45/hó + €300-500 egyszeri ár értékelése
- **Pszichológiailag belépőszint, magyar KKV-nak vállalható** — különösen ha "microsite + hosting + maintenance + AI tartalomfrissítés" csomagként van pozícionálva.
- **Önmagában túl alacsony** lenne klasszikus egyedi fejlesztésre.
- **Működik:** ha sablonosított vertikális gyártás + add-on monetizáció.

### Standardizáció követelmények (Perplexity szerint)
- 5-8 iparági template
- Kötött oldalszerkezet
- Strukturált intake
- AI-asszisztált copy
- Opcionális fotó-/review-import
- Külön fizetős add-onok

### Add-on portfólió javaslat
- Booking
- Többnyelvűség
- SEO landingek
- FAQ generálás
- Review widget
- Call tracking
- GDPR/cookie setup
- Kampány landingek

---

## 📅 Vertikum sorrend — Perplexity ajánlása

1. **Fogászat** (első) — magas ügyfél-revenue, erős verseny, web→lead direkt
2. **Szépségipar** (második) — booking centrális, web+booking csomagok már piacon
3. **Könyvelők** (harmadik) — lassabb értékesítés
4. **Ügyvédek** (negyedik) — corporate brochure szemlélet, lassú

> **Megjegyzés (Claude):** Eredeti BUSINESS_PLAN.md sorrendje: fogászat → szépségipar → ügyvédek → könyvelők. Perplexity szerint a könyvelőket az ügyvédek elé kell vinni (univerzálisabb pain point, vállalkozó-fókusz). **[?] Validálandó.**

---

## 🛠️ Tech / addon piaci tájékozódás

### Booking embed lehetőségek (saját kutatás további körben szükséges)
A Perplexity csak részben válaszolt — az alábbi szereplőket említi mint releváns játékos:
- **Cal.com** — open-source, ingyenes alap, embed-elhető
- **Calendly** — szabványos
- **Fresha** — szépségiparra optimalizált
- **SimplyBook** — booking-fókuszú
- **Google Calendar Appointment Scheduling** — ingyenes Workspace alatt

> **TODO:** Részletes embed-feltételek és pricing táblázat — következő research körben.

### Cloudflare limit (TODO — Perplexity nem válaszolt erre konkrétan)
> Önállóan validálandó: Cloudflare Pages free tier (100k requests/day) + custom domain limit + projekt darabszám.

---

## 🎯 Kulcs következtetések — hatás a BMC-re

### Megerősítések
✅ **Fogászat mint első vertikum** — Perplexity is ezt javasolja, dental tourism extra layerrel.
✅ **Árazás reális** — magyar KKV-knak belépőszint, működik IF standardizáció.
✅ **Done-for-you framing** — a magyar AI-adopciós gap (3,7%) miatt működő híd.
✅ **GTM üzenet:** "fogászati online jelenlét" > "AI weboldal".

### Új insightok beépítendők
🆕 **Dental tourism mint duplán prémium szegmens** — Budapest specifikus, magasabb ASP, többnyelvű igény.
🆕 **Vertical sorrend:** könyvelők előbb mint ügyvédek (Perplexity javaslat).
🆕 **Standardizáció + add-on monetizáció** = az árazás működőképességének kulcsa.
🆕 **Validációs lépések** — Perplexity konkrét javaslata: 20 audit + 8-10 interjú + landing A/B teszt.

### Még nyitott — második Perplexity körre
- [ ] Cold outreach response rate benchmark (lokális SMB HU/EU)
- [ ] CAC benchmark SMB B2B EU 2025
- [ ] Cloudflare Pages 2026 limit
- [ ] Magyar fogászatok jellemző builder-szegmentációja (Wix vs. Webnode vs. ügynökségi custom)
- [ ] Booking-platformok teljes ár- és integráció-mátrixa
- [ ] Magyar lokális AI website builder verseny (van-e ilyen)

---

## Források (Perplexity hivatkozott)
- EU Digital Decade országjelentés 2024
- Deloitte AI Magyarország 2025
- Bookimed, Dental Departures, Booking.dentist (versenytárs-benchmark)
- Dental-tourism-hungary, Flatio (HU dental tourism kontextus)
- Egyéb (smartlegal, ecovis-law, zunapro) — kapcsolódó vertikum-források
