#!/usr/bin/env python3
"""
PWA Data Pipeline: Obsidian vault -> static HTML in docs/.
Generates complete HTML — no Eleventy needed at runtime.
"""
import os, re, yaml, shutil, json
from pathlib import Path
from datetime import datetime

REPO = Path(__file__).resolve().parent
VAULT = Path("/Volumes/SSD_4TB/nextcloud/app/data/hendrik/files/Obsidian/PWA")
DOCS = REPO / "docs"
PREFIX = "/pwa-website"

def sanitize_filename(name):
    for ch in ':*?"<>|\\/':
        name = name.replace(ch, '-')
    return name.strip()

def parse_frontmatter(text):
    if text.startswith('---'):
        parts = re.split(r'^---\s*$', text, maxsplit=2, flags=re.MULTILINE)
        if len(parts) >= 3:
            try:
                fm = yaml.safe_load(parts[1]) or {}
            except:
                fm = {}
            return fm, parts[2]
    return {}, text

def to_yaml(d):
    return yaml.dump(d, allow_unicode=True, default_flow_style=False, sort_keys=False)

# --- HTML Templates ---

HTML_HEAD = """<!DOCTYPE html>
<html lang="de">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} | PWA</title>
  <link rel="stylesheet" href="{prefix}/styles/main.css">
  <link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>🏟️</text></svg>">
</head>
<body>
  <nav class="top-nav">
    <a href="{prefix}/" class="nav-brand">🏟️ PWA</a>
    <div class="nav-links">
      <a href="{prefix}/events/">📅 Events</a>
      <a href="{prefix}/wrestlers/">🤼 Wrestler</a>
      <a href="{prefix}/championships/">🏆 Titles</a>
      <a href="{prefix}/rankings/pwi-500/">⭐ PWI 500</a>
    </div>
  </nav>
  <main class="content">
"""

HTML_FOOT = """  </main>
  <footer class="site-footer">
    <p>PWA — Pro Wrestling Action · Static Archive · 1982–2019</p>
  </footer>
</body>
</html>"""

def html_page(title, body, prefix=PREFIX):
    head = HTML_HEAD.format(title=title, prefix=prefix)
    return head + body + HTML_FOOT

def breadcrumb(parent_title, parent_url, current_title, prefix=PREFIX):
    if parent_url:
        return '<nav class="breadcrumb">\n  <a href="{p}/">Home</a> › <a href="{p}{url}">{pt}</a> › {ct}\n</nav>\n'.format(
            p=prefix, url=parent_url, pt=parent_title, ct=current_title)
    return '<nav class="breadcrumb">\n  <a href="{p}/">Home</a> › {ct}\n</nav>\n'.format(
        p=prefix, ct=current_title)


EVENT_SLUG_MAP = {}

def convert_wikilinks(text):
    def replacer(m):
        inner = m.group(1)
        if '|' in inner:
            target, alias = inner.split('|', 1)
        else:
            target = alias = inner
        target = target.strip()
        alias = alias.strip()
        slug = target.lower().replace(' ', '-')
        slug = re.sub(r'[^\w-]', '', slug)
        if re.match(r'\d{4}-\d{2}-\d{2}', target):
            if target in EVENT_SLUG_MAP:
                href = '{}/events/{}/'.format(PREFIX, EVENT_SLUG_MAP[target])
            else:
                href = '{}/events/{}/'.format(PREFIX, sanitize_filename(target))
        elif target in ['PWA World Heavyweight Championship', 'PWA International Championship',
                         'PWA Junior Heavyweight Championship', 'PWA World Tag Team Championship']:
            href = '{}/championships/{}/'.format(PREFIX, slug)
        else:
            href = '{}/wrestlers/{}/'.format(PREFIX, slug)
        return '<a href="{}">{}</a>'.format(href, alias)
    return re.sub(r'\[\[([^\]]+)\]\]', replacer, text)

def convert_inline_dataview(text):
    return re.sub(r'\(([^:]+)::\s*([^)]*)\)', r'\2', text)

def strip_dataview_blocks(text):
    return re.sub(r'```dataviewjs.*?```', '', text, flags=re.DOTALL)

def star_to_numeric(star_str):
    if not star_str:
        return 0
    stars = star_str.count('\u2605')
    bonus = 0
    if '\u00bd' in star_str: bonus = 0.5
    elif '\u00bc' in star_str: bonus = 0.25
    elif '\u00be' in star_str: bonus = 0.75
    return stars + bonus

def star_to_html(star_str):
    if not star_str:
        return ''
    return '<span class="stars">{}</span>'.format(star_str)


