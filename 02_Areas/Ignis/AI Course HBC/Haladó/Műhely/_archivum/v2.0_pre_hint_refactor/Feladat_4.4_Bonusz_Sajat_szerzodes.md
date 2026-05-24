# (Bónusz) Feladat 4.4 — Saját szerződés deep-check

## Szituáció

Az F4.1-ben láttad ahogy a Cowork **30 másodperc alatt megtalál** egy elrejtett kockázatot a bérleti szerződésben (Béla bácsi cross-document referencia). De ez nem TransOffice-specifikus — minden szerződésednek **van rejtett kockázata**.

Itt az ideje saját szerződésed Cowork elé tenni.

## Feladat

Válassz egy olyan szerződést, amelyhez **valóban szeretnéd egy második véleményt**:

- Munkavállalói szerződésed
- Bérleti szerződésed (lakás vagy iroda)
- Beszállítói szerződésed
- Egy klauzulás megbízási szerződés
- Egy biztosítási kötvény
- Apartman társasházi rend (regulament)

> **⚠️ Fontos:** Ne tegyél ki közvetlenül érzékeny adatokat (TB-szám, bankszámla, lakcím). Ha kell, először lehúzod őket egy szerkesztővel. **A Cowork lokálisan dolgozik, de jó szokás óvatosnak lenni.**

### Javasolt prompt:

> "Itt egy [bérleti / munkavállalói / beszállítói] szerződésem. Olvasd el alaposan és:
>
> 1. Sorold fel a **TOP 5 legkockázatosabb** záradékot az ÉN szempontomból (mint [bérlő / munkavállaló / vevő])
> 2. Minden kockázathoz add meg: **mit jelent egyszerűen + mi a worst case + mit lehetne tárgyalni**
> 3. Van-e olyan klauzula ami **románul / magyarul / angolul írta egyébként homályos** és érdemes lenne kiegészíteni?
> 4. Van-e olyan hiányzó dolog ami **általában benne szokott lenni** egy ilyen szerződésben?
> 5. Végén: 1 mondatos vélemény (zöld / sárga / piros)"

## Elvárt kimenet

`szerzodes_check_[nev].md` — strukturált jelentés:

### Összegzés
- **Általános vélemény:** Sárga (van 3 dolog ami nyugtalan tesz, de nem deal-breaker)

### TOP 5 kockázat
| # | Záradék | Mit jelent | Worst case | Javasolt tárgyalás |
|---|---------|------------|------------|--------------------|
| 1 | Art. 5.3 | „Automatikus megújulás kivéve ha 90 nappal előtte felmondunk" | 1 év újabb elköteleződés ha lekésed | Ezt 30 napra csökkenteni |
| ... | ... | ... | ... | ... |

### Homályos pontok
- "Költségek időszakos felülvizsgálata" — mi az időszak? mi a mérték?

### Hiányzó tipikus elemek
- Force majeure záradék
- Vitarendezés első lépcsője (mediáció)

## Extra kihívás

> "Ha most kellene **újratárgyalnom** ezt a szerződést a partnerrel, írj egy 1 oldalas javaslatlistát (Markdown) amit elküldhetnék neki — udvarias hangnemben, számozott pontokkal, indoklással."

## Tipp

A Cowork **nem helyettesít ügyvédet** — de **megtalálja a kérdéseket** amiket egy ügyvédnek érdemes feltenni. Egy ügyvédi konzultáció ára 100-300 EUR/óra. Egy 5-perces Cowork-előkészítés azt jelenti, hogy az ügyvédnek a fontos részekre fókuszálsz a 100 EUR alatt.

## Tanulás

- Minden szerződés **tartalmaz 3-5 kockázatos pontot**, amit pénzügyileg vagy érzelmileg drágán fizetsz meg ha észre sem veszed
- Az AI itt **első szűrő, nem végső véleményező**
- A "homályos pontok" listája különösen értékes — gyakran épp ezek tudnak konfliktust okozni 2 év múlva
- Az újratárgyalási levél formátum azonnal akcionálható kimenet
