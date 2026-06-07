---
title: Sprint Ordering Review — Stratégiai értékelés
description: "Stratégiai értékelés a sprint sorrendzésről: javasolja a Sprint 2.5 beiktatását blocker feloldásra, a v0.3 leszűkítését 4 kulcsfunkcióra, a szünet törlését és a v0.4 Mobile korábbi indítását az erősebb kombinált hatás érdekében. Termékmenedzserek és fejlesztői vezetők döntéshozatal céljára."
description_source: auto
description_hash: 46d73cc205df7865
version: 1.0
date: 2026-04-11
author: Claude (Anthropic) + Szabolcs
status: REVIEW — Szabolcs döntésre vár
id: 244bb104-c247-4ccd-a1cb-d5d645189e7f
index_schema_version: 1
---
# Sprint Ordering Review — v0.2 → v0.3 → v0.4 értékelés

## Összefoglaló

A jelenlegi sprint sorrend (v0.2 → v0.3 Savings Engine → szünet → v0.4 Mobile) **alapvetően helyes**, de a scope és timing finomhangolásra szorul.

## Fő javaslatok

### 1. "Sprint 2.5" beiktatása (ápr. 17-25)
A beta és a v0.3 fejlesztés között 10 nap execution blocker feloldásra:
- Partnerségi megállapodás megkötése (BLOKKOLÓ)
- Pénzügyi adatok beszerzése (BLOKKOLÓ)
- DH-104 Firebase Analytics lezárása
- Legal minimum (ÁSZF + Impresszum draft)
- Első rendelések megfigyelése (operáció validáció)

### 2. Lean v0.3 (2 hét, 4 feature a 10 helyett)
MUST features (L1 + L3 core):
- Running savings counter (DH-117/118)
- Threshold nudge
- Post-order recap (DH-119)
- 1-click reorder (DH-120)

Kihagyva (v0.4.1 vagy v0.5-be):
- Családi csomagok, Swap suggestion, "Szokásos rendelésem", Email features

### 3. 2 hetes szünet törlése
A v0.3 és v0.4 közötti szünet beolvad — a 10.3x velocity mellett nem kell 2 hét management teszt.

### 4. v0.4 Mobile 2 héttel korábban indul
A savings + push notification EGYÜTT erősebb, mint külön-külön.

## Ajánlott timeline

| Hét | Mi történik | Verzió |
|-----|-------------|--------|
| Ápr. 14-17 | Beta launch | v0.2 |
| Ápr. 17-25 | Execution blockers + monitoring | "Sprint 2.5" |
| Ápr. 25 – Máj. 9 | Lean Savings Engine | v0.3 |
| Máj. 9-12 | v0.3 launch + adatgyűjtés | v0.3 |
| Máj. 12-30 | Mobile app + Push | v0.4 |
| Máj. 30 – Jún. 5 | Mérés + Habit | v0.4.1 |
| Jún. 5-10 | 30 napos pilot döntés | Scale/Pivot/Stop |

## Dokumentum-konfliktus (TISZTÁZANDÓ)
A v0.3-release-plan.md és a v0.4-v0.6-roadmap-plan.md ÜTKÖZŐ timeline-t tartalmaz (mindkettő ápr. 28-tól indul). Ezt a Lean v0.3 javaslat feloldja.

## Döntésre vár
- [ ] Elfogadod-e a Lean v0.3 scope-ot (4 feature)?
- [ ] Töröljük a 2 hetes szünetet?
- [ ] A "Sprint 2.5" execution blocker fázis reális-e?
- [ ] A partnerségi megállapodás mikor történik meg?
