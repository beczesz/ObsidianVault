#!/usr/bin/env python3
"""
DH Screen Catalog — Pre-deploy check script
Futtatás: python3 pre-deploy-check.py (inline Python-ként Cowork session-ből)
Ha bármelyik check ❌ → NE deployolj!

Tab struktúra szabályok:
  KÉPERNYŐK tab (screens[]) → UX wireframe, app screen, jogi wireframe (sprint=Legal)
  DOKUMENTÁCIÓ tab (docs[]) → referencia doc, szótár, business model, analytics spec
  ⚠️  MINDEN fájlnak screens/ mappában kell lennie — docs tab fájljai is!
"""
import os, json, re, sys

def find_real_mount():
    mnt = '/sessions/adoring-gifted-gates/mnt'
    if os.path.exists(mnt):
        try:
            for e in os.scandir(mnt):
                if 'Dea' in e.name and e.stat().st_mode & 0o777 == 0o700:
                    return e.path
        except Exception:
            pass
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

WORKSPACE     = find_real_mount()
CATALOG_DIR   = os.path.join(WORKSPACE, "design/screen-catalog")
SCREENS_DIR   = os.path.join(CATALOG_DIR, "screens")
INDEX_PATH    = os.path.join(CATALOG_DIR, "index.html")
MANIFEST_PATH = os.path.join(CATALOG_DIR, "manifest.json")

errors = []; warnings = []

def check(label, ok, msg=""):
    print(f"  {'✅' if ok else '❌'} {label}" + (f" — {msg}" if msg else ""))
    if not ok: errors.append(f"{label}: {msg}")

def warn(label, msg=""):
    print(f"  ⚠️  {label}" + (f" — {msg}" if msg else ""))
    warnings.append(f"{label}: {msg}")

print("=" * 58)
print("DH Screen Catalog — Pre-deploy check")
print(f"Catalog: {CATALOG_DIR}")
print("=" * 58)

# ── 1. Build számok ─────────────────────────────────────────
with open(INDEX_PATH, 'r') as f: idx = f.read()
m = re.search(r'"build":\s*(\d+)', idx)
idx_build = int(m.group(1)) if m else None
check("index.html build readable", idx_build is not None, str(idx_build))

with open(MANIFEST_PATH, 'r') as f: mf = json.load(f)
mf_build = mf.get('meta', {}).get('build')
check("manifest.json build readable", mf_build is not None, str(mf_build))

if idx_build and mf_build:
    check("Build numbers match", idx_build == mf_build,
          f"index={idx_build} vs manifest={mf_build}")

# ── 2. Disk fájlok ──────────────────────────────────────────
disk_files = set(f for f in os.listdir(SCREENS_DIR)
                 if f.endswith('.html') and not f.startswith('.'))

# ── 3. Screens tömb ─────────────────────────────────────────
mf_screens = set(s['file'].replace('screens/','') for s in mf.get('screens',[]))
ghosts   = mf_screens - disk_files
orphans  = disk_files - mf_screens

# Docs fájljai is screens/-ben kell legyenek
doc_files_in_manifest = set()
for cat in mf.get('docs', []):
    for item in cat.get('items', []):
        f = item.get('file','').replace('screens/','')
        if not f.startswith('..'):  # relative path a screens/-en belül
            doc_files_in_manifest.add(f)

all_manifest_files = mf_screens | doc_files_in_manifest
ghosts_all = all_manifest_files - disk_files
orphans_screens = disk_files - all_manifest_files  # sem screens, sem docs

check("No ghost entries", not ghosts_all,
      f"{sorted(ghosts_all)}" if ghosts_all else "")
if orphans_screens:
    warn("Orphan files (on disk, not in any manifest)", str(sorted(orphans_screens)))
else:
    print("  ✅ No orphan files")

# ── 4. screen-meta + back-to-catalog ────────────────────────
print("\n  Checking screen-meta and back-to-catalog...")
missing_meta, missing_back = [], []
for fname in sorted(disk_files):
    with open(os.path.join(SCREENS_DIR, fname),'r') as f: c = f.read()
    if 'screen-meta' not in c: missing_meta.append(fname)
    if 'back-to-catalog' not in c: missing_back.append(fname)
