---
description: Alfred RECAP — "mit csináltam ma / a héten / szerdán?". Read-only emberi összegzés a vault git-historyból + agent-eseményekből + napi jegyzetekből. Megerősítés nélkül fut.
id: a1f10012-0000-4c00-8000-000000000012
index_schema_version: 1
---

A felhasználó azt kérdezi, mit végzett egy adott időszakban (ma, a héten, egy adott napon). Alfred emberi nyelven, bizonyíték-alapon válaszol, és gyengéden ellensúlyozza a "nem csinálok eleget" érzést a tényleges output felmutatásával.

**$ARGUMENTS** — opcionális időszak. Default: **ma**. Értelmezd ezeket:
- üres / `today` / `ma` → since = mai dátum
- `yesterday` / `tegnap` → since = until = tegnap
- `week` / `hét` / `this-week` → since = a hét hétfője
- `--since YYYY-MM-DD` (+ opcionális `--until YYYY-MM-DD`)
- konkrét nap neve/dátum (pl. `szerda`, `2026-05-27`) → since = until = az a nap

**Tennivaló:**

1. Számold ki a `since` (és ha kell `until`) dátumot a fenti szabályok szerint. A mai dátumot a környezeti `currentDate`-ből vedd.
2. Futtasd a harvest-helpert (ez olvassa a markdown ledger shardokat, read-only):
   ```
   bash "00_Prompts/BDOS/agents/alfred/recap_harvest.sh" --since <YYYY-MM-DD> [--until <YYYY-MM-DD>]
   ```
   A forrás: `02_Areas/Personal Growth/Alfred/activity/YYYY-MM.<gép>.md` shardok (per-gép, sync-biztos), git és DB NÉLKÜL. A helper az összes gép shardját összefésüli idő szerint.
3. Az output szekciók értelmezése:
   - **ACTIVITY** = a nagy események összefésülve minden gépről, idő szerint. Minden sor: `- <ISO> · <forrás> · <kategória> · <összefoglaló>`. Ezeket csoportosítsd téma/nap szerint emberi mondatokká (NE nyers dump). A `denoise/fix/build/tend/publish/spec` kategóriákból fogalmazz természetes nyelvet.
   - **MACHINES seen** = melyik gépeken volt aktivitás az időszakban (ezt megemlítheted, ha több gép).
   - **DAILY NOTES** = ha van napi jegyzet, hivatkozz rá.
4. **Coverage-figyelmeztetés (ha releváns):** a ledger csak azt látja, amit beleírtak (agent mode-completion, session-end hook, manuális capture). Ha egy időszakban kevés a bejegyzés, jelezd, hogy lehet kézzel rögzítetlen munka is. Légy őszinte a hézagról.

**Output szekciók:**
- **Amit elvégeztél** (a git + agent események emberi összegzése, témákba csoportosítva)
- **Ami elromlott / figyelmet kér** (failure események, ha van)
- **Lefedettség** (egy sor: mennyire teljes a kép — commitolt vs uncommitted/session-munka)

Hangnem: tárgyilagos, de bátorító. Ne legyen üres dicséret; a tényekkel mutasd meg, hogy a nap/hét nem volt üres. Gondolatjelet SOHA ne használj (vault §0).

**Read-only** — nem módosít semmit. Confirmation nem kell.

Lásd: `00_Prompts/BDOS/capabilities/activity-ledger/SPEC.md` (Alfred = interface / recap szerep) és `00_Prompts/BDOS/agents/alfred/recap_harvest.sh`.
