---
description: Curator AUDIT mode — a dashboard-család mérése a 7 törvény + DESIGN_SYSTEM ellen. Drift mátrix, kontextus-védett riport.
id: df74bcb9-8442-4611-ad67-06a7f460d4f0
index_schema_version: 1
---

A felhasználó dashboard-családi auditot kér.

**$ARGUMENTS** — opcionális. Példák:
- (üres) → teljes család audit minden tagra
- `sales` → csak egy tagra fókuszálva
- `--strict` → még a "pending promote" extrákat is drift-ként jelöli

**Tennivaló:**

1. Hívd meg a Curator-t **`subagent_type: curator`** **audit módban**.
2. Curator beolvassa a `_dashboards/_design/DESIGN_SYSTEM.md`-t (kanonikus tokenek + 7 törvény), majd minden tagot ellene mér:
   - `:root` token-drift (értékek, hiányzók, extrák)
   - 7 törvény ellenőrzése (home button, version pill, audit-trail, sync indicator, csak DS-tokenek, launcher-regisztráció, read-only render)
   - light/dark téma + card-copy-ref konzisztencia
3. A riport a `_dashboards/00_CURATOR_AUDIT.md`-be kerül (vagy frissül), és a chat-ben kapsz egy rövid compliance mátrix-táblát: dashboard × megfelelőség.
4. A Curator **csak jelez** — nem javít. Javításhoz `/dash-tend` vagy `/dash-promote`.

**Kontextus-védelem:** a teljes drift-listát csak a riport-fájlba írja; a chat-ben csak az összefoglaló tábla + a prioritás-jelöltek jelennek meg.
