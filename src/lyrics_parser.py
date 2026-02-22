"""
Parse Sanremo lyrics files into structured sections.

Handles three file types:
  A) Bracket headers  — [Strofa 1], [Ritornello], etc.
  B) Blank-line separated stanzas
  C) Wall-of-text with repeated blocks (chorus detection)
"""

import re
from pathlib import Path
from dataclasses import dataclass, field
from typing import List, Optional
from collections import Counter

_LABEL_NORMALIZE = {
    # Strofa
    "strofa": "Strofa",
    "verse": "Strofa",
    # Ritornello
    "ritornello": "Ritornello",
    "chorus": "Ritornello",
    "refrain": "Ritornello",
    "hook": "Ritornello",
    # Pre-Ritornello
    "pre-ritornello": "Pre-Ritornello",
    "pre-chorus": "Pre-Ritornello",
    # Post-Ritornello
    "post-ritornello": "Post-Ritornello",
    "post-chorus": "Post-Ritornello",
    # Bridge
    "bridge": "Bridge",
    "ponte": "Bridge",
    "inciso": "Bridge",
    # Intro / Outro
    "intro": "Intro",
    "outro": "Outro",
    "outri": "Outro",
    "coda": "Outro",
    "conclusione": "Outro",
    # Interludio
    "interludio": "Interludio",
    "intermezzo": "Interludio",
    # Strumentale
    "strumentale": "Strumentale",
    "assolo": "Strumentale",
    "assolo di chitarra": "Strumentale",
    "scratch": "Strumentale",
    "pausa strumentale": "Strumentale",
    # Drop to None (artist cues, ad-libs, etc.)
    "adlib": None,
    "skit": None,
    "funky nano": None,
    "mattak": None,
    "mattak, funky nano": None,
    "funky": None,
    "session": None,
}


_DROP_NUMBER = {"Ritornello", "Pre-Ritornello", "Post-Ritornello", "Bridge", "Interludio"}


def _normalize_label(label: str) -> str:
    if not label:
        return label
    full_lower = label.lower().strip()
    if full_lower in _LABEL_NORMALIZE:
        return _LABEL_NORMALIZE[full_lower]
    parts = label.rsplit(None, 1)
    base = parts[0]
    suffix = parts[1] if len(parts) > 1 and parts[1].isdigit() else ""
    base_lower = base.lower().strip()
    normalized = _LABEL_NORMALIZE.get(base_lower, base)
    if normalized is None:
        return None
    if normalized in _DROP_NUMBER:
        return normalized
    return f"{normalized} {suffix}".strip() if suffix else normalized


_TESTO_RE = re.compile(r'^\[Testo\s+d[ie]\s+["\u201c]?.*?["\u201d]?\s*\]\s*$', re.IGNORECASE)

_SECTION_HEADER_RE = re.compile(
    r'^\[('
    r'Strofa|Ritornello|Verse|Chorus|Bridge|Intro|Outro|'
    r'Pre-Ritornello|Pre-Chorus|Post-Ritornello|Post-Chorus|'
    r'Hook|Refrain|Interludio|Strumentale|Intermezzo|'
    r'Pausa Strumentale|Coda|Conclusione|Inciso|Ponte|'
    r'Session|Assolo|AdLib|Skit|Funky|Mattak|Scratch|Outri'
    r')',
    re.IGNORECASE | re.MULTILINE,
)

_BARE_LABEL_RE = re.compile(
    r'^(Verse|Chorus|Bridge|Intro|Outro|Hook|'
    r'RIT\.?|RITORNELLO|STROFA|CORO)\s*\d*\s*$',
    re.IGNORECASE,
)


@dataclass
class Section:
    label: Optional[str]
    lines: List[str]

    @property
    def text(self) -> str:
        return "\n".join(self.lines)

    @property
    def is_empty(self) -> bool:
        return not any(l.strip() for l in self.lines)


@dataclass
class ParsedSong:
    filename: str
    title: str
    year: Optional[int]
    sections: List[Section] = field(default_factory=list)
    parse_method: str = ""

    @property
    def full_text(self) -> str:
        return "\n\n".join(s.text for s in self.sections if not s.is_empty)

    @property
    def section_texts(self) -> List[str]:
        return [s.text for s in self.sections if not s.is_empty]


def _extract_metadata(filename: str):
    stem = Path(filename).stem
    parts = stem.rsplit("_", 1)
    if len(parts) == 2 and parts[1].isdigit():
        return parts[0].strip(), int(parts[1])
    return stem, None


