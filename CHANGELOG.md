# Changelog

All notable changes to *Resistance in the Shackles* are recorded here. The headline deliverable is the **[System Reference](System%20Reference/README.md)** (the master ruleset); [`Shareable Editions/`](Shareable%20Editions/README.md) holds the recipe for player-facing primers, and the surrounding folders hold source and ideation material.

The format is loosely based on [Keep a Changelog](https://keepachangelog.com/). Dates are ISO (YYYY-MM-DD). When you change a rule, add a bullet under **[Unreleased]** and reference the Part you touched.

## [Unreleased]

- _Nothing yet._

## [0.7.0] — 2026-06-17

The third and last structural gap closed: opposition to point at the crew.

### Added

- **Part Fourteen — Adversaries** — generalises the adversary statblock off the ship case (DIFFICULTY / RESISTANCE / PROTECTION / STRESS + tags / RESOURCES / MOVES; no rounds; mobs as one Resistance; Legendary threats as arc-length weather), with a calibration box for stat ranges. Includes an original starter bestiary of ~20 Shackles threats:
  - **People of the Inner Sea** — Chelish naval officer, colonial marines, Aspis enforcer and factor, Rahadoumi Pure Legion zealot, press-gang, sea-witch.
  - **Beasts of the Shackles** — reef shark pack, reef lurker, brine-scuttler, jungle predator, bloodfly swarm, great squid.
  - **The Drowned & the Deep** — the Drowned, ghost-light, Ghol-Gan stone sentinel, trench-thing, revenant of the Code.
  - **Legendary Threats** — *Old Sorrow* (a leviathan), *What the Eye Keeps* (a storm-bound horror), *The Lord-Admiral's Hound* (a pirate-hunter and her warship).

### Changed

- **Cohesion gap analysis** updated: all three structural gaps (ancestries, GM chapter, bestiary) now closed — the System Reference stands on its own as a complete game. Remaining items are polish (combat/healing consolidation, a quick-reference page, worked landmarks, the character sheet in-tree).

## [0.6.0] — 2026-06-17

Added the GM half of the game.

### Added

- **Part Thirteen — Running the Game** — the GM chapter, consolidating front matter that was previously scattered across the rules: the GM's job and principles; when to call for a roll; setting difficulty; the craft of **assigning stress and choosing the track**; **framing fallout** as concrete fiction; **pacing the doom** (running Luck and the callings' Downfalls honestly, and never telling a player their beats); building landmarks, haunts, journeys, and adversaries from the templates; a **session-zero** procedure with safety tools; and running beats and advancement. Ends with a first-session checklist.

### Changed

- **Ancestries:** removed the proposed "Drowned" expansion kindred and recorded the reason — being claimed by the sea and returning not-quite-human is the **Tide** track's gravest stake and the heart of *Cursed Tides*; it must remain a fate, never a character-creation option. Noted in the ancestries index and the gap analysis.
- **Cohesion gap analysis** updated: Running the Game marked resolved; remaining roadmap is the adversary bestiary, then the smaller polish items.

## [0.5.0] — 2026-06-17

Reworked Ancestries into a two-tier **cultures + kindreds** model.

### Changed

- **Part Seven — Ancestries** restructured. **Cultures** (for humans, elves, half-elves and the like — defined by upbringing, not species; there is no standalone "human" or "elf" ancestry): **Shackleborn**, **Bonuwat**, **Chelaxian**, each now noting it is a culture open to multiple species. **Kindreds** (peoples set apart by nature):
  - **Small Folk** — merges halfling, gnome, and dwarf into the small "ordinary" peoples (was *Halfling*).
  - **Big Folk** — merges half-orc, minotaur, and hobgoblin into the large martial peoples (was *Half-Orc*).
  - **Beast-folk** — merges tengu, catfolk, ratfolk, merfolk, and naga into the animalistic peoples (was *Tengu*).

### Added

- **Goblinkin** (goblins, kobolds) — the "monstrous small," a deliberate contrast to Small Folk.
- **The Made** (androids, automatons, homunculi) — constructed beings claiming a self.

### Notes

- Files renamed via `git mv` (`halfling`→`small-folk`, `half-orc`→`big-folk`, `tengu`→`beast-folk`). README, character creation, primer spec, gap analysis, and navigation updated. Expansion picks reframed as a future **Drowned** kindred (gillmen/merfolk-kin/undine/sahuagin-touched) and **Planetouched** kindred (tieflings/aasimars).

## [0.4.0] — 2026-06-17

Added the third character pillar: **Ancestries**.

### Added

- **Part Seven — Ancestries** — who you are, before the dice. Mechanics-free, grounded in the Pathfinder *Golarion* Shackles, with an opening set of six peoples covering all five social positions from the design guide: **Shackleborn**, **Bonuwat**, **Chelaxian**, **Half-Orc**, **Halfling**, and **Tengu**. Each has a lore block, three world-anchored background questions, names with conventions, and a d20 trinkets table. The folder is extensible; the index lists strong next picks (Gillman, Tiefling, inland Mwangi, Grippli, Undine, sahuagin-touched).

### Changed

- **Renumbered** to slot Ancestries in as the third pillar (after Classes, before Character Creation): Character Creation → **Part Eight**, Equipment & Resources → **Part Nine**, Ships & the Sea → **Part Ten**, Ports/Havens/Haunts → **Part Eleven**, Location Tiers → **Part Twelve**. README, character creation, the ships intro, the primer spec, the cohesion gap analysis, and all navigation footers updated to match.
- **Cohesion gap analysis** updated: Ancestries marked resolved (opening set), with remaining expansion picks noted; build order advanced to Running the Game next.

## [0.3.0] — 2026-06-17

Added character creation and an honest map of what's still missing.

### Added

- **Part Seven — Character Creation** ("Make Your Pirate") — the build walkthrough (concept → class → calling → ancestry → resistances → bonds → crew/ship/home port → finish), an Advancement section (beats → minor/major/zenith advances), and a one-glance Quick Reference.
- **Appendix: [cohesion gap analysis](System%20Reference/appendices/cohesion-gap-analysis.md)** — a chapter-level comparison against Heart's structure identifying what the master still needs to be self-contained: **ancestries** (designed but unwritten), a **Running the Game / GM chapter**, an **adversary bestiary** (only ships are statted today), consolidated **healing & character-scale combat**, **worked landmarks/gazetteer**, a **quick-reference page**, and the **character sheet** in-tree — with a suggested build order.

### Changed

- **Renumbered** the back half to slot character creation into the player-facing block: Equipment & Resources → **Part Eight**, Ships & the Sea → **Part Nine**, Ports/Havens/Haunts → **Part Ten**, Location Tiers → **Part Eleven** (history preserved via `git mv`). README, cross-references, the primer spec, and all navigation footers updated to match.

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
[0.7.0]: #070--2026-06-17
[0.6.0]: #060--2026-06-17
[0.5.0]: #050--2026-06-17
[0.4.0]: #040--2026-06-17
[0.3.0]: #030--2026-06-17
[0.2.0]: #020--2026-06-17
[0.1.0]: #010--2026-06-17
