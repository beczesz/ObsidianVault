#!/usr/bin/env python3
"""BDOS Vault Indexing — cross-platform runtime paths & process utilities.

The vault itself is synced across machines (Google Drive) between macOS and
Windows. Runtime state that must NOT be shared between machines lives here,
OUTSIDE the synced vault tree, under a per-machine app-data directory:

  - vault.db    the regenerable FTS index — writing it from two machines at
                once would produce Google Drive conflict copies and corrupt
                the SQLite file, so each machine keeps its own local copy
  - watch.pid / events.pid   a PID is meaningless on another machine/OS
  - watch.log / events.log   per-machine watcher output

Auto-detection: the OS is detected here and the right app-data location is
chosen. Override everything with the BDOS_CACHE_DIR env var (used by tests
and by anyone who wants the legacy in-vault location back).

NOT relocated here: agent_observability.db, marketing_board.json sidecar, and
the marketing-board lock/log — those stay in the synced cache/ on purpose
(unified agent logs + dashboard sidecar are meant to be shared).
"""

import os
import platform
import sqlite3
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
# Legacy / synced location — still home to agent_observability.db and sidecars,
# and used as a read-only fallback for vault.db during the per-machine migration.
SYNCED_CACHE = SCRIPT_DIR / "cache"
LEGACY_DB = SYNCED_CACHE / "vault.db"


def machine_cache_dir() -> Path:
    """Per-machine, non-synced cache dir. Override with BDOS_CACHE_DIR."""
    override = os.environ.get("BDOS_CACHE_DIR")
    if override:
        p = Path(override)
    else:
        sysname = platform.system()
        if sysname == "Windows":
            base = os.environ.get("LOCALAPPDATA") or str(Path.home() / "AppData" / "Local")
            p = Path(base) / "bdos-vault-index"
        elif sysname == "Darwin":
            p = Path.home() / "Library" / "Application Support" / "bdos-vault-index"
        else:  # Linux / other POSIX
            base = os.environ.get("XDG_CACHE_HOME") or str(Path.home() / ".cache")
            p = Path(base) / "bdos-vault-index"
    p.mkdir(parents=True, exist_ok=True)
    return p


CACHE_DIR = machine_cache_dir()

# Writers (build_index, watch_event, watch) always target the local copy.
DB_PATH = CACHE_DIR / "vault.db"

PID_WATCHER = CACHE_DIR / "watch.pid"
PID_EVENTS = CACHE_DIR / "events.pid"
LOG_WATCH = CACHE_DIR / "watch.log"
LOG_EVENTS = CACHE_DIR / "events.log"


def db_read_path() -> Path:
    """Path a READER should open. Prefer the local per-machine index; fall back
    to the legacy synced index if the local one hasn't been built yet (keeps the
    other machine working during the migration). Writers must use DB_PATH."""
    if DB_PATH.exists():
        return DB_PATH
    if LEGACY_DB.exists():
        return LEGACY_DB
    return DB_PATH  # canonical location for the "not built yet" error message


def connect(db_path, *, wal: bool = True, busy_timeout_ms: int = 5000, timeout: float = 10.0):
    """Open a SQLite connection with sane concurrency defaults (B2, 2026-05-29).

    - busy_timeout: wait instead of failing immediately when the DB is briefly
      locked (default was 0 = fail-fast, the main "database is locked" source).
    - WAL: readers don't block the single writer and vice versa.

    WAL is a persistent DB-level setting, so setting it here is idempotent. New
    code should prefer this helper; existing scattered sqlite3.connect() sites
    can migrate incrementally (separate hygiene task).
    """
    con = sqlite3.connect(str(db_path), timeout=timeout)
    con.execute(f"PRAGMA busy_timeout={int(busy_timeout_ms)}")
    if wal:
        con.execute("PRAGMA journal_mode=WAL")
    return con


def read_pid(pid_file: Path) -> int:
    try:
        return int(Path(pid_file).read_text().strip())
    except (OSError, ValueError):
        return 0


def pid_is_running(pid: int) -> bool:
    """Cross-platform 'is this PID alive' check."""
    if not pid or pid <= 0:
        return False
    if platform.system() == "Windows":
        import ctypes
        PROCESS_QUERY_LIMITED_INFORMATION = 0x1000
        STILL_ACTIVE = 259
        kernel32 = ctypes.windll.kernel32
        handle = kernel32.OpenProcess(PROCESS_QUERY_LIMITED_INFORMATION, False, pid)
        if not handle:
            return False
        try:
            code = ctypes.c_ulong()
            if kernel32.GetExitCodeProcess(handle, ctypes.byref(code)):
                return code.value == STILL_ACTIVE
            return False
        finally:
            kernel32.CloseHandle(handle)
    else:
        try:
            os.kill(pid, 0)
        except ProcessLookupError:
            return False
        except PermissionError:
            return True
        return True
