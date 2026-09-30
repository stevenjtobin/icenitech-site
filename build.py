#!/usr/bin/env python3
"""Page builders + runner for the IceniTech site (imports helpers from generate.py)."""
from generate import *
import os

def build_index(tools):
    n = len(tools); impl = sum(1 for t in tools if t["impl"])
    topics = "".join(f'<a class="pill" href="videos/{cid}.html">{esc(lbl)}</a>' for cid,lbl,_ in VIDEO_CATS)
    body = f"""
<section class="hero"><div class="wrap">
<span class="eyebrow">Open-source tools · tutorials · community</span>
<h1>Build, learn, and tinker&nbsp;— together.</h1>
<p class="lede">Hi, I'm Steven. I build open-source field tools and share honest, hands-on tutorials across cyber security, coding, AI, crypto, 3D printing and hardware — and I'm gathering a community of people who like to make and understand their own kit.</p>
<div class="hero-cta">
<a class="btn btn-primary" href="software/index.html">Explore the software</a>
<a class="btn btn-ghost" href="videos/index.html">Watch &amp; learn</a>
<a class="btn btn-gold" href="community.html">Join the community</a>
</div>
<div style="margin-top:34px">{topics}</div>
</div></section>

<section class="soft"><div class="wrap">
<div class="section-head"><span class="eyebrow">What you'll find here</span><h2>Made to be used, and understood.</h2>
<p>Everything is open, documented for beginners, and yours to learn from.</p></div>
<div class="grid g3">
<a class="card" href="software/index.html"><div class="ico">🛠️</div><h3>Software</h3><p>Free, open-source field toolkits for tablets and microcontrollers — with a full guide and a manual for every single tool.</p></a>
<a class="card" href="videos/index.html"><div class="ico">🎥</div><h3>Videos &amp; guides</h3><p>Step-by-step builds and explainers, sorted into clear topics so you can follow the thread you care about.</p></a>
<a class="card" href="community.html"><div class="ico">🤝</div><h3>Community</h3><p>A friendly place for builders, tinkerers and the security-curious. Come say hello, share what you're making.</p></a>
</div></div></section>

<section class="band"><div class="wrap">
<div class="section-head"><span class="eyebrow">Featured software</span><h2>Andraste — a field toolkit in your pocket.</h2>
<p>A native app that turns an ordinary tablet into a {n}-tool field kit — {impl} tools working today across Wi-Fi, Bluetooth, network, location, camera and more. Free, open source, and it updates itself over the air.</p></div>
<div class="hero-cta">
<a class="btn btn-gold" href="software/andraste-tablet.html">Read the guide</a>
<a class="btn btn-ghost" style="color:#fff;border-color:rgba(255,255,255,.25)" href="https://github.com/stevenjtobin/andraste-ota/releases/latest" target="_blank" rel="noopener">Download</a>
</div></div></section>

<section><div class="wrap"><div class="join">
<span class="eyebrow" style="color:var(--gold)">Come build with us</span>
<h2>Join a community of makers.</h2>
<p>New videos, project files, early builds and a place to ask questions. Follow along wherever you like — and jump into the chat.</p>
{social_row(0,'socials')}
<div class="hero-cta" style="justify-content:center;margin-top:24px"><a class="btn btn-gold" href="community.html">See how to join</a></div>
</div></div></section>
"""
    write("index.html", f"{SITE['name']} — {SITE['tagline']}",
          "Open-source field tools, hands-on tutorials and a community of builders across cyber security, coding, AI, crypto, 3D printing and hardware.",
          body, 0, "home")

