"""One canonical, auditable dataset for all four PWA match rankings."""
import re


def parse_duration(raw):
    value = str(raw or '').strip()
    if not value:
        return None, 'missing'
    if value.casefold() in {'—', '-', '–', '?', 'n/a', 'unknown', 'tbd'}:
        return None, 'placeholder'
    words = re.fullmatch(r'(\d+)\s*Min\s*(\d+)\s*Sec', value, re.I)
    parts = [int(x) for x in value.split(':')] if re.fullmatch(r'\d+:\d{2}(?::\d{2})?', value) else None
    if words:
        parts = [int(words[1]), int(words[2])]
    if parts is None or parts[-1] >= 60 or (len(parts) == 3 and parts[1] >= 60):
        return None, 'invalid'
    seconds = parts[0] * 60 + parts[1] if len(parts) == 2 else parts[0] * 3600 + parts[1] * 60 + parts[2]
    return (seconds, 'valid') if seconds > 0 else (None, 'zero')


def event_rows(body):
    """Parse the six-column event table, including multiline finish cells.

    Protect wiki aliases before splitting; reject malformed rows rather than
    shifting a duration or star column into the numeric rating column.
    """
    section = re.search(r'^## Matches\s*\n(.*?)(?=^## |\Z)', body, re.M | re.S)
    if not section:
        return []
    chunks = re.split(r'(?m)(?=^\|\s*\d+\s*\|)', section[1])[1:]
    result = []
    for chunk in chunks:
        # Ignore prose/footnotes after the last table row.
        chunk = re.split(r'\n\s*\n', chunk, maxsplit=1)[0].strip()
        protected = re.sub(r'\[\[.*?\]\]', lambda m: m[0].replace('\\|', '|').replace('|', '\x01'), chunk)
        cells = [c.strip().replace('\x01', '|') for c in protected.strip('|').split('|')]
        if len(cells) != 6:
            raise ValueError('Malformed event match row: ' + chunk)
        number, name, finish, raw_time, raw_rating, stars = cells
        rating = float(raw_rating) if re.fullmatch(r'\d+(?:\.\d+)?', raw_rating) else None
        if rating is None and raw_rating not in {'', '-', '—', 'N/A', '?'}:
            raise ValueError('Unrecognized numeric rating: ' + raw_rating)
        seconds, status = parse_duration(raw_time)
        result.append(dict(number=int(number), name=name, finish=finish, rating=rating,
                           stars=stars, raw_time=raw_time, seconds=seconds, duration_status=status))
    return result


def analyze(rows, events):
    from collections import Counter
    from statistics import mean, median
    unique = {}
    duplicates = 0
    for row in rows:
        key = (row['event'], row['number'])
        if key in unique:
            if unique[key] != row:
                raise ValueError('Conflicting canonical match identity: ' + str(key))
            duplicates += 1
        unique[key] = row
    records = sorted(unique.values(), key=lambda r: (r['date'], r['event'], r['number']))
    matches = [r for r in records if r.get('kind', 'match') == 'match']
    ratings = [r['rating'] for r in matches if r['rating'] is not None]
    times = [r['seconds'] for r in matches if r['seconds'] is not None]
    summary = dict(events=len(set(events)), records=len(records), matches=len(matches),
                   segments=len(records)-len(matches), rated=len(ratings), timed=len(times),
                   rating_mean=mean(ratings) if ratings else None,
                   rating_median=median(ratings) if ratings else None,
                   duration_mean=mean(times) if times else None,
                   duration_median=median(times) if times else None,
                   duration_status=dict(Counter(r['duration_status'] for r in matches)),
                   duplicates_removed=duplicates,
                   first_date=min((r['date'] for r in records), default=None),
                   last_date=max((r['date'] for r in records), default=None))
    rankings = {}
    for kind, field, direction in [('top', 'rating', -1), ('worst', 'rating', 1),
                                  ('longest', 'seconds', -1), ('shortest', 'seconds', 1)]:
        rankings[kind] = sorted((r for r in matches if r[field] is not None),
                                key=lambda r: (direction * r[field], r['date'], r['event'], r['number']))[:25]
    return dict(summary=summary, records=records, rankings=rankings)


