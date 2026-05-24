# (Bónusz) Feladat 5.5 — Pályázati form ön-validáció

## Szituáció

Az F5.3-ban kitöltöttük a pályázati formot — de a beadás előtti **utolsó 10 percben** mindig van egy stresszes pillanat: "tényleg jó minden? semmit sem felejtettem el? a szám-mezők stimmelnek?"

A pályázati portálok rugalmatlanok: ha egy mezőben elgépelsz, a rendszer **visszadob** és minden el van veszve. A Cowork **átnézi és ellenőrzi**, mielőtt a Submit gombot megnyomod.

## Feladat

Tedd a Cowork elé a kitöltött pályázati form-tartalmat (vagy egy export-ot a portálból), és kérj egy alapos ön-validációt.

### Javasolt prompt:

> "Itt van a kitöltött pályázati form-om (`palyazat_form_kitoltott.md`). Kérlek játszd el a **bírálati előellenőrzés** szerepét:
>
> 1. **Adatkonzisztencia** — ahol ugyanaz a szám szerepel többször, egyezik-e? (CUI, alkalmazottak száma, árbevétel)
>
> 2. **Logikai ellenőrzés** — a számok elvileg helyesek-e? (Pl. profit ≤ árbevétel - költség. Önerő + támogatás = összköltség. Új járművek db × ár = összköltség.)
>
> 3. **Hiányzó mezők** — van-e mező amit üresen hagytam vagy 'N/A'-val töltöttem ki, de tartalom kellene?
>
> 4. **Formátum hibák** — telefonszámok, dátumok, IBAN egységes formátum? Ékezetek helyesek?
>
> 5. **Eligibility kockázatok** — van-e mező amit kitöltöttem de **valószínűleg pontot veszítek érte** vagy diskvalifikáló?
>
> 6. **Mellékletek kompatibilitása** — amit a form-ban állítok, megerősíti-e a feltöltött Excel és üzleti terv?
>
> Adj egy **piros/sárga/zöld jelzést** mindegyik kategóriához, és sorold fel a top 3 dolgot amit változtassak BEADÁS ELŐTT."

## Elvárt kimenet

`palyazat_validacio_riport.md`:

### Összegzés
- 1. Adatkonzisztencia: 🟢 Zöld
- 2. Logikai ellenőrzés: 🟡 Sárga (lásd: alkalmazotti adó számítás)
- 3. Hiányzó mezők: 🟢 Zöld
- 4. Formátum: 🟡 Sárga (lásd: dátum formátum)
- 5. Eligibility: 🟢 Zöld
- 6. Mellékletek: 🔴 Piros (lásd: a form-ban 7M RON árbevétel, az Excel-ben 1.8M)

### Top 3 dolog BEADÁS ELŐTT

1. **🔴 KRITIKUS — Árbevétel eltérés:** Form szerint 7M, az Excel-ben 1.8M → ez egy elgépelés (7M valószínűleg 1.7M kellene)
2. **🟡 Logikai — Alkalmazotti adó:** A "salarii brutte" mező 350k RON, de a "contributii" csak 56k → ennek 100k körül kellene lennie. Ellenőrizd a Mihaela számokkal.
3. **🟡 Formátum — Dátumok:** "15.06.2025" és "15/06/2025" keverve. Pályázati portálok általában csak az egyiket fogadják el.

### Részletes jelentés mezőnként
[mezőrőll mezőre]

## Extra kihívás

Egy második prompt a validáció után:
> "Most simulálj egy szigorú bírálót aki MIND a 100 pontot meg akarná dobni rólunk. Mit kérdezne, mit kifogásolna? Adj 5 ilyen kifogást — hadd lássam mire kell felkészülnöm."

## Tipp

**Ezt a validációt soha ne hagyd ki** — minden 200 EUR-os pályázati tanácsadó ezt csinálja az utolsó fázisban, és **itt menthető meg az egész pályázat**. A Cowork ugyanezt 5 percben megcsinálja.

**Mindig** mentsd el a validáció riportot — ha a pályázatot esetleg elutasítják, ebből látod **hol vesztettünk**.

## Tanulás

- Az AI mint **harmadik szempár** — nem az aki kitölti, hanem aki utánanéz
- A leggyakoribb pályázati elutasítási ok: **technikai hiba** (formátum, ellentmondás, hiányzó mező) — NEM tartalmi
- A "bíráló-szimuláció" extra kihívás = elővételezett védelem
- Ez az **utolsó 5 perc** ami eldönti a pályázat sorsát, és most automatizálható
