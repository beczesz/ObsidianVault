#!/usr/bin/env python3
"""
Deák Húsmíves Products — MD to JSON builder.

Reads:  MASTER/products/*.md     (one file per product, Option C format)
        MASTER/_categories.yaml
        MASTER/_settings.yaml
        MASTER/_options.yaml     (NEW v1.2: VG/option-type master, DH-173)
        MASTER/_schema-v{schema_version}.json
Writes: generated/products-v{version}.json

Usage:
    python3 build.py [--version 1.2] [--schema-version 1.2]

MD-ONLY fields (kept in MD, NOT in JSON):
    - YAML keys:   seasonal, sources, last_updated, option_ids, option_value_overrides
                   (option_ids + overrides are CONSUMED by the builder, not output as-is)
    - MD sections: Felhasználás, Opciók, Termelői megjegyzések, History

DH-173 v1.2:
    - YAML frontmatter `option_ids: [pacolas, szeletes]` → builder pulls
      the matching option from _options.yaml
    - YAML frontmatter `option_value_overrides: { meret: { kisebb: { weight_range_min: 1.2 } } }`
      → per-product override merged on top of the master
    - The output `options[]` array is fully self-contained per product
      (frontend doesn't need _options.yaml).

Schema v1.2 enforces additionalProperties: false on every object.
"""
import os, sys, re, json, datetime, argparse, copy
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.exit("ERROR: pyyaml required. Install: pip install pyyaml")

try:
    import jsonschema
except ImportError:
    sys.exit("ERROR: jsonschema required. Install: pip install jsonschema")


class _DateAsStringLoader(yaml.SafeLoader):
    pass

def _date_constructor(loader, node):
    return loader.construct_scalar(node)

_DateAsStringLoader.add_constructor("tag:yaml.org,2002:timestamp", _date_constructor)


def yaml_load(text):
    return yaml.load(text, Loader=_DateAsStringLoader)


# ─── PATHS ───────────────────────────────────────────────────────
SCRIPT_DIR = Path(__file__).resolve().parent
MASTER_DIR = SCRIPT_DIR.parent
PRODUCTS_DIR = MASTER_DIR / "products"
CATEGORIES_FILE = MASTER_DIR / "_categories.yaml"
SETTINGS_FILE = MASTER_DIR / "_settings.yaml"
OPTIONS_FILE = MASTER_DIR / "_options.yaml"
PRODUCTS_ROOT = MASTER_DIR.parent
GENERATED_DIR = PRODUCTS_ROOT / "generated"


# ─── CONSTANTS ───────────────────────────────────────────────────
# YAML keys consumed by the builder (NOT passed through to JSON as-is)
MD_ONLY_YAML_KEYS = {
    "seasonal", "sources", "last_updated",
    "option_ids", "option_value_overrides",  # v1.2: consumed by builder
}

MD_ONLY_SECTIONS = {"Felhasználás", "Opciók", "Termelői megjegyzések", "History"}

SCHEMA_REQUIRED_FIELDS = {
    "id", "product_name_ro", "product_name_hu", "image", "price",
    "unit", "product_type", "category", "is_available"
}

SCHEMA_ALLOWED_FIELDS = SCHEMA_REQUIRED_FIELDS | {
    "description_ro", "description_hu", "note_ro", "note_hu",
    "estimated_weight_per_piece", "weight_range_min", "weight_range_max",
    "popularity_score", "quantity_override",
    "internal_code",
    "options",  # v1.2 NEW
}


# ─── PARSERS ─────────────────────────────────────────────────────
RE_YAML_BLOCK = re.compile(r"```yaml\n(.*?)```", re.DOTALL)
RE_BULLET_BILINGUAL = re.compile(r"^\s*-\s*\*\*(HU|RO):\*\*\s*(.+?)\s*$", re.MULTILINE)


def extract_yaml_block(md: str) -> dict:
    m = RE_YAML_BLOCK.search(md)
    if not m:
        raise ValueError("No yaml block found")
    data = yaml_load(m.group(1))
    if not isinstance(data, dict):
        raise ValueError("YAML block must be a mapping")
    return data


