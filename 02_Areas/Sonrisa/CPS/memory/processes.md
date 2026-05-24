# Recurring Processes

**Last Updated:** 2026-04-16

---

## Monthly TIG Review -- Bánfi István

**What:** Verify contractor (Bánfi István) hours, get AM sign-off, accept TIG officially.
**When:** Monthly (after month-end)
**Owner:** Szabolcs

### Key Links

- **TIG Folder (SharePoint):** https://sonrisakft-my.sharepoint.com/personal/banfi_istvan_sonrisa_hu/_layouts/15/onedrive.aspx?e=5%3A24036c3d960b4954a312eaac240bce75&sharingv2=true&fromShare=true&at=9&CT=1776347213013&OR=OWA%2DNT%2DMail&CID=b8b162d8%2Dc917%2Da0af%2D94d9%2Dc512c9eb1868&id=%2Fpersonal%2Fbanfi%5Fistvan%5Fsonrisa%5Fhu%2FDocuments%2FTIG&FolderCTID=0x0120008670C0D5F4C2174CA75D3756ADC51DA1&view=0
  - István uploads his TIGs here every month
- **Detailed Timesheet (SharePoint):** https://sonrisakft.sharepoint.com/sites/sales/Megosztott%20dokumentumok/Forms/AllItems.aspx?id=%2Fsites%2Fsales%2FMegosztott%20dokumentumok%2FGeneral%2FPlanning%2FServices%2FCloud%20Platform%20Services%2Fraports&viewid=dfd2979e%2D7b28%2D49ac%2D9be0%2Dc493d63eeabc
  - Raw hour data per project/month

### Process Steps

1. **Check TIG upload** -- Go to TIG Folder, verify István uploaded the current month's TIG
2. **Cross-reference with timesheet** -- Open the detailed timesheet for the given month, check raw numbers per project
3. **Identify AMs** -- From the timesheet, note which projects István worked on and who the AM is for each (varies monthly)
4. **Draft confirmation emails (Hungarian)** -- Write to each AM asking them to confirm the hours for their project
5. **Optionally CC the PM** -- If there's a PM on the project, include them too
6. **Collect confirmations** -- Wait for all AMs to reply with acceptance
7. **Accept TIG** -- Once all confirmations received, officially accept István's TIG

### Email Template (Hungarian)

Subject: Bánfi István - [HÓNAP] havi órák visszaigazolása - [PROJEKT NÉV]

---

Szia [AM NÉV],

Bánfi István [HÓNAP] havi teljesítményigazolását szeretném lezárni. A kimutatás szerint a Te projektedre ([PROJEKT NÉV]) **[X] órát** dolgozott ebben a hónapban.

Kérlek nézd át, és ha rendben van, erősítsd meg nekem egy rövid válaszban.

Ha bármi eltérést látsz, jelezd és egyeztetünk.

Köszönöm,
Szabolcs

---

### Key Contacts

- **Nagy Sándor** (PM): nagy.sandor.pm@sonrisa.hu
- **Sajó Péter** (AM): peter.sajo@sonrisa.hu
- **Szellár Tamara** (Finance): szellar.tamara@sonrisa.hu

### Email Preparation

1. Compare TIG hours with Sontime data per project -- all must match
2. Send one email per project to the AM (CC: PM + Finance)
3. Email is in Hungarian, short and to the point -- one sentence asking to acknowledge the hours
4. Subject format: `Bánfi István - [HÓNAP] havi órák visszaigazolása - [PROJEKT NÉV]`
5. After all AMs confirm, officially accept the TIG

### Notes

- AMs vary monthly depending on which projects István was assigned to
- The timesheet is the source of truth for raw numbers
- TIG = Teljesítmény Igazolás (Certificate of Completion)
- This process could be built into a Cowork skill later (trigger: "tig review" or "istvan hours")
- Project name mapping (TIG vs Sontime):
  - "CPS - Architektúra tervezés" = "Cloud Platform Services"
  - "Idomsoft - architektúra tervezés" = "Idomsoft - Legacy költöztetés"
  - "Silver 3.0" = "Silver 3.0"
  - "Sonrisa Presales" = "Sonrisa Presales"
