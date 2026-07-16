#!/usr/bin/env python3
"""docx_tool.py — portable, stdlib-only .docx helper for contract-review skills.

Works in any agent environment (Claude Code, Codex, OpenCode) — no pip installs.

Subcommands:
  extract  <input.docx>                              Print paragraph text (one per line).
  create   <input.md|txt> <output.docx>              Build a .docx from markdown-ish text.
  annotate <input.docx> <findings.json> <output.docx>
                                                     Inject Word comments anchored to clause
                                                     text; optionally prepend an executive
                                                     summary page.

findings.json format:
{
  "author":   "Legal Risk Skill",          // optional, default "Review"
  "initials": "LR",                        // optional
  "summary":  "summary.md",                // optional path to markdown prepended as page 1
  "findings": [
    {"anchor": "verbatim text appearing in the document",
     "comment": "Comment text.\n\nMay contain multiple paragraphs."}
  ]
}

Notes:
- Anchors are matched against whitespace-normalized paragraph text; the comment wraps the
  whole paragraph containing the anchor (robust across run splits).
- Comment text is escaped automatically — pass plain text in JSON, no XML entities needed.
- Markdown supported in `create`/summary: #..#### headings, "- " bullets, **bold**,
  blank-line paragraph separation, "<!--pagebreak-->" for a manual page break.
- Unmatched anchors are reported on stderr; exit code 2 if any anchor failed.
"""
import json
import os
import re
import shutil
import sys
import tempfile
import zipfile
from datetime import datetime, timezone
from xml.sax.saxutils import escape

W_NS = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
R_NS = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"

# ---------------------------------------------------------------- helpers

