#!/usr/bin/env python3
"""Reel Factory — YouTube long-form → short reel pipeline.

Subcommands:
    download URL                                   download YT source at best quality
    clip SRC --start MM:SS --end MM:SS             frame-accurate trim
    reframe SRC --aspect 9:16                      reframe with blurred background
    transcribe SRC                                 Whisper → .srt (fallback only)
    extract-subs FULL_SRT --start --end            slice + shift the full-episode SRT
    compose VIDEO --subs SRT [--music] [--title]   burn subs + title + mix music
    full URL --start --end [--full-srt] [--title]  end-to-end
    publish REEL --dest DIR --slug SLUG            copy reel to area folder + scaffold PUBLISH.md

Preferred input for the subtitle layer is the FULL episode SRT (manually-vetted
ground truth). Use `extract-subs` to slice it for the clip. Whisper output is a
fallback only — see CLAUDE.md §0 (workflow rule).

Working/intermediate files live under the capability's output/ scratch dir.
FINAL deliverables go to the AREA's own folder via `publish` (e.g. a Navigátor
episode's Reels/ subfolder) — never committed to the capability. See CLAUDE.md
§ "Tárolási konvenció".
"""
from __future__ import annotations

import argparse
import json
import shlex
import shutil
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path

# Windows: default console is cp1252 — force utf-8 so non-ASCII (→, accents) survive.
try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except (AttributeError, OSError):
    pass

CAPABILITY_ROOT = Path(__file__).resolve().parent.parent
OUTPUT_ROOT = CAPABILITY_ROOT / "output"

# --- subtitle style — v0.2 standard (Iter 3: Opus-konform) ---
# Bold sans-serif, drop-shadow style, lower-third position.
#
# IMPORTANT: libass with no ASS header uses default PlayResY=288. Fontsize and
# MarginV are in those 288 logical units, scaled to actual video height
# (1920 / 288 ≈ 6.67x). So:
#   Fontsize=18 → ~120 actual pixels (large, readable, Opus-like)
#   MarginV=70  → ~466 actual pixels from bottom = y=1454 (lower third)
# If you need pixel-direct sizing, prefer generating an .ass with PlayResY=1920.
SUBTITLE_STYLE = (
    "Fontname=Arial,Fontsize=18,Bold=1,"
    "PrimaryColour=&H00FFFFFF,OutlineColour=&H00000000,"
    "BorderStyle=1,Outline=2,Shadow=2,"
    "Alignment=2,MarginV=70"
)

# --- title-card style (Iter 3) ---
TITLE_FONT_CANDIDATES = [
    "C:/Windows/Fonts/seguibl.ttf",   # Segoe UI Black
    "C:/Windows/Fonts/segoeuib.ttf",  # Segoe UI Bold
    "C:/Windows/Fonts/arialbd.ttf",   # Arial Bold
]
TITLE_DEFAULT_DURATION = 3.5    # seconds the title pill is visible
TITLE_PADDING_X = 28
TITLE_PADDING_Y = 18
TITLE_FONT_SIZE = 46
TITLE_LINE_GAP = 6
TITLE_RADIUS = 22
TITLE_MAX_WIDTH = 940           # px, fits inside 1080 with margins
TITLE_BG_RGBA = (255, 255, 255, 255)
TITLE_TEXT_RGB = (18, 18, 18)
TITLE_TOP_MARGIN_FRAC = 0.06    # 6% from top of canvas


# ---------------------------------------------------------------------------
# helpers
# ---------------------------------------------------------------------------

def run(cmd: list[str], cwd: Path | None = None, env_extra: dict | None = None) -> None:
    """Run a command, stream output, raise on failure."""
    print(f"\n$ {' '.join(shlex.quote(c) for c in cmd)}")
    env = None
    if env_extra:
        import os
        env = os.environ.copy()
        env.update(env_extra)
    result = subprocess.run(cmd, cwd=cwd, env=env)
    if result.returncode != 0:
        sys.exit(f"FAIL: exit {result.returncode}")


