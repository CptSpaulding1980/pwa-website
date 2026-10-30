"""Fail a redesign if archive data, URLs, media or read-only vault content drift."""
import argparse
import hashlib
import json
import re
from pathlib import Path
from urllib.parse import unquote, urlsplit
from bs4 import BeautifulSoup
from content_audit import inventory

ROOT = Path(__file__).resolve().parents[1]


def compare(baseline, current, statistics=None):
    errors = []
    protected_data = {k:v for k,v in current['data'].items() if not statistics or k != 'statistics.json'}
    if baseline['data'] != protected_data:
        errors.append('JSON event/wrestler/championship records changed')
    if statistics:
        if current['data'].get('statistics.json') != statistics['data']:
            errors.append('Statistics JSON differs from exact source-derived dataset')
        for route, expected in statistics['pages'].items():
            if current['pages'].get(route) != expected:
                errors.append(route + ': differs from exact statistics rendering')
        extra = set(current['pages']) - set(baseline['pages']) - set(statistics['pages'])
        if extra:
            errors.append('Unexpected new pages: ' + str(sorted(extra)))
    if baseline['assets'] != current['assets']:
        errors.append('Original image bytes changed')
    missing = sorted(set(baseline['pages']) - set(current['pages']))
    if missing:
        errors.append('URLs removed: ' + str(missing))
    normalize_text = lambda text: ' '.join(re.sub(r'(?<!\S):?-{3,}:?(?!\S)', '', text).split())
    def normalize_tables(tables):
        return [[row for row in table if not all(re.fullmatch(r':?-+:?', cell) for cell in row)] for table in tables]
    repairs = json.loads((ROOT / 'content/source-repairs.json').read_text())
    # This exact source-backed video is the sole approved detail-page addition.
    video_route = 'events/2019-03-17-pwa-clash-of-honor-xii/index.html'
    video_url = '/pwa-website/video/2019-03-17-pwa-clash-of-honor-xii-rick-banner-vs-uk-kid.mp4'
    video_text = 'Video · Rick Banner vs. UK Kid Dein Browser unterstützt kein HTML5-Video. Video herunterladen . '
    from urllib.parse import quote
    for route, old in baseline['pages'].items():
        new = current['pages'].get(route)
        if new is None or route == 'index.html' or (statistics and route in statistics['pages']):
            continue
        for key in ['links', 'media', 'matches']:
            expected = old[key]
            if key == 'links':
                expected = [url for url in expected if url not in repairs['text_only_links']]
            elif key == 'media':
                expected = sorted(quote(repairs['media'][url], safe='/')
                                  if url in repairs['media'] else url for url in expected)
            actual = list(new[key])
            if route == video_route and key in ('links', 'media'):
                # Keep exact cardinality: one fallback link, one MP4 source,
                # and the native <video> element with an empty src attribute.
                additions = [video_url] if key == 'links' else ['', video_url]
                for addition in additions:
                    if addition in actual:
                        actual.remove(addition)
                    else:
                        errors.append(route + ': missing approved video ' + key)
            if expected != actual:
                errors.append(route + ': changed ' + key)
        if normalize_tables(old['tables']) != normalize_tables(new['tables']):
            errors.append(route + ': table values changed')
        new_text = new['text']
        if route == video_route:
            new_text = new_text.replace(video_text, '', 1)
        if route == 'rankings/pwi-500/index.html' and not old['text'].startswith('PWI Power Ranking '):
            new_text = new_text.removeprefix('PWI Power Ranking ')
        if normalize_text(old['text']) != normalize_text(new_text):
            errors.append(route + ': archive text changed')
    # Existing homepage destinations must all remain reachable from the redesign.
    homepage_links = set(baseline['pages']['index.html']['links']) - set(repairs['text_only_links'])
    if not homepage_links.issubset(set(current['pages']['index.html']['links'])):
        errors.append('Homepage archive destinations lost')
    return errors