def build_about(tools):
    body = f"""
<section class="hero"><div class="wrap doc">
<span class="eyebrow">About</span>
<h1>Hi, I'm Steven.</h1>
<p class="sub">I'm a builder and tinkerer from Norfolk, England, working across cyber security, coding, AI, crypto and hardware — and sharing all of it openly.</p>
</div></section>
<section><div class="wrap doc">
<p>I make things because I'd rather understand my tools than rent them. That started with small hardware builds and grew into full field toolkits, home-lab projects, mining experiments and AI-assisted workflows. Along the way I kept notes, recorded what worked, and open-sourced the results.</p>
<p>This site is where all of that lives: the <a href="software/index.html">software I build</a>, the <a href="videos/index.html">videos and guides</a> where I show how it works, and a <a href="community.html">community</a> for people who share the itch to make and learn.</p>
<h2>What I work on</h2>
<ul>
<li><strong>Cyber security</strong> — field tools, detection, and learning the craft defensively.</li>
<li><strong>Coding &amp; software</strong> — from small scripts to real services and infrastructure.</li>
<li><strong>AI</strong> — practical, everyday AI: coding assistants, automation, and creative uses.</li>
<li><strong>Crypto &amp; mining</strong> — coins, wallets, and building the infrastructure behind them.</li>
<li><strong>3D printing &amp; hardware</strong> — designing, printing, and building cyberdecks and kit.</li>
</ul>
<h2>How I build</h2>
<div class="callout"><strong>Open, honest, and beginner-friendly.</strong> Everything is documented so someone new can follow it. Security tooling is defensive and educational by default — detectors and scanners, not attacks — and meant only for systems you own or are authorised to test.</div>
<p>If any of that sounds like your kind of thing, I'd love for you to <a href="community.html">join in</a>.</p>
</div></section>
"""
    write("about.html", f"About — {SITE['name']}",
          "Steven from Norfolk builds open-source field tools and shares tutorials across cyber security, coding, AI, crypto and hardware.",
          body, 0, "about")

def build_community():
    cards = "".join(
        f'<a class="card" href="{url}" target="_blank" rel="noopener"><div class="ico">{ICONS[key]}</div><h3>{label}</h3><p>Follow along and say hello.</p></a>'
        for label,key,url in SOCIALS)
    body = f"""
<section class="hero"><div class="wrap">
<span class="eyebrow">Community</span>
<h1>Come build with us.</h1>
<p class="lede">Whether you're deep into this already or just curious, there's a place for you. Follow the videos, grab the tools, and join the conversation — questions very welcome.</p>
</div></section>
<section class="soft"><div class="wrap">
<div class="section-head"><h2>Find me here</h2><p>Pick whichever suits you — it all helps grow a friendly, sharp little community.</p></div>
<div class="grid g3">{cards}</div>
<p class="muted" style="margin-top:24px;font-size:.9rem">Links being wired up — the icons in the header and footer point to these too.</p>
</div></section>
<section><div class="wrap doc">
<h2>The vibe</h2>
<p>Helpful, curious and honest. Share what you're making, ask the "silly" question, and keep it legal and ethical — security tools here are for learning and for systems you're allowed to test.</p>
</div></section>
"""
    write("community.html", f"Community — {SITE['name']}",
          "Join a friendly community of builders and the security-curious — on YouTube, Discord and more.",
          body, 0, "community")

def build_software_index():
    body = f"""
<section class="hero"><div class="wrap">
<span class="eyebrow">Software</span>
<h1>Open-source field toolkits.</h1>
<p class="lede">Free to download, documented for beginners, and built to run on hardware you already have. Each one has a full guide and a manual for every tool.</p>
</div></section>
<section><div class="wrap"><div class="grid g2">
<a class="card" href="andraste-tablet.html"><div class="ico">📱</div><h3>Andraste — Tablet Edition</h3>
<p>A native Android app that turns an Amazon Fire tablet into a field kit — Wi-Fi, Bluetooth, network, location, camera, files and a terminal bridge. Updates over the air.</p>
<p style="margin-top:12px"><span class="badge gold">Guide + manuals</span></p></a>
<a class="card" href="andraste-cyd.html"><div class="ico">🖥️</div><h3>Andraste — CYD (ESP32)</h3>
<p>The original cyberdeck firmware for the ESP32 "Cheap Yellow Display" — a self-contained handheld that pulls over-the-air updates once flashed.</p>
<p style="margin-top:12px"><span class="badge gold">Guide + firmware</span></p></a>
</div>
<div class="empty" style="margin-top:20px">More builds are on the way — follow the <a href="../videos/index.html">videos</a> to see them as they land.</div>
</div></section>
"""
    write("software/index.html", f"Software — {SITE['name']}",
          "Andraste field toolkits for tablets and ESP32 boards — free, open source, fully documented.",
          body, 1, "software")

