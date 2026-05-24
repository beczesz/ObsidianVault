# Deák Húsmíves — Wireframe Gallery

## Struktúra
- `index.html` — Wireframe gallery (gombok az egyes wireframe-ekhez) · Build #3
- Minden wireframe külön HTML fájl, önállóan is megnyitható

## Aktuális wireframe-ek
| Fájl | Leírás |
|------|--------|
| `v0.3-wireframes-v3.html` | v0.3 Savings Engine — spórolás számláló, post-order recap, családi csomagok, újrarendelés, swap javaslat |
| `v0.3-consent-gdpr.html` | GDPR Consent & ÁSZF (v2) — regisztrációs consent, béléptető kapu, cookie banner, kétnyelvűség (DH-132 + DH-137) |

## Deploy
- **Netlify site:** [deakhus.netlify.app](https://deakhus.netlify.app)
- Deploy: zip-ben minden fájl → Netlify file upload (atomi deploy — minden fájl lecserélődik)
- A deploy csak Szabolcs jóváhagyásával történik
- **FONTOS: Minden deploy kreditet fogyaszt — mindig tesztelj lokálisan (Chrome JS inject + resize) mielőtt deployolsz\!**

## Szabályok
- Mindig legyen `index.html` ami összefogja az összes wireframe-et (még ha csak 1 van)
- Az `index.html` csak gombokat tartalmazzon (NEM iframe preview)
- A wireframe-ek külön fájlban, külön megnyithatóak
- Build szám a headerben — minden újrageráláskor nő
- **Ha egy wireframe fájl nem létezik, NEM kap gombot az index.html-ben**
- **Minden verzióváltásnál fríssítsd a README.md-t is**

## Changelog
- **Build #3 v2** (2026-04-16): GDPR wireframe frissítve: cookie banner tab, kétnyelvűség (HU+RO), nem-regisztrált userek kezelése
- **Build #3** (2026-04-16): GDPR Consent & ÁSZF wireframe hozzáadva (DH-132), index.html fríssítve
- **Build #2** (2026-04-11): Tiszta gomb-alapú gallery, mobil responsive CSS hozzáadva a wireframe-ekhez
- **Build #1** (2026-04-11): Első verzió iframe preview-val (deprecated)
