---
description: Curator SURVEY mode — élő dashboard-index regenerálása (_dashboards/00_DASHBOARD_INDEX.md). Bejár minden tagot, kiolvassa a verziót/adatforrást/patternt/DS-státuszt.
id: b6d63565-d087-49db-8a82-1a77bef5e6bf
index_schema_version: 1
---

A felhasználó dashboard-leltárt kér a Curator-tól.

**$ARGUMENTS** — opcionális. Üresen: teljes `_dashboards/` család survey-e. Példák:
- (üres) → teljes family survey + index regen
- `--quiet` → index regen kommentár nélkül, csak a változások listája

**Tennivaló:**

1. Hívd meg a Curator-t **`subagent_type: curator`**-ral **survey módban**.
2. Curator bejárja a `_dashboards/` családot, kiolvassa minden HTML-ből: verzió (comment + pill), adatforrás (fetch path), pattern/recipe, launcher-regisztráció, DS-alignment státusz.
3. Regenerálja a `_dashboards/00_DASHBOARD_INDEX.md`-t (ez non-destruktív, confirmation nélkül megy).
4. Visszaad egy rövid összefoglalót: hány tag, mi változott a legutóbbi survey óta.

**Kontextus-védelem:** ne ismételd meg a teljes index-tartalmat a chat-ben — csak a változás-deltát és a kulcs-statokat.
