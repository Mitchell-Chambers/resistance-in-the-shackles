# -*- coding: utf-8 -*-
# Assemble the PLAYER primer from the System Reference.
# Player-facing surface only: no balance/design commentary, no beats/zenith/Downfall
# scaffolding, no endgame reveals. The full versions live in the System Reference.
import re, os
SRC="/sessions/zealous-happy-clarke/mnt/Resistance in the Shackles/System Reference"
def read(p): return open(os.path.join(SRC,p),encoding="utf-8").read()
def strip_nav(t):
    i=t.find("<!-- nav -->")
    if i!=-1: t=t[:i]
    return t.rstrip()+"\n"
def drop_h1(t): return re.sub(r'^#\s+[^\n]*\n','',t,count=1)
def demote(t): return re.sub(r'(?m)^(#{1,5}) ', r'#\1 ', t)
def cut_from_to(t, start, stop):
    """remove [start .. stop). stop=None removes to end. start not found -> unchanged."""
    i=t.find(start)
    if i==-1: return t
    if stop is None: return t[:i].rstrip()+"\n"
    j=t.find(stop, i+len(start))
    if j==-1: return t[:i].rstrip()+"\n"
    return t[:i].rstrip()+"\n\n"+t[j:]
def section(t, start, stop=None):
    i=t.find(start)
    if i==-1: return ""
    return t[i:(t.find(stop,i+len(start)) if stop and t.find(stop,i+len(start))!=-1 else len(t))]

def ensure_blank_before_lists(t):
    """Markdown needs a blank line before a list. Insert one wherever a list item
    directly follows a non-blank, non-list line (this is what made sub-abilities
    render as a run-on block)."""
    lines=t.split("\n"); out=[]
    li=re.compile(r'^\s*([-*+]|\d+\.)\s')
    for i,l in enumerate(lines):
        if li.match(l) and i>0 and lines[i-1].strip() and not li.match(lines[i-1]):
            out.append("")
        out.append(l)
    return "\n".join(out)

OUT=[]
def add(s): OUT.append(s.rstrip()+"\n")

# ---------- COVER ----------
add("""# Blood, Water & Violent Wind

## A Player's Primer

*Resistance in the Shackles — liberty, and the reckoning that follows.*

<div class="cover-note">A pirate campaign in the Pathfinder Shackles. This primer is everything you need to make a pirate and understand a roll. What it costs to live this life, you will discover at sea.</div>
""")

# ---------- PRIMER (00) ----------
p=drop_h1(strip_nav(read("00-primer.md")))
p=re.sub(r'^##\s+Blood, Water.*\n','',p,count=1)
p=re.sub(r'^\*A pirate campaign.*\n','',p,count=1)
add("# The Pitch\n"+p)

# ---------- THE WORLD (01) ----------
add("# The World\n"+drop_h1(strip_nav(read("01-the-world.md"))))

# ---------- HOW TO PLAY (02, trimmed) ----------
sys=drop_h1(strip_nav(read("02-the-system.md")))
sys=cut_from_to(sys, "## Equipment, Resources & Tags", None)
sys=sys.replace(" Where a zenith grants the surviving party a once-per-campaign effect, that single use belongs to the party.","")
add("# How to Play\n"+sys)
add("""## Reading Your Gear

You don't track coins or count shots. A piece of equipment is a **stress die** (how big a hit it lands or heals) and maybe a **tag**. No suitable gear means a **D4**. The ladder runs **D4** improvised · **D6** civilian · **D8** professional · **D10** exotic · **D12** legendary. The tags you'll meet in a starting kit:

- **Brutal** — roll two stress dice, keep the highest.
- **Piercing** — ignores armour (Blood protection).
- **Ranged** — works at a distance. **Reload** — needs reloading between shots.
- **Tiring** — its die drops a step when you fail with it.
- **Block** — +1 Blood protection (the only gear that adds protection).
- **Wyrd** — roll the max and you mark Tide; the deep noticed.""")

# ---------- THE FIVE TRACKS ----------
add("""# The Five Tracks

Stress is the toll the Shackles takes — not a health bar, but the slow accumulation of pain, bad luck, supernatural attention, and lost coin. Every character carries five tracks. The GM marks stress to whichever one the *fiction* points at, and when a track's fallout fires, something concrete goes wrong. Some of it you can mend. Some of it, you cannot — not until it collects.""")
add("<!--TRACKS_START--><!--TRACKS_END-->")

# ---------- SKILLS & DOMAINS ----------
add("# Skills & Domains\n\nA **skill** is what you can do; a **domain** is where you know it and who you know there. When one is relevant, add a die and keep the highest. Both apply? Roll two. Gain either a second time and you get a **knack** — roll that narrow thing with mastery. The combination is the character: *Tend + Deepwater* is a ship's surgeon; *Tend + Ruins* patches people up in collapsing Ghol-Gan chambers.")
add("<!--SKILLS_START--><!--SKILLS_END-->")
add("<!--DOMAINS_START--><!--DOMAINS_END-->")

