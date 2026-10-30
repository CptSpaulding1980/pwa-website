"""Approved source-side scoped release while upstream historical repair is open.

The last verified publication is an immutable archival source. Only the exact
independently verified Landfall note is added; no regenerated profiles, PWI,
championship history, old events or charts are implicitly trusted. Normal builds
remain deterministic despite unrelated changes in the live Obsidian vault.
"""
import copy
import hashlib
import json
from pathlib import Path
from html import escape

ROOT = Path(__file__).resolve().parent
NOTE = '2019-10-08 - PWA Tuesday Night Action 296 - Landfall.md'
NOTE_SHA = 'a58f5ae6089d3ce9731a87c7f13532a8328998e283cd9b0d483921b72aaaf4ed'
SNAPSHOT_SHA = '42eadf4da16210e55b277ae87a7ae4dd731106e76b6251fb2db8e0792a7d75d0'
SLUG = '2019-10-08-pwa-tuesday-night-action-296-landfall'

def snapshot():
    raw = (ROOT/'content/published-tna295.json').read_bytes()
    if hashlib.sha256(raw).hexdigest() != SNAPSHOT_SHA:
        raise ValueError('Published historical source snapshot changed')
    return json.loads(raw)

def validated_note():
    import build
    text = (build.VAULT/'Events'/NOTE).read_text(encoding='utf-8')
    if hashlib.sha256(text.encode()).hexdigest() != NOTE_SHA:
        raise ValueError('Landfall source changed; a fresh source audit is required')
    return text

def landfall():
    from build import parse_frontmatter
    from match_statistics import event_rows
    fm, body = parse_frontmatter(validated_note())
    rows = event_rows(body)
    if [(r['rating'],r['seconds']) for r in rows] != [(78,1200),(81,829),(83,1220)]:
        raise ValueError('Landfall differs from audited full-card evidence')
    return fm, [dict(r, event=SLUG, date='2019-10-08', title=fm['title'],
                     source='Events/'+NOTE, name_format='wiki', kind='match') for r in rows]

def statistics():
    from match_statistics import analyze
    before = snapshot()['statistics']
    _, new_rows = landfall()
    events = {r['event'] for r in before['records']} | {SLUG}
    # Include published empty events too, not only events represented by matches.
    events |= {r['slug'] for r in snapshot()['data']['events.json']}
    events -= set(before['event_aliases'])
    result = analyze(copy.deepcopy(before['records']) + new_rows, events)
    result['event_aliases'] = before['event_aliases']
    result['excluded_alias_records'] = before['excluded_alias_records']
    result['summary']['duplicates_removed'] = before['summary']['duplicates_removed']
    result['summary']['event_urls'] = before['summary']['event_urls'] + 1
    return result

def event_source():
    import build
    fm, rows = landfall()
    body = build.breadcrumb('Events','/events/',fm['title'])
    body += '<h1>'+escape(fm['title'])+'</h1><div class="event-header"><div class="event-meta">'
    for label, value in [('Date','2019-10-08'),('Venue',fm['venue']),('Location',fm['location'])]:
        body += '<strong>'+label+':</strong> '+escape(value)+'<br>\n'
    body += '</div></div><h2>Matches</h2>\n'
    for row in rows:
        # Stipulation is a label, not an invented wrestler destination.
        name = row['name'].replace('[[Falls Count Anywhere]]','Falls Count Anywhere')
        body += ('<div class="match-card"><span class="match-number">#{number}</span>'
                 '<div class="match-details"><div class="match-name">{name}</div>'
                 '<div class="match-finish">{finish}</div><div class="match-meta">'
                 '<span class="match-time">{time}</span> '
                 '<span class="match-points">Rating: {rating:g}</span> '
                 '<span class="match-rating">{stars}</span></div></div></div>\n').format(
                     number=row['number'], name=build.convert_wikilinks(name),
                     finish=escape(row['finish']), time=row['raw_time'],
                     rating=row['rating'], stars=escape(row['stars']))
    record = dict(title=fm['title'], date='2019-10-08', venue=fm['venue'], slug=SLUG, match_count=3)
    return record, build.html_page(fm['title'],body)

def render(root):
    """Render exclusively from protected archival and audited incremental sources."""
    import build
    from match_statistics import render as render_statistics, ROUTES
    frozen = snapshot()
    for route, text in frozen['pages'].items():
        target = root/route
        target.parent.mkdir(parents=True,exist_ok=True)
        target.write_text(text,encoding='utf-8')
    record, html = event_source()
    target = root/'events'/SLUG/'index.html'
    target.parent.mkdir(parents=True,exist_ok=True)
    target.write_text(html,encoding='utf-8')
    data = copy.deepcopy(frozen['data'])
    data['events.json'].append(record)
    data['events.json'].sort(key=lambda r:r['date'],reverse=True)
    for name, values in data.items():
        (root/name).write_text(json.dumps(values,indent=2,ensure_ascii=False),encoding='utf-8')
    stats = statistics()
    (root/'statistics.json').write_text(json.dumps(stats,ensure_ascii=False,indent=2),encoding='utf-8')
    for kind, (_, slug) in ROUTES.items():
        path = root/'rankings'/slug/'index.html'
        path.parent.mkdir(parents=True,exist_ok=True)
        path.write_text(build.html_page('Statistiken',render_statistics(stats,kind,build.PREFIX)),encoding='utf-8')
    build.generate_index_pages(data['events.json'],data['wrestlers.json'],data['championships.json'])
    build.generate_homepage(data['events.json'],data['wrestlers.json'],data['championships.json'])
    return data

def build_release():
    import build
    import shutil
    frozen = snapshot()
    # Never overwrite published-only media with unreviewed regenerated charts.
    for route, digest in frozen['assets'].items():
        target = build.DOCS/route
        if not target.is_file() or hashlib.sha256(target.read_bytes()).hexdigest() != digest:
            raise ValueError('Protected published asset differs: '+route)
    # Refuse residual unvalidated URLs instead of hiding them in an unused folder.
    approved = set(frozen['pages']) | {'events/'+SLUG+'/index.html'}
    extra = {p.relative_to(build.DOCS).as_posix() for p in build.DOCS.rglob('*.html')} - approved
    if extra:
        raise ValueError('Unapproved generated routes must be archived outside docs: '+str(sorted(extra)))
    (build.DOCS/'styles').mkdir(parents=True,exist_ok=True)
    shutil.copy2(ROOT/'assets/styles/main.css',build.DOCS/'styles/main.css')
    data = render(build.DOCS)
    print('Scoped Landfall release:', {key:len(value) for key,value in data.items()})
    print('Historical published pages, title histories, PWI and media preserved; no 1982 imports.')
