# STÁCIÓ 5.A — Form-katalogizáló (A.18 prompt)

> **Prompt:** A.18 — `formular_depunere_AFM_Mobilitate_Verde.html` mezők kategória szerint csoportosítva, kötelező-e + formátum
> **Idő:** 5 perc
> **Cowork-futás:** ~40 mp

---

## Form-mezők strukturált táblája

### 1. Cégadatok (10 mező)

| Mező | Kötelező | Formátum | Megjegyzés |
|------|----------|----------|------------|
| Denumire societate | ✅ | szöveg | TransOffice Trade SRL |
| CUI / CIF | ✅ | szám (8-10 cifra) | onrc.ro-ról |
| Nr. înregistrare ONRC | ✅ | szöveg (J19/421/2003) | cégkivonatból |
| Adresă sediu social | ✅ | szöveg | Odorheiu Secuiesc |
| Adresă punct de lucru | ✅ | szöveg | Calea Băieșenilor 22 |
| Județ | ✅ | dropdown | Harghita |
| Cod CAEN principal | ✅ | szám (4 jegyű) | 4649 |
| Forma juridică | ✅ | dropdown | SRL |
| Telefon contact | ✅ | szám | Márton mobil |
| Email contact | ✅ | szöveg @ szöveg | contact@transoffice.ro |

### 2. Reprezentant legal (5 mező)

| Mező | Kötelező | Formátum |
|------|----------|----------|
| Nume reprezentant | ✅ | szöveg |
| Prenume reprezentant | ✅ | szöveg |
| CNP | ✅ | szám (13 cifra) |
| Funcție | ✅ | szöveg |
| Telefon personal | ✅ | szám |

### 3. Pénzügyi adatok (8 mező)

| Mező | Kötelező | Formátum |
|------|----------|----------|
| Cifra de afaceri 2023 (RON) | ✅ | szám |
| Cifra de afaceri 2024 (RON) | ✅ | szám |
| EBITDA 2023 (RON) | ✅ | szám |
| EBITDA 2024 (RON) | ✅ | szám |
| Număr mediu salariați 2023 | ✅ | szám |
| Număr mediu salariați 2024 | ✅ | szám |
| Capitaluri proprii 31.12.2024 (RON) | ✅ | szám |
| Datorii totale 31.12.2024 (RON) | ✅ | szám |

### 4. Projektleírás (9 mező)

| Mező | Kötelező | Formátum |
|------|----------|----------|
| Titlu proiect | ✅ | szöveg (max 250 char) |
| Descriere proiect (rezumat) | ✅ | szöveg (max 2000 char) |
| Obiective specifice | ✅ | szöveg (max 1500 char) |
| Număr vehicule electrice solicitate | ✅ | szám (1-5) |
| Tip vehicule (categoria N1, N2, M1...) | ✅ | dropdown |
| Număr puncte de reîncărcare | ✅ | szám |
| Putere instalată totală (kW) | ✅ | szám |
| Buget total (RON) | ✅ | szám |
| Cofinanțare solicitată (%) | ✅ | szám (max 70%) |

### 5. Impact (5 mező)

| Mező | Kötelező | Formátum |
|------|----------|----------|
| Reducere CO2 estimată (t/an) | ✅ | szám |
| Reducere combustibil (l/an) | ✅ | szám |
| Distanță anuală cu flota nouă (km) | ✅ | szám |
| Locuri muncă create/menținute | ✅ | szám |
| Categoria de impact regional | ✅ | dropdown (Harghita = deficit) |

### 6. Mellékletek (file upload — 13 db)

| Mező | Kötelező | Formátum |
|------|----------|----------|
| Bilanț 2023 | ✅ | PDF (max 10 MB) |
| Bilanț 2024 | ✅ | PDF |
| Certificat constatator | ✅ | PDF |
| Certificat fiscal ANAF | ✅ | PDF |
| Plan de afaceri | ✅ | PDF |
| Macheta financiară | ✅ | XLSX |
| Plan de înnoire parc auto | ✅ | PDF |
| M-11 park auto existent | ✅ | PDF/XLSX |
| 3 oferte furnizori vehicule | ✅ | PDF (zip) |
| 1 oferte furnizor punct reîncărcare | ✅ | PDF |
| Document drept asupra imobilului | ✅ | PDF |
| Acord proprietar | ✅ | PDF |
| CV-uri echipa managerială | ✅ | PDF |

### 7. Declarații (5 checkbox)

| Mező | Kötelező | Formátum |
|------|----------|----------|
| Declarație eligibilitate | ✅ | checkbox + PDF feltöltés |
| Declarație de minimis | ✅ | checkbox + PDF |
| Declarație confidențialitate GDPR | ✅ | checkbox |
| Acord prelucrare date | ✅ | checkbox |
| Acord termeni și condiții | ✅ | checkbox |

---

## Összesítés

| Kategória | Mező db | Kötelező db |
|-----------|---------|-------------|
| Cégadatok | 10 | 10 |
| Reprezentant | 5 | 5 |
| Pénzügy | 8 | 8 |
| Projekt | 9 | 9 |
| Impact | 5 | 5 |
| Mellékletek (fájl) | 13 | 13 |
| Declarații | 5 | 5 |
| **ÖSSZ** | **55** | **55 (100%)** |

**Minden mező kötelező.** A form **strict validációval** működik — egy hiányzó mező = nem küldhető.
