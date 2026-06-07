---
title: Watch skill — local Whisper patch
date: 2026-05-28
author: Becze Szabolcs
status: active
description: A `claude-video` (/watch) skill patch-e, ami lokális faster-whisper (large-v3-turbo) backendet ad az eredetileg API-only (Groq/OpenAI) transcript-réteghez. Offline, ingyen, magyar ASR. Újra-alkalmazandó ha a /plugin update vagy git pull felülírja a skillt.
tags: [bdos, watch, whisper, faster-whisper, patch, reel-factory]
id: 6547b026-f510-47d3-8738-0425d0fbe5db
index_schema_version: 1
---

# Watch skill — local Whisper patch

## Mi ez

A `~/.claude/skills/watch/` (`claude-video` by Brad Automates) skill **eredetileg API-only** Whisper transcripttel (Groq `whisper-large-v3` / OpenAI `whisper-1`). Ez a patch egy **lokális backendet** ad: `faster-whisper` + `large-v3-turbo` model — offline, kulcs nélkül, Apple Silicon CPU-n gyors.

## Telepítési előfeltétel

```bash
python3 -m pip install --user faster-whisper
```
(Telepítve 2026-05-28: faster-whisper 1.2.1 + ctranslate2 4.7.2)

## Mit módosít

- **`scripts/whisper.py`**: új `local_available()`, `resolve_backend()`, `transcribe_local()` függvények + `transcribe_video()` route a `local` backendre. `LOCAL_MODEL = "large-v3-turbo"`.
- **`scripts/watch.py`**: `--whisper` choices bővítés (`local`), import `resolve_backend`, és a transcript-blokk a `resolve_backend()`-et hívja `load_api_key()` helyett.

## Viselkedés a patch után

| `--whisper` flag | Mit használ |
|---|---|
| (nincs) | API kulcs ha van (Groq>OpenAI), különben **auto-fallback local** ha faster-whisper telepítve |
| `local` | lokális `large-v3-turbo`, offline |
| `groq` / `openai` | csak az adott API |
| `--no-whisper` | nincs transcript (frames-only) |

Fontos: a Whisper csak akkor fut, ha **nincs natív caption** (a caption mindig elsőbbség). Saját Navigator-epizódoknál amúgy is van full SRT ground-truth — a /watch transcriptje főleg **versenytárs-videókon** számít.

## Újra-alkalmazás (ha /plugin update vagy git pull felülírta)

```bash
cd ~/.claude/skills/watch && git apply "/Users/becze-mac/My Drive (beczesz.szabolcs@gmail.com)/0. Ideas Vault/00_Prompts/BDOS/capabilities/reel-factory/patches/watch-local-whisper.patch"
```

Ha a `git apply` konfliktusol (upstream is változtatta ugyanazokat a sorokat), kézzel kell újra-portolni a `whisper.py` + `watch.py` változásokat a fenti leírás alapján.

## Model cache

Első futás letölti a `large-v3-turbo`-t (~1.5 GB) ide: `~/.cache/huggingface/`. Későbbi futások onnan töltik.

## Kapcsolódó

- Patch fájl: [`watch-local-whisper.patch`](watch-local-whisper.patch)
- Skill teszt-napló: [`../../../_inbox/youtube-skill-integration-candidates.md`](../../../_inbox/youtube-skill-integration-candidates.md)
- reel-factory (lokális Whisper testvér-use): [`../CLAUDE.md`](../CLAUDE.md)
