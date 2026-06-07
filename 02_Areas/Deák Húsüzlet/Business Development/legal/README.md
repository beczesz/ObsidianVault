---
description: "Deák Húsmíves online platform összes jogi dokumentumát tartalmazó gyűjtemény: v1.0 szerződési feltételek, adatvédelmi szabályzatok, és szerződések három nyelven, jogi review-ra várakozva. Platform fejlesztők és jogi csapat használja a dokumentum státusz és verziózás követésére."
description_source: auto
description_hash: e2a3da764558d230
file: README.md
version: v1.0
date: 2026-04-17
status: ACTIVE — extracted legal docs from wireframes
owner: Szabolcs
id: 12216f07-c88a-4ec4-a718-bb950310e3d2
index_schema_version: 1
---
# Legal dokumentumok — Deák Húsmíves Online Platform

## Áttekintés

Ebben a mappában találhatóak a platform jogi dokumentumai.
A `v1.0` az elsőként a wireframe-ekből kibányászott draftokat jelöli — ezek **jogi review-ra várnak**.

## Fájlok (v1.0 — 2026-04-17 extrakció)

### Általános Szerződési Feltételek (ÁSZF)
Forrás: `design/wireframes/aszf-wireframe-v2.html`

| Nyelv | Fájl |
|-------|------|
| 🇭🇺 Magyar | [aszf-v1.0-hu.md](./aszf-v1.0-hu.md) |
| 🇷🇴 Română | [aszf-v1.0-ro.md](./aszf-v1.0-ro.md) |
| 🇬🇧 English | [aszf-v1.0-en.md](./aszf-v1.0-en.md) |

### Adatvédelmi Szabályzat (Privacy Policy)
Forrás: `design/wireframes/privacy-policy-wireframe-v2.html`

| Nyelv | Fájl |
|-------|------|
| 🇭🇺 Magyar | [privacy-policy-v1.0-hu.md](./privacy-policy-v1.0-hu.md) |
| 🇷🇴 Română | [privacy-policy-v1.0-ro.md](./privacy-policy-v1.0-ro.md) |
| 🇬🇧 English | [privacy-policy-v1.0-en.md](./privacy-policy-v1.0-en.md) |

### Szerződések

| Dokumentum | Verzió | Státusz |
|-----------|--------|---------|
| [contract-cadru-exar-deak-v1.2.docx](./contract-cadru-exar-deak-v1.2.docx) | v1.2 | aláírásra vár |
| [comanda-nr1-phase1-v1.3.docx](./comanda-nr1-phase1-v1.3.docx) | v1.3 | ✅ aláírásra vár (6,8% helyes) |

### Archívum
A `archive/` mappa tartalmazza a korábbi verziókat.

## Státusz mátrix

| Dokumentum | Draft | Jogi review | Élesítve |
|-----------|-------|-------------|----------|
| ÁSZF HU | ✅ v1.0 | ⏳ | ❌ |
| ÁSZF RO | ✅ v1.0 | ⏳ | ❌ |
| ÁSZF EN | ✅ v1.0 | ⏳ | ❌ |
| Privacy HU | ✅ v1.0 | ⏳ | ❌ |
| Privacy RO | ✅ v1.0 | ⏳ | ❌ (de `deakhus.ro/privacy` él — ellenőrizni!) |
| Privacy EN | ✅ v1.0 | ⏳ | ❌ |
| Contract-cadru | ✅ v1.2 | ⏳ | ⏳ aláírás |
| Comanda nr.1 | ✅ v1.3 | ⏳ | ⏳ aláírásra vár (6,8% helyes) |

## Verziózási szabály

- **v1.0** — wireframe-ből kinyert draft (2026-04-17)
- **v1.1+** — szöveg javítások, frissítések
- **v2.0** — jogi review utáni átfogó revízió
- **v2.x** — jogi review utáni kisebb módosítások
- **v3.0** — éles verzió (aláírt szerződéssel összhangban)

Minden új verzió új fájl — a régit `archive/`-ba mozgatni vagy `**prefix`-szel jelölni.

## Vonatkozó Jira ticketek

- [DH-130](https://exarlabs.atlassian.net/browse/DH-130) — ÁSZF draft (v1.0 kész → Jira Done update)
- [DH-131](https://exarlabs.atlassian.net/browse/DH-131) — Impresszum (még nincs)
- [DH-132](https://exarlabs.atlassian.net/browse/DH-132) — GDPR consent checkbox (implementáció)
- [DH-133](https://exarlabs.atlassian.net/browse/DH-133) — Jogi szolgáltató tisztázás → marketplace modell megerősítve
- [DH-134](https://exarlabs.atlassian.net/browse/DH-134) — Privacy Policy frissítés (v0.4)
- [DH-136](https://exarlabs.atlassian.net/browse/DH-136) — ANSVSA engedély → Deáknál megvan
- [DH-137](https://exarlabs.atlassian.net/browse/DH-137) — Cookie policy
