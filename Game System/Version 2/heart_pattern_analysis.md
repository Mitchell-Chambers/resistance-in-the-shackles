# Heart vs Version 2 — Pattern Analysis & Conversion Pass

*Fresh-eyes comparison of the nine Heart core classes (Reference/) against the ten Version 2 classes, read as standalone texts. 2026-06-10.*

---

## Part 1 — Pattern Findings

### Verbosity: not a problem

Average words per ability, player-facing text only (design notes excluded):

| Tier | Heart | Version 2 |
|---|---|---|
| Cores | 73.0 | 71.6 |
| Minors | 39.2 | 37.6 |
| Majors | 162.3 | 150.6 |
| Zeniths | 175.9 | 182.6 |

Version 2 has fully internalized Heart's word budget. No trimming needed for length alone.

### The real divergence: Heart sells odds, Version 2 sells guarantees

Certainty language ("without a roll," "you always," "the GM tells you," "never") in player-facing text: Heart's nine classes contain roughly **1–5 instances total**; Version 2's ten contain **49**.

Heart's grammar of power is: roll with mastery, gain a tag, shift a dice size, mark stress elsewhere, once per session ask one question. Even its strongest minors (Marked for Death, Liar's Burden) route through dice or cost. Version 2's original material constantly bypasses the dice instead. Same word count — but Heart spends words on fictional colour (spit that hardens to glue, grave-dirt under fingernails) while Version 2 spends them on binding promises.

In a Resistance game this is doubly costly: no roll → no stress → no fallout → no doom engine. The system was chosen to deliver the inevitable fall; guarantee-dense classes opt out of it.

### Within-class similarity

Heart scatters each class's minors across unrelated spheres — every class gets a combat trick, a social trick, an exploration trick, a weird utility. Several Version 2 classes stack 4–6 abilities that are functionally the same verb:

- **Sharper**: The Web, Cold Read, Dead Drop Network, Bribed Harbour, Everybody Owes, What the Walls Heard — six "press button, GM reveals secret."
- **Sin Bosun**: Chart and Prayer, Read the Omen, Star-Reader, Weatherwise, Eyes of the Faithful — five flavors of free true information.
- **Sawbone**: Same Saw, Triage, Carpenter's Eye, Salvage Instinct — four "GM tells you the assessment."
- **Daredevil**: Always a Way Out, Vanishing Act, Impossible Route, Coastwise, Smoke and Shadow — five escapes; Knife Act / Knife Storm overlap.

### Power: localized in original material

Ported abilities are Heart-grade because they inherit Heart's costs. Drift concentrates in Pass-1-survivor originals, in two forms: **minors priced as majors** (Leverage, Knife Act, Ghol-Gan Fire) and **uncosted actives** (The Form, Read the Fighter, Perfect Shot, The Killing Word). Heart's actives are priced in stress or a casting roll; many V2 originals are gated only by frequency.

### Looseness: zenith-grade fiat pushed down the ladder

Heart confines "negotiate reality with the GM" to zeniths. V2 puts standing adjudication contracts in majors and cores: Grand Project, The Read, Perfect Lie, Violence as Argument, Naval Law. Individually playable; collectively the GM holds a dozen narrative contracts Heart never asks for.

### What matches Heart well

Zeniths are the best tier in the set — scale, cost, and "to activate this ability, die" grammar all faithful; several (Down with the Ship, The Grift Eternal) improve on their models. The protection matrix and forbidden-skill discipline exceed Heart's own consistency.

---

## Part 2 — The Conversion Rule

> **Anywhere an original ability says "without a roll," "you always know," or "the GM tells you," convert it to one of: (a) roll with mastery, (b) a once-per-session question, or (c) a stress cost.**

Heart's three legal shapes for information/certainty:

1. **Odds**: "roll with mastery" (Marked for Death, Righteous Rhetoric, Creative Acquisitions)
2. **Rationed question**: "once per session, ask the GM…" (Lost It All, Twisting Territory, Marshal)
3. **Priced effect**: "mark D4 stress to…" (On the Run, Invidious Spectre, Chimeric Strain)

Trivial sensory/utility colour (see in the dark, dig with bare hands, smell magic) may stay free — Heart does this too. The test: does the guarantee replace a roll the table would otherwise make at stake?

---

## Part 3 — Class-by-Class Flags

Labels: **CONVERT** = breaks Heart grammar, apply the rule. **TRIM** = overstuffed or borderline; cut a rider or add a gate. **WATCH** = defensible, monitor in play. Ported abilities not listed are clean.

### Castaway *(Cleaver port — light flags)*

