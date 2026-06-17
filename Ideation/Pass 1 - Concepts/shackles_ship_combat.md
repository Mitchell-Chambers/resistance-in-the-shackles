# The Shackles — Ship Combat

> *A ship in battle is not a weapon you aim. She is a living thing the sea is trying to kill, and your only job is to hold her together one round longer than they can hold theirs.*

**Status:** Pass 1 concept. Working title: *Where the Chaos Lands*.

---

## Design Goals

1. **Kill the station problem.** Stations make naval combat rote because they fix each player's verb — the helmsman rolls "steer" forever. This system randomises *who* acts and frees *what* they do.
2. **One mechanism for chase, flight, and battle.** Pursuit, escape, and the cannon duel are all the same tug-of-war, not separate subsystems.
3. **The ship is a delve.** The engagement is something happening *to* the vessel. The crew doesn't drive the fight — they resist the chaos that would slow her, break her, or take her. Pure Resistance posture: you hold her together, and eventually you can't.
4. **Boarding is the handoff.** The ship system's whole job is to deliver the crew onto a deck, carrying every point of stress the engagement cost them, where normal character-scale play takes over.

---

## The Engagement Ladder

Every engagement lives on a single range ladder:

```
ESCAPED ← Open Water ↔ Gun Range ↔ Close Quarters ↔ Grappled → BOARDING
```

| Band | What's Happening |
|---|---|
| **Open Water** | Hull-down on the horizon. A contest of sail, wind, and nerve. No shot lands here. |
| **Gun Range** | Long guns speak. Chain-shot for the rigging, round shot for the hull. |
| **Close Quarters** | Point-blank broadsides, grapeshot, fouled lines, fire risk everywhere. |
| **Grappled** | Hulls kiss. Grapples bite. The next thing that happens is boarding. |

The pursuer pushes the ladder right; the quarry pushes it left. Push past Open Water and the quarry **escapes**. Reach Grappled and the engagement ends — **boarding begins** (see below). A stalemate in the middle bands *is* the cannon duel; it doesn't need its own phase, it emerges whenever neither ship can win the ladder.

**What moves the ladder:** nobody ever rolls "I sail fast." Both ships are being hammered by sea and shot, and *the one that handles its chaos better is the one that closes or escapes.* You roll "the topsail's torn loose at the worst possible moment — save it," and if you do, she keeps her speed and the ladder moves your way.

---

## The Round

1. **Position.** Each player declares where they are on the ship (see Locations). Move freely between rounds; moving *during* a crisis costs (see Seizing the Spotlight).
2. **The GM frames the band.** What the enemy is doing, what the sea is doing — fiction only, no enemy rolls.
3. **Chaos roll.** The GM rolls the D12. Chaos lands at the indicated location.
4. **The crisis.** The GM names what happens there, flavoured by the current band (see crisis table). The player at that location responds however they can justify — any skill, any approach. *The location constrains the fiction; it never constrains the verb.*
5. **Resolve.**

