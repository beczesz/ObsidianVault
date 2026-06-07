---
description: Presto EXHAUST mode — seed lezárása (status: exhausted) emberi döntésre. Seed nem fejleszthető tovább, vagy szándékosan kihagyjuk. Ha a seed-ből már van Publication, figyelmeztet. Confirmation kötelező.
id: e6b4c0d5-2f7a-4b1c-d3e4-5f6a7b8c9d0e
index_schema_version: 1
bdos_index: true
---

A felhasználó egy seed-et lezár — nem fejleszthető tovább vagy szándékosan kihagyjuk.

**$ARGUMENTS** — kötelező:
- `--seed <seed-id>` — melyik seed-et zárja le
- opcionális `--reason "<szöveg>"` — az exhaust oka (ha hiányzik, Presto kérdezi)

**Tennivaló:**

1. Parsold az $ARGUMENTS-ből: `--seed` (kötelező), `--reason`.
2. Ha `--seed` hiányzik, kérdezz vissza: "Melyik seed-et zárjam le?"
3. Hívd `subagent_type: presto` **exhaust módban**:
   - Olvasd a seed fájlt (`00_Prompts/BDOS/agents/presto/_inbox/seeds/<seed-id>.md`)
   - Validáld: `status` nem már `exhausted` (ha igen, jelzi: "Ez a seed már exhausted.")
   - Ellenőrizd: van-e `linked_publications` a seed-ben (ha igen, figyelmeztet: "Ehhez a seed-hez N Publication létezik: [...]. Azok megmaradnak.")
4. Ha `--reason` hiányzik, kérdezd interaktívan: "Mi az exhaust oka? (pl. időszerűtlen, más kampány lefedi, user döntés)"
5. **Confirmation gate KÖTELEZŐ** — mutasd: seed-id, seed tartalom összefoglaló, kapcsolódó Publications (ha van), reason, következmény ("seed status: exhausted, ezentúl nem jelenik meg today/status-ban"). Vár igen/yes válaszra.
6. Igen után:
   - Frissítsd seed `status: exhausted`
   - Kitöltsd `exhausted_reason: <reason>` és `exhausted_date: YYYY-MM-DD`

**Fontos:**
- Seed exhaust NEM törli a seed fájlt — megmarad az archiv referenciának
- Linked Publications megmaradnak és függetlenül továbbléphetnek a pipeline-ban
- Exhaust visszafordítható: `status` manuálisan visszaállítható `new`-ra (de Presto nem csinál undo-parancsot — szándékos)

**Mikor NE exhaustálj:**
- Ha a seed csak régen nem volt érintve — ez `today` jelzés, nem auto-exhaust
- Ha csak egy csatornán nem működik — draft más csatornára (`/pres-draft --seed <id> --channel <más>`)

Lásd: `00_Prompts/BDOS/agents/presto.md` §6.4e.
