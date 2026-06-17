# -*- coding: utf-8 -*-
import re, markdown, urllib.parse

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
SKILLS=[
 ("Brave","Act in danger, brawl, hold your nerve."),
 ("Carouse","Drink, gamble, work the social theatre of port."),
 ("Command","Lead, intimidate, inspire — move people."),
 ("Deceive","Lie, cheat, forge, disguise, bluff."),
 ("Endure","Resist punishment, exposure, disease, the sea."),
 ("Hunt","Track, pursue, and end things, with skill."),
 ("Navigate","Chart courses, read weather, pilot, read tides."),
 ("Plunder","Board, break in, loot — fast and bold."),
 ("Reckon","Observe, deduce, read what's really happening."),
 ("Tend","Heal, maintain gear, run ship systems, brew."),
 ("Vanish","Hide, shadow, slip away, conceal."),
]
TRACKS=[
 ("Blood","#480C0C","#7B1C1C","The body","Wounds, exhaustion, fire, drowning, and the shock that lives in the flesh.",
  "<em>Winded</em>, <em>Bleeding</em>, <em>Broken</em> (a bone — useless until a surgeon sees it).","Rest, food, and a surgeon."),
 ("Tide","#0D2B45","#1B4F72","The supernatural got in","Ruins, rites, bargains, the deep paying attention — the rarest and most frightening track.",
  "<em>Salt Weeping</em>, <em>The Mark</em>, <em>Compulsion</em> — something must be done, or avoided.","The hardest — ritual, or a full arc of story. Rest does nothing."),
 ("Reputation","#2B1A0D","#7A3B0D","Your name","Being bested where it's seen, breaking the Code, a story that travels ahead of you.",
  "<em>Whispers</em>, <em>Bounty</em>, <em>Name Destroyed</em> in a stretch of the Shackles.","Public, witnessed deeds; standing the room a round; your bonds."),
 ("Luck","#0D3B2B","#1A5C3A","Fated misfortune","The universe collecting on audacity, recklessness, and the loose ends you leave behind.",
  "<em>Foreboding</em>, then <em>Crisis</em>; <em>The Tab</em> — a forgotten debt come due.","<strong>Nothing but its own fallout firing.</strong> The track that does not forgive."),
 ("Gold","#2B2000","#6B5200","Your material position","Coin, a prize lost, a bribe paid, gear broken, a debt called in at the worst moment.",
  "<em>Light Pockets</em>, <em>Broke</em>, <em>Marked for Collection</em>.","Plunder, a good prize, a debt settled."),
]

def cards_tracks():
    out=['<div class="grid tracks">']
    for name,d,m,sub,desc,fo,cl in TRACKS:
        out.append(f'''<div class="tcard" style="--d:{d};--m:{m}">
<div class="tcard-head"><span class="tname">{name}</span><span class="tsub">{sub}</span></div>
<div class="tcard-body"><p>{desc}</p>
<p class="tline"><b>Fallout looks like</b> — {fo}</p>
<p class="tline"><b>Clears by</b> — {cl}</p></div></div>''')
    out.append('</div>')
    return "\n".join(out)

def grid_domains():
    out=['<div class="grid domains">']
    for name,d,m,sub in DOMAINS:
        out.append(f'<div class="dchip" style="--d:{d};--m:{m}"><span class="dname">{name}</span><span class="dsub">{sub}</span></div>')
    out.append('</div>')
    return "\n".join(out)

def grid_skills():
    out=['<div class="grid skills">']
    for name,sub in SKILLS:
        out.append(f'<div class="schip"><span class="sname">{name}</span><span class="ssub">{sub}</span></div>')
    out.append('</div>')
    return "\n".join(out)

