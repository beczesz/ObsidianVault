---
title: "VG (Variation Group) tartalom specifikáció — 15 termék × 5 opció-típus"
description: "Specifikáció a backend-szintű tartalmához és adatmodelljéhez 15 termék 5 opció-típusára; tartalmazza a másolat, modális képi leírások és séma-definíciókat magyar és román nyelveken, valamint az opció-érték árazási szabályait és UI-megjelenítési logikáját."
description_source: auto
description_hash: 5f0f77c7e81dad6f
version: 1.1 DRAFT
date: 2026-05-09
author: Szabolcs (Exar Labs) + Cowork
status: REVIEW — Szabolcs javítja, majd Jira ticket frissítés
parent_spec: "product-variations-spec-v1.0.md"
parent_matrix: "product-options-matrix-v1.0.md"
wireframe: "design/screen-catalog/screens/v0.4-product-variations.html"
changelog:
  v1.0: "Első draft — 6 opció-típus, opt-in default modell."
  v1.1: "Pácolatlan érték drop (OFF = pácolatlan). Forma → Szeletelés (forma) Normál/Dupla. Vastagság + Szeletelés (egész/szeletelt) merge → Szeletelés (Vékony/Normál/Vastagabb). Méret és Zsírosság MANDATORY (no checkbox)."
  v1.2: "Price modifier mező hozzáadva — Pácolás +2 RON/kg, többi érték ingyenes. UI badge a radio mellett. Cart subtotal külön sor 'Felárak' címen."
id: 9f424e44-e550-43c5-b88e-49b3577f4cdc
index_schema_version: 1
---
# VG tartalom specifikáció v1.1

> **Cél:** Minden VG (Variation Group) és opció-érték backend-szintű tartalma, beleértve a copy-t (HU + RO) és az info modal tartalmát (kép-leírás + szöveg).
>
> **Hogyan használd:** Olvasd át, javítsd a copy-t és a default kapcsolásokat, majd a §8-as táblázatból generáljuk a backend seed adatokat és a Jira sub-tasks-okat. A tech stack és konkrét adatmodell-megvalósítás a fejlesztő döntése — az alábbi mező-leírások a schema v1.2 JSON struktúráját tükrözik, nem egy konkrét keretrendszer típusait.

---

## 1. Modell-szintű döntések

### 1.1 Két VG-fajta: OPTIONAL és MANDATORY

| Fajta | Checkbox | Default állapot | Mit jelent OFF / üres ha |
|---|---|---|---|
| **OPTIONAL** | van | OFF (ha nincs mentett pref) | "Mészáros dönt" → munkalapon `Standard` |
| **MANDATORY** | nincs | mindig ON, default érték kiválasztva | nem lehet üres — vagy mentett pref, vagy a default |

**Mikor melyik?**
- **OPTIONAL:** ha a termék OFF állapotban is teljes értékű (pl. a karaj pácolatlanul is megveszi, a vastagság opcionális ami fölött a mészáros dönthet)
- **MANDATORY:** ha a választás termékspecifikus alapparaméter ami nélkül a mészáros nem tud terméket előállítani (Méret hibrid termékeknél, Zsírosság darált húsnál)

### 1.2 Opt-in default modell — OPTIONAL VG-knél

| Állapot | Checkbox | Radio | Mészáros utasítás |
|---|---|---|---|
| Nincs mentett user-pref | OFF | rejtve | "Mészáros dönt" → `Standard` |
| Van mentett user-pref | ON (auto) | utolsó választás kijelölve | konkrét utasítás |
| User toggle ON, nincs pref | ON | üres | A user kell válasszon mielőtt kosárba teszi (validáció: ha ON és üres → "Válassz egyet") |
| User toggle OFF | OFF | rejtve | "Mészáros dönt" |

### 1.3 OFF-ekvivalens érték drop szabály — OPTIONAL VG-knél

Ha egy opció-érték szemantikailag azonos azzal, hogy "ne csinálj vele semmit / hagyd alapállapotban", akkor azt **NEM rögzítjük** értékként, mert a checkbox OFF állapota pontosan ezt fejezi ki:

- ❌ `pacolas` / `nem_pacolt` (Pácolatlan) — DROPPED, OFF = pácolatlan
- ❌ `szeletes` / `egesz` (Egész) — DROPPED, OFF = egészben hagyja
- ✅ `szeletes` / `normal` (4 mm közepes) — MEGTARTJUK, mert ez explicit kérés (nem azonos azzal, hogy OFF = egészben)

