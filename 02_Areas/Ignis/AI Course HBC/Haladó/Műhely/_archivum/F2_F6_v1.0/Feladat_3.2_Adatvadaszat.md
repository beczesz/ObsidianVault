# Feladat 3.2 — Adatvadászat: mit kérnek vs. mink van

## Szituáció

A 3.1-ben kiderült: pályázhatunk. Hargita megye (+15 pont), KKV-státusz oké, valószínűleg pozitív EBITDA, járműflotta részben dokumentált. Márton a kávéval visszaszáguld:

> "Oké, megyünk. De most jön a kemény része — kell 17 dokumentum. A 6. szakaszban van felsorolva. Olvastam, és sokat egyáltalán nem értek. Mi az UBO? Mi a REGES? Hol van bármelyik ezek közül? Anyám tudná, de már visszavonult."

> "Nézzük meg gyorsan: a 17 melléklet közül **mi az amink ténylegesen megvan az F1-ben rendszerezett mappáinkban**, mi az amit **könnyen meg tudunk szerezni**, és mi az ami **probléma lesz**."

## Feladat

Vesd össze a pályázati kiírás 6. szakaszában felsorolt **17 kötelező mellékletet** (M-01 – M-17 + N-01 – N-06 nyilatkozatok) a TransOffice valós helyzetével.

Minden mellékletre adj egy értékelést:
- **🟢 MEGVAN** — fellelhető a TransOffice/ mappában vagy a CLAUDE.md említi
- **🟡 KÖNNYEN BESZEREZHETŐ** — egy email, egy űrlap, egy könyvelői telefon (1-3 nap)
- **🔴 PROBLÉMA** — vagy nincs, vagy nem aktuális, vagy szakember kell hozzá (>1 hét vagy költség)
- **⚪ TISZTÁZANDÓ** — nem világos, hogy létezik-e

## Elvárt kimenet

Egy `mellekletek_gap_analysis.md` fájl:

1. **Vezetői összefoglaló**: hány zöld / sárga / piros van? Mennyi időre lesz szükség?
2. **Strukturált gap táblázat** (17 melléklet + 6 nyilatkozat = 23 sor):

| Kód | Melléklet | Státusz | Hol van / honnan jön | Felelős | Becslési idő |
|-----|-----------|---------|----------------------|---------|--------------|
| M-01 | Cégkivonat | 🟡 | ONRC online portál, 50 RON | Enikő | 1 nap |
| M-05 | Mérleg + EK 2023-24 | 🟢 | rendelesnaplo.xlsx + külső könyvelő | Enikő + külsős | 2 nap |
| M-11 | Járműflotta-leltár | 🔴 | nincs strukturált lista — Attila tudja fejből | Te + Attila | 3-5 nap |
| ... | ... | ... | ... | ... | ... |

3. **Kockázati elemzés**: a 🔴-ek közül melyik veszélyezteti leginkább a beadási határidőt (2025.04.30)?
4. **Kritikus út**: mely mellékletek függenek egymástól (pl. M-13 üzleti terv csak akkor készülhet, ha M-11 járműflotta megvan)?
5. **Költségbecslés**: van-e külső költség (közjegyző, fordító, dealer, könyvelő)?

## Prompt javaslat

```
Olvasd el ismét a pályázati kiírás 6. szakaszát (Kötelező mellékletek). 17 melléklet (M-01 – M-17) 
és 6 nyilatkozat (N-01 – N-06) van.

Vesd össze őket a TransOffice valós helyzetével:
- A CLAUDE.md cégadataival
- A TransOffice/ mappa fájljaival (vannak-e itt szerződések, mérlegek, ügyfélnyilvántartások?)
- Az F2 meeting transcriptjében említett adathiányokkal (járművek "3? 4?", ügyfellistából több verzió, stb.)

Készíts gap analysis táblázatot:

| Kód | Melléklet | Státusz | Hol van / honnan jön | Felelős | Becsléi idő |

Státuszok:
🟢 MEGVAN — már a kezünkben van vagy az F1 mappákban
🟡 KÖNNYEN BESZEREZHETŐ — 1-3 nap, ismert forrásból
🔴 PROBLÉMA — több mint egy hét, vagy jelentős munka, vagy költség
⚪ TISZTÁZANDÓ — nem világos, hogy létezik-e

Add hozzá:
- Vezetői összefoglaló (hány zöld/sárga/piros, becsült teljes idő)
- Top 3 kockázat: melyik melléklet veszélyezteti leginkább a 2025.04.30 határidőt?
- Kritikus út: mely mellékletek függenek másokétól (dependency)
- Külső költségek becslése
```

