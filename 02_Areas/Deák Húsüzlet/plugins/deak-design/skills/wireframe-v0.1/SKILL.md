---
name: wireframe-v0.1
version: 0.1
description: >
  Deák Húsmíves wireframe generálási skill. Aktiválódjon minden wireframe, HTML prototípus,
  UI screen tervezési feladatnál. Biztosítja, hogy az összes wireframe konzisztens
  design token-eket, phone frame struktúrát és konvenciókat használjon.
  Trigger szavak: wireframe, tervezzünk, prototípus, screen design, UI terv, HTML terv,
  mockup, frame, deploy wireframe.
changelog:
  - version: "0.1"
    date: "2026-04-17"
    changes: "Első kiadás — design tokenek, phone frame sablon, tab rendszer, deploy checklist, verziókezelési szabályok"
id: bd822e02-5b5f-4588-b8a9-b5401a3b8f37
index_schema_version: 1
---

# Deák Húsmíves — Wireframe Skill (v0.1)

> **Arany szabály:** Minden wireframe feladatnál ELŐSZÖR olvasd be a kontextus fájlokat.
> A design drift oka: a tokenek kiesnek a kontextusból. Ez a skill megakadályozza.

---

## 0. Verziókezelési szabályok (kötelező betartani!)

### Skill verzió
- A skill neve tartalmazza a verziószámot: `wireframe-v{X.Y}`
- A skill mappájának neve is tükrözi: `skills/wireframe-v{X.Y}/`
- Verzió növelés szabályai:
  - **Minor (X.Y → X.Y+1):** token frissítés, új komponens snippet, szabály pontosítás
  - **Major (X.Y → X+1.0):** struktúraváltás, teljesen új sablon, Breaking change
- Minden verzióváltásnál:
  1. A mappa neve megváltozik (`wireframe-v0.1` → `wireframe-v0.2`)
  2. A `name:` és `version:` frontmatter frissül
  3. A `changelog:` bővül az új bejegyzéssel
  4. A `PLUGIN.md` `skills:` listája frissül az új verzióra
  5. A `PLUGIN.md` `version:` mezője is nő

### Plugin verzió
- A PLUGIN.md `version:` mezője `MAJOR.MINOR.PATCH` formátumot követ
- Skill verzióváltás → Plugin MINOR növekedés (pl. 0.1.0 → 0.2.0)
- Csak doksimódosítás → Plugin PATCH növekedés (pl. 0.1.0 → 0.1.1)

### Verzióváltás workflow (step-by-step)
```
1. Módosítsd a SKILL.md tartalmát
2. Frissítsd: name: wireframe-v{ÚJ}
3. Frissítsd: version: {ÚJ}
4. Adj hozzá changelog bejegyzést
5. Nevezd át a mappát: mv wireframe-vREGI wireframe-vUJ
6. Frissítsd PLUGIN.md skills: listát
7. Frissítsd PLUGIN.md version: mezőt
```

---

## 1. Kötelező kontextus betöltés (MINDEN feladatnál, kivétel nélkül)

Mielőtt egyetlen sor HTML-t írnál, olvasd be:

```
plugins/deak-design/context/design-system.md  ← tokenek, komponensek
plugins/deak-design/context/ui-strings.md     ← magyar/román szövegek
```

Ha a feladat meglévő wireframe módosítása:
```
design/wireframes/[érintett fájl]  ← az aktuális állapot
design/wireframes/index.html       ← build szám ellenőrzés
```

**FUSE mount path pattern** (mindig így navigálj):
```python
import os
mnt = '/sessions/adoring-gifted-gates/mnt'
for item in os.scandir(mnt):
    if item.is_dir() and 'De' in item.name:
        base = item.path  # ez a valódi FUSE mount
        break
```

---

## 2. Helyes design tokenek

**CSS variables — EZEKET HASZNÁLD, NEM MÁST:**

```css
:root {
  /* Háttér és felszínek */
  --bg: #F5F0EB;           /* App fő háttere (meleg bézs) */
  --card: #FFFFFF;          /* Kártyák, inputok */
  --border: #E8E2DB;        /* Általános border (meleg) */
  --border-input: #C5BCB3;  /* Input border */

  /* Alap szöveg */
  --text: #2C2825;          /* Fő szövegszín */
  --text2: #777777;         /* Másodlagos, muted */

  /* Elsődleges — burgundi vörös */
  --primary: #9B2335;       /* ← HELYES (nem #7B2D3B!) */
  --primary-light: #F9E0E3;

  /* Zöld — siker, savings */
  --green: #2D7A4F;
  --green-light: #D4EDDA;

  /* Arany — savings threshold, progress */
  --gold: #F0A500;
  --gold-light: #FFF8E1;

  /* Figyelmeztetés */
  --warning: #C4841D;
  --warning-light: #FEF3C7;

  /* Admin panel (kék) */
  --admin: #1A237E;
  --admin-bg: #E8EAF6;
  --admin-border: #9FA8DA;
}
```

