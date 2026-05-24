# Prezentáció Styleguide

## Elemzés összefoglaló

### 1. Esemény landing page (assets-eur.mkt.dynamics.com)
- Kék gradient háttér (sötétkék balról, világosabb kék jobbra)
- Fehér szöveg kék háttéren
- Mindkét logó (Promise Group + HLB) megjelenik
- Fehér "Regisztrálj" gomb lekerekített sarkokkal
- Professzionális, modern, tech-érzet
- Ez az, amit a közönség először lát -- a prezentációnak ehhez kell illeszkednie

### 2. Promise Group (promisegroup.com)
- Elsődleges: Sötétkék (#0056A7, #1863DC)
- Akcentus: Arany/sárga a "PROMISE GROUP" felirathoz
- Háttér: Fehér, világosszürke (#F0F1F4)
- Szöveg: Sötétszürke (#3E3E3E)
- Stílus: Vállalati, kifinomult, Microsoft-partner arculat
- Érettség: MAGAS -- professzionális, konzisztens

### 3. HLB - Hallenbeck IT (hlb.hu)
- Elsődleges akcentus: Sárga/arany (#FFD431)
- Fejléc: Sötétszürke (#333333)
- Háttér: Fehér, világosszürke (#F9F9F9)
- Szöveg: Sötét (#222222)
- Link szín: Kék (#1E73BE)
- Font: Montserrat
- Stílus: Tiszta, minimalista, meleg, SMB-barát
- Izometrikus illusztrációk, vonalas ikonok
- Érettség: KÖZEPES -- szép, de kevésbé kifinomult

---

## Döntés: Az esemény designját követjük

**Miért?** Az esemény landing page már egyesíti mindkét brand vizuális elemeit egy koherens designban. A résztvevők ezt látták regisztrációkor -- ha a prezentáció ehhez illeszkedik, az egységes és professzionális hatást kelt.

A kék gradient az esemény oldal domináns eleme, és jól passzol a tech/AI témához is.

---

## Színpaletta

### Elsődleges színek
| Szín | Hex | RGB | Használat |
|------|-----|-----|-----------|
| **Sötétkék** | `#1A3580` | 26, 53, 128 | Háttér (cím/szekció diák), szöveg sötét felületen |
| **Kék** | `#2266E3` | 34, 102, 227 | Elsődleges akcentus, gombok, kiemelések |
| **Világoskék** | `#4A8CF7` | 74, 140, 247 | Gradient jobb oldala, másodlagos kiemelés |

### Másodlagos színek
| Szín | Hex | RGB | Használat |
|------|-----|-----|-----------|
| **Fehér** | `#FFFFFF` | 255, 255, 255 | Szöveg sötét háttéren, tartalom háttér |
| **Világosszürke** | `#F0F1F4` | 240, 241, 244 | Tartalom diák háttere (alternatíva a fehérhez) |
| **Sötétszürke** | `#333333` | 51, 51, 51 | Szöveg fehér háttéren |
| **Középszürke** | `#3E3E3E` | 62, 62, 62 | Másodlagos szöveg |

### Akcentus szín (HLB-ből)
| Szín | Hex | RGB | Használat |
|------|-----|-----|-----------|
| **Arany/Sárga** | `#FFD431` | 255, 212, 49 | Kiemelés, fontos szám, ikon háttér (takarékosan!) |

---

## Tipográfia

| Elem | Font | Méret | Stílus |
|------|------|-------|--------|
| **Dia cím** | Montserrat | 36-40pt | Bold |
| **Szekció fejléc** | Montserrat | 22-26pt | Bold |
| **Törzs szöveg** | Calibri | 16-18pt | Regular |
| **Feliratok, megjegyzések** | Calibri | 12-14pt | Regular, szürke |
| **Nagy szám/statisztika** | Montserrat | 60-72pt | Bold |

---

## Dia típusok és elrendezés

### 1. Cím/Szekció diák (sötét)
- **Háttér**: Kék gradient (balról #1A3580, jobbra #4A8CF7)
- **Szöveg**: Fehér
- **Használat**: Nyitó dia, szekció átmenetek, záró dia
- Minimális szöveg, nagy betűméret, erős vizuális hatás

### 2. Tartalom diák (világos)
- **Háttér**: Fehér (#FFFFFF) vagy világosszürke (#F0F1F4)
- **Szöveg**: Sötétszürke (#333333)
- **Kiemelés**: Kék (#2266E3) a fontos szavakhoz
- **Használat**: A tartalom nagy része

### 3. Kontrasztos kiemelő diák
- **Háttér**: Sötétkék (#1A3580)
- **Szöveg**: Fehér + arany (#FFD431) akcentus
- **Használat**: Kulcs gondolat, idézet, erős állítás -- takarékosan

---

## Vizuális elemek

### Ikonok
- Vonalas (line-art) stílus, fehér sötét háttéren, kék világos háttéren
- Kék körben fehér háttéren (Promise Group stílus)
- Konzisztens méret: 40-50px

### Képek
- Lekerekített sarkok (az esemény oldalon a speaker fotó is kerek keretben van)
- Profi, tech-témájú illusztrációk ahol szükséges

### Elválasztók
- Nem használunk vonalakat a címek alatt (mesterséges érzetet kelt)
- Helyette: üres tér vagy háttérszín váltás

### Logók
- Promise Group + HLB logó az első és utolsó dián
- Kis méretben, diszkréten

---

## Struktúra ("szendvics" elrendezés)

```
[SÖTÉT] Nyitó dia -- kék gradient
[VILÁGOS] Tartalom diák
[SÖTÉT] Szekció átmenet
[VILÁGOS] Tartalom diák
[SÖTÉT] Szekció átmenet
[VILÁGOS] Tartalom diák
[SÖTÉT] Demo szekció intro
[VILÁGOS] Demo tartalom
[SÖTÉT] Záró dia -- kék gradient
```

---

## Kerülendő

- Ne használj szöveges felsorolásokat (bullet points) önmagukban -- mindig legyen vizuális elem mellette
- Ne ismételd ugyanazt az elrendezést egymás után -- variálj
- Ne használj 3-nál több színt egy dián
- Ne zsúfolj túl sok szöveget egy diára
- Ne használj sötét szöveget sötét háttéren vagy világos szöveget világos háttéren
- Ne használj aláhúzott címeket vagy accent vonalakat címek alatt
