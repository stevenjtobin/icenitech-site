# prasutagus-site

The public website for Prasutagus — https://prasutagus.com

Static site (no build step). The served directory is `dist/`.

## Deploy (on the Contabo VPS)
nginx serves `prasutagus.com` from `/var/www/prasutagus/dist`. To update:

```bash
cd /var/www/prasutagus
# first time:  git clone https://github.com/stevenjtobin/prasutagus-site .
git pull
# nginx already points at /var/www/prasutagus/dist — no reload needed for static files
```

## Structure
- `dist/index.html` — the landing page (inline CSS, Google Fonts: Literata + Geist)
- `dist/assets/` — screenshots and images

House style: cool-grey paper #F3F5F7, graphite #171B21, torc-gold #8C6210, link #1F4F8A.
