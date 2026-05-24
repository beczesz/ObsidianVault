# AFM Mobilitate Verde IMM 2026 — Pályázati form mezőlistája

**Forrás:** `formular_depunere_AFM_Mobilitate_Verde.html` (Chrome MCP-ből kinyerve)
**Készült:** 2026-05-15
**Összesen:** 130 űrlap-mező + 22 csatolt dokumentum = **152 elem**

**Jelölés**: `KÖT` = kötelező · `opc` = opcionális · `[Fx.yy]` = a form belső mező-azonosítója

---

## 1. Cégadatok — *Date de identificare solicitant* (18 mező, 16 kötelező)

| # | Kód | Mező | Típus | Köt? | Megjegyzés |
|---|---|---|---|---|---|
| 1 | F1.01 | Denumire completă societate | szöveg | KÖT | |
| 2 | F1.02 | Cod unic de înregistrare (CUI) | szöveg | KÖT | pl. 15847291 |
| 3 | F1.03 | Nr. Registrul Comerțului | szöveg | KÖT | pl. J19/421/2003 |
| 4 | F1.04 | Plătitor de TVA | select | KÖT | Da/Nu/Impozit microîntreprinderi |
| 5 | F1.05 | Cod CAEN principal | szöveg | KÖT | |
| 6 | F1.06 | Descrierea activității principale | textarea | KÖT | |
| 7 | F1.07 | Județul | select | KÖT | Alba/Brașov/Covasna/**Harghita**/Mureș/Sibiu |
| 8 | F1.08 | Localitatea | szöveg | KÖT | |
| 9 | F1.09 | Strada | szöveg | KÖT | |
| 10 | F1.10 | Număr | szöveg | KÖT | |
| 11 | F1.11 | Cod poștal | szöveg | opc | |
| 12 | F1.12 | Telefon | tel | KÖT | |
| 13 | F1.13 | Email | email | KÖT | |
| 14 | F1.14 | Nume și prenume (reprezentant legal) | szöveg | KÖT | |
| 15 | F1.15 | Funcția | szöveg | KÖT | |
| 16 | F1.16 | CNP | szöveg | KÖT | |
| 17 | F1.17 | Seria și nr. CI | szöveg | KÖT | |
| 18 | F1.18 | Email reprezentant | email | opc | |

---

## 2. IMM-besorolás és eligibility — *Încadrare IMM și eligibilitate* (14 mező, MIND kötelező)

| # | Kód | Mező | Típus | Köt? | Megjegyzés |
|---|---|---|---|---|---|
| 1 | F2.01 | Categoria IMM | select | KÖT | Microîntreprindere / mică / mijlocie |
| 2 | F2.02 | Nr. mediu salariați (ultimul an) | szám | KÖT | |
| 3 | F2.03 | Cifra de afaceri netă (RON) | szám | KÖT | |
| 4 | F2.04 | Total active (RON) | szám | KÖT | |
| 5 | F2.05 | Cifra de afaceri netă în EUR | szám | KÖT | |
| 6 | F2.06 | Curs BNR EUR/RON utilizat | szöveg | KÖT | |
| 7 | F2.07 | ☑ Înregistrat conform Legii 31/1990 | checkbox | KÖT | nyilatkozat |
| 8 | F2.08 | ☑ Nu e în insolvență/faliment/lichidare | checkbox | KÖT | nyilatkozat |
| 9 | F2.09 | ☑ Nu are datorii la buget de stat/local | checkbox | KÖT | nyilatkozat |
| 10 | F2.10 | ☑ Nu fost decizie recuperare ajutor de stat | checkbox | KÖT | nyilatkozat |
| 11 | F2.11 | ☑ Drept proprietate/folosință imobil ≥5 ani | checkbox | KÖT | nyilatkozat |
| 12 | F2.12 | ☑ Angajament menținere investiție ≥3 ani | checkbox | KÖT | nyilatkozat |
| 13 | F2.13 | Total ajutoare de minimis primite (EUR) | szám | KÖT | 3 év halmozott |
| 14 | F2.14 | Valoare ajutor solicitat (EUR) | szám | KÖT | |

