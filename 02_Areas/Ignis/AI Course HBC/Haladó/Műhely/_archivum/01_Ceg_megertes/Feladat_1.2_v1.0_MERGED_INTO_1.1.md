# Feladat 1.2 — CLAUDE.md: A cég memóriája

## Szituáció

Elkészítetted az összefoglalót Mártonnak. Szuper munka. De most csukd be a Claude-ot és nyisd meg újra.

...

Üres. Nem emlékszik semmire. Fogalma sincs ki a TransOffice, ki vagy te, vagy mi történt az előbb.

**Ez az AI legnagyobb korlátja: nincs hosszútávú memóriája.**

Hacsak... nem adsz neki egyet.

---

## A CLAUDE.md koncepciója

A Claude Cowork-ben van egy speciális fájl: `CLAUDE.md`. Ha ez létezik a mappádban, a Claude **minden új beszélgetés elején automatikusan elolvassa**. Olyan mint egy "briefing" amit minden reggel kap az AI, mielőtt elkezd dolgozni.

### Miért fontos ez?

| CLAUDE.md nélkül | CLAUDE.md-vel |
|------------------|---------------|
| Minden chatben elölről kell elmagyarázni ki vagy | Azonnal tudja a kontextust |
| "Nézd meg a fájlokat" → újra 5 perc mire érti | Már tudja melyik fájl micsoda |
| Nem emlékszik a döntésekre | Emlékezik a szabályokra, preferenciákra |
| Csak annyira jó amennyit megmondasz neki | Proaktívan tud segíteni |

### Hasonlat

Képzeld el hogy minden reggel egy új gyakornok jön be az irodába. Okos, gyors, de nem ismeri a céget. A CLAUDE.md az az "onboarding dokumentum" amit az első percben elolvas és rögtön hatékonyan tud dolgozni.

---

## Feladat

Készíts egy `CLAUDE.md` fájlt a projekt mappájában (oda ahol a TransOffice mappa is van). Használd az előző feladat eredményét (ceg_attekintes.md) mint kiindulópontot.

### A CLAUDE.md tartalmazzon:

```markdown
# TransOffice Trade SRL — Kontextus

## Rólam
[Ki vagy te a cégnél? Mi a szereped?]

## A cég
[1-2 mondat: mit csinálunk, hol, mekkora]

## Csapat
| Név | Szerep | Fontos tudnivaló |
|-----|--------|------------------|
| ... | ... | ... |

## Ügyfelek (top 5-10)
[Akikkel a legtöbbet foglalkozunk]

## Aktív problémák / Prioritások
[Amit most kell megoldani]

## Szabályok
[Amit a Claude-nak mindig szem előtt kell tartania]
- pl. "A BicoToner szerződés problémás — mindig jelezd ha releváns"
- pl. "Orbán Csilla ügyvédnő kényes ügyfél — extra figyelem"
- pl. "Árak: az arak_2023.xlsx ELAVULT, ne hivatkozz rá mint aktuálisra"
```

## Hogyan csináld

1. Nyisd meg a Claude Cowork-öt
2. Mondd neki: *"Készíts egy CLAUDE.md fájlt az előző összefoglalónk alapján. Ez lesz a te memóriád — minden új chatben ezt fogod elolvasni először."*
3. Nézd át az eredményt és iterálj: adj hozzá amit fontosnak tartasz

## Demonstráció (instructor mutatja)

Miután a CLAUDE.md kész:
1. **Zárd be a chatet** (új beszélgetés)
2. Nyiss egy teljesen új ablakot
3. Írj be valamit mint: *"Mi a helyzet a BicoToner szerződéssel?"*
4. **A Claude azonnal tudni fogja** — nem kell kontextust adnod!

→ Ez a "mágikus pillanat" amit a résztvevőkkel meg kell éltetni.

## Időkeret

- Kurzuson: ~15-20 perc
- Ebből 5 perc elmagyarázni MIÉRT, 10 perc megcsinálni, 5 perc demonstrálni

## Tanulás

- **Context engineering** = az AI hatékonyságának kulcsa
- Nem elég jó promptokat írni — jó kontextust kell adni
- A CLAUDE.md egy "élő dokumentum" — ahogy tanulsz új dolgokat a cégről, beleírod
- Ez a különbség a "néha használom az AI-t" és az "AI-asszisztensem van" között

## Értékelési szempontok

- [ ] Létrehozta a CLAUDE.md-t
- [ ] A tartalom releváns és tömör (nem 5 oldal, nem 3 sor)
- [ ] Demonstráció sikeres: új chatben a Claude "emlékszik"
- [ ] A résztvevő érti MIÉRT működik (nem mágia, hanem fájl-olvasás)
