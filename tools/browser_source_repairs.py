"""Real Chromium checks for all 27 repaired portraits, local or canonical live."""
import argparse
import hashlib
import json
import threading
from pathlib import Path
from urllib.parse import quote, unquote, urlsplit
from http.server import ThreadingHTTPServer
from playwright.sync_api import sync_playwright
from browser_audit import Handler

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'evidence/repairs-t_833056e0'


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--base-url')
    args = parser.parse_args()
    audit = json.loads((ROOT / 'evidence/source-audit-t_57b773fb/audit.json').read_text())
    safe = [x for x in audit['media'] if x['category'] == 'safe_existing_pwa_asset']
    allowed = {x['url'] for x in audit['media'] if x not in safe}
    dead = {x['url'] for x in audit['links']}
    server = ThreadingHTTPServer(('127.0.0.1', 0), Handler)
    threading.Thread(target=server.serve_forever, daemon=True).start()
    base = args.base_url or f'http://127.0.0.1:{server.server_port}/pwa-website/'
    label = 'live' if args.base_url else 'local'
    records, images = [], []
    with sync_playwright() as p:
        browser = p.chromium.launch()
        for width in [375, 1440]:
            page = browser.new_page(viewport={'width': width, 'height': 900})
            errors = []
            page.on('pageerror', lambda error: errors.append(str(error)))
            for item in safe:
                route = item['generated_occurrences'][0]['path'].removeprefix('docs/')
                image_url = quote(item['target_url'], safe='/')
                with page.expect_response(lambda r: unquote(urlsplit(r.url).path) == item['target_url']) as response:
                    navigation = page.goto(base + quote(route, safe='/'), wait_until='networkidle')
                actual = response.value
                digest = hashlib.sha256(actual.body()).hexdigest()
                image = page.locator('img[src="' + image_url + '"]')
                assert image.count() == 1
                image.scroll_into_view_if_needed()
                size = image.evaluate('(x)=>({w:x.naturalWidth,h:x.naturalHeight,complete:x.complete})')
                assert actual.status == 200 and digest == item['sha256'] and size['w'] > 0 and size['complete']
                assert navigation.status == 200
                images.append({'width': width, 'route': route, 'url': actual.url, 'status': actual.status, 'sha256': digest, **size})
                if any(name in route for name in ['bob-harris', 'felix-santana-jr', 'harley-race']):
                    page.screenshot(path=str(OUT / f'{label}-{width}-{Path(route).parent.name}.png'))
            routes = ['championships/pwa-world-tag-team-championship/', 'wrestlers/tri-clops/',
                      'wrestlers/theobold-lovecraft/', 'wrestlers/sammy-blake/',
                      'rankings/top-25-matches/', 'rankings/worst-25-matches/']
            for route in routes:
                response = page.goto(base + route, wait_until='networkidle')
                data = page.evaluate('''() => ({
                  links:[...document.querySelectorAll('a[href]')].map(x=>x.getAttribute('href')),
                  broken:[...document.images].filter(x=>!x.complete||!x.naturalWidth).map(x=>decodeURI(x.getAttribute('src'))),
                  overflow:document.documentElement.scrollWidth>innerWidth,
                  breadcrumb:document.querySelector('.breadcrumb')?.textContent.trim(),
                  text:document.querySelector('main').innerText})''')
                assert response.status == 200 and not data['overflow'] and not (set(data['links']) & dead)
                assert set(data['broken']) <= allowed
                if route.startswith('rankings/'):
                    assert 'Rankings' in data['breadcrumb']
                if 'world-tag-team' in route:
                    assert 'Chris Hero & Claudio Castagnoli' in data['text']
                if 'sammy-blake' in route:
                    assert 'Veteran Veteran Devastators' in data['text']
                page.screenshot(path=str(OUT / f'{label}-{width}-{route.strip("/").replace("/", "-")}.png'))
                records.append({'width': width, 'route': route, 'status': response.status, **data})
            assert not errors, errors
            page.close()
        browser.close()
    server.shutdown()
    assert len({r['url'] for r in images}) == 27 and len(images) == 54
    (OUT / f'browser-{label}.json').write_text(json.dumps({'images': images, 'pages': records, 'errors': []}, ensure_ascii=False, indent=2))
    print(json.dumps({'label': label, 'unique_images': 27, 'image_checks': len(images), 'page_checks': len(records), 'errors': []}))


if __name__ == '__main__':
    main()
