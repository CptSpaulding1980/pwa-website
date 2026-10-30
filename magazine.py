"""Data-driven homepage components; reads generated content, never authors canon."""
from html import escape
from pathlib import Path
import re


def display_date(value):
    parts = value.split('-')
    return '{}.{}.{}'.format(parts[2], parts[1], parts[0][-2:]) if len(parts) == 3 else value


def homepage(events, wrestlers, champs, docs, prefix, video=''):
    latest = sorted(events, key=lambda row: row['date'], reverse=True)[:10]
    events_html = []
    for event in latest:
        events_html.append('<a class="event-link" href="{p}/events/{s}/"><time class="event-date" datetime="{date}">{d}</time><span class="event-title">{t}<small>{v}</small></span><span class="event-count">{n} Matches <span aria-hidden="true">↗</span></span></a>'.format(
            p=prefix, s=event['slug'], date=event['date'], d=display_date(event['date']), t=escape(event['title']), v=escape(event['venue']), n=event['match_count']))
    champions_html = []
    for champ in champs:
        source = (docs / 'championships' / champ['slug'] / 'index.html').read_text(encoding='utf-8')
        current = re.search(r'<p>Current Champion:\s*(.*?)</p>', source, re.S)
        image = re.search(r'<h1>\s*(<img\b[^>]*>)', source)
        belt = image.group(1) if image else ''
        if belt:
            belt = re.sub(r'\s(?:style|width)="[^"]*"', '', belt)
            if 'alt=' not in belt:
                belt = belt.replace('<img ', '<img alt="{}" '.format(escape(champ['name'], quote=True)))
        champions_html.append('<article class="champion-card">{image}<div><a class="title-link" href="{p}/championships/{s}/">{title}</a><div class="champion-name">{current}</div></div></article>'.format(
            image=belt, p=prefix, s=champ['slug'], title=escape(champ['name']), current=current.group(1) if current else 'Titelhistorie ansehen'))
    ranking_path = docs / 'rankings' / 'pwi-500' / 'index.html'
    ranking = ranking_path.read_text(encoding='utf-8') if ranking_path.exists() else ''
    ranking_body = re.search(r'<tbody>(.*?)</tbody>', ranking, re.S)
    rank_rows = []
    if ranking_body:
        for row in re.findall(r'<tr>(.*?)</tr>', ranking_body.group(1), re.S)[:5]:
            cells = re.findall(r'<td[^>]*>(.*?)</td>', row, re.S)
            if len(cells) == 8:
                rank_rows.append('<tr><td>{}</td><td>{}</td><td>{}</td></tr>'.format(cells[0], cells[1], cells[7]))
    # Show a real, poster-backed event as an archive feature (not as the latest show).
    feature = ''
    for event in sorted(events, key=lambda row: row['date'], reverse=True):
        posters = sorted((docs / 'img' / 'posters').glob(event['date'] + '*'))
        if posters:
            feature = '<section class="archive-feature"><a class="poster-link" href="{p}/events/{s}/"><img src="{p}/img/posters/{img}" alt="{t} – Eventposter" width="240" height="320" loading="lazy"></a><div><span class="eyebrow">Im Archiv · {date}</span><h2><a href="{p}/events/{s}/">{t}</a></h2><p>{venue} · {n} Matches</p><a class="button" href="{p}/events/{s}/">Ergebnisse ansehen <span aria-hidden="true">↗</span></a></div></section>'.format(
                p=prefix, s=event['slug'], img=escape(posters[0].name, quote=True), t=escape(event['title']), date=display_date(event['date']), venue=escape(event['venue']), n=event['match_count'])
            break
    stats = ''.join('<a class="stat-item" href="{p}/{route}/"><strong>{n}</strong><span>{label} <span aria-hidden="true">↗</span></span></a>'.format(p=prefix, route=route, n=n, label=label) for route, n, label in [('events',len(events),'Events'), ('wrestlers',len(wrestlers),'Wrestler'), ('championships',len(champs),'Championships')])
    latest_date = display_date(latest[0]['date']) if latest else '–'
    return '''<section class="home-intro"><div><span class="eyebrow">Die parallele Wrestling-Welt</span><h1>Harte Matches.<br><span>Klare Fakten.</span></h1><p>Von den Anfängen im NAWA-Territorium über die Underground-Ära bis zur Renaissance: das PWA-Archiv auf einen Blick.</p></div><div class="archive-status"><span class="status-dot"></span> Letzter Eventstand<strong>{latest_date}</strong><a href="{p}/events/">Zum Eventarchiv ↗</a></div></section>
{video}
<div class="stats-strip">{stats}</div>
<div class="magazine-grid"><section class="panel latest-panel"><div class="section-heading"><h2>Die letzten Events</h2><a href="{p}/events/">Alle Events ↗</a></div><div class="event-list">{events}</div></section>
<aside class="panel ranking-panel"><span class="eyebrow">PWI Power Ranking</span><h2>Die Top 5</h2><div class="ranking-preview"><table><thead><tr><th scope="col">#</th><th scope="col">Wrestler</th><th scope="col">Pts</th></tr></thead><tbody>{ranks}</tbody></table></div><a class="button" href="{p}/rankings/pwi-500/">Komplettes Ranking ↗</a><div class="stat-links"><a href="{p}/rankings/top-25-matches/">Statistiken ↗</a><a href="{p}/rankings/worst-25-matches/">Worst 25 Matches ↗</a></div></aside></div>
<section class="panel champions-panel"><div class="section-heading"><div><span class="eyebrow">Titelträger laut Archiv</span><h2>Die Champions</h2></div><a href="{p}/championships/">Alle Titelhistorien ↗</a></div><div class="champion-grid">{champions}</div></section>
{feature}'''.format(p=prefix, latest_date=latest_date, video=video, stats=stats, events=''.join(events_html), ranks=''.join(rank_rows), champions=''.join(champions_html), feature=feature)