def guide_tool_rows(tools, depth):
    p = rel(depth)
    out = ""
    for cat in CAT_ORDER:
        ct = [t for t in tools if t["cat"]==cat]
        if not ct: continue
        name, blurb = CATS[cat]
        rows = ""
        for t in ct:
            badges = risk_badge(t["risk"])
            if t["root"]: badges += ' <span class="badge">Root</span>'
            if t["hw"]: badges += f' <span class="badge">{esc(t["hw"])}</span>'
            if t["impl"]: badges += ' <span class="badge passive">Ready</span>'
            rows += f"""<div class="toolrow"><div class="tx">
<div class="nm">{esc(t['name'])}</div><div class="ds">{esc(t['desc'])}</div>
<div class="badges">{badges}</div></div>
<div class="act"><a class="btn btn-ghost" href="{p}tools/{esc(t['id'])}.html">Manual →</a></div></div>"""
        out += f'<div class="toolcat"><h3>{esc(name)} <span class="cnt">{len(ct)} tools</span></h3><p class="muted" style="margin:-6px 0 8px">{esc(blurb)}</p>{rows}</div>'
    return out

def build_tablet_guide(tools):
    n=len(tools); impl=sum(1 for t in tools if t["impl"])
    body = f"""
<section class="hero"><div class="wrap doc">
<div class="breadcrumb"><a href="index.html">Software</a> / Andraste — Tablet Edition</div>
<span class="eyebrow">Software guide</span>
<h1>Andraste — Tablet Edition</h1>
<p class="sub">{n} tools in one native app for the Amazon Fire HD 8 — {impl} working today, the rest ready as you add hardware or root. Free, open source, updates over Wi-Fi.</p>
<div class="hero-cta">
<a class="btn btn-primary" href="https://github.com/stevenjtobin/andraste-ota/releases/latest" target="_blank" rel="noopener">Download APK</a>
<a class="btn btn-ghost" href="https://github.com/stevenjtobin/andraste-fire" target="_blank" rel="noopener">Source</a></div>
</div></section>
<section><div class="wrap doc">
<h2>What it is</h2>
<p>Andraste is an app-launcher of field tools, grouped by category. It runs natively on the tablet's own radios, camera and sensors — no Google services needed — and bridges to the Linux security toolchain through Termux. Tools are badged by risk so you always know what a tool does before you run it.</p>
<h2>Getting started</h2>
<ol>
<li><strong>Turn on developer options</strong> on the Fire tablet and enable installing apps over USB (or from unknown sources).</li>
<li><strong>Install the APK</strong> — grab it from the <a href="https://github.com/stevenjtobin/andraste-ota/releases/latest" target="_blank" rel="noopener">latest release</a> and open it to install.</li>
<li><strong>Grant permissions</strong> (Location, Camera, etc.) from the Permissions screen — Android needs Location switched on for Wi-Fi and Bluetooth scanning.</li>
<li><strong>Update over the air</strong> from <em>System → OTA Update</em> — no cable needed after the first install.</li>
</ol>
<div class="callout"><strong>New here?</strong> Every tool below has a plain-English manual — tap <em>Manual →</em> to see what it does, how to use it, and what to expect on your hardware.</div>
<h2>The tools</h2>
<p class="muted">Grouped by category. Badges: <span class="badge passive">Passive</span> read-only · <span class="badge active">Active</span> touches the target · <span class="badge offensive">Advanced</span> authorised use only · <span class="badge">Ready</span> working today.</p>
{guide_tool_rows(tools,1)}
</div></section>
"""
    write("software/andraste-tablet.html", "Andraste Tablet — full guide",
          "Full guide to Andraste Tablet Edition: install, permissions, OTA updates, and a manual for every tool.",
          body, 1, "software")