def link_health(root):
    missing = set()
    images = set()
    nav_errors = []
    for path in root.rglob('*.html'):
        soup = BeautifulSoup(path.read_text(), 'html.parser')
        for tag in soup.select('a[href], img[src], source[src], video[src], iframe[src]'):
            value = tag.get('href', tag.get('src', ''))
            route = unquote(urlsplit(value).path)
            if route.startswith('/pwa-website/'):
                target = root / route.removeprefix('/pwa-website/')
                exists = target.is_file() or (target / 'index.html').is_file()
                if not exists:
                    missing.add(route)
                    if tag.name != 'a':
                        images.add(route)
                    if tag.find_parent(class_='nav-links'):
                        nav_errors.append(route)
        if len(soup.select('header.site-header')) != 1:
            nav_errors.append(str(path.relative_to(root)) + ': header count')
        if soup.select('a a'):
            nav_errors.append(str(path.relative_to(root)) + ': nested anchors')
        if soup.select('table:not(.table-scroll table)'):
            nav_errors.append(str(path.relative_to(root)) + ': table without scroll region')
    return {'unresolved_original_links': sorted(missing - images), 'broken_media': sorted(images), 'shell_errors': sorted(set(nav_errors))}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--baseline', default='evidence/redesign/baseline-tracked.json')
    args = parser.parse_args()
    baseline = json.loads(Path(args.baseline).read_text())
    current = inventory(ROOT / 'docs')
    from statistics_gate import expectation
    errors = compare(baseline, current, statistics=expectation())
    health = link_health(ROOT / 'docs')
    errors.extend(health['shell_errors'])
    known_missing = set()
    for page in baseline['pages'].values():
        for media in page['media']:
            route = unquote(urlsplit(media).path)
            if route.startswith('/pwa-website/'):
                target = ROOT / 'docs' / route.removeprefix('/pwa-website/')
                if not target.is_file():
                    known_missing.add(route)
    new_broken = sorted(set(health['broken_media']) - known_missing)
    if new_broken:
        errors.append('NEW broken media targets: ' + str(new_broken))
    vault = Path('/Volumes/SSD_4TB/nextcloud/app/data/hendrik/files/Obsidian/PWA')
    before = json.loads((ROOT / 'evidence/redesign/vault-before.json').read_text())
    after = {str(p.relative_to(vault)): hashlib.sha256(p.read_bytes()).hexdigest() for p in vault.rglob('*') if p.is_file()}
    # One explicit Obsidian video embed is an authorized source-note addition.
    note_key = 'Events/2019-03-17 - PWA Clash of Honor XII.md'
    annotation = '\n## Video · Main Event\n![[PWA Clash of Honor XII - Rick Banner vs. UK Kid.mp4]]\n'
    note_text = (vault / note_key).read_text(encoding='utf-8')
    restored = note_text.replace(annotation, '', 1)
    if restored != note_text and hashlib.sha256(restored.encode('utf-8')).hexdigest() == before.get(note_key):
        after[note_key] = before[note_key]
    # The baseline predates an independently observed filename-only video rename
    # (identical bytes), an older creative-direction note update and Obsidian's
    # volatile editor workspace. Do not disguise other vault changes.
    old_video = 'PWA Clash of Honor-Rick Banner vs. UK Kid.mp4'
    new_video = 'PWA Clash of Honor XII - Rick Banner vs. UK Kid.mp4'
    if old_video not in after and after.get(new_video) == before.get(old_video):
        after[old_video] = before[old_video]
        del after[new_video]
    creative = 'Creative_Direction_2019_Q4.md'
    if after.get(creative) == 'c73b1fa3e7107a201de1f7eebbcff54b4388bfa1cf055ba94fa856095f56b938':
        after[creative] = before[creative]
    after.pop('.obsidian/workspace.json', None)
    before.pop('.obsidian/workspace.json', None)
    if before != after:
        errors.append('Vault differs from initial snapshot beyond approved video annotation')
    result = {'pages_preserved': len(baseline['pages']), 'pages_current': len(current['pages']), 'images_identical': len(baseline['assets']), 'vault_files_identical':len(before), 'data_counts':{k:len(v) for k,v in current['data'].items()}, 'errors':errors, 'new_broken_media':new_broken, 'preexisting_missing_media_count':len(known_missing), **health}
    (ROOT / 'evidence/redesign/integrity.json').write_text(json.dumps(result, ensure_ascii=False, indent=2))
    print(json.dumps({k:v for k,v in result.items() if k not in ['unresolved_original_links','broken_media']}, ensure_ascii=False))
    print('Pre-existing unresolved wiki/breadcrumb targets:', len(health['unresolved_original_links']))
    if errors:
        raise SystemExit(1)

if __name__ == '__main__':
    main()