Ez a szabály **csak OPTIONAL VG-kre** vonatkozik. A MANDATORY VG-knél minden érték megmarad, mert ott nincs OFF.

### 1.4 Info modal kötelező mezők — option_value bővítés

Az option_value adatmodellt (lásd `_schema-v1.2.json` `option_value` definíció) az alábbi mezőkkel kell bővíteni. A típusok a JSON schema szempontjából vannak megadva — a konkrét adatbázis-séma és tárolási megvalósítás a fejlesztő döntése.

| Mező | JSON típus | Példa |
|---|---|---|
| `image_url` | string (nullable) | `/files/options/pacolas-hagyomanyos.webp` |
| `image_alt_hu` | string (nullable) | "Hagyományos pácolt karaj közelről" |
| `image_alt_ro` | string (nullable) | "Cotlet marinat tradițional în prim-plan" |
| `description_hu` | string, hosszú szöveg (HTML/Markdown engedett) | (lásd §3-§7 értékenként) |
| `description_ro` | string, hosszú szöveg | (lásd §3-§7 értékenként) |
| `meta_hint_hu` | string (≤60 char) | "Só, bors, fokhagyma" |
| `meta_hint_ro` | string (≤60 char) | "Sare, piper, usturoi" |
| `price_modifier` | number, default 0 (RON) | `2` (pácolás esetén) |
| `price_modifier_unit` | enum: `per_kg` / `per_unit` / `flat` / null | `per_kg` |

**Pricing modell:** A `price_modifier` az ALAP termék ára FÖLÉ adódik, a `price_modifier_unit` szerint:
- `per_kg`: szorzódik a kosár-tétel kg-jával (pl. Pácolás 2 RON/kg × 1 kg = +2 RON)
- `per_unit`: szorzódik a darabszámmal (db-os termékeknél)
- `flat`: egyszeri felár, mennyiségtől függetlenül
- A 0 értékű (default) az opció **ingyenes**

**Image guidelines:** 16:9 vagy 4:3 arány, min. 800×600px, fehér háttér NEM kötelező (a DH a hagyományos műhelyfotót javasolja). Az `alt` szöveg a screen reader és print-fallback miatt kell.

### 1.5 VG fejléc copy és kind — product_option bővítés

Az option adatmodellt (lásd `_schema-v1.2.json` `product_option` definíció) az alábbi mezőkkel kell bővíteni:

| Mező | JSON típus | Példa | Cél |
|---|---|---|---|
| `kind` | enum: `optional` / `mandatory` | `optional` | UI rendering módja |
| `default_value` | string (nullable optional, required mandatory esetén) | `kozepes` | MANDATORY VG-knél a default radio. OPTIONAL-nál fallback. |
| `vg_off_hint_hu` | string (nullable) | "Pácolatlan" | Fejlécben látszik OFF állapotban (csak OPTIONAL) |
| `vg_off_hint_ro` | string (nullable) | "Nemarinat" | RO production |

A meglévő `option_name_hu` / `option_name_ro` (pl. "Pácolás" / "Marinare") a VG fejlécében jelenik meg. Az `option_id` (`pacolas`) a stabil azonosító a backend perzisztenciához (user-preferenciák kulcsa).

---

## 2. Opció-típus könyvtár

A 15 termékre **5 opció-típus** van használatban. Ugyanaz az opció-típus minden termékre azonos copy-val és érték-listával (a méret-tartomány kivétel: termékenként más kg-szám).

| # | option_id | HU név | RO név | Kind | Értékek | Termékek |
|---|---|---|---|---|---|---|
| 1 | `pacolas` | Pácolás | Marinare | OPTIONAL | 2 (Hagyományos, Barbecue) | 6 |
| 2 | `forma` | Szeletelés *(forma)* | Tăiere *(formă)* | OPTIONAL | 2 (Normál, Dupla) | 1 |
| 3 | `szeletes` | Szeletelés | Tăiere | OPTIONAL | 3 (Vékony, Normál, Vastagabb) | 9 |
| 4 | `meret` | Méret | Mărime | **MANDATORY** | 3 (Kisebb, Közepes, Nagyobb) | 3 |
| 5 | `zsirossag` | Zsírosság | Conținut de grăsime | **MANDATORY** | 3 (Kevésbé zsíros, Normál, Zsírosabb) | 1 |

