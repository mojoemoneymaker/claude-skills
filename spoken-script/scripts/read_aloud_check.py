#!/usr/bin/env python3
"""Deterministic read-aloud checker for spoken scripts.

Usage:
    python read_aloud_check.py FILE [FILE ...] [--max-words N] [--spoken-only]

What it flags (FAIL stops the script from shipping, WARN needs a human read):
    FAIL  em dash or en dash anywhere (Joe's law, joe-copy-standards rule 1)
    FAIL  banned words (joe-copy-standards rule 2)
    FAIL  a sentence over the hard ceiling (30 words, cannot be said in one breath)
    FAIL  eye-only punctuation inside spoken text: parentheses, brackets, semicolons,
          slashes, markdown bold or headings
    WARN  a sentence over --max-words (default 22)
    WARN  a sentence stacked with more than three commas
    WARN  softer AI-tell words the WDJM standards ban (Incredible, Unlock your potential)
    WARN  numerals with symbols or ranges the mouth might read two ways (%, /, x, ranges)
    WARN  addressing a crowd ("you all", "you guys", "everyone", "everybody")

If a file contains fenced blocks tagged ```spoken, the eye-only punctuation, sentence and
crowd checks run only inside those blocks (delivery notes may use whatever they like).
The dash and banned-word checks always run on the whole file, because a delivery note
with an em dash still trains the model that em dashes are fine. Use --spoken-only to
treat the entire file as spoken text when there are no fences.

Exit code 1 on any FAIL, 0 otherwise.
"""
import argparse
import re
import sys

BANNED_HARD = [
    "elevate", "transform", "game-changer", "game changer", "next level", "skyrocket",
    "crushing it",
]
BANNED_SOFT = ["incredible", "unlock your potential"]
CROWD = ["you all", "you guys", "everyone", "everybody", "y'all", "ladies and gentlemen"]
HARD_CEILING = 30

SENTENCE_SPLIT = re.compile(r"(?<=[.!?])\s+")


def spoken_blocks(text):
    """Return list of (start_line, block_text) for ```spoken fences; empty if none."""
    blocks = []
    lines = text.split("\n")
    inside = False
    start = 0
    buf = []
    for i, line in enumerate(lines, 1):
        if not inside and line.strip().startswith("```spoken"):
            inside, start, buf = True, i + 1, []
            continue
        if inside and line.strip().startswith("```"):
            blocks.append((start, "\n".join(buf)))
            inside = False
            continue
        if inside:
            buf.append(line)
    return blocks


def check_whole(text, findings):
    for i, line in enumerate(text.split("\n"), 1):
        if "—" in line or "–" in line:
            findings.append(("FAIL", i, "em or en dash", line.strip()))
        low = line.lower()
        for w in BANNED_HARD:
            if re.search(r"\b" + re.escape(w) + r"\b", low):
                findings.append(("FAIL", i, f"banned word: {w}", line.strip()))
        for w in BANNED_SOFT:
            if re.search(r"\b" + re.escape(w) + r"\b", low):
                findings.append(("WARN", i, f"AI-tell word: {w}", line.strip()))


def check_spoken(text, offset, max_words, findings):
    lines = text.split("\n")
    for i, line in enumerate(lines):
        n = offset + i
        s = line.strip()
        if not s:
            continue
        if re.search(r"[()\[\];/]", s):
            findings.append(("FAIL", n, "eye-only punctuation ( ) [ ] ; /", s))
        if re.match(r"^\s*(#+\s|[-*]\s|\d+\.\s)", line) or "**" in s:
            findings.append(("FAIL", n, "markdown inside spoken text", s))
        low = s.lower()
        for c in CROWD:
            if re.search(r"\b" + re.escape(c) + r"\b", low):
                findings.append(("WARN", n, f"speaks to a crowd: '{c}', speak to one person", s))
        if re.search(r"\d+\s*[%x/]|\d+\s*(to|-)\s*\d+", low):
            findings.append(("WARN", n, "numeral the mouth might read two ways, write it as said", s))
    # sentence checks across the block
    flat = " ".join(l.strip() for l in lines if l.strip())
    for sent in SENTENCE_SPLIT.split(flat):
        words = sent.split()
        if not words:
            continue
        if len(words) > HARD_CEILING:
            findings.append(("FAIL", offset, f"sentence of {len(words)} words, over the {HARD_CEILING} word ceiling", sent))
        elif len(words) > max_words:
            findings.append(("WARN", offset, f"sentence of {len(words)} words, over {max_words}, one breath?", sent))
        if sent.count(",") > 3:
            findings.append(("WARN", offset, "more than three commas, stacked clauses", sent))


def run(path, max_words, spoken_only):
    text = open(path, encoding="utf-8").read()
    findings = []
    check_whole(text, findings)
    blocks = spoken_blocks(text)
    if blocks:
        for start, block in blocks:
            check_spoken(block, start, max_words, findings)
    elif spoken_only:
        check_spoken(text, 1, max_words, findings)
    return findings


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("files", nargs="+")
    ap.add_argument("--max-words", type=int, default=22)
    ap.add_argument("--spoken-only", action="store_true",
                    help="treat the whole file as spoken text when it has no ```spoken fences")
    args = ap.parse_args()
    failed = False
    for path in args.files:
        findings = run(path, args.max_words, args.spoken_only)
        fails = [f for f in findings if f[0] == "FAIL"]
        warns = [f for f in findings if f[0] == "WARN"]
        print(f"== {path}: {len(fails)} FAIL, {len(warns)} WARN")
        for level, line, why, snippet in findings:
            snippet = snippet if len(snippet) <= 110 else snippet[:107] + "..."
            print(f"  {level} L{line}: {why}\n        {snippet}")
        if fails:
            failed = True
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
