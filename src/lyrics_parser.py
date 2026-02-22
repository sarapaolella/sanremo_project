"""
Parse Sanremo lyrics files into structured sections.

Handles three file types:
  A) Bracket headers  — [Strofa 1], [Ritornello], etc.
  B) Blank-line separated stanzas
  C) Wall-of-text with repeated blocks (chorus detection)
"""

import json
import re
from pathlib import Path
from dataclasses import dataclass, field
from typing import List, Optional, Dict
from collections import Counter

# Lazy-loaded AI structure overrides
_AI_STRUCTURES: Optional[Dict[str, list]] = None


def _load_ai_structures() -> Dict[str, list]:
    """Load AI-generated structure overrides from ai_structures.json."""
    global _AI_STRUCTURES
    if _AI_STRUCTURES is not None:
        return _AI_STRUCTURES
    _AI_STRUCTURES = {}
    json_path = Path(__file__).parent.parent / "ai_structures.json"
    if json_path.exists():
        with open(json_path, encoding="utf-8") as f:
            data = json.load(f)
        for entry in data:
            fname = entry.get("file", "")
            structure = entry.get("structure", [])
            if fname and structure:
                _AI_STRUCTURES[fname] = structure
    return _AI_STRUCTURES

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


def _find_all_repeated_blocks(lines: List[str], min_block: int = 2, max_block: int = 8):
    """Find all non-overlapping repeated blocks, longest first."""
    clean = [l.strip().lower() for l in lines]
    found = []  # list of (block_tuple, positions, size)
    used = set()

    for size in range(max_block, min_block - 1, -1):
        blocks: dict = {}
        for i in range(len(clean) - size + 1):
            if any(j in used for j in range(i, i + size)):
                continue
            key = tuple(clean[i:i + size])
            if all(k.strip() for k in key):
                blocks.setdefault(key, []).append(i)

        for block, positions in blocks.items():
            valid = [p for p in positions
                     if not any(j in used for j in range(p, p + size))]
            if len(valid) >= 2:
                found.append((block, valid, size))
                for p in valid:
                    for j in range(p, p + size):
                        used.add(j)

    return found


def _parse_wall_of_text(lines: List[str]) -> List[Section]:
    """Use repeated-block detection to split wall-of-text into sections.

    Finds multiple repeated blocks to detect Ritornello, Pre-Ritornello,
    and Bridge patterns. Falls back to simple chorus detection when only
    one repeated block exists.
    """
    clean_lines = [l for l in lines if l.strip()]
    if not clean_lines:
        return [Section(label=None, lines=lines)]

    all_blocks = _find_all_repeated_blocks(clean_lines)
    if not all_blocks:
        return [Section(label=None, lines=clean_lines)]

    # Longest repeated block → Ritornello
    chorus_block, chorus_positions, chorus_size = all_blocks[0]

    # Build a map: line index → (label, block_start)
    line_labels = {}  # idx → (label, block_start_idx)
    chorus_starts = set(chorus_positions)
    for pos in chorus_positions:
        for j in range(pos, pos + chorus_size):
            line_labels[j] = ("Ritornello", pos)

    # Secondary blocks: label based on position relative to chorus
    for block, positions, size in all_blocks[1:]:
        # Check if this block consistently appears right before a chorus
        before_chorus = 0
        between_choruses = 0
        for pos in positions:
            block_end = pos + size
            # Is there a chorus starting right after (within 0-1 lines)?
            near_chorus = any(
                cp >= block_end and cp <= block_end + 1
                for cp in chorus_positions
            )
            if near_chorus:
                before_chorus += 1
            # Is it between two chorus instances?
            has_chorus_before = any(cp + chorus_size <= pos for cp in chorus_positions)
            has_chorus_after = any(cp >= pos + size for cp in chorus_positions)
            if has_chorus_before and has_chorus_after:
                between_choruses += 1

        if before_chorus >= 2:
            label = "Pre-Ritornello"
        elif between_choruses >= 1 and len(positions) <= 2:
            label = "Bridge"
        else:
            label = None  # can't determine, will become Strofa

        if label:
            for pos in positions:
                for j in range(pos, pos + size):
                    line_labels[j] = (label, pos)

    # Build sections by walking through lines
    sections: List[Section] = []
    current_lines: List[str] = []
    current_label = "_verse"  # sentinel for unlabeled
    verse_num = 0

    for i, line in enumerate(clean_lines):
        if i in line_labels:
            label, block_start = line_labels[i]
            if i == block_start:
                # Starting a new labeled block — flush current verse
                if current_lines:
                    verse_num += 1
                    sections.append(Section(
                        label=f"Strofa {verse_num}",
                        lines=current_lines,
                    ))
                    current_lines = []
            # If this is the start of a labeled block, create section
            if i == block_start:
                block_size = sum(1 for j in range(i, len(clean_lines))
                                 if j in line_labels and line_labels[j][1] == block_start)
                sections.append(Section(
                    label=label,
                    lines=clean_lines[i:i + block_size],
                ))
        else:
            current_lines.append(line)

    # Flush remaining lines
    if current_lines:
        verse_num += 1
        sections.append(Section(
            label=f"Strofa {verse_num}",
            lines=current_lines,
        ))

    # --- Post-processing refinements ---

    # Outro detection: trailing section after last Ritornello that is
    # significantly shorter than the average Strofa (not just ≤3 lines)
    if len(sections) >= 2:
        last = sections[-1]
        second_last = sections[-2]
        if (last.label and last.label.startswith("Strofa")
                and second_last.label == "Ritornello"):
            last_len = len([l for l in last.lines if l.strip()])
            strofa_lens = [len([l for l in s.lines if l.strip()])
                           for s in sections if s.label and s.label.startswith("Strofa")
                           and s is not last]
            avg_strofa = (sum(strofa_lens) / len(strofa_lens)) if strofa_lens else 99
            if last_len <= max(4, avg_strofa * 0.5):
                sections[-1] = Section(label="Outro", lines=last.lines)

    # Chorus-first detection: if the first section is very short (≤2 lines)
    # and labeled Strofa, and the Ritornello comes right after, the "Strofa 1"
    # is likely just a junk/title line — remove it.
    if (len(sections) >= 2
            and sections[0].label and sections[0].label.startswith("Strofa")
            and sections[1].label == "Ritornello"
            and len([l for l in sections[0].lines if l.strip()]) <= 2):
        sections.pop(0)

    return sections if sections else [Section(label=None, lines=clean_lines)]