_TRAILING_JUNK_RE = re.compile(
    r'^\s*\(?\s*(grazie\s+a\s+\w+\s+per|thanks\s+to|credits?|fonte|source|testo di|testo:|'
    r'inviato da|scritto da|traduzione|autore|autori|'
    r'parole e musica|parole di|musica di|music by|lyrics by)\b',
    re.IGNORECASE,
)


def _strip_testo_header(lines: List[str]) -> List[str]:
    """Remove [Testo di "..."] if it's the first non-blank line."""
    for i, l in enumerate(lines):
        if l.strip():
            if _TESTO_RE.match(l.strip()):
                return lines[i + 1:]
            break
    return lines


def _strip_trailing_junk(lines: List[str]) -> List[str]:
    """Remove trailing metadata lines like '(Grazie a ... per questo testo)'."""
    while lines:
        last = lines[-1].strip()
        if not last:
            lines = lines[:-1]
            continue
        if _TRAILING_JUNK_RE.match(last):
            lines = lines[:-1]
            continue
        break
    return lines


def _has_bracket_headers(text: str) -> bool:
    return bool(_SECTION_HEADER_RE.search(text))


def _has_bare_labels(text: str) -> bool:
    return bool(re.search(
        r'^(Verse|Chorus|Bridge|Intro|Outro|Hook)\s*\d*\s*$',
        text, re.MULTILINE | re.IGNORECASE,
    ))


def _parse_bracket_headers(lines: List[str]) -> List[Section]:
    """Split on [Header] lines. Each header starts a new section."""
    sections: List[Section] = []
    current_label = None
    current_lines: List[str] = []
    in_multiline_header = False

    for line in lines:
        stripped = line.strip()

        if in_multiline_header:
            if "]" in stripped:
                in_multiline_header = False
            continue

        if stripped.startswith("[") and _SECTION_HEADER_RE.match(stripped):
            if current_label is not None or current_lines:
                sections.append(Section(label=current_label, lines=current_lines))
            label_text = stripped.lstrip("[").split("]")[0] if "]" in stripped else stripped.lstrip("[")
            current_label = _normalize_label(re.sub(r'\s*:.*', '', label_text).strip())
            current_lines = []
            if "]" not in stripped:
                in_multiline_header = True
        elif stripped.startswith("[") and _TESTO_RE.match(stripped):
            continue
        else:
            current_lines.append(line.rstrip())

    if current_label is not None or current_lines:
        sections.append(Section(label=current_label, lines=current_lines))

    for s in sections:
        while s.lines and not s.lines[0].strip():
            s.lines.pop(0)
        while s.lines and not s.lines[-1].strip():
            s.lines.pop()

    sections = _subsplit_large_sections(sections)

    return sections


def _subsplit_large_sections(sections: List[Section]) -> List[Section]:
    """If a section has blank lines inside, split it into sub-sections.
    Only applies when there are very few bracket headers relative to content."""
    total_lyric_lines = sum(
        len([l for l in s.lines if l.strip()]) for s in sections
    )
    if not sections or total_lyric_lines < 10:
        return sections

    avg_lines = total_lyric_lines / len(sections)
    if avg_lines < 15:
        return sections

    result: List[Section] = []
    for s in sections:
        blank_count = sum(1 for l in s.lines if not l.strip())
        if blank_count >= 2:
            subs = _parse_blank_lines(s.lines)
            subs[0] = Section(label=s.label, lines=subs[0].lines)
            result.extend(subs)
        else:
            result.append(s)
    return result


def _parse_blank_lines(lines: List[str]) -> List[Section]:
    """Split on blank lines."""
    sections: List[Section] = []
    current: List[str] = []

    for line in lines:
        if not line.strip():
            if current:
                sections.append(Section(label=None, lines=current))
                current = []
        else:
            current.append(line.rstrip())

    if current:
        sections.append(Section(label=None, lines=current))

    return sections


def _parse_bare_labels(lines: List[str]) -> List[Section]:
    """Split on bare Verse/Chorus/Bridge labels."""
    sections: List[Section] = []
    current_label = None
    current_lines: List[str] = []

    for line in lines:
        stripped = line.strip()
        if _BARE_LABEL_RE.match(stripped):
            if current_label is not None or current_lines:
                sections.append(Section(label=current_label, lines=current_lines))
            current_label = _normalize_label(stripped)
            current_lines = []
        else:
            current_lines.append(line.rstrip())

    if current_label is not None or current_lines:
        sections.append(Section(label=current_label, lines=current_lines))

    for s in sections:
        while s.lines and not s.lines[0].strip():
            s.lines.pop(0)
        while s.lines and not s.lines[-1].strip():
            s.lines.pop()

    return sections


