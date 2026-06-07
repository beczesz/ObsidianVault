---
schema: sage.learning.v1
slug: verify-before-trust-after-publish
type: failure-mode
status: proposed
confidence: medium
proposed_at: 2026-05-26T00:00:00+02:00
confirmed_at: null
last_applied_at: null
applications_count: 0
evidence:
  - "EP43 launch session 2026-05-26: YT EP43 publish a felhasználó szóbeli 'publikálva' jelzésre lett pub-fájlban published-re bumpolva, Chrome MCP verifikáció nélkül — ha YT scheduling fail történt volna, post-hoc derült volna ki."
retired_at: null
retired_reason: null
retire_after_condition: "Ha 3 hónapig nincs ismételt 'trusted user word, post-hoc bug' eset."
scope: "Publication-state changes (scheduled → published, manual posts confirmations), external API submissions. YT, FB, Spotify és bármely külső platform state-módosítása."
id: a1f4c832-9e5b-4d8e-b307-2f17d6c9e501
index_schema_version: 1
description: Meta-learning arról, hogy state-modifying public-platform publish akciók (YT, FB, Spotify) után az agent NE fogadja el a user szóbeli 'megtörtént' jelzését verifikáció nélkül. Chrome MCP read-back vagy explicit UNVERIFIED jelzés kötelező, különben post-hoc publish-bugok csak később derülnek ki.
bdos_index: true
---

## A tanulság

**Amikor egy state-modifying akció megtörtént (különösen public-platform publish, mint YT/FB/Spotify), az agent NE BIZONYÍTÁS NÉLKÜL fogadja el a user szavát hogy "megtörtént". Verifikáció szükséges a state-update előtt.**

### 1. szabály — Automatikus Chrome MCP read-back

Bármely state-modifying public-akció (pl. `scheduled → published`, manuális post megerősítése) után az agent **automatikus Chrome MCP read-back**-et (screenshot vagy DOM-check) végez MIELŐTT a pub-fájlban frissíti az állapotot.

Az agentnek:
1. Chrome MCP-vel vagy screenshot-tal ellenőrizni, hogy a platform ténylegesen tükrözi az új állapotot.
2. Csak sikeres verifikáció után bumpolni a pub-fájl state mezőjét.
3. A verifikáció eredményét (URL, screenshot path vagy DOM-elem) megjegyezni az operacionális logban.

**Ne bízzon a user szóbeli visszajelzésére egyedül platform state-változásnál.**

### 2. szabály — UNVERIFIED jelzés ha a tool nem elérhető

Ha a verifikáció nem lehetséges (Chrome MCP unavailable, platform bejelentkezési fal, stb.):

- A state-frissítés **megtörténhet**, de a pub-fájlba kötelező: `verified: false` mező VAGY inline komment: `# UNVERIFIED — user verbal only`.
- A session summary-ban explicit risk-flag: "EP43 YT publish UNVERIFIED — validáld manuálisan a következő munkamenetben."

## Mire vonatkozik

Publication-state változások minden külső platformon: YouTube (upload, visibility toggle), Facebook/Instagram (post submit), Spotify (episode live check). Bármely agent, amely pub-fájlt kezel (Presto elsősorban, de Curator és Maestro is érintett ha state-t frissít).

## Hogyan vonom vissza

Ha 3 hónapig nincs ismételt "trusted user word, post-hoc bug" eset → retire (confirmed pattern stabil). Ha ismétlődik → escalate: Chrome MCP pre-check kötelező workflow-lépésként a runbook-ba kell.

## Kapcsolódó

- `capability-script-restart-and-smoke-test` — hasonló elv: agent-oldali ellenőrzés deliverable-részként, ne user fedezze fel a hibát.
- Presto runbook: publish-flow state-machine, `scheduled → published` transition lépés.
