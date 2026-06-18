# Class Grant Audit — Skill & Domain Duplicates

**Scope:** Every class file in `System Reference/06-classes/` except `sawbone.md` (already fixed) and `README.md`.
**Audited:** Castaway, Chronicler, Corsair, Daredevil, Errant, Powder Mage, Sharper, Sin Bosun, Tidecaller.
**Date:** 2026-06-18

## What was checked

For each class, every ability that grants a skill or domain — core abilities, minor abilities, and the sub-options (MINORs) under major abilities — was extracted and compared, looking for:

1. **Duplicate skill grants** — two+ abilities that each grant the same skill (the Sawbone bug).
2. **Duplicate domain grants** — two+ abilities that each grant the same domain.
3. **Redundant-with-starting grants** — a minor that grants the class's own starting SKILL or DOMAIN.
4. **Self-duplicating choice lists** — a "gain access to one of the following" list that offers a skill/domain the class already grants for free or starts with (low-priority, by design).

## Headline result

**No class has the Sawbone-style bug.** Across all nine files there are **zero duplicate skill grants, zero duplicate domain grants, and zero redundant-with-starting grants.** Every direct skill grant and every direct domain grant within each class points at a distinct, non-starting skill or domain. The double-grant problem appears to have been isolated to Sawbone.

The only systematic observation is item 4 (the generic choice lists), which is present in identical form in every class and reads as deliberate design rather than error. It is documented once below and noted per class.

---

## Castaway

**Core:** SKILL Endure · DOMAIN Wilderness
**Skill grants:** Brave (THE CHANGED PALATE), Hunt (FERAL TRACKING), Plunder (SCAVENGED ARSENAL), Tend (CRAB AND ROOT), Vanish (SALT-STILL) — all distinct.
**Domain grants:** Arcane (SPEAKING TO STRAYS), Deepwater (DESPERATE MEASURES), Ruins (RUIN-WALKER) — all distinct.

**No errors.** Clean of duplicate skills, duplicate domains, and redundant-with-starting grants.

One thing worth a glance (not an error): both `FERAL TRACKING` ("Gain the Hunt skill.") and the major `THE WILD HUNT` ("Those who commune **gain the Hunt skill if they don't already have it**…") reference Hunt. This is *not* a dead duplicate — THE WILD HUNT grants Hunt to **journey participants** as a party buff and already self-guards with "if they don't already have it." No fix needed.

- Observation (item 4): `GUT INSTINCT` lists the starting skill **Endure**; `INTERIOR` lists the starting domain **Wilderness**. Both lists also re-offer several free-granted options. By design.

## Chronicler

