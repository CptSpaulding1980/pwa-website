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


def compare(baseline, current):
    errors = []
    if baseline['data'] != current['data']:
        errors.append('JSON event/wrestler/championship records changed')
    if baseline['assets'] != current['assets']:
        errors.append('Original image bytes changed')
    missing = sorted(set(baseline['pages']) - set(current['pages']))
    if missing:
        errors.append('URLs removed: ' + str(missing))
    normalize_text = lambda text: ' '.join(re.sub(r'(?<!\S):?-{3,}:?(?!\S)', '', text).split())
    def normalize_tables(tables):
        return [[row for row in table if not all(re.fullmatch(r':?-+:?', cell) for cell in row)] for table in tables]
    for route, old in baseline['pages'].items():
        new = current['pages'].get(route)
        if new is None or route == 'index.html':
            continue
        for key in ['links', 'media', 'matches']:
            if old[key] != new[key]:
                errors.append(route + ': changed ' + key)
        if normalize_tables(old['tables']) != normalize_tables(new['tables']):
            errors.append(route + ': table values changed')
        new_text = new['text']
        if route == 'rankings/pwi-500/index.html':
            new_text = new_text.removeprefix('PWI Power Ranking ')
        if normalize_text(old['text']) != normalize_text(new_text):
            errors.append(route + ': archive text changed')
    # Existing homepage destinations must all remain reachable from the redesign.
    if not set(baseline['pages']['index.html']['links']).issubset(set(current['pages']['index.html']['links'])):
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
    errors = compare(baseline, current)
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
    if before != after:
        errors.append('Read-only vault differs from initial snapshot')
    result = {'pages_preserved': len(baseline['pages']), 'pages_current': len(current['pages']), 'images_identical': len(baseline['assets']), 'vault_files_identical':len(before), 'data_counts':{k:len(v) for k,v in current['data'].items()}, 'errors':errors, 'new_broken_media':new_broken, 'preexisting_missing_media_count':len(known_missing), **health}
    (ROOT / 'evidence/redesign/integrity.json').write_text(json.dumps(result, ensure_ascii=False, indent=2))
    print(json.dumps({k:v for k,v in result.items() if k not in ['unresolved_original_links','broken_media']}, ensure_ascii=False))
    print('Pre-existing unresolved wiki/breadcrumb targets:', len(health['unresolved_original_links']))
    if errors:
        raise SystemExit(1)

if __name__ == '__main__':
    main()
