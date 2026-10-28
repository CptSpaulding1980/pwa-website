"""Real Chromium responsive smoke tests; screenshots and DOM evidence."""
import argparse
import functools
import json
import threading
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import unquote
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
PAGES = ['', 'events/', 'events/2019-10-03-pwa-power-hour-31/', 'wrestlers/', 'wrestlers/ox-hemlock/', 'championships/', 'championships/pwa-world-heavyweight-championship/', 'rankings/pwi-500/', 'rankings/top-25-matches/', 'rankings/worst-25-matches/']

class Handler(SimpleHTTPRequestHandler):
    def translate_path(self, path):
        return str(ROOT / 'docs' / unquote(path.split('?', 1)[0]).removeprefix('/pwa-website/'))
    def log_message(self, *args):
        pass


def run(label, strict=False, base_url=None):
    output = ROOT / 'evidence' / 'redesign' / label
    output.mkdir(parents=True, exist_ok=True)
    server = ThreadingHTTPServer(('127.0.0.1', 0), Handler)
    threading.Thread(target=server.serve_forever, daemon=True).start()
    records = []
    with sync_playwright() as p:
        browser = p.chromium.launch()
        for width in [320, 375, 768, 1440, 1920]:
            for route in PAGES:
                page = browser.new_page(viewport={'width': width, 'height': 1000}, device_scale_factor=1)
                errors = []
                page.on('pageerror', lambda e: errors.append(str(e)))
                page.on('console', lambda message: errors.append(message.text) if message.type == 'error' else None)
                response = page.goto((base_url or f'http://127.0.0.1:{server.server_port}/pwa-website/') + route, wait_until='networkidle')
                data = page.evaluate('''() => ({width: innerWidth, scrollWidth: document.documentElement.scrollWidth,
                  headings: [...document.querySelectorAll('h1')].map(x=>x.textContent),
                  headers: document.querySelectorAll('.site-header').length,
                  tables: [...document.querySelectorAll('.table-scroll')].map(x=>({client:x.clientWidth,scroll:x.scrollWidth,tabindex:x.tabIndex,role:x.getAttribute('role')})),
                  brokenImages:[...document.images].filter(x=>!x.complete||!x.naturalWidth).map(x=>x.getAttribute('src')),
                  nestedAnchors:document.querySelectorAll('a a').length,
                  links:[...document.querySelectorAll('main a')].slice(0,5).map(x=>({text:x.textContent,color:getComputedStyle(x).color,decoration:getComputedStyle(x).textDecorationLine})),
                  nav:[...document.querySelectorAll('.nav-links a')].map(x=>({text:x.textContent,href:x.getAttribute('href'),active:x.getAttribute('aria-current')}))})''')
                data.update(route=route, viewport=width, status=response.status, errors=errors)
                if width in [375, 1440]:
                    filename = (route.strip('/').replace('/', '-') or 'home') + f'-{width}.png'
                    page.screenshot(path=str(output / filename), full_page=not route)
                    if page.locator('.table-scroll').count():
                        page.locator('.table-scroll').first.scroll_into_view_if_needed()
                        page.screenshot(path=str(output / filename.replace('.png', '-data.png')), full_page=False)
                # Exercise the skip link and actual keyboard focus, not merely existence.
                if strict:
                    page.locator('.skip-link').focus()
                    data['focusOutline'] = page.locator('.skip-link').evaluate('(x)=>getComputedStyle(x).outlineStyle')
                    page.keyboard.press('Enter')
                    data['skipTarget'] = page.evaluate('document.activeElement.id')
                # Exercise keyboard focus and horizontal scrolling, not just CSS dimensions.
                for region in page.locator('.table-scroll').all():
                    if region.evaluate('(x)=>x.scrollWidth>x.clientWidth'):
                        region.focus()
                        page.keyboard.press('ArrowRight')
                        page.wait_for_timeout(70)
                        data.setdefault('keyboardScroll', []).append(region.evaluate('(x)=>x.scrollLeft'))
                records.append(data)
                page.close()
        browser.close()
    server.shutdown()
    (output / 'browser.json').write_text(json.dumps(records, ensure_ascii=False, indent=2))
    issues = [r for r in records if r['scrollWidth'] > r['width'] or r['errors'] or r['status'] != 200 or (strict and (r['headers'] != 1 or r['nestedAnchors'] or r['brokenImages'] or r.get('skipTarget') != 'main-content' or r.get('focusOutline') == 'none' or any(x <= 0 for x in r.get('keyboardScroll', []))))]
    print(json.dumps({'checks':len(records),'issues':issues,'broken_image_occurrences':sum(len(r['brokenImages']) for r in records)},ensure_ascii=False))
    if strict and issues:
        raise SystemExit(1)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('label')
    parser.add_argument('--strict',action='store_true')
    parser.add_argument('--base-url')
    args=parser.parse_args()
    run(args.label,args.strict,args.base_url)
