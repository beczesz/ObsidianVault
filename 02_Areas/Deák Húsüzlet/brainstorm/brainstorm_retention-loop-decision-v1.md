---
description: "Brainstorming session from April 2026 covering three interconnected topics: retention strategy (economic engine as primary driver, routine as missing dimension, three-layer stack), economic loop formalization (six-step cycle from user behavior to feedback), and decision memo with scenario-based actions and gate structure."
description_source: auto
description_hash: 24590ba8e4c2a861
topic: DHOP Retention Strategy + Economic Loop + Decision Memo
created: 2026-04-11
last_updated: 2026-04-11
status: active
depends_on: brainstorm_strategiai-attekintes-v1.md
id: d716c632-dc92-488e-87e6-625709d128ab
index_schema_version: 1
---
# Brainstorm: Retention Deep Dive + Economic Loop + Decision Memo

## Sessions
| Date | AI(s) Used | Key Outcome |
|------|-----------|-------------|
| 2026-04-11 | ChatGPT (Deak GPT) + Claude | 3-topic deep dive: retention, economic loop, decision memo |

## AI Session Link
- ChatGPT: https://chatgpt.com/g/g-p-69cbee4a04c481918a2a738959b92361-deak/c/69da0a38-ce68-8391-bfb4-a2bbf24a66e7

---

## SZINTÉZIS #1 — RETENTION STRATEGY (ChatGPT + Claude)

### Szabolcs hipotézise:
Két EGYENRANGÚ retention pillér van: (1) Economic Engine és (2) Mobile + Push

### ChatGPT verdict: NEM egyenrangúak.
- **Economic Engine = PRIMARY** (value-based retention: "Miért jöjjek vissza?")
- **Mobile + Push = AMPLIFIER** (attention-based retention: "Mikor jut eszembe?")

Analógia: Economic Engine = motor, Mobile + Push = gyújtás + pedál. Motor nélkül semmi. Gyújtás nélkül motor van de nem használják.

### App hatás a PMF szint függvényében:
| Állapot | App hatása |
|---------|-----------|
| Nincs PMF | Semmi |
| Gyenge PMF | Minimális |
| Erős PMF | Erős boost |

→ App túl korán = waste. App jó időben = multiplier.

### A HIÁNYZÓ DIMENZIÓ: Routine/Ritmus
A DHOP nem social app, nem game → household routine system.
3 elem kell:
1. **Fix ritmus:** "szerdai rendelés nap", "pénteki delivery" → habit anchor
2. **Predictability:** "hetente ajánlott kosár", "last order repeat"
3. **Memory offload:** "nem kell gondolkodni, rendszer gondolkodik helyetted"
→ Erősebb retention driver, mint social/gamification

### Maximum Retention Strategy — 3-Layer Stack:
| Layer | Elemek | Üzenet |
|-------|--------|--------|
| L1 ECONOMIC | savings, threshold, bundles | "megéri" |
| L2 ROUTINE | weekly cycle, reorder defaults, recurring patterns | "nem kell gondolkodni" |
| L3 TRIGGERS | push, icon, recap | "eszembe jut" |

### Claude kiegészítés:
- A L2 ROUTINE layer NINCS a jelenlegi sprint tervekben explicit módon
- A "Szokásos rendelésem" gomb (DH-127) és a "heti ajánlott kosár" ide tartozik
- A v0.3 Lean-ból ezek kiestek → v0.4.1-be kell bekerüljenek
- A Deák szállítási napirendje (kedd/csütörtök/szombat) a habit anchor alapja

---

## SZINTÉZIS #2 — ECONOMIC LOOP FORMALIZÁLÁSA

### A 6 lépéses loop:

**STEP 1 — USER BEHAVIOR**
User: nagyobb kosár, group order, reorder
Adat: basket size, frequency, product mix

**STEP 2 — SYSTEM EFFICIENCY**
Rendszer: jobb batching, kevesebb waste, optimalizált route
Adat: cost/order ↓, waste ↓, margin ↑

**STEP 3 — SAVINGS GENERATION**
Efficiency gain → savings pool keletkezik

**STEP 4 — SAVINGS DISTRIBUTION**
User felé: threshold discount, bundle pricing, recap

**STEP 5 — FEEDBACK**
User látja: "eddig X lejt spóroltál", "next threshold Y lejnél"

**STEP 6 — BEHAVIOR CHANGE**
User: nagyobb kosár, visszatérés, reorder → loop bezárul

### Sprint Mapping a Loop-ra:
| Sprint | Loop elemek | Szerep |
|--------|------------|--------|
| v0.3 | STEP 4 (threshold) + STEP 5 (savings counter, recap) + STEP 6 (reorder) | Feedback + behavior layer |
| v0.4 | STEP 5 trigger (mobile) + STEP 6 trigger (push) | Loop activation |
| v0.5 | STEP 1 influence (bundles, swap) + STEP 1 expansion (shared basket) | Behavior shaping |
| v0.6 | STEP 1 automation (predictive) + STEP 2 scaling (multi-supplier) | System depth |

