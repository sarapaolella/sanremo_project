#!/usr/bin/env python3
"""
Fetch lyrics from Genius for all songs in lista_canzoni_sanremo.csv.
Uses the Genius API for search + fetches the song page for lyrics.
Keeps section headers ([Verse], [Chorus], [Bridge], etc.) intact.
Saves to testi/<song_safe>_<year>.txt.
"""
import argparse
import os
import re
import time
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

import pandas as pd
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()

OUT_DIR = Path(__file__).resolve().parent / "testi"
CSV_PATH = Path(__file__).resolve().parent / "lista_canzoni_sanremo.csv"
API_BASE = "https://api.genius.com"


def safe_filename(song: str, year: int) -> str:
    s = str(song).strip()
    for c in r'\/:*?"<>|':
        s = s.replace(c, "_")
    s = re.sub(r"\s+", " ", s).strip()
    return f"{s or 'unknown'}_{year}.txt"


def clean_lyrics(raw: str) -> str:
    """Strip Genius first-line header but keep all section labels and lyrics."""
    text = raw.strip()
    if not text:
        return text
    first_line = text.split("\n")[0]
    if re.search(r"^\d*\s*Contributor", first_line, re.IGNORECASE) or first_line.rstrip().endswith("Lyrics"):
        text = "\n".join(text.split("\n")[1:]).strip()
    # Remove trailing "You might also like" or "Embed" artifacts
    text = re.sub(r"You might also like.*$", "", text, flags=re.DOTALL).strip()
    text = re.sub(r"\d*Embed$", "", text).strip()
    return text


def search_song_url(token, title, artist, max_retries=3):
    """Use the official Genius API to search for a song; return its genius URL."""
    headers = {"Authorization": f"Bearer {token}"}
    params = {"q": f"{title} {artist}"}
    for attempt in range(max_retries):
        try:
            r = requests.get(f"{API_BASE}/search", headers=headers, params=params, timeout=10)
            if r.status_code == 429:
                wait = min(2 ** attempt * 5, 60)
                time.sleep(wait)
                continue
            r.raise_for_status()
            data = r.json()
            break
        except Exception:
            if attempt < max_retries - 1:
                time.sleep(2)
                continue
            return None
    else:
        return None
    hits = data.get("response", {}).get("hits", [])
    if not hits:
        return None
    title_clean = re.sub(r"[^\w\s]", "", title.lower())
    artist_clean = re.sub(r"[^\w\s]", "", artist.lower())
    for hit in hits:
        result = hit.get("result", {})
        hit_title = re.sub(r"[^\w\s]", "", result.get("title", "").lower())
        hit_artist = re.sub(r"[^\w\s]", "", result.get("primary_artist", {}).get("name", "").lower())
        if title_clean in hit_title or hit_title in title_clean:
            return result.get("url")
        if hit_artist and (artist_clean in hit_artist or hit_artist in artist_clean):
            if len(set(title_clean.split()) & set(hit_title.split())) >= 1:
                return result.get("url")
    return None


def fetch_lyrics_from_page(url):
    """Fetch the Genius song page and extract lyrics with section headers."""
    try:
        r = requests.get(url, timeout=15)
        r.raise_for_status()
    except Exception:
        return None
    soup = BeautifulSoup(r.text.replace("<br/>", "\n"), "html.parser")
    divs = soup.find_all("div", class_=re.compile(r"Lyrics__Container|Lyrics-sc"))
    if not divs:
        return None
    lyrics = "\n".join(div.get_text(separator="\n") for div in divs)
    return lyrics.strip() or None


def process_song(token, year, artist, song, force):
    """Process a single song: search + fetch lyrics. Returns (year, artist, song, status, path)."""
    fname = safe_filename(song, year)
    out_path = OUT_DIR / fname
    if out_path.exists() and not force:
        return (year, artist, song, "skipped", str(out_path))
    url = search_song_url(token, song, artist)
    if not url:
        return (year, artist, song, "not_found", "")
    raw = fetch_lyrics_from_page(url)
    if not raw:
        return (year, artist, song, "no_lyrics_on_page", url)
    text = clean_lyrics(raw)
    if len(text) < 20:
        return (year, artist, song, "too_short", url)
    out_path.write_text(text, encoding="utf-8")
    return (year, artist, song, "ok", str(out_path))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--force", action="store_true")
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument("--workers", type=int, default=2, help="Parallel workers (default 2)")
    parser.add_argument("--delay", type=float, default=1.0, help="Delay in seconds between batches (default 1.0)")
    args = parser.parse_args()

    token = os.environ.get("GENIUS_ACCESS_TOKEN")
    if not token:
        print("Set GENIUS_ACCESS_TOKEN in .env or environment.")
        raise SystemExit(1)

    OUT_DIR.mkdir(exist_ok=True)
    df = pd.read_csv(CSV_PATH)
    df["song"] = df["song"].astype(str).str.strip()

    tasks = []
    for _, row in df.iterrows():
        song = row["song"]
        if song == "nan" or not song:
            continue
        tasks.append((int(row["year"]), str(row["artist"]).strip(), song))
    if args.limit:
        tasks = tasks[:args.limit]

    total = len(tasks)
    done = 0
    skipped = 0
    failed = []

    delay = getattr(args, 'delay', 1.0)
    print(f"Processing {total} songs with {args.workers} workers, {delay}s delay...")
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        futures = {}
        for idx, (y, a, s) in enumerate(tasks):
            futures[pool.submit(process_song, token, y, a, s, args.force)] = (y, a, s)
            if idx % args.workers == 0 and idx > 0:
                time.sleep(delay)
        for i, future in enumerate(as_completed(futures), 1):
            year, artist, song, status, info = future.result()
            if status == "ok":
                done += 1
            elif status == "skipped":
                skipped += 1
            else:
                failed.append((year, artist, song, status))
            if i % 25 == 0 or i == total:
                sys.stdout.write(f"\r  [{i}/{total}] written={done} skipped={skipped} failed={len(failed)}")
                sys.stdout.flush()

    print(f"\nDone. Written: {done}, Skipped: {skipped}, Failed: {len(failed)}")
    if failed:
        log_path = Path(__file__).resolve().parent / "scrape_failed.txt"
        with open(log_path, "w", encoding="utf-8") as f:
            for y, a, s, reason in failed:
                f.write(f"{y}\t{a}\t{s}\t{reason}\n")
        print(f"Failed log: {log_path}")


if __name__ == "__main__":
    main()
