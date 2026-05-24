---
title: Sage — Referencia chat formátum
date: 2026-05-24
author: Becze Szabolcs
status: active
version: 0.2
description: Hogyan írj a Referencia chatbe, hogy Sage biztosan értse. Példák + mockoltapéldát smoke teszthez. Ez a fájl mind dokumentáció (neked), mind Sage prompt-input (parsing-mintaként).
tags: [BDOS, sage, reference, smoke-test]
id: f779905e-87c2-403f-83fb-776eb039e1da
index_schema_version: 1
---

# Sage — Referencia chat formátum

> **Referencia chat URL:** https://chatgpt.com/g/g-p-67987afa409c8191b7ce9f798c887544-szemelyes-gondolatok/c/6a1265db-8910-83eb-8677-1e977c03fc01

## A formátum

Sage minden reggel 06:00-kor ide néz be. Az új user-üzeneteket "referencia"-ként parse-olja. Egy referencia akkor érthető Sage számára, ha tartalmazza ezeket:

| Mező | Mit jelent | Példa |
|---|---|---|
| **project / folder** | ChatGPT-projekt vagy mappa neve | "ExarLabs mappa", "Navigátor projekt", "Személyes" |
| **chat title** | a hivatkozott chat címe (vagy egyértelmű részlet) | "AI alapú operációs rendszer", "az új podcast strukturáció chat" |
| **window** | hol a chatben (üzenet-tartomány) | "utolsó 10-15 üzenet", "a tegnapi rész", "a legelső blokk" |
| **distribution hint** *(opc.)* | hova szánt | "LinkedIn-re mehet", "podcast témának jó", "csak belső" |

A többi szabad szöveg lehet, Sage tolerálja.

## 3 jó példa

### Példa 1 — explicit, mindenmező megvan

> "Új gondolat az AI Ops-ról az ExarLabs mappában, nézd meg az 'AI alapú operációs rendszer' chatet, utolsó kb. 10-15 üzenet. LinkedIn-re mehet."

Sage értelmezése:
```yaml
project: ExarLabs
chat_title: AI alapú operációs rendszer
window: last_10_15
distribution_hints: [LinkedIn]
```

### Példa 2 — laza, distribution hint nélkül

> "A Navigátor projektben a 'podcast pipeline átgondolása' chatben a tegnapi részben van valami fontos arról, hogy hogyan delegáljam a vágást. Nézd meg."

Sage értelmezése:
```yaml
project: Navigátor
chat_title: podcast pipeline átgondolása
window: yesterday
distribution_hints: []
```

### Példa 3 — több referencia egy üzenetben

> "Két dolog: (1) ExarLabs / 'cognition stack' chat, utolsó 5 üzenet — atomi gondolat a marketing fal-ról, LinkedIn poszt lehet. (2) Személyes / 'reggeli rutinok' chat, az új rész — csak belső."

Sage minkettőt kinyeri, két különböző `thoughts/...` note-ot generál.

## 1 rossz példa

> "Néz meg a tegnapit, érdekes volt."

→ Nincs project, nincs chat title. Sage `_inbox/thoughts/2026-05-24_uncertain_<slug>.md`-be ment, és heti curate-kor user-review kell.

---

## Smoke test — mockolt referencia

Az alábbi referenciát én generáltam smoke teszt céljára. Ez nem éles use case — csak arra való, hogy az első Sage harvest fusson, és a teljes pipeline (parse → navigate → extract → write note) végigmenjen, mielőtt valódi referenciákat adsz neki.

**Tedd be ezt egy új üzenetként a Referencia chatbe** (vagy bármelyik magas-üzenetbe, ami Sage `last_seen` után van):

```
[SMOKE TEST] Sage, ez egy próba-referencia. A "Személyes gondolatok" projekt
"ExarLabs - AI alapú operációs rendszer" chatjébe, az utolsó 15 üzenet közt
van egy gondolat arról, hogy a központi cognition-agent nem lehet
marketing-optimalizált. LinkedIn-re potenciálisan mehet, de először csak
atomic-jelöltként vedd fel. Forrás-author: hibrid (ChatGPT-5 + én).
```

**Várt Sage-output a smoke test után:**

1. `thoughts/2026-05-25_central-agent-not-marketing.md` — frontmatter + 1 mondatos summary + idézet + LinkedIn hint
2. `_inbox/atomic_proposals/cognition-not-marketing-optimized.md` — atomic-jelölt
3. Update `state/last_run.md`:
   ```yaml
   last_daily_status: ok
   last_harvest:
     references_seen: 1
     thoughts_created: 1
     atomic_proposals: 1
     inbox_uncertain: 0
     notified_user: false
   ```
4. Append `_journal/2026-05.md` — egy YAML-blokk a futásról
5. Update `state/last_seen.md` — az új üzenet ID-ja

Ha bármelyik output hiányzik vagy hibás → smoke fail, debug.

## Sage tanul ebből is

A REFERENCE_FORMAT.md egy **input Sage prompt-jához** is — daily_harvest prompt példáit innen veszi. Ha új mintát felismersz, ami működik, **fűzd hozzá ehhez a fájlhoz** — Sage következő futása már tudni fogja.
