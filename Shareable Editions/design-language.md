# Design Language

*Reverse-engineered from the original* Resistance in the Shackles *PDF/Word document and reconciled with the project's "aged sea chart" character-sheet brief. This is the visual specification to reuse when styling any shareable edition.*

The single most distinctive thing about the original document is that **it colour-codes the game's taxonomies**. Skills, domains, and stress tracks each carry a thematic colour, and within the domains *every individual domain has its own colour family*. That system is the spine of this design language; everything else serves it.

---

## 1. Principles

1. **Colour is meaning.** A reader should be able to tell what *kind* of thing they're looking at — a domain, a skill, a track — from its colour alone, before reading a word. Never use a category's colour for anything else.
2. **Banners, not boxes.** Each entry is introduced by a coloured banner band (a "carved nameplate"), not a thin rule. The name sits in the band.
3. **Three tones per family.** Every thematic colour exists as **dark** (the name banner), **mid** (the description banner), and **light** (the callout tint). This three-step rhythm repeats across the whole document.
4. **Warm, aged, legible.** The aesthetic is an aged sea chart — parchment, oxblood, sepia ink — but contrast and legibility always win over texture.

## 2. Substrate & neutrals

The original PDF sat on plain white. For shareable editions, move to the brief's parchment, which reads warmer and more in-world while staying high-contrast.

| Token | Hex | Use |
|---|---|---|
| Parchment (page) | `#EFE6D2` → `#E4D6B8` | Page background, faint foxed/mottled texture, subtly darkened edges. (White `#FFFFFF` is the legacy PDF substrate — acceptable, plainer.) |
| Sepia ink (body) | `#1A1208` / `#2B2118` | Body text, the darkest ink. The document body uses near-black warm sepia, never pure `#000`. |
| Gold leaf (on dark) | `#C9A97A` | Text colour for entry **names** sitting on a dark banner. The signature accent. |
| Banner white | `#FFFFFF` | Text colour for **descriptions/taglines** sitting on a mid banner. |
| Faded brown (rules) | `#9B7E55` | Hairlines, table rules, ruled write-in lines, low-contrast borders. |

## 3. The thematic colour system

This is the heart of the language. Each family has **dark / mid / light**. Names go on *dark* in gold (`#C9A97A`); descriptions go on *mid* in white; callouts/fallout-flavour tint boxes are *light* with sepia text.

### Domains — nine families (exact, from the source document)

| Domain | Dark (name) | Mid (description) | Light (callout) |
|---|---|---|---|
| **Deepwater** | `#0D2B45` | `#1B4F72` | `#D6E8F5` |
| **Shallows** | `#0D3B2B` | `#1A5C3A` | `#D0EDDC` |
| **Port** | `#2B1A0D` | `#7A3B0D` | `#F5E6CC` |
| **Outlaw** | `#1A0D0D` | `#6B1A1A` | `#F5D6D6` |
| **Colonial** | `#1A1A2B` | `#2B2B6B` | `#D6D6F5` |
| **Arcane** | `#2B0D2B` | `#5C1A6B` | `#EDD6F5` |
| **Faith** | `#2B2000` | `#6B5200` | `#F5EBB0` |
| **Ruins** | `#1A1A10` | `#4A4A28` | `#E5E5CC` |
| **Wilderness** | `#1A2B0D` | `#3B5C1A` | `#D8EDCC` |

Each domain's colour is thematic: Deepwater is open-ocean blue, Shallows reef-green, Port harbour-amber, Outlaw blood-red, Colonial naval indigo, Arcane witch-purple, Faith ochre-gold, Ruins khaki-stone, Wilderness jungle-green.

### Skills — one family

Skills all share an **oxblood-red** family in the source (sampled `#6B1A1A` mid, `~#480C0C` dark, `#F5D6D6` light — the same red as the Outlaw domain). Skills are a single category, so one colour reads correctly.

| | Dark | Mid | Light |
|---|---|---|---|
| **Skills** | `#480C0C` | `#6B1A1A` | `#F5D6D6` |

### Stress tracks — five families (one per track)

The tracks are colour-coded individually, reusing the thematic palette so a track's colour matches its felt meaning:

| Track | Dark | Mid | Light | Borrowed from |
|---|---|---|---|---|
| **Blood** | `#480C0C` | `#7B1C1C` | `#F5D6D6` | oxblood red |
| **Tide** | `#0D2B45` | `#1B4F72` | `#D6E8F5` | Deepwater blue |
| **Reputation** | `#2B1A0D` | `#7A3B0D` | `#F5E6CC` | Port amber |
| **Luck** | `#0D3B2B` | `#1A5C3A` | `#D0EDDC` | Shallows green |
| **Gold** | `#2B2000` | `#6B5200` | `#F5EBB0` | Faith ochre |

*(Blood/Tide/Reputation/Luck/Gold hues are confirmed by sampling the source pages; the dark/light steps follow the domain family they share so the three-tone rhythm stays consistent.)*

### Callings & Classes

The source treats these as single categories with a restrained, dark/neutral header (closer to plain sepia-on-parchment than a saturated band). Recommended: give **callings** and **classes** each one quiet family so they read as their own kind without competing with the loud domain/track colours — e.g. callings in the deep **oxblood** house red (`#7A1F12` dark per the brief), classes in **sepia/charcoal** (`#2B2118`). Keep them subdued; the saturated colour budget belongs to domains and tracks.

