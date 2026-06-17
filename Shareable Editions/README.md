# Shareable Editions

The [`System Reference/`](../System%20Reference/README.md) is the master ruleset — complete, plain, and built for version control. It is *not* the thing you hand a new player in Discord.

This folder holds the recipe for turning the master into **shareable editions**: readable, attractive, on-boarding-friendly documents compiled from a curated slice of the master.

- **[`player-primer-content-spec.md`](player-primer-content-spec.md)** — the instruction manual: exactly what content goes into a player primer, what stays out, in what order, and which output format to use for Discord (and why).
- **[`design-language.md`](design-language.md)** — the visual design language reverse-engineered from the original PDF and reconciled with the project's aged-sea-chart brief: the colour system, typography, and layout to reuse when styling a primer.

When you compile a primer, you are pulling the ✅ parts of the master (see the System Reference contents table), trimming GM material, and pouring the result into the design language below. Compiled editions live alongside these two specs.

## Compiled editions

- **[`Player Primer/`](Player%20Primer/README.md)** — *Blood, Water & Violent Wind*, the first compiled player primer: a responsive **HTML** edition (best for Discord/mobile) and an A5 print **PDF**, both built from one Markdown source by the scripts in its `build/` folder. Rebuild after any rules change.