def build_cyd_guide(tools):
    cyd_cats = ["WIFI","BLE","NETWORK","LOCATION","TRIBE","SYSTEM"]
    ct = [t for t in tools if t["cat"] in cyd_cats and not t["hw"] and "TERMUX" not in t["caps"] and "CAMERA" not in t["caps"]]
    body = f"""
<section class="hero"><div class="wrap doc">
<div class="breadcrumb"><a href="index.html">Software</a> / Andraste — CYD</div>
<span class="eyebrow">Software guide</span>
<h1>Andraste — CYD (ESP32)</h1>
<p class="sub">The original Andraste: a self-contained cyberdeck firmware for the ESP32 "Cheap Yellow Display" board — a handheld field tool with its own screen, Wi-Fi and Bluetooth.</p>
<div class="hero-cta">
<a class="btn btn-primary" href="https://github.com/stevenjtobin/andraste-ota/releases" target="_blank" rel="noopener">Firmware releases</a></div>
</div></section>
<section><div class="wrap doc">
<h2>What it is</h2>
<p>The CYD build runs directly on an ESP32 microcontroller with a built-in touchscreen — no phone or tablet required. Because it's close to the metal, its Wi-Fi and Bluetooth radios can do lower-level work than a stock tablet, while the tablet edition wins on storage, camera, GPS and the full Linux toolchain.</p>
<h2>Flashing it</h2>
<ol>
<li>Get a supported ESP32 "Cheap Yellow Display" board.</li>
<li>Download the latest firmware from the <a href="https://github.com/stevenjtobin/andraste-ota/releases" target="_blank" rel="noopener">releases page</a>.</li>
<li>Flash it over USB, then it pulls over-the-air updates on its own after that.</li>
</ol>
<div class="callout"><strong>Tablet vs CYD.</strong> Many tools exist in both. Each tool's manual has a "what happens on your hardware" section explaining the difference — camera and terminal tools are tablet-only; several Wi-Fi tools are stronger on the CYD.</div>
<h2>Tools that fit the CYD</h2>
<p class="muted">A representative set that maps well to ESP32 hardware. Open a manual for the full picture.</p>
{guide_tool_rows(ct,1)}
</div></section>
"""
    write("software/andraste-cyd.html", "Andraste CYD — guide",
          "Guide to the Andraste CYD (ESP32) cyberdeck firmware: what it is, flashing, and how it compares to the tablet edition.",
          body, 1, "software")