> ⚠️ **Ismert drift:** Korábbi wireframe-ekben `--primary: #7B2D3B` szerepel — ez ROSSZ.
> A helyes érték a design-system.md alapján: `#9B2335`.

---

## 3. Phone frame sablon (kötelező struktúra)

```html
<div class="phone-label">Képernyő leírása</div>
<div class="phone">
  <div class="phone-header">
    <span>Oldal cím</span>
    <!-- jobb oldal: ikon vagy felirat -->
  </div>
  <div class="phone-body">
    <!-- tartalom ide -->
  </div>
  <div class="bottom-nav">
    <div class="nav-item [active]"><!-- ikon + felirat --></div>
    <div class="nav-item"><!-- ikon + felirat --></div>
    <div class="nav-item"><!-- ikon + felirat --></div>
    <div class="nav-item"><!-- ikon + felirat --></div>
  </div>
</div>
```

**Kötelező phone CSS:**
```css
.phone { width:375px; background:var(--bg); border-radius:24px; border:2px solid var(--border); overflow:hidden; box-shadow:0 8px 32px rgba(0,0,0,.12); flex-shrink:0; }
.phone-label { text-align:center; font-size:11px; font-weight:700; color:var(--text2); margin-bottom:8px; text-transform:uppercase; letter-spacing:.5px; }
.phone-header { background:var(--bg); padding:14px 20px; border-bottom:1px solid var(--border); display:flex; align-items:center; justify-content:space-between; }
.phone-header span:first-child { font-size:19px; font-weight:700; font-family:Georgia,serif; }
.phone-body { padding:0 16px 80px; max-height:620px; overflow-y:auto; }
.bottom-nav { position:sticky; bottom:0; background:white; border-top:1px solid var(--border); display:flex; padding:8px 0 4px; }
.nav-item { flex:1; display:flex; flex-direction:column; align-items:center; gap:3px; font-size:10px; color:var(--text2); cursor:pointer; padding:6px 0; }
.nav-item.active { color:var(--primary); font-weight:700; }
```

---

## 4. Ikonok — CSAK Lucide SVG, SOHA emoji

```html
<!-- Home --><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/></svg>

<!-- Kosár --><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="9" cy="21" r="1"/><circle cx="20" cy="21" r="1"/><path d="M1 1h4l2.68 13.39a2 2 0 0 0 2 1.61h9.72a2 2 0 0 0 2-1.61L23 6H6"/></svg>

<!-- Rendelések --><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 5H7a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V7a2 2 0 0 0-2-2h-2"/><rect x="9" y="3" width="6" height="4" rx="1" ry="1"/></svg>

<!-- Profil --><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/></svg>

<!-- RotateCcw (Reorder) --><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="1 4 1 10 7 10"/><path d="M3.51 15a9 9 0 1 0 .49-6.51"/></svg>

<!-- Truck --><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="1" y="3" width="15" height="13"/><polygon points="16 8 20 8 23 11 23 16 16 16 16 8"/><circle cx="5.5" cy="18.5" r="2.5"/><circle cx="18.5" cy="18.5" r="2.5"/></svg>

<!-- Coins (Savings) --><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="8" cy="8" r="6"/><path d="M18.09 10.37A6 6 0 1 1 10.34 18"/><path d="M7 6h1v4"/></svg>

<!-- Share --><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="18" cy="5" r="3"/><circle cx="6" cy="12" r="3"/><circle cx="18" cy="19" r="3"/><line x1="8.59" y1="13.51" x2="15.42" y2="17.49"/><line x1="15.41" y1="6.51" x2="8.59" y2="10.49"/></svg>

<!-- Star (Kedvencek) --><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>

<!-- CircleCheck --><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg>
```

---

## 5. Tab rendszer sablon

```css
.tabs { display:flex; gap:8px; max-width:1200px; margin:16px auto; padding:0 24px; overflow-x:auto; }
.tab { padding:9px 18px; border-radius:24px; font-size:12px; border:1px solid var(--border); background:white; cursor:pointer; white-space:nowrap; transition:all 0.2s; }
.tab.active { background:var(--primary); color:white; border-color:var(--primary); font-weight:700; }
.tab:hover:not(.active) { border-color:var(--primary); }
.content { max-width:1200px; margin:0 auto; padding:0 24px 40px; }
.feature { display:none; }
.feature.active { display:block; }
.feature > h2 { font-size:17px; font-weight:700; margin:0 0 6px; }
.feature > p.desc { font-size:13px; color:var(--text2); margin-bottom:16px; }
.phones { display:flex; gap:20px; flex-wrap:wrap; align-items:flex-start; }
```

```html
<script>
function showTab(n) {
  document.querySelectorAll('.feature').forEach((f,i) => f.classList.toggle('active', i===n));
  document.querySelectorAll('.tab').forEach((t,i) => t.classList.toggle('active', i===n));
}
</script>
```

---

## 6. Wireframe konvenciók