---

## 3. Projektleírás — *Descrierea investiției propuse* (32 mező, 10 kötelező főmező + autó-altáblák)

### 3.A — Alapadatok (4 mező)

| # | Kód | Mező | Típus | Köt? |
|---|---|---|---|---|
| 1 | F3.01 | Titlul proiectului | szöveg | KÖT |
| 2 | F3.02 | Rezumatul proiectului | textarea | KÖT |
| 3 | F3.03 | Justificarea necesității investiției | textarea | KÖT |
| 4 | F3.04 | Număr total vehicule electrice solicitate | select | KÖT | 1-5 jármű |

### 3.B — Jármű 1 [F3.05a–F3.15a] (11 mező — sablon ismétlődik 2 járműre)

| # | Kód | Mező | Típus | Köt? |
|---|---|---|---|---|
| 5 | F3.05a | Marca și modelul (autó 1) | szöveg | opc |
| 6 | F3.06a | Categorie vehicul | select | opc | N1 (<3,5t) / M1 |
| 7 | F3.07a | Tip propulsie | select | opc | BEV / PHEV |
| 8 | F3.08a | Autonomie WLTP (km) | szám | opc |
| 9 | F3.09a | Capacitate baterie (kWh) | szám | opc |
| 10 | F3.10a | Putere motor (kW) | szám | opc |
| 11 | F3.11a | Sarcină utilă maximă (kg) | szám | opc |
| 12 | F3.12a | Volum de încărcare (m³) | szám | opc |
| 13 | F3.13a | Preț catalog fără TVA (RON) | szám | opc |
| 14 | F3.14a | Dealer / Furnizor | szöveg | opc |
| 15 | F3.15a | Nr. ofertă de preț | szöveg | opc |

### 3.C — Jármű 2 [F3.05b–F3.15b] (11 mező, ugyanúgy)

### 3.D — Töltőállomás (6 mező, MIND kötelező)

| # | Kód | Mező | Típus | Köt? |
|---|---|---|---|---|
| 27 | F3.16 | Tip stație | select | KÖT |
| 28 | F3.17 | Putere nominală (kW) | szám | KÖT |
| 29 | F3.18 | Nr. puncte de încărcare | szám | KÖT |
| 30 | F3.19 | Locație amplasare | szöveg | KÖT |
| 31 | F3.20 | Preț stație cu instalare, fără TVA (RON) | szám | KÖT |
| 32 | F3.21 | Accesibilitate publică | select | KÖT |

---

## 4. Költségvetés és pénzügyi terv — *Buget și plan financiar* (14 mező)

### 4.A — Költségtábla (12 cella, auto-számolt)

| Sor | Tétel | Érték nélk. TVA (RON) | AFM-finanszírozás (80%) | Önrész (20%) |
|---|---|---|---|---|
| F4.01 | Jármű 1 | szám | szám | szám |
| F4.02 | Jármű 2 | szám | szám | szám |
| F4.03 | Töltőállomás (telepítéssel) | szám | szám | szám |
| F4.04 | **TOTAL PROIECT** | szám | szám | szám |

### 4.B — Önrész igazolása (2 mező, KÖT)

| # | Kód | Mező | Típus | Köt? |
|---|---|---|---|---|
| 13 | F4.05 | Sold cont bancar la data depunerii (RON) | szám | KÖT |
| 14 | F4.06 | Sursa co-finanțării | select | KÖT | Surse proprii / Credit / Mix |

---

## 5. Járműflotta és referencia-indikátorok — *Parcul auto existent* (28 mező)

### 5.A — Összesített indikátorok (4 mező, MIND kötelező)