## Tanulási pont

- A Cowork **két dokumentum-univerzumot** képes egyszerre kezelni: a pályázati kiírást ÉS a teljes TransOffice mappát
- A gap analysis a klasszikus tanácsadói munka **lényege**: mit kérnek vs. mink van — most 5 perc, korábban napok
- Az AI **konkrét fájlnevet ad vissza** ("megvan a `szerzodes_PaperWorld_2021.pdf`-ben"), nem általánosít
- A 🔴 piros státuszok azonnal **TODO listává válnak** az F2 Productivity pluginen keresztül — átadhatjuk Enikőnek, Attilának, Ilonának (telefon)

## Tippek

- A meeting transcript szerint **a járműflotta nem dokumentált pontosan** ("3? 4?") → M-11 és M-12 szinte biztos 🔴
- A **Kovacs_Ilona/** mappa zaja között (200+ fájl) lehet régi cégkivonat, biztosítási papírok — **kérdezd meg az AI-t hogy keresse ki**
- Az **M-13 üzleti terv** önmagában egy projekt — ezt valószínűleg külsős vagy mi magunk írjuk (F4-ben jövőbeli téma)
- A **N-01 KKV-státusz nyilatkozat** triviális (12 fő, ~360k EUR árbevétel), de **N-02 De minimis** komolyabb: az utolsó 3 év állami támogatásait kell előbányászni

## Checkpoint

**WOW (te demózod):**
- Megnyitod a kiírás 6. szakaszát + a TransOffice/ mappát egyszerre
- Egy prompttal: 23 elemes gap táblázat 1 perc alatt
- Punchline: "Itt van 23 sor. Ebből 6 zöld, 11 sárga, 6 piros. Az utolsó 6 elem amit meg kell oldanunk — és pontosan tudjuk, ki, mit, mikorra."

**MICRO HANDS-ON (ők csinálják):**
- Mindenki kiválaszt **EGY** mellékletet a 23-ból
- Saját Coworkban megkérdezi: "ez nálunk megvan? Honnan tudjuk megszerezni?"
- Az AI válaszol — ők értékelik a választ
- 3 perc, az élmény: **konkrét fájlnevekkel válaszol, nem hallucinál**

**FLOW tovább:**
- Visszaülünk, te megmutatod ahogy a 23-as táblát átadhatjuk a Productivity pluginnek
- Minden 🔴-ből és 🟡-ből egy TODO-t generálunk → már F2-re épül
- Átkötés 3.3-ba: "Most rendezzük ezt felelős-határidős akciótervvé."

## Időkeret

- Workshopon: ~8-10 perc (6p demo + 3p hands-on + 1-2p átkötés)
- Cél: a résztvevők értsék meg, hogy **az AI nemcsak a kiírást olvassa, hanem a saját fájljaikat is** — és ez **kombinálva** ad új információt

## Értékelési szempontok (instructor számára)

A résztvevő sikeresen részt vett, ha:
- [ ] Látta, hogy az AI konkrét fájlra hivatkozik (pl. "rendelesnaplo.xlsx alapján…")
- [ ] Felismeri a státuszrendszer logikáját (zöld/sárga/piros/⚪)
- [ ] Megtapasztalta, hogy egy 🔴-ből hogyan lesz konkrét TODO
- [ ] Az "1 melléklet hands-on"-t megcsinálta
