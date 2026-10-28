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

# Exact source-audited exceptions only; never infer identities from filenames.
from urllib.parse import quote
SOURCE_REPAIRS = json.loads((REPO / 'content/source-repairs.json').read_text())

def sanitize_filename(name):
    for ch in ':*?"<>|\\/':
        name = name.replace(ch, '-')
    return name.strip()

def slugify(text):
    """Convert text to URL-safe slug: lowercase, spaces→hyphens, remove special chars."""
    text = text.strip().lower()
    text = text.replace(' ', '-')
    text = re.sub(r'[^\w-]', '', text)
    text = re.sub(r'-+', '-', text)
    return text.strip('-')

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

def resolve_image_path(z_path, prefix=PREFIX):
    """Convert /z_Images/X.png to /pwa-website/img/subdir/actual_filename.
    
    Searches z_Images/Wrestler, /Championships, /charts, /Poster, and z_Images/ root
    for a case-insensitive match. Falls back to simple path replacement."""
    audited_url = z_path.replace('/z_Images/', PREFIX + '/img/', 1)
    if audited_url in SOURCE_REPAIRS['media']:
        target = SOURCE_REPAIRS['media'][audited_url].removeprefix(PREFIX)
        return prefix + quote(target, safe='/')
    basename = Path(z_path).name
    
    search_dirs = [
        (VAULT / "z_Images" / "Wrestler", "wrestler"),
        (VAULT / "z_Images" / "Championships", "championships"),
        (VAULT / "z_Images" / "charts", "charts"),
        (VAULT / "z_Images" / "Poster", "posters"),
        (VAULT / "z_Images", ""),
    ]
    
    for src_dir, web_dir in search_dirs:
        if not src_dir.is_dir():
            continue
        for f in src_dir.glob("*"):
            if f.is_file() and f.name.lower() == basename.lower():
                path_part = f"{web_dir}/{f.name}" if web_dir else f.name
                return f'{prefix}/img/{path_part}'
    
    # Published media can outlive a moved/missing read-only vault source.
    for f in sorted((DOCS / 'img').rglob('*')):
        if f.is_file() and f.name.lower() == basename.lower():
            return '{}/{}'.format(prefix, f.relative_to(DOCS).as_posix())
    return z_path.replace('/z_Images/', f'{prefix}/img/')

def fix_image_srcs(html, prefix=PREFIX):
    """Rewrite all src=\"/z_Images/...\" attributes to proper /pwa-website/img/... paths."""
    def replace_src(m):
        z_path = m.group(1)
        return f'src="{resolve_image_path(z_path, prefix)}"'
    return re.sub(r'src="(/z_Images/[^"]+)"', replace_src, html)

def to_yaml(d):
    return yaml.dump(d, allow_unicode=True, default_flow_style=False, sort_keys=False)

# Shared HTML shell is maintained in presentation.py.

def repair_source_html(body, prefix=PREFIX):
    """Apply the exact audited URL exceptions only at the HTML boundary.

    Keep inner markup/entities verbatim (including wiki aliases). Inert spans
    retain text-node boundaries without inventing destinations. This also covers
    saved legacy HTML without mutating its protected source or JSON records.
    """
    from html import unescape
    text_only = {prefix + url.removeprefix(PREFIX)
                 for url in SOURCE_REPAIRS['text_only_links']}

    def anchor(match):
        href = re.search(r'\bhref\s*=\s*([\"\'])(.*?)\1', match['attrs'], re.I | re.S)
        if href and unescape(href[2]) in text_only:
            return '<span>' + match['label'] + '</span>'
        return match[0]

    body = re.sub(r'<a\b(?P<attrs>[^>]*)>(?P<label>.*?)</a\s*>',
                  anchor, body, flags=re.I | re.S)
    for old, target in SOURCE_REPAIRS['media'].items():
        old = prefix + old.removeprefix(PREFIX)
        target = prefix + quote(target.removeprefix(PREFIX), safe='/')
        body = body.replace('src="' + old + '"', 'src="' + target + '"')
    return body