def process_events():
    events_dir = VAULT / "Events"
    output_dir = DOCS / "events"
    output_dir.mkdir(parents=True, exist_ok=True)
    all_events = []

    for md_file in sorted(events_dir.glob("*.md")):
        text = md_file.read_text(encoding='utf-8')
        fm, body = parse_frontmatter(text)
        if not fm.get('title'):
            continue

        matches = fm.get('matches', [])
        title = fm.get('title', '')
        event_date = str(fm.get('date', ''))
        event_slug = sanitize_filename('{} - {}'.format(event_date, title))
        EVENT_SLUG_MAP[event_date] = event_slug

        # Process matches
        processed_matches = []
        for i, m in enumerate(matches):
            name = m.get('name', '')
            finish = m.get('finish', '')
            rating_str = m.get('rating', '')
            time_match = re.search(r'(\d+)\s*Min\s*(\d+)\s*Sec', finish)
            match_time = '{}:{:02d}'.format(int(time_match.group(1)), int(time_match.group(2))) if time_match else ''
            processed_matches.append({
                'number': i + 1,
                'name': convert_wikilinks(name),
                'finish': convert_wikilinks(finish),
                'rating_stars': star_to_html(rating_str),
                'rating_num': star_to_numeric(rating_str),
                'time': match_time,
            })

        # Poster
        poster_html = ''
        poster_files = list((VAULT / "z_Images" / "Poster").glob("{}*".format(event_date)))
        if poster_files:
            dest_dir = DOCS / "img" / "posters"
            dest_dir.mkdir(parents=True, exist_ok=True)
            shutil.copy2(poster_files[0], dest_dir / poster_files[0].name)
            poster_html = '<img src="{}/img/posters/{}" class="event-poster" alt="Poster">'.format(
                PREFIX, poster_files[0].name)

        # Build match cards HTML
        match_cards = []
        for m in processed_matches:
            match_cards.append(
                '<div class="match-card">\n'
                '<span class="match-number">#{n}</span>\n'
                '<div class="match-details">\n'
                '<div class="match-name">{name}</div>\n'
                '<div class="match-finish">{finish}</div>\n'
                '<div class="match-meta">\n'
                '<span class="match-time">{time}</span>\n'
                '<span class="match-rating">{stars}</span>\n'
                '</div>\n</div>\n</div>'.format(
                    n=m['number'], name=m['name'], finish=m['finish'],
                    time=m['time'], stars=m['rating_stars']))

        # Event page body
        body = '{}\n<h1>{}</h1>\n<div class="event-header">\n<div class="event-meta">\n'.format(
            breadcrumb('Events', '/events/', title), title)
        body += '<strong>Date:</strong> {}<br>\n'.format(event_date)
        body += '<strong>Venue:</strong> {}<br>\n'.format(fm.get('venue', ''))
        body += '<strong>Location:</strong> {}\n'.format(fm.get('location', ''))
        body += '</div>\n{}\n</div>\n'.format(poster_html)
        body += '<h2>Matches</h2>\n'
        body += '\n'.join(match_cards)

        out_dir = output_dir / event_slug
        out_dir.mkdir(parents=True, exist_ok=True)
        (out_dir / "index.html").write_text(html_page(title, body), encoding='utf-8')

        all_events.append({
            'title': title, 'date': event_date,
            'venue': fm.get('venue', ''), 'slug': event_slug,
            'match_count': len(matches),
        })

    all_events.sort(key=lambda e: e['date'], reverse=True)
    # Write JSON data for index pages
    (DOCS / "events.json").write_text(json.dumps(all_events, indent=2, ensure_ascii=False), encoding='utf-8')
    return all_events


def process_wrestlers(events):
    wrestlers_dir = VAULT / "Wrestler"
    output_dir = DOCS / "wrestlers"
    output_dir.mkdir(parents=True, exist_ok=True)
    all_wrestlers = []

    for md_file in sorted(wrestlers_dir.glob("*.md")):
        text = md_file.read_text(encoding='utf-8')
        fm, body = parse_frontmatter(text)
        name = fm.get('title', md_file.stem)
        slug = name.strip().lower().replace(' ', '-')
        slug = re.sub(r'[^\w-]', '', slug)

        body = strip_dataview_blocks(body)
        body = convert_inline_dataview(body)
        body = convert_wikilinks(body)

        # Convert markdown body to HTML (basic conversion)
        html_body = markdown_to_html('{}\n{}'.format(breadcrumb('Wrestlers', '/wrestlers/', name), body))

        out_dir = output_dir / slug
        out_dir.mkdir(parents=True, exist_ok=True)
        (out_dir / "index.html").write_text(html_page(name, html_body), encoding='utf-8')
        all_wrestlers.append({'name': name, 'slug': slug})

    all_wrestlers.sort(key=lambda w: w['name'])
    (DOCS / "wrestlers.json").write_text(json.dumps(all_wrestlers, indent=2, ensure_ascii=False), encoding='utf-8')
    return all_wrestlers


