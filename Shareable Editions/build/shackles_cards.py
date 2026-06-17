# -*- coding: utf-8 -*-
"""
Shackles theme module for build_designed_doc.py.
Provides bespoke colour-coded HTML for the per-category design system
(the five stress tracks, the nine domains, the eleven skills) and a slug map.

The builder calls INJECTIONS to replace placeholder markers in the assembled
Markdown with this raw HTML *before* markdown conversion. Put the markers on
their own line in the source, e.g.:   <!--TRACKS--><!--SKILLS--><!--DOMAINS-->
"""
DOMAINS=[
 ("Deepwater","#0D2B45","#1B4F72","The open ocean, sea-monsters, storms, and the deep."),
 ("Shallows","#0D3B2B","#1A5C3A","Reefs, coastlines, tidal caves, hidden anchorages."),
 ("Port","#2B1A0D","#7A3B0D","Taverns, markets, dockside politics and crime."),
 ("Outlaw","#1A0D0D","#6B1A1A","The Code, Free Captain politics, smuggling, pirate culture."),
 ("Colonial","#1A1A2B","#2B2B6B","Cheliax, the guilds, and the powers you exist to rob."),
 ("Arcane","#2B0D2B","#5C1A6B","Sea-magic, curses, witch-pacts, things older than ships."),
 ("Faith","#2B2000","#6B5200","Gods, cults, omens, and the religious life of the sea."),
 ("Ruins","#1A1A10","#4A4A28","Ghol-Gan and pre-human sites, and what's buried below."),
 ("Wilderness","#1A2B0D","#3B5C1A","Jungle interiors, island ecosystems, and survival."),
]
SKILLS=[("Brave","Act in danger, brawl, hold your nerve."),("Carouse","Drink, gamble, work the social theatre of port."),
 ("Command","Lead, intimidate, inspire — move people."),("Deceive","Lie, cheat, forge, disguise, bluff."),
 ("Endure","Resist punishment, exposure, disease, the sea."),("Hunt","Track, pursue, and end things, with skill."),
 ("Navigate","Chart courses, read weather, pilot, read tides."),("Plunder","Board, break in, loot — fast and bold."),
 ("Reckon","Observe, deduce, read what's really happening."),("Tend","Heal, maintain gear, run ship systems, brew."),
 ("Vanish","Hide, shadow, slip away, conceal.")]
TRACKS=[
 ("Blood","#480C0C","#7B1C1C","The body","Wounds, exhaustion, fire, drowning, and the shock that lives in the flesh.",
  "<em>Winded</em>, <em>Bleeding</em>, <em>Broken</em>.","Rest, food, and a surgeon."),
 ("Tide","#0D2B45","#1B4F72","The supernatural got in","Ruins, rites, bargains, the deep paying attention — the rarest, most frightening track.",
  "<em>Salt Weeping</em>, <em>The Mark</em>, <em>Compulsion</em>.","The hardest — ritual, or a full arc of story."),
 ("Reputation","#2B1A0D","#7A3B0D","Your name","Being bested where it's seen, breaking the Code, a story that travels ahead of you.",
  "<em>Whispers</em>, <em>Bounty</em>, <em>Name Destroyed</em>.","Public deeds; standing the room a round; your bonds."),
 ("Luck","#0D3B2B","#1A5C3A","Fated misfortune","The universe collecting on audacity, recklessness, and the loose ends you leave.",
  "<em>Foreboding</em>, then <em>Crisis</em>; <em>The Tab</em>.","<strong>Nothing but its own fallout firing.</strong>"),
 ("Gold","#2B2000","#6B5200","Your material position","Coin, a prize lost, a bribe paid, gear broken, a debt called at the worst moment.",
  "<em>Light Pockets</em>, <em>Broke</em>, <em>Marked for Collection</em>.","Plunder, a good prize, a debt settled."),
]
def tracks():
    o=['<div class="grid tracks">']
    for n,d,m,sub,desc,fo,cl in TRACKS:
        o.append(f'<div class="tcard" style="--d:{d};--m:{m}"><div class="tcard-head"><span class="tname">{n}</span>'
                 f'<span class="tsub">{sub}</span></div><div class="tcard-body"><p>{desc}</p>'
                 f'<p class="tline"><b>Fallout looks like</b> — {fo}</p>'
                 f'<p class="tline"><b>Clears by</b> — {cl}</p></div></div>')
    return "\n".join(o+['</div>'])
def domains():
    o=['<div class="grid domains">']
    for n,d,m,sub in DOMAINS:
        o.append(f'<div class="dchip" style="--d:{d};--m:{m}"><span class="dname">{n}</span><span class="dsub">{sub}</span></div>')
    return "\n".join(o+['</div>'])
def skills():
    o=['<div class="grid skills">']
    for n,sub in SKILLS:
        o.append(f'<div class="schip"><span class="sname">{n}</span><span class="ssub">{sub}</span></div>')
    return "\n".join(o+['</div>'])

INJECTIONS={
 "<!--TRACKS_START--><!--TRACKS_END-->": tracks,
 "<!--SKILLS_START--><!--SKILLS_END-->": skills,
 "<!--DOMAINS_START--><!--DOMAINS_END-->": domains,
 "<!--TRACKS-->": tracks, "<!--SKILLS-->": skills, "<!--DOMAINS-->": domains,
}
# Stable, human-friendly chapter slugs for the primer (optional; pass --slug-map SLUGS)
SLUGS={
 "The Pitch":"pitch","The World":"world","How to Play":"how","The Five Tracks":"tracks",
 "Skills & Domains":"skills","Callings — Why You Sail":"callings","Classes — What You Can Do":"classes",
 "Ancestries — Who You Are":"ancestries","Make Your Pirate":"make","Quick Reference":"quickref",
}
