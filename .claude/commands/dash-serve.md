---
description: Curator SERVE mode — a lokális dashboard-szerver vezérlése a 4321 porton (start/open/status/stop).
id: dce28557-5ed5-4edd-9bf3-c7ccbbd64edc
index_schema_version: 1
---

A felhasználó a dashboard-szervert vezérli.

**$ARGUMENTS** — opcionális akció. Példák:
- (üres) vagy `start` → indítás (ha már fut, helyette `open`)
- `open` → launcher megnyitása böngészőben
- `status` → fut-e, melyik porton, mióta
- `stop` → leállítás
- `restart` → stop + start

**Tennivaló:**

1. Hívd meg a Curator-t **`subagent_type: curator`** **serve módban** a megadott akcióval (default: `start`).
2. Curator a `_dashboards/_tools/dash-server.mjs`-t vezérli a 4321 porton:
   - `start` — háttérben indítja, jelzi a PID-t
   - `open` — `http://localhost:4321/` böngészőben (a launcher)
   - `status` — `lsof` ellenőrzéssel jelzi fut-e, és mióta
   - `stop` — graceful shutdown a `_tools/stop-dashboard.command`-on át
3. A `start`/`stop` info-akció — nem destruktív, megerősítés nélkül megy.

**Megjegyzés:** a szerver disk-ről szolgál ki, tehát file-mentés után **automatikusan friss** — nem kell restartolni a dashboardok frissítéséhez.