def html_page(title, body, prefix=PREFIX):
    from presentation import page
    return page(title, repair_source_html(body, prefix), prefix)

def breadcrumb(parent_title, parent_url, current_title, prefix=PREFIX):
    if parent_url:
        return '<nav class="breadcrumb">\n  <a href="{p}/">Home</a> › <a href="{p}{url}">{pt}</a> › {ct}\n</nav>\n'.format(
            p=prefix, url=parent_url, pt=parent_title, ct=current_title)
    return '<nav class="breadcrumb">\n  <a href="{p}/">Home</a> › {ct}\n</nav>\n'.format(
        p=prefix, ct=current_title)


EVENT_SLUG_MAP = {}

def convert_wikilinks(text):
    # Handle image embeds first: ![[image.png]] or ![[image.png|width]]
    def embed_replacer(m):
        inner = m.group(1)
        if '|' in inner:
            target = inner.split('|', 1)[0].strip()
        else:
            target = inner.strip()
        # Resolve the image path
        img_path = resolve_image_path('/z_Images/{}'.format(target))
        return '<img src="{}" style="max-width:250px;border-radius:8px;" alt="donut chart">'.format(img_path)
    
    text = re.sub(r'!\[\[([^\]]+)\]\]', embed_replacer, text)
    
    # Then handle regular wikilinks [[...]]
    def replacer(m):
        inner = m.group(1)
        if '|' in inner:
            target, alias = inner.split('|', 1)
        else:
            target = alias = inner
        target = target.strip()
        alias = alias.strip()
        slug = slugify(target)
        if re.match(r'\d{4}-\d{2}-\d{2}', target):
            if target in EVENT_SLUG_MAP:
                href = '{}/events/{}/'.format(PREFIX, EVENT_SLUG_MAP[target])
            else:
                href = '{}/events/{}/'.format(PREFIX, slugify('{}'.format(target)))
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
        event_slug = slugify('{} - {}'.format(event_date, title))
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
        slug = slugify(name)

        body = strip_dataview_blocks(body)
        body = convert_inline_dataview(body)
        body = convert_wikilinks(body)

        # Convert markdown body to HTML (basic conversion)
        html_body = markdown_to_html('{}\n{}'.format(breadcrumb('Wrestlers', '/wrestlers/', name), body))
        html_body = fix_image_srcs(html_body)

        out_dir = output_dir / slug
        out_dir.mkdir(parents=True, exist_ok=True)
        (out_dir / "index.html").write_text(html_page(name, html_body), encoding='utf-8')
        all_wrestlers.append({'name': name, 'slug': slug})

    all_wrestlers.sort(key=lambda w: w['name'])
    (DOCS / "wrestlers.json").write_text(json.dumps(all_wrestlers, indent=2, ensure_ascii=False), encoding='utf-8')
    return all_wrestlers


