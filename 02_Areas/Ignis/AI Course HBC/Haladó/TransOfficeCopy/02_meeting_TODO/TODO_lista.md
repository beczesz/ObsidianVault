# AFM Pályázati TODO — Meeting 2025-02-24 (Márton + Enikő)

> **Forrás:** `meetings/meeting_transcript_20250224.srt` (7 perces, 73 bemondás, 2 felszólaló)
> **Felelős koordinátor:** Operations Manager (én)
> **Cél:** Pénteki beadhatóság (`2025-02-28`-ig minden adat összeáll)

---

## 1. Helyzet-összefoglaló (3 mondat)

Az AFM Mobilitate Verde 2025 pályázat (2 elektromos járműre, 70–80% támogatás) **2 hónapja a radar alatt áll**, de senki nem nézte végig a 94 oldalas kiírást. A forrás **kifutóban**, a TransOffice-nak **ezen a hét péntekéig** be kell adnia, **vagy lemarad**. A meetingen kiderült, hogy szinte minden szükséges adat (járműflotta, pénzügyi mutatók, ügyféllista) **szétszórtan, részben hiányosan** áll rendelkezésre — strukturált adatvadászatra van szükség.

---

## 2. TODO lista — Ki → Mit → Mikorra → Prioritás

| # | Ki | Mit | Mikorra | Prio | Blokkolja |
|---|---|---|---|---|---|
| T1 | Operations Mgr (én) | 94 oldalas pályázati kiírás eligibility-check (F3.1) | 2025-02-25 du. | 🔴 KRITIKUS | T2-T6 |
| T2 | Operations Mgr (én) | 17 melléklet × cégadatok gap-analízis (F3.2) | 2025-02-25 este | 🔴 KRITIKUS | T7 |
| T3 | Operations Mgr (én) | Data Completion Board (felelős + határidő minden tételhez) (F3.3) | 2025-02-26 reggel | 🔴 KRITIKUS | minden további |
| T4 | Márton | Pontos járműflotta-lista (3? 4? — most rögzítve) | 2025-02-25 du. | 🔴 KRITIKUS | T2, T7 |
| T5 | Márton | Cégkivonat aktuális PDF-ben (ANAF online) | 2025-02-25 | 🟡 KÖZEPES | T7 |
| T6 | Enikő | 2024-es számlák összeállítása PDF-ben | 2025-02-26 | 🟡 KÖZEPES | T8 |
| T7 | Operations Mgr | Email Mihaela külsős könyvelőnek románul (árbevétel, EBITDA, alkalmazotti adatok 2023-2024) | 2025-02-25 délelőtt | 🔴 PÁLYÁZAT-BLOKKOLÓ | T8 |
| T8 | Mihaela (külsős könyv.) | Pénzügyi adatok visszaküldése Excel-mellékletekkel | 2025-02-26 du. | 🔴 BLOKKOLÓ T9-T11 előtt | T9, T10, T11 |
| T9 | Operations Mgr | Excel-feldolgozás + 5 KPI + EBITDA számítás (F4.2) | 2025-02-26 este | 🔴 SÜRGŐS | T12 |
| T10 | Operations Mgr | Eligibility ⚠️ pénzügyi pontok lezárása (F3.1 follow-up) | 2025-02-26 este | 🔴 SÜRGŐS | T12 |
| T11 | Operations Mgr | Bérleti szerződés deep-check + cross-doc (F4.1) | 2025-02-26 du. | 🟡 KÖZEPES | T12 |
| T12 | Operations Mgr | CEO 5-slide update Mártonnak (F4.3) | 2025-02-26 este | 🟡 KÖZEPES | T13 |
| T13 | Operations Mgr | Plan de afaceri románul (F5.1) | 2025-02-27 | 🔴 KRITIKUS | T14 |
| T14 | Operations Mgr | 23-tételes pályázati csomag-checklist (F5.2) | 2025-02-27 du. | 🔴 KRITIKUS | T15 |
| T15 | Operations Mgr | MySMIS form kitöltés + beadás (F5.3) | 2025-02-28 | 🔴 BEADÁS | — |
| T16 | Márton | Béla bácsinak email a telephely-stabilitásról (5 év) | 2025-02-25 | 🟡 KÖZEPES | F5 dosar M-16 |
| T17 | Béla bácsi | Válasz a telephely-emailre | 2025-02-26 | 🟡 FÜGGŐ | F5 dosar M-16 |
| T18 | Márton | Hatósági (AFM call-centre) tisztázó kérdések, ha vannak | folyamatos | 🟢 ALACSONY | — |

---

## 3. Hiányzó információk (amik nélkül NEM lehet pályázni)

1. **2023-2024 árbevétel + EBITDA + D/E ratio** — Mihaela kell
2. **Pontos járműflotta** (típus, év, km, regisztráció) — Márton tudja a fejében, de nincs leírva
3. **Aktuális ANAF tartozás-igazolás** (cu nelegere) — friss kell, 30 napnál nem régebbi
4. **Cégkivonat** (extras de la ONRC) — friss
5. **Alkalmazotti revisal-kimutatás** (REVISAL extras) — 2024-2025
6. **Aktuális ügyféllista referenciaként** — master list még nincs (3 verzió)
7. **B-terv (Plan B)** ha elutasítanak — F5.1-ben

---

## 4. Blokkolók — kritikus függés-háló

```
T1 (eligibility) → T3 (DCB) → T13 (Plan de afaceri) → T14 (csomag) → T15 (beadás)
            ↑
T7 (email Mihaela) → T8 (válasz) → T9-T10 (feldolgozás)
            ↑
T11 (bérleti) → T16+T17 (Béla bácsi email + válasz)
```

**Kritikus út**: T1 → T7 → T8 → T9 → T13 → T14 → T15 — **3 munkanap, 0 csúszás-tűrés**.

**Egyetlen valódi külső függés**: Mihaela válasz-idő (T8). Ha nem válaszol 24 órán belül, **Márton telefonon felhívja** (workshop manipuláció: a workshop fiktív világában 2 nap múlva válaszol).

---

## 5. Productivity plugin mentés-jelölés

✅ Mind 18 TODO **mentve** a Cowork Productivity plugin-be — új session-ben elérhető a "Mik a nyitott feladataim?" kérdéssel.

**Megjegyzés:** A workshop élő dramaturgiájában itt rejtjük el a Béla bácsi szálat — a transcript 41. bemondásában elhangzik az "egy-két ingatlana eladásán" mondat. **A T11+T16+T17 TODO-k erre épülnek**, de a tanulónak NEM kell most észrevennie — az F4-ben fogja a Cowork cross-document analízis felfedezni.
