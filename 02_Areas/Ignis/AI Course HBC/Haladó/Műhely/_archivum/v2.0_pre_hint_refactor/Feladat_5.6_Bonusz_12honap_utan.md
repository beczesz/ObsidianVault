# (Bónusz) Feladat 5.6 — 12 hónapos megvalósítási terv (ha megnyerjük)

## Szituáció

Tegyük fel: **megnyerjük a pályázatot**. 200.000 EUR támogatás 5 elektromos járműre. Január 1-jén megérkezik az értesítés. **Most mit csinálsz?**

A legtöbb cég pánikba esik ebben a pillanatban: a pénz **kötött**, az időkeret **rögzített**, az elszámolási követelmények **drákóiak**. Aki nem készül elő, **6 hónap múlva pénzügyi katasztrófában találja magát**.

A Cowork-kel **a beadás napján** kész egy 12-hónapos megvalósítási terv.

## Feladat

Készíts egy projekt-tervet a teljes megvalósítási időszakra:

### Javasolt prompt:

> "Tegyük fel hogy a pályázatot megnyerjük: 200.000 EUR támogatás 5 elektromos járműre + 2 töltőpontra, 18 hónapos megvalósítási időszakkal.
>
> Készíts egy **havi bontású, részletes projekt-tervet**, ami tartalmazza:
>
> **1. Hónap-szerinti milestone-ok** (Gantt-stílus szöveges leírás)
> - Mit kell elvégezni / dokumentálni hónap végéig
> - Mi a kritikus út (CP)
>
> **2. Cash flow terv havi bontásban**
> - Mikor érkezik a támogatás (előleg, részletek)
> - Mikor megy ki saját önerő
> - Hol vannak likviditási kockázatok
>
> **3. Beszerzési ütemezés**
> - Mikor kell megrendelni a 5 járművet
> - Töltőpont telepítés (telephely-tulajdonossal egyeztetés!)
> - Versenyeztetés / közbeszerzés ha kell
>
> **4. Compliance és dokumentáció**
> - Negyedéves jelentések
> - Fotódokumentáció követelmények
> - Auditra való felkészülés
>
> **5. Kockázatok és intervallumok**
> - Hol érdemes 'buffer időt' tartani
> - Mely lépéseknél kellhet pl. ügyvédet bevonni"

## Elvárt kimenet

`projekt_terv_18honap_AFM.md`:

### Hónap-bontás (M1-M18)

**M1 — 2025-07:** Szerződéskötés az AFM-mel + bankgarancia bejelentés + első jármű-szállító kiválasztása
**M2 — 2025-08:** 5 jármű megrendelése + szerződéses előleg utalása + töltőpont engedélyezési eljárás indítása
**M3 — 2025-09:** Első 2 jármű átvétele + személyzeti képzés a használatra
[... folytatás M18-ig]

### Cash flow terv

| Hónap | Bevétel (támogatás) | Kiadás | Nettó | Likviditási bufferünk |
|-------|---------------------|--------|-------|----------------------|
| M1 | 0 | -8.000 | -8.000 | 50.000 |
| M2 | 80.000 (előleg) | -45.000 | +35.000 | 85.000 |
| ... | ... | ... | ... | ... |

### Beszerzési ütemezés
[Detailed timeline]

### Compliance checklist
[Quarterly checks]

### Risk-mitigated milestones
[Buffer points + escalation triggers]

## Extra kihívás

> "A 18-hónapos terv alapján: ki a 3 ember akinek az ÉN cégemnél (TransOffice) a következő 18 hónapban a legtöbb extra munkája lesz? Mit tegyek hogy ne legyen burn-out?"

Ez a humán-oldal — amit az AI tervek gyakran kihagynak, de gyakorlatban itt törik el a projekt.

## Tipp

A megvalósítási terv **élő dokumentum** — érdemes a Cowork Productivity plugin-nel naprakészen tartani. Minden hónap végén:
- "Mit tettem meg ebből a hónapból?"
- "Mit csúszott?"
- "Hova kell beavatkozni?"

## Tanulás

- A megnyert pályázat **csak a kezdet** — a megvalósítás 80% a projekt sikerének
- A "minden a fejemben van" mentalitás itt **veszélyes** — a Cowork strukturál
- A cash flow tervezés különösen kritikus: **80% a támogatás az ELSZÁMOLÁS után érkezik**, nem előre
- A humán-oldal a kockázatok közül a leggyakrabban kihagyott pont