| # | Kód | Mező | Típus | Köt? |
|---|---|---|---|---|
| 1 | F5.01 | Număr total vehicule în parcul auto | szám | KÖT |
| 2 | F5.03 | Consum total motorină/an (litri) | szám | KÖT |
| 3 | F5.04 | Emisii CO₂ estimate (tone/an) | szám | KÖT |
| 4 | F5.05 | Cost total combustibil/an (RON) | szám | KÖT |

### 5.B — Járműflotta-tábla (4 sor × 6 oszlop = 24 cella, [F5.02a–F5.02d])

| Sor | Marca/Model | An fabricație | Combustibil | Nr. înmatriculare | Km/an | Stare |
|---|---|---|---|---|---|---|
| F5.02a | szöveg | szám | select | szöveg | szám | select |
| F5.02b | szöveg | szám | select | szöveg | szám | select |
| F5.02c | szöveg | szám | select | szöveg | szám | select |
| F5.02d | szöveg | szám | select | szöveg | szám | select |

---

## 6. Telephely és ingatlanjog — *Locul de implementare* (8 mező, 6 kötelező)

| # | Kód | Mező | Típus | Köt? |
|---|---|---|---|---|
| 1 | F6.01 | Tipul dreptului asupra imobilului | select | KÖT | Proprietate / Închiriere ≥5 ani / Comodat ≥5 ani / Concesiune / Superficie |
| 2 | F6.02 | Nr. contract / act juridic | szöveg | KÖT |
| 3 | F6.03 | Data expirării | dátum | KÖT |
| 4 | F6.04 | Proprietar imobil | szöveg | KÖT |
| 5 | F6.05 | Adresa completă imobil implementare | textarea | KÖT |
| 6 | F6.06 | Nr. cadastral / Nr. carte funciară | szöveg | opc |
| 7 | F6.07 | Suprafață totală imobil (m²) | szám | KÖT |
| 8 | F6.08 | Observații privind stabilitatea dreptului | textarea | opc |

---

## 7. Hatás és teljesítmény-indikátorok — *Impact și indicatori* (7 mező, 6 kötelező)

| # | Kód | Mező | Típus | Köt? |
|---|---|---|---|---|
| 1 | F7.01 | Reducere emisii CO₂ (tone/an) | szám | KÖT |
| 2 | F7.02 | Reducere consum combustibil fosil (litri/an) | szám | KÖT |
| 3 | F7.03 | Economie anuală estimată (RON) | szám | KÖT |
| 4 | F7.04 | Perioada de recuperare a investiției proprii (luni) | szám | KÖT |
| 5 | F7.05 | Km parcurși anual estimat cu vehiculele electrice | szám | KÖT |
| 6 | F7.06 | Măsuri de durabilitate (≥3 ani) | textarea | KÖT |
| 7 | F7.07 | Contribuție la obiective strategice locale/regionale | textarea | opc |

---

## 8. Csatolt dokumentumok — *Documente atașate* (22 fájl, 21 kötelező, 1 opcionális)

