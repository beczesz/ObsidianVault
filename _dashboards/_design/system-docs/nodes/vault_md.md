---
id: vault_md
title: Markdown vault ★
layer: data
purpose: |
  Az Ideas Vault markdown fájljainak összessége — a teljes BDOS
  persistence layer. Ez a rendszer egyetlen forrás-az-igazságra.
  Minden agent, minden dashboard, minden API ebből olvas; visszaírni
  csak az erre jogosult végpontok (ep_capture, ep_process) írnak.
  Google Drive-on szinkronizálódik Mac ↔ Windows között.
depends_on: []
status_endpoint: /health (component: vault_md)
index_schema_version: 1
---

## Miért létezik — és miért csillagos (★)

A vault_md a rendszer gravitációs középpontja. Mindent lehet újraépíteni
(vault.db regenerálható, obs.db regenerálható, a szerver újraindítható),
de a markdown fájlok az egyetlen dolog, ami nem regenerálható automatikusan —
ezek tartalmazzák a tudást, a döntéseket, a logokat, a task-okat, az
ötleteket. Ha ez elvész, elvész minden.

A csillag (★) ezt jelöli: ez az egyetlen igazi forrás-az-igazságra.
Minden más derived — beleértve ezt a dashboardot is.

## Struktúra

```
0. Ideas Vault/
├── 01_Projects/    # rövid távú, deadline-os feladatok
├── 02_Areas/       # tartós felelősségi körök (a vault zöme)
├── 03_Resources/   # külső input, referencia
├── 04_Archive/     # inaktív anyag
├── 05_DailyNotes/  # napi jegyzetek
├── 00_Prompts/     # AI prompt-ok, agent definíciók
└── _dashboards/    # HTML dashboardok (nem markdown!)
```

## Read-only kontraktus

A dashboardok **sosem írnak** a vault_md-be JS-ből. Minden write az
ep_capture vagy ep_process végponton keresztül történik, amelyek belső
ellenőrzésekkel védik az adatintegritást.

## Szinkronizáció

Google Drive szinkronizálja a fájlokat Mac és Windows gép között.
A `gdrive` node a sync layer; a `windows_peer` a másik gép.

## Kapcsolódó

- [Vault Launcher](/_dashboards/index.html)
- [Librarian — Knowledge Manager](/_dashboards/librarian/index.html)