> **Megjegyzés a §2 / §3 névütközéshez:** Az `option_id=forma` és `option_id=szeletes` mindkettő HU label "Szeletelés", de **soha nem jelennek meg ugyanazon a terméken** (a forma csak nyakaskarajra, a szeletes a többire). Az UI-ban így nincs ütközés.

---

## 3. Opció-típus: Pácolás / Marinare

**`option_id`: `pacolas`** · OPTIONAL · 2 érték · 6 termékben (014, 015, 016, 019, 020, 946) · **díjköteles: +2 RON/kg**

**VG fejléc:**
- HU: `Pácolás` · RO: `Marinare`
- OFF hint HU: `Pácolatlan` · RO: `Nemarinat`

> **💰 Pricing:** A pácolás a Phase 1-ben az **egyetlen díjköteles VG**: mindkét érték (Hagyományos, Barbecue) `+2 RON/kg` felárat ad a tétel árához (`price_modifier = 2`, `price_modifier_unit = per_kg`). OFF állapotban (Pácolatlan) NINCS felár. A többi opció-típus (Szeletelés-forma, Szeletelés-vastagság, Méret, Zsírosság) **ingyenes**, `price_modifier = 0`.

> **OFF szemantika:** A Pácolatlan érték nem szerepel külön opcióként, mert a checkbox OFF állapota ezt fejezi ki. Az munkalapon `Standard` jelenik meg.

### 3.1 `hagyomanyos` · Hagyományos / Tradițional · **+2 RON/kg**

| Mező | HU | RO |
|---|---|---|
| Label | Hagyományos | Tradițional |
| Meta hint | Só, bors, fokhagyma | Sare, piper, usturoi |
| Price modifier | `2` RON, `per_kg` | `2` RON, `per_kg` |
| Modal title | Hagyományos pácolás | Marinare tradițională |
| Modal image alt | Sózott-borsozott, fokhagymás karaj | Cotlet sărat-piperat cu usturoi |
| Modal description | Só, bors, fokhagyma, friss fűszerek. Klasszikus kárpát-medencei ízprofil sütésre és grillezésre. A mészáros 24 órás pácolást javasol, hogy az ízek mélyen átjárják a húst. **Felár: +2 RON/kg.** | Sare, piper, usturoi, ierburi proaspete. Profil clasic carpatic pentru frigare și grătar. Măcelarul recomandă 24 de ore de marinare pentru ca aromele să pătrundă bine. **Supliment: +2 RON/kg.** |

### 3.2 `barbecue` · Barbecue / Barbecue · **+2 RON/kg**

| Mező | HU | RO |
|---|---|---|
| Label | Barbecue | Barbecue |
| Meta hint | Paradicsomos, BBQ-szerű | Cu roșii, stil BBQ |
| Price modifier | `2` RON, `per_kg` | `2` RON, `per_kg` |
| Modal title | Barbecue pácolás | Marinare Barbecue |
| Modal image alt | Paradicsomos BBQ pácban karaj grillen | Cotlet în marinată BBQ cu roșii pe grătar |
| Modal description | Paradicsomos, édeskés, füstös ízprofil. Grillezésre kifejezetten ajánlott. A pác benne van, közvetlenül a grillre helyezhető. **Felár: +2 RON/kg.** | Profil cu roșii, dulce, afumat. Recomandat pentru grătar. Marinata este deja în carne, direct pe grătar. **Supliment: +2 RON/kg.** |

---

## 4. Opció-típus: Szeletelés (forma) / Tăiere (formă)

**`option_id`: `forma`** · OPTIONAL · 2 érték · 1 termékben (014 Sertés nyakaskaraj)

**VG fejléc:**
- HU: `Szeletelés` · RO: `Tăiere`
- OFF hint HU: `Mészáros dönt` · RO: `Decide măcelarul`

> Ez a "karaj-specifikus szeletelés", csak nyakaskarajra. A `Normál` szelet vagy `Dupla` (más néven *Lecsi pecsi*) — két szelet középen egyben, kinyitva, potyolva.

### 4.1 `normal` · Normál / Normal

| Mező | HU | RO |
|---|---|---|
| Label | Normál | Normal |
| Meta hint | Klasszikus szelet | Felie clasică |
| Modal title | Normál szeletelés | Tăiere normală |
| Modal image alt | Klasszikus nyakaskaraj szelet | Felie clasică de ceafă |
| Modal description | Egyszelet, klasszikus, minimum újnyi vastagságú. Pörkölthez, rántott karajhoz, gyorsan átsülő ételekhez. | O singură felie clasică, minimum un deget de groasă. Pentru tocăniță, șnițel, rețete care se gătesc rapid. |

