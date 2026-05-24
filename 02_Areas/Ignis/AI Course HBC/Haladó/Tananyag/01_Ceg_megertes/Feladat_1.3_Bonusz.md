# (Bónusz) Feladat 1.3 — Inkonzisztenciák listája

## Szituáció

Márton megemlítette: "Ha találtál valami furcsát, azt is írd bele." De mi van ha nem csak egy-két furcsaság van, hanem rendszerszintű zűrzavar? Csináljunk ebből egy részletes auditot.

Gondolj erre úgy, mint egy belső könyvvizsgálatra — csak ahelyett hogy te néznéd végig kézzel mind a 27 fájlt és hasonlítanád össze a számokat, az AI csinálja meg 5 perc alatt.

## Feladat

Kérd meg a Claude-ot, hogy hasonlítsa össze a különböző adatforrásokat és listázza ki az **ÖSSZES** inkonzisztenciát, hiányosságot, és kérdéses adatot.

## Hint

Indulj egy nyitott kérdéssel — kérd meg a Cowork-öt, hogy hasonlítsa össze a fő adatforrásokat (3 ügyféllista, pénzügyi számok, beszállítói infók) és emeljen ki minden inkonzisztenciát. Ha tetszik a kimenet, iterálj: kérd hogy minden tételhez adjon felelős-ajánlást.


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
