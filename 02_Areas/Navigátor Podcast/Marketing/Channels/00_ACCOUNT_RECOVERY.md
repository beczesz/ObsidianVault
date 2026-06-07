---
title: "Account Recovery & Credential Map"
date: 2026-05-25
author: Becze Szabolcs
status: active
description: "Központi nyilvántartás az összes social media fiók email-jelszó-telefonszám függőségeiről és recovery chain-jeiről."
id: sys-account-recovery-001
index_schema_version: 1
bdos_index: true
---

# Account Recovery & Credential Map

> **BIZTONSÁGI MEGJEGYZÉS:** Ez a fájl NEM tartalmaz jelszavakat — csak az email-fiók-telefon függőségi láncot dokumentálja. Jelszavakat password manager-ben kell tárolni.

## Recovery dependency graph

```
mediamuhely11@gmail.com          ← ⚠️ Peter Maria-nál van a jelszó
  └── fokuszpont2024@gmail.com   ← recovery email a fenti
       └── @fokuszpont_ (Instagram, Meta Accounts Center)
            └── telefonszám: asszisztens száma ← CSERÉLNI

beczesz.szabolcs@gmail.com       ← Szabolcs fő email
  └── YouTube Brand Account (Navigátor Podcast)
  └── Google Cloud projekt (Navigator YouTube MCP v2)
  └── @beczesz (Instagram — személyes, Edit Profile-on látszott)

navigator.podc@gmail.com         ← Podcast dedikált email
  └── (felhasználása tisztázandó)
```

## Fiók leltár

| # | Fiók / Handle | Platform | Email | Telefonszám | Recovery email | Státusz |
|---|---------------|----------|-------|-------------|----------------|---------|
| 1 | @NavigatorPodcast | YouTube | beczesz.szabolcs@gmail.com | — | — | ✅ OK |
| 2 | @beczesz | Instagram | beczesz.szabolcs@gmail.com (?) | — | — | 🔍 Tisztázandó |
| 3 | @fokuszpont_ | Instagram | fokuszpont2024@gmail.com | ⚠️ asszisztens | mediamuhely11@gmail.com | ❌ Recovery szükséges |
| 4 | Navigator Podcast | Instagram (?) | — | — | — | 🔍 Létezik? |
| 5 | — | Facebook (személyes) | — | — | — | 🔍 Audit szükséges |
| 6 | — | Facebook (Navigator) | — | — | — | 🔍 Audit szükséges |
| 7 | — | TikTok | — | — | — | 🔍 Audit szükséges |
| 8 | — | X (Twitter) | — | — | — | 🔍 Audit szükséges |

## Email fiókok

| Email | Tulajdonos | Jelszó hozzáférés | Használat |
|-------|-----------|-------------------|-----------|
| beczesz.szabolcs@gmail.com | Szabolcs | ✅ | YouTube, Google Cloud, Instagram @beczesz |
| navigator.podc@gmail.com | Szabolcs | ✅ (?) | Podcast dedikált |
| fokuszpont2024@gmail.com | Szabolcs / Fókuszpont | ❌ Recovery kell | Instagram @fokuszpont_ |
| mediamuhely11@gmail.com | Peter Maria | ❌ Jelszó szükséges | Recovery email fokuszpont2024-hez |

## Akcióterv

### Sürgős (most)
- [ ] **Peter Maria-tól megkérni a mediamuhely11@gmail.com jelszavát**
- [ ] mediamuhely11@gmail.com-mal recovery-zni fokuszpont2024@gmail.com-ot
- [ ] fokuszpont2024@gmail.com jelszó reset + hozzáférés biztosítása
- [ ] @fokuszpont_ telefonszám cseréje

### Rövid távon
- [ ] Minden fiók email-telefon párosítás megerősítése
- [ ] Password manager beállítása (ha nincs)
- [ ] 2FA engedélyezése minden fiókon
- [ ] Backup recovery kódok mentése

### Hosszú távon
- [ ] Negyedéves credential audit
- [ ] Recovery drill (tudja-e mindenki, hogyan kell visszaszerezni a fiókját?)