# ---------- CALLINGS (player-facing intro + entries, zeniths cut) ----------
add("""# Callings — Why You Sail

Your calling is your reason for sailing — the obsession that keeps you from a quiet life ashore. It is not a class or a profession; it is closer to a wound that has set into a direction. Choose the one that names what your character cannot stop wanting; it will deepen as you play, in ways you cannot yet see. Everyone also carries the shared **Piracy** calling alongside their own.

| Calling | The pull |
|---|---|
| **Hunger** | The wanting that the next prize never fills. |
| **Monument** | Making something — a name, a power — that outlasts you. |
| **Vendetta** | A single account that has to be settled. |
| **Freedom** | You were owned once; every cage you meet is yours to break. |
| **Cursed Tides** | The sea has marked you for its own. |
| **Legacy** | A name that went to sea before you did. |
| **Fellowship** | The crew is the only wealth you have ever counted. |
| **Piracy** *(shared)* | The life you all chose, and the ledger it keeps. |""")
cov=strip_nav(read("05-callings/README.md"))
add(section(cov, "## Choosing Your Calling"))   # the in-fiction "if torn between two" guide
for c in ["hunger","monument","vendetta","freedom","cursed-tides","legacy","fellowship","piracy"]:
    t=strip_nav(read(f"05-callings/{c}.md"))
    t=cut_from_to(t, "## ZENITH BEATS", "Roll 1d10")   # hide the endings; keep the carry table
    add(demote(t))

# ---------- CLASSES (player-facing intro + entries, zeniths cut) ----------
add("""# Classes — What You Can Do

Your class is the reason you are not dead yet — the hard-won expertise that has kept you alive through everything the Shackles has thrown at you. Pick one of the ten. You begin with its core skill and domain, a little gear, and one or two signature abilities; you grow new tricks as you sail.""")
cr=strip_nav(read("06-classes/README.md"))
add(section(cr, "## The Ten Classes", "## How a Class Works"))   # the one-line table only
for c in ["castaway","chronicler","corsair","daredevil","errant","powder-mage","sawbone","sharper","sin-bosun","tidecaller"]:
    t=strip_nav(read(f"06-classes/{c}.md"))
    t=cut_from_to(t, "## ZENITH ABILITIES", None)      # hide the mythic endgame
    t=re.sub(r'(?m)^- MINOR: ([^.\n]+?)\.', r'- **\1.**', t)   # sub-abilities: bold name, drop jargon
    add(demote(t))

# ---------- ANCESTRIES (player-facing intro + entries) ----------
add("""# Ancestries — Who You Are

Your ancestry is who you are before the dice hit the table — where you come from, how the world has treated you, what ghosts you carry onto a pirate deck. It grants no rules; it is who you are, not what you can do.""")
ar=strip_nav(read("07-ancestries/README.md"))
add(section(ar, "## Two kinds of ancestry", "## How to use an ancestry"))
add("To make a character: read your culture's or kindred's lore, **answer one** of its three questions out loud at the table, **choose a name**, and **roll twice** on its trinkets table.")
for c in ["shackleborn","bonuwat","chelaxian","small-folk","goblinkin","big-folk","the-made","beast-folk","planetouched"]:
    add(demote(strip_nav(read(f"07-ancestries/{c}.md"))))

# ---------- MAKE YOUR PIRATE (08, drop Advancement internals) ----------
mk=drop_h1(strip_nav(read("08-character-creation.md")))
mk=cut_from_to(mk, "## Advancement — How You Grow", "## Quick Reference — The Build")
mk=mk.replace(" (see Advancement, below)","")
mk=mk.replace("those are *advances*, earned in play","those come in play")
mk=mk.replace("any minor, major, or zenith abilities","its other abilities")
add("# Make Your Pirate\n"+mk)

# ---------- QUICK REFERENCE (drop the beats/zenith/Downfall reveal) ----------
qr=drop_h1(strip_nav(read("quick-reference.md")))
qr=re.sub(r'\*The whole game.*?\*\n','',qr,count=1,flags=re.S)
qr=cut_from_to(qr, "## Beats & Advancement", None)
qr=re.sub(r'\n*\[Contents\].*$','',qr,flags=re.S)
add("# Quick Reference\n"+qr)

md="\n".join(OUT)
# self-contained: internal relative links -> plain text
md=re.sub(r'\[([^\]]+)\]\((?!https?:|#)[^)]*\)', r'\1', md)
md=ensure_blank_before_lists(md)
open("/sessions/zealous-happy-clarke/mnt/outputs/player-primer.md","w",encoding="utf-8").write(md)
print("primer.md bytes:", len(md))
print("H1:", re.findall(r'(?m)^# (.+)$', md))
