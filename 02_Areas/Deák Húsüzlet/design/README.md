---
title: "DH Design — Screen Catalog"
date: 2026-05-05
author: Becze Szabolcs
status: active
description: "Comprehensive reference guide for managing the DH Design screen catalog, including folder structure, how the generated index.html works with embedded manifest data, status color coding, sprint grouping logic, and step-by-step instructions for adding new screens and deploying updates to Netlify."
description_source: auto
description_hash: 89e8136f9cc6d39b
id: 068d1b27-aab4-4fe6-956e-7a146ee26c5e
index_schema_version: 1
bdos_index: true
---
# DH Design — Screen Catalog

> **Utolsó frissítés:** 2026-04-25 · **Aktuális build:** #35  
> **Live URL:** https://deakhus.netlify.app

Ez a dokumentum egyetlen forrás egy új session számára. Elolvasása után tudsz:
1. Frissíteni az `index.html`-t (struktúra + design megértése)
2. Új HTML képernyőt beintegrálni a katalógusba
3. Deployolni Netlify-ra

---

## Mappastruktúra

```
design/
  README.md                      ← ez a dokumentum
  design-system.md               ← DH design tokens, komponens spec
  screen-catalog/
    index.html                   ← GENERÁLT — ne szerkeszd kézzel!
    manifest.json                ← GENERÁLT — ne szerkeszd kézzel!
    workflow.md                  ← részletes technikai leírás (belső referencia)
    screens/                     ← itt élnek a screen HTML fájlok
      v0.3-reorder-v2.html
      v0.3-post-order-recap.html
      v0.3-savings-counter.html
      v0.3-founding50.html
      v0.3-consent-gdpr.html
      aszf-wireframe-v2.html
      privacy-policy-wireframe-v2.html
      v0.4-profile-admin.html
      v0.5-shared-basket-v2.html
  wireframes/
    archive/b33-final/           ← korábbi build archívum (referencia)
    *.zip                        ← régi build zip-ek
```

---

## Aktuális katalógus állapota (Build #35)

| Sprint | File | Státusz | Jira |
|--------|------|---------|------|
| Sprint 3 | v0.3-reorder-v2.html | done | DH-120, DH-121 |
| Sprint 3 | v0.3-post-order-recap.html | done | DH-119 |
| Sprint 3 | v0.3-savings-counter.html | done | DH-117, DH-118 |
| Sprint 3 | v0.3-founding50.html | done | DH-153, DH-154 |
| Legal | v0.3-consent-gdpr.html | approved | DH-132 |
| Legal | aszf-wireframe-v2.html | approved | DH-130 |
| Legal | privacy-policy-wireframe-v2.html | approved | DH-134 |
| Legal | v0.4-profile-admin.html | approved | DH-147 |
| Sprint 5 | v0.5-shared-basket-v2.html | review | DH-149 |

---

## 1. Az index.html struktúrája

### Hogyan működik

Az `index.html` **nem olvassa a manifest.json-t fetch-chel** — a manifest közvetlenül **beágyazva** van JS változóként:

```javascript
const MANIFEST = {
  "meta": { "build": 35, "generatedAt": "..." },
  "screens": [ ... ]
};
```

Ez azért szükséges, mert `file://` protokollon a `fetch()` CORS-t dob. A változó neve mindig `MANIFEST`, a `init()` függvény ebből épít mindent.

### Renderelési logika (`init()` függvény)

1. **Sprint csoportok** — a `sprint` mező alapján csoportosít, numerikusan rendez (`parseInt` a számra). A "Legal" csoport neve nem tartalmaz számot, ezért mindig **utolsó** (fallback: 999).
2. **Sorrend spriten belül** — `order` mező alapján növekvő, kivéve: `done` státuszú elemek mindig a **lista aljára** kerülnek.
3. **Státusz szűrő** — fejléc felett: All / Approved / Review / Done / Draft gombok.
4. **Collapsible csoportok** — `.group` / `.group-head` / `.group-body` CSS osztályok, `toggleGroup()` és `toggleAll()` JS függvényekkel. `localStorage`-ban perzisztál.

### Design tokenek (`:root` CSS változók)

```css
--primary: #9B2335        /* DH piros */
--primary-light: #F9E0E3
--primary-pale: #F4E6E8
--info: #1E40AF           /* kék — approved/ready státusz */
--info-light: #DBEAFE
--done-text: #065F46      /* zöld — done státusz */
--done-bg: #D1FAE5
--amber: #92400E          /* narancs — review státusz */
--amber-light: #FEF3C7
--bg: #FAF7F4             /* oldal háttér */
--card: #FFFFFF
--text: #2C2825
--text-muted: #8A8078
--border: #E8E2DB
```

