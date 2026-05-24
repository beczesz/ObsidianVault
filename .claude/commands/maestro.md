---
description: Maestro — Brand-to-Site Conductor. Egyszavas hívás a Brand Spine pipeline 5 módjához (status / next / continue / start / audit). Felméri, hol vagyunk egy brand→site projektben, javasolja a következő lépést tool + skill + paranccsal, folytatja a félbehagyott munkát.
id: c0f2e4ee-f56c-4399-bf57-8d7fdaddd430
index_schema_version: 1
---

A felhasználó a **Maestro** agent-et hívja a Brand Spine pipeline-on.

**$ARGUMENTS** — a mód + opcionális paraméterek. Példák:
- `status` → riport a current project állapotáról (vagy a megnevezettről)
- `next` → következő konkrét lépés javaslata
- `continue` → folytatja a félbehagyott munkát (megerősítést kér)
- `start "Sonrisa CPS"` → új projektet indít (megerősítést kér tier-rel együtt)
- `start "Sonrisa CPS" --tier=standard` → tier előre megadva
- `audit` → minőségi check a kész rétegekre
- `audit --layers=1,2,3` → csak a megnevezett rétegek

Default project: current working directory. Override: `--project=<path>`.

## Tennivaló

1. Parsold a mode-ot az `$ARGUMENTS` első szavából
2. Ha a mode nem valid (`status` | `next` | `continue` | `start` | `audit`), kérdezz vissza egy mondatban, mutasd a 5 érvényes módot
3. Parsold a többi paramétert: project name (idézőjelek között), `--tier=`, `--project=`, `--layers=`
4. Hívd meg a Maestro-t **`subagent_type: maestro`**-val (vagy fallback general-purpose), átadva:
   - `mode: <status | next | continue | start | audit>`
   - `project: <path | current>`
   - mode-specifikus paraméterek (lásd canonical §4)
5. A subagent felelőssége olvasni a `brand-spine-state.md`-t, a recipe-t (`recipes/<tier>.md`), és a `tools/INVENTORY.md`-t
6. **Confirmation gate:** ha a mód `continue` vagy `start`, a Maestro mutatja a tervezett akciót és **megerősítést kér** mielőtt bármit írna. Az info-módok (`status`, `audit`) megerősítés nélkül futnak.

## Példa-hívások

```
/maestro status
/maestro next
/maestro continue
/maestro continue --project="02_Areas/Sonrisa"
/maestro start "Sonrisa CPS Új weboldal"
/maestro start "Új projekt" --tier=lean
/maestro audit
/maestro audit --layers=1,2,3
```

## Output-elv

- **Egységes formátum:** monospace dobozok riportokra, természetes nyelv magyarázatokra
- **Magyarul** alapesetben (ha a user angolul írt, váltsd)
- **Tömör:** ne ismételd az állapotot újra meg újra
- **Másolható parancsok:** minden javasolt parancs **code-block-ban** legyen, kész másolásra
- **Vissza-hivatkozások:** linkelj a `diagram.html#tool-<id>` URL-re, ha a részletes tool-wiki ott van

Ha minden tiszta, futtasd a Maestro-t a megfelelő móddal.