### 4.2 `dupla` · Dupla *(Lecsi pecsi)* / Dublă

| Mező | HU | RO |
|---|---|---|
| Label | Dupla | Dublă |
| Meta hint | Lecsi pecsi, két szelet egyben | Lecsi pecsi, două felii unite |
| Modal title | Dupla szeletelés (Lecsi pecsi) | Tăiere dublă (Lecsi pecsi) |
| Modal image alt | Dupla nyakaskaraj kinyitva, potyolva | Ceafă dublă deschisă și bătută |
| Modal description | Két szelet középen egyben tartva, kinyitva, potyolva — a hagyományos "Lecsi pecsi". Vastagabb, férfiasabb porció lassú sütésre. A mészáros 4 ujjnyi vastagságot javasol pörkölésre. | Două felii unite la mijloc, deschise, bătute, "Lecsi pecsi" tradițional. Porție mai groasă pentru gătit lent. Măcelarul recomandă grosime de 4 degete pentru frigare. |

---

## 5. Opció-típus: Szeletelés / Tăiere

**`option_id`: `szeletes`** · OPTIONAL · 3 érték · 9 termékben (015, 019, 020, 917, 946, 948, 949, 991, 9904)

**VG fejléc:**
- HU: `Szeletelés` · RO: `Tăiere`
- OFF hint HU: `Egészben, mészáros dönt` · RO: `Întreg, decide măcelarul`

> **OFF szemantika:** Ha kikapcsolod, a hús egészben jön (vákuumozva, nem szeletelve). Ha bekapcsolod, a mészáros a kívánt vastagságra szeleteli. Ez egyesíti a régi "egész vs szeletelt" döntést és a "vastagság" választást egy VG-be.
>
> **Termékspecifikus mm-érték:** A "Normál" mm-értelmezése termékenként más:
> - Szalámi (917, 991, 9904): Vékony 2mm · Normál 4mm · Vastagabb 6mm
> - Karaj-félék (015, 949): Vékony 1cm · Normál 1,5cm · Vastagabb 2,5cm
> - Has, oldalas (019, 020, 946): Vékony 1,5cm · Normál 2cm · Vastagabb 3cm
> - Füstölt nyakas karaj (948): Vékony 2mm · Normál 4mm · Vastagabb 6mm (felvágott)
>
> Ezt a per-termék `option_value_overrides` mechanizmussal oldjuk meg (lásd `MASTER/products/*.md` YAML frontmatter), ami a `meta_hint_hu` / `meta_hint_ro` mezőket termékenként felülírja. A build pipeline a master `_options.yaml`-t és a per-termék override-okat merge-eli a végső `products-vX.Y.json` `options[]` array-be.

### 5.1 `vekony` · Vékony / Subțire

| Mező | HU | RO |
|---|---|---|
| Label | Vékony | Subțire |
| Meta hint (sablon) | {thickness_min} | {thickness_min} |
| Modal title | Vékony szeletek | Felii subțiri |
| Modal image alt | Vékonyra szeletelt hús | Carne feliată subțire |
| Modal description (sablon) | {thickness_min} vastagságra szeletelve. Klasszikus szendvicsbe, hideg tálra, gyorsan átsülő ételekhez, finom ízekhez. | Feliat la {thickness_min}. Pentru sandviș clasic, platou rece, rețete rapide, arome fine. |

### 5.2 `normal` · Normál / Normal

| Mező | HU | RO |
|---|---|---|
| Label | Normál | Normal |
| Meta hint (sablon) | {thickness_normal} | {thickness_normal} |
| Modal title | Normál szeletek | Felii normale |
| Modal image alt | Egységesen szeletelt hús közepes vastagságra | Carne feliată uniform la grosime medie |
| Modal description (sablon) | {thickness_normal} — a leggyakoribb választás. Egységes vastagság szendvicsre, sütésre, harapásra egyaránt. | {thickness_normal} — cea mai populară alegere. Grosime uniformă pentru sandviș, gătit, gustare. |

### 5.3 `vastagabb` · Vastagabb / Mai gros

| Mező | HU | RO |
|---|---|---|
| Label | Vastagabb | Mai gros |
| Meta hint (sablon) | {thickness_max} | {thickness_max} |
| Modal title | Vastagabb szeletek | Felii mai groase |
| Modal image alt | Vastag szeletek hús | Felii groase de carne |
| Modal description (sablon) | {thickness_max}. Robusztus szelet, falatozásra, paraszti tálra, vajaskenyérre, lassú sütésre. Karakteres íz. | {thickness_max}. Felie robustă, pentru gustare, platou țărănesc, pâine cu unt, gătit lent. Aromă pronunțată. |