def process_championships(events):
    champs_dir = VAULT / "Championships"
    output_dir = DOCS / "championships"
    output_dir.mkdir(parents=True, exist_ok=True)
    all_champs = []

    for md_file in sorted(champs_dir.glob("*.md")):
        text = md_file.read_text(encoding='utf-8')
        fm, body = parse_frontmatter(text)
        name = fm.get('title', md_file.stem)
        slug = name.strip().lower().replace(' ', '-')
        slug = re.sub(r'[^\w-]', '', slug)

        body = strip_dataview_blocks(body)
        body = convert_inline_dataview(body)
        body = convert_wikilinks(body)

        html_body = markdown_to_html('{}\n{}'.format(breadcrumb('Championships', '/championships/', name), body))

        out_dir = output_dir / slug
        out_dir.mkdir(parents=True, exist_ok=True)
        (out_dir / "index.html").write_text(html_page(name, html_body), encoding='utf-8')
        all_champs.append({'name': name, 'slug': slug})

    all_champs.sort(key=lambda c: c['name'])
    (DOCS / "championships.json").write_text(json.dumps(all_champs, indent=2, ensure_ascii=False), encoding='utf-8')
    return all_champs


def markdown_to_html(text):
    """Basic markdown -> HTML conversion (handles the common patterns used in PWA vault)."""
    lines = text.split('\n')
    out = []
    in_table = False
    in_list = False
    in_blockquote = False
    blockquote_lines = []

    for line in lines:
        # Blockquote
        if line.startswith('>') and not in_blockquote:
            if in_list:
                out.append('</ul>')
                in_list = False
            in_blockquote = True
            blockquote_lines = [line[1:].strip()]
            continue
        elif in_blockquote:
            if line.startswith('>'):
                blockquote_lines.append(line[1:].strip())
                continue
            else:
                out.append('<blockquote>')
                for bl in blockquote_lines:
                    out.append('  <p>{}</p>'.format(bl))
                out.append('</blockquote>')
                in_blockquote = False
                blockquote_lines = []

        # Headings
        if line.startswith('### '):
            if in_list:
                out.append('</ul>')
                in_list = False
            out.append('<h3>{}</h3>'.format(line[4:]))
        elif line.startswith('## '):
            if in_list:
                out.append('</ul>')
                in_list = False
            out.append('<h2>{}</h2>'.format(line[3:]))
        elif line.startswith('# '):
            if in_list:
                out.append('</ul>')
                in_list = False
            out.append('<h1>{}</h1>'.format(line[2:]))
        # Table
        elif line.startswith('|') and '|' in line[1:]:
            if in_list:
                out.append('</ul>')
                in_list = False
            cells = [c.strip() for c in line.split('|')[1:-1]]
            if not in_table:
                out.append('<table>')
                if all(c.startswith('-') for c in cells):
                    out.append('<thead><tr>{}</tr></thead>'.format(
                        ''.join('<th>{}</th>'.format(c) for c in cells)))
                else:
                    out.append('<tr>{}</tr>'.format(
                        ''.join('<td>{}</td>'.format(c) for c in cells)))
                in_table = True
            else:
                out.append('<tr>{}</tr>'.format(
                    ''.join('<td>{}</td>'.format(c) for c in cells)))
        elif in_table and not line.startswith('|'):
            out.append('</table>')
            in_table = False
            if line.strip():
                out.append('<p>{}</p>'.format(line))
        # List items
        elif line.startswith('- '):
            if not in_list:
                out.append('<ul>')
                in_list = True
            out.append('<li>{}</li>'.format(line[2:]))
        elif in_list and not line.startswith('- '):
            if line.strip():
                out.append('</ul>')
                in_list = False
                out.append('<p>{}</p>'.format(line))
            else:
                out.append('</ul>')
                in_list = False
        # Paragraphs
        elif line.strip():
            line = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', line)
            line = re.sub(r'\*(.+?)\*', r'<em>\1</em>', line)
            out.append('<p>{}</p>'.format(line))
        else:
            if in_list:
                out.append('</ul>')
                in_list = False

    if in_list:
        out.append('</ul>')
    if in_table:
        out.append('</table>')
    if in_blockquote:
        out.append('<blockquote>')
        for bl in blockquote_lines:
            out.append('  <p>{}</p>'.format(bl))
        out.append('</blockquote>')

    return '\n'.join(out)


