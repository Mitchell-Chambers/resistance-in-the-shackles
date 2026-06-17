# Class Errata — Pending Application to Version 4

*STATUS: **APPLIED 2026-06-10** — sections 1–5 executed against Version 4 in a single pass and verified (no remaining "exchange" timing units outside THE LAST BOUT's exempt prose; Tend Blood/Tide gone; Degenerating restored; tier blockquote replaced; Living Ship in Hull grammar; each touched file carries an errata line in its design notes). Section 6 remains a list of design options, deliberately not applied.*

---

## 1. Exchange rewrites (pure-Heart durations)

| File : line | Current | Proposed |
|---|---|---|
| corsair : BOARDING MASTER | "+1 Blood protection for the first exchange" | "+1 Blood protection until they next act" |
| corsair : BOARDING ACTION | "roll with mastery for the first exchange" | "roll with mastery on the first action they take under your direction" |
| daredevil : THE READ | "observing … for one exchange" | "observing … for a few moments" |
| daredevil : LEAVE A DOUBLE | "It buys one full exchange before anyone realises you are gone." | "It buys a few precious seconds — until someone acts on it — before anyone realises you are gone." |
| errant : FORM PERFECT | "roll with mastery on the first exchange" | "roll with mastery on your first action" |
| powder_mage : PERFECT SHOT | "after at least one exchange" | "after shots have been traded at least once" |
| powder_mage : SECOND GUN | "The first exchange cannot catch you without options." | "The opening moments cannot catch you without options." |
| sin_bosun : STORM CALLING | "Ships caught in it take D8 Hull stress per exchange." | "Ships caught in the storm mark D8 Hull stress whenever they fail or partially succeed on an action to sail, fight or free themselves within it — and whenever the GM judges the storm simply finds them." |
| sin_bosun : THE EYE | "Enemies cannot follow into the calm without taking Hull stress each exchange." | "Enemies who follow you into the calm mark D8 Hull stress for every action they take to do so." |

## 2. Equipment conformance

- **sin_bosun, Core Traits** — "Scripture-inked bandages, blessed rum and a belaying pin *Tend Blood/Tide D6*" → "*Tend Blood D6*". Tide is not equipment-healable (ratified). The bandages still matter to the priest; the soul-care lives in MINISTRATIONS and the Leeward Shrine-style haunts, where it belongs.
- Audit all class equipment against the tag glossary — all currently used tags are now defined (incl. Maddening); no other changes expected.

## 3. Tag resolutions

- **Wyrd stays Wyrd** — the long-pending rename (Fathomless/Tide-touched) is closed: per the tag glossary, names keep, tracks remap (Wyrd now marks Tide). Remove the rename note from castaway's design notes and the V2/V3 overview dependency lists.
- **Degenerating is canon** — optionally restore daredevil SPECIALTY LOAD's poison option to "the knives gain the Degenerating tag" (cleaner than the improvised D8 wording).
- **Spread now has full rules** (Vanish+Domain to avoid; NPCs simply take it) — KNIFE STORM, SPLINTER SHOT, THE NAME SPOKEN OVER WATER and THE CYCLOPS CANTO need no text changes; they simply work now.

## 4. Tier conformance

- **castaway, ISLANDSBLOOD** — delete the inline "Location Tiers (working draft)" blockquote; replace with "(see Location Tiers)". The ability text itself is unchanged; tier-as-number is now defined in the tier doc.
- Anything keyed to "size and importance" of a port (corsair HOMECOMING, the old shrine-refresh grammar) may optionally be re-anchored to the tier table (D4 at Tier 0–1 … D12 at the legendary ports); GM-judgement wording is also fine as-is. Decision at application time.

## 5. Hull conformance

- **sawbone, THE LIVING SHIP** — "Hull stress marked against your vessel is reduced by 1" may be reworded "your vessel counts as having +1 Hull protection" to use the track's own grammar. Mechanically identical.
- CANNIBALISED PARTS, REPAIR IN MOTION, IMPOSSIBLE REPAIR, NO DEAD SHIPS, FIRING SOLUTION, POWDER KEG — all now resolve cleanly against the Hull track; no text changes.

## 6. Opportunities — RESOLVED 2026-06-10 against Heart precedent

Reviewed every option against what Heart's classes actually do:

- **BACK ROOM as bond — APPLIED.** Direct precedent: the Witch's LAIR says verbatim "Your lair acts as a bond (p. 98)." The V4 port dropped the clause only because bonds didn't exist in our system yet — that was the error, now corrected in class_sharper.md.
- **Web contacts / congregations / drinking companions as bonds — REJECTED.** Heart forms bonds "at the GM's discretion" and never auto-converts an NPC network: the Incarnadine's NETWORK *references* bonds ("communicate with bonds or haunts") but doesn't create them. Our relationships are bond *candidates* the table can promote in play, exactly as Heart intends.
- **PERFECT INSTRUMENT creates Renowned items — REJECTED.** Heart: renowned items "aren't the kind of things you can purchase… you tend to inherit them," and no Heart ability manufactures one — even RUST AND IRON tops out at quality steps plus bad tags. A Perfect Instrument may *become* Renowned through story at the GM's discretion, like anything else; writing that into the ability would exceed every precedent.
- **Class abilities granting knacks — already conformant.** Heart grants knacks from class text exactly twice (RED FEAST, OATH OF FURY); our RED FEAST port carries the line, and nothing else should. Knacks otherwise arrive via taking a skill twice or Renowned equipment.
- **Carouse Reputation-refresh line — APPLIED** to shackles_skills.md (also retiring the stale "Nerve" track name in that bullet).
- **Quest-reward donation loop — APPLIED** to the Reputation section of shackles_stress_tracks.md.

**New item from the review:** Pass 1's per-skill knack lists pre-date the Heart extraction and several violate Heart's knack grammar — in Heart a knack does one thing only: "Using a knack allows you to roll with mastery" (max one mastery die per roll). Entries like Carouse's *The Story* (once per session a story becomes true) and *Cardsharp* (no-roll cheating) are ability-grade fiat, not knacks. The conformance pass on shackles_skills.md was completed 2026-06-10 — all 44 knacks reduced to named facets, with the mastery rule stated once in the Knacks section.