def compute_championship_stats(history_lines_md, prefix=PREFIX):
    """Parse championship history table and compute summary statistics.
    Returns an HTML string with a stats summary box, or empty string if not enough data."""
    if not history_lines_md or len(history_lines_md) < 2:
        return ""
    
    reigns = []
    for line in history_lines_md:
        cells = [c.strip() for c in line.split('|')[1:-1]]
        if len(cells) < 5:
            continue
        champion = cells[0]
        won = cells[1]
        lost = cells[2]
        days_str = cells[3]
        defenses_str = cells[4]
        
        # Skip header/separator rows
        if champion in ('Champion', '---', '') or champion.startswith('-'):
            continue
        
        try:
            days = int(days_str)
        except ValueError:
            days = 0
        try:
            defenses = int(defenses_str)
        except ValueError:
            defenses = 0
        
        is_vacant = 'vacant' in champion.lower()
        is_current = lost.lower() == 'current'
        
        reigns.append({
            'champion': champion,
            'won': won,
            'lost': lost,
            'days': days,
            'defenses': defenses,
            'is_vacant': is_vacant,
            'is_current': is_current,
        })
    
    if not reigns:
        return ""
    
    # Compute stats
    non_vacant = [r for r in reigns if not r['is_vacant']]
    vacant = [r for r in reigns if r['is_vacant']]
    completed = [r for r in non_vacant if not r['is_current']]
    
    total_reigns = len(non_vacant)
    unique_champs = len(set(r['champion'] for r in non_vacant))
    vacant_count = len(vacant)
    
    first = non_vacant[-1] if non_vacant else None  # last in list = earliest chronologically
    
    completed_with_days = [r for r in completed if r['days'] > 0]
    avg_days = sum(r['days'] for r in completed_with_days) // len(completed_with_days) if completed_with_days else 0
    
    longest = max(non_vacant, key=lambda r: r['days']) if non_vacant else None
    shortest = min((r for r in completed if r['days'] > 0), key=lambda r: r['days'], default=None)
    
    most_reigns_data = {}
    for r in non_vacant:
        most_reigns_data[r['champion']] = most_reigns_data.get(r['champion'], 0) + 1
    most_reigns_champ = max(most_reigns_data, key=most_reigns_data.get) if most_reigns_data else None
    
    most_def = max(non_vacant, key=lambda r: r['defenses']) if non_vacant else None
    
    total_defenses = sum(r['defenses'] for r in non_vacant)
    total_title_matches = total_reigns + total_defenses  # each reign starts with a title match
    defense_rate = round(total_defenses / total_title_matches * 100) if total_title_matches > 0 else 0
    
    current_champ = reigns[0] if reigns and reigns[0]['is_current'] and not reigns[0]['is_vacant'] else None
    
    # Build HTML stats table
    def champ_link(name):
        if not name or 'vacant' in name.lower():
            return name or 'Vacant'
        # If already an HTML link (from wikilink conversion), use as-is
        if '<a href=' in name:
            return name
        slug = slugify(name)
        return '<a href="{}/wrestlers/{}/">{}</a>'.format(prefix, slug, name)
    
    rows = []
    rows.append('<tr><td><strong>Insgesamt Regentschaften</strong></td><td>{}</td></tr>'.format(total_reigns))
    rows.append('<tr><td><strong>Verschiedene Champions</strong></td><td>{}</td></tr>'.format(unique_champs))
    if vacant_count:
        rows.append('<tr><td><strong>Vakante Phasen</strong></td><td>{}</td></tr>'.format(vacant_count))
    if first:
        rows.append('<tr><td><strong>Erster Champion</strong></td><td>{} ({})</td></tr>'.format(champ_link(first['champion']), first['won']))
    rows.append('<tr><td><strong>⌀ Regentschaftsdauer</strong></td><td>{} Tage</td></tr>'.format(avg_days))
    if longest:
        rows.append('<tr><td><strong>Längste Regentschaft</strong></td><td>{} ({} Tage)</td></tr>'.format(champ_link(longest['champion']), longest['days']))
    if shortest:
        rows.append('<tr><td><strong>Kürzeste Regentschaft</strong></td><td>{} ({} Tage)</td></tr>'.format(champ_link(shortest['champion']), shortest['days']))
    if most_reigns_champ:
        rows.append('<tr><td><strong>Meiste Regentschaften</strong></td><td>{} ({}x)</td></tr>'.format(champ_link(most_reigns_champ), most_reigns_data[most_reigns_champ]))
    if most_def and most_def['defenses'] > 0:
        rows.append('<tr><td><strong>Meiste Verteidigungen</strong></td><td>{} ({})</td></tr>'.format(champ_link(most_def['champion']), most_def['defenses']))
    rows.append('<tr><td><strong>Titelmatches gesamt</strong></td><td>{}</td></tr>'.format(total_title_matches))
    rows.append('<tr><td><strong>Erfolgreiche Verteidigungen</strong></td><td>{} ({}%)</td></tr>'.format(total_defenses, defense_rate))
    if current_champ:
        rows.append('<tr><td><strong>Aktuelle Regentschaft</strong></td><td>{} — seit {} 🔥</td></tr>'.format(champ_link(current_champ['champion']), current_champ['won']))
    
    return '<h2>📊 Statistiken</h2>\n<table>\n<thead><tr><th>Kategorie</th><th>Wert</th></tr></thead>\n<tbody>\n{}\n</tbody>\n</table>\n'.format('\n'.join(rows))