def build_tool_pages(tools):
    for t in tools:
        cat_name = CATS[t["cat"]][0]
        tablet, cyd = hardware_notes(t)
        reqs = ", ".join(sorted(c.replace("_"," ").title() for c in t["caps"])) or "None"
        status = "Working today" if t["impl"] else ("Needs the hardware above" if t["hw"] else ("Needs root" if t["root"] else "Coming soon"))
        body = f"""
<section><div class="wrap doc" style="padding-top:40px">
<div class="breadcrumb"><a href="../index.html">Home</a> / <a href="index.html">Tools</a> / {esc(t['name'])}</div>
<h1>{esc(t['name'])}</h1>
<p class="sub">{esc(t['desc'])}.</p>
<div class="meta-row">{risk_badge(t['risk'])}
<span class="badge gold">{esc(cat_name)}</span>
{'<span class="badge">Root</span>' if t['root'] else ''}
{f'<span class="badge">{esc(t["hw"])}</span>' if t['hw'] else ''}
<span class="badge {'passive' if t['impl'] else ''}">{esc(status)}</span></div>

{safety_note(t['risk'])}

<h2>What it does</h2>
<p>{esc(beginner_what(t))}</p>

<h2>How to use it</h2>
<ol>{how_to(t)}</ol>

<h2>What happens on your hardware</h2>
<p><strong>On the Andraste Tablet:</strong> {tablet}</p>
<p><strong>On the Andraste CYD (ESP32):</strong> {cyd}</p>

<h2>At a glance</h2>
<table class="kv">
<tr><td>Category</td><td>{esc(cat_name)}</td></tr>
<tr><td>Risk level</td><td>{t['risk'].title()}</td></tr>
<tr><td>Needs</td><td>{esc(reqs)}</td></tr>
<tr><td>Extra hardware</td><td>{esc(t['hw']) if t['hw'] else 'None'}</td></tr>
<tr><td>Root required</td><td>{'Yes' if t['root'] else 'No'}</td></tr>
<tr><td>Status</td><td>{esc(status)}</td></tr>
</table>
<p style="margin-top:26px"><a class="btn btn-ghost" href="../software/andraste-tablet.html">← Back to the tablet guide</a></p>
</div></section>
"""
        write(f"tools/{t['id']}.html", f"{t['name']} — manual", f"How to use {t['name']}: {t['desc']}.", body, 1)

def build_tools_index(tools):
    rows = ""
    for cat in CAT_ORDER:
        ct = [t for t in tools if t["cat"]==cat]
        if not ct: continue
        name = CATS[cat][0]
        rows += f'<div class="toolcat"><h3>{esc(name)} <span class="cnt">{len(ct)}</span></h3>'
        for t in ct:
            s = (t['name']+" "+t['desc']+" "+name).lower()
            b = risk_badge(t['risk'])
            if t['impl']: b += ' <span class="badge passive">Ready</span>'
            rows += f'<div class="toolrow" data-s="{esc(s)}"><div class="tx"><div class="nm">{esc(t["name"])}</div><div class="ds">{esc(t["desc"])}</div><div class="badges">{b}</div></div><div class="act"><a class="btn btn-ghost" href="{esc(t["id"])}.html">Manual →</a></div></div>'
        rows += "</div>"
    js = "<script>function tf(){var q=document.getElementById('q').value.toLowerCase();document.querySelectorAll('.toolrow').forEach(function(r){r.style.display=r.dataset.s.indexOf(q)>-1?'':'none';});document.querySelectorAll('.toolcat').forEach(function(c){var any=Array.prototype.some.call(c.querySelectorAll('.toolrow'),function(r){return r.style.display!=='none';});c.style.display=any?'':'none';});}</script>"
    body = f"""
<section class="hero"><div class="wrap doc">
<span class="eyebrow">Tools</span>
<h1>Every tool, explained.</h1>
<p class="sub">{len(tools)} tools across the Andraste toolkits. Search, then open any manual for a plain-English walkthrough.</p>
<input id="q" oninput="tf()" placeholder="Search tools…" style="width:100%;margin-top:18px;padding:13px 16px;border:1px solid var(--line);border-radius:10px;font-family:var(--sans);font-size:1rem;background:#fff">
</div></section>
<section><div class="wrap doc">{rows}</div></section>{js}
"""
    write("tools/index.html", f"All tools — {SITE['name']}",
          "Search every Andraste tool and open its manual — Wi-Fi, Bluetooth, network, location, camera, radio, terminal, files and more.",
          body, 1, "tools")