**Core:** SKILL Reckon · DOMAIN Ruins
**Skill grants:** Tend (THE ARCHIVE, core), Deceive (PROVENANCE), Navigate (THE DIG MAPPED), Plunder (THE EXCAVATOR'S ANSWER) — all distinct.
**Domain grants:** Arcane (TONGUE OF THE DEAD), Colonial (ACADEMIC NETWORK), Faith (THE OLD WAY), Shallows (GRAVE GOODS) — all distinct.

**No errors.** Clean.

- Observation (item 4): `FIELD RESEARCH` lists the starting skill **Reckon** and also re-offers Tend/Deceive/Navigate/Plunder (all granted free elsewhere). `COMPARATIVE STUDIES` lists the starting domain **Ruins** and re-offers Arcane/Shallows/Faith/Colonial. By design.

## Corsair

**Core:** SKILL Brave · DOMAIN Deepwater
**Skill grants:** Command (BOARDING MASTER), Endure (IRON STOMACH), Hunt (NOTCHES ON THE HILT), Plunder (THE KILLING GROUND), Tend (OLD SALT'S STITCHES) — all distinct.
**Domain grants:** Outlaw (WHAT'S MINE), Port (HARBOUR LEGEND), Shallows (RAIDER'S COVES) — all distinct.

**No errors.** Clean.

- Observation (item 4): `FIGHTING TRIM` lists the starting skill **Brave**; `WHERE THE WIND TAKES YOU` lists the starting domain **Deepwater**. Both lists re-offer free-granted options. By design.

## Daredevil

**Core:** SKILL Vanish · DOMAIN Outlaw
**Skill grants:** Brave (ACROBAT), Carouse (SMOKE AND SHADOW), Deceive (MISDIRECTION), Hunt (KNIFE ACT), Reckon (PICKPOCKET) — all distinct.
**Domain grants:** Colonial (STREET-LEARNED), Deepwater (RIGGING RAT), Shallows (COASTWISE) — all distinct.

**No errors.** Clean.

- Observation (item 4): `THE PRESTIGE` lists the starting skill **Vanish**; `THE ROVING LIFE` lists the starting domain **Outlaw**. Both re-offer free-granted options. By design.

## Errant

**Core:** SKILL Hunt · DOMAIN Colonial
**Skill grants:** Brave (SECOND STEEL), Command (CHALLENGE), Deceive (COLONIAL PASSAGE), Endure (MEASURED THREAT), Reckon (NAVAL LAW) — all distinct.
**Domain grants:** Faith (SWORN ORDER), Outlaw (THE CODE DUELLO), Port (FORM PERFECT) — all distinct.

**No errors.** Clean.

- Observation (item 4): `ACADEMY TRAINING` lists the starting skill **Hunt**; `A WIDER EDUCATION` lists the starting domain **Colonial**. Both re-offer free-granted options. By design.

## Powder Mage

**Core:** SKILL Hunt · DOMAIN Arcane
**Skill grants:** Brave (QUICK DRAW), Reckon (CALLED SHOT), Tend (SLOW MATCH), Vanish (SMOKE AND MIRRORS) — all distinct.
**Domain grants:** Colonial (NAVY GUNNER), Faith (FALSE THUNDER), Outlaw (THE POWDER TRADE), Ruins (GHOL-GAN FIRE) — all distinct.

**No errors.** Clean.

- Observation (item 4): `BY ANY MEANS` lists the starting skill **Hunt**; `BEEN EVERYWHERE` lists the starting domain **Arcane**. Both re-offer free-granted options. By design.

## Sharper

**Core:** SKILL Deceive · DOMAIN Port
**Skill grants:** Carouse (EVERY ROOM'S NATIVE), Command (THE LONG CON'S END), Hunt (THE SLEEVE), Plunder (CARDSHARP'S FINGERS), Reckon (THE TELL), Vanish (FALSE FACE) — all distinct.
**Domain grants:** Colonial (THE BRIBED HARBOUR), Outlaw (NOSE FOR GOLD) — all distinct.

**No errors.** Clean.

- Observation (item 4): `THE LONG GAME` lists the starting skill **Deceive**; `OLD HAUNTS` lists the starting domain **Port**. Both re-offer free-granted options. By design.

## Sin Bosun

**Core:** SKILL Navigate · DOMAIN Faith
**Skill grants:** Brave (BLESSED STEEL), Carouse (SERMON ON THE DECK), Command (SCRIPTURE OF SALT), Reckon (LIAR'S BURDEN), Tend (DEAD RECKONING) — all distinct.
**Domain grants:** Deepwater (WEATHERWISE), Outlaw (CONFESSOR), Port (LAST RITES) — all distinct.

**No errors.** Clean.

- Observation (item 4): `THE GOD'S GIFTS` lists the starting skill **Navigate**; `PILGRIM ROUTES` lists the starting domain **Faith**. Both re-offer free-granted options. By design.

## Tidecaller

**Core:** SKILL Command · DOMAIN Arcane
**Skill grants:** Endure (TIDEBLOOD), Hunt (FAMILIAR), Reckon (HEX SIGHT), Tend (WITCH'S HANDS), Vanish (BLOOD-QUIET) — all distinct.
**Domain grants:** Deepwater (STORM-DEBT), Faith (DEEPSPEAK), Ruins (THE DROWNED PLACES) — all distinct.

**No errors.** Clean.

- Observation (item 4): `SALT-TAUGHT` lists the starting skill **Command**; `OLD WATERS` lists the starting domain **Arcane**. Both re-offer free-granted options. By design.

---

## Summary table

| Class | Dup. skill | Dup. domain | Redundant-with-start | Verdict |
|---|---|---|---|---|
| Castaway | none | none | none | Clean |
| Chronicler | none | none | none | Clean |
| Corsair | none | none | none | Clean |
| Daredevil | none | none | none | Clean |
| Errant | none | none | none | Clean |
| Powder Mage | none | none | none | Clean |
| Sharper | none | none | none | Clean |
| Sin Bosun | none | none | none | Clean |
| Tidecaller | none | none | none | Clean |

## Note on the choice lists (item 4)

Every class carries two generic advances — one "gain access to one of the following **skills**" and one "…**domains**." In **all nine** classes, each list includes the class's own **starting** skill/domain *and* several skills/domains the class already grants for free through named minors. Choosing an already-owned option would waste the advance, but in practice a player simply picks an option they don't yet have, so the list functions as intended. This pattern is uniform across the line (and matches the Heart "core advance" convention), so it reads as deliberate rather than a per-class error. Flagged here only for completeness; **no change recommended** unless you want to trim each list down to options the class can't already obtain.

## Bottom line

The Sawbone double-Brave issue does **not** recur anywhere in the other nine classes. No fixes are required. The only thing for you to decide is whether the generic choice lists (item 4) should be tightened — a stylistic call, not a bug.
