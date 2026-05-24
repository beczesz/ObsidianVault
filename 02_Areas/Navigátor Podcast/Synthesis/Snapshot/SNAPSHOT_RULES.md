---
version: 1.0
date: 2026-04-09
type: snapshot-rules
description: "Periodikus csatorna- és videószintű KPI snapshotok szabályrendszere a Navigátor Podcast optimalizációs hatásainak mérésére."
id: 20078d87-44dc-4f8e-a7ca-3e49472a6027
index_schema_version: 1
---

# Snapshot Rules — Navigátor Podcast

## Cél

A Snapshot rendszer célja, hogy **mérhető adatokkal igazoljuk** a Fázis 4a/4b/4c optimalizációs változtatások (cím, leírás, end screen, cards, SEO) hatását a csatorna teljesítményére. Minden snapshot egy időpillanat-felvétel a YouTube Studio Analytics-ból.

**Kontextus:** A cím + leírás re-optimalizálás 2026-04-08 és 2026-04-09 között készült el mind a 15 kiemelt videóra. Az első snapshot (2026-04-09) a "post-optimization baseline" — ehhez hasonlítjuk az összes későbbi mérést.

---

## Frekvencia

- **Heti** — Szabolcs manuálisan triggereli ("csináld meg a heti snapshot-ot")
- **Minimum:** heti 1×, ideálisan ugyanazon a napon (pl. szerdán)
- **Első 4 hét:** heti snapshot kötelező (a leggyorsabb változások itt látszanak)
- **Utána:** kéthetente is elég, hacsak nem történik újabb nagyobb változtatás

---

## Fájl formátum

Minden snapshot egy külön fájl:
```
Synthesis/Snapshot/SNAPSHOT_YYYY-MM-DD.md
```

Példa: `SNAPSHOT_2026-04-09.md`, `SNAPSHOT_2026-04-16.md`, stb.

---

## Mért KPI-ok

### A) Csatorna-szintű (28 napos ablak)

| KPI | Mértékegység | Honnan |
|-----|-------------|--------|
| Views (28d) | szám | YT Studio → Analytics → Overview |
| Watch time hours (28d) | óra | YT Studio → Analytics → Overview |
| Subscribers net (28d) | szám (+/-) | YT Studio → Analytics → Overview |
| Avg view duration (28d) | MM:SS | YT Studio → Analytics → Overview |
| Impressions (28d) | szám | YT Studio → Analytics → Reach |
| Impressions CTR (28d) | % | YT Studio → Analytics → Reach |

### B) Traffic Sources (28d, %)

| Forrás | Honnan |
|--------|--------|
| Browse features | YT Studio → Analytics → Reach → Traffic source |
| Suggested videos | YT Studio → Analytics → Reach → Traffic source |
| YouTube search | YT Studio → Analytics → Reach → Traffic source |
| External | YT Studio → Analytics → Reach → Traffic source |
| Direct or unknown | YT Studio → Analytics → Reach → Traffic source |

### C) TOP 15 Optimalizált Videók (egyéni)

Ezek azok a videók, amelyeknek a címét és leírását 2026-04-08/09-én frissítettük:

| # | EP | YouTube ID | Vendég/Téma |
|---|-----|-----------|-------------|
| 1 | EP14 | FUJxOv6kXtk | Bencze Edit (nárcizmus) |
| 2 | EP29 | j0tFeNxMR7g | Dr. Lőrinczi Kincső (vércukor) |
| 3 | EP17 | el5X3cywTdk | ChatGPT eredményesség |
| 4 | EP36 | (ID) | Both Richárd (fáradtság) |
| 5 | EP28 | (ID) | Bencze Edit (nárcizmus 2) |
| 6 | EP30 | NKkRDMfKGmw | Dr. Csala Dénes (AI+iskola) |
| 7 | EP37 | (ID) | Reziliencia 21 (kiégés) |
| 8 | EP34 | (ID) | Süket Csaba (startup bukás) |
| 9 | EP06 | EMdzmI4tUVw | Bencze Edit (identitáskrízis) |
| 10 | EP19 | DeGjg1EM7Qw | Becze Juliánna és Szabolcs (házasság) |
| 11 | EP26 | yhUxLJO5OWY | Balázs Anna & Zoltáni Kinga (rák) |
| 12 | EP38 | o4xWWp5qZDM | Gál Ildikó (örökbefogadás) |
| 13 | EP24 | X3Rhtpal5tA | Faragó Zénó & Fodor Alain Leonard (függőség) |
| 14 | EP31 | h2i9WNsdWrc | Simon Károly & Kolumbán S. (AI 80%) |
| 15 | EP35 | X1EF52Eez4o | Lang Máté (IT versenyképesség) |

**Videószintű KPI-ok (mindegyik videóra):**

| KPI | Mértékegység | Honnan |
|-----|-------------|--------|
| Views (since published) | szám | YT Studio → videó → Analytics |
| Impressions (since published) | szám | YT Studio → videó → Analytics → Reach |
| CTR | % | YT Studio → videó → Analytics → Reach |
| Avg view duration | MM:SS | YT Studio → videó → Analytics → Engagement |
| Watch time hours | óra | YT Studio → videó → Analytics → Engagement |

> **Megjegyzés:** A videószintű adatok "since published" módban relevánsak, mert a view-szám kumulatív. A változás = jelenlegi snapshot − előző snapshot.

### D) End Screen metrikák (csatorna-szintű)

| KPI | Honnan |
|-----|--------|
| End screen element shown | YT Studio → Analytics → Engagement → End screen |
| End screen element click rate | YT Studio → Analytics → Engagement → End screen |

---

## Összehasonlítás módja

### Baseline vs Current

```
Δ = (current - baseline) / baseline × 100%
```

- **Zöld (pozitív):** CTR↑, Views↑, Avg view duration↑, Suggested%↑, Watch time↑
- **Piros (negatív):** CTR↓, Views stagnálás, Suggested%↓

### Heti változás

```
Δ_heti = (current - previous_week) / previous_week × 100%
```

### Értelmezés irányelvek

- **CTR változás:** ±0.5pp már szignifikáns kis mintán
- **View szám:** 7 napos ablakban nézd, ne napiban (túl zajos)
- **Suggested %:** Az algoritmus reakcióideje 1-3 hét — ne várj azonnali ugrást
- **Search %:** SEO hatás 2-6 hét múlva látszik (YouTube index frissítés)

---

## Snapshot készítés workflow (Chrome MCP)

1. Navigálj a YouTube Studio Analytics oldalra
2. Állítsd be a dátumot "Last 28 days"-re
3. Olvasd le az Overview tab KPI-okat (Views, Watch time, Subscribers, Avg view duration)
4. Váltsd a Reach tab-ra → Impressions, CTR, Traffic sources %
5. Váltsd az Engagement tab-ra → End screen metrics
6. A 15 optimalizált videó adataihoz: Content tab → videólista → egyenként megnézni
7. Töltsd ki a SNAPSHOT_YYYY-MM-DD.md sablon-t

> **Tipp:** A TOP 15 videó adatait a Content tab-ról gyorsan le lehet olvasni (views, CTR látható a listában). Az egyéni videóoldalra csak akkor kell menni, ha részletes retention adatot is akarunk.

---

## Sablon

Lásd: az első snapshot (`SNAPSHOT_2026-04-09.md`) a sablon referencia. Minden későbbi snapshot ugyanezt a struktúrát követi.
