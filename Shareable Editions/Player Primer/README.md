# Player Primer — *Blood, Water & Violent Wind*

The first compiled, shareable player primer for *Resistance in the Shackles* — everything a player needs to roll up a pirate and understand a roll, themed in the project's aged-sea-chart design language.

| File | What it is | Best for |
|---|---|---|
| **[`player-primer.html`](player-primer.html)** | Single-file, responsive HTML | **Sharing in Discord / reading on a phone.** Open it or host it (e.g. GitHub Pages); it reflows to any screen. |
| **[`player-primer.pdf`](player-primer.pdf)** | A5 single-column print PDF | Printing, archiving, and offline reading. ~165 A5 pages. |
| **[`player-primer.md`](player-primer.md)** | The assembled Markdown source | The single source both exports are built from. |
| **[`build/`](build/)** | The two build scripts | Reproducing the exports after a rules change. |

## What's in it (and what isn't)

Compiled per the [content spec](../player-primer-content-spec.md): the premise, the world, how to play (the roll, stress & fallout, timing, combat, a gear box), the five tracks, skills & domains, **all** callings, **all** classes, **all** ancestries, character creation, and a quick-reference card. GM-only material — ships, ports & haunts economics, location tiers, adversaries, and the GM chapter — is deliberately left out.

## Rebuilding it

After you change a rule in the [System Reference](../../System%20Reference/README.md), regenerate both exports from source:

```sh
# from this folder's build/ directory, with python3 + the markdown and weasyprint packages
python3 build/assemble_primer.py   # System Reference  ->  player-primer.md
python3 build/theme_primer.py      # player-primer.md   ->  player-primer.html (+ run weasyprint for the PDF)
```

The assembler pulls and trims the System Reference parts; the themer applies the [design language](../design-language.md) (parchment, oxblood banners, the per-track and per-domain colour system, woodcut headers) and emits the HTML, from which WeasyPrint renders the A5 PDF.

> **Note on fonts:** the HTML pulls *Cinzel* and *EB Garamond* from Google Fonts and degrades gracefully to serif offline. The PDF embeds whatever was available at build time.