def process_championships(events):
    champs_dir = VAULT / "Championships"
    output_dir = DOCS / "championships"
    output_dir.mkdir(parents=True, exist_ok=True)
    all_champs = []

    for md_file in sorted(champs_dir.glob("*.md")):
        text = md_file.read_text(encoding='utf-8')
        fm, body = parse_frontmatter(text)
        name = fm.get('title', md_file.stem)
        slug = slugify(name)

        body = strip_dataview_blocks(body)
        body = convert_inline_dataview(body)
        body = convert_wikilinks(body)

        # Parse history table for stats
        history_lines = []
        in_history = False
        for line in body.split('\n'):
            if line.strip().startswith('## History'):
                in_history = True
                continue
            if in_history:
                if line.strip().startswith('## '):
                    break
                if line.strip().startswith('|'):
                    history_lines.append(line.strip())

        # Compute and inject stats (after HTML conversion to avoid markdown mangling)
        stats_html = compute_championship_stats(history_lines)

        html_body = markdown_to_html('{}\n{}'.format(breadcrumb('Championships', '/championships/', name), body))
        html_body = fix_image_srcs(html_body)
        
        if stats_html:
            # Insert stats after <ul> that follows "Current Champion" block
            html_body = re.sub(
                r'(<p>Current Champion.*?</ul>\n)',
                r'\1\n' + stats_html + '\n',
                html_body, count=1
            )
            # Fallback: insert before <h2>History</h2>
            if stats_html not in html_body:
                html_body = re.sub(
                    r'(<h2>History</h2>)',
                    stats_html + '\n' + r'\1',
                    html_body, count=1
                )

        out_dir = output_dir / slug
        out_dir.mkdir(parents=True, exist_ok=True)
        (out_dir / "index.html").write_text(html_page(name, html_body), encoding='utf-8')
        all_champs.append({'name': name, 'slug': slug})

    all_champs.sort(key=lambda c: c['name'])
    (DOCS / "championships.json").write_text(json.dumps(all_champs, indent=2, ensure_ascii=False), encoding='utf-8')
    return all_champs