def collect(vault, legacy_path):
    """Tables are the numeric source of truth; never reverse-map stars to ratings.

    Canonical identity is the existing event URL slug plus its source match
    number. Legacy published-only cards participate in the same population;
    missing numeric values remain missing, not extrapolated from partial Top25.
    """
    import json
    from bs4 import BeautifulSoup
    from build import parse_frontmatter, slugify
    rows, events = [], set()
    for path in sorted((vault / 'Events').glob('*.md')):
        fm, body = parse_frontmatter(path.read_text(encoding='utf-8'))
        if not fm.get('title'):
            continue
        date, title = str(fm.get('date', '')), fm['title']
        slug = slugify(date + ' - ' + title)
        extracted = event_rows(body)
        if [r['number'] for r in extracted] != list(range(1, len(fm.get('matches', [])) + 1)):
            raise ValueError('Match table/frontmatter scope mismatch: ' + path.name)
        events.add(slug)
        for row in extracted:
            rows.append(dict(row, event=slug, date=date, title=title,
                             source='Events/' + path.name, name_format='wiki'))
    for item in json.loads(legacy_path.read_text(encoding='utf-8')):
        if item['kind'] != 'events' or item['record']['slug'] in events:
            continue
        event = item['record']
        events.add(event['slug'])
        cards = BeautifulSoup(item['body'], 'html.parser').select('.match-card')
        if len(cards) != event['match_count']:
            raise ValueError('Legacy match count mismatch: ' + event['slug'])
        for card in cards:
            raw_time = card.select_one('.match-time').get_text(strip=True)
            seconds, status = parse_duration(raw_time)
            rows.append(dict(event=event['slug'], number=int(card.select_one('.match-number').text.lstrip('#')),
                             name=card.select_one('.match-name').decode_contents(), name_format='html',
                             finish=card.select_one('.match-finish').get_text(' ', strip=True),
                             date=event['date'], title=event['title'], rating=None,
                             stars=card.select_one('.match-rating').get_text(strip=True),
                             raw_time=raw_time, seconds=seconds, duration_status=status,
                             source='content/published-legacy.json'))
    # Independently inspected duplicate: identical card/finishes/times/stars, but
    # the unprefixed copy stores star-scale decimals in the points column.
    # Preserve BOTH published pages; select only the points-scale PWA event here.
    aliases = {'2019-09-24-tuesday-night-action-294-the-ox-celebration':
               '2019-09-24-pwa-tuesday-night-action-294-the-ox-celebration'}
    discarded = []
    for alias, canonical in aliases.items():
        copies = [r for r in rows if r['event'] == alias]
        originals = [r for r in rows if r['event'] == canonical]
        if copies:
            signature = lambda rs: [(r['number'],r['name'],r['finish'],r['raw_time'],r['stars']) for r in rs]
            if signature(copies) != signature(originals):
                raise ValueError('Audited event alias no longer matches canonical event: ' + alias)
            discarded.extend(copies)
            rows = [r for r in rows if r['event'] != alias]
            events.remove(alias)
    for row in rows:
        row['kind'] = 'segment' if row['name'].startswith('Interview Segment /w ') else 'match'
    result = analyze(rows, events)
    result['summary']['event_urls'] = len(events) + len({r['event'] for r in discarded})
    result['summary']['duplicates_removed'] += len(discarded)
    result['excluded_alias_records'] = discarded
    result['event_aliases'] = aliases
    return result


ROUTES = {'top': ('Top Matches', 'top-25-matches'),
          'worst': ('Worst Matches', 'worst-25-matches'),
          'longest': ('Longest Matches', 'longest-25-matches'),
          'shortest': ('Shortest Matches', 'shortest-25-matches')}


def format_duration(seconds):
    if seconds is None:
        return '—'
    seconds = int(seconds + 0.5)  # Display means to nearest second; JSON retains exact values.
    minutes, sec = divmod(seconds, 60)
    return f'{minutes // 60}:{minutes % 60:02d}:{sec:02d}' if minutes >= 60 else f'{minutes}:{sec:02d}'


