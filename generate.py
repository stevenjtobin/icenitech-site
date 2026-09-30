#!/usr/bin/env python3
"""IceniTech site generator — multi-page static site from the Andraste tool registry."""
import os, re, html, shutil

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, "dist")
REGISTRY = os.path.join(ROOT, "..", "andraste-tablet", "app", "src", "main", "kotlin",
                        "com", "andraste", "tablet", "tools", "ToolRegistry.kt")

SITE = {
    "name": "IceniTech",
    "tagline": "Field tools, honest tutorials, and a community of builders.",
    "email": "stevenjtobin@gmail.com",
    "domain": "icenitech.com",
}
# Fill these with your real profile URLs.
SOCIALS = [
    ("YouTube",   "youtube",   "#"),
    ("Discord",   "discord",   "#"),
    ("Instagram", "instagram", "#"),
    ("TikTok",    "tiktok",    "#"),
    ("X",         "x",         "#"),
    ("Facebook",  "facebook",  "#"),
]

CATS = {
    "WIFI":     ("Wi-Fi",       "Discover and analyse the wireless networks around you."),
    "BLE":      ("Bluetooth",   "Find and inspect nearby Bluetooth Low Energy devices."),
    "NETWORK":  ("Network",     "Map and probe the devices and services on a network."),
    "NFC":      ("NFC",         "Read and work with NFC tags and cards."),
    "LOCATION": ("Location",    "Position, satellites and location logging."),
    "CAMERA":   ("Camera",      "Use the camera for scanning and inspection."),
    "SDR":      ("Radio (SDR)", "Receive and decode radio signals with an SDR dongle."),
    "TERMINAL": ("Terminal",    "Run the Linux security toolchain through Termux."),
    "FILES":    ("Files",       "Browse, inspect and share files and captures."),
    "TRIBE":    ("Dashboard",   "A live overview of your surroundings and your progress."),
    "SYSTEM":   ("System",      "Device info, permissions, updates and settings."),
}
CAT_ORDER = ["WIFI","BLE","NETWORK","LOCATION","CAMERA","SDR","NFC","TERMINAL","FILES","TRIBE","SYSTEM"]

VIDEO_CATS = [
    ("cyber-security", "Cyber Security", "Hands-on security, tooling and defence."),
    ("coding",         "Coding & Software", "Building real software, from scripts to services."),
    ("ai",             "AI", "Practical AI — coding assistants, models and automation."),
    ("crypto",         "Crypto & Mining", "Coins, wallets, and building mining infrastructure."),
    ("3d-printing",    "3D Printing", "Design, slicing and AI-assisted printing."),
    ("hardware",       "Hardware & Cyberdecks", "ESP32, tablets, Pis and field-kit builds."),
]
# Add videos here later. Each: {id(YouTube), title, desc, cats:[...], date}
VIDEOS = []

# ---- SVGs ----
LOGO = ('<svg class="mk" viewBox="0 0 32 32" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">'
        '<rect x="14.5" y="4" width="3" height="18" fill="#B07A1E"/>'
        '<path d="M16 1.5 L18 5 L14 5 Z" fill="#B07A1E"/>'
        '<rect x="9" y="20" width="14" height="2.6" fill="#B07A1E"/>'
        '<circle cx="16" cy="27" r="3.2" fill="none" stroke="#2E7D74" stroke-width="2"/></svg>')
