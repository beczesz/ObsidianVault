---
title: "(Bónusz) Feladat 1.3 — Inkonzisztenciák listája"
date: 2026-05-14
author: Becze Szabolcs
status: active
description: "Útmutató AI-alapú audithoz, amely végigmegy a TransOffice mappában található fájlokon, azonosítja az adateltéréseket, hiányosságokat és elavult információkat, majd strukturált listát készít az inkonzisztenciákról és nyitott kérdésekről a stakeholderek felé."
description_source: auto
description_hash: 82e3a6f6957d450d
id: 1ab80edc-cae7-430c-a3c1-b4baf8d7593c
index_schema_version: 1
bdos_index: true
---
# (Bónusz) Feladat 1.3 — Inkonzisztenciák listája

## Szituáció

Márton megemlítette: "Ha találtál valami furcsát, azt is írd bele." De mi van ha nem csak egy-két furcsaság van, hanem rendszerszintű zűrzavar? Csináljunk ebből egy részletes auditot.

Gondolj erre úgy, mint egy belső könyvvizsgálatra — csak ahelyett hogy te néznéd végig kézzel mind a 27 fájlt és hasonlítanád össze a számokat, az AI csinálja meg 5 perc alatt.

## Feladat

Kérd meg a Claude-ot, hogy hasonlítsa össze a különböző adatforrásokat és listázza ki az **ÖSSZES** inkonzisztenciát, hiányosságot, és kérdéses adatot.

### Javasolt prompt:

> "Nézd végig az összes fájlt a TransOffice mappában. Hasonlítsd össze az adatokat egymással: ügyféllista vs ügyféllista, árbevételi számok, árak, beszállítói információk. Listázd ki minden inkonzisztenciát, eltérést, és hiányosságot amit találsz. Minden tételnél jelöld meg: melyik fájlban van, mi az eltérés, és kinek kellene feltenni a kérdést hogy melyik az igazi adat."

## Elvárt kimenet

Egy `audit_inkonzisztenciak.md` ami tartalmazza:

### 1. Adateltérések
| # | Adat | Fájl A | Fájl B | Eltérés | Kérdés |
|---|------|--------|--------|---------|--------|
| 1 | Cégnév | ugyfelek_2019.xlsx | ugyfelek_VEGLEGES.xlsx | "Hegyi & Társa" vs "Hegyi és Társai" | Melyik a hivatalos? → Kérdezd Mártont |
| 2 | Árbevétel 2022 | eves_jelentes_2022.xlsx | (máshol hivatkozott) | 1.75M vs 1.8M RON | Melyik a végleges? → Kérdezd Enikőt |
| ... | ... | ... | ... | ... | ... |

### 2. Hiányzó adatok
- Mely ügyfelek vannak a 2019-esben de nincsenek a 2022-esben? (Elmentek? Elfelejtették?)
- Az ugyfelek_uj_marton.xlsx-ben miért csak 8 ügyfél van? A többi 32 nem aktív?
- stb.

### 3. Elavult információk
- arak_2023.xlsx → 2 éves árak
- keszlet_aktualis.xlsx → 3 hónapja nem frissült
- szallitok_lista_regi.xlsx → 3/8 beszállító halott

### 4. Nyitott kérdések (to-do)
| Kérdés | Kitől | Prioritás |
|--------|-------|-----------|
| Hegyi & Társa pontos neve? | Márton / Hegyi Zoli | Alacsony |
| Árbevétel 2022 melyik a helyes? | Enikő (könyvelő) | Magas |
| BicoToner: 15% vagy 12% a kedvezmény? | Szerződés vs számla → jogi kérdés | Magas |

## Hogyan csináld

1. A CLAUDE.md-t már beállítottad (Feladat 1.2), tehát a Claude tudja a kontextust
2. Egy új chatben add ki a fenti promptot
3. Ha a Claude nem talál meg mindent: "Van-e még eltérés amit nem említettél? Nézd meg az árbevételt is."
4. Az eredményt mentsd el a projekt mappába

## Tanulás

- Az AI nem csak összefoglal — **ellenőriz és validál**
- Ez a "második szempár" effektus: amit te nem vennél észre, ő 3 másodperc alatt megtalálja
- Valós üzleti érték: audit, compliance, adattisztaság → mind AI-feladat lehet