def render(data, kind, prefix):
    from html import escape
    from urllib.parse import unquote, urlsplit
    from bs4 import BeautifulSoup
    from build import DOCS, convert_wikilinks, repair_source_html
    s = data['summary']
    label = ROUTES[kind][0]
    def de(value):
        return f'{value:.2f}'.replace('.', ',') if value is not None else '—'
    def date(value):
        from datetime import date as date_type
        return date_type.fromisoformat(value).strftime('%d.%m.%y') if value else '—'
    tabs = ''.join(f'<a href="{prefix}/rankings/{route}/"' + (' aria-current="page"' if key == kind else '') + f'>{title}</a>'
                   for key, (title, route) in ROUTES.items())
    cards = [(s['matches'], 'Erfasste Matches', f"{s['events']} Events · {s['segments']} Segmente separat"),
             (s['rated'], 'Numerisch bewertet', f"{s['matches'] - s['rated']} ohne numerisches Rating"),
             (s['timed'], 'Zeitlich auswertbar', f"{s['matches'] - s['timed']} Dauern ausgeschlossen"),
             (de(s['rating_mean']), 'Ø Rating', f"Median {de(s['rating_median'])} · n = {s['rated']}"),
             (format_duration(s['duration_mean']), 'Ø Matchdauer', f"Median {format_duration(s['duration_median'])} · n = {s['timed']}")]
    panels = ''.join(f'<div class="statistics-card"><dt>{escape(str(title))}</dt><dd>{escape(str(value))}</dd><span>{escape(detail)}</span></div>'
                     for value, title, detail in cards)
    breadcrumb = f'<nav class="breadcrumb" aria-label="Brotkrümelnavigation"><a href="{prefix}/">Home</a> › '
    breadcrumb += 'Statistiken' if kind == 'top' else f'<a href="{prefix}/rankings/top-25-matches/">Statistiken</a> › {label}'
    body = breadcrumb + '</nav><div class="statistics-hub"><span class="eyebrow">PWA Archiv · Zahlen &amp; Ranglisten</span><h1>Statistiken</h1>'
    body += f'<p class="statistics-intro">Das veröffentlichte Archiv vom {date(s["first_date"])} bis {date(s["last_date"])}. Archivzeitraum, kein heutiges Kalenderdatum.</p>'
    body += '<dl class="statistics-grid">' + panels + '</dl>'
    body += '<nav class="statistics-nav" aria-label="Match-Ranglisten">' + tabs + '</nav>'
    body += f'<section aria-labelledby="ranking-heading"><h2 id="ranking-heading">{label}</h2>'
    criterion = {'top':'Numerisches Quellrating, absteigend', 'worst':'Numerisches Quellrating, aufsteigend',
                 'longest':'Gültige positive Gesamtdauer, absteigend', 'shortest':'Gültige positive Gesamtdauer, aufsteigend'}[kind]
    body += f'<p class="statistics-method">{len(data["rankings"][kind])} Einträge · {criterion}. Gleichstand: Datum aufsteigend, Event-URL, Matchnummer.</p>'
    body += f'<table class="statistics-table"><caption>{label} · Top 25 des auswertbaren Archivbestands</caption><thead><tr>'
    body += ''.join('<th scope="col">' + h + '</th>' for h in ['Rang','Datum','Show','Match','Rating','Sterne','Dauer']) + '</tr></thead><tbody>'
    for index, row in enumerate(data['rankings'][kind], 1):
        name = convert_wikilinks(row['name']) if row['name_format'] == 'wiki' else row['name']
        name = repair_source_html(name, prefix)
        # Source match-type aliases have no published profile: retain exact labels,
        # never invent wrestler destinations. Existing working links stay intact.
        fragment = BeautifulSoup(name, 'html.parser')
        for anchor in fragment.select('a[href]'):
            route = unquote(urlsplit(anchor['href']).path)
            if route.startswith(prefix + '/'):
                target = DOCS / route.removeprefix(prefix + '/')
                if not target.is_file() and not (target / 'index.html').is_file():
                    anchor.unwrap()
        name = str(fragment)
        rating = f'{row["rating"]:g}' if row['rating'] is not None else '—'
        event_url = f'{prefix}/events/{row["event"]}/'
        body += f'<tr data-event="{escape(row["event"])}" data-match="{row["number"]}"><td>{index}</td><td><time datetime="{row["date"]}">{date(row["date"])}</time></td>'
        body += f'<td><a href="{event_url}">{escape(row["title"])}</a></td><td><span class="statistics-match-number">#{row["number"]}</span> {name}</td>'
        body += f'<td>{rating}</td><td><span class="stars">{escape(row["stars"])}</span></td><td>{format_duration(row["seconds"])}</td></tr>'
    body += '</tbody></table></section>'
    statuses = s['duration_status']
    excluded = ', '.join(f'{statuses.get(key,0)} {text}' for key,text in [('missing','fehlend'),('placeholder','Platzhalter'),('zero','Nullzeit (0:00)'),('invalid','ungültig')])
    body += '<details class="statistics-definitions"><summary>Datenbasis &amp; Berechnung</summary>'
    body += f'<p>Ein gemeinsamer Bestand: {s["matches"]} Matches und {s["segments"]} ausdrücklich als „Interview Segment /w“ benannte Segmente ({s["records"]} Datensätze). Segmente bleiben in allen vier Ranglisten und Match-Mittelwerten ausgeschlossen. {s["events"]} kanonische Events aus {s["event_urls"]} veröffentlichten Event-URLs. Identität: kanonische Event-URL + Matchnummer; keine Doppelzählung aus Top-/Worst-Snapshots.</p>'
    body += f'<p>Geprüfte Dublette: „Tuesday Night Action 294 – The Ox Celebration“ vom 24.09.19 ist zusätzlich ohne PWA-Präfix veröffentlicht. Die identischen {s["duplicates_removed"]} Matchkopien zählen nur beim PWA-Event mit Quellpunkten 81/83/79; die Aliaswerte 3,75/3,75/3,50 sind eine andere Skala, keine schlechten Punkteratings. Beide historischen Event-URLs bleiben unverändert erreichbar.</p>'
    body += '<p>Quelle: vollständige Matchtabellen der Event-Notizen plus veröffentlichte Legacy-Eventkarten. Ratings sind die numerischen Quellpunkte (auch über 100), nicht aus Sternen zurückgerechnet. Sterne bleiben eine separate Quellangabe. Die alten Top-/Worst-25-Notizen sind Teilansichten, keine Gesamtbasis.</p>'
    body += f'<p>Bewertungskennzahlen nutzen nur die {s["rated"]} numerisch bewerteten Einträge; {s["matches"]-s["rated"]} Legacy-Einträge ohne numerisches Rating bleiben ausgeschlossen. Ø = Summe / Anzahl; Median = mittlerer Wert (bei gerader Anzahl Mittel der zwei mittleren Werte).</p>'
    body += f'<p>Dauerkennzahlen und Zeitranglisten nutzen nur {s["timed"]} gültige positive Quelldauern. Ausgeschlossen: {excluded}. Ungültiges Beispiel: 108:108 (Sekunden ≥ 60); keine Korrektur aus einer widersprüchlichen Finish-Angabe. Fehlende Dauern werden nicht aus einzelnen Falls/Eliminierungen geschätzt.</p>'
    body += '<p>Zeitformate: M:SS (auch über 59 Minuten), H:MM:SS oder explizit „Min / Sec“; Sekunden und Stunden-Minuten jeweils 0–59. Anzeige ab einer Stunde als H:MM:SS; Mittelwerte auf die nächste Sekunde gerundet. Keine Hochrechnung auf nicht veröffentlichte Events.</p>'
    body += f'<p><a href="{prefix}/statistics.json">Vollständiger Statistikdatensatz (JSON)</a> · Quellen, Rohzeiten, Ausschlussgründe und ungerundete Kennzahlen.</p></details></div>'
    return body


