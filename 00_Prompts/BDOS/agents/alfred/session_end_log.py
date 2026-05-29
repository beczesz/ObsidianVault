#!/usr/bin/env python3
"""
session_end_log.py — Claude Code SessionEnd hook → Alfred activity ledger.
===========================================================================
Fires ONCE when a vault Claude Code session ends (project-scoped hook, so it
only runs for sessions in this vault). Reads the session transcript, asks
Haiku 4.5 for a one-line "what was accomplished" summary, and appends it to the
per-machine markdown ledger shard via ledger_append.sh.

This is the primary AUTOMATIC feed for "what did I do" — one big-event line per
work session (inherently non-granular). No git, no DB. Sync-safe (per-machine
shard). Robust: any failure is swallowed and the script always exits 0 so it
can never block a session from ending.

Input: SessionEnd hook JSON on stdin (cwd, transcript_path, session_id, reason).
"""
import json
import os
import ssl
import subprocess
import sys
import urllib.request


def _ssl_context():
    """Build an SSL context with a working CA bundle (Python.org python on macOS
    has no system certs; certifi provides them). Falls back to default."""
    try:
        import certifi
        return ssl.create_default_context(cafile=certifi.where())
    except Exception:
        try:
            return ssl.create_default_context()
        except Exception:
            return None

HERE = os.path.dirname(os.path.abspath(__file__))
APPEND = os.path.join(HERE, "ledger_append.sh")
MODEL = "claude-haiku-4-5"
MAX_TRANSCRIPT_CHARS = 6000


def _strip_code(text):
    """Drop fenced code blocks and collapse whitespace, so the summary model
    sees intent prose, not code it might echo/continue."""
    out, in_fence = [], False
    for ln in text.splitlines():
        if ln.lstrip().startswith("```"):
            in_fence = not in_fence
            continue
        if not in_fence:
            out.append(ln)
    return " ".join(" ".join(out).split())


def read_transcript_text(path):
    """Build a clean intent-focused digest from a Claude Code JSONL transcript.

    Strategy: the USER turns state what was actually asked for ("what we did");
    they are the cleanest, least-echoable signal. We keep all user turns (code
    stripped) plus short tails of assistant turns for outcome context. Returns
    (digest_text, n_user_turns)."""
    if not path or not os.path.isfile(path):
        return "", 0
    user_turns, assistant_tails, n_user = [], [], 0
    try:
        with open(path, "r", encoding="utf-8", errors="replace") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    obj = json.loads(line)
                except ValueError:
                    continue
                msg = obj.get("message") or obj
                role = msg.get("role") or obj.get("type")
                if role not in ("user", "assistant"):
                    continue
                content = msg.get("content")
                if isinstance(content, str):
                    text = content
                elif isinstance(content, list):
                    text = " ".join(b.get("text", "") for b in content
                                     if isinstance(b, dict) and b.get("type") == "text")
                else:
                    text = ""
                text = _strip_code(text)
                if not text or text.startswith("<") or len(text) < 3:
                    continue
                if role == "user":
                    n_user += 1
                    user_turns.append("- " + text[:400])
                else:
                    assistant_tails.append(text[:160])
    except OSError:
        return "", 0
    if n_user == 0:
        return "", 0
    digest = ("FELHASZNÁLÓI KÉRÉSEK (időrendben):\n" + "\n".join(user_turns)
              + "\n\nNÉHÁNY EREDMÉNY-RÉSZLET:\n" + " | ".join(assistant_tails[-12:]))
    if len(digest) > MAX_TRANSCRIPT_CHARS:
        # keep the user-requests head (intent) over assistant tails
        digest = digest[:MAX_TRANSCRIPT_CHARS]
    return digest, n_user


def haiku_summary(transcript_text):
    """One-line Hungarian summary via Anthropic API. Returns None on any failure."""
    key = os.environ.get("ANTHROPIC_API_KEY")
    if not key or not transcript_text.strip():
        return None
    sys_prompt = (
        "A bemenet egy munka-session naplója (felhasználói kérések + eredmény-részletek). "
        "A feladatod: írj egy TÉNYKÖZLŐ összefoglalót arról, MIVEL FOGLALKOZTUNK ebben a "
        "sessionben, 1-2 tömör magyar mondatban. "
        "SZABÁLYOK: (1) NE folytasd és NE másold a bemenet szövegét. (2) Csak sima próza, "
        "TILOS a kód, backtick, kódblokk, felsorolás. (3) Az eredményekre/témákra fókuszálj, "
        "ne a lépésekre. (4) SOHA ne használj gondolatjelet (—), helyette vessző. "
        "Csak magát az összefoglalót add vissza, semmi mást."
    )
    body = json.dumps({
        "model": MODEL,
        "max_tokens": 220,
        "system": sys_prompt,
        "messages": [{"role": "user", "content": transcript_text}],
    }).encode("utf-8")
    req = urllib.request.Request(
        "https://api.anthropic.com/v1/messages",
        data=body,
        headers={
            "content-type": "application/json",
            "x-api-key": key,
            "anthropic-version": "2023-06-01",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=30, context=_ssl_context()) as resp:
            data = json.loads(resp.read().decode("utf-8"))
        parts = [b.get("text", "") for b in data.get("content", []) if b.get("type") == "text"]
        line = " ".join(" ".join(parts).split())
        line = line.replace("—", ",").replace("--", ",").strip()
        return line or None
    except Exception:
        return None


def append_ledger(summary):
    try:
        subprocess.run(
            ["bash", APPEND, "--source", "session", "--category", "session",
             "--summary", summary],
            check=False, capture_output=True, timeout=15,
        )
    except Exception:
        pass


def main():
    try:
        payload = json.load(sys.stdin)
    except Exception:
        return  # no/invalid payload → nothing to do
    transcript_path = payload.get("transcript_path", "")
    text, n_turns = read_transcript_text(transcript_path)
    if n_turns == 0:
        return  # empty session → skip (don't log noise)
    summary = haiku_summary(text)
    if not summary:
        # Fallback: no API / failure. Still record that a session happened.
        summary = f"Munka-session lezárult ({n_turns} üzenet); részletek a ledgerben nélkül (AI összegzés nem elérhető)."
    append_ledger(summary)


if __name__ == "__main__":
    try:
        main()
    finally:
        sys.exit(0)  # NEVER block session end