# The maintained parser preserves raw HTML blocks, and emits semantic data tables.
# It deliberately does not rewrite the actual archive values or wiki-link content.
def markdown_to_html(text):
    def inline(value):
        value = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', value)
        return re.sub(r'\*(.+?)\*', r'<em>\1</em>', value)

    lines = text.splitlines()
    result = []
    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        if not stripped:
            i += 1
            continue
        if stripped.startswith('|'):
            rows = []
            while i < len(lines) and lines[i].strip().startswith('|'):
                cells = [c.strip() for c in lines[i].strip().split('|')[1:-1]]
                rows.append(cells)
                i += 1
            if len(rows) > 1 and all(re.fullmatch(r':?-{3,}:?', c) for c in rows[1]):
                headers = rows.pop(0)
                rows.pop(0)
                result.append('<table><thead><tr>' + ''.join('<th scope="col">' + inline(c) + '</th>' for c in headers) + '</tr></thead><tbody>')
            else:
                result.append('<table><tbody>')
            for row in rows:
                result.append('<tr>' + ''.join('<td>' + inline(c) + '</td>' for c in row) + '</tr>')
            result.append('</tbody></table>')
            continue
        if stripped.startswith('- '):
            result.append('<ul>')
            while i < len(lines) and lines[i].strip().startswith('- '):
                result.append('<li>' + inline(lines[i].strip()[2:]) + '</li>')
                i += 1
            result.append('</ul>')
            continue
        if stripped.startswith('>'):
            result.append('<blockquote>')
            while i < len(lines) and lines[i].strip().startswith('>'):
                result.append('<p>' + inline(lines[i].strip()[1:].strip()) + '</p>')
                i += 1
            result.append('</blockquote>')
            continue
        heading = re.match(r'^(#{1,6}) (.*)$', stripped)
        if heading:
            level = len(heading.group(1))
            result.append('<h{0}>{1}</h{0}>'.format(level, inline(heading.group(2))))
        elif re.match(r'</?(?:div|nav|p|img|table|section|article|iframe|video|source|ul|li|hr)\b', stripped):
            result.append(line)
        else:
            result.append('<p>' + inline(line) + '</p>')
        i += 1
    return '\n'.join(result)


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
    """Copy ALL images from Obsidian PWA Vault to docs/img/."""
    z_images = VAULT / "z_Images"
    doc_img = DOCS / "img"
    doc_img.mkdir(parents=True, exist_ok=True)

    # Direct images in z_Images (banners, logos, maps, SVGs)
    for img in z_images.glob("*"):
        if img.is_file() and img.suffix.lower() in ('.png', '.jpg', '.jpeg', '.gif', '.svg', '.webp'):
            shutil.copy2(img, doc_img / img.name)

    # Subdirectories: posters, wrestler, championships, charts
    for sub in ['Poster', 'Wrestler', 'Championships', 'charts']:
        src_dir = z_images / sub
        if not src_dir.is_dir():
            continue
        dest_sub = sub.lower()
        if sub == 'Poster':
            dest_sub = 'posters'
        elif sub == 'Wrestler':
            dest_sub = 'wrestler'
        elif sub == 'Championships':
            dest_sub = 'championships'
        # charts stays as charts
        dest_dir = doc_img / dest_sub
        dest_dir.mkdir(parents=True, exist_ok=True)
        for img in src_dir.glob("*"):
            if img.is_file() and img.suffix.lower() in ('.png', '.jpg', '.jpeg', '.gif', '.svg', '.webp'):
                shutil.copy2(img, dest_dir / img.name)


def generate_homepage(events, wrestlers, champs):
    from magazine import homepage
    body = homepage(events, wrestlers, champs, DOCS, PREFIX)
    (DOCS / "index.html").write_text(html_page('PWA - Professional Wrestling Association', body), encoding='utf-8')


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


def preserve_published_archive(events, wrestlers):
    """Retain four already-public records absent from the current read-only vault.

    This explicit source snapshot prevents a redesign/rebuild from deleting canon.
    A restored vault source always takes precedence over its archival fallback.
    """
    groups = {'events': list(events), 'wrestlers': list(wrestlers)}
    for item in json.loads((REPO / 'content' / 'published-legacy.json').read_text(encoding='utf-8')):
        group = groups[item['kind']]
        record = item['record']
        if any(row['slug'] == record['slug'] for row in group):
            continue
        group.append(record)
        target = DOCS / item['kind'] / record['slug']
        target.mkdir(parents=True, exist_ok=True)
        title = record.get('title', record.get('name', 'PWA'))
        (target / 'index.html').write_text(html_page(title, item['body']), encoding='utf-8')
    groups['events'].sort(key=lambda row: row['date'], reverse=True)
    groups['wrestlers'].sort(key=lambda row: row['name'])
    for name, values in groups.items():
        (DOCS / (name + '.json')).write_text(json.dumps(values, indent=2, ensure_ascii=False), encoding='utf-8')
    return groups['events'], groups['wrestlers']


def main():
    print("=== PWA Data Pipeline ===")
    (DOCS / 'styles').mkdir(parents=True, exist_ok=True)
    shutil.copy2(REPO / 'assets' / 'styles' / 'main.css', DOCS / 'styles' / 'main.css')

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

    print("Preserving published archive records...")
    events, wrestlers = preserve_published_archive(events, wrestlers)

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
