---
id: capture_fallback
title: Capture-only fallback
layer: processing
purpose: |
  Tier-3 feldolgozó: ha mind a Tier-1 (claude_cli) és Tier-2
  (haiku_fallback) sikertelen, a szöveg AI-parse nélkül, nyers
  szövegként kerül az inbox.md fájlba. Garantáltan működő végső fallback.
depends_on: [vault_md]
status_endpoint: /health (component: capture_fallback)
index_schema_version: 1
---

## Miért létezik

A capture guarantee az Alfred rendszer alapígérete: amit a felhasználó
begépelt, az sosem vész el. Még ha minden AI component nem elérhető,
a nyers szöveg bekerül a vaultba, és a következő Alfred sync alkalmával
feldolgozható.

## Működés

```
inbox.md append:
- 2026-05-30T14:32:00 [UNPROCESSED] Megnézni a Deák havi számokat
```

A `[UNPROCESSED]` tag jelzi Alfred-nek, hogy ezt még field-ek szerint
kell parse-olni (scope, priority, due). Az `/alf-sync` mód elvégzi ezt
a következő munkamenetben.

## Státusz értelmezés

A capture_fallback `idle` státusza normális — nem jelent hibát. Csak
aktív, ha a felsőbb tier-ek failenak. A `gap` státusz azt jelenti, hogy
maga az inbox.md írás sem sikerült (pl. filesystem hiba, read-only mount).