md=open("player-primer.md",encoding="utf-8").read()
# inject bespoke taxonomy HTML into the markdown (block-level raw HTML, passed through verbatim)
md=md.replace("<!--TRACKS_START--><!--TRACKS_END-->", "\n\n"+cards_tracks()+"\n\n")
md=md.replace("<!--SKILLS_START--><!--SKILLS_END-->", "\n\n"+grid_skills()+"\n\n")
md=md.replace("<!--DOMAINS_START--><!--DOMAINS_END-->", "\n\n"+grid_domains()+"\n\n")
html=markdown.markdown(md, extensions=['sane_lists','attr_list','tables','toc'], output_format='html5')

# wrap chapters: split on <h1 ...>...</h1>
def slug(t):
    t=t.lower()
    for k,s in [("blood, water","cover"),("pitch","pitch"),("the world","world"),("how to play","how"),
                ("five tracks","tracks"),("skills","skills"),("callings","callings"),("classes","classes"),
                ("ancestries","ancestries"),("make your pirate","make"),("quick reference","quickref")]:
        if k in t: return s
    return re.sub(r'[^a-z0-9]+','-',t).strip('-')
parts=re.split(r'(<h1[^>]*>.*?</h1>)', html, flags=re.S)
# parts: [pre, h1, body, h1, body, ...]
chapters=[]
i=1
pre=parts[0]
while i < len(parts):
    h1=parts[i]; body=parts[i+1] if i+1<len(parts) else ""
    title=re.sub(r'<[^>]+>','',h1)
    chapters.append((slug(title),h1,body))
    i+=2
body_html=[pre]
toc=['<nav class="toc"><div class="toc-title">Contents</div><ol>']
for sl,h1,bd in chapters:
    if sl=="cover": continue
    title=re.sub(r'<[^>]+>','',h1)
    toc.append(f'<li><a href="#{sl}">{title}</a></li>')
toc.append('</ol></nav>')
for sl,h1,bd in chapters:
    h1a=re.sub(r'<h1', f'<h1 id="{sl}"', h1, count=1)
    cls="chapter ch-"+sl
    if sl=="cover":
        body_html.append(f'<section class="{cls}">{h1a}{bd}</section>')
        body_html.append("".join(toc))
    else:
        body_html.append(f'<section class="{cls}">{h1a}{bd}</section>')
content="\n".join(body_html)

COMPASS=urllib.parse.quote('''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><g fill="none" stroke="#7A1F12" stroke-width="0.6"><circle cx="50" cy="50" r="46"/><circle cx="50" cy="50" r="34"/></g><g fill="#7A1F12"><polygon points="50,4 56,50 50,96 44,50"/><polygon points="4,50 50,44 96,50 50,56"/></g><g fill="#9B7E55"><polygon points="22,22 50,46 78,78 46,50"/><polygon points="78,22 54,46 22,78 50,54"/></g></svg>''')