| Kód | Dokumentum | Köt? | Formátum / megkötés |
|---|---|---|---|
| **A. Jogi és adóügyi dokumentumok** | | | |
| A-01 | Certificat constatator ONRC | KÖT | PDF, max 10 MB, **max 30 napos** |
| A-02 | Act constitutiv (forma consolidată) | KÖT | PDF, max 10 MB |
| A-03 | CI administrator | KÖT | PDF, max 5 MB |
| A-04 | Declarație beneficiar real (UBO) — notarială | KÖT | PDF, max 10 MB, **notari eredeti** |
| A-05 | Certificat atestare fiscală ANAF | KÖT | PDF, max 10 MB, **max 30 napos!** |
| A-06 | Certificat atestare fiscală LOCAL (DITL) | KÖT | PDF, max 10 MB, **max 30 napos!** |
| **B. Pénzügyi dokumentumok** | | | |
| B-01 | Bilanț contabil 2023 (ANAF-letétbe helyezett) | KÖT | PDF, aláírt + bélyegzett |
| B-02 | Bilanț contabil 2024 (ANAF-letétbe helyezett) | KÖT | PDF, aláírt + bélyegzett |
| B-03 | Bankkivonat — utolsó 3 hónap | KÖT | PDF, max 10 MB |
| **C. EV-beszerzési ajánlatok** | | | |
| C-01 | Ofertă dealer nr. 1 | KÖT | PDF, max 10 MB, részletes |
| C-02 | Ofertă dealer nr. 2 | KÖT | PDF, max 10 MB |
| C-03 | Ofertă dealer nr. 3 (3. kötelező szállító) | KÖT | PDF, min. 3 dílertől |
| **D. Ingatlan-okmányok** | | | |
| D-01 | Contract de închiriere / act proprietate | KÖT | PDF, hiteles másolat |
| D-02 | Extras carte funciară | **opc** | PDF, ajánlott |
| **E. Anexák és nyilatkozatok** | | | |
| E-01 | Plan de afaceri (Anexa 6 kitöltve) | KÖT | PDF, max 20 MB, Anexa 6 struktúra |
| E-02 | Declarație IMM (Anexa 1) | KÖT | PDF, aláírt + bélyegzett |
| E-03 | Declarație de minimis (Anexa 2) | KÖT | PDF, aláírt + bélyegzett |
| E-04 | Declarație menținere investiție 3 ani | KÖT | PDF, aláírt + bélyegzett |
| E-05 | Declarație menținere locuri de muncă | KÖT | PDF, aláírt + bélyegzett |
| E-06 | Declarație impact mediu | KÖT | PDF, aláírt + bélyegzett |
| E-07 | Declarație incompatibilitate / conflict de interese | KÖT | PDF, aláírt + bélyegzett |
| E-08 | Acord GDPR | KÖT | PDF, aláírt |

---

## 9. Záró nyilatkozat — *Declarație finală și angajamente* (9 mező, MIND kötelező)

| # | Kód | Mező | Típus | Köt? |
|---|---|---|---|---|
| 1 | F9.01 | ☑ Adatok teljesek, helyesek, valósak | checkbox | KÖT |
| 2 | F9.02 | ☑ Cég nincs nehéz helyzetben (2014/C 249/01) | checkbox | KÖT |
| 3 | F9.03 | ☑ Investiție-menținere ≥3 év + non-elidegenítés | checkbox | KÖT |
| 4 | F9.04 | ☑ Munkahely-szám tartása ≥3 év | checkbox | KÖT |
| 5 | F9.05 | ☑ Ghidul Solicitantului tudomásul vétele | checkbox | KÖT |
| 6 | F9.06 | ☑ GDPR-egyetértés (Reg. UE 2016/679) | checkbox | KÖT |
| 7 | F9.07 | ☑ Nincs duplikált finanszírozás-igénylés | checkbox | KÖT |
| 8 | F9.08 | Nume și prenume reprezentant legal | szöveg | KÖT |
| 9 | F9.09 | Data completării | dátum | KÖT |

---

## Összefoglaló — kötelezőség breakdown

| Kategória | Mezők össz. | Kötelező | Opcionális |
|---|---:|---:|---:|
| 1. Cégadatok | 18 | 16 | 2 |
| 2. IMM + eligibility | 14 | 14 | 0 |
| 3. Projektleírás | 32 | 10 | 22 (jármű-altáblák) |
| 4. Költségvetés | 14 | 2 | 12 (auto-számolt) |
| 5. Járműflotta | 28 | 4 | 24 (járműflotta-tábla)* |
| 6. Telephely | 8 | 6 | 2 |
| 7. Hatás-indikátorok | 7 | 6 | 1 |
| 9. Nyilatkozatok | 9 | 9 | 0 |
| **8. Csatolt PDF-ek** | **22** | **21** | **1** |
| **ÖSSZESEN** | **152** | **88** | **64** |

*A jármű- és költség-altáblák "opc" jelzésűek a HTML-ben, mert a `*` markert csak a fej-mezőre tették — **gyakorlatilag mind kötelező**, ha valóban annyi járművet/költségsort jelentesz be.
