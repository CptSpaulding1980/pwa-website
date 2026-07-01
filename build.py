#!/usr/bin/env python3
"""
PWA Data Pipeline: Obsidian vault -> Eleventy-ready content.
"""
import os, re, yaml, shutil, json
from pathlib import Path
from datetime import datetime

VAULT = Path("/Volumes/SSD_4TB/nextcloud/app/data/hendrik/files/Obsidian/PWA")
SITE = Path("/Users/homeserver/pwa-website/src")
DOCS = Path("/Users/homeserver/pwa-website/docs")

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

# Global lookup for event slug resolution
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
            # Look up the full slug from the event map
            if target in EVENT_SLUG_MAP:
                href = '/pwa-website/events/{}/'.format(EVENT_SLUG_MAP[target])
            else:
                href = '/pwa-website/events/{}/'.format(sanitize_filename(target))
        elif target in ['PWA World Heavyweight Championship', 'PWA International Championship',
                         'PWA Junior Heavyweight Championship', 'PWA World Tag Team Championship']:
            href = '/pwa-website/championships/{}/'.format(slug)
        else:
            href = '/pwa-website/wrestlers/{}/'.format(slug)
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
    if '\u00bd' in star_str:
        bonus = 0.5
    elif '\u00bc' in star_str:
        bonus = 0.25
    elif '\u00be' in star_str:
        bonus = 0.75
    return stars + bonus

def star_to_html(star_str):
    if not star_str:
        return ''
    return '<span class="stars">{}</span>'.format(star_str)

def to_yaml(d):
    return yaml.dump(d, allow_unicode=True, default_flow_style=False, sort_keys=False)

def process_events():
    events_dir = VAULT / "Events"
    output_dir = SITE / "events"
    output_dir.mkdir(parents=True, exist_ok=True)
    all_events = []

    for md_file in sorted(events_dir.glob("*.md")):
        text = md_file.read_text(encoding='utf-8')
        fm, body = parse_frontmatter(text)
        if not fm.get('title'):
            continue

        matches = fm.get('matches', [])
        event_slug = sanitize_filename('{} - {}'.format(fm.get('date', ''), fm.get('title', '')))
        # Register in global map for wikilink resolution
        EVENT_SLUG_MAP[str(fm.get('date', ''))] = event_slug

        eleventy_fm = {
            'layout': 'event.njk',
            'title': fm.get('title', ''),
            'date': str(fm.get('date', '')),
            'venue': fm.get('venue', ''),
            'location': fm.get('location', ''),
            'promotion': fm.get('promotion', 'PWA'),
            'permalink': '/events/{}/'.format(event_slug),
            'tags': ['events'],
        }

        processed_matches = []
        for i, m in enumerate(matches):
            name = m.get('name', '')
            finish = m.get('finish', '')
            rating_str = m.get('rating', '')
            rating_num = star_to_numeric(rating_str)
            time_match = re.search(r'(\d+)\s*Min\s*(\d+)\s*Sec', finish)
            match_time = '{}:{:02d}'.format(int(time_match.group(1)), int(time_match.group(2))) if time_match else ''

            processed_matches.append({
                'number': i + 1,
                'name': convert_wikilinks(name),
                'finish': convert_wikilinks(finish),
                'rating_stars': star_to_html(rating_str),
                'rating_num': rating_num,
                'time': match_time,
            })

        # Poster
        poster_html = ''
        event_date = str(fm.get('date', ''))
        poster_files = list((VAULT / "z_Images" / "Poster").glob("{}*".format(event_date)))
        if poster_files:
            dest_dir = DOCS / "img" / "posters"
            dest_dir.mkdir(parents=True, exist_ok=True)
            shutil.copy2(poster_files[0], dest_dir / poster_files[0].name)
            poster_html = '<img src="/pwa-website/img/posters/{}" class="event-poster" alt="Poster">'.format(poster_files[0].name)

        # Build content
        lines = [
            '---',
            to_yaml(eleventy_fm).strip(),
            'matches_json: {}'.format(json.dumps(processed_matches, ensure_ascii=False)),
            '---',
            '',
            '# {}'.format(fm.get('title', '')),
            '',
            '<div class="event-header">',
            '<div class="event-meta">',
            '**Date:** {}<br>'.format(fm.get('date', '')),
            '**Venue:** {}<br>'.format(fm.get('venue', '')),
            '**Location:** {}'.format(fm.get('location', '')),
            '</div>',
            poster_html,
            '</div>',
            '',
            '## Matches',
            '',
            '{% for match in matches_json %}',
            '<div class="match-card">',
            '<span class="match-number">#{{ match.number }}</span>',
            '<div class="match-details">',
            '<div class="match-name">{{ match.name | safe }}</div>',
            '<div class="match-finish">{{ match.finish | safe }}</div>',
            '<div class="match-meta">',
            '<span class="match-time">{{ match.time }}</span>',
            '<span class="match-rating">{{ match.rating_stars | safe }}</span>',
            '</div>',
            '</div>',
            '</div>',
            '{% endfor %}',
        ]

        out_file = output_dir / md_file.name
        out_file.write_text('\n'.join(lines), encoding='utf-8')

        all_events.append({
            'title': fm.get('title', ''),
            'date': str(fm.get('date', '')),
            'venue': fm.get('venue', ''),
            'slug': event_slug,
            'match_count': len(matches),
        })

    all_events.sort(key=lambda e: e['date'], reverse=True)
    (SITE / "_data" / "events.json").write_text(
        json.dumps(all_events, indent=2, ensure_ascii=False), encoding='utf-8')
    return all_events

