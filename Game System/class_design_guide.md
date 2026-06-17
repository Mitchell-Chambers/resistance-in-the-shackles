# Class Design Guide

This document codifies patterns extracted from all nine Heart: The City Beneath base classes. Use it as a checklist and reference when designing new classes for Resistance in the Shackles.

---

## 1. Class Structure Overview

Every class is built from the same skeleton, in this order:

1. **Flavour introduction** — one paragraph establishing who this person is and why they're in the Heart.
2. **Core Traits** — skill, domain, resource, equipment.
3. **Core Abilities** — 1–2 abilities that define the class's unique mechanical identity.
4. **Minor Abilities** — ~13 advances (3 generic + ~10 named).
5. **Major Abilities** — 4–6 abilities, each with exactly 3 sub-minor advances.
6. **Zenith Abilities** — exactly 3 retirement/end-state abilities.

---

## 2. Core Traits

### Skill & Domain
Each class has one **core skill** and one **core domain**. These are the two most important design decisions — everything else flows from them.

- The core domain is used in nearly every major ability roll check, so it defines the class's mechanical "flavour tradition."
- The core skill signals what the class does most often in play.
- No two classes should share the same core skill + core domain combination.

### Resource
One resource with a domain tag and a dice value (almost always D6). The domain on the resource is typically the core domain or a close secondary. The item should be evocative of the class's lifestyle.

### Equipment
Either a **fixed item + pick one of three options**, or **pick one of three options** with no fixed item. The three options should cover:
- A damage-focused weapon (D8 or better)
- A utility or support item (Mend, Delve, etc.)
- A hybrid or flavour option

---

## 3. Core Abilities

Most classes have **2 core abilities**; simpler or more focused classes may have 1.

A good core ability pair follows one of these structures:
- **Passive + Active** — one always-on effect, one triggered or rolled ability.
- **Identity + Engine** — one ability establishing the class fantasy, one providing the primary mechanical loop that other abilities feed into.

> **Key rule:** At least one major ability should upgrade or directly extend a core ability. Design the core abilities with that scaling potential in mind.

---

## 4. Minor Abilities

### The Building Blocks

Every named minor ability is built from exactly **one primary building block** plus **optional ability text**:

| Building Block | Usage |
|---|---|
| **Named skill grant** | "Gain the [Skill] skill." |
| **Named domain grant** | "Gain the [Domain] domain." |
| **Protection +2** | "Gain +2 [Resistance] Protection." — almost never paired with ability text. |
| **Protection +1** | Used almost exclusively in the generic repeatable advance. Exception: the Hound pairs +1 protection with ability text for its named advances, making it a structural outlier. |
| **Ability text** | The unique mechanical effect. Almost always paired with a skill or domain grant, not standalone. |

**The standard formula:**
`[Gain skill X] + [ability text]` or `[Gain domain X] + [ability text]`

**The protection formula:**
`[Gain +2 Resistance X]` — no additional text.

Two building blocks may be combined in the same advance, but this should be the exception (e.g. gain a skill + gain +1 protection). This signals an advance that trades breadth for specificity.

---

### The Three Generic Repeatable Advances

Every class has exactly **three generic advances** with no ability text, each repeatable:

1. **Skill picklist** — "Gain access to one of the following skills: [list]. You can take this advance more than once."
2. **Domain picklist** — "Gain access to one of the following domains: [list]. You can take this advance more than once."
3. **Protection +1 picklist** — "Gain +1 Protection in the [Resistance], [Resistance], [Resistance] or [Resistance] resistance. You can take this advance more than once."

These are the mechanical floor — the catch-up advances any player can take if nothing else fits their build.

---

### The Named +2 Protection Pair

Every class has exactly **two** named (non-generic) advances that grant **+2 protection**, each in a different resistance. The Hound is the one exception, using three +1 protection advances with ability text instead.

When choosing a class's protection pair, note these existing pairs to avoid straight duplication:

| Pair | Classes |
|---|---|
| Blood + Echo | Deep Apiarist, Vermissian Knight |
| Blood + Mind | Witch |
| Blood + Supplies | Deadwalker |
| Fortune + Echo | Cleaver |
| Fortune + Mind | Heretic |
| Fortune + Supplies | Incarnadine, Junk Mage |