ICONS = {
 "youtube":'<svg viewBox="0 0 24 24"><path d="M23 12s0-3.9-.5-5.8a3 3 0 0 0-2.1-2.1C18.5 3.5 12 3.5 12 3.5s-6.5 0-8.4.6A3 3 0 0 0 1.5 6.2C1 8.1 1 12 1 12s0 3.9.5 5.8a3 3 0 0 0 2.1 2.1c1.9.6 8.4.6 8.4.6s6.5 0 8.4-.6a3 3 0 0 0 2.1-2.1C23 15.9 23 12 23 12zM10 15.5v-7l6 3.5-6 3.5z"/></svg>',
 "discord":'<svg viewBox="0 0 24 24"><path d="M20 4.4A19 19 0 0 0 15.3 3l-.2.5a14 14 0 0 1 4 2 16 16 0 0 0-14 0 14 14 0 0 1 4-2L8.7 3A19 19 0 0 0 4 4.4 20 20 0 0 0 .5 18a19 19 0 0 0 5.8 3l.8-1.3a12 12 0 0 1-2-1l.5-.4a13 13 0 0 0 11 0l.5.4a12 12 0 0 1-2 1l.8 1.3a19 19 0 0 0 5.8-3A20 20 0 0 0 20 4.4zM8.5 14.5c-1 0-1.8-1-1.8-2.1S7.5 10.3 8.5 10.3s1.8 1 1.8 2.1-.8 2.1-1.8 2.1zm7 0c-1 0-1.8-1-1.8-2.1s.8-2.1 1.8-2.1 1.8 1 1.8 2.1-.8 2.1-1.8 2.1z"/></svg>',
 "instagram":'<svg viewBox="0 0 24 24"><path d="M12 2.2c3.2 0 3.6 0 4.9.1 1.2.1 1.8.3 2.2.4.6.2 1 .5 1.4.9.4.4.7.8.9 1.4.1.4.3 1 .4 2.2.1 1.3.1 1.7.1 4.9s0 3.6-.1 4.9c-.1 1.2-.3 1.8-.4 2.2-.2.6-.5 1-.9 1.4-.4.4-.8.7-1.4.9-.4.1-1 .3-2.2.4-1.3.1-1.7.1-4.9.1s-3.6 0-4.9-.1c-1.2-.1-1.8-.3-2.2-.4-.6-.2-1-.5-1.4-.9-.4-.4-.7-.8-.9-1.4-.1-.4-.3-1-.4-2.2C2.2 15.6 2.2 15.2 2.2 12s0-3.6.1-4.9c.1-1.2.3-1.8.4-2.2.2-.6.5-1 .9-1.4.4-.4.8-.7 1.4-.9.4-.1 1-.3 2.2-.4C8.4 2.2 8.8 2.2 12 2.2zM12 0C8.7 0 8.3 0 7 .1 5.7.1 4.8.3 4.1.6c-.8.3-1.4.7-2 1.4-.7.6-1.1 1.2-1.4 2C.3 4.8.1 5.7.1 7 0 8.3 0 8.7 0 12s0 3.7.1 5c0 1.3.2 2.2.5 2.9.3.8.7 1.4 1.4 2 .6.7 1.2 1.1 2 1.4.7.3 1.6.5 2.9.5 1.3.1 1.7.1 5 .1s3.7 0 5-.1c1.3 0 2.2-.2 2.9-.5.8-.3 1.4-.7 2-1.4.7-.6 1.1-1.2 1.4-2 .3-.7.5-1.6.5-2.9.1-1.3.1-1.7.1-5s0-3.7-.1-5c0-1.3-.2-2.2-.5-2.9-.3-.8-.7-1.4-1.4-2-.6-.7-1.2-1.1-2-1.4C19.2.3 18.3.1 17 .1 15.7 0 15.3 0 12 0zm0 5.8A6.2 6.2 0 1 0 18.2 12 6.2 6.2 0 0 0 12 5.8zm0 10.2A4 4 0 1 1 16 12a4 4 0 0 1-4 4zm6.4-10.9a1.44 1.44 0 1 0 1.44 1.44 1.44 1.44 0 0 0-1.44-1.44z"/></svg>',
 "tiktok":'<svg viewBox="0 0 24 24"><path d="M16.5 2h-3v13a2.5 2.5 0 1 1-2.5-2.5c.2 0 .4 0 .5.1V9.5a5.6 5.6 0 0 0-.5 0A5.5 5.5 0 1 0 16.5 15V8.3a7 7 0 0 0 4 1.3V6.5a4 4 0 0 1-4-4z"/></svg>',
 "x":'<svg viewBox="0 0 24 24"><path d="M18.9 2H22l-7.6 8.7L23.3 22h-6.9l-5.4-7-6.2 7H1.6l8.2-9.3L1 2h7.1l4.9 6.5L18.9 2zm-1.2 18h1.9L7.2 4H5.2l12.5 16z"/></svg>',
 "facebook":'<svg viewBox="0 0 24 24"><path d="M24 12a12 12 0 1 0-13.9 11.9v-8.4H7v-3.5h3.1V9.4c0-3 1.8-4.7 4.5-4.7 1.3 0 2.7.2 2.7.2v3h-1.5c-1.5 0-2 .9-2 1.9v2.2h3.4l-.5 3.5h-2.9v8.4A12 12 0 0 0 24 12z"/></svg>',
 "play":'<svg viewBox="0 0 24 24"><path d="M8 5v14l11-7z"/></svg>',
 "menu":'<svg viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 6h18M3 12h18M3 18h18"/></svg>',
}