def process_wrestlers():
    wrestlers_dir = VAULT / "Wrestler"
    output_dir = SITE / "wrestlers"
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

        eleventy_fm = {
            'layout': 'wrestler.njk',
            'title': name,
            'permalink': '/wrestlers/{}/'.format(slug),
            'tags': ['wrestlers'],
        }

        content = '---\n{}\n---\n{}'.format(to_yaml(eleventy_fm).strip(), body)
        out_file = output_dir / sanitize_filename('{}.md'.format(name))
        out_file.write_text(content, encoding='utf-8')
        all_wrestlers.append({'name': name, 'slug': slug})

    all_wrestlers.sort(key=lambda w: w['name'])
    (SITE / "_data" / "wrestlers.json").write_text(
        json.dumps(all_wrestlers, indent=2, ensure_ascii=False), encoding='utf-8')
    return all_wrestlers

def process_championships():
    champs_dir = VAULT / "Championships"
    output_dir = SITE / "championships"
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

        eleventy_fm = {
            'layout': 'championship.njk',
            'title': name,
            'permalink': '/championships/{}/'.format(slug),
            'tags': ['championships'],
        }

        content = '---\n{}\n---\n{}'.format(to_yaml(eleventy_fm).strip(), body)
        out_file = output_dir / sanitize_filename('{}.md'.format(name))
        out_file.write_text(content, encoding='utf-8')
        all_champs.append({'name': name, 'slug': slug})

    all_champs.sort(key=lambda c: c['name'])
    (SITE / "_data" / "championships.json").write_text(
        json.dumps(all_champs, indent=2, ensure_ascii=False), encoding='utf-8')
    return all_champs

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
                elif in_table and not line.startswith('|'):
                    break

        (SITE / "_data" / "pwi_ranking.json").write_text(
            json.dumps(singles_data, indent=2, ensure_ascii=False), encoding='utf-8')

        body = strip_dataview_blocks(body)
        body = convert_inline_dataview(body)
        body = convert_wikilinks(body)

        out_dir = SITE / "rankings"
        out_dir.mkdir(parents=True, exist_ok=True)

        content = '---\n{}\n---\n{}'.format(
            to_yaml({'layout': 'ranking.njk', 'title': 'PWI Power Ranking',
                     'permalink': '/rankings/pwi-500/', 'tags': ['rankings']}).strip(),
            body)
        (out_dir / "pwi-power-ranking.md").write_text(content, encoding='utf-8')

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
        out_dir = SITE / "rankings"
        out_dir.mkdir(parents=True, exist_ok=True)

        content = '---\n{}\n---\n{}'.format(
            to_yaml({'layout': 'ranking.njk', 'title': name,
                     'permalink': '/rankings/{}/'.format(slug), 'tags': ['rankings']}).strip(),
            body)
        (out_dir / sanitize_filename('{}.md'.format(name))).write_text(content, encoding='utf-8')

