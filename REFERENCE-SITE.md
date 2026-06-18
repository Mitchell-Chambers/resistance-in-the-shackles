# Reference Site — Build & Deploy

This repo doubles as the source for a living, searchable reference site (the
Archive-of-Nethys / Compcon equivalent), built with **MkDocs Material** from the
Markdown in `System Reference/`. Edit a rule, push, and the site updates itself.

## How it's wired

- **`mkdocs.yml`** — site config. `docs_dir` is set to `System Reference/`, so only
  the reference is published; the rest of the vault (Ideation, Person Workspace,
  Reference rulebooks, etc.) stays private.
- **Auto nav** — there is deliberately no `nav:` list. MkDocs builds the sidebar
  from the file tree. Files are numbered (`00-`, `01-`…) so they sort correctly,
  and each page's title comes from its `# H1`. A folder's `README.md` becomes that
  section's landing page. **Drop in a new class/ancestry/calling `.md` and it shows
  up automatically** — nothing to maintain.
- **`System Reference/assets/shackles-site.css`** — custom skin reusing your design
  language (parchment + oxblood + gold, Cinzel/EB Garamond, the nine domain colours).
- **`.github/workflows/deploy.yml`** — builds and publishes to GitHub Pages on every
  push to `main`.

## Preview locally

```bash
pip install -r requirements.txt
mkdocs serve            # live-reloading preview at http://127.0.0.1:8000
```

`mkdocs build --strict` produces the static site in `site/` (git-ignored).

## Publish to GitHub Pages (one-time setup)

1. Push this repo to GitHub (private repos can still publish Pages on most plans).
2. On GitHub: **Settings → Pages → Build and deployment → Source: GitHub Actions**.
3. Push to `main`. The workflow builds and deploys; the live URL appears in the
   **Actions** run summary and under **Settings → Pages**.
4. Copy that URL into `site_url:` and the two `link:` fields in `mkdocs.yml`
   (used for the sitemap, social-share links, and the GitHub icon).

The published URL looks like `https://<username>.github.io/<repo>/`.

## Domain colour coding (optional polish)

To tint an entry with its domain colour, use `attr_list` in the Markdown:

```markdown
## Deepwater {.domain-deepwater}

<div class="domain-callout domain-arcane" markdown>
A tinted callout in the Arcane family.
</div>
```

Available: `domain-deepwater`, `-shallows`, `-port`, `-outlaw`, `-colonial`,
`-arcane`, `-faith`, `-ruins`, `-wilderness`.

## A Compcon-style character/ship builder (later)

The interactive builder is a separate, bigger project — a small web app that reads
your taxonomies as data. It can live at a subpath of the same site when you're ready.