def _apply_ai_structure(lines: List[str], labels: List[str]) -> List[Section]:
    """Apply AI-generated section labels to lyrics lines.

    Splits lines into stanzas by blank lines, then assigns labels in order.
    If blank-line stanzas match label count, use those splits.
    Otherwise, distribute content lines evenly across labels.
    """
    if not labels:
        return [Section(label=None, lines=lines)]

    content_lines = [l for l in lines if l.strip()]

    # Try blank-line splitting first
    stanzas: List[List[str]] = []
    current: List[str] = []
    for line in lines:
        if line.strip() == "":
            if current:
                stanzas.append(current)
                current = []
        else:
            current.append(line)
    if current:
        stanzas.append(current)

    if len(stanzas) >= len(labels):
        # Enough stanzas: assign labels in order
        sections = []
        for i, stanza in enumerate(stanzas):
            label = labels[i] if i < len(labels) else labels[-1]
            sections.append(Section(label=label, lines=stanza))
        return sections

    # Not enough blank-line stanzas: distribute content lines evenly
    n_labels = len(labels)
    n_lines = len(content_lines)
    chunk_size = max(1, n_lines // n_labels)
    sections = []
    for i, label in enumerate(labels):
        start = i * chunk_size
        end = start + chunk_size if i < n_labels - 1 else n_lines
        chunk = content_lines[start:end] if start < n_lines else [""]
        sections.append(Section(label=label, lines=chunk))
    return sections


def parse_lyrics(text: str, filename: str = "") -> ParsedSong:
    title, year = _extract_metadata(filename)
    lines = text.split("\n")

    lines = _strip_testo_header(lines)
    lines = _strip_trailing_junk(lines)

    raw = "\n".join(lines)

    # Check for AI-generated structure override
    ai_structs = _load_ai_structures()
    if filename in ai_structs:
        ai_labels = ai_structs[filename]
        sections = _apply_ai_structure(lines, ai_labels)
        method = "ai_override"
    elif _has_bracket_headers(raw):
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

    # Strip leading/trailing None-labeled sections (Genius "Title Lyrics" junk)
    while sections and sections[0].label is None:
        sections.pop(0)
    while sections and sections[-1].label is None:
        sections.pop()

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
