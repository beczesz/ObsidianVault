# CLAUDE.md: Napsugár Tejüzem projekt (THR)

> Projekt-szintű szabálykönyv. A gyökér `../../CLAUDE.md` általános szabályai IDE is érvényesek; itt csak a projekt-specifikumok.

## A projekt
- **Beneficiar:** SC NAPSUGÁR TEJÜZEM SRL (fiktív), Cristuru Secuiesc, jud. Harghita
- **Kód:** THR
- **Tárgy:** tejfeldolgozó-üzem bővítése (építési beruházás)
- **Finanszírozás:** PNRR-szerű, TVA 19%, curs 4,97 lei/EUR
- **Beruházás:** deviz general TOTAL 6 455 000 lei fără TVA (7 681 450 cu TVA)
- **Fázis:** implementation (kivitelezés folyik, monitoring aktív)

## Hol mi van ebben a projektben
- `01_Cerere_de_finantare/`: Anexa B üzleti terv (kitöltött), a pályázati deviz
- `02_Editabil/`: a kanonikus deviz general (szerkeszthető master)
- `08_Dosare_de_achizitii/04.04_DAL_Lucrari/`: a munkálatok beszerzése: `Scan/` a kivitelező szkennelt ajánlata, `Editabil/` az abból kinyert (OCR) használható adat + a forrás-ajánlat
- `10_Monitorizare/`: a Centralizator (situații de lucrări követés: SL1/SL2/SL3 + Rest de executat)

## Tipikus feladatok itt (amit az AI-tól kérünk)
1. Szkennelt ajánlat (`04.04_DAL_Lucrari/Scan/`) → használható md/tábla (`.../Editabil/`).
2. Deviz-templét kitöltése forrásból (killer-demo).
3. Ajánlatkérés vs. ajánlat tételes összevetése.
4. Monitoring Centralizator frissítése az új situație de lucrări-val.