Sharing a pair with an existing class is not forbidden, but does signal "cousin" archetype territory. If intentional, lean into it.

---

### Preferred Domains & Skills (Named Advances)

Named advances (excluding pick lists) should grant the following:

- **4–5 named domains** (3 is narrow but defensible for tightly focused classes)
- **5–6 named skills**

**Three domains appear in every class's pick list** and should almost always be available to any new class: **Cursed, Desolate, Warren**. Haven and Technology are the most frequently excluded from pick lists and should only appear if they suit the class's identity.

**Forbidden skills** are intentional. Each class should have 1–2 skills it simply cannot access through any advance. This differentiates classes and prevents homogenisation. Decide which skills don't fit the class fantasy, then exclude them from both named advances and the pick list.

---

### Total Minor Advance Count

Aim for **13 minor advances** per class: 3 generic + 10 named. This gives enough variety without overwhelming choice.

The 10 named advances should cover a mix of:
- ~4–5 skill grants with ability text
- ~3–4 domain grants with ability text
- ~2 bare +2 protection advances (the protection pair)

---

## 5. Major Abilities

### Count
**4–6 major abilities** per class. Simpler or combat-focused classes sit at 4–5. Spell-heavy or mechanically complex classes sit at 5–6.

---

### Functional Categories

Every major ability belongs to one of eight categories. **No class should have more than two majors in the same category.**

| Category | What it does |
|---|---|
| **Weapon grant** | Creates a new attack profile, named weapon, or fighting technique |
| **Companion** | Grants a persistent creature, manifestation, or bonded entity |
| **Area / environment** | Transforms or controls the battlefield or a space |
| **Core upgrade** | Directly enhances or extends a core ability |
| **Support / healing** | Removes stress or fallout, benefits allies |
| **Information / scrying** | Reveals hidden facts about people, places, or futures |
| **Social / control** | Uses NPCs as targets or vectors for effects |
| **Spatial / travel** | Movement between or through spaces, connections between landmarks |

**Near-mandatory categories:** Almost every class has at least one **spatial/travel** major and one **weapon grant or fighting technique**. These two should be the default starting point when designing a new suite.

---

### Roll Formula

Active major abilities use: `[Skill] + [Core Domain]`

The skill signals the *approach type*:

| Skill | Approach signals |
|---|---|
| Compel | Social, manipulation, commands |
| Discern | Detection, revelation, reading situations |
| Endure | Ritual, willpower, sustained effort |
| Mend | Construction, binding, healing-based |
| Delve | Exploration, navigation, opening paths |
| Evade | Speed, chaos magic, reactive effects |
| Hunt | Tracking, targeting, pursuit |
| Kill | Rarely the activation roll — usually the effect roll |

The domain is **almost always the class's core domain**. Using a secondary domain (one the class can access but didn't start with) is acceptable for thematic variety, but should be the exception.

---

### Cost Structure

Assign every active major ability one cost type:

| Cost | When to use |
|---|---|
| **Mark stress to Echo** | Supernatural, wyrd, or body-warping effects |
| **Mark stress to Fortune** | Overextension, luck-pressing, risk-taking abilities |
| **Mark stress to Mind** | Psychological strain, possession, communion with alien things |
| **Resource consumption** | Abilities that "fuel" off the class's resource loop |
| **Time / preparation** | Rituals, landmark-based abilities (10 min to 1 hour) |
| **Conditional trigger** | Passive abilities requiring a specific circumstance to activate |

Blood stress as an *activation cost* should be rare and explicitly self-sacrificial in flavour. Mind stress as activation cost is rare — only use it when the flavour of mental strain is central.

---

### The One Mechanic Rule

Each major ability introduces **exactly one new mechanical concept**. The sub-minors modify *only that concept* — they do not introduce new systems.

> **Test:** Can you describe the major ability's core function in one sentence? If not, split it or simplify.

---

### Sub-Minor Structure

Every major has exactly **3 sub-minors**, filling three distinct roles:

1. **Power** — raw increase: bigger dice, new weapon tag, extra target, more stress removed.
2. **Expansion** — broader scope: applies to more people, doesn't need a condition, works in more situations.
3. **Alternate mode** — a different way to trigger or use the same ability: different target type, different payoff, different activation condition.

No two sub-minors should do the same thing. If two feel like "power increases," reframe one as an expansion or alternate.

