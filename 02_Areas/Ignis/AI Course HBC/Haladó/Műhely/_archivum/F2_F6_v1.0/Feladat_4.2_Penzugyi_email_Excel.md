# F4.2 — Pénzügyi adatok: könyvelő email + Excel feldolgozás

## Kontextus
A Data Completion Board-ból kiderült, hogy a pályázathoz pénzügyi adatok kellenek: árbevétel, alkalmazotti létszám, EBITDA. A meeting transcriptben Enikő mondta: *"a legfrissebb számok még nincsenek összerakva teljesen. A tavalyi megvan, de az idei… hát…"*

A külsős könyvelőt nehéz elérni — email talán. De mit írjunk neki? És ha válaszol egy Excel-lel, mit csinálunk vele?

## Feladat

### 1. lépés — Email a könyvelőnek
Kérd meg a Claude-ot, hogy írjon emailt a külsős könyvelőnek. Legyen benne konkrétan:
- Mire kell (AFM Mobilitate Verde pályázat)
- Milyen adatok kellenek (árbevétel, eredménykimutatás, alkalmazotti létszám, EBITDA)
- Milyen formátumban (Excel, aláírt PDF)
- Mikorra (határidő: 5 munkanap)

```
Írj egy emailt a külsős könyvelőnknek (Ionescu Mihaela, kontaktus: mihaela.ionescu@contabilpro.ro).
A TransOffice Trade SRL pályázatot ad be az AFM Mobilitate Verde programra.
Kérjük tőle:
1. Utolsó lezárt éves mérleg (bilant) és eredménykimutatás — aláírt PDF
2. Alkalmazotti létszám igazolás (declaratie)
3. EBITDA kalkuláció az utolsó 2 évre
Határidő: 5 munkanap. Hangnem: udvarias, professzionális, románul.
```

### 2. lépés — Excel feldolgozás (demo)
Az oktató bemutatja: "Megérkezett Mihaela válasza egy Excel-lel." A `TransOffice/` mappából betöltjük az `arak_2023.xlsx`-et (vagy egy pénzügyi adatokat tartalmazó xlsx-et), és a Claude-dal feldolgozzuk:

```
Nézd meg ezt az Excel fájlt és mondd meg:
1. Az éves árbevétel megfelel-e az AFM kritériumnak (max 50M EUR / IMM kategória)?
2. Van-e benne elég adat az EBITDA kiszámításához?
3. Mi hiányzik még?
```

## Tanulási pont
- Az AI specifikus, célzott emailt ír — nem generikus "kérjük az adatokat"
- Az Excel feldolgozás mutatja: a Cowork nemcsak szöveget ért, hanem táblázatokat is
- A könyvelő emailjének románul kell lennie — az AI nyelvváltása természetes

## Időkeret
~10-12 perc

## Checkpoint
**WOW:** Egy prompt → kész email románul a könyvelőnek, pontos kérésekkel
**MICRO HANDS-ON:** Változtasd meg a határidőt vagy adj hozzá egy plusz kérést — nézd meg hogyan módosul az email
