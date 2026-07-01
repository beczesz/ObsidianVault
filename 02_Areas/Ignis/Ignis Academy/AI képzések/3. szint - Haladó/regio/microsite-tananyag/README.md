# Regio tananyag letöltő-microsite (deploy-kész csomag)

Cél-URL: **`ignis.academy/regio/tananyag`** · Jelszó: **`ignis387`** (a deck 13. diája erre mutat).

## Mi van itt
- `index.html` — a Regio letöltő-oldal (Ignis-stílus, `ignis387` jelszó-kapu; helyes jelszóra megjelenik a letöltés). Önálló, CDN-fontokkal, lokális asset nélkül.
- `Regio-Tananyag-v0.1.zip` — a jelenlegi Regio tananyag (a `../fiktiv_pelda/` teljes tartalma: Napsugár sandbox + CLAUDE.md-k, deviz/üzleti terv üres+kitöltött sablonok, forrás-ajánlat, szkennelt ajánlat + OCR, monitoring, F2/F4 megoldókulcsok). 32 fájl, ~342 KB.

## Deploy (amint a live site elérhető)
A live `ignis-academy` site forrása jelenleg nincs ezen a gépen (a `00_Microsite_es_tananyagok.md`-ben dokumentált `~/Downloads/munka/ExarLabs/microsite-factory/sites/ignis-academy/` út megszűnt; a mostani `D:/work/Exar/microsite-factory`-ban nincs ignis-academy). Amint megvan a repo:
1. Másold ezt a mappát a site-ba `src/regio/`-ként (a `halado/` mintájára): `index.html` → a `/regio/tananyag` route, a zip a `/regio/` alá.
2. A `halado/`-hoz hasonló route/oldal-mintát követve tedd elérhetővé a `/regio/tananyag` útvonalat.
3. Deploy: `source ../../.env && npx wrangler deploy --env production` (a factory-konvenció szerint), majd írd be a `deploy-history.md`-be.
4. Frissítsd a `00_Microsite_es_tananyagok.md` oldaltérképet a `/regio/tananyag` sorral.

## Megjegyzés
- „Egyelőre a mostani tananyaggal": a zip a jelenlegi Regio-példakészlet. Ha a végleges tananyag (pl. külön tanulói vs. oktatói csomag, valós Regio-sablonok) elkészül, új verzió: `Regio-Tananyag-v0.2.zip`, és az `index.html` letöltő-linkjét arra kell bumpolni.
- A jelszó-kapu kliens-oldali, „lágy" védelem (a jelszó a decken is látszik), nem valódi hozzáférés-védelem.
