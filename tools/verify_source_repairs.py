"""Exact before/after proof against the independent, approved source audit.

Usage: python3 tools/verify_source_repairs.py
Evidence is intentionally outside docs/ and is archived separately, not deployed.
"""
import hashlib
import json
import zipfile
from collections import Counter
from pathlib import Path
from urllib.parse import quote
from bs4 import BeautifulSoup
from content_audit import inventory
from verify_integrity import compare, link_health

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'evidence/repairs-t_833056e0'
AUDIT = ROOT / 'evidence/source-audit-t_57b773fb/audit.json'


def main():
    audit = json.loads(AUDIT.read_text())
    repairs = json.loads((ROOT / 'content/source-repairs.json').read_text())
    media = {x['url']: x['target_url'] for x in audit['media'] if x['category'] == 'safe_existing_pwa_asset'}
    links = {x['url'] for x in audit['links']}
    assert repairs['media'] == media and set(repairs['text_only_links']) == links
    assert len(media) == 27 and len(links) == 59
    before = json.loads((OUT / 'before.json').read_text())
    after = inventory(ROOT / 'docs')
    assert not compare(before, after), compare(before, after)
    assert set(before['pages']) == set(after['pages']) and len(after['pages']) == 518
    # Stronger than text-only comparison: the complete parsed HTML tree may only
    # differ by the approved anchor wrappers and exact image src attributes.
    seen_links, seen_media = Counter(), Counter()
    with zipfile.ZipFile(OUT / 'before-source-output.zip') as old:
        for route in before['pages']:
            expected = BeautifulSoup(old.read('docs/' + route), 'html.parser')
            for a in expected.select('a[href]'):
                if a['href'] in links:
                    seen_links[a['href']] += 1
                    a.name = 'span'
                    a.attrs = {}
            for img in expected.select('img[src]'):
                if img['src'] in media:
                    seen_media[img['src']] += 1
                    img['src'] = quote(media[img['src']], safe='/')
            actual = BeautifulSoup((ROOT / 'docs' / route).read_text(), 'html.parser')
            assert str(expected) == str(actual), 'Unexpected DOM drift: ' + route
        for name in ['events.json', 'wrestlers.json', 'championships.json']:
            assert old.read('docs/' + name) == (ROOT / 'docs' / name).read_bytes(), name
    assert dict(seen_links) == {x['url']: len(x['generated_occurrences']) for x in audit['links']}
    assert dict(seen_media) == {x['url']: len(x['generated_occurrences']) for x in audit['media'] if x['url'] in media}
    health = link_health(ROOT / 'docs')
    expected_missing = sorted(x['url'] for x in audit['media'] if x['url'] not in media)
    assert health['broken_media'] == expected_missing and len(expected_missing) == 187
    assert not health['unresolved_original_links'] and not health['shell_errors']
    assert hashlib.sha256((ROOT / 'content/published-legacy.json').read_bytes()).hexdigest() == '65c40e0bcec586fe6593a7b644a2ac61024f57054c54d069a8559dcfd61c179c'
    vault = Path('/Volumes/SSD_4TB/nextcloud/app/data/hendrik/files/Obsidian/PWA')
    hashes = {str(p.relative_to(vault)): hashlib.sha256(p.read_bytes()).hexdigest() for p in vault.rglob('*') if p.is_file()}
    assert hashes == audit['vault_hashes']
    media_rows = []
    for item in audit['media']:
        if item['url'] not in media:
            continue
        path = ROOT / 'docs' / item['target_url'].removeprefix('/pwa-website/')
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        assert digest == item['sha256']
        media_rows.append({'before': item['url'], 'after': quote(item['target_url'], safe='/'), 'sha256': digest, 'occurrences': seen_media[item['url']]})
    result = {'pages': [len(before['pages']), len(after['pages'])],
              'images_identical': len(after['assets']), 'vault_files_identical': len(hashes),
              'data_counts': {k: len(v) for k, v in after['data'].items()},
              'broken_media': [214, 187], 'invalid_link_targets': [59, 0],
              'invalid_link_occurrences': [sum(seen_links.values()), 0],
              'new_broken_references': [], 'unexpected_dom_changes': [],
              'fallback_sha256_unchanged': True, 'media': media_rows,
              'links': [{'before': url, 'after': 'unchanged label, no link', 'occurrences': seen_links[url]} for url in sorted(links)],
              'open_media': expected_missing}
    (OUT / 'matrix.json').write_text(json.dumps(result, ensure_ascii=False, indent=2))
    print(json.dumps({k: v for k, v in result.items() if k not in ['media', 'links', 'open_media']}, ensure_ascii=False))


if __name__ == '__main__':
    main()