---

## 6. Opció-típus: Méret / Mărime · MANDATORY

**`option_id`: `meret`** · MANDATORY · 3 érték · 3 hibrid termékben (007, 945, 945.1)

**VG fejléc (NINCS checkbox):**
- HU: `Méret` · RO: `Mărime`
- Default: `kozepes` (Közepes / Mediu)

> **Mandatory szemantika:** A hibrid termékek (csülök) mérete kritikus a logisztikához és az árszámításhoz. A user nem hagyhatja "üresen" — vagy a mentett pref, vagy a default `Közepes` lesz kiválasztva. Nincs OFF állapot. A radio mindig látható.

### 6.1 `kisebb` · Kisebb / Mai mic

| Mező | HU | RO |
|---|---|---|
| Label | Kisebb | Mai mic |
| Meta hint (sablon) | {weight_range} | {weight_range} |
| Modal title | Kisebb méret | Mărime mai mică |
| Modal image alt | Kisebb csülök referenciával méretarányhoz | Ciolan mai mic cu referință de scară |
| Modal description (sablon) | {weight_range} kg. Ideális kisebb háztartásnak, 2-3 fős vacsorára. Gyorsabban sül. | {weight_range} kg. Ideal pentru gospodării mici, cină pentru 2-3 persoane. Se gătește mai repede. |

### 6.2 `kozepes` · Közepes / Mediu *(default)*

| Mező | HU | RO |
|---|---|---|
| Label | Közepes | Mediu |
| Meta hint (sablon) | {weight_range} · alapértelmezett | {weight_range} · standard |
| Modal title | Közepes méret | Mărime medie |
| Modal image alt | Közepes csülök, referencia konyhakéssel | Ciolan mediu, referință cu cuțit |
| Modal description (sablon) | {weight_range} kg. A leggyakoribb választás. 4 fős család vasárnapi ebédjéhez. | {weight_range} kg. Cea mai populară alegere. Pentru prânzul de duminică al unei familii de 4. |

### 6.3 `nagyobb` · Nagyobb / Mai mare

| Mező | HU | RO |
|---|---|---|
| Label | Nagyobb | Mai mare |
| Meta hint (sablon) | {weight_range} | {weight_range} |
| Modal title | Nagyobb méret | Mărime mai mare |
| Modal image alt | Nagyobb csülök tálon | Ciolan mai mare pe platou |
| Modal description (sablon) | {weight_range} kg. Nagyobb társasághoz, lassan sült ünnepi ételekhez. Hosszabb sütési idővel. | {weight_range} kg. Pentru grupuri mai mari, mâncăruri festive gătite lent. Timp de gătire mai lung. |

---

## 7. Opció-típus: Zsírosság / Conținut de grăsime · MANDATORY

**`option_id`: `zsirossag`** · MANDATORY · 3 érték · 1 termékben (902 Sertés Őrölt Hús)

**VG fejléc (NINCS checkbox):**
- HU: `Zsírosság` · RO: `Conținut de grăsime`
- Default: `normal` (Normál)

> **Mandatory szemantika:** Az őrölt hús zsírtartalma alapparaméter ami nélkül a mészáros nem tudja összekeverni a megfelelő arányú húst. A radio mindig látható, nincs OFF.

### 7.1 `kevesbe_zsiros` · Kevésbé zsíros / Mai slab

| Mező | HU | RO |
|---|---|---|
| Label | Kevésbé zsíros | Mai slab |
| Meta hint | Bolognai, ragú · kb. 70/30 | Bolognese, ragout · cca. 70/30 |
| Modal title | Kevésbé zsíros · kb. 70/30 | Mai slab · cca. 70/30 |
| Modal image alt | Sovány, kevés zsírral darált hús | Carne tocată slabă cu puțină grăsime |
| Modal description | Kb. 70% sovány, 30% zsír. Egészségtudatosabb választás bolognai szószhoz, ragúhoz, könnyebb fasírthoz. | Aprox. 70% slab, 30% grăsime. Alegere mai sănătoasă pentru sos bolognez, ragout, chiftele ușoare. |

### 7.2 `normal` · Normál / Normal *(default)*