def split_h2_sections(md: str) -> dict:
    parts = re.split(r"^## (.+?)\s*$", md, flags=re.MULTILINE)
    sections = {}
    for i in range(1, len(parts), 2):
        heading = parts[i].strip()
        body = parts[i + 1] if i + 1 < len(parts) else ""
        sections[heading] = body.strip()
    return sections


def parse_bilingual_bullets(text: str):
    result = {}
    for m in RE_BULLET_BILINGUAL.finditer(text):
        lang = m.group(1).lower()
        result[lang] = m.group(2).strip()
    return result


# ─── OPTIONS MERGE ───────────────────────────────────────────────
def load_options_master():
    """Load _options.yaml and return as dict {option_id: option_def}."""
    if not OPTIONS_FILE.exists():
        return {}
    with OPTIONS_FILE.open(encoding="utf-8") as f:
        data = yaml_load(f.read())
    if not data or "options" not in data:
        return {}
    return {opt["option_id"]: opt for opt in data["options"]}


def deep_merge_value(master_value: dict, override: dict) -> dict:
    """Merge per-product override into a master value. Override only changes
    explicitly listed keys; everything else stays from master."""
    merged = copy.deepcopy(master_value)
    for k, v in override.items():
        merged[k] = v
    return merged


def build_product_options(option_ids, value_overrides, options_master, product_id):
    """Construct the options[] array for one product:
    - Pull each option_id from master.
    - Apply per-product value_overrides (if any).
    - Return list of fully-resolved option dicts.
    """
    if not option_ids:
        return []
    result = []
    for oid in option_ids:
        if oid not in options_master:
            raise ValueError(
                f"Product '{product_id}': option_id '{oid}' not found in _options.yaml"
            )
        opt = copy.deepcopy(options_master[oid])
        # Apply per-product value-level overrides
        if value_overrides and oid in value_overrides:
            opt_override = value_overrides[oid]
            if not isinstance(opt_override, dict):
                raise ValueError(
                    f"Product '{product_id}': option_value_overrides['{oid}'] must be a dict"
                )
            new_values = []
            for v in opt["values"]:
                vid = v["value_id"]
                if vid in opt_override:
                    v = deep_merge_value(v, opt_override[vid])
                new_values.append(v)
            opt["values"] = new_values
        result.append(opt)
    return result


# ─── PRODUCT PARSER ──────────────────────────────────────────────
def parse_product_md(path: Path, options_master: dict) -> dict:
    md = path.read_text(encoding="utf-8")
    yml = extract_yaml_block(md)
    sections = split_h2_sections(md)

    # Pull v1.2 option binding fields BEFORE filtering MD_ONLY keys
    option_ids = yml.get("option_ids", [])
    value_overrides = yml.get("option_value_overrides", {})

    # Start from frontmatter, drop MD-only YAML keys
    product = {k: v for k, v in yml.items() if k not in MD_ONLY_YAML_KEYS}

    if "Név" in sections:
        names = parse_bilingual_bullets(sections["Név"])
        if "hu" in names:
            product["product_name_hu"] = names["hu"]
        if "ro" in names:
            product["product_name_ro"] = names["ro"]

    if "Leírás" in sections:
        descs = parse_bilingual_bullets(sections["Leírás"])
        product["description_hu"] = descs.get("hu")
        product["description_ro"] = descs.get("ro")

    if "Megjegyzés" in sections:
        notes = parse_bilingual_bullets(sections["Megjegyzés"])
        product["note_hu"] = notes.get("hu")
        product["note_ro"] = notes.get("ro")

    pt = product.get("product_type")
    if pt in ("weight", "piece"):
        product["estimated_weight_per_piece"] = None
        product["weight_range_min"] = None
        product["weight_range_max"] = None

    product.setdefault("popularity_score", 0)
    product.setdefault("quantity_override", None)
    product.setdefault("note_hu", None)
    product.setdefault("note_ro", None)
    product.setdefault("description_hu", None)
    product.setdefault("description_ro", None)
    product.setdefault("internal_code", None)

    # v1.2: build options[] from binding
    product["options"] = build_product_options(
        option_ids, value_overrides, options_master, product.get("id", path.stem)
    )

    extra = set(product.keys()) - SCHEMA_ALLOWED_FIELDS
    for k in extra:
        product.pop(k)

    return product