def process_rankings():
    """Process PWI ranking and top/worst matches."""
    pwi_file = VAULT / "Statistiken" / "PWI Power Ranking.md"
    if pwi_file.exists():
        text = pwi_file.read_text(encoding='utf-8')
        fm, body = parse_frontmatter(text)

        singles_data = []
        in_table = False
        for line in body.split('\n'):
            line = line.strip()
            if line.startswith('| # | Wrestler'):
                in_table = True
                continue
            if in_table:
                if line.startswith('|') and '|' in line[1:]:
                    parts = [p.strip() for p in line.split('|') if p.strip()]
                    if len(parts) >= 8 and parts[0].replace(':', '').isdigit():
                        singles_data.append({
                            'rank': parts[0].replace(':', ''),
                            'name': convert_wikilinks(parts[1]),
                            'wins': parts[2], 'losses': parts[3],
                            'draws': parts[4], 'win_pct': parts[5],
                            'avg_stars': parts[6], 'points': parts[7],
                        })

        out_dir = DOCS / "rankings"
        out_dir.mkdir(parents=True, exist_ok=True)

        # Build PWI table HTML
        table_rows = []
        for r in singles_data:
            table_rows.append(
                '<tr><td class="pwi-rank">{rank}</td><td class="pwi-name">{name}</td>'
                '<td>{w}</td><td>{l}</td><td>{d}</td><td>{pct}</td>'
                '<td>{stars}</td><td>{pts}</td></tr>'.format(
                    rank=r['rank'], name=r['name'], w=r['wins'], l=r['losses'],
                    d=r['draws'], pct=r['win_pct'], stars=r['avg_stars'], pts=r['points']))

        body_html = markdown_to_html(body)
        pwi_body = '{}\n<div class="pwi-table">\n<table>\n<thead><tr>'.format(
            breadcrumb('Rankings', '/rankings/pwi-500/', 'PWI Power Ranking'))
        pwi_body += '<th>#</th><th>Wrestler</th><th>W</th><th>L</th><th>D</th><th>Pct</th><th>Stars</th><th>Pts</th>'
        pwi_body += '</tr></thead>\n<tbody>\n'
        pwi_body += '\n'.join(table_rows)
        pwi_body += '\n</tbody>\n</table>\n</div>\n'

        out_sub = out_dir / "pwi-500"
        out_sub.mkdir(parents=True, exist_ok=True)
        (out_sub / "index.html").write_text(html_page('PWI Power Ranking', pwi_body), encoding='utf-8')

    for name in ['Top 25 Matches', 'Worst 25 Matches']:
        src = VAULT / "Statistiken" / "{}.md".format(name)
        if not src.exists():
            continue
        text = src.read_text(encoding='utf-8')
        _, body = parse_frontmatter(text)
        body = strip_dataview_blocks(body)
        body = convert_inline_dataview(body)
        body = convert_wikilinks(body)

        slug = name.lower().replace(' ', '-')
        out_sub = DOCS / "rankings" / slug
        out_sub.mkdir(parents=True, exist_ok=True)

        html_body = markdown_to_html('{}\n{}'.format(
            breadcrumb('Rankings', '/rankings/', name), body))
        (out_sub / "index.html").write_text(html_page(name, html_body), encoding='utf-8')


def copy_images():
    poster_dir = VAULT / "z_Images" / "Poster"
    dest_dir = DOCS / "img" / "posters"
    dest_dir.mkdir(parents=True, exist_ok=True)
    for img in poster_dir.glob("*.png"):
        shutil.copy2(img, dest_dir / img.name)
    for img in (VAULT / "z_Images").glob("Banner_*.png"):
        shutil.copy2(img, DOCS / "img" / img.name)