## 4. Typography

| Role | Treatment |
|---|---|
| **Display / banners** | A weathered slab or engraved "woodcut" serif, **all-caps, letter-spaced** — carved-nameplate feel. (The brief's direction; the legacy doc used a plain bold serif, which is the fallback.) |
| **Part & section titles** | Same display face, oxblood `#7A1F12`, large. |
| **Body** | A readable serif, sepia ink, generous line-height. Justified in the print PDF; left-aligned in HTML. |
| **Sub-labels** (e.g. "THIS SKILL APPLIES WHEN YOU…") | Display face, small, oxblood caps, letter-spaced. |
| **Italic accents** (taglines, overlap notes, flavour) | Flowing italic, oxblood or muted sepia. |

Embed or use widely available faces. A safe free pairing that matches the intent: **display** — a slab serif such as *Zilla Slab* or *Aleo*; **body** — a humanist serif such as *Source Serif* or *EB Garamond*. Keep to two families.

## 5. Components

- **Entry banner** — full-width band, dark family colour, name in gold caps (`#C9A97A`), letter-spaced. Optionally a left-edge colour bar in the same family (the tracks use a vertical sidebar in the source).
- **Description band** — immediately under the name, mid family colour, white italic tagline.
- **Callout / fallout-flavour box** — light family tint, sepia text, used for the short "what this costs you" notes.
- **Bullets** — a small **diamond ◆** glyph in the family's mid colour (the source uses ◆ for "applies when" lists).
- **Tables** — faded-brown `#9B7E55` hairlines, parchment ground, sepia text; header row in the section's dark colour with gold text.
- **Statblocks** (landmarks, ships, enemies) — a bordered parchment box, label words (`DOMAINS`, `TIER`, `STRESS`, `RESISTANCE`) in oxblood small-caps, values in sepia; render the leading `>` blockquotes from the master this way.
- **Tag chips** — small sepia-outlined pills for equipment tags (the source shows tags like `VANISH` in a dark inset box).

## 6. Motifs (sparing, never load-bearing)

From the aged-sea-chart brief: torn/darkened parchment edges; banner ribbons pinned with a nail, rope-tie, or wax seal; a faint **compass-rose** watermark behind large open areas (notes, chapter openers); an optional low-contrast rope or chain border. Texture must never reduce text or rule contrast, and the whole thing must survive **greyscale printing and photocopying** — colour is a bonus, not load-bearing.

## 7. Reusable tokens (CSS)

Drop-in variables for the responsive HTML edition (and any CSS-to-PDF pipeline). Each family exposes `-dark`, `-mid`, `-light`; set them per section/entry.

```css
:root {
  /* substrate & neutrals */
  --paper: #EFE6D2;  --paper-edge: #E4D6B8;
  --ink: #1A1208;    --ink-strong: #2B2118;
  --gold: #C9A97A;   --on-banner: #FFFFFF;
  --rule: #9B7E55;   --oxblood: #7A1F12;

  /* domains */
  --deepwater-dark:#0D2B45; --deepwater-mid:#1B4F72; --deepwater-light:#D6E8F5;
  --shallows-dark:#0D3B2B;  --shallows-mid:#1A5C3A;  --shallows-light:#D0EDDC;
  --port-dark:#2B1A0D;      --port-mid:#7A3B0D;      --port-light:#F5E6CC;
  --outlaw-dark:#1A0D0D;    --outlaw-mid:#6B1A1A;    --outlaw-light:#F5D6D6;
  --colonial-dark:#1A1A2B;  --colonial-mid:#2B2B6B;  --colonial-light:#D6D6F5;
  --arcane-dark:#2B0D2B;    --arcane-mid:#5C1A6B;    --arcane-light:#EDD6F5;
  --faith-dark:#2B2000;     --faith-mid:#6B5200;     --faith-light:#F5EBB0;
  --ruins-dark:#1A1A10;     --ruins-mid:#4A4A28;     --ruins-light:#E5E5CC;
  --wilderness-dark:#1A2B0D;--wilderness-mid:#3B5C1A;--wilderness-light:#D8EDCC;

  /* skills (one red family) */
  --skill-dark:#480C0C; --skill-mid:#6B1A1A; --skill-light:#F5D6D6;

  /* stress tracks */
  --blood-dark:#480C0C; --blood-mid:#7B1C1C; --blood-light:#F5D6D6;
  --tide-dark:#0D2B45;  --tide-mid:#1B4F72;  --tide-light:#D6E8F5;
  --rep-dark:#2B1A0D;   --rep-mid:#7A3B0D;   --rep-light:#F5E6CC;
  --luck-dark:#0D3B2B;  --luck-mid:#1A5C3A;  --luck-light:#D0EDDC;
  --gold-dark:#2B2000;  --gold-mid:#6B5200;  --gold-light:#F5EBB0;
}
```

## 8. Do & don't

- **Do** keep one colour per category; **do** carry dark/mid/light through every banner; **do** keep oxblood `#7A1F12` as the house red for Part titles and structural accents.
- **Don't** let domain/track colours bleed onto unrelated UI; **don't** drop below greyscale legibility for the sake of texture; **don't** introduce a third type family or a colour outside the families above.