| Mező | HU | RO |
|---|---|---|
| Label | Normál | Normal |
| Meta hint | Alapértelmezett, fele-fele | Standard, jumi-juma |
| Modal title | Normál · kb. 50/50 | Normal · cca. 50/50 |
| Modal image alt | Klasszikus arányú darált hús | Carne tocată cu raport clasic |
| Modal description | Kb. 50-50% sovány-zsír arány. A mészáros alapbeállítása, minden klasszikus recepthez illik. | Aprox. 50-50% slab-grăsime. Setarea standard a măcelarului, potrivită pentru toate rețetele clasice. |

### 7.3 `zsirosabb` · Zsírosabb / Mai gras

| Mező | HU | RO |
|---|---|---|
| Label | Zsírosabb | Mai gras |
| Meta hint | Fasírt, töltelékes káposzta · kb. 35/65 | Chiftele, sarmale · cca. 35/65 |
| Modal title | Zsírosabb · kb. 35/65 | Mai gras · cca. 35/65 |
| Modal image alt | Zsírosabb, lédús darált hús | Carne tocată mai grasă, suculentă |
| Modal description | Kb. 35% sovány, 65% zsír. Lédús fasírthoz, töltelékes káposztához, hagyományos magyar és román ételekhez. | Aprox. 35% slab, 65% grăsime. Pentru chiftele suculente, sarmale, mâncăruri tradiționale ungare și românești. |

---

## 8. Termék-szintű VG kiosztás

A 15 termék mindegyikére: melyik VG-k jelennek meg, milyen sorrendben.

| # | Termék | Kód | Termék típus | VG-k (sorrendben) | Kind |
|---|---|---|---|---|---|
| 1 | Sertés Csülök | 007 | hibrid | 1. Méret | M |
| 2 | Sertés Hasrész Csontnélkül | 019 | weight | 1. Szeletelés · 2. Pácolás | O · O |
| 3 | Sertés Oldalas | 020 | weight | 1. Szeletelés · 2. Pácolás | O · O |
| 4 | Sertés fehérkaraj csontnélkül | 015 | weight | 1. Szeletelés · 2. Pácolás | O · O |
| 5 | Sertés Csontos Karaj | 016 | hibrid | 1. Pácolás | O |
| 6 | Sertés nyakaskaraj | 014 | weight | 1. Szeletelés *(forma)* · 2. Pácolás | O · O |
| 7 | Sertés Őrölt Hús | 902 | weight | 1. Zsírosság | **M** |
| 8 | Füstölt Csülök | 945 | hibrid | 1. Méret | **M** |
| 9 | Füstölt Csülök Csont Nélkül | 945.1 | hibrid | 1. Méret | **M** |
| 10 | Füstölt Fehér Karaj | 949 | weight | 1. Szeletelés | O |
| 11 | Füstölt Has | 946 | weight | 1. Szeletelés · 2. Pácolás | O · O |
| 12 | Füstölt Nyakas Karaj | 948 | weight | 1. Szeletelés | O |
| 13 | Házi szalámi | 991 | weight | 1. Szeletelés | O |
| 14 | Sertés Szalámi | 917 | weight | 1. Szeletelés | O |
| 15 | Téli Szalámi | 9904 | weight | 1. Szeletelés | O |

> **Legend:** M = MANDATORY, O = OPTIONAL. A 016 hibrid + Pácolás eset (még mindig csak 1 VG, de hibrid termék-típus): a hibrid súly-tartomány a termékkártyán külön kommunikálódik (1 db ≈ 1,5 kg, ±10%), nem a Méret VG-vel.

> **A maradék 31 termék** (a 46-ból) NEM kap VG-t.

---

## 9. Méret-tartomány overrides (hibrid termékek, MANDATORY)

A `meret` opció `value_id`-i egységesek (`kisebb` / `kozepes` / `nagyobb`), de a kg-tartomány termékenként eltér. A §6 modal description sablonjába a `{weight_range}` placeholder helyébe ezek kerülnek:

| Termék | Kód | `kisebb` | `kozepes` *(default)* | `nagyobb` |
|---|---|---|---|---|
| Sertés Csülök | 007 | 1,2-1,4 kg | 1,4-1,6 kg | 1,6-1,8 kg |
| Füstölt Csülök | 945 | 1,2-1,5 kg | 1,5-1,7 kg | 1,7-1,9 kg |
| Füstölt Csülök Csont Nélkül | 945.1 | 1,0-1,2 kg | 1,2-1,4 kg | 1,4-1,5 kg |

> ⚠ A 945 és 945.1 számok becslések, a termelő (Mikado) **erősítse meg** a 2026-05-12-i meeting előtt.