def parse_tools():
    txt = open(REGISTRY, encoding="utf-8").read()
    tools = []
    pat = re.compile(r'ToolDef\(\s*"([^"]+)",\s*"([^"]+)",\s*ToolCategory\.(\w+),\s*"([^"]*)"(.*?)\)\s*,?\s*(?://.*)?$', re.M)
    for m in pat.finditer(txt):
        tid, name, cat, desc, rest = m.groups()
        risk = "PASSIVE"
        rm = re.search(r'RiskLevel\.(\w+)', rest)
        if rm: risk = rm.group(1)
        caps = set(re.findall(r'Capability\.(\w+)', rest))
        impl = "isImplemented = true" in rest
        root = "requiresRoot = true" in rest
        hw = None
        hm = re.search(r'requiresHardware = "([^"]*)"', rest)
        if hm: hw = hm.group(1)
        tools.append(dict(id=tid,name=name,cat=cat,desc=desc,risk=risk,caps=caps,
                          impl=impl,root=root,hw=hw))
    return tools

def esc(s): return html.escape(s, quote=True)
def rel(depth): return "../"*depth

def social_row(depth, cls="socials"):
    out = f'<div class="{cls}">'
    for label, key, url in SOCIALS:
        out += f'<a href="{url}" target="_blank" rel="noopener me" aria-label="{label}" title="{label}">{ICONS[key]}</a>'
    return out + "</div>"

def head(title, desc, depth):
    p = rel(depth)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Literata:ital,opsz,wght@0,7..72,400;0,7..72,600;0,7..72,700;1,7..72,400&family=Geist:wght@300;400;500;600&family=Geist+Mono:wght@400;500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{p}assets/style.css">
</head>
<body>"""

def nav(depth, active=""):
    p = rel(depth)
    links = [("home","Home",f"{p}index.html"),("software","Software",f"{p}software/index.html"),
             ("tools","Tools",f"{p}tools/index.html"),("videos","Videos",f"{p}videos/index.html"),
             ("about","About",f"{p}about.html")]
    ln = "".join(f'<a href="{href}" class="{ "active" if key==active else "" }">{label}</a>' for key,label,href in links)
    return f"""<header class="nav"><div class="wrap nav-in">
<a class="brand" href="{p}index.html">{LOGO} {SITE['name']}</a>
<nav class="nav-links" id="navlinks">{ln}<a href="{p}community.html" class="{ 'active' if active=='community' else '' }">Community</a></nav>
<div class="nav-right">{social_row(depth)}
<button class="nav-toggle" onclick="document.getElementById('navlinks').classList.toggle('open')" aria-label="Menu">{ICONS['menu']}</button></div>
</div></header>"""

def footer(depth):
    p = rel(depth)
    return f"""<footer><div class="wrap"><div class="foot">
