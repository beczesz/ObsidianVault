---
description: Sage HARVEST mode — kézi napi harvest a Referencia chatből (cron-on kívül). Új gondolatokat extract-el, atomic-javaslatokat tesz.
id: 493c0de9-9476-4c0d-8529-57c72847b5c0
index_schema_version: 1
---

A felhasználó kézi Sage harvest-et kér. Ez ugyanaz, ami minden reggel 06:00-kor automatikusan fut, csak most azonnal.

**$ARGUMENTS** — opcionális. Lehet:
- üres → standard napi harvest
- `--since <ISO ts>` → felülírja a `last_seen`-t, ettől az időponttól nézi az új üzeneteket
- `--dry-run` → fut, de NEM ír note-ot / state-et (csak jelenti, mit csinálna)

**Tennivaló:**

1. Értelmezd az $ARGUMENTS-et
2. Hívd meg a Sage agentet **`subagent_type: sage`**-vel (fallback `general-purpose` a kanonikus prompttal)
3. Adj át paramétereket:
   - `mode: harvest`
   - `prompt_file: 00_Prompts/BDOS/agents/sage/prompts/daily_harvest.md`
   - `manual: true`
   - opcionális: `since`, `dry_run`
4. A subagent izolált contextusban fut — várd a summary-t (max ~400 szó)
5. Add vissza a felhasználónak:
   - hány új thought / atomic-proposal / uncertain
   - notify-flag és indoka
   - bármi meglepő

Ha Sage `errors`-szal tér vissza, mutasd ki egyértelműen — nem rejtjük el.
