# Projektmenedzsment & SLA Követő Eszközök -- CPS Összehasonlítás

**Dátum:** 2026-03-21
**Cél:** A CPS számára megfelelő eszköz kiválasztása, amely támogatja a projektmenedzsmentet, az SLA-k követését és az ITIL-alapú munkafolyamatokat.

---

## Értékelési szempontok (CPS-specifikus)

- Ügyfelenként eltérő SLA-k kezelése (Safety Net / Essential / Growth / Scale csomagok)
- Ticketing + projekt menedzsment egységben
- MSP-mód: több ügyfél kezelése egy felületen
- ITIL folyamatok (Incident, Change, Problem, Request)
- Automatizálás és eskalációs szabályok
- Ár/érték arány ~13 főre
- Cloud (SaaS) preferált, de self-hosted opció is szempont

---

## Eszközök összehasonlítása

### 1. Jira Service Management (Atlassian)

| | |
|---|---|
| **Típus** | ITSM + projekt menedzsment (cloud) |
| **ITIL megfelelőség** | Magas -- Incident, Problem, Change, Request |
| **SLA kezelés** | Natív, erős -- ügyfélszintű SLA-k, automatikus eskaláció |
| **MSP mód** | Korlátozott (nem dedikált MSP eszköz, de megvalósítható) |
| **Integrációk** | 3000+ (Confluence, GitHub, Slack, PagerDuty stb.) |
| **CI/CD integráció** | Erős (Atlassian ökoszisztéma) |
| **Ár (Standard)** | $19/ügynök/hó (~13 ügynök: ~$247/hó) |
| **Ár (Premium)** | $57/ügynök/hó (~13 ügynök: ~$741/hó) |
| **Ingyenes tier** | Igen, 3 ügynökig |
| **Self-hosted** | Nem (cloud only az újabb verzióban) |
| **Erősség** | Legjobb DevOps integrációk, fejlett automatizálás |
| **Gyengeség** | Drága, összetett konfiguráció, nem dedikált MSP eszköz |

**CPS értékelés:** ★★★★☆ -- Kiváló DevOps csapatnak, de MSP-hez plusz konfigurálás kell.

---

### 2. Freshservice (Freshworks)

| | |
|---|---|
| **Típus** | ITSM / MSP platform (cloud) |
| **ITIL megfelelőség** | Magas -- teljes ITIL modul készlet |
| **SLA kezelés** | Natív, fejlett -- ügyfélszintű, automatikus eskaláció, riportok |
| **MSP mód** | Igen, Growth+ tervtől dedikált MSP mód |
| **Integrációk** | Erős (Slack, Teams, Azure, AWS, Jira stb.) |
| **CI/CD integráció** | Közepes |
| **Ár (Starter)** | $19/ügynök/hó éves számlázással (~13 ügynök: ~$247/hó) |
| **Ár (Growth -- MSP)** | $49/ügynök/hó éves számlázással (~13 ügynök: ~$637/hó) |
| **Ár (Pro)** | $99/ügynök/hó (~13 ügynök: ~$1.287/hó) |
| **Ingyenes tier** | 14 napos trial |
| **Self-hosted** | Nem |
| **Erősség** | Legjobb MSP-mód, gyors bevezetés, AI funkciók |
| **Gyengeség** | Drágább a magasabb terveken, AI add-on extra cost |

**CPS értékelés:** ★★★★★ -- Legjobb jelölt MSP-ként, ha a Growth csomag megfizethető.

---

### 3. Plane.so

| | |
|---|---|
| **Típus** | Projekt menedzsment (cloud + self-hosted) |
| **ITIL megfelelőség** | Alacsony -- nem ITSM eszköz |
| **SLA kezelés** | Business tervtől (custom SLA-k), de korlátozott |
| **MSP mód** | Nincs dedikált |
| **Integrációk** | GitHub, Slack, Jira import |
| **CI/CD integráció** | Közepes |
| **Ár (Free)** | $0 (korlátozott) |
| **Ár (Pro)** | ~$6/felhasználó/hó |
| **Ár (Business)** | ~$13/felhasználó/hó (~13 fő: ~$169/hó) |
| **Ingyenes tier** | Igen |
| **Self-hosted** | Igen (nyílt forráskódú Community Edition) |
| **Erősség** | Olcsó, modern UI, self-hosted lehetőség |
| **Gyengeség** | Nem ITSM/MSP eszköz, SLA kezelés gyenge, ticketing hiányos |

