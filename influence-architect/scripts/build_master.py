#!/usr/bin/env python3
"""Build references/master-prompt.md from SKILL.md and the reference files.

The master is the single paste-in block for any other AI. It is generated, never
edited by hand, so the rules keep one home. Run from anywhere:

    python3 influence-architect/scripts/build_master.py
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILL = ROOT / "SKILL.md"
TOOLKIT = ROOT / "references" / "toolkit.md"
CONTEXT = ROOT / "references" / "context-and-limits.md"
OUT = ROOT / "references" / "master-prompt.md"

HEADER = """# INFLUENCE ARCHITECT

Operating instructions for an AI built on Eli Wilde's NLP for Sales principles, generalized to any conversation that has to change what someone believes. Generated from the influence-architect skill by scripts/build_master.py; edit the skill, not this file. Paste everything below the rule into the system prompt, custom instructions or project instructions of the AI you are using.

---

"""


def strip_frontmatter(text: str) -> str:
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end != -1:
            text = text[end + 4:]
    return text.lstrip()


def drop_section(text: str, heading: str) -> str:
    """Remove a level-2 section (heading line through the line before the next ## or #)."""
    pattern = re.compile(rf"^## {re.escape(heading)}.*?(?=^## |^# |\Z)", re.S | re.M)
    return pattern.sub("", text)


def demote(text: str) -> str:
    """Push headings one level down so the master reads as one document."""
    return re.sub(r"^(#+) ", lambda m: "#" + m.group(1) + " ", text, flags=re.M)


def main() -> int:
    skill = strip_frontmatter(SKILL.read_text(encoding="utf-8"))
    skill = re.sub(r"^# influence-architect\n", "", skill)
    skill = drop_section(skill, "Reference map")
    skill = skill.replace("Run the context intake in `context-and-limits.md`", "Run the context intake in Part 2")
    skill = skill.replace("the type (see `context-and-limits.md`)", "the type (Part 2, section 4)")
    skill = skill.replace("Read `toolkit.md` before writing any line. Read `context-and-limits.md` before choosing which tools are allowed.\n\n", "")
    skill = skill.replace("Joe", "the user").replace("the user's", "the user's")

    toolkit = TOOLKIT.read_text(encoding="utf-8")
    toolkit = re.sub(r"^# Toolkit\n\n", "", toolkit)
    context = CONTEXT.read_text(encoding="utf-8")
    context = re.sub(r"^# Context and limits\n\n", "", context)
    context = context.replace("Joe", "the user")
    toolkit = toolkit.replace("Joe", "the user")

    body = (
        "# PART 1. THE OPERATING CORE\n\n" + demote(skill).strip() + "\n\n"
        "# PART 2. CONTEXT AND LIMITS\n\n" + demote(context).strip() + "\n\n"
        "# PART 3. THE TOOLKIT\n\n" + demote(toolkit).strip() + "\n"
    )
    out = HEADER + body
    for ch in ("\u2013", "\u2014"):
        if ch in out:
            print(f"dash found in generated master: {ch!r}", file=sys.stderr)
            return 1
    OUT.write_text(out, encoding="utf-8")
    print(f"wrote {OUT} ({len(out.split())} words)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
