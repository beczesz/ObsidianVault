# Feladat 3.1 — Eligibility check: pályázhatunk-e egyáltalán?

## Szituáció

Másnap reggel. Márton már 7-kor az irodában. Kávé, laptop, az asztalon a kinyomtatott pályázati kiírás 94 oldala — a margón már kis kockás betűk, áthúzások, nyilak.

> "Figyelj, egész éjjel ez járt a fejemben. Ha ennek nincs értelme, ne is kezdjünk bele — ne pazaroljuk Enikő idejét sem. De ha tényleg pályázhatunk, akkor azonnal indulunk. Nézd meg gyorsan: van itt 12 kritérium, és nekünk azt kell tudnunk, hogy mind a 12-nek megfelelünk-e. Ha akár egy is nem stimmel — vége. Ha mind oké — futunk."

> "Tegnap megvan a TODO listánk az F2-ből, megvan a CLAUDE.md-d az F1-ből a cég adataival. Tegyél fel egy egyszerű kérdést: pályázhatunk-e?"

## Feladat

Olvastasd be a pályázati kiírást (`Palyazat_kiiras/Ghidul-solicitantului-Mobilitate-Verde-IMM-2025.md`) és vesd össze a TransOffice cégadataival (F1 CLAUDE.md + a `TransOffice/` mappa fájljai).

A 12 eligibility kritérium (CR-01 – CR-12) mindegyikére adj egy egyértelmű választ:
- **✅ TELJESÜL** (és miért, melyik fájl alapján)
- **⚠️ RÉSZBEN / KOCKÁZATOS** (mi hiányzik, mit kell tisztázni)
- **❌ NEM TELJESÜL** (és ez véglegesen kizár-e, vagy lehet rajta változtatni)

## Elvárt kimenet

Egy `eligibility_check.md` fájl ami tartalmazza:

1. **Vezetői összefoglaló** (3-5 mondat): pályázhatunk-e? Igen / Részben / Nem.
2. **12 kritérium táblázat**: kritérium → státusz → indoklás → forrásfájl
3. **Stoppolók (deal-breakers)**: ha van olyan kritérium, ami véglegesen kizár, az legyen kiemelve
4. **Tisztázandók (clarifications)**: amelyiknél nem egyértelmű, és pontosan mit kell ellenőrizni
5. **Pontozási becslés**: a 8. szakaszban lévő értékelési pontrendszer alapján — hol állunk várhatóan? (CO2-megtakarítás, pénzügyi stabilitás, földrajzi bónusz, stb.)
6. **Javaslat**: érdemes-e pályázni az adott helyzetben

## Prompt javaslat

```
Olvasd át a pályázati kiírást: Palyazat_kiiras/Ghidul-solicitantului-Mobilitate-Verde-IMM-2025.md.

A 4. szakaszban van 12 eligibility kritérium (CR-01 – CR-12). Vesd össze ezeket a TransOffice 
adataival, amik a CLAUDE.md-ben és a TransOffice/ mappában megtalálhatók.

Készíts egy strukturált eligibility check riportot:

1. Vezetői összefoglaló: pályázhatunk-e? (Igen / Részben / Nem) — 3-5 mondat
2. Részletes táblázat mind a 12 kritériumra:
   | Kritérium | Státusz (✅/⚠️/❌) | Indoklás | Forrás |
3. Stoppolók: van-e olyan kritérium, ami biztosan kizár?
4. Tisztázandók: mire kell még adatot szerezni?
5. Pontozási becslés a 8. szakasz alapján (max 100 pont, min 60 kell)
6. Záró ajánlás: induljunk-e?

Ha valamelyik adat hiányzik a cégfájlokból, jelezd — ne találd ki.
```

## Tanulási pont

- A Cowork **kombinálja** a friss dokumentumot (pályázati kiírás) a perzisztens cégadatokkal (CLAUDE.md, korábbi fájlok)
- Az AI nem találja ki az adatokat — **megmondja, ha valami hiányzik**, és ezzel azonosítja a következő lépést
- A pályázat-elbírálás 30%-a tisztán formai ellenőrzés. A Cowork ezt a 30%-ot 5 perc alatt elvégzi.
- **Ez nem pályázatírás. Ez döntéstámogatás:** "érdemes-e elindulni?" — és ha nem, **most spórolunk meg napokat**.

## Tippek

- A Hargita megyei székhely **automatikus +15 pont** (8.4. szakasz) — ezt mindenképp építsd be
- A **"Stagnálás 2015-2022" + Márton átvette 2023** kombinációból nézd: van-e pozitív EBITDA legalább egy évben? (CR-05)
- A meeting transcriptben Márton említette: "három, négy autó… nem tudom pontosan" — ez **CR-08 (járműflotta dokumentáltsága) kockázat**
- A De minimis (CR-06) küszöb **közúti fuvarozásnál** csak 100k EUR — kérdezd meg az AI-tól, **alkalmazható-e** ez a TransOffice-ra (logisztikai cég de fő tev. kereskedelem)

## Checkpoint

**WOW (te demózod):**
- Megmutatod, ahogy a Claude 30 másodperc alatt elolvassa a 94 oldalas kiírást
- Még 30 mp és kihúzza a 12 kritériumot
- Még 1 perc és összeveti a TransOffice adataival
- Az output: egy strukturált igen/nem válasz **indoklással**
- Punchline: "Ezt egy könyvelő 2-3 nap alatt csinálná meg. Most 2 perc volt."

**MICRO HANDS-ON (ők csinálják):**
- Mindenki kiválaszt **EGY** kritériumot (pl. "CR-08 — járműflottánk dokumentált?")
- Megkérdezi a saját Cowork session-jében: "ez a kritérium teljesül a TransOffice-ra?"
- Az AI válaszol → ők értékelik: meggyőző-e? Hol bizonytalan?
- 3 perc, és az élmény: **én is meg tudom kérdezni**

**FLOW tovább:**
- Visszaülünk, megmutatod a végső eligibility riportot
- Átkötés a 3.2-be: "Oké, pályázhatunk. De akkor most 17 dokumentumot kell összeszednünk."

## Időkeret

- Workshopon: ~8-10 perc (6 perc demo + 3 perc mikro hands-on + 1-2 perc átkötés)
- A cél NEM az, hogy mindenki kapjon egy tökéletes riportot — a cél: **mindenki érezze, hogy 94 oldalas dokumentum + cégadatok = AI 2 perc alatt eldönti**

## Értékelési szempontok (instructor számára)

A résztvevő sikeresen részt vett, ha:
- [ ] Megnyitotta a pályázati kiírást és látta a 12 kritériumot
- [ ] Megtapasztalta, hogy az AI a saját CLAUDE.md-ből hozza a cégadatokat (nem találja ki)
- [ ] Felismeri, hogy az AI **jelez, ha hiányzik adat** — nem hallucinál
- [ ] Az "1 kritérium hands-on"-t megcsinálta