**CPS értékelés:** ★★☆☆☆ -- Jó belső projekt követésre, de SLA és MSP kezelésre nem alkalmas.

---

### 4. Azure DevOps (Microsoft)

| | |
|---|---|
| **Típus** | DevOps platform (CI/CD, projekt menedzsment) |
| **ITIL megfelelőség** | Alacsony -- nem ITSM eszköz |
| **SLA kezelés** | Nincs natív SLA tracking |
| **MSP mód** | Nincs |
| **Integrációk** | Microsoft ökoszisztéma (Teams, Azure, VS Code stb.) |
| **CI/CD integráció** | Kiemelkedő (Azure Pipelines) |
| **Ár** | Ingyenes 5 felhasználóig, utána $6/felhasználó/hó |
| **Ingyenes tier** | Igen (5 felhasználó + 1800 pipeline perc) |
| **Self-hosted** | Azure DevOps Server (on-premise) |
| **Erősség** | CI/CD, Microsoft integráció, projekt boards |
| **Gyengeség** | Nincs SLA tracking, nincs ITSM, nincs MSP mód |

**CPS értékelés:** ★★☆☆☆ -- Fejlesztési pipeline-hoz kiváló, de ügyfél SLA kezelésre nem alkalmas.

---

### 5. Redmine / Easy Redmine

| | |
|---|---|
| **Típus** | Projekt menedzsment (open source, self-hosted) |
| **ITIL megfelelőség** | Közepes (Easy Redmine pluginekkel) |
| **SLA kezelés** | Csak Easy Redmine (HelpDesk modul) verzióban, natívan nem |
| **MSP mód** | Nincs dedikált |
| **Integrációk** | Pluginekkel bővíthető, de korlátozott |
| **CI/CD integráció** | Gyenge |
| **Ár (Redmine)** | Ingyenes (hosting + karbantartás = rejtett költség) |
| **Ár (Easy Redmine)** | ~$17-25/felhasználó/hó (~13 fő: ~$221-325/hó) |
| **Ingyenes tier** | Redmine: igen (self-hosted) |
| **Self-hosted** | Igen |
| **Erősség** | Nyílt forráskód, rugalmas, olcsó |
| **Gyengeség** | Régi UI, magas karbantartási igény, SLA csak pluginnel, nincs MSP mód |

**CPS értékelés:** ★★☆☆☆ -- Túl sok karbantartás, gyenge SLA és MSP támogatás.

---

### 6. ManageEngine ServiceDesk Plus

| | |
|---|---|
| **Típus** | ITSM eszköz (cloud + on-premise) |
| **ITIL megfelelőség** | Nagyon magas -- ITIL v4 tanúsított |
| **SLA kezelés** | Natív, fejlett -- site-specifikus SLA, automatikus eskaláció |
| **MSP mód** | Igen (MSP Edition elérhető) |
| **Integrációk** | ManageEngine ökoszisztéma (ADManager, OpManager, Desktop Central) |
| **CI/CD integráció** | Gyenge |
| **Ár (Standard -- cloud)** | ~$13/technikus/hó (éves) |
| **Ár (Professional)** | ~$27/technikus/hó |
| **Ár (Enterprise)** | ~$69/technikus/hó |
| **Ingyenes tier** | Igen, 5 technikusig (Standard) |
| **Self-hosted** | Igen |
| **Erősség** | Legjobb ár/érték arány ITSM-ben, erős SLA, ITIL v4 kész |
| **Gyengeség** | Régebbi UI, gyengébb DevOps integráció |

**CPS értékelés:** ★★★★☆ -- Kiváló ITIL és SLA kezelés, jó ár. Javasolt alternatíva.

---

### 7. HaloITSM / HaloPSA

