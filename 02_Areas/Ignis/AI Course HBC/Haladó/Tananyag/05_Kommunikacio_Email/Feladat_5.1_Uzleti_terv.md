# Feladat 5.1 (Stáció 5.A) — Form-katalogizáló

> **Típus:** ⏸ STÁCIÓ — saját laptopon, copy-paste prompt
> **Idő:** ~5 perc · **Mód:** egyénileg
> **MEGJEGYZÉS:** Korábbi v1.0-ban ez egy DEMO volt (Plan de afaceri). v2.0-ban átkerült stációra — a Plan de afaceri DEMO az oktatóé marad. A te dolgod itt a **form-katalogizáló**.

---

## Szituáció

Az oktató épp megmutatta:
1. Hogyan generált a Cowork **teljes Plan de afaceri**-t (románul, 260 sor)
2. Hogyan állított össze egy **23 tételes** pályázati csomag-checklistet

Most jön a **MySMIS form** — a pályázati portál űrlapja, 40 mező románul. **De mielőtt** látnánk hogyan tölti ki a Cowork, **ti** előbb megtanuljátok **AI-val összefoglalni egy formot**.

---

## A stáció prompt

A `formular_depunere_AFM_Mobilitate_Verde.html` fájl mindenkinek elérhető a `Tananyag/05_Kommunikacio_Email/` mappában.

Másold ki és illeszd be a saját Cowork-jébe:

```
Itt a pályázati formunk: formular_depunere_AFM_Mobilitate_Verde.html

Nyisd meg, és listázd ki az ÖSSZES mezőt kategória szerint csoportosítva
(pl. Cégadatok, Pénzügy, Projektleírás, Mellékletek). Minden mezőhöz írd:
- kötelező-e
- milyen formátumban kell kitölteni (szöveg / szám / dátum / fájl)

A kimenet egy strukturált tábla legyen.
```

---

## Elvárt eredmény

A Cowork 60-90 másodperc alatt:
- Megnyitja a `formular_depunere_AFM_Mobilitate_Verde.html`-t
- Megszámolja a mezőket — kb. **40 db** összesen
- **Kategóriákba** csoportosítja (Cégadatok, Pénzügy, Projektleírás, Mellékletek, stb.)
- Minden mezőre: **kötelező-e**, **formátum**, **típus**
- Egy strukturált .md-tábla a kimenet

---

## Miért ez a stáció

**Egy üzleti életben** sose írunk pályázatot az adott pillanatban a kiírásra:
- **Először** megtudjuk **mire kell** felkészülni — ez a katalogizáló-lépés
- **Aztán** összegyűjtjük az adatokat
- **Végül** kitöltjük

A Cowork-kel ez a **lépcsőzetes előkészítés** percekben elvégezhető — bármilyen pályázati / űrlap / RFP esetén.

---

## Tipp

Ha a Cowork **rosszul számolja a mezőket** (pl. egy radio-button-csoportot 1-nek vesz a 4 helyett), kérdezz vissza: *„Nézd meg a HTML forrását, és minden `<input>`, `<select>`, `<textarea>` egy-egy mező."*

---

## Otthoni elmélyítés

Saját formjaiddal — bónusz feladatok:
- `Feladat_5.5_Bonusz_Form_validacio.md` — saját kitöltött form validáció
- `Feladat_5.7_Bonusz_Cover_letter.md` — kísérőlevél pályázati tanácsadónak

---

**Verzió:** 2.0 (Stáció modell — átalakult Plan de afaceri-ról form-katalogizálóra)
