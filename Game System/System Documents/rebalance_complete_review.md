# Rebalance — Complete Review

*Capstone review of the whole rebalancing pass: the framework adopted, every class change drafted, the recomputed set-level distribution, and verification against the three goals — **combat floor met everywhere, spikes resolved, healing spread.** Compared throughout to Heart and to the pre-change V4.*

---

## 1. What we decided (framework)

- **The Median Class** (`the_median_class.md`) — identity is scored *relative to par* on each of six axes, zero-sum: rising above par on one axis is paid for below par on another. Default = one Proficiency, at most one Neglect; anything more is an **Extreme** needing sign-off.
- **The Combat Floor** (adopted) — Combat is a *protected axis*. No class below par (3). Rationale: piracy is steel, smoke and blood; everyone fights at par. This matches Heart, which has the same hard floor of 3.
- The earlier absolute ●/◐/○ table is superseded by the relative model.

## 2. What we changed (all drafts)

| Class | Change | Source doc |
|---|---|---|
| **Sawbone** | Combat 0→3 (saw/maul, Brave); Heal 6→3 retargeted to Hull/Vermissian | `sawbone_combat_and_hull_draft.md` |
| **Chronicler** | Combat 1→3 (weaponized lore); Knowledge +9→+5 (merge/fold/convert) | `chronicler_combat_and_trim_draft.md` |
| **Sharper** | Combat 1→3 (concealed weapons, Hunt); Social +6→+3 (convert 2 minors) | `sharper_combat_and_trim_draft.md` |
| **Sin Bosun** | Combat 1→3 (divine steel + storm); light Knowledge trim | `sin_bosun_combat_draft.md` |
| **Castaway** | Heal 3→4 (ally-reach); Skill −1 | `heal_redistribution_draft.md` |
| **Corsair** | Heal 2→3 (ship's surgeon); Social −1 | `heal_redistribution_draft.md` |
| **Tidecaller** | Heal 2→3 (sea-physick); Knowledge −1 | `heal_redistribution_draft.md` |
| **Powder Mage** | No change — Combat +6 signed off as on-theme Extreme | — |
| **Daredevil** | No change — healthy (clean Travel Proficiency) | — |
| **Errant** | No change — healthy (dual Combat+Social, one Travel Neglect) | — |

## 3. The set after all changes (recomputed)

Per-class fingerprints [Combat / Social / Knowledge / Skill / Travel / Heal]:

| Class | C | S | K | Sk | T | H | Combat ≥ floor? |
|---|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| Castaway | 6 | 0 | 0 | 8 | 2 | 4 | ✓ |
| Tidecaller | 3 | 0 | 5 | 8 | 2 | 3 | ✓ |
| Corsair | 6 | 3 | 2 | 6 | 0 | 3 | ✓ |
| Powder Mage | 9 | 0 | 1 | 10 | 0 | 1 | ✓ |
| Sharper | 3 | 5 | 3 | 9 | 0 | 0 | ✓ |
| Daredevil | 4 | 2 | 1 | 9 | 3 | 0 | ✓ |
| Sin Bosun | 3 | 3 | 4 | 5 | 2 | 3 | ✓ |
| Sawbone | 3 | 0 | 2 | 9 | 1 | 3 | ✓ |
| Chronicler | 3 | 1 | 7 | 8 | 1 | 0 | ✓ |
| Errant | 5 | 5 | 3 | 5 | 0 | 2 | ✓ |
| **TOTAL** | **45** | **19** | **28** | **77** | **11** | **19** | **10/10** |

## 4. Distribution: before → after → vs Heart

| Axis | Heart | V4 before | **V4 after** | Read |
|---|:--:|:--:|:--:|---|
| Combat | 22% | 18% | **23%** | Up to Heart parity (slightly above) — the floor fixes did this |
| Social | 6% | 11% | **9.5%** | Eased toward Heart; still intentionally above |
| Knowledge | 10% | 16% | **14%** | Eased toward Heart; still intentionally above |
| Skill | 46% | 39% | **39%** | Unchanged — the catch-all, definitionally lower than Heart |
| Travel | 4% | 5% | **5.5%** | Unchanged-ish |
| Heal | 12% | 9% | **9.5%** | Up slightly, and now *spread* not concentrated |

## 5. Verification against the three goals

**① Combat floor met everywhere — YES.** All ten classes now score ≥3 on Combat (lowest are the four fixed classes, each at exactly par 3). The set-level Combat share rose 18%→23%, landing on Heart's 22% — the "steel, smoke and blood" target. No class is a non-combatant.

**② Spikes resolved — YES.**
- Knowledge: Chronicler 11→7 (+9 spike → +5 signed Proficiency); Tidecaller 6→5. No ability stack above +5.
- Social: Sharper 8→5 (+6 spike → +3 signed Proficiency). No social stack above +5.
- The only remaining large number is **Powder Mage Combat 9 (+6)** — a *combat* spike, on-theme, consciously signed off. Per the floor ethos, combat spikes are welcome; it stands.

**③ Healing spread — YES.** Was: Sawbone 6, everyone else ≤3, one point of failure. Now: party-Blood healing across **five** classes (Castaway 4, Corsair/Tidecaller/Sin Bosun/Sawbone 3, Errant 2). The Sawbone's remaining Heal is Hull/self/miracle, not party medicine. No single owner.

## 6. Extreme sign-offs on the books

| Class | Extreme | Status |
|---|---|---|
| Powder Mage | Combat +6 spike + triple Neglect (Soc/Trv/Heal) | **Signed — on-theme glass cannon** |
| Castaway | Double Neglect (Social 0 + Knowledge 0) | **Signed — wordless feral survivor** |
| Sharper | Double Neglect (Travel 0 + Heal 0) | **Signed — urban information spider** |
| Chronicler | Knowledge Proficiency +5 + Heal Neglect (0) | **Signed — drowned-lore scholar** |
| Sin Bosun | none (clean baseline) | n/a |
| Others | single Proficiency / single Neglect within default | n/a |

Every Extreme is now a *recorded choice*, not an unnoticed accident — which was the whole point of the median framework.

## 7. Open items before this goes into the class files

1. **Numbers are ±1 content-analysis estimates.** Re-tally each touched class after the actual rewrite to confirm Combat lands at floor and the trimmed axes sit where intended.
2. **Combo flags** (in each draft): don't stack two weak-point/ambush effects on one strike — Sawbone (Breaking Point vs Saw Cuts Both Ways), Sharper (Long Con's End vs Cheap Shot).
3. **Skill axis still ~39%** vs Heart's 46% — this is the catch-all and mostly definitional, but worth a later look at whether some "generic" picks should be re-pointed, the same way we re-pointed Social/Knowledge.
4. **Travel still the soft spot (5.5%).** The rebalance didn't touch the earlier finding that no class is a dedicated voyage specialist. Separate workstream if journeys are to become a pillar.
5. **Roll drafts into `class_*.md`** — all seven changed classes are still standalone working docs; nothing is written into Version 4 yet. Recommend a Version 5 folder when these are committed.

---

*This review reflects the drafted changes in the seven working docs listed in §2. It is an analysis layer; no class file has been modified yet.*