def norm(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip()


def die(msg: str, code: int = 1):
    sys.stderr.write(f"docx_tool: {msg}\n")
    sys.exit(code)


# ---------------------------------------------------------------- extract

PARA_RE = re.compile(r"<w:p[ >].*?</w:p>|<w:p/>", re.S)
TEXT_RE = re.compile(r"<w:t(?: [^>]*)?>(.*?)</w:t>", re.S)


def para_text(p_xml: str) -> str:
    parts = TEXT_RE.findall(p_xml)
    txt = "".join(parts)
    txt = txt.replace("&amp;", "&").replace("&lt;", "<").replace("&gt;", ">")
    txt = txt.replace("&quot;", '"').replace("&apos;", "'")
    return txt


def cmd_extract(docx_path: str):
    with zipfile.ZipFile(docx_path) as z:
        xml = z.read("word/document.xml").decode("utf-8")
    for p in PARA_RE.findall(xml):
        t = para_text(p)
        if t.strip():
            print(t)


# ---------------------------------------------------------------- markdown -> WordprocessingML

def _runs_from_inline(text: str, base_props: str = "") -> str:
    """Convert **bold** spans into runs; escape everything."""
    out = []
    for i, seg in enumerate(re.split(r"\*\*(.+?)\*\*", text)):
        if seg == "":
            continue
        bold = i % 2 == 1
        props = base_props + ("<w:b/>" if bold else "")
        rpr = f"<w:rPr>{props}</w:rPr>" if props else ""
        out.append(f'<w:r>{rpr}<w:t xml:space="preserve">{escape(seg)}</w:t></w:r>')
    return "".join(out) or '<w:r><w:t xml:space="preserve"></w:t></w:r>'


def md_to_paragraphs(md: str) -> list:
    """Return list of <w:p>...</w:p> strings from markdown-ish text."""
    paras = []
    heading_sizes = {1: 32, 2: 28, 3: 26, 4: 24}  # half-points
    for raw_line in md.splitlines():
        line = raw_line.rstrip()
        if line.strip() == "<!--pagebreak-->":
            paras.append('<w:p><w:r><w:br w:type="page"/></w:r></w:p>')
            continue
        if not line.strip():
            paras.append("<w:p/>")
            continue
        m = re.match(r"^(#{1,4})\s+(.*)$", line)
        if m:
            lvl = len(m.group(1))
            sz = heading_sizes[lvl]
            base = f'<w:b/><w:sz w:val="{sz}"/><w:szCs w:val="{sz}"/>'
            runs = _runs_from_inline(m.group(2), base)
            paras.append(f"<w:p><w:pPr><w:spacing w:before=\"240\" w:after=\"120\"/></w:pPr>{runs}</w:p>")
            continue
        m = re.match(r"^\s*[-*]\s+(.*)$", line)
        if m:
            runs = _runs_from_inline("• " + m.group(1))
            paras.append(f'<w:p><w:pPr><w:ind w:left="360"/></w:pPr>{runs}</w:p>')
            continue
        paras.append(f"<w:p>{_runs_from_inline(line)}</w:p>")
    return paras


# ---------------------------------------------------------------- create

CONTENT_TYPES = (
    '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
    '<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">'
    '<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>'
    '<Default Extension="xml" ContentType="application/xml"/>'
    '<Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>'
    "</Types>"
)
ROOT_RELS = (
    '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
    '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
    '<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/>'
    "</Relationships>"
)
DOC_RELS_EMPTY = (
    '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
    '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"/>'
)


def cmd_create(src_path: str, out_path: str):
    with open(src_path, encoding="utf-8") as f:
        md = f.read()
    body = "".join(md_to_paragraphs(md))
    doc = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        f'<w:document xmlns:w="{W_NS}" xmlns:r="{R_NS}">'
        f"<w:body>{body}"
        '<w:sectPr><w:pgSz w:w="11906" w:h="16838"/>'
        '<w:pgMar w:top="1417" w:right="1417" w:bottom="1417" w:left="1417"/></w:sectPr>'
        "</w:body></w:document>"
    )
    with zipfile.ZipFile(out_path, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("[Content_Types].xml", CONTENT_TYPES)
        z.writestr("_rels/.rels", ROOT_RELS)
        z.writestr("word/_rels/document.xml.rels", DOC_RELS_EMPTY)
        z.writestr("word/document.xml", doc)
    print(f"Created {out_path}")


# ---------------------------------------------------------------- annotate

def _comment_xml(cid: int, author: str, initials: str, date: str, text: str) -> str:
    paras = []
    for line in text.split("\n"):
        paras.append(
            f'<w:p><w:r><w:t xml:space="preserve">{escape(line)}</w:t></w:r></w:p>'
            if line.strip()
            else "<w:p/>"
        )
    return (
        f'<w:comment w:id="{cid}" w:author="{escape(author)}" '
        f'w:date="{date}" w:initials="{escape(initials)}">'
        + "".join(paras)
        + "</w:comment>"
    )


def _wrap_paragraph_with_comment(p_xml: str, cid: int) -> str:
    """Insert commentRangeStart after <w:pPr> (or at start) and RangeEnd+reference at end."""
    start = f'<w:commentRangeStart w:id="{cid}"/>'
    end = (
        f'<w:commentRangeEnd w:id="{cid}"/>'
        f'<w:r><w:rPr><w:rStyle w:val="CommentReference"/></w:rPr>'
        f'<w:commentReference w:id="{cid}"/></w:r>'
    )
    if p_xml.endswith("/>"):  # empty paragraph — shouldn't happen for matched anchors
        return p_xml
    m = re.search(r"<w:pPr[ >].*?</w:pPr>|<w:pPr/>", p_xml, re.S)
    if m:
        insert_at = m.end()
    else:
        insert_at = p_xml.index(">") + 1
    body_end = p_xml.rindex("</w:p>")
    return p_xml[:insert_at] + start + p_xml[insert_at:body_end] + end + p_xml[body_end:]


def cmd_annotate(docx_path: str, findings_path: str, out_path: str):
    with open(findings_path, encoding="utf-8") as f:
        spec = json.load(f)
    author = spec.get("author", "Review")
    initials = spec.get("initials", "".join(w[0] for w in author.split()[:2]).upper() or "R")
    findings = spec.get("findings", [])
    date = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    tmpdir = tempfile.mkdtemp(prefix="docx_tool_")
    try:
        with zipfile.ZipFile(docx_path) as z:
            names = z.namelist()
            z.extractall(tmpdir)

        doc_path = os.path.join(tmpdir, "word", "document.xml")
        with open(doc_path, encoding="utf-8") as f:
            doc = f.read()

        # existing comment ids (if the doc already has comments)
        comments_path = os.path.join(tmpdir, "word", "comments.xml")
        existing_comments = ""
        next_id = 1000  # avoid clashing with any existing ids
        if os.path.exists(comments_path):
            with open(comments_path, encoding="utf-8") as f:
                existing = f.read()
            m = re.search(r"(<w:comments[^>]*>)(.*)(</w:comments>)", existing, re.S)
            if m:
                existing_comments = m.group(2)
                ids = [int(i) for i in re.findall(r'<w:comment [^>]*w:id="(\d+)"', existing)]
                if ids:
                    next_id = max(max(ids) + 1, next_id)

        # match anchors to paragraphs
        paras = list(PARA_RE.finditer(doc))
        para_norm = [norm(para_text(m.group(0))) for m in paras]
        new_comments = []
        unmatched = []
        replacements = {}  # para index -> list of comment ids

        for fnd in findings:
            anchor = norm(fnd["anchor"])
            idx = None
            for i, pt in enumerate(para_norm):
                if anchor and anchor in pt:
                    idx = i
                    break
            if idx is None and len(anchor) > 60:  # fallback: first 60 chars
                short = anchor[:60]
                for i, pt in enumerate(para_norm):
                    if short in pt:
                        idx = i
                        break
            if idx is None:
                unmatched.append(fnd["anchor"][:80])
                continue
            cid = next_id
            next_id += 1
            new_comments.append(_comment_xml(cid, author, initials, date, fnd["comment"]))
            replacements.setdefault(idx, []).append(cid)

        # apply wraps from last paragraph to first (offsets stay valid)
        for idx in sorted(replacements, reverse=True):
            m = paras[idx]
            p_xml = m.group(0)
            for cid in replacements[idx]:
                p_xml = _wrap_paragraph_with_comment(p_xml, cid)
            doc = doc[: m.start()] + p_xml + doc[m.end():]

        # prepend executive summary
        if spec.get("summary"):
            with open(spec["summary"], encoding="utf-8") as f:
                summary_md = f.read()
            summary_xml = "".join(md_to_paragraphs(summary_md))
            summary_xml += '<w:p><w:r><w:br w:type="page"/></w:r></w:p>'
            bm = re.search(r"<w:body[^>]*>", doc)
            if not bm:
                die("word/document.xml has no <w:body> element")
            doc = doc[: bm.end()] + summary_xml + doc[bm.end():]

        with open(doc_path, "w", encoding="utf-8") as f:
            f.write(doc)

        if new_comments:
            comments_xml = (
                '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
                f'<w:comments xmlns:w="{W_NS}">'
                + existing_comments
                + "".join(new_comments)
                + "</w:comments>"
            )
            with open(comments_path, "w", encoding="utf-8") as f:
                f.write(comments_xml)

            # [Content_Types].xml override
            ct_path = os.path.join(tmpdir, "[Content_Types].xml")
            with open(ct_path, encoding="utf-8") as f:
                ct = f.read()
            if "/word/comments.xml" not in ct:
                ct = ct.replace(
                    "</Types>",
                    '<Override PartName="/word/comments.xml" ContentType="application/'
                    'vnd.openxmlformats-officedocument.wordprocessingml.comments+xml"/></Types>',
                )
                with open(ct_path, "w", encoding="utf-8") as f:
                    f.write(ct)

            # document.xml.rels relationship
            rels_path = os.path.join(tmpdir, "word", "_rels", "document.xml.rels")
            if os.path.exists(rels_path):
                with open(rels_path, encoding="utf-8") as f:
                    rels = f.read()
            else:
                os.makedirs(os.path.dirname(rels_path), exist_ok=True)
                rels = DOC_RELS_EMPTY
            if "relationships/comments" not in rels:
                rids = [int(i) for i in re.findall(r'Id="rId(\d+)"', rels)]
                rid = max(rids, default=0) + 1
                new_rel = (
                    f'<Relationship Id="rId{rid}" Type="http://schemas.openxmlformats.org/'
                    f'officeDocument/2006/relationships/comments" Target="comments.xml"/>'
                )
                if rels.rstrip().endswith("/>") and "<Relationship " not in rels:
                    rels = rels.replace("/>", ">") + new_rel + "</Relationships>"
                else:
                    rels = rels.replace("</Relationships>", new_rel + "</Relationships>")
                with open(rels_path, "w", encoding="utf-8") as f:
                    f.write(rels)

        # repack, preserving every original part
        if os.path.abspath(out_path) == os.path.abspath(docx_path):
            die("output path must differ from input path")
        with zipfile.ZipFile(out_path, "w", zipfile.ZIP_DEFLATED) as z:
            written = set()
            for name in names:
                src = os.path.join(tmpdir, name)
                if os.path.isfile(src):
                    z.write(src, name)
                    written.add(name)
            for root, _, files in os.walk(tmpdir):
                for fn in files:
                    full = os.path.join(root, fn)
                    arc = os.path.relpath(full, tmpdir).replace(os.sep, "/")
                    if arc not in written:
                        z.write(full, arc)

        print(f"Wrote {out_path}: {len(new_comments)} comment(s)"
              + (", summary prepended" if spec.get("summary") else ""))
        if unmatched:
            sys.stderr.write("UNMATCHED ANCHORS (fix and re-run):\n")
            for u in unmatched:
                sys.stderr.write(f"  - {u}\n")
            sys.exit(2)
    finally:
        shutil.rmtree(tmpdir, ignore_errors=True)


# ---------------------------------------------------------------- main

def main():
    args = sys.argv[1:]
    if not args:
        die(__doc__.strip(), 1)
    cmd = args[0]
    try:
        if cmd == "extract" and len(args) == 2:
            cmd_extract(args[1])
        elif cmd == "create" and len(args) == 3:
            cmd_create(args[1], args[2])
        elif cmd == "annotate" and len(args) == 4:
            cmd_annotate(args[1], args[2], args[3])
        else:
            die("usage: docx_tool.py extract <in.docx> | create <in.md> <out.docx> | "
                "annotate <in.docx> <findings.json> <out.docx>")
    except (KeyError, json.JSONDecodeError) as e:
        die(f"bad findings.json: {e}")
    except (OSError, zipfile.BadZipFile) as e:
        die(str(e))


if __name__ == "__main__":
    main()
