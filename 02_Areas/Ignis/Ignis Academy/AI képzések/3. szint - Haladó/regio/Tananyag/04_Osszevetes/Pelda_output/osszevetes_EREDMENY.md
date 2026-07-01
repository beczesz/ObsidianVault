# Ajánlatkérés (deviz) és ajánlat összevetése: Napsugár (F4 várt eredmény)

> Az F4 demó „megoldókulcsa". Az AI egyszerre nézi az **ajánlatkérést** (a deviz general Cap. 4 = investiția de bază, `02_Editabil` deviz) és a **kivitelező ajánlatát** (az OCR-ből: `..._OCR.md`), majd tételesen összeveti. Minden érték lei, fără TVA.

## Tételes összevetés (Cap. 4, investiția de bază)

| Deviz-tétel | Ajánlatkérés (deviz) | Ajánlat (kivitelező) | Eltérés | Megjegyzés |
|---|---:|---:|---:|---|
| 4.1 Construcții și instalații | 3 190 000 | 3 190 000 | 0 | tételesen egyezik (Hala, Depozit, Centrală, Amenajări) |
| 4.2 Montaj utilaje | 95 000 | 95 000 | 0 | egyezik |
| 4.3 Utilaje cu montaj (linie procesare) | 1 850 000 | 1 850 000 | 0 | egyezik |
| 4.5 Dotări | 240 000 | 240 000 | 0 | egyezik |
| **4.6 Active necorporale (szoftver)** | **60 000** | **0** | **−60 000** | ⚠ **az ajánlat nem tartalmazza** |
| **Cap. 4 összesen** | **5 435 000** | **5 375 000** | **−60 000** | |

## A megtalált eltérés (amit külön-külön olvasva kihagynál)
Az ajánlat a construcții, montaj, utilaje és dotări tételeket fillérre pontosan lefedi, a **4.6 Active necorporale (60 000 lej, szoftver)** viszont kimaradt belőle. Ez nem a kivitelező munkája, hanem külön beszerzés (`04.05_DAF_Furnizare`), vagy tisztázni kell a beneficiárral. Pontosan ez az a tétel, amit az F2 egyeztetésen is jeleztek.

## Ellenőrzési fegyelem
- A számokat a szkennelt ajánlat OCR-jéből vettük. **Kontroll-összeg:** az ajánlat tételeinek összege 5 375 000, és ennyi a feltüntetett végösszeg is. ✓
- Eltérés esetén mindig a **forrás** (a deviz kiírás) az irányadó: az AI jelzi, az ember dönt.