### KPI-k loop-elemenként:
| Step | KPI 1 | KPI 2 |
|------|-------|-------|
| 1 — Behavior | Avg Order Value | Orders/user |
| 2 — Efficiency | Cost/order | Waste % |
| 3 — Savings pool | Savings/order | Margin delta |
| 4 — Distribution | Threshold hit rate | Bundle adoption |
| 5 — Feedback | Recap open rate | Savings awareness % |
| 6 — Behavior change | Second order rate | Reorder rate |

### Töréspontok (ahol a loop eltörhet):
1. **Fake savings** → user nem hiszi el
2. **No real efficiency** → nincs miből visszaadni
3. **Complexity** → user nem érti
4. **Supply instability** → loop megszakad
5. **Wrong incentives** → margin elégtelen

### Kapcsolat retention-nel:
> "Retention = Economic Loop működése időben. Ha loop működik → retention automatikus. Ha nem → push sem segít."

### Claude kiegészítés:
- **STEP 2 (System Efficiency) jelenleg NEM MÉRHETŐ** — a Deáktól pénzügyi adatok kellenek (waste%, per-product margin, delivery cost). Ez a Sprint 2.5 / "Economic Ground Truth Sprint" feladata.
- **STEP 3 (Savings Generation) jelenleg FELTÉTELEZÉS** — amíg STEP 2 nincs mérve, a savings counter "reference price vs app price" marad, nem "system efficiency gain share" (ahogy a ChatGPT javasolta).
- **A loop LEGGYENGÉBB pontja**: STEP 2→3 átmenet. Ha a Deák nem ad pénzügyi adatot, az egész loop vak.

---

## SZINTÉZIS #3 — DECISION MEMO

### Metrika tábla:
| Metrika | Mit mér | Prioritás |
|---------|---------|-----------|
| Regisztráció | Érdeklődés (top-of-funnel) | Alacsony |
| Rendelés | Valós érték (conversion) | Közepes |
| Repeat | Habit (retention) | LEGMAGASABB |
| AOV | Gazdasági erő (basket) | Magas |
| Delivery success | Operáció (supply) | Magas |

### Szcenárió → Döntés → Akció:
| Szcenárió | Döntés | Fő akció |
|-----------|--------|---------|
| 25/12/3 | ITERATE | Onboarding + retention gap fix (2-4 hét) |
| 40/20/12 | SCALE | Ops stabilizálás, loop megerősítés |
| 35/18/2 | PIVOT (retention) | User interview, value/experience redesign |
| 8/4/2 | CONDITIONAL STOP | Ha marketing jó → stop; ha nem → retry |
| 50/30/15 + supply fail | THROTTLE | Delivery cap, idősávok, growth stop |

### Decision Gate struktúra:
| Gate | Időpont | Cél |
|------|---------|-----|
| 30 nap | Signal detection | Melyik hipotézis dőlt meg? |
| 60 nap | Hypothesis test | Célzott iteráció eredménye |
| 90 nap | Board decision | Scale / Pivot / Park / Stop |

### Red Flag lista (AZONNALI reakció):
| 🔴 Red Flag | Akció |
|-------------|-------|
| Nincs repeat (0 visszatérő 14 nap után) | Azonnali deep dive: mi történik az első rendelés után? |
| Supply fail (Deák nem tud szállítani) | Growth stop, delivery cap, ops review |
| User complaint spike | Ops review, quality check |
| Margin negatív | Pricing fix, threshold review |
| Push nélkül nincs aktivitás | Nincs valódi retention — Economic Engine vizsgálata |

---

## Decisions Made (2026-04-11)
- Economic Engine = PRIMARY retention driver, Mobile = AMPLIFIER (ChatGPT verdict, elfogadva)
- 3-layer retention stack: Economic → Routine → Triggers (ChatGPT framework)
- Economic Loop formalizálva: 6 lépés (behavior → efficiency → savings → distribution → feedback → behavior change)
- Decision Memo: 5 szcenárió + 30/60/90 gate + red flag lista
- L2 ROUTINE layer bekerül a sprint tervbe (v0.4.1)
- A loop leggyengébb pontja: STEP 2→3 (efficiency → savings) — pénzügyi adatok nélkül vak

## Open Questions
- [ ] ChatGPT: ENGINE v1 — pricing + savings model (matematikai modell)
- [ ] Szabolcs: Pénzügyi adatok mikor érkeznek? (a loop STEP 2-höz kritikus)
- [ ] Szabolcs: A Deák szállítási naprendje fix? (habit anchor alapja)
- [ ] Claude: A "heti ajánlott kosár" (L2 ROUTINE) melyik sprintbe kerüljön?