---

### Sub-Minor Patterns by Category

**Weapon grant majors:**
- Power: add a tag (Brutal, Piercing, etc.) or increase dice size
- Expansion: apply to ranged as well as melee, or remove a restriction
- Alternate: new weapon profile (One-Shot variant, Spread, etc.) or different trigger

**Companion majors:**
- Combat utility: the companion helps in a fight (mastery on a roll, one-shot damage, etc.)
- Tool stat block: the companion functions as a weapon or delve item with a dice value
- Resilience / life-saving: the companion absorbs a fallout, prevents a death, or has higher capacity

**Roll-to-cast spell majors:**
- Expansion: broaden from single target to nearby, or include self
- Duration: extend from situation to session, or make permanent
- Secondary effect: add a second payoff on success, or an alternate casting mode

**Core upgrade majors:**
Sub-minors should extend the *original core ability* further, not the upgrade itself. The upgrade is already the power increase — sub-minors add breadth and alternate uses.

---

### The Core Upgrade Major

At least one major per class should directly upgrade or extend a core ability. These work best when the core ability has an obvious scaling dimension (more targets, better resources, stronger effects, relaxed conditions).

If a class's core ability is already complete and self-contained, this may be replaced with a thematically adjacent major instead.

---

## 6. Zenith Abilities

Every class has exactly **3 zenith abilities**. Each one is a retirement trigger — using it removes the character from play in some permanent way (death, transformation, absorption into something greater, ascension, etc.).

Zeniths should:
- Be enormously powerful, well beyond anything in the minor/major tiers.
- Be narratively irreversible.
- Reflect the class's core identity taken to its logical extreme.
- Offer three distinct *flavours* of ending for the character (e.g. one violent/sacrificial, one triumphant, one transcendent).

Zeniths do not need sub-minor advances.

---

## 7. Domain & Skill Reference

### The Eight Domains
`Cursed` `Desolate` `Haven` `Occult` `Religion` `Technology` `Warren` `Wild`

- **Cursed, Desolate, Warren** — appear in every class's domain pick list. Universal Heart flavour.
- **Haven** — social/settlement focus. Exclude for classes with no ties to communities.
- **Technology** — rare as a named advance; mostly for artificer/engineer archetypes.
- **Occult, Religion, Wild** — magic/faith/nature flavour. Assign based on class tradition.

### The Nine Skills
`Compel` `Delve` `Discern` `Endure` `Evade` `Hunt` `Kill` `Mend` `Sneak`

Skills to consider making "forbidden" (class cannot access) based on archetype:
- **Sneak** — odd for front-line fighters, open classes
- **Evade** — odd for heavy/armoured archetypes
- **Mend** — odd for nihilistic or death-focused classes
- **Delve** — odd for classes with no interest in exploration
- **Endure** — odd for glass-cannon or luck-based classes

---

## 8. Quick Design Checklist

### Core
- [ ] Core skill and core domain chosen; unique combination
- [ ] Resource has a domain and evocative description
- [ ] Equipment covers damage, utility, and hybrid options
- [ ] 1–2 core abilities; at least one has scaling potential

### Minors
- [ ] Exactly 3 generic repeatable advances (skill pick, domain pick, +1 protection pick)
- [ ] ~10 named advances: ~4–5 skill+text, ~3–4 domain+text, 2 bare +2 protection
- [ ] Named domains: 4–5 total (including core domain)
- [ ] Named skills: 5–6 total (including core skill)
- [ ] +2 protection pair covers two different resistances
- [ ] 1–2 forbidden skills identified and excluded from all lists
- [ ] Cursed, Desolate, Warren available in domain pick list

### Majors
- [ ] 4–6 major abilities total
- [ ] No more than 2 majors in any single functional category
- [ ] At least one spatial/travel major
- [ ] At least one weapon grant or fighting technique major
- [ ] At least one support/ally-benefiting major
- [ ] At least one core upgrade major (or strong thematic substitute)
- [ ] Every active major uses [Skill]+[Core Domain]
- [ ] Every major has exactly one central mechanic
- [ ] Every major has exactly 3 sub-minors: one power, one expansion, one alternate

### Zeniths
- [ ] Exactly 3 zenith abilities
- [ ] Each one is a retirement trigger
- [ ] Three distinct flavours of ending
