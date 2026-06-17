# Player Primer — Content Spec

*An instruction manual for compiling a shareable player primer from the master [System Reference](../System%20Reference/README.md). It defines what goes in, what stays out, the order, the length, and the output format for Discord.*

A **player primer** is the document you put in front of someone at session zero. Its job is narrow: get a new player from "I've never heard of this" to "I have a character and I understand a roll" — and make them *want* to. It is not the rulebook. It omits everything a player doesn't need to start, and it never includes GM machinery.

---

## 1. What goes in

Pull these from the master, in this order. Each line notes the **source** and the **trim** to apply.

1. **Cover & premise** — *Blood, Water & Violent Wind*, the tagline, and the "you are not heroes; you are pirates" framing.
   *Source:* [`00-primer.md`](../System%20Reference/00-primer.md). *Trim:* none — use whole.
2. **The World** — the Shackles, the Free Captains, the Eye, the crew.
   *Source:* [`01-the-world.md`](../System%20Reference/01-the-world.md). *Trim:* none, or cut "The Crew" if space is tight.
3. **How to Play** — the D10 roll and result table, difficulty (Risky/Dangerous), then stress & fallout, then the four timing gates in one paragraph.
   *Source:* [`02-the-system.md`](../System%20Reference/02-the-system.md). *Trim:* keep The Core Roll, Stress & Fallout, and a short Timing note. **Cut** the full Equipment/Resources/Tag glossary — replace with a half-page "reading your gear" box (dice = how big the stress die, plus a 6–8 tag mini-glossary covering only tags the starting kits use: Brutal, Piercing, Ranged, Reload, Tiring, Block, Wyrd).
4. **The Five Tracks** — what Blood / Tide / Reputation / Luck / Gold each mean, and one line on how each clears.
   *Source:* [`04-stress-tracks.md`](../System%20Reference/04-stress-tracks.md). *Trim:* keep the intro, the five-track table, and each track's one-paragraph description + "clearing" line. **Cut or collapse** the full Minor/Major fallout tables to "examples of what fallout looks like" (3–4 per track) — the GM owns the full tables; players meet them in play.
5. **Skills & Domains** — the eleven skills and nine domains with their one-line definitions, plus the knack rule.
   *Source:* [`03-skills-and-domains/`](../System%20Reference/03-skills-and-domains/). *Trim:* use the one-line table for each, plus the "skill + domain = who you are" paragraph. The full per-skill "applies when / knacks / overlaps" can be cut or moved to an appendix — nice but not needed to start.
6. **Callings** — the full set. Players choose one; this must be complete.
   *Source:* [`05-callings/`](../System%20Reference/05-callings/). *Trim:* none. Include the choosing guide and each calling's flavour, core ability, questions, beats, and carry table.
7. **Classes** — the full set. Players choose one; this must be complete.
   *Source:* [`06-classes/`](../System%20Reference/06-classes/). *Trim:* none (design notes are already stripped). Keep the balance note short or cut it — it's designer-facing.
8. **Ancestries** — the peoples of the Shackles (three cultures + five kindreds). Players choose one; include the lot.
   *Source:* [`07-ancestries/`](../System%20Reference/07-ancestries/). *Trim:* none — each is short (lore, three questions, names, a trinket table) and fully player-facing.
9. **Make Your Pirate** — the character-creation walkthrough.
   *Source:* [`08-character-creation.md`](../System%20Reference/08-character-creation.md). *Trim:* use the steps and the Quick Reference; you may cut the Advancement detail to a short "how you grow" paragraph for a session-zero primer.
10. **The Character Sheet** — the print-and-play sheet.
   *Source:* the existing `Character Sheet — Designer Build Brief` (in the *Personal: Custom Pirate Themed Roleplaying System* folder). Embed the finished sheet or link it.

> **The "◑ partly" rule.** Part Nine (Equipment & Resources) is the only ◑ part: a player needs *enough* of it to read a starting kit, but not buying/selling, haggling, armour, or the resource generator. Compress it to the gear box in item 3.

## 2. What stays out

Never put these in a player primer — they are full-system or GM-facing:

- **Part Ten — Ships & the Sea** (engagement ladder, chaos die, Hull repair, enemy statblocks). Players *experience* ship combat; they don't need to read it to start. A one-paragraph "your ship has a Hull track and the sea is its own kind of danger" teaser is the most a primer should carry.
- **Part Eleven — Ports, Havens & Haunts** (haunt economics, haunt upgrade maths, journey resistance, the bond fallout table). Players meet haunts and bonds in play; a short "you heal and make allies in port" note is plenty.
- **Part Twelve — Location Tiers** (regional danger, reward maths, statblock templates) — entirely GM.
- **The Appendices** (design frameworks, balance reviews, draft trails) — never.
- **Design notes, errata lines, "status: drafted" provenance, watch-lists, playtest flags** — strip all.
- **Enemy statblocks, GM "Distributing Resources" calibration, anything addressed to "the GM"**.

## 3. Shape & length

- **Target length:** Heart's own player primer is short — aim for **18–28 pages** at primer scale, the bulk of it the callings and classes (which carry most of the page count and can't be trimmed).
- **Reading order is onboarding order:** premise → world → how to play → tracks → skills/domains → callings → classes → make your pirate → sheet. A player should be able to read top-to-bottom and end with a character.
- **One voice:** second-person, present-tense, evocative but concrete — match the master's tone. No rules-lawyering, no cross-references a player can't follow, no "(see Part Eleven)".
- **Self-contained:** a primer must not depend on the reader having the master. Inline anything you reference.

## 4. Output format — solving the Discord/mobile problem

A print-style **PDF** is faithful but reflows badly on phones, and most of your table will open it on a phone in Discord. Recommended approach, in priority order:

1. **Primary — a single-file, responsive HTML edition.** One `.html` file, mobile-first, that reflows to any screen, themed with the [design language](design-language.md). Share it as a hosted link (GitHub Pages off this repo is free and natural, or any static host) or as a file drop. This is the best Discord-on-mobile experience by a wide margin: tap, read, pinch nothing.
2. **Secondary — a print/archival PDF**, generated from the *same* Markdown source. To make it survive mobile as well as possible: **single column, A5 or 6×9″ portrait, ~12–13pt body, generous line-height**, no multi-column spreads. A5 single-column is far more phone-legible than A4 two-column.
3. **Lightweight — chunked Markdown / Discord posts.** For quick reference, post the callings and classes as individual pinned messages or a Discord "forum" thread per class. Discord renders Markdown natively; the per-file structure of the master makes this almost copy-paste.
4. **Optional — section cards as PNGs.** For maximum in-client convenience, render each class/calling as a styled image card people can post inline. Highest effort; best for a "pick your class" pinned gallery.

**Compile once, export many.** Keep the primer as **one Markdown source** assembled per this spec; generate HTML and PDF from it (e.g. Pandoc, or a small static-site setup) so the two never drift. The design language is applied as one stylesheet shared by both.

## 5. Compile checklist

- [ ] Assemble the Markdown from §1 in onboarding order (the **"Make Your Pirate"** section now lives in Part Eight).
- [ ] Apply every §2 exclusion; strip all designer/GM text and cross-references.
- [ ] Compress Part Nine to the gear box; collapse the full fallout tables to examples.
- [ ] Apply the [design language](design-language.md): per-category colours, banners, typography.
- [ ] Export the responsive **HTML** (primary) and the A5 single-column **PDF** (secondary) from the one source.
- [ ] Proof on an actual phone in Discord before sharing.
- [ ] Drop the compiled edition in this folder and note it in the [CHANGELOG](../CHANGELOG.md).