| | |
|---|---|
| **Típus** | ITSM + PSA (Professional Services Automation) |
| **ITIL megfelelőség** | Magas |
| **SLA kezelés** | Natív, erős -- SLA monitoring, contract management |
| **MSP mód** | Igen, dedikált PSA modul MSP-khez |
| **Integrációk** | Microsoft 365, Azure, Slack, monitiring eszközök |
| **CI/CD integráció** | Közepes |
| **Ár** | ~$75/agent/hó (all-inclusive) |
| **Ingyenes tier** | 30 napos trial |
| **Self-hosted** | Igen |
| **Erősség** | MSP PSA + ITSM egyben, szerződés és SLA kezelés |
| **Gyengeség** | Magasabb ár, kisebb közösség |

**CPS értékelés:** ★★★★☆ -- Erős MSP PSA eszköz, ha a pénzügyi oldalra (számlázás, szerződések) is szükség van.

---

## Összesített összehasonlítás

| Eszköz | ITSM/ITIL | SLA | MSP mód | Ár (13 fő/hó) | Ajánlás |
|--------|-----------|-----|---------|----------------|---------|
| **Freshservice Growth** | ★★★★★ | ★★★★★ | ★★★★★ | ~$637 | ✅ Legjobb MSP választás |
| **Jira Service Mgmt** | ★★★★☆ | ★★★★☆ | ★★★☆☆ | ~$247-741 | ✅ DevOps fókuszhoz |
| **ManageEngine SDP** | ★★★★★ | ★★★★★ | ★★★★☆ | ~$170-900 | ✅ Legjobb ár/érték |
| **HaloPSA** | ★★★★☆ | ★★★★☆ | ★★★★★ | ~$975 | ⚠️ PSA-hoz ideális |
| **Plane.so** | ★★☆☆☆ | ★★☆☆☆ | ★☆☆☆☆ | ~$169 | ❌ SLA-hoz gyenge |
| **Azure DevOps** | ★☆☆☆☆ | ★☆☆☆☆ | ★☆☆☆☆ | ~$78 | ❌ CI/CD-hez igen, SLA-hoz nem |
| **Redmine** | ★★☆☆☆ | ★★☆☆☆ | ★☆☆☆☆ | ~$0-325 | ❌ Magas karbantartás |

---

## CPS Javaslat

### Rövid távú (azonnali): Freshservice Growth

A CPS számára a **Freshservice Growth** csomag a legjobb kiindulópont:

- Dedikált MSP mód: több ügyfél kezelése egy felületen
- SLA automatizálás csomagok szerint (Safety Net 6h, Essential 40h stb.)
- Gyors bevezetés (napokban, nem hetekben)
- ITIL v3/v4 folyamatok: Incident, Change, Problem, Request
- Freshservice Growth ár: **~$49/ügynök/hó** (éves), 13 ügynökkel = **~$637/hó**

### Közép/hosszú távú alternatíva: ManageEngine ServiceDesk Plus MSP

Ha az ár kritikus szempont:

- ManageEngine SDP Standard: **~$13/technikus/hó** -- 13 főre ~$169/hó
- ITIL v4 tanúsított, erős SLA management
- Self-hosted opció (teljes adatvédelem)

### Nem javasolt: Plane, Azure DevOps, Redmine

Ezek az eszközök **nem** alkalmasak ügyfelekkel szembeni SLA-k kezelésére MSP környezetben.

---

## Következő lépések

- [ ] Freshservice 14 napos trial indítása: https://www.freshworks.com/freshservice/
- [ ] ManageEngine SDP ingyenes tier tesztelése: https://www.manageengine.com/products/service-desk/
- [ ] SLA sablonok kidolgozása (Safety Net / Essential / Growth / Scale csomagokhoz)
- [ ] ITIL folyamatok dokumentálása (Incident, Change, Problem, Request templates)

---

*Forrás: [DevOpsSchool SLA Tools](https://www.devopsschool.com/blog/top-10-sla-management-tools-in-2025-features-pros-cons-comparison/) | [Freshservice MSP Pricing](https://msp.support.freshservice.com/support/solutions/articles/50000011279) | [Jira Service Management Pricing](https://clearfeed.ai/blogs/jira-service-management-pricing) | [Plane Pricing](https://plane.so/pricing) | [ITSM Tools Comparison](https://kanini.com/blog/itsm-software-comparison-2025-servicenow-vs-jira-vs-freshservice-vs-zendesk-vs-ivanti-vs-solarwinds/) | [Best ITSM for MSPs](https://help-desk-migration.com/itsm-software-for-msps/)*
