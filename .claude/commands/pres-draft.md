---
description: Presto DRAFT mode — seed-ből Publication draft generálása. Olvassa a seed intent blokkját, hívja /marketing:draft-content skillt, létrehoz presto.publication.v2 fájlt publication_status draft állapotban. Confirmation kötelező.
id: c4f2a8b3-0d5e-4f9a-b1c2-3d4e5f6a7b8c
index_schema_version: 1
bdos_index: true
---

A felhasználó seed-ből draft publikációt generál.

**$ARGUMENTS** — kötelező:
- `--seed <seed-id>` — melyik seed-ből dolgozzon
- opcionális `--channel <override>` — felülírja a seed `channels[0]`-ját
- opcionális `--area <override>` — ha eltér a seed area-jától

**Tennivaló:**

1. Parsold az $ARGUMENTS-ből: `--seed` (kötelező), `--channel`, `--area`.
2. Ha `--seed` hiányzik, kérdezz vissza: "Melyik seed-ből dolgozzak? (seed-id)"
3. Hívd `subagent_type: presto` **draft módban**:
   - Olvasd `00_Prompts/BDOS/agents/presto/_inbox/seeds/<seed-id>.md`-t
   - Validáld: `status` nem `exhausted` (ha igen, figyelmeztet: "Ez a seed exhausted. Biztosan folytatod?")
   - Határozd meg a target channel-t: `--channel` override VAGY seed `channels[0]`
   - Olvasd az Area `Marketing/MARKETING_ENGINE.md`-ből a brand-tone-t (ha létezik)
   - Olvasd az `00_Prompts/BDOS/agents/presto/audience-learnings/active/*.md`-ből a vonatkozó tanulságokat
   - Generálj `pub-id`-t: `pub-<channel>-<YYYYMMDD>-<slug>`
4. **Confirmation gate KÖTELEZŐ** — mutasd: seed-id, target channel, brand-tone, pub-id, `/marketing:draft-content` hívás. Vár igen/yes válaszra.
5. Igen után:
   - Hívd `/marketing:draft-content`-et az intent + tone + channel-specifikus formátummal
   - Írj `02_Areas/<area>/Marketing/Publications/<pub-id>.md`-t (`presto.publication.v2`, `publication_status: draft`)
   - Frissítsd seed `status: in-progress`, `linked_publications: [<pub-id>]`

**Publication schema minimuma (pub-id.md):**
```yaml
---
schema: presto.publication.v2
pub_id: pub-channel-YYYYMMDD-slug
publication_status: draft
seed_id: <seed-id>
area: <name>
channel: LinkedIn|X|Blog|Newsletter|...
intent:
  audience: "<örökölt a seed-ből>"
  message: "<örökölt>"
  hook_angle: "<örökölt>"
publish_date: null
---

## Body
<draft szöveg>

## Variants
(prepare mód tölti ki)

## Review findings
(prepare mód tölti ki)
```

**Következő lépés draft után:**
- `/pres-prepare --pub <pub-id>` → brand-review + variációk + schedule javaslat

**Soha:** ne publikálj draft-ot közvetlenül — előbb `/pres-prepare`, majd `/pres-approve`.

Lásd: `00_Prompts/BDOS/agents/presto.md` §6.4b.