def _find_chorus_block(lines: List[str], min_block: int = 2, max_block: int = 8):
    """Find the longest repeated consecutive block of lines (likely chorus)."""
    clean = [l.strip().lower() for l in lines]
    best_block = None
    best_positions = []

    for size in range(max_block, min_block - 1, -1):
        blocks: dict = {}
        for i in range(len(clean) - size + 1):
            key = tuple(clean[i:i + size])
            if key not in blocks:
                blocks[key] = []
            blocks[key].append(i)

        for block, positions in blocks.items():
            if len(positions) > 1 and all(b.strip() for b in block):
                if best_block is None or size > len(best_block):
                    best_block = block
                    best_positions = positions
                    break
        if best_block:
            break

    return best_block, best_positions


def _parse_wall_of_text(lines: List[str]) -> List[Section]:
    """Use repeated-block detection to split wall-of-text into sections."""
    clean_lines = [l for l in lines if l.strip()]
    if not clean_lines:
        return [Section(label=None, lines=lines)]

    chorus_block, positions = _find_chorus_block(clean_lines)

    if not chorus_block:
        return [Section(label=None, lines=clean_lines)]

    block_size = len(chorus_block)
    sections: List[Section] = []
    used = set()

    for pos in positions:
        for i in range(pos, pos + block_size):
            used.add(i)

    current_verse: List[str] = []
    verse_num = 0
    chorus_num = 0

    for i, line in enumerate(clean_lines):
        if i in used:
            if i in positions:
                if current_verse:
                    verse_num += 1
                    sections.append(Section(
                        label=f"Strofa {verse_num}" if verse_num > 0 else None,
                        lines=current_verse,
                    ))
                    current_verse = []
                chorus_num += 1
                sections.append(Section(
                    label="Ritornello",
                    lines=[clean_lines[j] for j in range(i, i + block_size)],
                ))
        else:
            current_verse.append(line)

    if current_verse:
        verse_num += 1
        sections.append(Section(
            label=f"Strofa {verse_num}" if verse_num > 0 else None,
            lines=current_verse,
        ))

    return sections if sections else [Section(label=None, lines=clean_lines)]


def parse_lyrics(text: str, filename: str = "") -> ParsedSong:
    title, year = _extract_metadata(filename)
    lines = text.split("\n")

    lines = _strip_testo_header(lines)
    lines = _strip_trailing_junk(lines)

    raw = "\n".join(lines)

    if _has_bracket_headers(raw):
        sections = _parse_bracket_headers(lines)
        method = "bracket_headers"
    elif _has_bare_labels(raw):
        sections = _parse_bare_labels(lines)
        method = "bare_labels"
    else:
        blank_count = sum(1 for l in lines if l.strip() == "")
        if blank_count >= 2:
            sections = _parse_blank_lines(lines)
            method = "blank_lines"
        else:
            sections = _parse_wall_of_text(lines)
            method = "repeated_blocks"

    sections = [s for s in sections if not s.is_empty]

    return ParsedSong(
        filename=filename,
        title=title,
        year=year,
        sections=sections,
        parse_method=method,
    )


def parse_file(path) -> ParsedSong:
    p = Path(path)
    text = p.read_text(encoding="utf-8")
    return parse_lyrics(text, filename=p.name)


def load_corpus(testi_dir="testi"):
    """Load and parse all lyrics files. Returns list of ParsedSong."""
    testi = Path(testi_dir)
    songs = []
    for f in sorted(testi.glob("*.txt")):
        songs.append(parse_file(f))
    return songs


def corpus_stats(songs: List[ParsedSong]) -> dict:
    """Summary statistics for a parsed corpus."""
    methods = Counter(s.parse_method for s in songs)
    section_counts = [len(s.sections) for s in songs]
    total_sections = sum(section_counts)
    labeled = sum(1 for s in songs for sec in s.sections if sec.label)

    return {
        "total_songs": len(songs),
        "parse_methods": dict(methods),
        "total_sections": total_sections,
        "avg_sections_per_song": total_sections / len(songs) if songs else 0,
        "labeled_sections": labeled,
        "unlabeled_sections": total_sections - labeled,
    }
