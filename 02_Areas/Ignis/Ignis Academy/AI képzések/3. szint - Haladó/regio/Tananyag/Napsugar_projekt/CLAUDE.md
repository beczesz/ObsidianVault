# CLAUDE.md: Regio Consult (fiktív sandbox)

> Ezt olvassa el az AI ELŐSZÖR, valahányszor ebben a mappában dolgozik. Ez a cég „memóriája" és szabálykönyve. (Teljesen fiktív gyakorló-példa, a valós RC belső sztenderd szerkezetén.)

## Kik vagyunk
Regio Consult: EU / állami pályázati tanácsadó. 3 iroda, 21 fő. Minden projekt AZONOS, strukturált rendszerben él, hogy bárki fél óra alatt átvegyen egy ismeretlen projektet.

## Elnevezési konvenció (KÖTELEZŐ)
`sorszám_dokumentumnév_Iniciálé_dátum`, például `01.a_ST_Cerere de finantare_ISZ_08.11.2021`.
- sorszám: a Dokumentumkövetés szerint (01.a, 04.04, ...)
- kód: projekt-kód (pl. THR = Napsugár Tejüzem)
- dátum: NN.HH.ÉÉÉÉ

## Mappa-hierarchia (minden projekt így néz ki)
| Mappa | Tartalom |
|---|---|
| `01_Cerere_de_finantare` | pályázati dosszié (üzleti terv/Anexa B, deviz), datált variánsok |
| `02_Editabil` | a végleges, SZERKESZTHETŐ dokumentumok (egyetlen aktuális verzió) |
| `03_Documente_de_lucru` | munkaanyag, kapott dokumentumok, régi verziók |
| `04_Scan` | leadott PDF-ek, beadási sorrendben |
| `05_Semnat` | elektronikusan aláírt, beadott dokumentumok |
| `06_Contract_de_finantare` | támogatási szerződés + acte adiționale |
| `07_Proiect_tehnic` | technikai terv (edit + scan) |
| `08_Dosare_de_achizitii` | beszerzési dossziék: `04.01 DAC` konzultáció, `04.02 DAP` tervezés, `04.03 DAD` dirigenție, `04.04 DAL` munkálatok, `04.05 DAF` szállítás |
| `09_Cereri_de_plata` | kifizetési/elszámolási kérések (CR/CP), alkönyvtárakkal |
| `10_Monitorizare` | Rapoarte de progres, notificări, Centralizator (SL követés) |

## Navigáció (kalandkönyv-elv)
- Ha egy KONKRÉT projekten dolgozol → `Projects/<KÓD>_<Név>/`, és ott olvasd el a projekt saját `CLAUDE.md`-jét.
- Jelenlegi projekt: **Napsugár Tejüzem** → `Projects/THR_Napsugar_Tejuzem/`.
- Általános céges beállítások → `00_General_info/`.

## Kommunikáció / formátum szabályok
- Brand: Regio Consult. Minden dokumentum: **Verdana 9**.
- Alap kommunikáció email; „chat" jellegű egyeztetés WhatsApp; online meeting Teams; nagy fájl Wetransfer.
- Munkaidő 8:00-19:00; emailt/hívást ezen belül.

## Az AI-nak szóló alapszabályok
- A `02_Editabil` a kanonikus, aktuális verzió. Régi/kapott anyag → `03_Documente_de_lucru`.
- Levédett Excel-cellák (képletek) NEM módosítandók; csak a szürke input-cellákba írj.
- Bármit generálsz, a fenti sztenderdet és elnevezést kövesd.