### Státusz színek

| Státusz | Szín | CSS osztály |
|---------|------|-------------|
| `approved` | 🔵 kék | `.status-approved`, `.icon-approved` |
| `done` | 🟢 zöld | `.status-done`, `.icon-done` |
| `review` | 🟡 amber | `.status-review`, `.icon-review` |
| `draft` | ⚪ szürke | `.status-draft`, `.icon-draft` |

`done` kártyák `opacity: 0.72` (hover-re 1.0).

### Build szám frissítése

A build szám két helyen él — mindkettőt frissíteni kell egyszerre:
1. `manifest.json` → `meta.build`
2. `index.html` → `const MANIFEST = { "meta": { "build": N, ...`

A Python script (ld. 3. fejezet) egyszerre csinálja mindkettőt.

---

## 2. Új screen HTML beintegrálása

### A. Screen HTML előkészítése

Minden screen fájlnak tartalmaznia kell a `<head>`-ben:

```html
<head>
<script type="application/json" id="screen-meta">
{
  "title": "Checkout — Szállítás",
  "feature": "checkout",
  "sprint": "Sprint 4",
  "status": "draft",
  "publish": true,
  "order": 10,
  "platform": "mobile",
  "version": "v1",
  "tags": ["DH-XXX", "checkout", "delivery"]
}
</script>

<style>
.back-to-catalog {
  position: fixed; top: 12px; left: 12px; z-index: 9999;
  display: inline-flex; align-items: center; gap: 6px;
  background: rgba(155,35,53,0.92); color: white;
  font-family: -apple-system, sans-serif;
  font-size: 12px; font-weight: 600;
  padding: 7px 12px 7px 10px;
  border-radius: 999px; text-decoration: none;
}
</style>
</head>
<body>
<a class="back-to-catalog" href="../index.html">
  <svg viewBox="0 0 24 24" width="14" height="14" stroke="white" stroke-width="2.5" fill="none"><polyline points="15 18 9 12 15 6"/></svg>
  Katalógus
</a>
<!-- screen tartalma -->
```

**Fontos:** `href="../index.html"` — a `screens/` alkönyvtárból egy szinttel fel kell menni.

### B. Fájl elhelyezése

```
design/screen-catalog/screens/[feature]-[leírás].html
```

### C. manifest.json frissítése

```python
import os, glob, json
from datetime import datetime

bases = glob.glob('/sessions/adoring-gifted-gates/mnt/*/')
real = next(b for b in bases if os.path.exists(os.path.join(b, 'CLAUDE.md')))
manifest_path = os.path.join(real, 'design', 'screen-catalog', 'manifest.json')

with open(manifest_path, 'r', encoding='utf-8') as fh:
    manifest = json.load(fh)

# Új screen hozzáadása
manifest['screens'].append({
    "file": "screens/checkout-delivery.html",
    "title": "Checkout — Szállítás",
    "feature": "checkout",
    "sprint": "Sprint 4",
    "status": "draft",
    "publish": True,
    "order": 10,
    "platform": "mobile",
    "version": "v1",
    "tags": ["DH-XXX", "checkout", "delivery"]
})

BUILD = manifest['meta']['build'] + 1
manifest['meta']['build'] = BUILD
manifest['meta']['generatedAt'] = datetime.utcnow().isoformat()

with open(manifest_path, 'w', encoding='utf-8') as fh:
    json.dump(manifest, fh, ensure_ascii=False, indent=2)
```

### D. manifest.json visszaágyazása index.html-be

```python
idx_path = os.path.join(real, 'design', 'screen-catalog', 'index.html')
with open(idx_path, 'r', encoding='utf-8') as fh:
    html = fh.read()

manifest_json = json.dumps(manifest, ensure_ascii=False, indent=2)
new_block = 'const MANIFEST = ' + manifest_json + ';'

# Régi MANIFEST blokk cseréje
start = html.find('const MANIFEST = {')
depth = 0
i = start + len('const MANIFEST = ')
while i < len(html):
    if html[i] == '{': depth += 1
    elif html[i] == '}':
        depth -= 1
        if depth == 0:
            end = i + 1
            if html[end:end+1] == ';': end += 1
            break
    i += 1
html = html[:start] + new_block + html[end:]

with open(idx_path, 'w', encoding='utf-8') as fh:
    fh.write(html)
```

