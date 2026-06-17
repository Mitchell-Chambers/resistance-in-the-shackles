# Part Two — The System

This game runs on the Resistance engine from *Heart: The City Beneath*. Play is a conversation: the GM describes the world, you say what your character does, and dice are rolled only when an action has real stakes and an uncertain outcome. Everything below is the machinery beneath that conversation.

## The Core Roll

When your character attempts something with potential consequences, you roll a pool of ten-sided dice (D10) and **keep the single highest** — you never add dice together. You always roll at least one die. Add another for a relevant **skill**, another for a relevant **domain**, and one more for a **mastery** die if a knack applies (to a maximum of four dice). More dice means a better chance of a high result.

| Highest die | Result |
|---|---|
| **10** | **Critical success.** You get what you wanted, and something extra goes right. Step up your outgoing stress dice. |
| **8–9** | **Success.** You get what you wanted. No stress. |
| **6–7** | **Success at a cost.** You get what you wanted, but you take stress or face a complication. |
| **2–5** | **Failure.** It goes wrong. You take stress; the GM describes what happens. |
| **1** | **Critical failure.** It goes badly wrong. Take double stress. |

### Difficulty

Most actions are **Standard** — roll your pool, keep the highest. When circumstances are against you, the action is harder:

- **Risky** — remove the highest die from your pool before reading the result.
- **Dangerous** — remove the two highest dice.

Good or excellent equipment, a clever plan, or the right preparation can step a Dangerous action down to Risky, or a Risky action down to Standard.

## Stress & Fallout

Stress is the Resistance system's currency of consequence. It is not a hit-point bar. It is the accumulation of harm — physical, supernatural, social, fated, material — that erodes a person until something finally breaks.

When you fail or partially succeed, you **mark stress** to a track. The GM chooses the track based on what is happening in the fiction, not the skill you used, and sets the **stress dice** by severity:

| Dice | Severity |
|---|---|
| **D4** | Minor trouble |
| **D6** | Serious |
| **D8** | Genuinely dangerous |
| **D10** | Catastrophic |

**Protection** — from class abilities, circumstances, or the `Block` tag — reduces the number rolled before it is marked.

Each character has **five stress tracks**: Blood, Tide, Reputation, Luck, and Gold (see [Part Four](04-stress-tracks.md)). The moment you mark stress, the GM rolls a **D12** and compares it to your **total** stress across all tracks:

| D12 vs. total stress | Outcome |
|---|---|
| **Higher than your total** | No fallout. Stress accumulates. |
| **Equal or lower, and the D12 shows 1–6** | **Minor fallout.** Clear all stress in the marked track. |
| **Equal or lower, and the D12 shows 7–12** | **Major fallout.** Clear all stress from **all** tracks. Something has permanently changed. |

Fallout is the point of the system. It ranges from a passing inconvenience to a permanent change that reshapes who your character is. Sometimes it fires immediately; sometimes it lingers for sessions. The fuller your tracks, the likelier the next mark tips you over — so recklessness is rewarded right up until the bill arrives.

> Ships carry their own **Hull** track — structural damage, crew morale, the ability to keep sailing — separate from personal stress. When the Hull breaks, everyone aboard has a very bad day. The Hull rules live in the wider system documents (*Hull & the Ship*).

## Clearing Stress

Each track clears differently, and that is deliberate — see each track's entry in [Part Four](04-stress-tracks.md) for the specifics. In short: **Blood** clears with rest, food, and a surgeon; **Gold** clears with plunder and good trades; **Reputation** clears with public, witnessed deeds (and through bonds and haunts); **Tide** resists clearing and usually needs ritual or arc-length story work; and **Luck** cannot be cleared by rest, coin, or carousing at all — it clears only when its fallout finally fires. Luck is the track that does not forgive. It is the mechanical promise at the centre of this game.

## Timing: No Rounds, No Initiative

Play is paced by the fiction, not by a clock. There are **no rounds, no turns, and no initiative order** — at any scale, including ship-to-ship engagements. Adversaries never "take a turn." They inflict stress through your results (your failures and partial successes) and through the GM's framing when you stall, hide, or do nothing.

### The Four Gates

Every recurring ability is limited by exactly one of these — no other gating currencies exist:

- **Once per situation** — a single contiguous scene of pressure (a fight, a storm, a negotiation, a delicate job). It ends when the pressure breaks; the GM calls the boundary.
- **Once per session** — one real-world sitting of play.
- **Once per journey** — the whole passage between two landmarks, however many sessions it takes.
- **Once per campaign** — a single use across the entire campaign, never refreshed. Where a zenith grants the surviving party a once-per-campaign effect, that single use belongs to the party.

### Legal Durations