# ─── BUILD ───────────────────────────────────────────────────────
def build(version: str, schema_version: str) -> dict:
    schema_path = MASTER_DIR / f"_schema-v{schema_version}.json"
    if not schema_path.exists():
        sys.exit(f"ERROR: Schema not found: {schema_path}")
    with schema_path.open(encoding="utf-8") as f:
        schema = json.load(f)

    if not CATEGORIES_FILE.exists():
        sys.exit(f"ERROR: Categories file not found: {CATEGORIES_FILE}")
    with CATEGORIES_FILE.open(encoding="utf-8") as f:
        categories = yaml_load(f.read())

    if not SETTINGS_FILE.exists():
        sys.exit(f"ERROR: Settings file not found: {SETTINGS_FILE}")
    with SETTINGS_FILE.open(encoding="utf-8") as f:
        settings = yaml_load(f.read())

    options_master = load_options_master()
    print(f"Options master: {len(options_master)} option types loaded from _options.yaml")

    md_files = sorted(PRODUCTS_DIR.glob("*.md"))
    if not md_files:
        sys.exit(f"ERROR: No product MD files found in {PRODUCTS_DIR}")

    products = []
    errors = []
    products_with_options = 0
    for path in md_files:
        try:
            product = parse_product_md(path, options_master)
            products.append(product)
            opts_count = len(product.get("options", []))
            if opts_count:
                products_with_options += 1
            print(f"  ✓ {path.name} → {product.get('id', '?')} ({opts_count} options)")
        except Exception as e:
            errors.append(f"  ✗ {path.name}: {e}")

    if errors:
        print("\nPARSE ERRORS:")
        for e in errors:
            print(e)
        sys.exit(1)

    print(f"\n{products_with_options}/{len(products)} products have options[]")

    result = {
        "meta": {
            "version": version,
            "schema_version": schema_version,
            "date": datetime.date.today().isoformat(),
            "author": "Becze Szabolcs / Exar Labs",
            "description": (
                f"Deák Húsmíves termékkatalógus — {len(products)} termék, "
                f"{len(categories)} kategória, {products_with_options} termék VG-opcióval (DH-173). "
                f"Generated from MASTER/products/*.md + _options.yaml."
            ),
        },
        "categories": categories,
        "products": products,
        "settings": settings,
    }

    print(f"\nValidating against schema v{schema_version}...")
    try:
        jsonschema.validate(result, schema)
        print("  ✓ Schema validation passed")
    except jsonschema.ValidationError as e:
        print(f"  ✗ Schema validation FAILED:")
        print(f"    Path: {list(e.path)}")
        print(f"    Message: {e.message}")
        sys.exit(2)

    return result


# ─── CLI ─────────────────────────────────────────────────────────
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--version", default="1.2", help="Products data version (e.g. 1.2)")
    parser.add_argument("--schema-version", default="1.2", help="Schema version (e.g. 1.2)")
    parser.add_argument("--out", default=None, help="Output path (default: generated/products-v{VERSION}.json)")
    args = parser.parse_args()

    print(f"Building products v{args.version} (schema v{args.schema_version})...")
    print(f"Source: {PRODUCTS_DIR}")
    print()

    result = build(args.version, args.schema_version)

    out_path = Path(args.out) if args.out else GENERATED_DIR / f"products-v{args.version}.json"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with out_path.open("w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)

    print(f"\n✓ Written: {out_path}")
    print(f"  {len(result['products'])} products, {len(result['categories'])} categories, settings included")


if __name__ == "__main__":
    main()
