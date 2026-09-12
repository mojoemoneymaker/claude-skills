#!/usr/bin/env python3
"""Build the Perplexity package: the knowledge file as .txt, .pdf and .docx, and a
check that the Space instructions fit the 8,000 character cap.

Perplexity applies Space instructions every turn and only retrieves matching passages
from attached files, so the operating core lives in references/perplexity-instructions.md
and the toolkit travels as the knowledge file. The .md upload has failed for Joe, so the
knowledge file is emitted in three formats every source agrees Perplexity accepts.

    python3 influence-architect/scripts/build_perplexity.py [output-dir]
"""
import html
import re
import shutil
import subprocess
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MASTER = ROOT / "references" / "master-prompt.md"
INSTR = ROOT / "references" / "perplexity-instructions.md"
CAP = 8000
NAME = "Influence-Architect-Knowledge"

HEADER = """INFLUENCE ARCHITECT KNOWLEDGE

Knowledge file for the Influence Architect Space. The Space instructions govern every turn; this file carries the full operating core, the context and limits, and the toolkit: questions, the 14 reframe patterns, the frames, the objection protocol in Eli Wilde's words, the money moments, the metaphor library, delivery notes, domain rules, what defeats each technique, and the types. Generated from the influence-architect skill by scripts/build_perplexity.py.

"""

CHROME = [
    "/opt/pw-browsers/chromium_headless_shell-1194/chrome-linux/headless_shell",
    "/opt/pw-browsers/chromium-1194/chrome-linux/chrome",
]


def body_text() -> str:
    text = MASTER.read_text(encoding="utf-8")
    return text.split("\n---\n", 1)[1].lstrip()


def inline(s: str) -> str:
    s = html.escape(s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", s)
    s = re.sub(r"`(.+?)`", r"<code>\1</code>", s)
    return s


def md_to_html(md: str) -> str:
    out, para, lst = [], [], None

    def flush_para():
        if para:
            out.append("<p>" + inline(" ".join(para)) + "</p>")
            para.clear()

    def close_list():
        nonlocal lst
        if lst:
            out.append(f"</{lst}>")
            lst = None

    for line in md.split("\n"):
        m = re.match(r"^(#{1,4}) (.*)", line)
        if m:
            flush_para(); close_list()
            lvl = len(m.group(1))
            out.append(f"<h{lvl}>{inline(m.group(2))}</h{lvl}>")
            continue
        m = re.match(r"^- (.*)", line)
        if m:
            flush_para()
            if lst != "ul":
                close_list(); out.append("<ul>"); lst = "ul"
            out.append(f"<li>{inline(m.group(1))}</li>")
            continue
        m = re.match(r"^\d+\. (.*)", line)
        if m:
            flush_para()
            if lst != "ol":
                close_list(); out.append("<ol>"); lst = "ol"
            out.append(f"<li>{inline(m.group(1))}</li>")
            continue
        if line.strip() == "" or line.strip() == "---":
            flush_para(); close_list()
            continue
        if lst and line.startswith("   "):
            out[-1] = out[-1][:-5] + " " + inline(line.strip()) + "</li>"
            continue
        close_list()
        para.append(line.strip())
    flush_para(); close_list()
    css = ("body{font-family:Georgia,serif;font-size:11pt;line-height:1.45;max-width:7in;margin:0.6in auto}"
           "h1{font-size:18pt}h2{font-size:14pt;margin-top:1.4em}h3{font-size:12pt}code{font-family:monospace}")
    return f"<!doctype html><html><head><meta charset='utf-8'><title>{NAME}</title><style>{css}</style></head><body>{''.join(out)}</body></html>"


def md_to_plain(md: str) -> str:
    md = re.sub(r"\*\*(.+?)\*\*", r"\1", md)
    md = md.replace("`", "")
    return md


def write_docx(md: str, path: Path) -> None:
    def esc(s):
        return html.escape(s, quote=False)

    def p(text, bold=False, size=None):
        rpr = ""
        if bold or size:
            rpr = "<w:rPr>" + ("<w:b/>" if bold else "") + (f"<w:sz w:val=\"{size}\"/>" if size else "") + "</w:rPr>"
        return f"<w:p><w:r>{rpr}<w:t xml:space=\"preserve\">{esc(text)}</w:t></w:r></w:p>"

    paras = []
    for line in md_to_plain(md).split("\n"):
        m = re.match(r"^(#{1,4}) (.*)", line)
        if m:
            lvl = len(m.group(1))
            paras.append(p(m.group(2), bold=True, size={1: 32, 2: 28, 3: 24, 4: 22}[lvl]))
        elif line.strip() in ("", "---"):
            paras.append("<w:p/>")
        else:
            paras.append(p(line))
    document = ("<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?>"
                "<w:document xmlns:w=\"http://schemas.openxmlformats.org/wordprocessingml/2006/main\"><w:body>"
                + "".join(paras) + "</w:body></w:document>")
    content_types = ("<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?>"
                     "<Types xmlns=\"http://schemas.openxmlformats.org/package/2006/content-types\">"
                     "<Default Extension=\"rels\" ContentType=\"application/vnd.openxmlformats-package.relationships+xml\"/>"
                     "<Default Extension=\"xml\" ContentType=\"application/xml\"/>"
                     "<Override PartName=\"/word/document.xml\" ContentType=\"application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml\"/>"
                     "</Types>")
    rels = ("<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?>"
            "<Relationships xmlns=\"http://schemas.openxmlformats.org/package/2006/relationships\">"
            "<Relationship Id=\"rId1\" Type=\"http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument\" Target=\"word/document.xml\"/>"
            "</Relationships>")
    with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("[Content_Types].xml", content_types)
        z.writestr("_rels/.rels", rels)
        z.writestr("word/document.xml", document)


def main() -> int:
    out_dir = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "dist"
    out_dir.mkdir(parents=True, exist_ok=True)

    instr = INSTR.read_text(encoding="utf-8").split("\n---\n", 1)[1].strip()
    if len(instr) > CAP:
        print(f"Space instructions are {len(instr)} chars, cap is {CAP}", file=sys.stderr)
        return 1
    (out_dir / "Influence-Architect-Space-Instructions.txt").write_text(instr + "\n", encoding="utf-8")

    md = HEADER + body_text()
    for ch in ("–", "—"):
        if ch in md or ch in instr:
            print("dash found", file=sys.stderr)
            return 1

    (out_dir / f"{NAME}.txt").write_text(md_to_plain(md), encoding="utf-8")
    html_path = out_dir / f"{NAME}.html"
    html_path.write_text(md_to_html(md), encoding="utf-8")
    write_docx(md, out_dir / f"{NAME}.docx")

    chrome = next((c for c in CHROME if Path(c).exists()), shutil.which("chromium") or shutil.which("google-chrome"))
    if chrome:
        pdf = out_dir / f"{NAME}.pdf"
        subprocess.run([chrome, "--headless", "--no-sandbox", "--disable-gpu", "--no-pdf-header-footer",
                        f"--print-to-pdf={pdf}", html_path.as_uri()], check=True, capture_output=True, timeout=120)
    else:
        print("no chromium found, pdf skipped", file=sys.stderr)
    html_path.unlink()
    for f in sorted(out_dir.iterdir()):
        print(f"{f.name}\t{f.stat().st_size} bytes")
    print(f"instructions: {len(instr)} chars (cap {CAP})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
