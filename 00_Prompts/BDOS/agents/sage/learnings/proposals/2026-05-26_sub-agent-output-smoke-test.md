---
schema: sage.learning.v1
slug: sub-agent-output-smoke-test
type: failure-mode
status: proposed
confidence: medium
proposed_at: 2026-05-26T00:00:00+02:00
confirmed_at: null
last_applied_at: null
applications_count: 0
evidence:
  - "EP43 launch session 2026-05-26: Curator UnboundLocalError-t hagyott a events_server.py broadcast_vault_update()-ben (_clients scope-bug) — smoke-test hiányában néma fail jutott el a user-ig."
  - "EP43 launch session 2026-05-26: Curator Navigator-FB.md schema véletlen presto.channel-dna.v2-re ment a kanonikus v1 helyett — parent agent nem ellenőrizte diff-fel."
  - "EP43 launch session 2026-05-26: Curator azt állította a calendar-click v0.10.0 óta működik — valójában a sidecar file_path mező hiányzott, így a feature soha nem volt aktív. Verzió-pill bump is kimaradt néha."
retired_at: null
retired_reason: null
retire_after_condition: "Ha 4 hétig nincs sub-agent-output-bug (agent állítja, user nem találja hibát post-session)."
scope: "Curator dashboard tend, Presto publication-create, Maestro brand-spine ops, Librarian indexelés. Bármely sub-agent kódváltozás vagy schema-érintő művelet."
id: b2e5d943-0fa7-4c1f-a418-3e28a7b0f602
index_schema_version: 1
description: Meta-learning arról, hogy parent agent (Claude main, Presto, Maestro) NE fogadja el feltétel nélkül a sub-agent (Curator, Librarian) outputját. Sub-agent kódváltozás után kötelező smoke-test, schema-érintő módosítás után kötelező grep/diff ellenőrzés a kanonikus minta ellen — három független EP43-as eset alapján azonosított failure-mode.
bdos_index: true
---

## A tanulság

**Amikor a parent agent sub-agentet hív (pl. Claude main → Curator, Presto → Librarian), a sub-agent outputját NE fogadd el feltétel nélkül. A sub-agent hibákat termelhet: schema-version typo, scoping-bug, lint warning ignored, missing field, verzió-pill elmaradt.**

### 1. szabály — Smoke-test kötelező sub-agent kódváltozás után

Sub-agent kódot ír vagy módosít (dashboard HTML, Python capability script, pub-fájl, stb.):

1. A parent agent **automatikusan futtat smoke-test**-et: érintsd meg a releváns fájlt / triggerd az eseményt / ellenőrizd a várt viselkedést 5-10 másodpercen belül.
2. Ha a smoke-test nem lehetséges (pl. browser nem indítható): explicit note a session summary-ban: "Curator calendar-click módosítás — smoke-test nem futott, manuális ellenőrzés kell."
3. A sub-agent "kész" jelzése NEM elegendő — a parent agent felelőssége a verifikáció.

### 2. szabály — Schema-érintő módosítás után kötelező diff/grep

Ha a sub-agent frontmatter mezőt, schema-verziót, channel-dna struktúrát, verzió-pill értéket módosít:

1. A parent agent **grep-pel vagy diff-fel** hasonlítja a kanonikus mintához: `grep 'schema:' <file>` vs. a spec dokumentum aktuális értéke.
2. Eltérés esetén azonnali visszahívás a sub-agentnek javításra — nem folytatja a workflow-t.
3. Verzió-pill bump-ot (`v0.10.0 → v0.11.0`) minden dashboard-módosítás után ellenőrzi: bump nélküli Curator output reject.

## Mire vonatkozik

Curator dashboard tend (HTML kód, schema mezők, verzió-pill), Presto publication-create (pub-fájl frontmatter, channel-dna schema), Maestro brand-spine ops (brand-spine fájlok, runbook scaffold), Librarian indexelés (index fájl struktúra). Általánosan: bármely sub-agent kódváltozás vagy schema-érintő művelet.

## Hogyan vonom vissza

Ha 4 hétig nincs sub-agent-output-bug (a user nem fedez fel sub-agent által hagyott hibát) → retire. Ha ismétlődik különböző agenteknél → escalate: sub-agent output-validation lépés kerüljön a BDOS Constitution-ba.

## Kapcsolódó

- `capability-script-restart-and-smoke-test` — szoros testvér: daemon-restart + smoke-test ugyanennek az elvnek egy speciális esete.
- `verify-before-trust-after-publish` — párhuzamos tanulság: agent NE bízzon output/state jelzésben verifikáció nélkül.
- Curator DESIGN_SYSTEM: schema verzió konvenciók, verzió-pill bump szabályok.