CSS = """
@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@500;700&family=EB+Garamond:ital,wght@0,400;0,600;1,400&display=swap');
@page{ size:A5; margin:13mm 11mm; }
@page{ @bottom-center{ content:counter(page); color:#7A1F12; font-family:serif; font-size:9pt } }
:root{
 --paper:#EFE6D2; --paper2:#E4D6B8; --ink:#1A1208; --ink2:#2B2118;
 --gold:#C9A97A; --rule:#9B7E55; --oxblood:#7A1F12; --oxdark:#3B0D0D;
}
*{box-sizing:border-box}
html{ -webkit-text-size-adjust:100% }
body{
 margin:0; background:var(--paper);
 color:var(--ink);
 font-family:'EB Garamond',Georgia,'Times New Roman',serif;
 font-size:1.08rem; line-height:1.62;
 background-image:
   radial-gradient(circle at 18% 12%, rgba(155,126,85,.10), transparent 40%),
   radial-gradient(circle at 82% 78%, rgba(122,31,18,.06), transparent 45%),
   linear-gradient(160deg,var(--paper),var(--paper2));
 background-attachment:fixed;
}
.wrap{max-width:820px; margin:0 auto; padding:1.4rem 1.15rem 4rem}
p{margin:.55rem 0}
a{color:var(--oxblood); text-decoration:none; border-bottom:1px solid rgba(122,31,18,.3)}
strong,b{color:var(--ink2)}
hr{border:0; border-top:1px solid var(--rule); opacity:.5; margin:1.6rem 0}

/* headings */
h1,h2,h3,h4{font-family:'Cinzel',serif; line-height:1.15; letter-spacing:.04em}
h1{ font-size:1.7rem; text-transform:uppercase; color:var(--oxblood);
 text-align:center; margin:0 0 .2rem; padding:1.5rem 0 .4rem; border-bottom:2px solid var(--oxblood)}
.chapter{padding-top:.6rem}
.chapter>h1{ margin-top:.4rem }
h2{ font-size:1.18rem; text-transform:uppercase; color:var(--gold);
 background:linear-gradient(100deg,var(--oxdark),var(--oxblood) 60%, #8f3a26);
 margin:1.7rem 0 .7rem; padding:.42rem .7rem; border-radius:2px;
 box-shadow:0 1px 0 rgba(0,0,0,.25); border-left:5px solid var(--gold)}
h3{ font-size:1.0rem; text-transform:uppercase; color:var(--oxblood);
 letter-spacing:.07em; margin:1.1rem 0 .35rem; border-bottom:1px solid var(--rule)}
h4{ font-size:.92rem; text-transform:uppercase; color:var(--ink2); letter-spacing:.06em; margin:.8rem 0 .2rem}
blockquote h2,blockquote h3{background:none;color:var(--oxblood);border:0;padding:0}

/* chapter accent (subtle) */
.ch-callings .chapter, .ch-callings h2{}
.ch-classes h2{ background:linear-gradient(100deg,#241a12,#2b2118 60%,#4a3a2a)}
.ch-ancestries h2{ background:linear-gradient(100deg,#2b1a0d,#7a3b0d 70%,#9a6a3a)}

/* lists with diamond bullets */
ul{list-style:none; padding-left:1.2rem}
ul>li{position:relative; margin:.2rem 0}
ul>li::before{content:"\\25C6"; color:var(--oxblood); position:absolute; left:-1.1rem; font-size:.7em; top:.35em}
ol{padding-left:1.4rem}
ol>li{margin:.2rem 0}
li>ul{margin:.2rem 0}

/* tables */
table{border-collapse:collapse; width:100%; margin:.8rem 0; font-size:.96rem; background:rgba(255,255,255,.18)}
th,td{border:1px solid var(--rule); padding:.32rem .5rem; text-align:left; vertical-align:top}
thead th{background:var(--oxblood); color:var(--gold); font-family:'Cinzel',serif; text-transform:uppercase; font-size:.8rem; letter-spacing:.04em}
tbody tr:nth-child(even){background:rgba(155,126,85,.10)}

/* statblock blockquotes */
blockquote{ margin:.9rem 0; padding:.6rem .9rem; background:rgba(245,230,204,.55);
 border:1px solid var(--rule); border-left:4px solid var(--oxblood); border-radius:2px}
blockquote p{margin:.25rem 0}
blockquote strong:first-child{font-family:'Cinzel',serif; letter-spacing:.03em}
code{background:rgba(122,31,18,.08); padding:.05em .3em; border-radius:3px; font-family:ui-monospace,Menlo,Consolas,monospace; font-size:.85em}

/* cover */
.ch-cover>h1{border:0; font-size:2.5rem; padding-top:2.2rem; text-shadow:0 1px 0 rgba(0,0,0,.1)}
.ch-cover{ text-align:center; position:relative;
 background:center/180px no-repeat url("data:image/svg+xml,%COMPASS%");
 background-position:center 58%}
.ch-cover h2{display:inline-block; background:none; color:var(--oxblood); box-shadow:none; border:0;
 font-size:1.05rem; letter-spacing:.18em; margin:.2rem 0 1rem}
.cover-note{ max-width:46ch; margin:1.3rem auto 0; font-style:italic; color:var(--ink2);
 border-top:1px solid var(--rule); border-bottom:1px solid var(--rule); padding:1rem 0}

/* TOC */
.toc{ margin:1.5rem 0 2.5rem; padding:1rem 1.2rem; background:rgba(255,255,255,.22);
 border:1px solid var(--rule); border-radius:3px}
.toc-title{font-family:'Cinzel',serif; text-transform:uppercase; color:var(--oxblood); letter-spacing:.1em; font-size:.85rem; margin-bottom:.4rem}
.toc ol{columns:2; column-gap:1.6rem}
@media(max-width:520px){ .toc ol{columns:1} }

/* bespoke grids */
.grid{display:grid; gap:.7rem; margin:1rem 0}
.tracks{grid-template-columns:1fr}
@media(min-width:620px){ .tracks{grid-template-columns:1fr 1fr} }
.tcard{ border-radius:4px; overflow:hidden; border:1px solid rgba(0,0,0,.25);
 background:var(--m); color:#fff8ec; box-shadow:0 1px 2px rgba(0,0,0,.2)}
.tcard-head{ background:var(--d); padding:.4rem .7rem; display:flex; align-items:baseline; gap:.6rem}
.tname{font-family:'Cinzel',serif; text-transform:uppercase; color:var(--gold); letter-spacing:.06em; font-size:1.02rem}
.tsub{font-style:italic; color:#e8dcc4; font-size:.85rem}
.tcard-body{padding:.5rem .75rem}
.tcard-body p{margin:.3rem 0; font-size:.93rem}
.tline{ background:rgba(255,255,255,.92); color:var(--ink); border-radius:2px; padding:.25rem .45rem }
.tline b{color:var(--oxblood); font-family:'Cinzel',serif; font-size:.74rem; text-transform:uppercase; letter-spacing:.03em}

.domains{grid-template-columns:1fr 1fr}
@media(min-width:680px){ .domains{grid-template-columns:1fr 1fr 1fr} }
.dchip{ background:var(--m); color:#fff8ec; border-radius:4px; border:1px solid rgba(0,0,0,.25); overflow:hidden}
.dname{ display:block; background:var(--d); color:var(--gold); font-family:'Cinzel',serif; text-transform:uppercase;
 letter-spacing:.05em; font-size:.85rem; padding:.3rem .55rem}
.dsub{ display:block; padding:.4rem .55rem; font-size:.85rem; line-height:1.4}

.skills{grid-template-columns:1fr 1fr}
@media(min-width:680px){ .skills{grid-template-columns:1fr 1fr 1fr} }
.schip{ background:#F5D6D6; border:1px solid #6B1A1A; border-radius:4px; overflow:hidden}
.sname{ display:block; background:#6B1A1A; color:var(--gold); font-family:'Cinzel',serif; text-transform:uppercase;
 letter-spacing:.05em; font-size:.82rem; padding:.28rem .55rem}
.ssub{ display:block; padding:.35rem .55rem; font-size:.84rem; color:#3a1414; line-height:1.4}

/* quickref */
.ch-quickref{ }
.ch-quickref table{font-size:.9rem}

/* print */
@media print{
 body{background:#fff; font-size:10.3pt}
 .wrap{max-width:none; padding:0}
 .toc{break-after:page}
 .chapter{break-before:page}
 .ch-cover{break-before:auto}
 h1,h2,h3,h4{break-after:avoid}
 blockquote,.tcard,.dchip,.schip,table,li{break-inside:avoid}
 a{border:0; color:var(--ink)}
}
"""
CSS=CSS.replace("%COMPASS%", COMPASS)

doc=f"""<!DOCTYPE html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Blood, Water & Violent Wind — A Player's Primer</title>
<style>{CSS}</style></head>
<body><div class="wrap">{content}
<footer style="margin-top:3rem;border-top:1px solid var(--rule);padding-top:1rem;font-style:italic;color:var(--ink2);text-align:center;font-size:.9rem">
Resistance in the Shackles — player primer · compiled from the System Reference · the full rules and the GM's half live there.</footer>
</div></body></html>"""
open("player-primer.html","w",encoding="utf-8").write(doc)
print("html bytes:", len(doc), " chapters:", len(chapters))
