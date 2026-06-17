# Changelog

All notable changes to *Resistance in the Shackles* are recorded here. The headline deliverable is the **[System Reference](System%20Reference/README.md)** (the master ruleset); [`Shareable Editions/`](Shareable%20Editions/README.md) holds the recipe for player-facing primers, and the surrounding folders hold source and ideation material.

The format is loosely based on [Keep a Changelog](https://keepachangelog.com/). Dates are ISO (YYYY-MM-DD). When you change a rule, add a bullet under **[Unreleased]** and reference the Part you touched.

## [Unreleased]

- _Nothing yet._

## [0.2.0] — 2026-06-17

Reframed the project from a player primer into the **master system reference**. The six-part player reference was the wrong scope — it is now the player-facing *subset* of a complete ruleset.

### Changed

- **Renamed `Player Reference/` → `System Reference/`** (history preserved via `git mv`) and reframed it as the master ruleset. The README now marks each part's primer-eligibility (✅ player / ◑ partial / ⚙️ full-system & GM).

### Added

- **Part Seven — Equipment & Resources** — the full equipment, quality, tag, resource, and haggling rules (Part Two keeps a condensed summary that now links here).
- **Part Eight — Ships & the Sea** — Ships of the Shackles (engagement ladder, chaos die, fittings), the Hull track, and Journeys at Sea.
- **Part Nine — Ports, Havens & Haunts** — landmarks, journeys, haunts, removing stress by track, and bonds.
- **Part Ten — Location Tiers** — regional danger 0–4, default stress, rewards, statblock template.
- **Appendices** — a curated index of the design frameworks, balance reviews, and draft trails behind the rules (links, not copies).
- **`Shareable Editions/`** — `player-primer-content-spec.md` (what goes into a shareable primer, what stays out, and Discord/mobile format guidance) and `design-language.md` (the original document's per-category colour system, exact domain palette, typography, and reusable CSS tokens, synthesized with the aged-sea-chart brief).

### Notes

- Folded system docs had their "status: drafted" provenance lines trimmed; their design reasoning is preserved in the Appendices index.
- Navigation footers regenerated across all 36 reference pages for the expanded structure.

## [0.1.0] — 2026-06-17

First version-controlled build. The old 145-page PDF player reference was rebuilt as a six-part Markdown project under `Player Reference/`, assembled from the latest canonical sources, and the repository was initialized.

### Added

- **Repository** initialized at the project root with `.gitignore` (excludes PDFs, `.obsidian/`, OS cruft) and this changelog.
- **Player Reference** — a six-part player-facing document mirroring the original primer's structure, with prev/next/contents navigation footers on every page:
  - **Primer** and **Part One — The World** — setting and tone carried forward from the original PDF (the Shackles, the Free Captains, the Eye of Abendego, the crew).
  - **Part Two — The System** — the core D10 roll, stress & fallout (D12 vs. total), the four timing gates, and a full equipment + tag glossary.
  - **Part Three — Skills & Domains** — the eleven skills and nine domains.
  - **Part Four — Stress Tracks** — Blood, Tide, Reputation, Luck, Gold, with full fallout tables.
  - **Part Five — Callings** — eight callings plus the shared Piracy calling, with a shared-rules and calling-choosing guide.
  - **Part Six — Classes** — all ten classes, with the balance summary.
- **Project sources** committed as a baseline: class Versions 2–5, callings Passes 1–3, system documents, and Heart reference notes.

### Canonical sources used

- **Classes** — `Game System/Version 5/` (the play-style rebalance: combat floor enforced, social/knowledge spikes trimmed, party healing spread across five classes).
- **Callings** — `Ideation/Pass 3 - Callings/` (the story-arc rebuild; every core ability reworked to Heart-grammar in the core-ability workshop). Chosen over the older Pass 2 ("v2").
- **Core** (skills, domains, stress tracks) — `Ideation/Pass 1 - Concepts/`, with the 2026-06-10 errata applied (pure-Heart fiction-scoped timing, equipment-tag conformance, Wyrd→Tide remap).

### Notes

- Non-player-facing "Design Notes" sections were stripped from the copied class files; the reference contains only player-facing rules and flavour.
- Ship-scale systems (Hull, Journeys, Ship Combat, Ships of the Shackles), Ports & Haunts, Location Tiers, and the full Equipment & Resources document remain in the wider project and are referenced from the reference where relevant.

[Unreleased]: #unreleased
[0.2.0]: #020--2026-06-17
[0.1.0]: #010--2026-06-17