def copy_images():
    poster_dir = VAULT / "z_Images" / "Poster"
    dest_dir = DOCS / "img" / "posters"
    dest_dir.mkdir(parents=True, exist_ok=True)
    for img in poster_dir.glob("*.png"):
        shutil.copy2(img, dest_dir / img.name)
    for img in (VAULT / "z_Images").glob("Banner_*.png"):
        shutil.copy2(img, DOCS / "img" / img.name)

def generate_homepage(events, wrestlers, champs):
    latest = sorted(events, key=lambda e: e['date'], reverse=True)[:10]
    event_links = []
    for e in latest:
        event_links.append('- **{}** - [{}](/pwa-website/events/{}/) - {} - {} Matches'.format(
            e['date'], e['title'], e['slug'], e['venue'], e['match_count']))

    fm = to_yaml({
        'layout': 'home.njk',
        'title': 'PWA - Pro Wrestling Action',
        'permalink': '/',
        'tags': ['home'],
    }).strip()

    body = """# PWA - Pro Wrestling Action

> Die parallele Wrestling-Welt. Von den Anfaengen im NAWA-Territorium (1980)
> ueber die Underground-Aera bis zur Renaissance 2015-2019.

## Quick Stats

| Events | Wrestler | Championships |
|---|---|---|
| **{}** | **{}** | **{}** |

## Latest Events

{}

## Navigation

- [All Events](/pwa-website/events/) - {} shows from 1982-2019
- [Wrestler Index](/pwa-website/wrestlers/) - {} superstars
- [Championships](/pwa-website/championships/) - Title histories
- [PWI Power Ranking](/pwa-website/rankings/pwi-500/) - Official rankings
- [Top 25 Matches](/pwa-website/rankings/top-25-matches/) - Best rated
- [Worst 25 Matches](/pwa-website/rankings/worst-25-matches/) - Lowest rated

---
*PWA Static Site - Generated {}*""".format(
        len(events), len(wrestlers), len(champs),
        '\n'.join(event_links),
        len(events), len(wrestlers),
        datetime.now().strftime('%Y-%m-%d %H:%M')
    )

    content = '---\n{}\n---\n{}'.format(fm, body)
    (SITE / "index.md").write_text(content, encoding='utf-8')


def main():
    print("=== PWA Data Pipeline ===")
    print("Processing events...")
    events = process_events()
    print("  -> {} events".format(len(events)))

    print("Processing wrestlers...")
    wrestlers = process_wrestlers()
    print("  -> {} wrestlers".format(len(wrestlers)))

    print("Processing championships...")
    champs = process_championships()
    print("  -> {} championships".format(len(champs)))

    print("Processing rankings...")
    process_rankings()
    print("  -> Done")

    print("Copying images...")
    copy_images()
    print("  -> Done")

    print("Generating homepage...")
    generate_homepage(events, wrestlers, champs)
    print("  -> Done")

    print("\n=== Pipeline Complete ===")
    print("Events: {}".format(len(events)))
    print("Wrestlers: {}".format(len(wrestlers)))
    print("Championships: {}".format(len(champs)))

if __name__ == '__main__':
    main()
