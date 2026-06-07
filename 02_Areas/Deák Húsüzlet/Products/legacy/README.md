---
title: "Legacy / Archived Files — DO NOT USE"
date: 2026-05-07
author: Becze Szabolcs
status: active
description: "Archived pre-v1.0 product files kept for historical reference only; current source of truth is Products/MASTER/products/*.md generated as products-v1.X.json since the versioning scheme changed from 3.x to 1.0 on 2026-05-07."
description_source: auto
description_hash: 1f4186bc0cba7b28
id: 320a3641-6d35-4c21-9f96-53ceb969fd2e
index_schema_version: 1
bdos_index: true
---
# Legacy / Archived Files — DO NOT USE

> These files are **archived from the pre-v1.0 era** when the product versioning scheme used 3.x numbers.
> They are kept for historical reference only.
> **Source of truth is the current `Products/MASTER/products/*.md`** — generated as `products-v1.X.json`.

## Files

| File | Origin | Note |
|------|--------|------|
| `products_v3.1.json` | Original Google Sheet sync (2026-03-31) | 37 products, simple flat list |
| `products-v3.2.json` | Build experiment (2026-05-07 reggel) | Uses old (incorrect) self-made schema |
| `products-v1.0.json` | Build experiment (2026-05-07 délután) | 1 product, schema v1.0 (replaced by v1.1) |
| `product_listing_v0.7_*.md` | Auto-generated MD listings (legacy) | Replaced by build pipeline |
| `deploy_*` | Old deploy artifacts | Replaced in deploy zip from build #79 |

## Why archived?

The product data is now versioned starting at **v1.0** (and currently at **v1.1**), aligned with the production Frappe backend schema. The old 3.x numbering was a legacy continuity artifact and was **dropped on 2026-05-07**.

If you need to reference the old data, look here. But for any active work, use the current `MASTER/` system.
