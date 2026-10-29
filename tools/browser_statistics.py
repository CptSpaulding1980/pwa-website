"""Exercise all four statistics tabs, links and keyboard tables in real Chromium."""
import argparse
import json
import threading
from http.server import ThreadingHTTPServer
from pathlib import Path
from playwright.sync_api import sync_playwright
from browser_audit import Handler

ROOT=Path(__file__).resolve().parents[1]
ROUTES=['top','worst','longest','shortest']


def run(label,base=None):
    out=ROOT/'evidence/statistics'/label
    out.mkdir(parents=True,exist_ok=True)
    server=ThreadingHTTPServer(('127.0.0.1',0),Handler)
    threading.Thread(target=server.serve_forever,daemon=True).start()
    base=base or f'http://127.0.0.1:{server.server_port}/pwa-website/'
    records=[]
    from urllib.parse import unquote, urlsplit
    baseline=json.loads((ROOT/'evidence/statistics/before/inventory.json').read_text())
    known_missing={unquote(urlsplit(url).path) for page in baseline['pages'].values() for url in page['media']
                   if url.startswith('/pwa-website/') and not (ROOT/'docs'/unquote(urlsplit(url).path).removeprefix('/pwa-website/')).is_file()}
    with sync_playwright() as p:
        browser=p.chromium.launch()
        for width in [320,375,768,1440,1920]:
            page=browser.new_page(viewport={'width':width,'height':1080},device_scale_factor=1)
            failures=[]
            page.on('pageerror',lambda error:failures.append({'text':str(error),'url':''}))
            page.on('console',lambda msg:failures.append({'text':msg.text,'url':msg.location.get('url','')}) if msg.type=='error' else None)
            response=page.goto(base,wait_until='networkidle')
            assert response.status==200
            page.locator('.nav-links a',has_text='Statistiken').click()
            page.wait_for_load_state('networkidle')
            for kind in ROUTES:
                page.locator(f'.statistics-nav a[href$="/{kind}-25-matches/"]').click()
                page.wait_for_load_state('networkidle')
                assert page.url==base+f'rankings/{kind}-25-matches/'
                assert page.title()=='Statistiken | PWA'
                assert page.locator('h1').inner_text()=='STATISTIKEN' or page.locator('h1').inner_text()=='Statistiken'
                assert page.locator('tbody tr').count()==25
                assert page.locator('.nav-links a[aria-current]').inner_text()=='Statistiken'
                assert page.locator('.statistics-nav a[aria-current]').get_attribute('href').endswith(f'/{kind}-25-matches/')
                size=page.evaluate('({width:innerWidth,scrollWidth:document.documentElement.scrollWidth})')
                assert size['width']==size['scrollWidth'],size
                cards=page.locator('.statistics-card').evaluate_all('(xs)=>xs.map(x=>({client:x.clientWidth,scroll:x.scrollWidth,text:x.textContent}))')
                assert all(c['scroll']<=c['client'] for c in cards),cards
                for tab in page.locator('.statistics-nav a').all():
                    box=tab.bounding_box()
                    assert box['x']>=0 and box['x']+box['width']<=width and box['height']>=44,box
                    tab.focus()
                    assert tab.evaluate('(x)=>getComputedStyle(x).outlineStyle')!='none'
                page.locator('.skip-link').focus()
                page.keyboard.press('Enter')
                assert page.evaluate('document.activeElement.id')=='main-content'
                page.screenshot(path=str(out/f'{kind}-{width}.png'),full_page=False)
                region=page.locator('.table-scroll')
                region.scroll_into_view_if_needed()
                region.focus()
                assert region.get_attribute('role')=='region' and region.get_attribute('tabindex')=='0'
                scrollable=region.evaluate('(x)=>x.scrollWidth>x.clientWidth')
                if scrollable:
                    page.keyboard.press('ArrowRight')
                    page.wait_for_timeout(100)
                    assert region.evaluate('(x)=>x.scrollLeft')>0
                page.screenshot(path=str(out/f'{kind}-{width}-table.png'),full_page=False)
                region.evaluate('(x)=>x.scrollLeft=0')
                assert not failures,failures  # Statistics pages themselves must be clean.
                # Real Show and person link navigation (not just href existence).
                show=page.locator('tbody tr').first.locator('td').nth(2).locator('a')
                show_url=show.get_attribute('href')
                show.click()
                page.wait_for_load_state('networkidle')
                assert page.url.endswith(show_url)
                assert page.locator('.match-card').count()>0
                page.go_back(wait_until='networkidle')
                person=page.locator('tbody a[href*="/wrestlers/"]').first
                person_url=person.get_attribute('href')
                person.click()
                page.wait_for_load_state('networkidle')
                assert page.url.endswith(person_url)
                assert page.locator('h1').count()==1
                page.go_back(wait_until='networkidle')
                page.locator('.statistics-definitions summary').click()
                assert page.locator('.statistics-definitions').get_attribute('open') is not None
                assert '108:108' in page.locator('.statistics-definitions').inner_text()
                preexisting=[f for f in failures if unquote(urlsplit(f['url']).path) in known_missing and '404' in f['text']]
                assert len(preexisting)==len(failures),failures
                records.append(dict(width=width,kind=kind,url=page.url,rows=25,body_overflow=False,cards=cards,
                                    tab_click=True,show_link=show_url,person_link=person_url,keyboard_table_scroll=scrollable,
                                    skip_link=True,definitions_open=True,preexisting_destination_media=preexisting,errors=[]))
                failures.clear()
            page.close()
        browser.close()
    server.shutdown()
    (out/'browser.json').write_text(json.dumps(records,ensure_ascii=False,indent=2))
    print(json.dumps({'checks':len(records),'screenshots':len(list(out.glob('*.png'))),'errors':[],'output':str(out)},ensure_ascii=False))

if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('label')
    parser.add_argument('--base-url')
    args=parser.parse_args()
    run(args.label,args.base_url)