| Ability | Issue | Suggested fix |
|---|---|---|
| FERAL TRACKING | "Follow any trail… without a roll" | **CONVERT** — roll with mastery when tracking; keep the deliberate/careless read as the free colour |
| SALT-STILL | "Cannot be detected… you choose when to be noticed" — absolute | **CONVERT** — while still in natural terrain, Vanish rolls are never Risky (Mark of Shadow grammar) |
| SCAVENGED ARSENAL | Skill + no-roll crafting + D6 improvised weapons — three riders | **TRIM** — keep skill + D6 improvised (Quartermaster Training precedent); crafting under pressure takes a roll |
| RUIN-WALKER | "No stress from passive ruin hazards" + "always know where you are" — double guarantee | **TRIM** — pick one; hazard immunity becomes "the first hazard each delve gives you warning enough to act" (also duplicates Chronicler's RUIN SOVEREIGN — see Part 4) |

### Tidecaller *(Witch port — cleanest class)*

| Ability | Issue | Suggested fix |
|---|---|---|
| THE PACT / FAMILIAR | D3 dice — Heart never rolls D3 | **TRIM** — standardize to D4 |
| HEX SIGHT | "You always know… can identify… without a roll" | **CONVERT** — auto-sense that magic is present (colour-grade); identifying its nature is a Reckon roll or once per situation |
| STORM-DEBT | Once/session weather working, "costs nothing" | **WATCH** — in-grade with Call of the Wild if scale stays scene-dressing; add a Tide cost if it starts winning engagements |

### Corsair *(Hound port)*

| Ability | Issue | Suggested fix |
|---|---|---|
| VIOLENCE AS ARGUMENT (core) | "The GM treats it as carrying the weight of action" — undefined contract | **CONVERT** — threats against those who know your history roll with mastery; keep the once-per-session Reputation clear |
| DREAD NAME | "They must act on that information" — no roll, open-ended compulsion | **CONVERT** — give it Staredown grammar (the Errant's DUELLIST'S GAZE already does this correctly); PREEMPTIVE SURRENDER's GM-roll is the right shape |
| NO QUARTER (sub) | "They cannot simply disengage" — fiat | **TRIM** — disengaging requires a successful roll against you |
| THE UNSTOPPABLE + ON YOUR FEET | Already flagged in design notes | **WATCH** — Corsair has more Blood protection than the Hound; fallout may not land often enough to fuel it |

### Powder Mage *(Junk Mage port)*

| Ability | Issue | Suggested fix |
|---|---|---|
| POWDER BOND (core) | Detonate "without a roll" — includes powder carried by adversaries | **TRIM** — unattended powder detonates freely (identity); powder on a person is an attack: roll, or use SPARK IN THE CHAMBER's profile |
| GHOL-GAN FIRE | Domain + three ammo types — overstuffed minor | **TRIM** — know one round type; the other two become knacks or a second take of the advance |
| SMOKE AND MIRRORS | "Reposition unseen… without a roll" | **CONVERT** — after firing, roll Vanish with mastery |
| SHATTERING LOAD (sub) | Protection to 0 — already flagged in notes | **TRIM** — reduce by 2 |
| PERFECT SHOT (sub) | "Automatically succeeds and deals maximum stress" | **CONVERT** — roll with mastery, stress dice +2 steps; the duel already gates it |
| READ THE DRAW (sub) | "Always know" + free interrupt | **TRIM** — once per duel |
| POWDER KEG | D10 to all, but priced (D6 self) and once/session | **WATCH** — costed correctly; monitor scale |

### Sharper *(heaviest information-economy flags)*

| Ability | Issue | Suggested fix |
|---|---|---|
| THE WEB (core) | 3 free taps/session; "they may ask for something in return" is soft | **TRIM** — keep the taps but harden the price: each use marks D4 stress to Gold or Reputation, or creates a tracked debt with teeth |
| COLD READ | GM tells three things, free, every first meeting | **CONVERT** — once per session free; otherwise roll Reckon+Port |
| CARDSHARP'S FINGERS | "Can lift anything… rig any game" | **CONVERT** — use the Daredevil's PICKPOCKET grammar (Vanish roll vs watchers, partial = noticed) — that version is the model |
| EVERY ROOM'S NATIVE | "Never take stress from social environments" | **CONVERT** — +1 Reputation protection in social scenes, or mastery on blending in |
| LEVERAGE | Once/arc total compliance from a powerful NPC — **as a minor** | **CONVERT** — this is a major in minor's clothing. Either promote it, or the target acts under your direction for one scene and the roll still happens for anything self-destructive |
| THE PERFECT LIE | "Holds without rolls" indefinitely | **TRIM** — holds without rolls until actively investigated; then you roll with mastery. Or upkeep: mark D4 Luck per session maintained |
| THE KILLING WORD | Automatic Major Reputation fallout, once/arc | **CONVERT** — inflicts D10 Reputation stress with fallout rolled normally, or keep the auto-fallout but price it: mark D6 Luck — fate notices authors |
| THE BACK ROOM | "You know everything that happens inside its walls" | **TRIM** — base grants mastery on social actions inside; omniscience is what the WHAT THE WALLS HEARD sub is for (currently redundant with its own base) |

### Daredevil *(most conversions needed; the doom-engine bypass class)*

| Ability | Issue | Suggested fix |
|---|---|---|
| ALWAYS A WAY OUT (core) | No-roll escape, once/situation | **TRIM** — keep (it's the thesis) but price it: mark D4 Luck when used, or you always leave something behind — GM's choice what |
| MOMENTUM (core) | Free move rides on a successful roll | **Model** — keep; this is Heart-shaped |
| KNIFE ACT | Skill + auto-hit called shots + D8 + infinite ammo — four riders | **TRIM** — skill + thrown blades (Hunt D6, Ranged, Brutal); called shots roll with mastery |
| MISDIRECTION | Next action "requires no roll, and no one present remembers" | **CONVERT** — next action rolls with mastery; the memory-wipe is supernatural-grade, cut it. (Own design notes already flag this) |
| COASTWISE | Evade an actively searching coastline "without a roll" | **CONVERT** — roll with mastery |
| SMOKE AND SHADOW | "Cannot be pursued out of a social scene" | **CONVERT** — pursuers' attempts are Risky |
| RIGGING RAT | Three riders; movement overlaps ACROBAT | **TRIM** — keep high-ground + drop-attack Brutal; no-roll rigging movement is what Acrobat already covers |
| THE IMPOSSIBLE ROUTE | "You take it. It works." | **CONVERT** — reuse MOMENTUM's own grammar: roll with mastery; on a failure you still arrive, but something goes wrong on the way |
| THE READ | "Narrate how the next minute unfolds. It happens as described" — player authorship of GM turf | **CONVERT** — becomes a question: GM tells you how the next minute will unfold; you and allies roll with mastery acting on it. THE OPENING's auto-max-stress → mastery + 1 dice step |
| THE VANISHING ACT | No-roll disappearance, even mid-combat | **TRIM** — price it: mark D4 Luck, or partial-success table (you're gone, but you left something/someone) |
| KNIFE STORM | "Every opponent must roll to avoid" — inverts Heart's player-facing rolls | **CONVERT** — weapon profile: (Hunt D6, Spread), once per situation. ENCORE doubling: **WATCH** |
| LEAVE A DOUBLE (sub) | D3 rounds | **TRIM** — D4, or "one exchange" |

### Sin Bosun *(information stack)*

| Ability | Issue | Suggested fix |
|---|---|---|
| THE CHART AND THE PRAYER (core) | Free true info on every consult + once/journey auto-success | **TRIM** — info: once per session free, then by roll. Auto-success → "functions as a D6 boon" or roll with mastery (Heart has no auto-success navigation) |
| READ THE OMEN | Free true omen **once per scene** | **CONVERT** — once per session; per-scene is the most frequent free-info clock in the set |
| WEATHERWISE | D6 days of accurate forecast, no roll | **WATCH** — low-stakes utility, Custodian-grade; fine unless weather is a journey threat, then make it a roll |
| EYES OF THE FAITHFUL (sub) | Another free-info tap on a class that has five | **TRIM** — fold into the church's once-per-visit benefits (see Part 4 redundancy note) |
| THE PERFECT COURSE | "The passage succeeds without incident, regardless" | **TRIM** — it deletes journey content once per session. On success the passage functions as a major boon (D8), or you choose the one incident you do face |
| STORM CALLING | Priced (D8 Tide), rolled, bounded | **Model** — this is what a big V2 active should look like |

### Sawbone

| Ability | Issue | Suggested fix |
|---|---|---|
| THE SAME SAW (core) | Standing free diagnosis | **WATCH** — acceptable identity colour, but route "what will fail next" through a roll when the answer has stakes |
| THE GRAND PROJECT (core) | Pure GM contract | **TRIM** — not a conversion; needs the milestone-pricing paragraph the design notes already call for |
| TRIAGE | "Without a roll" — and redundant with Same Saw | **TRIM** — fold into THE SAME SAW or replace with a different sphere of perk |
| CARPENTER'S EYE | "Immediately know… fastest way to bring it down" | **CONVERT** — mastery on structural assessment and demolition; knowing weak points is fine, exploiting them still rolls |
| AMPUTATION | Removes Major fallout **and clears all Blood stress** in one action, as a minor | **TRIM** — fallout removed, stress remains (the limb is the price, but Heart never clears a full track from a minor) |
| SABOTEUR (sub) | "Without a roll… always looks like an accident" | **CONVERT** — roll with mastery; "looks like an accident" on a full success |
| THE IMPOSSIBLE REPAIR (sub) | Clear **all** Hull stress once/session | **TRIM** — clear D8 Hull |
| THE IMPOSSIBLE SURGERY (sub) | Already flagged in notes | **TRIM** — Minor fallout only, or once per arc |
| NOT TODAY | "The bill arrives later" is soft | **TRIM** — codify: mark D6 stress to two resistances of the GM's choice when the bill lands |

### Chronicler *(Junk Mage port — fairly clean)*

| Ability | Issue | Suggested fix |
|---|---|---|
| OBJECT READING | Full provenance, free, per object | **TRIM** — once per session free; otherwise a Reckon+Arcane roll |
| THE NARROW HOUR (sub) | GM pre-reveals an opponent's action, once per situation | **CONVERT** — own notes flag it; make it a mastery grant on acting against that opponent |
| RUIN SOVEREIGN | "Never trigger passive hazards" + automatic peer status | **TRIM** — hazards: warning enough to act (keep); peer status: until you give cause is fine, but note the overlap with Castaway's RUIN-WALKER |
| THE SPELL BEYOND MEMORY | D8 Tide, once per arc | **Model** — correctly priced wildcard |

### Errant *(strongest cores in the set)*

| Ability | Issue | Suggested fix |
|---|---|---|
| THE FORM (core) | Permanent +1 stress step **and** immunity to opponent-skill difficulty — stronger than any Heart core | **CONVERT** — keep the dice step in form-conditions (the condition is the gate), drop the difficulty immunity, or make the immunity once per situation. One benefit, not two |
| READ THE FIGHTER (core) | Three free facts, no roll, no gate — own notes flag it | **CONVERT** — once per situation, or roll Reckon; on success the GM gives all three |
| COLONIAL PASSAGE | "Without a roll" baseline | **CONVERT** — invert the existing structure: roll normally, with mastery always (currently mastery is the *scrutiny* case, which is backwards) |
| NAVAL LAW | "The GM confirms it is real and incorporates its consequences" | **CONVERT** — reframe as Heart's question grammar: once per session, ask the GM "what legal mechanism applies here?" — the GM answers honestly |
| THE POINT THAT ENDS ARGUMENTS | "On **any** success — partial or full — the target yields," once/session | **TRIM** — full success ends it; partial success they yield at a price (you mark stress, or they set one condition) |
| THE REPUTATION OF THE BLADE | "Fighters must succeed on a Brave action to engage you" — NPCs rolling, inverting player-facing dice | **CONVERT** — fiction-first: fighters who know your record find reasons to delay unless something forces them; or once per session you make the roll to face them down |

---

## Part 4 — Cross-Cutting Notes

**Within-class redundancy to consolidate.** Sharper info-taps (six), Sin Bosun omens (five), Sawbone assessments (four), Daredevil escapes (five). Suggested budget: at most **two** free-information abilities per class — one core-grade, one minor — with everything else converted to rolls or folded. Freed minor slots should buy abilities in spheres the class currently lacks (Heart's scatter principle: every class gets a trick outside its theme).

**Cross-class duplication.** RUIN-WALKER (Castaway) vs RUIN SOVEREIGN (Chronicler) grant near-identical hazard immunity; PICKPOCKET (Daredevil) vs CARDSHARP'S FINGERS (Sharper) are the same ability at two power levels — keep the Daredevil's rolled version as the template for both.

**Roll-economy inversions.** Heart rolls are player-facing. KNIFE STORM ("every opponent must roll") and REPUTATION OF THE BLADE ("fighters must succeed on a Brave action") put dice in NPC hands. Convert to weapon profiles or player rolls.

**Dice and gate vocabulary.** D3s (The Pact, Familiar, Leave a Double) don't exist in Heart — standardize to D4. Gating currencies have multiplied: Heart uses session/situation/delve only; V2 adds arc, port visit, scene, duel, naval engagement. Per-arc is acceptable (it's doing zenith-adjacent work) but pick a canonical list and define each in the core rules. Verify nonstandard tags (e.g. Degenerating in KNIFE STORM's Specialty Load) against the tag glossary.

**Core count.** All ten V2 classes have two cores; Heart varies (Heretic, Hound and Vermissian Knight have one). Several V2 classes pair an engine core *with* an oracle core (Sin Bosun, Sawbone, Errant, Sharper) — each is individually fine, but the pairing is where most certainty-stacking lives. When converting, the oracle core is usually the one to soften.

**Models to imitate from V2's own pages.** MOMENTUM, STORM CALLING, THE SPELL BEYOND MEMORY, PICKPOCKET, and every directly ported major. The set already contains its own style guide.
