---
topic: Founding 50 Program — DH-150
created: 2026-04-22
last_updated: 2026-04-22
status: active
id: 034c60c2-b64b-40b5-9b0a-83ac03acda7d
index_schema_version: 1
---

# Brainstorm: Founding 50 Program (DH-150)

## Sessions
| Date | AI(s) Used | Key Outcome |
|------|-----------|-------------|
| 2026-04-22 | ChatGPT (Deák GPT) | Koncepció véglegesítés + feature spec + UX flow + szövegek |

## AI Session Links
- ChatGPT: https://chatgpt.com/g/g-p-69cbee4a04c481918a2a738959b92361-deak/c/69da0a38-ce68-8391-bfb4-a2bbf24a66e7 (msg 74-95, 2026-04-22)

## Key Insights (ChatGPT + Szabolcs)

### Koncepció — "Founding 50"
- **NEM marketing kampány** — kontrollált user cohort kísérlet
- **50 fő limit** (nem 100 — reálisabb 30k-s kisvárosban)
- **3 hónap ingyenes szállítás** (nem 6 — rövidebb, intenzívebb)
- **Soft retention feltétel:** ha 30 napig nem rendel → státusz elvesztése (NEM kommunikált upfront)
- **Waitlist:** ha betelt → várólistára kerülhet, kiesőt pótolni lehet (MVP-ben manuális)

### UX/UI döntések (Szabolcs)
- **Kampány modal** a termékek oldalon (NEM azonnal — 2-3 sec delay vagy első scroll után)
- **Counter** kötelező: "37/50 hely betelve" vagy "Már csak 13 hely maradt" → scarcity
- **CTA:** "Csatlakozom most" + secondary: "Talán később"
- **Flow:** Kampány link (UTM) → termékek → modal → regisztráció (Google/Facebook/email) → vissza termékekhez → gratuláció modal
- **User badge:** "Alapító tag" — profilban + rendelési felületen

### Szövegek (ChatGPT draft)
**Kampány modal:**
- Cím: "Legyél az első 50 alapító tag között"
- Leírás: "Csatlakozz a Deák online rendelési programhoz Székelyudvarhelyen, és 3 hónapig ingyenes kiszállítást kapsz. Már csak kevés hely maradt."
- CTA: "Csatlakozom most"
- Secondary: "Talán később"

**Gratuláció modal:** (még nem kidolgozott — ChatGPT nem válaszolt az utolsó kérésre)

### Technikai minimum (ChatGPT spec)
- **Backend:** user flag (founding_member), expiry_date, order tracking
- **Frontend:** counter (query: count users), conditional UI, badge
- **Delivery logika:** `if founding_member AND current_date < expiry → delivery_fee = 0`
- **UTM tracking:** acquisition_source, acquisition_campaign, registration_date

### Tracking / KPI-k
- % user aki rendel 7 napon belül
- % user aki rendel másodszor
- orders/user/hónap
- retention (30 nap)
- AOV (average order value)

## Decisions Made
- 50 fő (nem 100) — Szabolcs döntése
- 3 hónap (nem 6) — Szabolcs döntése
- Havonta 2 rendelés feltétel (soft, backend-based) — Szabolcs döntése
- UTM + campaign source tracking — Szabolcs
- Modal delay (nem instant popup) — ChatGPT javaslat, Szabolcs elfogadta
- NEM teljes kampányrendszer — minimális impl. elég Phase 1-re

## Open Questions
- [ ] Gratuláció modal szöveg — kidolgozandó
- [ ] Román nyelvű verziók — szükségesek? (Székelyudvarhelyen többségében magyar)
- [ ] Pontos kampány indulás dátum — v0.3 beta után (~2026-05-15)?
- [ ] Toborzási csatorna: bolt + QR + személyes? Facebook is?
- [ ] Budget cap: mennyit ér az ingyenes szállítás 50 fő × 3 hónap × ~2 rendelés/hó?
- [ ] Jira sub-taskokra bontás — mikor?

## Context References
- TASKS.md → DH-150 ticket
- CLAUDE.md → DH projekt kontextus
- Business Development/pilot-husuzlet/BMC-v2.2.md → business model
- Business Development/pilot-husuzlet/dev-roadmap-v2.0.md → roadmap

## Raw Notes
Szabolcs eredeti ötlete (msg 74): Tesztelési hullámok, early adopterek toborzása kedvezményekkel. Cél: forgalom generálás + közvetlen feedback + retention. Többféle hullámban gondolkodik (alpha, beta, mobil app teszterek).

ChatGPT finomítások: 50 fő (nem 100), 3 hónap (nem 6), "Founding 50" branding, soft retention filter (30 nap inaktivitás = kiesés, de nem kommunikált), scarcity counter kötelező, badge rendszer.

Szabolcs UX pontosítás (msg 86, 92): UTM source tracking, kampány modal a termékek oldalon, regisztráció = csatlakozás, gratuláció visszavezetés termékekhez.