---

## 10. Szeletelés mm-tartomány overrides

A `szeletes` opció (§5) `value_id`-i egységesek (`vekony` / `normal` / `vastagabb`), a mm-érték termékenként eltér. A `meta_hint` és modal description sablonjába ez kerül:

| Termék | Kód | `vekony` | `normal` | `vastagabb` |
|---|---|---|---|---|
| Füstölt Fehér Karaj | 949 | 1 cm | 1,5 cm | 2,5 cm |
| Sertés fehérkaraj csontnélkül | 015 | 1 cm | 1,5 cm | 2,5 cm |
| Sertés Hasrész | 019 | 1,5 cm | 2 cm | 3 cm |
| Sertés Oldalas | 020 | 1,5 cm | 2 cm | 3 cm |
| Füstölt Has | 946 | 2 mm | 4 mm | 6 mm |
| Füstölt Nyakas Karaj | 948 | 2 mm | 4 mm | 6 mm |
| Házi szalámi | 991 | 2 mm | 4 mm | 6 mm |
| Sertés Szalámi | 917 | 2 mm | 4 mm | 6 mm |
| Téli Szalámi | 9904 | 2 mm | 4 mm | 6 mm |

> ⚠ A karaj-félék (015, 949) és a has/oldalas (019, 020) cm-es vastagságai becslések — termelővel egyeztetendők. A felvágott / szalámi 2/4/6 mm a meeting (2026-05-07) megerősített értéke.

---

## 11. MANDATORY VG default értékek

Mivel a MANDATORY VG-knek nincs OFF állapotuk, a `default_value` mindig kiválasztott:

| Option ID | Default | Indoklás |
|---|---|---|
| `meret` | `kozepes` | Bell curve közepe, leggyakoribb fogyasztói szokás |
| `zsirossag` | `normal` | Mészáros alap (902-es spec-ben is ez), univerzális használhatóság |

---

## 12. Implementációs sorrend (Jira sub-tasks javaslat)

A v1.0 fő DH-173 ticket alá:

| Sub-task | Cél | Becslés |
|---|---|---|
| **DH-173-1** | Backend adatmodell-bővítés: `option_value` (image_url, image_alt_*, description_*, meta_hint_*, price_modifier, price_modifier_unit), `option` (kind, default_value, vg_off_hint_*) — lásd `_schema-v1.2.json` | 5h |
| **DH-173-2** | Schema v1.1 → v1.2 bump (`options[]` mező + build pipeline update) — **DONE design szakaszban** | 6h ✅ |
| **DH-173-3** | Backend seed adatok: 5 opció-típus × értékek + 15 termék VG-binding (`_options.yaml` + MD master alapján a §3-§10 szerint) | 8h |
| **DH-173-4** | Termékfotók beszerzése: ~15 új fotó (lásd §13) | termelő |
| **DH-173-5** | Frontend VG komponens: opt-in checkbox + radio list + info modal (kind=optional/mandatory, narrow variáns kosárhoz) | 14h |
| **DH-173-6** | Termékdetail oldal integráció: VG stack a Mennyiség alá | 4h |
| **DH-173-7** | Kosár integráció: VG narrow mód + per-item state + collapsed summary | 6h |
| **DH-173-8** | Mészáros munkalap (külön ticket: új DH-XXX) | 4h |
| **DH-173-9** | Analytics event-ek: `vg_toggled_on/off`, `vg_value_selected`, `vg_info_opened`, `vg_mandatory_default_kept` | 2h |
| **DH-173-10** | User-preferencia perzisztencia: sikeres rendelés után az aktív VG-választás mentése per user × termék | 4h |

---

## 13. Fotó-igénylista a termelőnek

Összesen **~15 új fotó** kell. Standard arány 4:3 vagy 16:9, min. 800×600px.

### 13.1 Pácolás (2 fotó)
| Fájl | Téma |
|---|---|
| `pacolas-hagyomanyos.webp` | Sózott-borsozott karaj fokhagymával |
| `pacolas-barbecue.webp` | BBQ pácban karaj grillen vagy tálon |

### 13.2 Szeletelés (forma) — nyakaskaraj (2 fotó)
| Fájl | Téma |
|---|---|
| `forma-normal.webp` | Klasszikus nyakaskaraj szelet |
| `forma-dupla.webp` | Dupla nyakaskaraj kinyitva, potyolva (Lecsi pecsi) |

