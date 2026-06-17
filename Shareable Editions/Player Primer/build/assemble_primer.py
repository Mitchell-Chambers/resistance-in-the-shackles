# -*- coding: utf-8 -*-
import re, os
SRC="/sessions/zealous-happy-clarke/mnt/Resistance in the Shackles/System Reference"
def read(p): return open(os.path.join(SRC,p),encoding="utf-8").read()
def strip_nav(t):
    i=t.find("<!-- nav -->")
    if i!=-1: t=t[:i]
    return t.rstrip()+"\n"
def drop_h1(t):
    return re.sub(r'^#\s+[^\n]*\n','',t,count=1)
def demote(t):
    return re.sub(r'(?m)^(#{1,5}) ', r'#\1 ', t)
def section(t, start, end=None):
    """keep from heading 'start' up to (not incl) heading 'end'"""
    s=t.find(start)
    if s==-1: return ""
    if end:
        e=t.find(end, s+len(start))
        return t[s: e if e!=-1 else len(t)]
    return t[s:]
def cut_from(t, marker):
    i=t.find(marker)
    return t[:i] if i!=-1 else t

OUT=[]
def add(s): OUT.append(s.rstrip()+"\n")

# ---------- COVER ----------
add("""# Blood, Water & Violent Wind

## A Player's Primer

*Resistance in the Shackles — liberty, and the reckoning that follows.*

<div class="cover-note">A pirate campaign in the Pathfinder Shackles, run on the Resistance engine of <em>Heart: the City Beneath</em>. This primer is everything a player needs to roll up a pirate and understand a roll. The full rules live in the System Reference; the doom lives in the dice.</div>
""")

# ---------- PRIMER (00) ----------
p=strip_nav(read("00-primer.md"))
p=drop_h1(p)              # drop "# Primer"
p=re.sub(r'^##\s+Blood, Water.*\n','',p,count=1)  # drop duplicate banner subtitle
p=re.sub(r'^\*A pirate campaign.*\n','',p,count=1)
add("# The Pitch\n"+p)

# ---------- THE WORLD (01) ----------
w=strip_nav(read("01-the-world.md")); w=drop_h1(w)
add("# The World\n"+w)

# ---------- HOW TO PLAY (02, trimmed) ----------
sys=strip_nav(read("02-the-system.md")); sys=drop_h1(sys)
sys=cut_from(sys, "## Equipment, Resources & Tags")   # drop heavy gear glossary
add("# How to Play\n"+sys)
add("""## Reading Your Gear

You don't track coins or count shots. A piece of equipment is just a **stress die** (how big a hit it lands or heals) and maybe a **tag**. No suitable gear means a **D4**. The ladder runs **D4** improvised · **D6** civilian · **D8** professional · **D10** exotic · **D12** legendary. The tags you'll meet in a starting kit:

- **Brutal** — roll two stress dice, keep the highest.
- **Piercing** — ignores armour (Blood protection).
- **Ranged** — works at a distance. **Reload** — needs reloading between shots, so the enemy gets a moment.
- **Tiring** — its die drops a step when you fail with it.
- **Block** — +1 Blood protection (the only gear that adds protection).
- **Wyrd** — roll the max and you mark Tide; the deep noticed.

*(The full equipment, quality, and resource rules are in the System Reference.)*""")

# ---------- THE FIVE TRACKS (04, cards in themer) ----------
add("""# The Five Tracks

Stress is the toll the Shackles takes — not a health bar, but the slow accumulation of pain, bad luck, supernatural attention, and lost coin. Every character carries five tracks. The GM marks stress to whichever one the *fiction* points at, and when a track's fallout fires, something concrete goes wrong. Four of the five can be cleared. One cannot — not until it collects.""")
add("<!--TRACKS_START--><!--TRACKS_END-->")

# ---------- SKILLS & DOMAINS (03, one-liners) ----------
add("# Skills & Domains\n\nA **skill** is what you can do; a **domain** is where you know it and who you know there. When one is relevant, add a die and keep the highest. Both apply? Roll two. Gain either a second time and you get a **knack** — roll that narrow thing with mastery (an extra die). The combination is the character: *Tend + Deepwater* is a ship's surgeon; *Tend + Ruins* patches people up in collapsing Ghol-Gan chambers.")
add("<!--SKILLS_START--><!--SKILLS_END-->")
add("<!--DOMAINS_START--><!--DOMAINS_END-->")

# ---------- CALLINGS (05, full) ----------
add("# Callings — Why You Sail\n")
cov=strip_nav(read("05-callings/README.md")); cov=drop_h1(cov)
add(cov)
for c in ["hunger","monument","vendetta","freedom","cursed-tides","legacy","fellowship","piracy"]:
    add(demote(strip_nav(read(f"05-callings/{c}.md"))))

# ---------- CLASSES (06, full) ----------
add("# Classes — What You Can Do\n")
cr=strip_nav(read("06-classes/README.md")); cr=drop_h1(cr)
add(cr)
for c in ["castaway","chronicler","corsair","daredevil","errant","powder-mage","sawbone","sharper","sin-bosun","tidecaller"]:
    add(demote(strip_nav(read(f"06-classes/{c}.md"))))

# ---------- ANCESTRIES (07, full) ----------
add("# Ancestries — Who You Are\n")
ar=strip_nav(read("07-ancestries/README.md")); ar=drop_h1(ar)
add(ar)
for c in ["shackleborn","bonuwat","chelaxian","small-folk","goblinkin","big-folk","the-made","beast-folk","planetouched"]:
    add(demote(strip_nav(read(f"07-ancestries/{c}.md"))))

# ---------- MAKE YOUR PIRATE (08) ----------
mk=strip_nav(read("08-character-creation.md")); mk=drop_h1(mk)
add("# Make Your Pirate\n"+mk)

# ---------- QUICK REFERENCE (card) ----------
qr=strip_nav(read("quick-reference.md")); qr=drop_h1(qr)
qr=re.sub(r'\*The whole game.*?\*\n','',qr,count=1,flags=re.S)
add("# Quick Reference\n"+qr)

md="\n".join(OUT)
open("/sessions/zealous-happy-clarke/mnt/outputs/player-primer.md","w",encoding="utf-8").write(md)
print("primer.md bytes:", len(md))
print("H1 sections:", re.findall(r'(?m)^# (.+)$', md))
