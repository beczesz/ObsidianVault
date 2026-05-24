---
title: "Deák Húsmíves — Founding 50 Launch Kampány"
version: v1.0
date: 2026-04-22
author: Szabolcs + Claude
status: TERVEZÉS
target_launch: ~2026-05-15 (v0.3 beta release után)
id: 53bdc1ed-f021-4f42-9599-287bc8630bac
index_schema_version: 1
---

# Founding 50 Launch Kampány — Kampányterv

## 1. Kampány összefoglaló

A Deák Húsmíves elindítja az online rendelési rendszerét Székelyudvarhelyen. A kampány fókusza a **Founding 50 program**: az első 50 regisztrált felhasználó 3 hónapig ingyenes kiszállítást kap. Ez nem klasszikus marketing — hanem egy kontrollált user cohort kísérlet, exkluzív hangulattal.

**Egy mondat:** „Legyél az első 50 alapító tag — 3 hónapig ingyenes kiszállítás."

---

## 2. Célkitűzés (SMART)

| Mutató | Cél | Időkeret |
|--------|-----|----------|
| Regisztráció | 50 fő (Founding 50 betöltése) | 2-4 hét |
| Első rendelés (TTFO) | ≤72 óra a regisztrációtól | Folyamatos |
| Second Order Rate | ≥40% (14 napon belül) | 3 hónap |
| Szórólap kiosztás | 200-300 db | Első 2 hét |
| FB elérés | 3.000-5.000 (organikus + boost) | Első hét |

**Siker definíció:** 50/50 hely betelt 4 héten belül + ≥20 visszatérő vásárló.

---

## 3. Célközönség

**Elsődleges:** Digitálisan nyitott, időszűkében lévő székelyudvarhelyi vásárlók, 25-45 év.

**Profil:** Családos ember (jellemzően nő, de nem kizárólag) aki hetente vásárol húst a Deák boltjában vagy konkurenciánál. Szeretné, ha nem kellene sorban állnia. Érdekli a minőség és a kényelem. Okostelefonja van, használja a Facebookot.

**Másodlagos:** A Deák Húsmíves meglévő törzsvásárlói, akik az üzletben találkoznak a szórólappal/plakáttal.

---

## 4. Üzenet hierarchia

### Fő üzenet
> **„Legyél az első 50 alapító tag között"**

### Támogató üzenetek (prioritás sorrendben)
1. **Exkluzivitás:** „Csak 50 hely — ha betelt, betelt."
2. **Jutalom:** „3 hónapig ingyenes kiszállítás minden rendelésedre."
3. **Egyszerűség:** „Rendelj online, mi visszük haza. Frissen, aznap."
4. **Bizalom:** „Ugyanaz a Deák minőség, amit ismersz — most házhoz."

### CTA
- **Elsődleges:** „Csatlakozom most" / „Regisztrálok"
- **Másodlagos:** „Megnézem a termékeket" → deakhus.ro

### Amit NEM kommunikálunk
- Nem említjük a „havonta min. 2 rendelés" soft feltételt
- Nem használunk „SIESS!" / „HIHETETLEN AKCIÓ!" stílusú nyelvezetet
- Nem pozícionáljuk a bolt ellen — az online kiegészíti, nem helyettesíti

---

## 5. Csatornák és eszközök

| Csatorna | Eszköz | Cél | Prioritás |
|----------|--------|-----|-----------|
| **Bolt (in-store)** | Szórólap + plakát + QR | Meglévő vásárlók konverziója | #1 |
| **Facebook** | Poszt + Story + boost | Elérés, awareness | #2 |
| **Személyes ajánlás** | Szóbeli + szórólap átadás | Bizalom, word-of-mouth | #3 |
| **deakhus.ro** | Landing + Founding 50 modal | Konverzió | Automatikus |

### Csatorna-specifikus UTM paraméterek

| Forrás | UTM |
|--------|-----|
| Szórólap QR | `?utm_source=qr_flyer&utm_medium=offline&utm_campaign=founding50` |
| Bolt plakát QR | `?utm_source=qr_poster&utm_medium=offline&utm_campaign=founding50` |
| Facebook poszt | `?utm_source=facebook&utm_medium=social&utm_campaign=founding50` |
| Facebook Story | `?utm_source=facebook_story&utm_medium=social&utm_campaign=founding50` |
| Bolt pult QR | `?utm_source=qr_counter&utm_medium=offline&utm_campaign=founding50` |

---

## 6. Időterv

| Hét | Tevékenység |
|-----|-------------|
| **H-1 (most)** | Kampányterv véglegesítés, design briefek, vizuális anyagok tervezése |
| **H0 (v0.3 release ~máj. 15)** | Szórólap nyomtatás, plakát kihelyezés, FB poszt publikálás |
| **H1** | Szórólapok kiosztása a 3 boltban, FB Story sorozat, organikus + kis boost |
| **H2** | Elérés értékelés, szükség esetén boost növelés, counter frissítés a posztban |
| **H3-4** | Utolsó helyek kommunikálása (scarcity fokozás), waitlist bevezetése ha közel 50 |

---

## 7. Budget

| Tétel | Összeg | Megjegyzés |
|-------|--------|------------|
| Szórólap nyomtatás (300 db A5) | ~150-200 RON | Helyi nyomda, duplex |
| Bolt plakát (3 db A3) | ~50 RON | A 3 boltba |
| Facebook boost | 200-500 RON | 1-2 hét, célzott Székelyudvarhely |
| Ingyenes szállítás költsége | max ~4.500 RON (~900 EUR) | 50 fő × 3 hó × 2 rendelés/hó × 15 RON |
| **Összesen** | **~5.000 RON (~1.000 EUR)** | A stop cap (12-13k EUR) alatt |

---

## 8. Mérés (KPI-k)

| KPI | Forrás | Cél |
|-----|--------|-----|
| Founding 50 regisztrációk | Firebase: founding50_registered | 50 |
| QR → Visit konverzió | Firebase: UTM tracking | 30-50% |
| TTFO (Time to First Order) | Firebase: first_order event | ≤72h |
| Second Order Rate (14d) | Firebase: North Star KPI | ≥40% |
| Modal → CTA konverzió | Firebase: founding50_modal_shown → cta_clicked | tracking |

---

## 9. Deliverables lista

| # | Deliverable | Formátum | Brief fájl |
|---|------------|----------|------------|
| 1 | Facebook poszt kép | 1080×1080px (square) | 02_brief_fb_poszt.md |
| 2 | Facebook/Instagram Story | 1080×1920px (9:16) | 03_brief_story.md |
| 3 | Szórólap (A5 duplex) | 148×210mm | 04_brief_szorolap.md |
| 4 | Bolt plakát (A3) | 297×420mm | 05_brief_plakat.md |
| 5 | Landing page hero banner | 1440×600px + 375×500px | 06_brief_hero_banner.md |

---

## 10. Brand voice emlékeztető

**Hangnem:** Őszinte, helyi, egyszerű, megbízható.
**Így hangzik:** „Hajnalban készül. Kézműves minőség. Most házhoz is."
**Így NEM hangzik:** „HIHETETLEN AKCIÓ! RENDELD MOST! SIESS!"
**Színvilág:** Piros (#C0392B / #E74C3C), fehér (#FFFFFF), sötétszürke (#2C2C2C)
**Logó:** Deák Húsmíves logó — SVG és PNG elérhető