<div><div class="brand">{LOGO} {SITE['name']}</div>
<p style="max-width:34ch;margin-top:12px;font-size:.92rem">{SITE['tagline']} Built in Norfolk, UK.</p>
{social_row(depth)}</div>
<div><h4>Software</h4><ul>
<li><a href="{p}software/andraste-tablet.html">Andraste — Tablet</a></li>
<li><a href="{p}software/andraste-cyd.html">Andraste — CYD</a></li>
<li><a href="{p}tools/index.html">All tools</a></li></ul></div>
<div><h4>Learn</h4><ul>
<li><a href="{p}videos/index.html">Videos</a></li>
<li><a href="{p}community.html">Community</a></li>
<li><a href="{p}about.html">About</a></li></ul></div>
<div><h4>Code</h4><ul>
<li><a href="https://github.com/stevenjtobin/andraste-fire" target="_blank" rel="noopener">Source</a></li>
<li><a href="https://github.com/stevenjtobin/andraste-ota/releases" target="_blank" rel="noopener">Downloads</a></li>
<li><a href="https://github.com/stevenjtobin" target="_blank" rel="noopener">GitHub</a></li></ul></div>
</div>
<div class="fineprint"><span>© 2026 {SITE['name']} · open source, AGPL-3.0</span><span class="mono">Made in Norfolk</span></div>
</div></footer></body></html>"""

def write(path, title, desc, body, depth, active=""):
    full = head(title, desc, depth) + nav(depth, active) + body + footer(depth)
    fp = os.path.join(OUT, path)
    os.makedirs(os.path.dirname(fp), exist_ok=True)
    open(fp, "w", encoding="utf-8").write(full)

def risk_badge(risk):
    cls = {"PASSIVE":"passive","ACTIVE":"active","OFFENSIVE":"offensive"}[risk]
    lbl = {"PASSIVE":"Passive","ACTIVE":"Active","OFFENSIVE":"Advanced"}[risk]
    return f'<span class="badge {cls}">{lbl}</span>'

# ---------- content helpers for manual pages ----------
def beginner_what(t):
    cat = CATS[t["cat"]][0]
    base = t["desc"]
    lead = {
        "WIFI":"This is a Wi-Fi tool. ",
        "BLE":"This is a Bluetooth tool. ",
        "NETWORK":"This is a network tool. ",
        "LOCATION":"This is a location tool. ",
        "CAMERA":"This uses the camera. ",
        "SDR":"This is a radio (SDR) tool. ",
        "NFC":"This is an NFC tool. ",
        "TERMINAL":"This runs in the terminal. ",
        "FILES":"This is a file tool. ",
        "TRIBE":"This is a dashboard view. ",
        "SYSTEM":"This is a system tool. ",
    }[t["cat"]]
    return lead + base + "."

def how_to(t):
    steps = []
    if "TERMUX" in t["caps"]:
        steps = ["Install Termux (from F-Droid) and the tool's package, if you haven't already.",
                 f"Open <strong>{esc(t['name'])}</strong> — Andraste hands the command to Termux.",
                 "Type the target or options when prompted, then run it.",
                 "Read the output back in the Termux window."]
    elif t["cat"]=="WIFI":
        steps = [f"Open <strong>{esc(t['name'])}</strong> from the Wi-Fi category.",
                 "Make sure Location is switched on (Android needs it for Wi-Fi scanning).",
                 "Tap scan/refresh — nearby networks appear with signal, channel and security.",
                 "Tap an entry (where supported) for more detail."]
    elif t["cat"]=="BLE":
        steps = [f"Open <strong>{esc(t['name'])}</strong> from the Bluetooth category.",
                 "Tap start — nearby Bluetooth LE devices are listed as they're found.",
                 "Watch signal strength and any decoded details update live.",
                 "Tap stop when you're done to save battery."]
    elif t["cat"]=="NETWORK":
        steps = [f"Connect the device to the network you want to look at.",
                 f"Open <strong>{esc(t['name'])}</strong> and enter the target (host/IP or range).",
                 "Run it — results stream in as they're found.",
                 "Review the findings; export or share if the tool supports it."]
    elif t["cat"]=="LOCATION":
        steps = [f"Open <strong>{esc(t['name'])}</strong> and grant location permission if asked.",
                 "Give it a moment to get a fix from GPS / the network.",
                 "Read the live values; start/stop logging where offered."]
    elif t["cat"]=="CAMERA":
        steps = [f"Open <strong>{esc(t['name'])}</strong> and allow camera access.",
                 "Point the camera at your subject.",
                 "The result appears on screen automatically."]
    elif t["cat"]=="FILES":
        steps = [f"Open <strong>{esc(t['name'])}</strong>.",
                 "Pick the file or folder you want to work with.",
                 "The tool processes it and shows the result; share or export as needed."]
    elif t["cat"]=="SDR":
        steps = ["Plug an RTL-SDR dongle into the tablet with a USB-OTG cable.",
                 f"Open <strong>{esc(t['name'])}</strong> and allow USB access.",
                 "Tune / start — decoded output appears as signals are received."]
    else:
        steps = [f"Open <strong>{esc(t['name'])}</strong> from its category.",
                 "Follow the on-screen prompts.",
                 "Review the results."]
    return "".join(f"<li>{s}</li>" for s in steps)

def hardware_notes(t):
    caps, hw, root = t["caps"], t["hw"], t["root"]
    # Tablet
    if hw and ("RTL-SDR" in hw or "LoRa" in hw or "RFID" in hw):
        tablet = f"Works on the tablet <em>once you add the required hardware</em> ({esc(hw)}) over USB-OTG. Without it, the tool is listed but inactive."
    elif "NFC" in caps or (hw and "NFC" in hw):
        tablet = "The Fire HD 8 has no NFC chip, so this is inactive on that tablet. It will work on an Android device that does have NFC."
    elif root:
        tablet = "Needs root and, for radio capture, a monitor-mode adapter. On a stock (unrooted) Fire tablet it stays inactive; see the rooting guide to enable it."
    elif "CAMERA" in caps:
        tablet = "Uses the tablet's built-in camera — works out of the box on the Fire HD 8."
    elif "FINE_LOCATION" in caps and t["cat"]=="LOCATION":
        tablet = "Uses the tablet's location services. Wi-Fi-only Fire tablets get a coarser fix than a phone with a dedicated GPS chip, but it works."
    elif "WIFI" in caps:
        tablet = "Uses the tablet's built-in 2.4 GHz Wi-Fi. Passive scanning works out of the box (with Location switched on)."
    elif "BLUETOOTH" in caps:
        tablet = "Uses the tablet's built-in Bluetooth — works out of the box."
    elif "TERMUX" in caps:
        tablet = "Runs through Termux on the tablet. Install Termux and the relevant package once, and it's ready."
    else:
        tablet = "Runs natively on the tablet — no extra hardware needed."
    # CYD / ESP32
    if "CAMERA" in caps:
        cyd = "The ESP32 cyberdeck boards have no camera, so this is tablet-only."
    elif "TERMUX" in caps:
        cyd = "The CYD runs its own firmware rather than Linux, so terminal tools are a tablet feature. The board has its own built-in equivalents where it makes sense."
    elif "USB_HOST" in caps:
        cyd = "SDR and USB add-ons attach differently on the ESP32 — support depends on the board and firmware build."
    elif "WIFI" in caps:
        cyd = "The ESP32's Wi-Fi radio can do more low-level Wi-Fi work than a stock tablet, so several of these have strong CYD equivalents."
    elif "BLUETOOTH" in caps:
        cyd = "The ESP32 has Bluetooth too, so a version of this runs on the CYD."
    elif "FINE_LOCATION" in caps:
        cyd = "The CYD needs an add-on GPS module for location features."
    else:
        cyd = "A comparable feature is available in the CYD firmware where the hardware allows."
    return tablet, cyd

def safety_note(risk):
    if risk=="PASSIVE":
        return ('<div class="callout"><strong>Safe to explore.</strong> This is a passive / read-only tool — '
                'it listens and reports, it doesn\'t change anything or transmit attacks.</div>')
    if risk=="ACTIVE":
        return ('<div class="callout warn"><strong>Use responsibly.</strong> This tool actively touches the target. '
                'Only run it against networks and devices you own or are explicitly authorised to test.</div>')
    return ('<div class="callout danger"><strong>Advanced — authorised use only.</strong> This is powerful tooling. '
            'Use it strictly on systems you own or have written permission to assess.</div>')
