"""PWA presentation components. Standard library only; canon lives in the vault."""
from html import escape
import re

PREFIX = '/pwa-website'
NAV = [('Start', '/'), ('Events', '/events/'), ('Wrestler', '/wrestlers/'), ('Championships', '/championships/'), ('Rankings', '/rankings/pwi-500/'), ('Match-Statistik', '/rankings/top-25-matches/')]


def page(title, body, prefix=PREFIX):
    """Apply one shared, accessible brand shell to every layout family."""
    # Older published pages contain paragraph-wrapped block HTML; normalize on import.
    body = re.sub(r'<p>\s*(</?(?:nav|div|p)\b[^>]*>)\s*</p>', r'\1', body)
    body = re.sub(r'<p>\s*(<p>.*?</p>)\s*</p>', r'\1', body)
    body = '\n'.join(line.rstrip() for line in body.splitlines())
    if '<h1' not in body:
        body = '<h1>' + escape(title) + '</h1>\n' + body
    def table_region(m):
        return '<div class="table-scroll" role="region" tabindex="0" aria-label="Datentabelle – horizontal scrollbar">' + m.group(0) + '</div>'
    body = re.sub(r'<table\b[^>]*>.*?</table>', table_region, body, flags=re.S)
    if title == 'PWA - Professional Wrestling Association':
        family = 'home'
    elif 'match-card' in body or 'class="event-list"' in body or 'href="' + prefix + '/events/"' in body:
        family = 'events'
    elif 'Current Champion' in body or 'champ-grid' in body or 'href="' + prefix + '/championships/"' in body:
        family = 'championships'
    elif 'Wrestler Index' in title or 'Advanced Stats' in body or 'href="' + prefix + '/wrestlers/"' in body:
        family = 'wrestlers'
    elif 'Ranking' in title or 'Matches' in title:
        family = 'rankings'
    else:
        family = 'home'
    links = []
    for label, href in NAV:
        active = ((family == 'home' and href == '/') or
                  (family != 'home' and href == '/' + family + '/') or
                  (family == 'rankings' and ('pwi-500' in href if 'Ranking' in title else 'top-25' in href)))
        links.append('<a href="{}{}"{}>{}</a>'.format(prefix, href, ' aria-current="page"' if active else '', label))
    return '''<!DOCTYPE html>
<html lang="de"><head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="color-scheme" content="dark">
<meta name="description" content="Das PWA Wrestling-Archiv: Events, Ergebnisse, Wrestler, Titelhistorien und Rankings.">
<title>{title} | PWA</title>
<link rel="icon" href="{prefix}/img/PWA_2019-ff.png">
<link rel="stylesheet" href="{prefix}/styles/main.css">
</head><body class="page-{family}">
<a class="skip-link" href="#main-content">Zum Inhalt</a>
<header class="site-header">
  <div class="brand-banner">
    <a class="brand-lockup" href="{prefix}/" aria-label="PWA – Startseite">
      <img class="brand-logo" src="{prefix}/img/PWA_2019-ff.png" alt="Professional Wrestling Association" width="148" height="148">
      <span class="brand-wordmark"><span class="eyebrow">Professional Wrestling Association</span><strong>PWA WRESTLING</strong><span class="brand-caption">Das Archiv. Die Matches. Die Geschichte.</span></span>
    </a>
    <span class="archive-tag">Independent spirit.<br>Wrestling history.</span>
  </div>
</header>
<nav class="top-nav" aria-label="Hauptnavigation"><div class="nav-links">{nav}</div></nav>
<main id="main-content" class="content" tabindex="-1">
{body}
</main>
<footer class="site-footer"><strong>PWA · Professional Wrestling Association</strong><p>Das Wrestling-Archiv · Ergebnisse, Titelhistorien &amp; Rankings</p><a href="{prefix}/events/">Events entdecken</a><a href="{prefix}/rankings/worst-25-matches/">Worst 25 Matches</a></footer>
</body></html>
'''.format(title=escape(title), prefix=prefix, family=family, nav=''.join(links), body=body)