### Tab struktúra (ajánlott sorrend)
1. Fő állapot(ok) — a feature normál megjelenése
2. Edge case(ok) — empty state, error, loading
3. Interakció — modal, bottom sheet, konfirmáció
4. **Acceptance Criteria** — kötelező utolsó tab minden wireframe-ben

### Acceptance Criteria tab
```html
<table class="ac-table">
  <tr><th>#</th><th>Feltétel</th><th>Prioritás</th><th>Állapot</th></tr>
  <tr>
    <td>AC-1</td>
    <td>Feltétel szövege</td>
    <td><span class="tag tag-p0">P0</span></td>
    <td><span style="color:#999;">○ TODO</span></td>
  </tr>
</table>
```

### Header badge
```html
<span style="display:inline-block; padding:3px 10px; border-radius:12px; font-size:11px; font-weight:700; background:#E8EAF6; color:#1A237E; margin-top:8px;">
  DH-XXX · Sprint N
</span>
```

### Back button (KÖTELEZŐ, kivéve index.html)
```html
<a href="index.html" style="display:block; text-align:center; color:#777; font-size:12px; padding:16px 0; text-decoration:none;">← Vissza a galériába</a>
```

---

## 7. Fájl írás — kötelező minta

**MINDEN végleges wireframe-t a FUSE mountra kell írni:**

```python
import os

mnt = '/sessions/adoring-gifted-gates/mnt'
for item in os.scandir(mnt):
    if item.is_dir() and 'De' in item.name:
        base = item.path
        break

out = f'{base}/design/wireframes/v0.X-feature-name.html'
with open(out, 'w') as f:
    f.write(html_content)
print(f'OK: {out} ({os.path.getsize(out)} bytes)')
```

**SOHA ne használd a `Write` toolt végleges wireframe-ekhez** — az árnyékmappába ír!

---

## 8. Deploy checklist + Netlify

**Deploy előtt:**
- [ ] `<a href="index.html">` minden HTML-ben (kivéve index.html)
- [ ] Nincs látható `<!--` comment a renderelt tartalomban
- [ ] Nincs emoji UI elemekben (csak Lucide SVG)
- [ ] Build szám nőtt az index.html-ben
- [ ] index.html frissítve (összes wireframe kártyája szerepel)
- [ ] Csak létező fájlokhoz van kártya

**Netlify deploy:**
```bash
cd /tmp/deploy && zip -r /tmp/deploy.zip .
curl -s -H "Content-Type: application/zip" \
  -H "Authorization: Bearer nfp_iEqWi7A9thMrn5vsFq3dtY2tNDbqpevB750e" \
  --data-binary "@/tmp/deploy.zip" \
  "https://api.netlify.com/api/v1/sites/f5c7e6ed-1ea2-4c72-b8e8-8c342ed3549e/deploys"
```
Site: `deakhus.netlify.app` | Site ID: `f5c7e6ed-1ea2-4c72-b8e8-8c342ed3549e`

---

## 9. Státusz badge-ek

| Magyar | Háttér | Szöveg |
|--------|--------|--------|
| Új rendelés | `#DBEAFE` | `#2B6CB0` |
| Előkészítés alatt | `#FEF3C7` | `#C4841D` |
| Kiszállításra kész | `#F5EDDF` | `#96724A` |
| Úton van | `#F9E0E3` | `#9B2335` |
| Kézbesítve | `#D4EDDA` | `#2D7A4F` |
| Lezárva | `#EDEAE6` | `#999999` |

---

## 10. Gyors komponens snippetek

### Kártya
```html
<div style="background:white; border-radius:16px; border:1px solid var(--border); padding:14px 16px; margin-bottom:10px;"></div>
```

### Gombok
```html
<!-- Primary -->
<button style="width:100%; padding:13px 16px; border-radius:12px; background:#9B2335; color:white; font-size:14px; font-weight:700; border:none; cursor:pointer; margin-bottom:8px;">Szöveg</button>
<!-- Secondary -->
<button style="width:100%; padding:13px 16px; border-radius:12px; background:transparent; border:2px solid #9B2335; color:#9B2335; font-size:14px; font-weight:700; cursor:pointer;">Szöveg</button>
```

### Savings progress bar
```html
<div style="background:var(--gold-light); border:1px solid var(--gold); border-radius:12px; padding:10px 12px; margin:8px 0 12px;">
  <div style="display:flex; justify-content:space-between; font-size:12px; color:#92400E; margin-bottom:4px;"><span>187 RON</span><span>300 RON küszöb</span></div>
  <div style="height:8px; background:#EEE; border-radius:8px; overflow:hidden;"><div style="height:100%; width:62%; border-radius:8px; background:var(--gold);"></div></div>
  <div style="font-size:12px; color:#92400E; margin-top:6px;">Még <strong>113 RON</strong> a következő küszöbig</div>
</div>
```

### Info box
```html
<div style="background:#EEF2FF; border:1px solid #C7D2FE; border-radius:12px; padding:12px 14px; font-size:13px; color:#3730A3; margin:12px 0;">
  <strong style="display:block; margin-bottom:4px;">Cím</strong>Szöveg
</div>
```