| Result | Effect |
|---|---|
| **Success** | The crisis is mastered. The ship holds her way — the ladder moves one step in your favour. |
| **Critical / success at cost paid in style** | As success, **plus press the advantage**: a free aggressive beat — loose a broadside (Hull stress to them), foul their rudder, cut their grapples, rake their deck. Aggression is the *reward* for mastering chaos, not a separate action economy. |
| **Partial** | The crisis is contained but it cost you — mark Hull stress *or* the ladder slips one step against you (GM's call from fiction). Personal stress may also land (splinters are Blood; the bargain you whispered to the wind is Tide). |
| **Failure** | Mark Hull stress *and* the ladder slips. The crisis may compound into next round's fiction. |

6. **Unmanned locations.** If chaos lands where nobody stands, there is no roll. The ship takes the Hull stress at a **stepped-up die**, and the ladder slips. This is the tactical layer: four crew, five locations, choose what you leave to fate — and the right answer changes by band (nobody needs the gun bay at Open Water; everyone wishes they were on deck at Grappled).

---

## Locations

Chaos strikes *places*, not job titles. Base D12 mapping:

| D12 | Location | The Kind of Chaos That Lands Here |
|---|---|---|
| 1–2 | **Helm** | The swell slams the rudder; shoals; the enemy's wake; a steering chain parts. |
| 3–4 | **Rigging** | Torn sails, snapped stays, chain-shot overhead, a falling spar, a man overboard. |
| 5–6 | **Gun Bay** | A loose hot coal, a jammed carriage, a misfire, smoke-blind crews, the magazine. |
| 7–8 | **Deck** | Fire, grapples, sharpshooters, wreckage fouling the lines, panicking crew. |
| 9–10 | **Below Decks** | Sprung planks, rising water, shifting cargo, the wounded, things in the bilge. |
| 11–12 | **Quarterdeck** | *Opportunity, not crisis.* The one place chaos arrives as an opening — a gap in their line, their helmsman exposed, the wind about to shift. Whoever stands here gets a proactive beat. |

- **Doubling up:** two crew at one location = the second assists (Heart's normal help rules). You're safer there and absent elsewhere.
- **Station abilities reshape the die.** This is what class/calling abilities and ship fittings do in this system: widen your range ("the Gun Bay is 5–7 for you"), trade numbers, reroll the chaos die, or make an unmanned location count as manned once per engagement. Stations affect *weighting*, never the verb.
- **NPC crew** can hold a location: they prevent the stepped-up die for unmanned chaos but never roll — the crisis auto-resolves as a Partial. Warm bodies buy time; they don't win engagements.

### Crisis Texture by Band

| | Open Water | Gun Range | Close Quarters |
|---|---|---|---|
| **Helm** | Crosscurrent, reef, dead wind | Turning into / out of their arc | Collision course, fouled rudder |
| **Rigging** | A stay parts under full press | Chain-shot through the tops | Their marines firing up at you |
| **Gun Bay** | Stow it or lose it in the swell | The long duel — heat, smoke, misfires | Grapeshot through the ports |
| **Deck** | Wave over the bow, lost gear | Splinter storm | Fire, grapples, first boarders |
| **Below** | The leak you already had | Shot below the waterline | Water gaining on the pumps |

---

## Seizing the Spotlight

The chaos die chose someone else — but you see the crisis and you *move*. Any player may take a crisis that landed at another location by **marking Luck stress** (D4 if adjacent, D6 across the ship) and describing how they physically get there: swinging on a halyard, vaulting the rail, shouldering through the smoke.

This is the thematic engine of the whole system. Fate didn't choose you; you leapt into its path, and the Shackles always collects on audacity. A crew that keeps seizing the spotlight wins more engagements and accrues the Luck debt that brings everything down later. Ship combat becomes a Luck economy.

Class abilities that "force the moment" (Corsair's Boarding Action, etc.) should hook here — guaranteeing the spotlight at the moment the class was built for, with or without the Luck cost.

---

## Hull Stress

The ship has a single **Hull** track (already assumed by V2: Storm Calling, Boarding Action, Powder Keg, Living Ship). It works like any other track: mark stress, GM rolls the D12 against the total, fallout fires.

Sketch fallout (to be developed into a full table):

- **Minor** *(clear Hull)* — **Fire on Deck** (someone must answer it next round or it spreads — D6 Hull, immediate), **Sprung Leak** (Below Decks counts as unmanned until repaired), **Tangled Wreckage** (the ladder cannot move in your favour until cut away).
- **Major** *(something permanently changed)* — **The Mast Falls** (the ladder locks: no escape, no pursuit — the engagement *will* end at Grappled), **Shot Below the Waterline** (she's sinking; every round, D6 Hull), **Magazine Flash** (everyone in the Gun Bay marks D8 Blood; the guns are done).

Major Hull fallout is how engagements end badly *short* of boarding — sinking, dismasting, striking the colours.

---

## The Enemy Vessel

The enemy ship never rolls. Heart-adversary style, it is defined by three numbers and some tags:

| Vessel | Chaos Dice It Deals | Hull Track | Tags (examples) |
|---|---|---|---|
| Fishing ketch | D4 | 4 | *Unarmed, Fast in Shallows* |
| Free Captain's sloop | D6 | 6 | *Weatherly* (wins ties on the ladder at Open Water) |
| Brig of the lesser lords | D8 | 8 | *Carronades* (steps up Gun Bay/Deck chaos at Close Quarters) |
| Chelish frigate | D10 | 12 | *Disciplined Gunnery* (its Press-the-Advantage hits trigger on your partials too), *Marines* |

Its aggression is expressed entirely through the *size and flavour* of the chaos it adds to your rounds; your Press-the-Advantage beats are how you hurt its Hull track.

---

## Boarding

There is no boarding subsystem. When the ladder reaches Grappled, the ship layer ends and character-scale play begins — on a deck, with everything the engagement cost still marked. The Blood from the splinter storm, the Tide from the bargain that caught the wind, the Luck from every seized spotlight: all of it walks across the planks with you. The engagement doesn't decide the fight; it decides *what shape you're in when the fight becomes personal.*

The GM should let the engagement's wreckage set the boarding scene: the fire still burning, the fallen spar bridging the two decks, the flooded hold someone gets thrown into.

---

## Open Questions / Watch-List

1. **Spotlight famine.** Short engagement, five players — someone may never act. Option: chaos die draws without replacement within a band (re-arm on band change). Or accept it; Seizing the Spotlight exists.
2. **Ladder length / pacing.** Is one step per success too fast? A brig-vs-brig fight might want each band to be a short track (2–3 successes to cross) so the cannon duel breathes.
3. **Multi-ship engagements.** Probably: one ladder per enemy vessel, one chaos roll per round total (chaos doesn't scale with enemies; *consequences* do). Needs a playtest.
4. **Weather and sea as third party.** A storm could roll its own chaos die — both ships suffer. Hooks into Journey rules (Wildsea) for where engagements begin.
5. **Quarterdeck balance.** Is a 2-in-12 proactive slot enough to make the captain's spot desirable without making it the only correct place to stand?
6. **Journey interface.** How an engagement starts (sighted on a journey leg, weather gauge, who holds it) should come from the Journey rules — define the handoff in both directions.
7. **Hull fallout table** needs a full Minor/Major write-up matching the stress-track doc's format.
8. **Locations on different hulls.** A ketch has no gun bay; a man-o-war might split Deck into fore and aft. Location maps could be per-ship, which makes ship choice mechanically real.
