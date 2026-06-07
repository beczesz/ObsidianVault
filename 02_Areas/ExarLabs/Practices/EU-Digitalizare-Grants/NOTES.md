---
type: practice
id: 1481a45a-5320-4ca0-b57f-dd05f155912d
practice: "EU Digitalizare Grants"
unit: "ExarLabs"
unit_display: "ExarLabs"
unit_short: "Exar"
slug: exarlabs-eu-digitalizare-grants
owner: "TBD (ExarLabs lead)"
status: active
maturity_stage: research
description: "ExarLabs practice area: digitalizációs projektek szállítása EU-pályázatból finanszírozott kkv-knak. ExarLabs vendor (nem pályázó): a kkv elnyeri a grantot, ExarLabs tervezi, fejleszti, leszállítja a digitalizációs projektet. Cross-client, ismétlődő szolgáltatás-vonal. Első aktív instance: Programul Regiunea Centru 2.2 Apel 2 (2026). Áthelyezve Sales/Cohorts-ból Forge stewardship alá 2026-05-30."
strategic_directions:
  - "ExarLabs mint EU-grant-funded digitalizációs vendor (Frappe/ERPNext, LMS, custom app)"
  - "Grant-call-onként újrahasznosítható playbook (eligibility-check, scope-fit, proposal-prep)"
  - "Reusable grant-context research réteg minden aktív call-ra"
next_step: "Hivatalos Ghidul Solicitantului kibányászása (megvan: 01_Projects/Palyazat/) és a research/grant-context felülírása autoritatív adatokkal"
deadline: "2026-08 (Apel 2 várható benyújtási ablak)"
blocker: "Ghidul consultativ draft, számadatok még nem véglegesek"
top_todos:
  - "Ghidul Solicitantului kulcsszakaszok kivonatolása (buget, cofinanțare, eligibilitate, dátumok)"
  - "Célszegmens-prioritás véglegesítése (élelmiszer/retail/oktatás/logisztika)"
  - "Reusable proposal-template a 15-200k EUR grant-sávra"
tags: [practice, exarlabs, eu-funding, digitalizare, centru-region, grant-delivery, frappe]
created: 2026-05-30
last_signal: 2026-05-30
related_engagements: []
related_practices:
  - "ExarLabs practice: Microsites"
counts:
  open_questions: 6
  related_engagements: 0
  learnings_active: 0
  learnings_proposed: 0
bdos_index: true
index_schema_version: 1
---

# EU Digitalizare Grants — ExarLabs Practice Area

> **Status 2026-05-30:** `active` / `research` stage. Áthelyezve a `Sales/Cohorts/regiunea-centru-digitalizare-2026/` Broker-kohortból Forge stewardship alá. Ok: ez nem egyetlen sales-pipeline, hanem cross-client, ismétlődő szolgáltatás-vonal (capability-layer), tehát Forge domainje, nem Broker-é.

## Mission

**Digitalizációs projektek szállítása EU-pályázatból finanszírozott kkv-knak.** ExarLabs pozíciója **vendor, nem pályázó**: a kkv nyeri el a grantot, ExarLabs tervezi, fejleszti és leszállítja a projektet, amit a grant finanszíroz (a számla ExarLabs-ra kerül).

A practice duális természetű (ezért practice area, nem egyszeri projekt):
- **Kutatási terület:** melyik EU/regionális digitalizációs call nyitott, mik a jogosultsági és elszámolhatósági feltételek, hogyan illeszthető hozzá egy ExarLabs deliverable.
- **Szolgáltatás:** kliensnek odaadható, ismétlődő grant-delivery csomag (eligibility-check → scope-fit → proposal-prep → implementáció).

## Scope

**In scope:**
- Aktív EU/regionális digitalizációs grant-call-ok monitorozása és kontextus-kutatása
- Kkv-eligibility előszűrés és scope-illesztés a grant elszámolható kategóriáihoz
- ExarLabs deliverable-mix összeillesztése (Frappe/ERPNext, Ignis LMS, custom app)
- Proposal- és projekt-scope előkészítés a pályázati benyújtáshoz
- Implementáció és testreszabás a grant-finanszírozott projekt keretében

**Out of scope:**
- Maga a pályázatírás/benyújtás a kkv nevében (consultant/pályázatíró feladata, nem ExarLabs core)
- ExarLabs SAJÁT pályázása forrásra (az project/strategy téma, lásd Ignis Academy)
- Konkrét, lezárt ügyfél-engagement adminisztrációja (az `Clients/` alá tartozik)

## Aktív instance: Programul Regiunea Centru 2.2 Apel 2 (2026)

Az első konkrét call, ami köré a practice szerveződik:
- **Grant-kontextus** (jogosultság, keret, dátumok): [[grant-pr-centru-2.2-apel2]] (`research/`)
- **Go-to-market terv** (szegmensek, value prop, fázisok, time-box): [[go-to-market-apel2]] (`proposals/`)
- **Hivatalos forrás:** a Ghidul Solicitantului (consultativ draft) már a vault-ban: `01_Projects/Palyazat/Ghidul-solicitantului-–-consultare-publica-1.pdf`

## Why this practice area

1. **Ismétlődő call-struktúra** — a regionális digitalizációs grantek ciklikusan újranyílnak (Apel 1, Apel 2, jövőbeli call-ok). A playbook újrahasznosítható.
2. **Cross-client** — több kkv jogosult ugyanarra a call-ra; a practice a kapacitás, nem egy lead-lista.
3. **ExarLabs-fit** — a Frappe-alapú gyors fejlesztés és a 15-200k EUR grant-sáv jól illeszkedik a portfólióhoz (Deák, Ignis referenciák).

## Folder structure

```
EU-Digitalizare-Grants/
├── NOTES.md             ← ITT
├── _inbox/              ← raw dump-ok, új call-signal
├── research/            ← grant-context fájlok (grant-pr-centru-2.2-apel2.md)
├── patterns/            ← reusable playbook (eligibility-check, scope-fit, proposal-template)
├── decisions/           ← ADR-ek (mely szegmens, mely deliverable-mix)
├── experiments/         ← kipróbált megközelítések
├── proposals/           ← ügyfél-facing / go-to-market (go-to-market-apel2.md)
├── learnings/           ← Forge structured learnings
├── related-projects.md  ← wikilinks
└── open-questions.md    ← nyitott kérdések
```

## Related engagements

Lásd: [[related-projects]]

## Open questions

Lásd: [[open-questions]]

## Forge log (append-only)

| Date | Event |
|---|---|
| 2026-05-30 | Practice area létrehozva. Tartalom áthelyezve a `Sales/Cohorts/regiunea-centru-digitalizare-2026/` Broker-kohortból (GRANT_CONTEXT → research/, COHORT GTM-tartalma → proposals/). Sales-kohort törölve. Forge stewardship. Maturity: `research`. |