def video_card(v, depth):
    cmap = dict((x[0],x[1]) for x in VIDEO_CATS)
    tags = "".join(f'<a class="pill" href="{c}.html">{esc(cmap.get(c,c))}</a>' for c in v.get("cats",[]))
    thumb = f'https://i.ytimg.com/vi/{v["id"]}/hqdefault.jpg'
    return f"""<a class="vcard" href="https://youtu.be/{v['id']}" target="_blank" rel="noopener" style="text-decoration:none;color:inherit">
<div class="vthumb" style="background:#000"><img src="{thumb}" alt="" style="width:100%;height:100%;object-fit:cover"></div>
<div class="vb"><h3>{esc(v['title'])}</h3><p class="muted" style="font-size:.9rem;margin-top:4px">{esc(v.get('desc',''))}</p>
<div class="tags">{tags}</div></div></a>"""

def build_videos():
    cards = ""
    for cid,lbl,blurb in VIDEO_CATS:
        cnt = sum(1 for v in VIDEOS if cid in v.get("cats",[]))
        cards += f'<a class="card" href="{cid}.html"><div class="ico">🎬</div><h3>{esc(lbl)}</h3><p>{esc(blurb)}</p><p style="margin-top:10px"><span class="badge gold">{cnt} video{"s" if cnt!=1 else ""}</span></p></a>'
    latest = "".join(video_card(v,1) for v in VIDEOS[:6])
    latest_block = f'<div class="vgrid">{latest}</div>' if VIDEOS else '<div class="empty">No videos published yet — new tutorials are coming. <a href="../community.html">Subscribe on YouTube</a> to be first to see them.</div>'
    body = f"""
<section class="hero"><div class="wrap">
<span class="eyebrow">Videos</span>
<h1>Watch, build, repeat.</h1>
<p class="lede">Tutorials and build logs, sorted into clear topics. A video often fits more than one — so you'll find, say, a mining-pool build under both Crypto and Coding.</p>
</div></section>
<section class="soft"><div class="wrap">
<div class="section-head"><h2>Browse by topic</h2></div>
<div class="grid g3">{cards}</div>
</div></section>
<section><div class="wrap">
<div class="section-head"><h2>Latest</h2></div>
{latest_block}
</div></section>
"""
    write("videos/index.html", f"Videos — {SITE['name']}",
          "Tutorials and build logs across cyber security, coding, AI, crypto, 3D printing and hardware.",
          body, 1, "videos")
    for cid,lbl,blurb in VIDEO_CATS:
        vids = [v for v in VIDEOS if cid in v.get("cats",[])]
        grid = "".join(video_card(v,1) for v in vids)
        block = f'<div class="vgrid">{grid}</div>' if vids else '<div class="empty">Nothing here yet — this topic is coming soon. <a href="../community.html">Follow along</a> so you don\'t miss it.</div>'
        body = f"""
<section class="hero"><div class="wrap doc">
<div class="breadcrumb"><a href="index.html">Videos</a> / {esc(lbl)}</div>
<span class="eyebrow">Videos</span><h1>{esc(lbl)}</h1><p class="sub">{esc(blurb)}</p>
</div></section>
<section><div class="wrap">{block}</div></section>
"""
        write(f"videos/{cid}.html", f"{lbl} videos — {SITE['name']}", blurb, body, 1, "videos")

def main():
    import shutil
    if os.path.isdir(OUT):
        for f in os.listdir(OUT):
            fp = os.path.join(OUT,f)
            if f=="assets": continue
            if os.path.isdir(fp): shutil.rmtree(fp)
            elif f.endswith(".html"): os.remove(fp)
    os.makedirs(OUT, exist_ok=True)
    tools = parse_tools()
    print(f"parsed {len(tools)} tools")
    build_index(tools); build_about(tools); build_community()
    build_software_index(); build_tablet_guide(tools); build_cyd_guide(tools)
    build_tools_index(tools); build_tool_pages(tools); build_videos()
    total = sum(len(files) for _,_,files in os.walk(OUT))
    print(f"generated -> {OUT} ({total} files)")

if __name__=="__main__":
    main()
