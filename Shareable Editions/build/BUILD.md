
# Designed Document Builder

Turn one or more Markdown files into a **themed, responsive HTML** edition and a matching **A5 print PDF**, both from a single source. Built for *Resistance in the Shackles* shareable editions, reusable for any designed doc.

## The pipeline

1. **Assemble** — pull the wanted sections out of the source/reference Markdown, apply trims, and concatenate into one `*.md`. (Project-specific; see `reference/assemble_primer.example.py` for a worked example that pulls + trims a System Reference.)
2. **Theme** — `scripts/build_designed_doc.py` converts that Markdown to a single self-contained HTML styled by `assets/shackles.css`, then (with `--pdf`) renders an A5 PDF via WeasyPrint.
3. **Verify** — render a few PDF pages to PNG and eyeball them before shipping.

```sh
pip install markdown weasyprint --break-system-packages   # one-time; also need poppler-utils + imagemagick to verify

# build HTML + A5 PDF from an assembled markdown file:
python scripts/build_designed_doc.py INPUT.md OUTPUT_BASENAME \
    --css assets/shackles.css --theme-module scripts/shackles_cards.py --slug-map SLUGS --pdf

# verify visually:
pdftoppm -f 1 -l 12 -r 70 -png OUTPUT_BASENAME.pdf pg && montage pg-*.png -tile 4x3 -geometry 300x -background white contact.png
```

The builder, by default, makes the doc **self-contained** (neutralises internal relative `.md` links to plain text), wraps each `#` chapter in a `<section>` with a slug id, and auto-builds a Contents list. Pass `--keep-links` to keep links, `--no-toc` to skip the TOC.

## Pitfalls — DO NOT repeat these

These cost real time the first build. The bundled scripts already handle them; honour them in any hand-rolled variant.

1. **Never use the `nl2br` markdown extension.** It mangles block parsing and *silently drops most of the document* (you get a tiny HTML with only the first few sections). Use exactly: `extensions=['sane_lists','attr_list','tables','toc']`.
2. **HTML-comment placeholder markers do not survive python-markdown.** Don't convert first and regex-replace `<!--X-->` in the HTML — the markers get mangled and the `.*?` swallows content. Instead **inject bespoke raw HTML into the Markdown string *before* conversion**, separated by blank lines, so markdown passes it through verbatim. (See `INJECTIONS` in `shackles_cards.py`.)
3. **Don't wrap content in `<div>` in the Markdown** expecting the inner Markdown to render — without the `md_in_html` extension + `markdown="1"` it won't. **Prefer demoting headings by one `#`** (so included files' `# Title` becomes `## Title`) to nest them under chapter headings; theme by chapter/section instead of wrapper divs.
4. **Make shareable docs self-contained.** Strip internal cross-links: `re.sub(r'\[([^\]]+)\]\((?!https?:|#)[^)]*\)', r'\1', md)`. A primer should not say "(see Part Nine)" with a dead link.
5. **`tcard`/`dchip`/`schip` are CSS *classes*, not tags.** When sanity-checking output, grep for `class="tcard"`, not `<tcard`. (This caused a false "the cards didn't render" alarm.)
6. **The repo `.gitignore` has a global `*.pdf` rule** (it excludes reference rulebooks). To commit a compiled PDF, add a negation: `!path/to/your-output.pdf`.
7. **OneDrive-mounted repos:** in the build VM, `rm`/unlink fails ("Operation not permitted") but rename works. Before each `git` op, sweep stale locks: `find .git -name '*.lock' | while read f; do mv "$f" ".git/.junk/$(basename "$f").$RANDOM"; done`. Pipe git output through `grep -v 'unable to unlink'`. File deletion can be enabled via the cowork delete-permission tool.
8. **A5 paging comes from `@page{ size:A5; margin:... }` in the CSS**, which WeasyPrint honours. Two-column grids collapse to one column at A5 width automatically (their media queries don't trigger). Always render a contact sheet (pdftoppm → montage) and *look* before declaring done.
9. **Fonts:** the HTML `@import`s *Cinzel* + *EB Garamond* from Google Fonts and degrades to serif offline; WeasyPrint embeds whatever it can fetch at build time. Don't assume the fancy face is present — keep serif fallbacks.
10. **A list needs a blank line before it.** If a sub-list (e.g. a major ability's sub-abilities) directly follows a paragraph with no blank line, python-markdown folds it into the paragraph and it renders as a run-on **block of text**. `ensure_blank_before_lists` inserts the blank line; honour it in any hand-rolled variant.

## The design language (what `shackles.css` encodes)

Parchment ground (`#EFE6D2`→`#E4D6B8`); sepia ink (`#1A1208`); **oxblood** house red (`#7A1F12`); **gold** accent (`#C9A97A`) for text on dark banners; faded-brown rules (`#9B7E55`). Display = *Cinzel* (carved caps); body = *EB Garamond*. H2s are oxblood→ember gradient banners with gold caps; diamond (◆) bullets; parchment statblock blockquotes.

The **per-category colour system** (the distinctive part) lives in `shackles_cards.py`: each of the **nine domains** has its own dark/mid family colour; the **five stress tracks** are colour-coded (Blood red, Tide blue, Reputation amber, Luck green, Gold ochre); **skills** share one oxblood-red family. These render as coloured cards/chips, injected at markers. The authoritative palette is `Shareable Editions/design-language.md` in the project.

## Files in this skill

- `scripts/build_designed_doc.py` — the generic, CLI builder (md → themed HTML + A5 PDF), with all pitfalls handled.
- `scripts/shackles_cards.py` — the Shackles theme module: per-track / per-domain / per-skill colour cards, marker `INJECTIONS`, and stable chapter `SLUGS`.
- `assets/shackles.css` — the full design-language stylesheet (screen + `@page` print), compass-rose motif embedded.
- `reference/assemble_primer.example.py` — a worked assembler: pulls + trims a System Reference into one primer Markdown (demote-headings, strip nav footers, curated front matter).
- `requirements.txt` — `markdown`, `weasyprint`.

To adapt for a **new edition** (e.g. a GM screen): write an assembler that selects the right sections, then run the builder with the same CSS/theme module. To adapt the **look**, edit `shackles.css` and the colour tables in `shackles_cards.py`.
