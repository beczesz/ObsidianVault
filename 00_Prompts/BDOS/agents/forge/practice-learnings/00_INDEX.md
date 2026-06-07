---
schema: forge.practice-learnings.index.v1
generated_at: null
counts:
  active: 0
  proposed: 0
  retired: 0
description: Forge cross-practice meta-learnings élő indexe — practice-development specifikus meta-tanulságok (8 tervezett típus, v0.2-ben véglegesítve). Forge `learn` módja frissíti. META szint: HOGYAN fejlődik egy practice area általában. NEM keverendő össze a per-area learnings/-szel (`Practices/<area>/learnings/`), ami egy konkrét területre vonatkozik.
id: 9b7c4f81-3e6d-4a92-8c15-7f2e9d6b4a83
index_schema_version: 1
bdos_index: true
---

# Forge — Cross-Practice Meta-Learnings Index

Meta-szintű tanulságok arról, **hogyan fejlődik egy practice area**. Sage/Presto/Broker mintára adaptálva.

**KÜLÖNBSÉG a per-area learnings-től:** ez nem az adott practice area konkrét tudását rögzíti (azt a `Practices/<area>/learnings/` mappa tartja), hanem a **practice management metafolyamatát**: mikor érdemes practice area-t létrehozni, mikor stabilizálódik egy pattern, mikor érdemes retire-olni, milyen evidence-küszöb működik.

## Active (0)
*Üres — Forge v0.1 most jött létre, nincsenek confirmed meta-learnings.*

## Proposed (0)
## Retired (0)

---

## Cap

- Max **15 active learning**, max **2000 token** preamble
- Sorrend: `confidence DESC, last_applied_at DESC`

## 8 practice-development meta-learning típus (v0.2-ben véglegesítve)

Tervezett típus-vocabulary (Broker 8-type mintára):

| Típus | Mit rögzít |
|---|---|
| `evidence-threshold` | hány független ügyfél-alkalmazás kell egy pattern stabilizálódásához (induló hipotézis: 3) |
| `area-lifecycle-stage` | hogyan ismerhető fel egy area maturity-stage váltása (forming → maturing → stable → retired) |
| `inbox-flow-pattern` | milyen szignál-tempóra refine-olunk és milyenre várunk |
| `cross-area-leak` | mikor "lóg össze" két practice area (pl. Inference Farm + Cloud Cost Opt) |
| `handoff-timing` | mikor érdemes Broker/Presto-nak átadni egy pattern-t (túl korán: spam, túl későn: elveszett opportunity) |
| `retire-signal` | mi prediktálja egy practice area haldoklását (last_applied_at, evidence-stagnálás) |
| `unit-fit-pattern` | mely unit-okban érdemes ugyanazt a practice area-t fenntartani vs. konszolidálni |
| `meta-pattern-emergence` | mikor érdemes egy practice area patternjét BDOS-szintű capability-be promote-olni |

## Lifecycle

Ugyanaz a `proposed → active → retired` mint Broker `sales-learnings/`. Lásd `00_Prompts/BDOS/agents/broker.md §4.8` a részletes pattern-ért.

## Cross-link

Sister-loops:
- Broker `sales-learnings` ([`../broker/sales-learnings/00_INDEX.md`](../../broker/sales-learnings/00_INDEX.md)) — sales-specifikus
- Presto `audience-learnings` — marketing-specifikus
- Sage `learnings` — cognition-specifikus

Maestro `observe` aggregátor látja mind a négyet.
