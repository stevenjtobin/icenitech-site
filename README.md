# icenitech-site

The website for **IceniTech** — https://icenitech.com — the shopfront and portfolio
for Andraste (the field security toolkit for tablets and ESP32 boards).

Static site, no build step. Served directory is `dist/`.

## Hosting (Contabo VPS, host alias `contabo`)
nginx serves `icenitech.com` as static files from `/var/www/icenitech/dist`.
(Previously this domain proxied the retired `etsyscope` app on :8082.)

To update:
```bash
# from this repo, on a machine with SSH to the VPS:
scp -r dist/* contabo:/var/www/icenitech/dist/
# static files — no nginx reload needed
```

The vhost is dev IP-locked (allow-list + deny all). To go public, remove the
`allow`/`deny` lines in /etc/nginx/sites-available/icenitech.com and reload nginx.

## Structure
- `dist/index.html` — landing page (inline CSS; Google Fonts: Literata + Geist)
- `dist/assets/` — screenshots

House style: cool-grey paper #F3F5F7, graphite #171B21, torc-gold #8C6210, link #1F4F8A.