def generate_homepage(events, wrestlers, champs):
    # Latest 10 events
    latest = sorted(events, key=lambda e: e['date'], reverse=True)[:10]
    event_lines = []
    for e in latest:
        event_lines.append(
            '<li><strong>{date}</strong> - <a href="{p}/events/{slug}/">{title}</a> - {venue} - {count} Matches</li>'.format(
                date=e['date'], p=PREFIX, slug=e['slug'], title=e['title'],
                venue=e['venue'], count=e['match_count']))

    body = """<h1>PWA - Pro Wrestling Action</h1>
<blockquote>
<p>Die parallele Wrestling-Welt. Von den Anfaengen im NAWA-Territorium (1980)<br>
ueber die Underground-Aera bis zur Renaissance 2015-2019.</p>
</blockquote>
<h2>Quick Stats</h2>
<table>
<thead><tr><th>Events</th><th>Wrestler</th><th>Championships</th></tr></thead>
<tbody><tr><td><strong>{ne}</strong></td><td><strong>{nw}</strong></td><td><strong>{nc}</strong></td></tr></tbody>
</table>
<h2>Latest Events</h2>
<ul>
{event_list}
</ul>
<h2>Navigation</h2>
<ul>
<li><a href="{p}/events/">All Events</a> — {ne} shows from 1982–2019</li>
<li><a href="{p}/wrestlers/">Wrestler Index</a> — {nw} superstars</li>
<li><a href="{p}/championships/">Championships</a> — Title histories</li>
<li><a href="{p}/rankings/pwi-500/">PWI Power Ranking</a> — Official rankings</li>
<li><a href="{p}/rankings/top-25-matches/">Top 25 Matches</a> — Best rated</li>
<li><a href="{p}/rankings/worst-25-matches/">Worst 25 Matches</a> — Lowest rated</li>
</ul>
<hr>
<p><small>PWA Static Site — Generated {gen}</small></p>""".format(
        ne=len(events), nw=len(wrestlers), nc=len(champs),
        event_list='\n'.join(event_lines), p=PREFIX,
        gen=datetime.now().strftime('%Y-%m-%d %H:%M'))

    (DOCS / "index.html").write_text(html_page('PWA - Pro Wrestling Action', body), encoding='utf-8')


def generate_index_pages(events, wrestlers, champs):
    """Generate list pages: /events/, /wrestlers/, /championships/"""

    # Events index
    body = breadcrumb('', None, 'Events')
    body += '<h1>All Events</h1>\n<div class="event-list">\n'
    for e in sorted(events, key=lambda x: x['date'], reverse=True):
        body += '<a href="{p}/events/{s}/" class="event-link"><span class="event-date">{d}</span><span class="event-title">{t}</span><span class="event-venue">{v}</span></a>\n'.format(
            p=PREFIX, s=e['slug'], d=e['date'], t=e['title'], v=e['venue'])
    body += '</div>\n'
    (DOCS / "events" / "index.html").write_text(html_page('All Events', body), encoding='utf-8')

    # Wrestlers index (grouped by first letter)
    body = breadcrumb('', None, 'Wrestlers')
    body += '<h1>Wrestler Index</h1>\n'
    groups = {}
    for w in sorted(wrestlers, key=lambda x: x['name']):
        letter = w['name'][0].upper()
        groups.setdefault(letter, []).append(w)
    for letter in sorted(groups.keys()):
        body += '<h2>{}</h2>\n<div class="wrestler-grid">\n'.format(letter)
        for w in groups[letter]:
            body += '<a href="{p}/wrestlers/{s}/" class="wrestler-card">{n}</a>\n'.format(
                p=PREFIX, s=w['slug'], n=w['name'])
        body += '</div>\n'
    (DOCS / "wrestlers" / "index.html").write_text(html_page('Wrestler Index', body), encoding='utf-8')

    # Championships index
    body = breadcrumb('', None, 'Championships')
    body += '<h1>Championships</h1>\n<div class="champ-grid">\n'
    for c in sorted(champs, key=lambda x: x['name']):
        body += '<a href="{p}/championships/{s}/" class="champ-card"><h2>{n}</h2></a>\n'.format(
            p=PREFIX, s=c['slug'], n=c['name'])
    body += '</div>\n'
    (DOCS / "championships" / "index.html").write_text(html_page('Championships', body), encoding='utf-8')


def main():
    print("=== PWA Data Pipeline ===")

    print("Copying images...")
    copy_images()
    print("  -> Done")

    print("Processing events...")
    events = process_events()
    print("  -> {} events".format(len(events)))

    print("Processing wrestlers...")
    wrestlers = process_wrestlers(events)
    print("  -> {} wrestlers".format(len(wrestlers)))

    print("Processing championships...")
    champs = process_championships(events)
    print("  -> {} championships".format(len(champs)))

    print("Processing rankings...")
    process_rankings()
    print("  -> Done")

    print("Generating homepage...")
    generate_homepage(events, wrestlers, champs)
    print("  -> Done")

    print("Generating index pages...")
    generate_index_pages(events, wrestlers, champs)
    print("  -> Done")

    print("\n=== Pipeline Complete ===")
    print("Events: {}".format(len(events)))
    print("Wrestlers: {}".format(len(wrestlers)))
    print("Championships: {}".format(len(champs)))


if __name__ == '__main__':
    main()
