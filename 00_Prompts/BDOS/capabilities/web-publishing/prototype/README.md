---
title: Microsite Factory — Prototype
version: 0.1
date: 2026-05-11
status: prototype
description: Cloudflare Pages Direct Upload prototípus a Microsite Factory-hoz. Egy site, egy parancs, atomi deploy. Ez a DH/Netlify workflow CF-portja.
id: d4f776db-8a80-41c4-86a1-6632b03cd321
index_schema_version: 1
---

# Microsite Factory — Prototype

Egy parancsos atomi deploy egy Cloudflare Pages projektre. Ez a Direct Upload API 5 lépéses flow-ját absztrahálja egy script mögé, hogy a hívó számára olyan egyszerű legyen mint a Netlify-os `curl` volt.

## Mit csinál

```
microsite_deploy.py <site-dir> --project=<name> [--branch=staging]
   │
   ├── Pre-deploy validáció (HTML/asset léte, build-szám, manifest sync)
   ├── Asset hashelés (blake3) → manifest készítés
   ├── CF API: upload-token (JWT)
   ├── CF API: assets upload (batch, max 50 MB)
   ├── CF API: upsert-hashes
   ├── CF API: deployment létrehozása (production vagy branch=staging)
   └── Status polling → URL kiírás
```

## Setup (egyszeri)

1. **Token** — lásd a kapacitás `infrastructure.md` STEP 1 szekcióját
2. **`.env`** fájl valahova (NE a vault-ba):
   ```bash
   CF_API_TOKEN=<token>
   CF_ACCOUNT_ID=f2166aa3fcc9e0e7b888aaaeb4db0517
   ```
3. **Python deps:**
   ```bash
   pip install requests requests-toolbelt blake3 python-dotenv
   ```
4. **Pages projekt létrehozása** (egyszeri / projekt):
   - Dashboardon Workers & Pages → Create application → Pages → "Upload assets" → projekt név
   - Vagy API-ból (lásd `create_project.py` később)

## Használat

```bash
# .env betöltve
export $(cat ~/microsite-factory.env | xargs)

# Production deploy
./microsite_deploy.py ./my-site --project=microsite-factory-test

# Staging deploy (preview URL)
./microsite_deploy.py ./my-site --project=microsite-factory-test --branch=staging
```

## Site mappa-struktúra (várt)

```
my-site/
├── index.html
├── manifest.json    ← {build, version, generated_at}
├── screens/         ← opcionális
│   └── *.html
├── assets/
│   ├── css/
│   ├── js/
│   └── img/
└── pre-deploy-check.py   ← opcionális, ha létezik fut
```

A manifest.json a DH-konvencióból jön: build számot tart, és az index.html inline-jával szinkronban kell legyen.

## Mit NEM csinál még

- DNS bind (custom domain automatika)
- Cache purge deploy után
- Rollback
- Több site batch deploy
- Progress bar / pretty output

Ezek a következő iterációkban.

## Hivatkozott

- Capability belépő: [`../CLAUDE.md`](../CLAUDE.md)
- Infrastruktúra-dosszié (API endpoints, gotchas): [`../infrastructure.md`](../infrastructure.md)
- DH precedens (Netlify workflow): `02_Areas/Deák Húsüzlet/design/README.md`
