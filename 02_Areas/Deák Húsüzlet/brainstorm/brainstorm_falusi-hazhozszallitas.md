---
topic: Falusi házhozszállítási modell — a DH pilot kiterjesztése vidékre
created: 2026-05-01
last_updated: 2026-05-01
status: SYNTHESIZED — 3 AI input összegezve, döntésre vár
id: a3450a6e-8581-4daf-84b1-0ab792ab6405
index_schema_version: 1
---

# Brainstorm: Falusi házhozszállítási modell

## Kiindulópont

Telefonos beszélgetés egy vidéki érdeklődővel (2026-04-30). Kulcs-insightok:
- Falvakban **NINCS friss hús** — ez nem kényelmi, hanem **elérhetőségi** probléma
- A házhozszállítás értéke rendkívül magas (nem kell bemenni a városba)
- **Ingyenes szállítás >> 2% kedvezmény** (a szállítási díj a döntő tényező)
- Javaslat: plakátok a falvakban + fix kiszállítási napok régiónként
- Geolokáció-alapú mobil rendelés (település-választó elég a pilothoz)

## Team

| Szerep | AI | Feladat |
|--------|-----|---------|
| **Director** | ChatGPT (Deák GPT) | Stratégiai iránymutatás, feladatkiosztás, kockázat-jelzés |
| **Researcher** | Perplexity | Piackutatás, európai példák, demográfia, árazási benchmarkok |
| **Analyst** | Gemini | Numerikus modellezés, route economics, breakeven, döntési mátrix |

## Sessions

| Dátum | AI(s) | Key Outcome |
|-------|-------|-------------|
| 2026-05-01 | ChatGPT (Director) | **Stratégiai keret:** fix-route pre-order modell; rendelés-sűrűség = a modell kulcsa; falu nem város (elérhetőség vs. kényelem); geolokáció túlzás pilothoz, település-választó elég |
| 2026-05-01 | Perplexity (Researcher) | **Piackutatás (45 forrás):** Picnic (NL) benchmark; Hargita megye 53 település; RO vidéki internet 88%; húsfogyasztás ~3,88 kg/hó/fő; EU free-delivery medián 50 EUR; fix-route demand koncentráció a siker kulcsa |
| 2026-05-01 | Gemini (Analyst) | **Numerikus modell:** fix-route optimális; 15 rendelés/route = 12-14 RON/kiszállítás; breakeven 10 rendelés (176 RON OPEX); ajánlott 120 RON ingyenes szállítási küszöb + 15 RON díj alatta; heti 2 route indulásnak |

## AI Session Links

- ChatGPT: https://chatgpt.com/g/g-p-69cbee4a04c481918a2a738959b92361-deak/c/69da0a38-ce68-8391-bfb4-a2bbf24a66e7
- Perplexity: (session link nem elérhető — új keresésben futott)
- Gemini: (session link nem elérhető — új session-ben futott)

## Key Insights — Szintézis

### 1. A modell: Fix-route pre-order ("tejkihordós" modell) — KONSZENZUS

Mind a 3 AI egybehangzóan a **fix napos, előrendeléses, route-alapú** modellt ajánlja. Ez NEM on-demand, hanem tervezett logisztika.

| Szempont | Fix-route előny |
|----------|----------------|
| Költséghatékonyság | Kiszámítható útvonal, konszolidált rendelések |
| Hűtőlánc | Rövidebb, tervezhető; nem kell hűtőboxot hagyni |
| Bevezethetőség | Alacsony tech igény (település-választó + nap kiválasztás elég) |
| Kulturális illeszkedés | A vidéki vásárló elfogadja a fix napot (piac-analógia) |

**ChatGPT kritikus figyelmeztetése:** "A rendelés-sűrűség az EGÉSZ modell kulcsa." Ha nincs elég rendelés egy route-on, a gazdaságosság összeomlik.

### 2. Kettős pozicionálás: város vs. falu

| Dimenzió | Város (Udvarhely) | Falu |
|----------|-------------------|------|
| Probléma | Kényelem (időmegtakarítás) | **Elérhetőség** (nincs bolt!) |
| Modell | On-demand / másnapi | Fix nap (hétfő/csütörtök) |
| Szállítás | Azonnali / aznapi | Route-alapú, tervezett |
| Értékajánlat | "Spórolj időt" | **"Friss hús az ajtódban"** |
| Ügyfél motiváció | Convenience | **Szükséglet-alapú** (erősebb!) |