def workdir(slug: str) -> Path:
    p = OUTPUT_ROOT / slug
    p.mkdir(parents=True, exist_ok=True)
    return p


def probe_duration(path: Path) -> float:
    out = subprocess.check_output([
        "ffprobe", "-v", "error", "-show_entries", "format=duration",
        "-of", "json", str(path),
    ])
    return float(json.loads(out)["format"]["duration"])


# ---------------------------------------------------------------------------
# SRT parsing / slicing
# ---------------------------------------------------------------------------

def parse_timestamp(ts: str) -> float:
    """Parse 'HH:MM:SS', 'MM:SS', or 'HH:MM:SS,mmm' (SRT) to seconds."""
    ts = ts.strip().replace(",", ".")
    parts = ts.split(":")
    if len(parts) == 3:
        h, m, s = parts
        return int(h) * 3600 + int(m) * 60 + float(s)
    if len(parts) == 2:
        m, s = parts
        return int(m) * 60 + float(s)
    return float(ts)


def fmt_srt_ts(t: float) -> str:
    """seconds → 'HH:MM:SS,mmm'."""
    if t < 0:
        t = 0
    h = int(t // 3600)
    m = int((t % 3600) // 60)
    s = t % 60
    return f"{h:02d}:{m:02d}:{s:06.3f}".replace(".", ",")


def parse_srt(text: str) -> list[dict]:
    """Parse SRT into list of {index, start, end, text} dicts (times in seconds)."""
    # tolerate BOM, CRLF
    text = text.lstrip("﻿").replace("\r\n", "\n").replace("\r", "\n")
    entries = []
    for block in text.strip().split("\n\n"):
        lines = [ln for ln in block.split("\n") if ln.strip()]
        if len(lines) < 2:
            continue
        # first line MIGHT be index; we trust the second line has ' --> '
        ts_line_idx = 0 if "-->" in lines[0] else 1
        if ts_line_idx >= len(lines) or "-->" not in lines[ts_line_idx]:
            continue
        ts_line = lines[ts_line_idx]
        start_s, end_s = [p.strip() for p in ts_line.split("-->")]
        entries.append({
            "start": parse_timestamp(start_s),
            "end": parse_timestamp(end_s),
            "text": "\n".join(lines[ts_line_idx + 1:]),
        })
    return entries


def slice_srt(entries: list[dict], start: float, end: float) -> list[dict]:
    """Keep entries overlapping [start, end] and shift to clip-relative."""
    out = []
    for e in entries:
        if e["end"] <= start or e["start"] >= end:
            continue
        new_start = max(e["start"], start) - start
        new_end = min(e["end"], end) - start
        if new_end <= new_start:
            continue
        out.append({"start": new_start, "end": new_end, "text": e["text"]})
    return out


def split_entry_to_fragments(entry: dict, max_words: int) -> list[dict]:
    """Split one entry into max_words-sized chunks with proportional timing.

    Long SRT entries (5-10s, 15+ words) read as a wall of text. Opus-style
    karaoke uses 1-3 words per pulse. This function does the time-arithmetic
    to break a long entry evenly across its duration.
    """
    text = " ".join(entry["text"].split())  # collapse whitespace
    words = text.split()
    if len(words) <= max_words or max_words <= 0:
        return [{"start": entry["start"], "end": entry["end"], "text": text}]

    duration = entry["end"] - entry["start"]
    total = len(words)
    fragments: list[dict] = []
    i = 0
    while i < total:
        chunk = words[i : i + max_words]
        frag_start = entry["start"] + duration * i / total
        frag_end = entry["start"] + duration * (i + len(chunk)) / total
        fragments.append({
            "start": frag_start,
            "end": frag_end,
            "text": " ".join(chunk),
        })
        i += max_words
    return fragments


def fragment_entries(entries: list[dict], max_words: int) -> list[dict]:
    """Apply word-fragment splitting to all entries."""
    if max_words <= 0:
        return entries
    out = []
    for e in entries:
        out.extend(split_entry_to_fragments(e, max_words))
    return out


def write_srt(entries: list[dict], out: Path) -> None:
    out.parent.mkdir(parents=True, exist_ok=True)
    lines = []
    for i, e in enumerate(entries, start=1):
        lines.append(str(i))
        lines.append(f"{fmt_srt_ts(e['start'])} --> {fmt_srt_ts(e['end'])}")
        lines.append(e["text"])
        lines.append("")
    out.write_text("\n".join(lines), encoding="utf-8")


# ---------------------------------------------------------------------------
# Title-card PNG renderer (Iter 3)
# ---------------------------------------------------------------------------

def _pick_title_font(size: int):
    from PIL import ImageFont
    for path in TITLE_FONT_CANDIDATES:
        if Path(path).exists():
            return ImageFont.truetype(path, size)
    return ImageFont.load_default()


def _wrap_to_width(text: str, font, max_w: int) -> list[str]:
    words = text.split()
    lines, cur = [], []
    for w in words:
        test = " ".join(cur + [w])
        bbox = font.getbbox(test)
        if (bbox[2] - bbox[0]) <= max_w or not cur:
            cur.append(w)
        else:
            lines.append(" ".join(cur))
            cur = [w]
    if cur:
        lines.append(" ".join(cur))
    return lines


def render_title_png(text: str, out: Path, font_size: int = TITLE_FONT_SIZE) -> tuple[int, int]:
    """Render a 'pill' title card to PNG (transparent background, rounded white box).

    Returns (width, height) of the rendered image in pixels.
    """
    from PIL import Image, ImageDraw

    font = _pick_title_font(font_size)
    inner_w = TITLE_MAX_WIDTH - 2 * TITLE_PADDING_X
    lines = _wrap_to_width(text, font, inner_w)

    # measure
    ascent_box = font.getbbox("ÁgyŐű")  # tall + descender reference
    line_h = ascent_box[3] - ascent_box[1] + TITLE_LINE_GAP
    text_h = line_h * len(lines)
    text_w = max((font.getbbox(line)[2] - font.getbbox(line)[0]) for line in lines)

    box_w = text_w + 2 * TITLE_PADDING_X
    box_h = text_h + 2 * TITLE_PADDING_Y - TITLE_LINE_GAP

    out.parent.mkdir(parents=True, exist_ok=True)
    img = Image.new("RGBA", (box_w, box_h), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    draw.rounded_rectangle(
        [(0, 0), (box_w - 1, box_h - 1)],
        radius=TITLE_RADIUS,
        fill=TITLE_BG_RGBA,
    )

    y = TITLE_PADDING_Y - ascent_box[1]  # align baseline accounting for top of bbox
    for line in lines:
        w = font.getbbox(line)[2] - font.getbbox(line)[0]
        x = (box_w - w) // 2 - font.getbbox(line)[0]
        draw.text((x, y), line, font=font, fill=TITLE_TEXT_RGB)
        y += line_h

    img.save(out, "PNG")
    return box_w, box_h


# ---------------------------------------------------------------------------
# extract-subs command (Iter 3)
# ---------------------------------------------------------------------------

def cmd_extract_subs(
    full_srt: Path, start: str, end: str, out: Path,
    max_words_per_frag: int = 3,
) -> None:
    """Slice the full-episode SRT to [start, end], shift, optionally word-split.

    max_words_per_frag=0 keeps entries as-is (no Opus-style fragmentation).
    Default 3 gives Opus-style karaoke pulses.
    """
    start_s = parse_timestamp(start)
    end_s = parse_timestamp(end)
    entries = parse_srt(full_srt.read_text(encoding="utf-8"))
    sliced = slice_srt(entries, start_s, end_s)
    fragmented = fragment_entries(sliced, max_words_per_frag)
    write_srt(fragmented, out)
    note = "" if max_words_per_frag <= 0 else f" (fragmented to ≤{max_words_per_frag} words each)"
    print(f"  → wrote {len(fragmented)} entries to {out}{note}")


# ---------------------------------------------------------------------------
# step 1 — download
# ---------------------------------------------------------------------------

def cmd_download(url: str, out: Path) -> None:
    """Download YT source at best mp4 quality."""
    out.parent.mkdir(parents=True, exist_ok=True)
    run([
        "yt-dlp",
        "-f", "bv*[ext=mp4]+ba[ext=m4a]/b[ext=mp4]/bv*+ba/b",
        "--merge-output-format", "mp4",
        "-o", str(out),
        url,
    ])


# ---------------------------------------------------------------------------
# step 2 — clip (frame-accurate trim)
# ---------------------------------------------------------------------------

def cmd_clip(src: Path, start: str, end: str, out: Path) -> None:
    """Trim [start, end]. Re-encodes for frame accuracy.

    -ss is placed AFTER -i (output seek) so libavformat decodes from the start
    and ffmpeg discards frames until `start`. Input seek (-ss before -i) snaps
    to the nearest keyframe before target and can pull in earlier frames.
    Output seek is slower but frame-accurate — critical for outros and tight
    edits.
    """
    run([
        "ffmpeg", "-y",
        "-i", str(src),
        "-ss", start, "-to", end,
        "-c:v", "libx264", "-preset", "medium", "-crf", "18",
        "-c:a", "aac", "-b:a", "192k",
        str(out),
    ])


# ---------------------------------------------------------------------------
# step 3 — reframe to 9:16 with blurred background
# ---------------------------------------------------------------------------

REFRAME_FILTERS = {
    "9:16": {
        "W": 1080, "H": 1920,
        # split into bg (cropped+blurred) and fg (scaled to fit width),
        # overlay fg centered on the blurred bg
        "filter": (
            "[0:v]split=2[bg][fg];"
            "[bg]scale={W}:{H}:force_original_aspect_ratio=increase,"
            "crop={W}:{H},boxblur=20:5,eq=brightness=-0.10[bgblur];"
            "[fg]scale={W}:-2[fgs];"
            "[bgblur][fgs]overlay=(W-w)/2:(H-h)/2"
        ),
    },
    "1:1": {
        "W": 1080, "H": 1080,
        "filter": (
            "[0:v]split=2[bg][fg];"
            "[bg]scale={W}:{H}:force_original_aspect_ratio=increase,"
            "crop={W}:{H},boxblur=20:5,eq=brightness=-0.10[bgblur];"
            "[fg]scale={W}:-2[fgs];"
            "[bgblur][fgs]overlay=(W-w)/2:(H-h)/2"
        ),
    },
}


def cmd_reframe(src: Path, aspect: str, out: Path) -> None:
    """Reframe to 9:16 (or 1:1) with blurred background."""
    if aspect not in REFRAME_FILTERS:
        sys.exit(f"unknown aspect: {aspect} (try: {list(REFRAME_FILTERS)})")
    spec = REFRAME_FILTERS[aspect]
    flt = spec["filter"].format(W=spec["W"], H=spec["H"])
    run([
        "ffmpeg", "-y",
        "-i", str(src),
        "-filter_complex", flt,
        "-c:v", "libx264", "-preset", "medium", "-crf", "18",
        "-c:a", "copy",
        str(out),
    ])


# ---------------------------------------------------------------------------
# step 4 — Whisper transcribe → .srt
# ---------------------------------------------------------------------------

def cmd_transcribe(src: Path, lang: str, model: str, out: Path, device: str = "cpu") -> None:
    """Run Whisper on src, write .srt to `out`. lang ISO-name (e.g. Hungarian).

    device defaults to cpu — on this Windows box the installed torch CUDA
    kernels are not compatible with the GPU, and Whisper's own stdout
    `print()` calls die on cp1252 if PYTHONIOENCODING isn't utf-8.
    """
    out_dir = out.parent
    out_dir.mkdir(parents=True, exist_ok=True)
    run(
        [
            "whisper", str(src),
            "--language", lang,
            "--model", model,
            "--device", device,
            "--output_format", "srt",
            "--output_dir", str(out_dir),
        ],
        env_extra={"PYTHONIOENCODING": "utf-8"},
    )
    # whisper names output after input stem
    produced = out_dir / (src.stem + ".srt")
    if produced != out:
        if out.exists():
            out.unlink()
        produced.rename(out)


# ---------------------------------------------------------------------------
# step 5 — compose final (burn subs + optional music mix)
# ---------------------------------------------------------------------------

DEFAULT_OUTRO = (
    Path(__file__).resolve().parent.parent / "assets" / "templates" / "outro-v0.mp4"
)


def _resolve_outro(arg) -> Path | None:
    """Accept Path, 'none', or None. Returns Path or None (= skip outro)."""
    if arg is None:
        return None
    if isinstance(arg, str) and arg.lower() == "none":
        return None
    p = Path(arg)
    if not p.exists():
        print(f"[warn] outro {p} does not exist — skipping")
        return None
    return p


def append_outro(main: Path, outro: Path, out: Path) -> None:
    """Concat outro mp4 to the end of main mp4 via the concat *demuxer*.

    Both must share specs (1080×1920, 25 fps, h264, aac). Codec copy — no
    re-encode, finishes in well under a second.

    The filter_complex variant (concat filter + re-encode) failed with
    EINVAL on this toolchain, even though the streams were spec-identical.
    The demuxer path is also strictly preferable when specs match.
    """
    listfile = main.parent / "_concat_list.txt"
    # Use forward slashes and absolute paths — robust on Windows.
    lines = [
        f"file '{main.resolve().as_posix()}'",
        f"file '{outro.resolve().as_posix()}'",
    ]
    listfile.write_text("\n".join(lines) + "\n", encoding="ascii")
    try:
        run([
            "ffmpeg", "-y",
            "-f", "concat", "-safe", "0",
            "-i", str(listfile),
            "-c", "copy",
            "-movflags", "+faststart",
            str(out),
        ])
    finally:
        listfile.unlink(missing_ok=True)


def cmd_compose(
    video: Path,
    subs: Path | None,
    music: Path | None,
    music_vol: float,
    out: Path,
    title: str | None = None,
    title_duration: float = TITLE_DEFAULT_DURATION,
    outro: Path | None = None,
) -> None:
    """Burn subs + optional title-card + optional music ducking → final mp4.

    Single ffmpeg pass with filter_complex. Stages inputs into the work dir
    to avoid Windows path-colon escaping pain in the subtitles filter.
    """
    work = video.parent
    staged_video = "stage_in.mp4"
    staged_out = "stage_out.mp4"
    staged_subs = "stage_subs.srt"
    staged_title = "stage_title.png"

    if (work / staged_video).exists():
        (work / staged_video).unlink()
    shutil.copy(video, work / staged_video)
    if subs is not None:
        shutil.copy(subs, work / staged_subs)

    title_size = None
    if title:
        title_size = render_title_png(title, work / staged_title)

    # Build inputs in fixed order: video, [music?], [title?]
    cmd = ["ffmpeg", "-y", "-i", staged_video]
    next_input = 1
    music_idx = title_idx = None
    if music is not None:
        cmd += ["-stream_loop", "-1", "-i", str(music)]
        music_idx = next_input
        next_input += 1
    if title:
        cmd += ["-i", staged_title]
        title_idx = next_input
        next_input += 1

    # Build the video filter chain step by step
    video_chain = "[0:v]"
    last_label = "[0:v]"
    filter_parts = []

    if subs is not None:
        filter_parts.append(
            f"[0:v]subtitles=filename='{staged_subs}':force_style='{SUBTITLE_STYLE}'[vsub]"
        )
        last_label = "[vsub]"

    if title:
        # overlay at top-center, visible for `title_duration` seconds
        # canvas H is the input video H; place at top_margin_frac
        # ffmpeg overlay accepts H/W placeholders for video, w/h for overlay
        filter_parts.append(
            f"{last_label}[{title_idx}:v]overlay="
            f"x=(W-w)/2:y=H*{TITLE_TOP_MARGIN_FRAC}:"
            f"enable='lt(t,{title_duration})'[vout]"
        )
        last_label = "[vout]"

    if music is not None:
        filter_parts.append(
            f"[{music_idx}:a]volume={music_vol},afade=t=in:st=0:d=0.5[bg]"
        )
        filter_parts.append(
            "[0:a][bg]amix=inputs=2:duration=first:dropout_transition=2[aout]"
        )
        audio_label = "[aout]"
    else:
        audio_label = "0:a"

    if filter_parts:
        cmd += ["-filter_complex", ";".join(filter_parts)]
        if last_label != "[0:v]":
            cmd += ["-map", last_label]
        else:
            cmd += ["-map", "0:v"]
        cmd += ["-map", audio_label]
    else:
        cmd += ["-c:a", "copy"]

    cmd += [
        "-c:v", "libx264", "-preset", "medium", "-crf", "18",
        "-movflags", "+faststart",
        staged_out,
    ]
    run(cmd, cwd=work)

    # If an outro is specified, the staged output becomes the "main" — then
    # concat the outro to produce `out`. Otherwise rename staged → out.
    if outro is not None:
        staged_main = work / "stage_main.mp4"
        if staged_main.exists():
            staged_main.unlink()
        (work / staged_out).rename(staged_main)
        if out.exists():
            out.unlink()
        append_outro(staged_main, outro, out)
        staged_main.unlink(missing_ok=True)
    else:
        if out.exists():
            out.unlink()
        (work / staged_out).rename(out)
    (work / staged_video).unlink(missing_ok=True)


# ---------------------------------------------------------------------------
# step 6 — full pipeline
# ---------------------------------------------------------------------------

def cmd_full(args: argparse.Namespace) -> None:
    slug = args.slug
    wd = workdir(slug)
    source = wd / "source.mp4"
    clipped = wd / "clip.mp4"
    reframed = wd / "reframed.mp4"
    subs = wd / "subs.srt"
    final = wd / f"reel-{slug}.mp4"

    if not source.exists() or args.force:
        cmd_download(args.url, source)
    else:
        print(f"[skip] {source} exists — use --force to re-download")

    cmd_clip(source, args.start, args.end, clipped)
    cmd_reframe(clipped, args.aspect, reframed)

    # Prefer the full-episode SRT (ground truth) over Whisper hallucinations.
    if args.full_srt:
        cmd_extract_subs(
            args.full_srt, args.start, args.end, subs,
            max_words_per_frag=args.max_words_per_frag,
        )
    else:
        cmd_transcribe(reframed, args.lang, args.model, subs, device=args.device)

    outro = _resolve_outro(args.outro)
    cmd_compose(
        reframed,
        subs=subs,
        music=Path(args.music) if args.music else None,
        music_vol=args.music_vol,
        out=final,
        title=args.title,
        title_duration=args.title_duration,
        outro=outro,
    )
    print(f"\nDONE → {final}")


# ---------------------------------------------------------------------------
# publish — move the final reel into an area's own deliverable folder
# ---------------------------------------------------------------------------

PUBLISH_TEMPLATE = """\
---
title: {slug}
date: {date}
author: Becze Szabolcs
status: előkészített
description: Publikálásra előkészített reel. Videó + platform-specifikus cím/leírás/tagek. A teljes epizód SRT-jéből készült (ground truth).
---

# {slug}

> **Státusz:** előkészített — publikálásra kész. Töltsd fel a platformokra az alábbi szövegekkel.

## Forrás

- **Epizód:** {episode}
- **Klip:** {clip_range}
- **Title card (a reelen):** {title}

## Videó

`{video_name}` — ebben a mappában.

---

## Instagram Reels / Facebook Reels

**Caption:**
```
<TÖLTSD KI>
```

**Hashtagek:**
```
#navigátorpodcast #magyarpodcast
```

## TikTok

**Caption:**
```
<TÖLTSD KI>
```

## YouTube Shorts

**Cím:**
```
<TÖLTSD KI>
```

**Leírás:**
```
<TÖLTSD KI>
```

---

## Publikálási checklist

- [ ] Instagram Reels
- [ ] Facebook Reels
- [ ] TikTok
- [ ] YouTube Shorts
- [ ] (opcionális) Patreon poszt

Publikálás után: a teljes reel-mappa törölhető (a videó a platformokon él).
"""


def cmd_publish(reel: Path, dest: Path, slug: str, title: str = "",
                episode: str = "", clip_range: str = "") -> None:
    """Copy a final reel into <dest>/<slug>/ and scaffold PUBLISH.md.

    `dest` is an AREA folder (e.g. a Navigátor episode's Reels/ dir), NOT the
    capability output. The scaffolded PUBLISH.md is filled in by the operator
    (or the AI) with platform-specific copy.
    """
    import datetime
    reel_dir = dest / slug
    reel_dir.mkdir(parents=True, exist_ok=True)
    video_name = f"{slug}.mp4"
    dest_video = reel_dir / video_name
    shutil.copy(reel, dest_video)

    publish_md = reel_dir / "PUBLISH.md"
    if not publish_md.exists():
        publish_md.write_text(
            PUBLISH_TEMPLATE.format(
                slug=slug,
                date=datetime.date.today().isoformat(),
                episode=episode or "<epizód>",
                clip_range=clip_range or "<klip tartomány>",
                title=title or "<title card szöveg>",
                video_name=video_name,
            ),
            encoding="utf-8",
        )
        print(f"  → scaffolded {publish_md}")
    else:
        print(f"  → {publish_md} exists, left untouched")
    print(f"  → published video to {dest_video}")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="reel", description="Reel Factory pipeline")
    sub = p.add_subparsers(dest="cmd", required=True)

    d = sub.add_parser("download", help="yt-dlp best quality")
    d.add_argument("url")
    d.add_argument("--out", type=Path, required=True)

    c = sub.add_parser("clip", help="frame-accurate trim")
    c.add_argument("src", type=Path)
    c.add_argument("--start", required=True, help="MM:SS or HH:MM:SS")
    c.add_argument("--end", required=True, help="MM:SS or HH:MM:SS")
    c.add_argument("--out", type=Path, required=True)

    r = sub.add_parser("reframe", help="9:16 (or 1:1) with blurred bg")
    r.add_argument("src", type=Path)
    r.add_argument("--aspect", default="9:16", choices=list(REFRAME_FILTERS))
    r.add_argument("--out", type=Path, required=True)

    t = sub.add_parser("transcribe", help="Whisper → .srt")
    t.add_argument("src", type=Path)
    t.add_argument("--lang", default="Hungarian")
    t.add_argument("--model", default="medium",
                   choices=["tiny", "base", "small", "medium", "large"])
    t.add_argument("--device", default="cpu", choices=["cpu", "cuda", "auto"])
    t.add_argument("--out", type=Path, required=True)

    es = sub.add_parser("extract-subs", help="slice + shift full-episode SRT")
    es.add_argument("full_srt", type=Path, help="path to the full episode SRT")
    es.add_argument("--start", required=True, help="MM:SS or HH:MM:SS")
    es.add_argument("--end", required=True, help="MM:SS or HH:MM:SS")
    es.add_argument("--max-words-per-frag", type=int, default=3,
                    help="word-fragment splitter (Opus-style karaoke). 0 = no split.")
    es.add_argument("--out", type=Path, required=True)

    cp = sub.add_parser("compose", help="burn subs + title + mix music + outro")
    cp.add_argument("video", type=Path)
    cp.add_argument("--subs", type=Path)
    cp.add_argument("--title", help="title-card text (top pill)")
    cp.add_argument("--title-duration", type=float, default=TITLE_DEFAULT_DURATION)
    cp.add_argument("--music", type=Path)
    cp.add_argument("--music-vol", type=float, default=0.15)
    cp.add_argument("--outro", type=Path, default=DEFAULT_OUTRO,
                    help="outro mp4 to append (default: assets/templates/outro-v0.mp4). "
                         "Pass 'none' to skip.")
    cp.add_argument("--out", type=Path, required=True)

    f = sub.add_parser("full", help="end-to-end")
    f.add_argument("url")
    f.add_argument("--slug", required=True,
                   help="working dir name under output/")
    f.add_argument("--start", required=True)
    f.add_argument("--end", required=True)
    f.add_argument("--aspect", default="9:16", choices=list(REFRAME_FILTERS))
    f.add_argument("--full-srt", type=Path,
                   help="path to full episode SRT (preferred over Whisper)")
    f.add_argument("--max-words-per-frag", type=int, default=3,
                   help="word-fragment splitter for subs (default 3, 0=off)")
    f.add_argument("--title", help="title-card text (top pill, optional)")
    f.add_argument("--title-duration", type=float, default=TITLE_DEFAULT_DURATION)
    f.add_argument("--outro", type=Path, default=DEFAULT_OUTRO,
                   help="outro mp4 to append (default: outro-v0.mp4). 'none' to skip.")
    f.add_argument("--lang", default="Hungarian")
    f.add_argument("--model", default="medium",
                   choices=["tiny", "base", "small", "medium", "large"])
    f.add_argument("--device", default="cpu", choices=["cpu", "cuda", "auto"])
    f.add_argument("--music", help="path to background music (optional)")
    f.add_argument("--music-vol", type=float, default=0.15)
    f.add_argument("--force", action="store_true",
                   help="re-download even if source exists")

    pub = sub.add_parser("publish", help="copy reel to area folder + scaffold PUBLISH.md")
    pub.add_argument("reel", type=Path, help="final reel mp4")
    pub.add_argument("--dest", type=Path, required=True,
                     help="area deliverable dir (e.g. .../EP43.../Reels)")
    pub.add_argument("--slug", required=True, help="per-reel folder name")
    pub.add_argument("--title", default="", help="title-card text (for PUBLISH.md)")
    pub.add_argument("--episode", default="", help="episode label (for PUBLISH.md)")
    pub.add_argument("--clip-range", default="", help="clip range label (for PUBLISH.md)")
    return p


def main(argv: list[str]) -> None:
    args = build_parser().parse_args(argv)
    if args.cmd == "download":
        cmd_download(args.url, args.out)
    elif args.cmd == "clip":
        cmd_clip(args.src, args.start, args.end, args.out)
    elif args.cmd == "reframe":
        cmd_reframe(args.src, args.aspect, args.out)
    elif args.cmd == "transcribe":
        cmd_transcribe(args.src, args.lang, args.model, args.out, device=args.device)
    elif args.cmd == "extract-subs":
        cmd_extract_subs(
            args.full_srt, args.start, args.end, args.out,
            max_words_per_frag=args.max_words_per_frag,
        )
    elif args.cmd == "compose":
        outro = _resolve_outro(args.outro)
        cmd_compose(
            args.video,
            subs=args.subs,
            music=args.music,
            music_vol=args.music_vol,
            out=args.out,
            title=args.title,
            title_duration=args.title_duration,
            outro=outro,
        )
    elif args.cmd == "full":
        cmd_full(args)
    elif args.cmd == "publish":
        cmd_publish(
            args.reel, args.dest, args.slug,
            title=args.title, episode=args.episode, clip_range=args.clip_range,
        )


if __name__ == "__main__":
    main(sys.argv[1:])