### 13.3 Szeletelés (vastagság) — generikus (3 fotó × variánsok)
A 9 termékre 3-3 fotó kéne, de gyakorlatban **3 reprezentatív termékkép** (1× szalámi, 1× karaj, 1× has) elég és termékenként hivatkozhatóak:

| Fájl | Téma |
|---|---|
| `szeletes-szalami-vekony.webp` | 2 mm szalámi szelet (referencia: vonalzó) |
| `szeletes-szalami-normal.webp` | 4 mm szalámi szelet |
| `szeletes-szalami-vastagabb.webp` | 6 mm szalámi szelet |
| `szeletes-karaj-vekony.webp` | 1 cm karaj szelet |
| `szeletes-karaj-normal.webp` | 1,5 cm karaj szelet |
| `szeletes-karaj-vastagabb.webp` | 2,5 cm karaj szelet |

> A has/oldalas valószínűleg a karaj-fotókat újrahasználhatja, vagy 1-1 dedikált fotó kell — termelővel egyeztetendő.

### 13.4 Méret (csülök, 9 fotó — termékenként 3)
| Fájl | Téma |
|---|---|
| `meret-007-kisebb.webp` | 1,2-1,4 kg sertés csülök |
| `meret-007-kozepes.webp` | 1,4-1,6 kg sertés csülök |
| `meret-007-nagyobb.webp` | 1,6-1,8 kg sertés csülök |
| `meret-945-kisebb.webp` | 1,2-1,5 kg füstölt csülök |
| `meret-945-kozepes.webp` | 1,5-1,7 kg füstölt csülök |
| `meret-945-nagyobb.webp` | 1,7-1,9 kg füstölt csülök |
| `meret-945.1-kisebb.webp` | 1,0-1,2 kg füstölt csülök csont nélkül |
| `meret-945.1-kozepes.webp` | 1,2-1,4 kg füstölt csülök csont nélkül |
| `meret-945.1-nagyobb.webp` | 1,4-1,5 kg füstölt csülök csont nélkül |

> A méret-csoport fotóinál fontos a **méretreferencia** (kéz, kés, vonalzó), különben nem érzékelhető a különbség.

### 13.5 Zsírosság — 902 Sertés Őrölt Hús (3 fotó)
| Fájl | Téma |
|---|---|
| `zsirossag-kevesbe_zsiros.webp` | 70/30 sovány darált hús |
| `zsirossag-normal.webp` | 50/50 darált hús |
| `zsirossag-zsirosabb.webp` | 35/65 zsírosabb darált hús |

**Összesen:** 2 + 2 + 6 + 9 + 3 = **22 fotó** (de 1-2 újrahasznosítható → ~17-20).

---

## 14. Szabolcs review checklist

- [x] §1.1 OPTIONAL vs MANDATORY modell elfogadható? Új state-machine helyett ez egységes mind a két fajtára? ✅ 2026-05-09
- [x] §1.3 OFF-ekvivalens drop szabály — Pácolatlan és Egész jól van-e ledobva? Más érték is droppolandó? ✅ 2026-05-09
- [x] §3 Pácolás: 2 érték (Hagyományos + Barbecue) elég, vagy kell egy harmadik (pl. specifikus regionális pác)? ✅ 2026-05-09
- [x] §4 Szeletelés (forma) — `Lecsi pecsi` HU/RO copy stimmel? RO-ban a "Lecsi pecsi" megmarad mint kifejezés? ✅ 2026-05-09
- [x] §5 Szeletelés (vastagság) — a Vékony/Normál/Vastagabb értékek termék-specifikus mm-ekre fordításai (§10) realisztikusak? ✅ 2026-05-09
- [x] §6 Méret MANDATORY — a hibrid termékeknél tényleg kötelező-e? Vagy a Közepes default elég gyakran "elfelejthető"? ✅ 2026-05-09
- [x] §7 Zsírosság MANDATORY — a Normál default elég konzervatív? ✅ 2026-05-09
- [ ] §10 mm-tartományok karaj és has-oldalas termékekhez (becslések) — termelővel egyeztetendők
- [ ] §13 fotó-lista: 17-22 fotó realisztikus határidővel? Mikor érkezik?
- [ ] §12 sub-task becslések elfogadhatók? Új helyett 5 opció-típus → kevesebb seed work?

---

**Verzió:** 1.1 DRAFT | **Dátum:** 2026-05-09 | **Wireframe:** [v0.4-product-variations.html](../../../design/screen-catalog/screens/v0.4-product-variations.html)
