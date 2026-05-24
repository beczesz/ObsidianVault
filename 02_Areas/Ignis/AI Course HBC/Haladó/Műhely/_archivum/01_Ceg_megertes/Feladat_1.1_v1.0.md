# Feladat 1.1 — Átlátni a rendszert

## Szituáció

Márton reggel odajön hozzád a második kávéddal:

> "Figyelj, elfelejtettem mondani tegnap — csütörtökön lesz egy meeting egy pályázati tanácsadóval. Valami AFM-es elektromos járműflotta pályázat, elég sok pénz. De ahhoz hogy értelmes dolgokat mondjak neki, tudnom kéne mi a helyzet a cégnél rendszer-szinten. Te tegnap óta nézegetted a fájlokat ugye? Tudnál nekem egy gyors összefoglalót csinálni? Olyan 1-2 oldalas, amit elolvasok meeting előtt. Ilyesmi kellene: hány ügyfelünk van, mennyi a forgalom, milyen rendszereink vannak (vagy nincsenek), mik a fő problémák. Ha találtál valami furcsát is, azt is írd bele. Csütörtökig van időd, szóval nem kell most rögtön, de ha ma meg tudod kezdeni, szuper."

## Feladat

Nézd át a `TransOffice/` mappa teljes tartalmát a Claude Cowork segítségével, és készíts egy **strukturált összefoglalót** Márton számára.

## Elvárt kimenet

Egy `ceg_attekintes.md` fájl ami tartalmazza:

1. **Cég alapadatok** — mit csinálunk, hol, hányan vagyunk
2. **Ügyfélkör** — hány aktív ügyfelünk van, kik a legnagyobbak, milyen szegmensek
3. **Pénzügyi helyzet** — árbevétel, trend (nő/csökken/stagnál?)
4. **Jelenlegi rendszerek** — hogyan működik az admin most (email, Excel, papír)
5. **Beszállítók** — kik, milyen feltételekkel, van-e probléma
6. **Azonosított problémák** — inkonzisztenciák, hiányosságok, kockázatok
7. **Javaslat** — 3-5 prioritás amit a pályázatban érdemes lenne megcélozni

## Hogyan csináld (javasolt megközelítés)

1. Nyisd meg a Claude Cowork-öt
2. Csatold a `TransOffice/` mappát (vagy adj hozzáférést a Cowork-nek)
3. Kérd meg a Claude-ot hogy nézze át a fájlokat és készítsen összefoglalót
4. Iterálj: kérdezz rá a részletekre, kérd hogy mélyebben vizsgálja meg amit talál

## Tippek

- Ne próbáld egyedül kézzel átnézni mind a 30+ fájlt — pont ez az AI lényege
- A Claude képes Excel fájlokat olvasni, Word dokumentumokat értelmezni, szövegfájlokat feldolgozni
- Ha a Claude kérdez (pl. "melyik ügyféllistát tekintsem mérvadónak?"), gondolkodj el — épp ezt tanulod

## Időkeret

- Kurzuson: ~20-25 perc (a master plan szerint)
- A cél NEM a tökéletes dokumentum, hanem az élmény: "erre kellett volna 2 nap, és 30 perc alatt kész"

## Értékelési szempontok (instructor számára)

A résztvevő sikeresen teljesítette ha:
- [ ] A Claude-ot használta a fájlok áttekintésére (nem kézzel olvasta)
- [ ] A kimenet strukturált és olvasható
- [ ] Legalább 1 inkonzisztenciát azonosított (árbevétel / ügyfélszám / néveltérés)
- [ ] A javaslatai relevánsak és a fájlokból következnek
