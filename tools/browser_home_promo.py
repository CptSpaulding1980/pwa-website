"""Exercise actual promo playback, looping, keyboard pause and motion preferences."""
import argparse
import json
import threading
from http.server import ThreadingHTTPServer
from pathlib import Path
from playwright.sync_api import sync_playwright, expect
from browser_audit import Handler

ROOT = Path(__file__).resolve().parents[1]


class VideoHandler(Handler):
    def copyfile(self, source, outputfile):
        # Browsers cancel media transfers when navigating or after seeking.
        try:
            super().copyfile(source, outputfile)
        except (BrokenPipeError, ConnectionResetError):
            pass


def run(label, base_url=None):
    out = ROOT / 'evidence/home-promo' / label
    out.mkdir(parents=True, exist_ok=True)
    server = ThreadingHTTPServer(('127.0.0.1', 0), VideoHandler)
    threading.Thread(target=server.serve_forever, daemon=True).start()
    base = base_url or f'http://127.0.0.1:{server.server_port}/pwa-website/'
    records = []
    with sync_playwright() as p:
        browser = p.chromium.launch()
        for width in [320, 375, 768, 1440, 1920]:
            for reduced in [False, True]:
                context = browser.new_context(viewport={'width': width, 'height': 1000},
                    is_mobile=width < 768, has_touch=width < 768,
                    reduced_motion='reduce' if reduced else 'no-preference')
                page = context.new_page()
                errors = []
                page.on('pageerror', lambda error: errors.append(str(error)))
                response = page.goto(base, wait_until='load')
                video = page.locator('#home-promo-video')
                button = page.locator('.home-promo-toggle')
                if reduced:
                    page.wait_for_timeout(500)
                    assert video.evaluate('(v)=>v.paused && !v.autoplay')
                    before = video.evaluate('(v)=>v.currentTime')
                    page.wait_for_timeout(400)
                    assert video.evaluate('(v)=>v.currentTime') == before
                else:
                    page.wait_for_function('!document.querySelector("video").paused && document.querySelector("video").currentTime > 0.1')
                initial = video.evaluate('v=>({paused:v.paused,muted:v.muted,loop:v.loop,autoplay:v.autoplay,controls:v.controls,playsInline:v.playsInline,time:v.currentTime})')
                assert initial['muted'] and initial['loop'] and initial['playsInline'] and not initial['controls']
                assert response.status == 200 and not errors
                assert page.evaluate('document.documentElement.scrollWidth <= innerWidth')
                assert video.evaluate('(v)=>v.getBoundingClientRect().width <= innerWidth')
                button.focus()
                assert button.evaluate('(b)=>getComputedStyle(b).outlineStyle') != 'none'
                page.keyboard.press('Enter')
                if reduced:
                    page.wait_for_function('!document.querySelector("video").paused && document.querySelector("video").currentTime > 0.1')
                else:
                    page.wait_for_function('document.querySelector("video").paused')
                    expect(button).to_have_text('Promo fortsetzen')
                    page.keyboard.press('Enter')
                    page.wait_for_function('!document.querySelector("video").paused')
                # Cross the real end of the file, then observe the loop restart and advance.
                page.wait_for_function('Number.isFinite(document.querySelector("video").duration)')
                duration = video.evaluate('(v)=>{v.currentTime=v.duration-0.25;return v.duration}')
                page.wait_for_function('document.querySelector("video").currentTime < 2 && !document.querySelector("video").paused', timeout=20000)
                page.wait_for_function('document.querySelector("video").currentTime > 0.1 && document.querySelector("video").currentTime < 3')
                loop_time = video.evaluate('(v)=>v.currentTime')
                page.emulate_media(reduced_motion='no-preference')
                page.wait_for_function('!matchMedia("(prefers-reduced-motion: reduce)").matches && !document.querySelector("video").paused')
                page.wait_for_timeout(100)
                page.emulate_media(reduced_motion='reduce')
                page.wait_for_function('document.querySelector("video").paused')
                expect(button).to_have_text('Promo fortsetzen')
                if width in [375, 1440] and not reduced:
                    page.screenshot(path=str(out / f'home-{width}.png'), full_page=True)
                records.append({'width': width, 'reduced_motion': reduced, 'initial': initial,
                    'duration': duration, 'loop_restart_time': loop_time, 'keyboard_toggle': True,
                    'dynamic_reduced_motion_paused': True, 'errors': errors})
                page.goto(base + 'events/2019-03-17-pwa-clash-of-honor-xii/', wait_until='load')
                event = page.locator('video').evaluate('(v)=>({controls:v.controls,preload:v.preload,autoplay:v.autoplay,paused:v.paused,loop:v.loop})')
                assert event == {'controls': True, 'preload': 'metadata', 'autoplay': False, 'paused': True, 'loop': False}, event
                records[-1]['event_player'] = event
                context.close()
        browser.close()
    server.shutdown()
    (out / 'browser.json').write_text(json.dumps(records, indent=2))
    print(json.dumps({'base': base, 'checks': len(records), 'all_passed': True, 'evidence': str(out)}))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('label')
    parser.add_argument('--base-url')
    args = parser.parse_args()
    run(args.label, args.base_url)
