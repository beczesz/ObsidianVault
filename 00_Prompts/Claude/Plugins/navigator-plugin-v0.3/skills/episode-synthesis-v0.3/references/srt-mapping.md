# SRT fájlnév → EP szám mapping

## Korai epizódok (EP01-EP13) — nincs EP szám a fájlnévben

A podcast első epizódjainál a fájlnév sorszámot tartalmaz (1., 2., 3...) de NEM EP számot.
Az offset: **EP szám = SRT sorszám + 1** (mert EP01 a Bevezető, EP02 az első vendéges).

| EP | SRT fájlnév (prefix) | Vendég |
|----|---------------------|--------|
| EP01 | `20240526 - Navigátor Podcast` | Bevezető (nincs vendég) |
| EP02 | `20240604 - 1. Vinczellér Árpád` | Vinczellér Árpád |
| EP03 | `20240618 - 2. Lukácsi Kata` | Lukácsi Kata |
| EP04 | `20240702 - 3. Nagy Lajos` | Nagy Lajos |
| EP05 | `20240716 - 4. Kirmájer Erika, Szabó Réka` | Kirmájer Erika, Szabó Réka |
| EP06 | `20240730 - 5. Szakács-Paál István` | Szakács-Paál István |
| EP07 | `20240813 - 6. Bencze Edit` | Bencze Edit |
| EP08 | `20240827 - 7. Széles Ferenc` | Széles Ferenc |
| EP09 | `20240910 - 8. Dr. Kurtus Aranka` | Dr. Kurtus Aranka |
| EP10 | `20240926 - 9. Dr. Simon Károly` | Dr. Simon Károly (= EP09 duplikátum) |
| EP11 | `20241008 - 10. Elekes István` | Elekes István |
| EP12 | `20241022 - 11. Pálfi Kinga` | Pálfi Kinga |
| EP13 | `20241105 - 12. Bándi Domokos` | Bándi Domokos |

## EP14-tól — EP szám a fájlnévben

Keresés: `f'EP {ep_num}' in filename or f'EP{ep_num}' in filename`

Példa: `20241203 - A nárcizmus rejtett arcai ｜ Bencze Edit ｜ EP14.hu.srt`

## Sorozatok (NEM epizód-szintézisek)

| Sorozat | SRT fájlnév minta | Synthesis mappa |
|---------|-------------------|-----------------|
| 7 Szokás (Covey) | `7 Szokás EP1`, `7 Szokás EP2`... | `Series/7Szokas EP1 - ...` |
| KAW (Betenbough) | `fejezet – Bevezetés a Királyságba` stb. | `Series/KAW 1 - ...` |
| Közösség | `Navigátor Közösség ｜ EP 01` stb. | `Series/Kozosseg EP01 - ...` |

**FIGYELEM:** A sorozat EP számok ÜTKÖZNEK a főepizód EP számokkal!
Mindig nézd a teljes fájlnevet.

## YouTube videó ID-k (ismert)

| EP | YouTube ID | EP | YouTube ID |
|----|-----------|-----|-----------|
| EP02 | `q7Q5aUY0w50` | EP22 | `yc50GxmlMNg` |
| EP03 | `1FmIRZ9kkVg` | EP23 | `XrvpAIs4I3U` |
| EP05 | `J9175griS7c` | EP24 | `X3Rhtpal5tA` |
| EP06 | `1hbim8vN9gQ` | EP25 | `-CBBMeGz6bI` |
| EP08 | `j_GotIYqXKs` | EP26 | `yhUxLJO5OWY` |
| EP09 | `Bzm2Ddxeni4` | EP27 | `RY14eU8NPU0` |
| EP11 | `wVLydj4eUFg` | EP28 | — |
| EP12 | `0fAIJ99yur0` | EP29 | — |
| EP13 | `CEBAnmXFlr8` | EP30 | `S8JeFX3V07k` |
| EP15 | `KYR2-VI3U3M` | EP31 | `h2i9WNsdWrc` |
| EP16 | `CR54gv3Ax8s` | EP32 | `SlSRu1yE6ws` |
| EP18 | `JhquTzM8dfU` | EP33 | `s8C6QyRpJhA` |
| EP19 | `DeGjg1EM7Qw` | EP34 | `vS0SK2x1NQI` |
| EP20 | `34K4pwugxLc` | EP35 | `X1EF52Eez4o` |
| EP21 | `ymSgaBRwN4k` | EP38 | `o4xWWp5qZDM` |

Gyors hozzáférés ha van ID:
```
Analytics: studio.youtube.com/video/{ID}/analytics/tab-overview/period-default
Comments: studio.youtube.com/video/{ID}/comments
Details:  studio.youtube.com/video/{ID}/edit
```
