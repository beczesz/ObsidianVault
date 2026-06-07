---
title: "Igény felmérése — email from Ács Gusztáv (Raab Computer)"
date: 2026-05-27
status: archive
description: "Verbatim archive of the inbound requirement email from Ács Gusztáv (Raab Computer Kft.) to becze.szabolcs@sonrisa.hu, 2026-05-27. Contains the sharpened Kubernetes cluster requirement + the original short brief from the end client's IT lead. Source document for the Raab Computer K8s opportunity."
tags: [raab-computer, email, requirement, kubernetes, lang-hu, archive]
from: "Ács Gusztáv <acsg@raabcomputer.hu>"
to: "becze.szabolcs@sonrisa.hu"
cc: "Horváth Mihály <horvathm@raabcomputer.hu>"
subject: "Igény felmérése"
received: "2026-05-27 11:19 CEST"
source_file: "C:\\Users\\EvoComputers\\Downloads\\Igény felmérése.eml"
id: fbc8f2ff-ed73-46e0-8b10-3d03ab3f82ac
index_schema_version: 1
---

# Igény felmérése — email archive

> **From:** Ács Gusztáv <acsg@raabcomputer.hu>
> **To:** becze.szabolcs@sonrisa.hu
> **CC:** Horváth Mihály <horvathm@raabcomputer.hu>
> **Subject:** Igény felmérése
> **Date:** 2026-05-27 11:19 CEST

---

Kedves Szabolcs!

Sikerült elérnem a cég informatikai vezetőjét, aki pontosított pár dolgot az alábbi igény megfogalmazáson (eredeti üzenet).

Ez elsősorban arra vonatkozott, hogy az első, a fejlesztési szakaszban (1-2 év) kellene első körben a cég környezetében kialakítani a kubernetes clustert, a lenti feladatokra, valamint annak support-ját megoldani, ami ebben az időszakban még nem 7/24, ez utóbbira az éles indulás után lenne szükség.

Most első körben a lenti leírás alapján egy indikatív ajánlatra lenne szükségük, hogy a vezetőség felé ez beterjeszthető legyen. Azt kérték, hogy ezt még péntek előtt valamilyen formában adjuk meg, ha ez lehetséges, fontosnak jelölték ezt meg. Ez megelőzné a pénteki megbeszélésünket, de ha ebben tudsz segíteni azt megköszönöm!

## Az eredeti rövid igény

> "Ahogy arról tegnap beszéltünk, kérlek nézzétek meg, hogy az alábbi környezet kialakításában tudnátok-e segítséget nyújtani nekünk.
>
> A rendszer magja egy Kubernetes cluster lenne. A clustert úgy kellene kialakítani, hogy az abban megtalálható egyes node-okat, podokat menedzselni tudjuk. Terhelés függvényében (ha lehet automatikusan) új podokat hozhassunk létre, azok regisztrálásával a hálózaton, tudjuk, hogy melyik microservice hol fut, hogyan lehet elérni. Szabályozva legyen, hogy az egyes service-ek milyen más service-ekkel kommunikálhatnak (hitelesítés és jogosultságkezelés). Az egyes node-ok, podok, microservice-ek állapota monitorozva legyen (health check), szükség esetén újraindítás, vagy ha ez nem sikerül, akkor riasztási mechanizmus be legyen építve.
>
> A cluster működhessen több adatközpontban is (pl cég hálózatban és egyes elemei Vultr-ben vagy más felhőszolgáltatónál). Arra készülünk, hogy olyan 100-as nagyságrendben lenne pod, illetve microservice létrehozva és futtatva a clusterben.
>
> Ebben gondolkodunk, ha esetleg javaslatotok lenne az elképzeléseinkkel kapcsolatban, akkor ne tartsátok magatokban! 🙂
>
> Természetesen a rendszer kiépítésén kívül az üzemeltetésében is számítanánk rátok a későbbiekben.
>
> Köszi szépen, ha elgondolkodtok rajta!"

---

Tisztelettel:

**Ács Gusztáv**
Raab Computer Kft.
9024 Győr, Malomszéki u. 7.
Tel.: 96/526-860 · Fax: 96/526-861
Mobil: 30/2172779
email: acsg@raabcomputer.hu

---

*(Email also contained an HTML alternative + the Raab Computer logo image attachment `logo_kicsi.JPG`. Original .eml preserved at the source_file path in frontmatter.)*
