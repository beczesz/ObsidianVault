---
title: "Microsite Factory — Üzleti terv és piackutatás"
date: 2026-05-16
author: Becze Szabolcs
status: active
description: "Magyar AI-asszisztált microsite gyár kisvállalkozásoknak, mely 30 perc alatt stratégiailag átgondolt, egyedi weboldalt készít."
description_source: auto
description_hash: 33ae601b584fb0d7
id: c0e88f89-f090-4aae-9cba-594ef8419e6d
index_schema_version: 1
bdos_index: true
---
# Microsite Factory — Üzleti terv és piackutatás

**Készült:** 2026-05-15
**Státusz:** Döntésre vár

---

## Mi ez a termék?

Egy AI-asszisztált microsite gyár, ami marketing landing page-eket gyárt kisvállalkozásoknak. Egy üzleti briefből 20-30 perc alatt stratégiailag átgondolt, egyedi designú, kész weboldalt készít — nem template-et, nem drag-and-drop-ot, hanem valódi, az ügyfélre szabott oldalt.

**Amit már megépítettünk:**
- 6 lépéses AI workflow (brief → BMC → pozícionálás → design system → build → polish)
- Cloudflare Workers deploy pipeline (staging + production)
- Scaffold template rendszer, automatizált deploy scriptek
- 2 kész referencia-oldal: Sonrisa Dental (élesben), Kingdom at Work (staging)

**Fejlesztési idő:** 1.5 nap

---

## Piackutatás

### Piac mérete

| Mutató | Érték |
|---|---|
| AI website builder piac (2025) | $2.7–3.8 milliárd USD |
| Várható méret (2030) | $8.6–17.4 milliárd USD |
| Éves növekedés (CAGR) | 19–26% |
| Kisvállalkozások weboldal nélkül (USA) | 27% — fő ok: túl drága |

### Fő versenytársak

| Név | Ár/hó | Erősség | Gyengeség |
|---|---|---|---|
| Durable | $15–95 | 30 mp generálás, beépített CRM | Lock-in, nem exportálható kód |
| Mixo | $9–39 | Leggyorsabb MVP | Nincs blog, korlátozott SEO |
| Wix ADI | $17–159 | Legnagyobb feature set | Bloated kód, vendor lock-in |
| B12 | $0–399 | AI + emberi hibrid | Drága |
| Hostinger | $2.69–10 | Legolcsóbb belépő | Ár megtriplázódik megújításkor |
| Framer | $0–100 | Design-fókuszú | Fejlesztőknek való |
| Hocoos | — | — | **Bezárt (2026. április)** |

### Azonosított piaci rések

1. **Lock-in probléma** — A versenytársak 68%-a NEM engedi a kód exportálását. Az ügyfél örökre fogoly.
2. **A $5–15/hó sáv üres** — A free tier-ek csonkák és szégyenletesek ("Made with Wix"), a használható csomagok $15+/hó-tól indulnak.
3. **Subdomain minőség** — A free subdomain-ek mindenhol csúnyák (`xyz.wixsite.com/valami`). Tiszta, professzionális subdomain nem létezik a piacon free/low-cost szinten.
4. **Teljesítmény** — A legtöbb builder bloated kódot generál. Edge deploy ritka.
5. **Piaci konszolidáció** — Versenytársak zárnak be (Hocoos), felhasználók felszabadulnak.

---

## Miért vagyunk jó pozícióban?

### Technológiai előnyök

| Mi | Versenytársak |
|---|---|
| Vanilla HTML/CSS/JS — ügyfél elviszi bárhová | Proprietary, platform-locked kód |
| Cloudflare Workers edge (300+ PoP, <50ms TTFB) | Centralizált hosting, lassabb |
| Tiszta god-domain subdomain (cegnev.midomainunk.com) | Csúnya subdomain + "Made with X" badge |
| 6 lépéses stratégiai workflow (BMC → design → build) | Template + AI kitöltés, nincs stratégia mögötte |

### Költségstruktúra — ez a legnagyobb előnyünk

| Tétel | Költség |
|---|---|
| God domain | ~€10/év |
| AI plan | ~€200/hónap (amúgy is megvan) |
| Hosting bármennyi site-ra | **€0** (Cloudflare free tier, napi 100k requestig) |
| **Összes marginális költség** | **~€10/év** |

**Gross margin: ~99%.** Minden beérkező euró szinte tiszta profit. Nincs szerverköltség, nincs skálázási probléma.

---

## Javasolt stratégia

### Alapelv: "Nail it before you scale it"

NE építsünk self-service platformot. NE menjünk globálisra. NE fejlesszünk tovább, amíg nincs fizető ügyfél.

### Célpiac az induláshoz

**Magyar fogászatok** — mert:
- Van kész referencia-oldalunk (Sonrisa Dental)
- Magas fizetési hajlandóság (prémium szolgáltatás)
- Kevesebb ügyfél kell a bevételi célhoz
- Könnyű megtalálni őket (Google Maps, kamarai listák)
- Lokálisan NINCS versenytársunk

