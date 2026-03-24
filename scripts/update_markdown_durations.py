#!/usr/bin/env python3
"""
Recalculate `duration` frontmatter: sum of Adobe TV video length(s) + reading time at 230 wpm.
Resolves {{$include ...}} for word count. Skips help/**/TOC.md and help/_includes/*.
"""
from __future__ import annotations

import json
import re
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
HELP = REPO / "help"
WPM = 230
INCLUDE_RE = re.compile(r"\{\{\$include\s+([^}]+?)\}\}")
# Only embedded players — not bare video links in prose or related-links lists
EMBED_VIDEO_RE = re.compile(
    r">\[!VIDEO\]\([^)]*video\.tv\.adobe\.com/v/(\d+)", re.IGNORECASE
)
# ms durations in bridge JSON (filter tiny playlist 0s entries)
DURATION_MS_RE = re.compile(r'"duration":(\d{4,})')


def strip_frontmatter(raw: str) -> str:
    if not raw.startswith("---"):
        return raw
    parts = raw.split("---", 2)
    if len(parts) < 3:
        return raw
    return parts[2].lstrip("\n")


def words_in_markdown(text: str) -> int:
    text = re.sub(r">\[!VIDEO\][^\n]*\n?", " ", text)
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"[#>*_`]", " ", text)
    text = re.sub(r"^[\s]*[-*+]\s+", " ", text, flags=re.M)
    text = re.sub(r"\s+", " ", text).strip()
    return len(text.split()) if text else 0


def collect_text_with_includes(body: str, visited: set[Path]) -> str:
    chunks = [body]
    for m in INCLUDE_RE.finditer(body):
        p = m.group(1).strip().lstrip("/")
        if not p.startswith("help/"):
            p = "help/" + p
        full = REPO / p
        if not full.is_file() or full in visited:
            continue
        visited.add(full)
        try:
            sub = strip_frontmatter(full.read_text(encoding="utf-8", errors="replace"))
        except OSError:
            continue
        chunks.append(sub)
        chunks.append(collect_text_with_includes(sub, visited))
    return "\n".join(chunks)


def video_ids_in_text(text: str) -> list[str]:
    return EMBED_VIDEO_RE.findall(text)


def fetch_video_seconds(vid: str, cache: dict[str, int]) -> int:
    if vid in cache:
        return cache[vid]
    url = f"https://video.tv.adobe.com/v/{vid}"
    req = urllib.request.Request(url, headers={"User-Agent": "commerce-learn-duration-script/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=45) as resp:
            html = resp.read().decode("utf-8", errors="replace")
    except (urllib.error.URLError, OSError) as e:
        print(f"WARN: fetch failed for {vid}: {e}", file=sys.stderr)
        cache[vid] = 0
        return 0
    ms_vals = [int(x) for x in DURATION_MS_RE.findall(html)]
    ms_vals = [x for x in ms_vals if 1000 <= x <= 86400000 * 1000]
    sec = round(max(ms_vals) / 1000) if ms_vals else 0
    cache[vid] = sec
    time.sleep(0.03)
    return sec


def total_video_seconds_for_page(full_raw: str, cache: dict[str, int]) -> int:
    body = strip_frontmatter(full_raw)
    visited: set[Path] = set()
    combined = collect_text_with_includes(body, visited)
    ids = list(dict.fromkeys(video_ids_in_text(combined)))
    total = 0
    for vid in ids:
        total += fetch_video_seconds(vid, cache)
    return total


def reading_seconds(full_raw: str) -> int:
    body = strip_frontmatter(full_raw)
    visited: set[Path] = set()
    combined = collect_text_with_includes(body, visited)
    w = words_in_markdown(combined)
    return round(w / WPM * 60)


def update_frontmatter_duration(content: str, new_duration: int) -> str | None:
    if not content.startswith("---"):
        return None
    parts = content.split("---", 2)
    if len(parts) < 3:
        return None
    fm, body = parts[1], parts[2]
    if re.search(r"^duration:\s*\d+\s*$", fm, re.M):
        fm_new = re.sub(r"^duration:\s*\d+\s*$", f"duration: {new_duration}", fm, flags=re.M)
    elif re.search(r"^duration:\s", fm, re.M):
        fm_new = re.sub(r"^duration:\s*\S+.*$", f"duration: {new_duration}", fm, flags=re.M)
    else:
        if re.search(r"^doc-type:", fm, re.M):
            fm_new = re.sub(
                r"(^doc-type:.*\n)",
                r"\1duration: " + str(new_duration) + "\n",
                fm,
                count=1,
                flags=re.M,
            )
        else:
            fm_new = fm.rstrip() + "\nduration: " + str(new_duration) + "\n"
    return "---" + fm_new + "---" + body


def should_process_help(path: Path) -> bool:
    rel = path.relative_to(HELP)
    parts = rel.parts
    if path.name == "TOC.md":
        return False
    if parts and parts[0] == "_includes":
        return False
    return True


def iter_target_markdown() -> list[Path]:
    out: list[Path] = sorted(p for p in HELP.rglob("*.md") if should_process_help(p))
    skip_root = {"README.md", "metadata.md", "landing-page-template.md", "sample.md"}
    for p in sorted(REPO.glob("*.md")):
        if p.name in skip_root:
            continue
        out.append(p)
    return sorted(set(out), key=lambda x: str(x))


def main() -> int:
    cache_path = REPO / "scripts" / ".video_duration_cache.json"
    cache: dict[str, int] = {}
    if cache_path.is_file():
        cache = json.loads(cache_path.read_text(encoding="utf-8"))
        print(f"Loaded {len(cache)} cached video durations", file=sys.stderr)

    md_files = iter_target_markdown()
    updated = 0
    for path in md_files:
        raw = path.read_text(encoding="utf-8", errors="replace")
        if not raw.startswith("---"):
            continue
        vsec = total_video_seconds_for_page(raw, cache)
        rsec = reading_seconds(raw)
        total = max(0, vsec + rsec)
        if total == 0:
            continue
        new_content = update_frontmatter_duration(raw, total)
        if new_content is None or new_content == raw:
            continue
        path.write_text(new_content, encoding="utf-8")
        updated += 1
        print(f"{path.relative_to(REPO)} -> duration: {total} (video {vsec}s + read ~{rsec}s)")

    cache_path.write_text(json.dumps(cache, indent=0, sort_keys=True), encoding="utf-8")
    print(f"Updated {updated} files; video cache has {len(cache)} ids", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