**Gemini insight:** A falusi kereslet potenciálisan stabilabb, mert nincs alternatíva. A városi vásárló bármikor bemehet a boltba — a falusi nem.

### 3. Route economics — számok (Gemini modell)

**Egy route költségstruktúrája:**

| Tétel | Összeg |
|-------|--------|
| Üzemanyag (40 km route) | 56 RON |
| Sofőr (3 óra x 30 RON) | 90 RON |
| Amortizáció + egyéb | 30 RON |
| **Összes OPEX / route** | **~176 RON** |

**Breakeven táblázat:**

| Rendelés/route | Költség/rendelés | Fedezet (120 RON AOV, 20% margin) | Profit/rendelés |
|---------------|-----------------|-----------------------------------|----------------|
| 5 | 35 RON | 24 RON | **-11 RON** |
| 10 | 17,6 RON | 24 RON | **+6,4 RON** |
| 15 | 11,7 RON | 24 RON | **+12,3 RON** |
| 20 | 8,8 RON | 24 RON | **+15,2 RON** |

**Breakeven: ~8-10 rendelés/route.** 15+ rendelés már egészséges margint ad.

### 4. Szállítási díj stratégia — 120 RON küszöb

| Kosárérték | Szállítási díj | Indoklás |
|-----------|----------------|----------|
| >= 120 RON | **INGYENES** | Ösztönzi a nagyobb kosarat + fedezi a route-ot |
| < 120 RON | **15 RON** | Visszatartja az apró rendeléseket |

**Perplexity kontextus:** EU free-delivery medián ~50 EUR (~250 RON). A 120 RON (kb. 24 EUR) alacsony, de a vidéki húsvásárlás méretéhez illeszkedik (3,88 kg/hó x ~30-40 RON/kg = ~120-155 RON/hó).

**ChatGPT figyelmeztetés:** Az ingyenes szállítás ROUTE + MINIMUM KOSÁR-hoz kötött legyen, ne általános ígéret.

### 5. Piacpotenciál — Hargita megye falvai

**Perplexity adatok:**
- Odorheiu Secuiesc (Székelyudvarhely): 31.335 lakos
- 40 km-es körzetben ~53 település, ~15.000-20.000 háztartás (becslés)
- Románia vidéki internet-penetráció: **88%** (2023) — nem akadály
- Húsfogyasztás: ~3,88 kg/fő/hó (RO átlag)

**Pilot-méretű becslés (3-5 falu, heti 2 route):**

| Paraméter | Konzervatív | Optimista |
|-----------|-------------|-----------|
| Háztartások (3-5 falu) | ~2.000 | ~3.500 |
| Penetráció (6 hó) | 2% | 5% |
| Aktív vásárlók | 40 | 175 |
| Rendelés/hó/fő | 2 | 3 |
| Havi rendelésszám | 80 | 525 |
| Havi forgalom (120 RON AOV) | 9.600 RON | 63.000 RON |

### 6. Marketing — a falusi "word of mouth" erő

**Konszenzus a 3 AI-tól:**

| Csatorna | Prioritás | Megjegyzés |
|----------|-----------|------------|
| **Falusi nagykövetek** (ambassador) | Magas | Helyi bizalmi személy (bolt, posta, iskola); kis jutalék vagy ingyenes szállítás |
| **Plakátok** (bolt, posta, templom) | Magas | QR kóddal; a telefonáló is ezt javasolta |
| **Facebook csoportok** (helyi) | Közepes | "Székelyudvarhelyi boldog szülők" típusú csoportok |
| **Személyes bemutató** | Közepes | Első route-on kóstoltatás / bemutató csomag |
| **Szórólap a szállítással** | Közepes | Minden kiszállítással egy szórólap a szomszédoknak |
| Helyi esemény / vásár | Alacsony | Alkalmi, nem rendszeres |

**Gemini részlet:** Az "ambassador" modellben a helyi bizalmi személy (pl. falusi boltosné, postás) összegyűjti a rendeléseket — ez csökkenti a tech-korlátot is.

### 7. Kockázatok és mitigáció