### Árazás

| Csomag | Ár | Tartalom |
|---|---|---|
| **Elkészítjük** | €300–500 egyszeri + €25/hó | Teljes workflow, egyedi oldal, hosting, karbantartás |
| **Csak hosting** | €9/hó | Ha már kész az oldal, fenntartás |

**Az első 5 ügyfélnek:** egyszeri díj ingyen, csak a havi díjat kérjük — a referenciák többet érnek, mint €2,500.

### A sales taktika: "Unsolicited Demo"

1. **Listát építünk** 50 budapesti fogászatról, akiknek nincs rendes weboldala (Google Maps-ből, 2 óra munka)
2. **Készítünk 5 demo oldalt kéretlenül** — a mi tool-unknal ez fogászatonként 30 perc
3. **Megkeressük őket** egy személyes emailben: "Láttam, hogy nincs modern weboldalatok. Készítettem egy demót — nézd meg. Ha tetszik, beszéljünk."
4. **Nem kérünk semmit, ADUNK valamit** — ez megfordítja a sales dinamikát

### Időterv

| Időszak | Teendő | Cél |
|---|---|---|
| **1. hét** | Saját landing page + lista 50 fogászat + 5 demo oldal | Indulásra kész |
| **2–4. hét** | Megkeresések, follow-up, első ügyfelek | 2–3 fizető ügyfél |
| **2. hónap** | Következő 10 megkeresés + ajánláskérés | 5–8 fizető ügyfél |
| **3. hónap** | 10+ ügyfél, szájról-szájra ajánlások beindulnak | Validált modell |
| **6. hónap** | Niche kiterjesztés (szépségipar, ügyvédek, könyvelők) | 30–40 ügyfél |
| **12. hónap** | Régiós terjeszkedés (SK, CZ, RO) | 60–80 ügyfél |
| **24. hónap** | Globális, self-service platform (opcionális) | 120+ ügyfél |

---

## Pénzügyi terv: út a havi €5,000-hoz (24 hónap)

### Bevételi modell 120 ügyfélnél

| Típus | Szám | Összeg |
|---|---|---|
| Egyszeri elkészítés | 3 új/hó × €400 | €1,200/hó |
| Recurring hosting | 80 ügyfél × €25/hó | €2,000/hó |
| Recurring + karbantartás | 40 ügyfél × €45/hó | €1,800/hó |
| **Összesen** | | **€5,000/hó** |

### Ehhez szükséges: havi ~5 új ügyfél

- Budapest: ~2,000 fogászati rendelő
- Becslés: 600–800-nak nincs rendes weboldala
- 120 ügyfél = a potenciális piac ~15–20%-a
- Több niche-sel (szépségipar, ügyvédek stb.) a piac megsokszorozódik

### Költség

| Tétel | Havi |
|---|---|
| Domain | ~€1 |
| AI plan (arányrész) | ~€17 |
| Sales munka (saját időnk) | €0 (nincs extra cost) |
| **Összes költség** | **~€18/hó** |

---

## Mi szúrhatja el — top 3 kockázat

### 1. Nem kezdjük el az értékesítést

A legvalószínűbb kudarc-ok. Tovább fejlesztjük a tool-t, szebb UI-t csinálunk, újabb feature-öket adunk hozzá — és közben egyetlen fogászt sem hívunk fel. **A fejlesztés biztonságos, az értékesítés félelmetes.** De a fejlesztés nem hoz pénzt.

**Ellenszer:** Az első hét feladata: 5 demo + 5 megkeresés. Semmi más.

### 2. Túl korán váltunk globálisra vagy platformot építünk

Mielőtt a lokális modell bizonyított, elkezdjük a self-service platform fejlesztését vagy angol nyelvű globális terjeszkedést. Széthúzódik az energia, egyik sem működik.

**Ellenszer:** Platform fejlesztés TILOS, amíg nincs 50 fizető ügyfél.

### 3. Nem kérünk elég pénzt

Magyar reflex: "de hát ez csak egy kis weboldal..." Egy fogász egy fogfehérítésért €200–500-at kér. Egy weboldal, ami HOZZA a pácienseket, megéri nekik €400 + €25/hó-t.

**Ellenszer:** Az ár fix. Nem alkudozunk. Ha nem éri meg valakinek, az nem a mi ügyfelünk.

---

## Következő lépés

**Döntés szükséges:** elindítjuk-e a sales-t a leírt terv szerint?

Ha igen, a konkrét első feladatok:
1. Landing page készítése saját magunknak (1 nap)
2. 50 fogászat listája Google Maps-ből (2 óra)
3. 5 demo oldal elkészítése (3 óra)
4. 5 megkeresés kiküldése (1 óra)

**Teljes indulási idő: ~2 nap. Költség: €0.**