### E. Sprint csoport sorrend

A sprint csoportok a `sprint` mező `parseInt` értéke alapján rendeznek:
- `"Sprint 3"` → 3
- `"Sprint 5"` → 5
- `"Legal"` → NaN → 999 (mindig utolsó)

Ha új sprint csoportot hozol létre, a neve legyen `"Sprint N"` (N = szám), vagy egy leíró szó, ha az utolsó helyen kell legyen (pl. `"Legal"`, `"Archive"`).

---

## 3. Deploy Netlify-ra

> **Szabály: csak akkor deployolj, ha Szabolcs explicitleg kéri.**

### Konfiguráció

| Paraméter | Érték |
|-----------|-------|
| Site | https://deakhus.netlify.app |
| Site ID | `f5c7e6ed-1ea2-4c72-b8e8-8c342ed3549e` |
| API token | `nfp_iEqWi7A9thMrn5vsFq3dtY2tNDbqpevB750e` |
| Deploy mód | Zip → curl API (SOHA ne Chrome file_upload!) |
| URL struktúra | `index.html` → `/` · `screens/foo.html` → `/screens/foo` |

### Deploy lépések (Python + bash)

```python
import os, glob, shutil, zipfile

bases = glob.glob('/sessions/adoring-gifted-gates/mnt/*/')
real = next(b for b in bases if os.path.exists(os.path.join(b, 'CLAUDE.md')))
sc = os.path.join(real, 'design', 'screen-catalog')

# 1. Deploy könyvtár összeállítása
deploy_dir = '/tmp/sc-deploy'
if os.path.exists(deploy_dir): shutil.rmtree(deploy_dir)
os.makedirs(os.path.join(deploy_dir, 'screens'))

for f in ['index.html', 'manifest.json', 'workflow.md']:
    shutil.copy2(os.path.join(sc, f), os.path.join(deploy_dir, f))

for fname in os.listdir(os.path.join(sc, 'screens')):
    if fname.endswith('.html'):
        shutil.copy2(os.path.join(sc, 'screens', fname),
                     os.path.join(deploy_dir, 'screens', fname))

# 2. Zip
zip_path = '/tmp/sc-deploy.zip'
with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zf:
    for root, dirs, files in os.walk(deploy_dir):
        for f in files:
            full = os.path.join(root, f)
            zf.write(full, os.path.relpath(full, deploy_dir))
```

```bash
# 3. Curl API deploy
DEPLOY_ID=$(curl -s \
  -H "Content-Type: application/zip" \
  -H "Authorization: Bearer nfp_iEqWi7A9thMrn5vsFq3dtY2tNDbqpevB750e" \
  --data-binary "@/tmp/sc-deploy.zip" \
  "https://api.netlify.com/api/v1/sites/f5c7e6ed-1ea2-4c72-b8e8-8c342ed3549e/deploys" \
  | python3 -c "import sys,json; print(json.load(sys.stdin)['id'])")

# 4. Státusz poll (várj ready-re)
for i in $(seq 1 15); do
  sleep 3
  STATE=$(curl -s \
    -H "Authorization: Bearer nfp_iEqWi7A9thMrn5vsFq3dtY2tNDbqpevB750e" \
    "https://api.netlify.com/api/v1/deploys/$DEPLOY_ID" \
    | python3 -c "import sys,json; print(json.load(sys.stdin).get('state','?'))")
  echo "[$i] $STATE"
  [ "$STATE" = "ready" ] && break
done
```

### Deploy QA (futtatás előtt)

Ellenőrizd, hogy:
- `index.html`-ben a `const MANIFEST` tartalmazza az összes screen-t
- Minden screen fájlban van `back-to-catalog` gomb `href="../index.html"` hivatkozással
- Nincs `href="index.html"` (hiányzó `../`) a screens/ könyvtárban

---

## 4. FUSE mount figyelmeztetés

A sandbox-ban **két** `Deák Húsüzlet` nevű mappa látszik:
- `mode 0o40700` → **valódi FUSE mount** (Google Drive) — Szabolcs ezt látja ✅
- `mode 0o40755` → VM árnyékmappa — Szabolcs NEM látja ❌

**Soha ne írj `Write` tool-lal a végső fájlokba** — az az árnyékmappába megy.  
**Mindig Python `open()` write-tal** dolgozz a FUSE mounton:

```python
# Helyes minta: real mount megkeresése
import os, glob
bases = glob.glob('/sessions/adoring-gifted-gates/mnt/*/')
real = next(b for b in bases if os.path.exists(os.path.join(b, 'CLAUDE.md')))
# real = '/sessions/adoring-gifted-gates/mnt/Deák Húsüzlet/'
```

---

## 5. Screen státuszok életciklusa

```
draft → review → approved → done
```

| Státusz | Jelentés | Szín | Pozíció |
|---------|----------|------|---------|
| `draft` | Folyamatban | ⚪ szürke | sorrend szerint |
| `review` | Design review alatt | 🟡 amber | sorrend szerint |
| `approved` | Fejlesztőknek átadható | 🔵 kék | sorrend szerint |
| `done` | Implementálva | 🟢 zöld | lista alja (minden csoportban) |

---

## 6. Variáns-hivatkozás konvenció (`.dh-copy` pattern)

Egy screen fájl gyakran több variánst / állapotot mutat egymás alatt (showcase). Ahhoz, hogy egy konkrét variánsra **egyértelműen tudjunk hivatkozni** design review-ban, Jira commentben, Slack-en, minden variáns-blokkhoz tartozik egy másoló gomb, ami vágólapra teszi a teljes hivatkozási stringet.

### Formátum

```
[DH] {Feature} › {Screen} › {Variáns betű} — {Variáns cím} ({fájlnév})
```

**Példa:**
```
[DH] Falusi route › Kör-választó › A — GPS-javaslat (engedélyezve) (v0.4-zone-picker.html)
```

Olvasandó:
- `[DH]` — projekt tag (Deák Húsüzlet)
- `Falusi route` — feature (Jira Epic szintű, pl. DH-184)
- `Kör-választó` — screen név (a fájlon belüli funkció)
- `A` — variáns betűjel (A, B, C, D… egy fájlon belül)
- `GPS-javaslat (engedélyezve)` — variáns rövid címe + zárójelben az állapot
- `(v0.4-zone-picker.html)` — forrásfájl a `screens/` alatt

### HTML minta

Minden variáns fejlécében egy `.dh-copy` gomb, `data-ref` attribútumban a teljes string:

```html
<div class="variant-header">
  <span class="ttl">GPS-javaslat <span class="muted">engedélyezve</span></span>
  <button class="dh-copy"
          data-ref="[DH] Falusi route › Kör-választó › A — GPS-javaslat (engedélyezve) (v0.4-zone-picker.html)"
          aria-label="Hivatkozás másolása"
          title="Másolás: A — GPS-javaslat"></button>
</div>
```

### JS minta (oldal végén egyszer)

```javascript
(function(){
  var COPY  = '<svg ...>copy ikon</svg>';
  var CHECK = '<svg ...>check ikon</svg>';
  function copyText(text, btn){
    function ok(){ btn.classList.add('copied'); btn.innerHTML=CHECK;
      setTimeout(function(){btn.classList.remove('copied'); btn.innerHTML=COPY;},1200);
      showToast('Másolva: '+text.slice(0,40)+(text.length>40?'…':''));
    }
    if(navigator.clipboard && window.isSecureContext){
      navigator.clipboard.writeText(text).then(ok).catch(function(){fb(text,ok,function(){showToast('Másolás sikertelen');});});
    } else { fb(text,ok,function(){showToast('Másolás sikertelen');}); }
  }
  document.addEventListener('click', function(e){
    var b=e.target.closest('.dh-copy'); if(!b) return;
    e.preventDefault(); e.stopPropagation();
    var ref=b.dataset.ref; if(ref) copyText(ref,b);
  });
  document.querySelectorAll('.dh-copy').forEach(function(b){
    if(!b.innerHTML.trim()) b.innerHTML=COPY;
  });
})();
```

### Mikor használd

- **Mindig**, amikor egy fájlon belül 2+ variáns/állapot van (pl. üres állapot, GPS engedélyezve/letiltva, perzisztens állapot, error state).
- A betűjelezés (A, B, C…) az olvasási sorrendet követi a fájlon belül.
- Ha egy screen állapotai változnak, a `data-ref` stringet **manuálisan szinkronban** kell tartani a látható címmel.

### Jelenleg használja (v0.4 falusi route screen-család)

`v0.4-zone-picker.html`, `v0.4-cart-rural.html`, `v0.4-checkout-rural.html`, `v0.4-order-confirm-rural.html`, `v0.4-route-banner.html`, `v0.4-courier-route.html`, és a katalógus `index.html`.

---

*Részletes technikai dokumentáció: `screen-catalog/workflow.md`*