| Kockázat | Valószínűség | Hatás | Mitigáció |
|----------|-------------|-------|-----------|
| **Alacsony rendelés-sűrűség** | Magas | Route nem fedezi magát | Minimum 8-10 rendelés/route indítási küszöb; pre-order cutoff 24h előtt |
| **Logisztikai kapacitás** | Közepes | Város + falu egyszerre túl sok | Város és falu külön napok; hűtős autó közös használat |
| **Hűtőlánc kockázat** | Közepes | Minőségromlás | Fix route = rövid, tervezett; hűtőtáska/box elegendő |
| **Szezonalitás** | Közepes | Nyáron kevesebb (kert, házi vágás) | Téli pilot indítás; szezonális termékek |
| **Tech korlát vidéken** | Alacsony | Idős vásárló nem tud rendelni | Ambassador / telefonos rendelés opció |
| **Deák kapacitás** | Közepes | Több route = több csomagolási idő | Fokozatos bevezetés (1 route/hét -> 2 -> 4) |

## Decisions Made

### D-1: Modell típus — Fix-route pre-order
- **Döntés:** KONSZENZUS — mind a 3 AI és a telefonáló is a fix napos modellt támogatja.
- **Indoklás:** Költséghatékony, kulturálisan illeszkedő, alacsony tech igény.

### D-2: Pilot méret — 2-3 falu, heti 1-2 route
- **Döntés javasolt:** Kis körrel indulni (pl. Szentegyháza + Zetelaka útvonal).
- **Státusz:** SZABOLCS DÖNTÉSÉRE VÁR.

### D-3: Szállítási küszöb — 120 RON / ingyenes, alatta 15 RON
- **Döntés javasolt:** Gemini + Perplexity adatok alapján.
- **Státusz:** SZABOLCS DÖNTÉSÉRE VÁR.

### D-4: Tech — település-választó (NEM geolokáció)
- **Döntés:** ChatGPT explicit figyelmeztetése: ne overengineereld. Dropdown elég a pilothoz.
- **Státusz:** ELFOGADVA (pilot scope).

### D-5: Marketing — ambassador + plakát + QR
- **Döntés javasolt:** Falusi bizalmi személy + fizikai plakátok a fő csatorna.
- **Státusz:** SZABOLCS DÖNTÉSÉRE VÁR.

## Open Questions

- [ ] [SZABOLCS] Melyik falvak az első route? (Szentegyháza + Zetelaka logikus — közel, nagyobb)
- [ ] [SZABOLCS] Deák kapacitás: bírják-e a csomagolást heti 2 extra route-ra?
- [ ] [SZABOLCS] Ki vezeti a szállítást? Meglévő sofőr vagy új?
- [ ] [SZABOLCS] Mikor indulhat a falusi pilot? v0.3 beta után, vagy külön fázis?
- [ ] [SZABOLCS] A 120 RON küszöb reális? (A telefonáló szerint a falusi vásárló nagyobb tételben vásárol)
- [ ] [CLAUDE] Route térkép: konkrét útvonaltervezés a kiválasztott falvakra
- [ ] [CLAUDE] Founding 50 kiterjesztés: a falusi pilot beépíthető-e a Founding 50 programba, vagy külön cohort?
- [ ] [CLAUDE] Szállítási díj logika beépítése a Frappe rendszerbe (settlement-based delivery fee)
- [ ] Phase trigger: mikor lépünk 2 route-ról 4-re? (Rendelés/route >= 15 stabilan 4 héten át?)

## Akcióterv (javasolt)

### Immediate (döntés után)
1. Falu-kiválasztás (Szabolcs + Deák) — 2-3 falu az első route-ra
2. Kapacitás-check Deákkal (csomagolás + szállítás)
3. Ambassador azonosítás (1-2 bizalmi személy faluként)

### Phase 1 — Soft launch (v0.3 beta + 2-4 hét)
4. Település-választó hozzáadás a rendelési felülethez
5. Fix kiszállítási nap logika (hétfő/csütörtök) a backendben
6. Plakátok + QR kódok nyomtatása (falusi verziók)
7. Első route indítása (heti 1x, pre-order cutoff 24h)

### Phase 2 — Bővítés (ha Phase 1 route breakeven elérve)
8. Második route hozzáadása (heti 2x)
9. További falvak bevonása
10. Szállítási díj optimalizálás a valós adatok alapján

## Context References

- `brainstorm/brainstorm_deak-pricing-revenue-share.md` — platformdíj modell (validált)
- `Business Development/pilot-husuzlet/founding50-spec-v1.0.md` — Founding 50 program
- `Business Development/pilot-husuzlet/BMC-v2.2.md` — Business Model Canvas
- `01_PROJECT_STATE.md` — projekt státusz
- `CLAUDE.md` — projekt kontextus és szabályok