Timed effects are scoped to the fiction, never to a number of rounds: *"your next action," "until you next act," "until the end of the situation," "until the end of the session," "until you next make landfall,"* or a fictional condition such as *"while you remain still"* or *"until someone acts on it."* If an effect needs to repeat — a fire spreading, a storm battering a hull, poison working through a body — it repeats through **results**: those caught in it mark the listed stress when they fail or partially succeed against it, and whenever the GM judges it simply finds them.

## Equipment, Resources & Tags

Characters don't track coin or count ammunition. What you carry is described by **stress dice**, **quality**, and **tags**.

### Equipment

When you roll to inflict or remove stress, you roll the dice listed on the equipment. **Without suitable equipment, the default stress dice is D4.** Weapons are tagged with the skill that suits their natural use — **Brave** (desperate, personal melee), **Hunt** (deliberate or ranged violence), **Plunder** (breach-and-board tools). **Journey gear** is tagged **Navigate** and lets you inflict stress on a journey. **Tend gear** removes stress and is split by the track it can treat — **Tend Blood**, **Tend Gold**, **Tend Hull**. *No equipment can remove Tide, Luck, or Reputation stress.*

| Dice | Grade |
|---|---|
| **D4** | Unequipped / improvised |
| **D6** | Civilian |
| **D8** | Professional |
| **D10** | Exotic (rare) |
| **D12** | Legendary (very rare) |

**Quality** is a separate axis from dice size. **Standard** gear follows the rules above; **Good** gear (designed for the task) steps a Risky action to Standard or a Dangerous one to Risky; **Excellent** gear steps Risky *or* Dangerous to Standard; **Renowned** gear is unique and storied, granting its bearer a **knack** for as long as they carry it. Blood protection comes from class advances, not armour — armour is narrative, and only the rare `Block` tag adds protection.

### Resources

Resources are consumable or tradable items of value, noted as *name (value, domain)* — for example, *a chart annotated in a dead pilot's hand (D6, Deepwater)*. Their primary use is to **access haunts and remove stress and fallout** (see the wider *Ports & Haunts* document); some class abilities also spend, destroy, or eat resources of a particular domain. The **Gold** track is your purchasing power: the GM sets a cost (D4 minor, D8 moderate, D12 expensive), and you mark that to Gold or trade resources of equal value.

### Tag Glossary

Tags take effect when a player uses the item, except where noted.

- **BLOCK** — +1 Blood protection.
- **BLOODBOUND** — mark D4 Blood to roll with mastery using this for the rest of the situation.
- **BRUTAL** — roll two stress dice against an adversary, keep the highest. Multiple instances stack.
- **CONDUIT** — mark D4 Tide to roll with mastery using this for the rest of the situation.
- **DANGEROUS** — when you inflict stress and roll the maximum, mark D6 Blood.
- **DEBILITATING** — once per situation, after you inflict stress, the next attack on that target rolls with mastery.
- **DEGENERATING** — if a weapon with this tag hurts you, roll Endure+[Domain] at the end of the situation. Failure: mark D6; partial: D4; success: none.
- **DISTRESSING** — when you inflict stress and roll the maximum, mark D6 Reputation.
- **DOUBLE-BARRELED** — as Reload, but two uses before reloading.
- **EXPENSIVE** — when you inflict stress and roll the maximum, mark D6 Gold.
- **EXTREME RANGE** — usable at extreme range.
- **LIMITED X** — usable X times before it gives out.
- **LOUD** — when you inflict stress and roll the maximum, mark D6 Luck.
- **MADDENING** — stress strikes the mind; against player characters it is marked to Tide. Against adversaries, fiction only.
- **OBSCURING** — bearer and nearby allies reduce incoming and outgoing ranged stress dice by one step.
- **ONE-SHOT** — long to prepare; once per situation.
- **PIERCING** — stress can't be reduced by Blood protection, and adversaries don't benefit from their protection.
- **POINT-BLANK** — as Ranged, but stress steps up at very close range and down at long range.
- **POTENT** — roll two dice for stress *removed*, keep the highest. Stacks.
- **RANGED** — usable at range.
- **RELOAD** — must be reloaded between uses, giving enemies a chance to close or flee.
- **SMOKE** — as Obscuring, but only when used and only around where it was used.
- **SPREAD** — others near the target roll Vanish+Domain to avoid marking stress too (NPCs simply take it).
- **TIRING** — on a failed action with this item, its stress dice drops by one for the rest of the situation.
- **TRUSTY** — roll two dice for stress against a *journey*, keep the highest. Stacks.
- **UNRELIABLE** — on a failed action, it can't be used again this situation (ashore) or this journey (at sea).
- **WYRD** — when you inflict stress and roll the maximum, mark D6 Tide.
