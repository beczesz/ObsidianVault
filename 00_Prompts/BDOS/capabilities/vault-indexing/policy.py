#!/usr/bin/env python3
"""BDOS Vault Indexing - Coverage Policy (single source of truth).

Declares what counts as vault knowledge and how deeply the index should cover
it. Imported by:
  - build_index.py : what to walk + how to ingest each class
  - watch.py       : inherits walk_vault/index_file from build_index
  - reach.py       : what to reconcile the index against
  - emit_stats.py  : honest coverage denominators

Keeping this in one place means the indexer and the reach auditor can never
silently disagree about what "everything" means. Before this module, the
indexer's reach was an implicit side effect of walk_vault yielding ".md" only.
Now it is an explicit, auditable declaration.
"""

# Directories that are never knowledge (duplicates, build artifacts, vault
# metadata, archives). Pruned during the walk.
EXCLUDE_DIRS = {
    ".smart-env", ".obsidian", ".smart-connections",
    "04_Archive", "_archive_old",          # inactive content, dark on purpose
    "node_modules", ".git", ".trash",      # build artifacts / vcs / trash
    "ExarSharedBrain",                      # nested git repo: vault-mirrored duplicates
}

# Extension classes. Every file lands in exactly one.
FULLTEXT_EXT = {".md", ".srt", ".txt", ".vtt"}                  # body indexed into FTS
METADATA_EXT = {".pdf", ".docx", ".doc", ".xlsx", ".pptx",
                ".ppt", ".epub", ".csv", ".rtf"}                # discoverable stub (no body yet)
MEDIA_EXT = {".mp3", ".m4a", ".wav", ".aac", ".flac",
             ".mp4", ".mov", ".mkv", ".webm",
             ".png", ".jpg", ".jpeg", ".gif", ".webp",
             ".svg", ".heic", ".bmp", ".ico", ".tiff"}          # not text knowledge
ASSET_EXT = {".html", ".css", ".js", ".mjs", ".json", ".py",
             ".sh", ".ps1", ".toml", ".xml", ".xhtml", ".yml",
             ".yaml", ".plist", ".vbs", ".bat", ".ipynb"}        # code / web / config
NOISE_EXT = {".zip", ".gz", ".tar", ".7z", ".rar", ".pyc", ".pyo",
             ".pid", ".lock", ".bak", ".tmp", ".db", ".sqlite",
             ".ds_store", ".log", ".shm", ".wal", ".part", ".crdownload"}

# What the index ingests: full-text bodies + discoverable metadata stubs.
KNOWLEDGE_EXT = FULLTEXT_EXT | METADATA_EXT


def ext_of(name):
    """Lowercased extension with leading dot, or '' if none."""
    if "." not in name:
        return ""
    return "." + name.rsplit(".", 1)[1].lower()


def classify(ext):
    """One of: fulltext, metadata, media, asset, noise, unclassified."""
    if ext in FULLTEXT_EXT:
        return "fulltext"
    if ext in METADATA_EXT:
        return "metadata"
    if ext in MEDIA_EXT:
        return "media"
    if ext in ASSET_EXT:
        return "asset"
    if ext in NOISE_EXT:
        return "noise"
    return "unclassified"


def is_knowledge(ext):
    return ext in KNOWLEDGE_EXT
