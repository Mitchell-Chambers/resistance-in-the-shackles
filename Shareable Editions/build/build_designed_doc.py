#!/usr/bin/env python3
"""
build_designed_doc.py — turn an assembled Markdown file into a themed, responsive
single-file HTML and (optionally) an A5 print PDF, using a design-language CSS.

This bakes in every pitfall fixed while building the first Shackles player primer.
See SKILL.md for the full process. Usage:

    python build_designed_doc.py INPUT.md OUTPUT_BASENAME \
        [--css assets/shackles.css] [--theme-module scripts/shackles_cards.py] \
        [--pdf] [--keep-links] [--no-toc] [--title "..."]

Produces OUTPUT_BASENAME.html and (with --pdf) OUTPUT_BASENAME.pdf.

Requires:  pip install markdown weasyprint --break-system-packages
"""
import argparse, importlib.util, os, re, sys
import markdown

def load_theme_module(path):
    if not path or not os.path.exists(path): return None
    spec = importlib.util.spec_from_file_location("theme_module", path)
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    return m

def ensure_blank_before_lists(md):
    """PITFALL 10: markdown needs a blank line before a list. Insert one wherever a
    list item directly follows a non-blank, non-list line, or sub-lists render as a
    run-on block of text."""
    lines=md.split("\n"); out=[]; li=re.compile(r"^\s*([-*+]|\d+\.)\s")
    for i,l in enumerate(lines):
        if li.match(l) and i>0 and lines[i-1].strip() and not li.match(lines[i-1]):
            out.append("")
        out.append(l)
    return "\n".join(out)

def slugify(text):
    return re.sub(r'[^a-z0-9]+', '-', text.lower()).strip('-') or "section"

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("input"); ap.add_argument("output")
    ap.add_argument("--css", default=os.path.join(os.path.dirname(__file__), "..", "assets", "shackles.css"))
    ap.add_argument("--theme-module", default=os.path.join(os.path.dirname(__file__), "shackles_cards.py"))
    ap.add_argument("--title", default=None)
    ap.add_argument("--pdf", action="store_true")
    ap.add_argument("--keep-links", action="store_true", help="keep internal .md links (default: neutralise to plain text for a self-contained doc)")
    ap.add_argument("--no-toc", action="store_true")
    ap.add_argument("--slug-map", default=None, help="optional theme-module attribute name holding a {title->slug} dict")
    a = ap.parse_args()

    md = open(a.input, encoding="utf-8").read()
    theme = load_theme_module(a.theme_module)

    # PITFALL 2: HTML-comment placeholder markers do NOT survive python-markdown.
    # Inject any bespoke raw-HTML blocks into the Markdown BEFORE conversion,
    # separated by blank lines so markdown passes them through verbatim.
    if theme and hasattr(theme, "INJECTIONS"):
        for marker, fn in theme.INJECTIONS.items():
            md = md.replace(marker, "\n\n" + fn() + "\n\n")

    # PITFALL 4: make the doc self-contained — turn internal relative links to plain text.
    if not a.keep_links:
        md = re.sub(r'\[([^\]]+)\]\((?!https?:|#)[^)]*\)', r'\1', md)

    # PITFALL 1: never use the 'nl2br' extension — it breaks block parsing and silently
    # drops most of the document. Use this safe extension set:
    md = ensure_blank_before_lists(md)
    html = markdown.markdown(md, extensions=['sane_lists', 'attr_list', 'tables', 'toc'],
                             output_format='html5')

    # Chapter wrapping: split on <h1> into sections; slug + class each, build a TOC.
    slug_map = getattr(theme, a.slug_map) if (theme and a.slug_map and hasattr(theme, a.slug_map)) else {}
    parts = re.split(r'(<h1[^>]*>.*?</h1>)', html, flags=re.S)
    pre = parts[0]; chapters = []
    i = 1
    while i < len(parts):
        h1 = parts[i]; body = parts[i+1] if i+1 < len(parts) else ""
        title = re.sub(r'<[^>]+>', '', h1).strip()
        sl = slug_map.get(title) or slugify(title)
        chapters.append((sl, h1, body)); i += 2

    body_html = [pre]; toc = []
    if not a.no_toc and len(chapters) > 1:
        toc = ['<nav class="toc"><div class="toc-title">Contents</div><ol>']
        for sl, h1, _ in chapters[1:]:
            toc.append(f'<li><a href="#{sl}">{re.sub(chr(60)+"[^"+chr(62)+"]+"+chr(62),"",h1)}</a></li>')
        toc.append('</ol></nav>')
    for idx, (sl, h1, bd) in enumerate(chapters):
        h1a = re.sub(r'<h1', f'<h1 id="{sl}"', h1, count=1)
        body_html.append(f'<section class="chapter ch-{sl}">{h1a}{bd}</section>')
        if idx == 0 and toc:
            body_html.append("".join(toc))
    content = "\n".join(body_html)

    css = open(a.css, encoding="utf-8").read()
    title = a.title or (re.sub(r'<[^>]+>', '', chapters[0][1]).strip() if chapters else "Document")
    doc = (f'<!DOCTYPE html><html lang="en"><head><meta charset="utf-8">'
           f'<meta name="viewport" content="width=device-width, initial-scale=1">'
           f'<title>{title}</title><style>{css}</style></head>'
           f'<body><div class="wrap">{content}</div></body></html>')

    out_html = a.output + ".html"
    open(out_html, "w", encoding="utf-8").write(doc)
    print("wrote", out_html, f"({len(doc)} bytes, {len(chapters)} chapters)")

    if a.pdf:
        # PITFALL 8: A5 paging comes from @page{size:A5} in the CSS; verify by rendering.
        from weasyprint import HTML
        out_pdf = a.output + ".pdf"
        HTML(out_html).write_pdf(out_pdf)
        print("wrote", out_pdf, f"({os.path.getsize(out_pdf)} bytes)")

if __name__ == "__main__":
    main()