check("All screens have screen-meta", not missing_meta,
      str(missing_meta) if missing_meta else "")
check("All screens have back-to-catalog", not missing_back,
      str(missing_back) if missing_back else "")

# ── 5. Tab placement ellenőrzés ─────────────────────────────
print("\n  Checking tab placement...")

# DOC-gyanús screensben: analytics/dictionary/spec/model/loop/economic
DOC_KEYWORDS = ['dictionary', 'analytics-dict', 'economic', 'loop', 'business-model',
                'kpi-framework', 'spec', 'design-system']
LEGAL_WIREFRAME_KEYWORDS = ['aszf', 'privacy', 'gdpr', 'consent', 'cookie']

misplaced_in_screens = []  # docs-ba kellene
misplaced_in_docs    = []  # screens-be kellene

for s in mf.get('screens', []):
    fname = s['file'].replace('screens/','').lower()
    # Ha a feature analytics/dictionary/business-model → docs-ba kellene
    feat = s.get('feature','').lower()
    if any(kw in fname for kw in DOC_KEYWORDS) or feat in ['analytics-dictionary','business-model']:
        misplaced_in_screens.append(s['file'])

for cat in mf.get('docs', []):
    for item in cat.get('items', []):
        fname = item.get('file','').replace('screens/','').lower()
        # Ha v0.X- prefix van és nem doc-keyword → screens-be kellene
        if re.match(r'v\d+\.\d+-', fname):
            if not any(kw in fname for kw in DOC_KEYWORDS):
                misplaced_in_docs.append(item['file'])

if misplaced_in_screens:
    warn("Possible doc-type files in screens[]", str(misplaced_in_screens))
else:
    print("  ✅ No suspicious doc-type files in screens tab")

if misplaced_in_docs:
    warn("Possible screen-type files in docs[]", str(misplaced_in_docs))
else:
    print("  ✅ No suspicious screen-type files in docs tab")

# ── 6. Stray HTML a wrong helyen ────────────────────────────
dev_dir = os.path.join(WORKSPACE, "development")
stray = []
if os.path.exists(dev_dir):
    for root, dirs, files in os.walk(dev_dir):
        dirs[:] = [d for d in dirs if d not in ['archive']]
        for f in files:
            if f.endswith('.html') and os.path.getsize(os.path.join(root,f)) > 5000:
                stray.append(os.path.relpath(os.path.join(root,f), WORKSPACE))
if stray:
    warn("HTML files outside screens/ (deploy-ban NEM szerepelnek!)", str(stray))
else:
    print("  ✅ No stray HTML files outside screens/")

# ── 7. Docs fájlok path validáció ───────────────────────────
print("\n  Checking docs file paths...")
bad_doc_paths = []
for cat in mf.get('docs', []):
    for item in cat.get('items', []):
        fp = item.get('file','')
        if fp.startswith('..') or (not fp.startswith('screens/') and not fp.startswith('../')):
            bad_doc_paths.append(fp)
        elif fp.startswith('screens/'):
            actual = os.path.join(SCREENS_DIR, fp.replace('screens/',''))
            if not os.path.exists(actual):
                bad_doc_paths.append(f"{fp} (NOT ON DISK)")
if bad_doc_paths:
    check("Docs file paths valid", False, str(bad_doc_paths))
else:
    print("  ✅ All docs file paths valid and on disk")

# ── Összefoglalás ────────────────────────────────────────────
n_screens = len(mf.get('screens',[]))
n_docs    = sum(len(c.get('items',[])) for c in mf.get('docs',[]))
print("\n" + "=" * 58)
print(f"Screens: {len(disk_files)} disk | {n_screens} in screens[] | {n_docs} in docs[]")
print(f"Build:   #{idx_build}")

if warnings:
    print(f"\n⚠️  Warnings ({len(warnings)}):")
    for w in warnings: print(f"   - {w}")

if errors:
    print(f"\n❌ DEPLOY BLOCKED — {len(errors)} error(s):")
    for e in errors: print(f"   - {e}")
    sys.exit(1)
else:
    print(f"\n✅ ALL CHECKS PASSED — safe to deploy build #{idx_build}")
    sys.exit(0)
