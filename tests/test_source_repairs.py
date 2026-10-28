"""Regression coverage for the explicit, source-audited legacy repairs."""
import unittest
from urllib.parse import quote
import build


class SourceRepairTests(unittest.TestCase):
    def test_audited_space_punctuation_and_published_only_images(self):
        cases = {
            'Bob_Harris.png': 'Bob Harris.png',
            'Felix_Santana_Jr..png': 'Felix_Santana_Jr.png',
            'Harley_Race.png': 'Harley Race.png',
        }
        for old, target in cases.items():
            with self.subTest(old=old):
                self.assertEqual(build.resolve_image_path('/z_Images/Wrestler/' + old),
                                 '/pwa-website/img/wrestler/' + quote(target, safe='/'))
        self.assertEqual(build.resolve_image_path('/z_Images/Wrestler/Kenny_Omega.png'),
                         '/pwa-website/img/Wrestler/Kenny_Omega.png')

    def test_wiki_alias_labels_status_teams_and_real_links(self):
        from bs4 import BeautifulSoup
        labels = ['None', 'Vacant', 'Veteran Devastators',
                  'Veteran Veteran Devastators', 'Chris Hero & Claudio Castagnoli',
                  'Gauntlet', 'Gauntlet Match', 'PWA World Title']
        for label in labels:
            with self.subTest(label=label):
                body = build.convert_wikilinks('[[' + label + '|Exact alias]] [[Ox Hemlock|Ox]]')
                soup = BeautifulSoup(build.html_page('Test', '<h1>Test</h1>' + body), 'html.parser')
                main = soup.select_one('main')
                main.select_one('h1').decompose()
                self.assertEqual(main.get_text(' ', strip=True), 'Exact alias Ox')
                self.assertEqual([a['href'] for a in main.select('a')],
                                 ['/pwa-website/wrestlers/ox-hemlock/'])

    def test_saved_fallback_html_and_rankings_are_repaired_at_render_time(self):
        import hashlib
        from bs4 import BeautifulSoup
        self.assertEqual(hashlib.sha256((build.REPO / 'content/published-legacy.json').read_bytes()).hexdigest(),
                         '65c40e0bcec586fe6593a7b644a2ac61024f57054c54d069a8559dcfd61c179c')
        for title in ['Top 25 Matches', 'Worst 25 Matches']:
            soup = BeautifulSoup(build.html_page(title, build.breadcrumb('Rankings', '/rankings/', title)), 'html.parser')
            self.assertEqual(soup.select_one('.breadcrumb').get_text(' ', strip=True), 'Home › Rankings › ' + title)
            self.assertEqual(len(soup.select('.breadcrumb a')), 1)
        raw = '<a class="old" href="/pwa-website/wrestlers/none/"><strong>Alias &amp; None</strong></a>'
        soup = BeautifulSoup(build.html_page('Old', raw), 'html.parser')
        self.assertEqual(soup.select_one('main strong').text, 'Alias & None')
        self.assertFalse(soup.select('main a'))

    def test_integrity_allows_only_exact_approved_reference_deltas(self):
        import copy
        import sys
        from pathlib import Path
        sys.path.insert(0, str(build.REPO / 'tools'))
        from verify_integrity import compare
        page = {'text': 'None Bob', 'tables': [], 'matches': [],
                'links': ['/pwa-website/wrestlers/none/', '/pwa-website/wrestlers/ox-hemlock/'],
                'media': ['/pwa-website/img/Wrestler/Bob_Harris.png']}
        baseline = {'data': {}, 'assets': {}, 'pages': {'index.html': {'links': []}, 'example.html': page}}
        current = copy.deepcopy(baseline)
        current['pages']['example.html']['links'] = ['/pwa-website/wrestlers/ox-hemlock/']
        current['pages']['example.html']['media'] = ['/pwa-website/img/wrestler/Bob%20Harris.png']
        baseline['pages']['index.html']['links'] = ['/pwa-website/wrestlers/none/']
        current['pages']['index.html']['links'] = []
        baseline['pages']['rankings/pwi-500/index.html'] = dict(page, text='PWI Power Ranking actual')
        current['pages']['rankings/pwi-500/index.html'] = dict(current['pages']['example.html'], text='PWI Power Ranking actual')
        self.assertEqual(compare(baseline, current), [])
        current['pages']['example.html']['links'] = []
        self.assertIn('example.html: changed links', compare(baseline, current))
        current['pages']['example.html']['text'] = 'Changed canon'
        self.assertIn('example.html: archive text changed', compare(baseline, current))

    def test_complete_explicit_allowlist_and_render_idempotence(self):
        from bs4 import BeautifulSoup
        from urllib.parse import unquote
        repairs = build.SOURCE_REPAIRS
        self.assertEqual(len(repairs['media']), 27)
        self.assertEqual(len(repairs['text_only_links']), 59)
        for old, target in repairs['media'].items():
            with self.subTest(image=old):
                expected = quote(target, safe='/')
                self.assertEqual(build.resolve_image_path(old.replace('/pwa-website/img/', '/z_Images/')), expected)
                self.assertTrue((build.DOCS / unquote(expected).removeprefix('/pwa-website/')).is_file())
                raw = '<img src="' + old + '">'
                self.assertEqual(build.repair_source_html(raw), '<img src="' + expected + '">')
        for url in repairs['text_only_links']:
            with self.subTest(link=url):
                raw = '<a href="' + url + '"><em>Exact &amp; unchanged</em></a>'
                rendered = build.repair_source_html(raw)
                self.assertEqual(rendered, '<span><em>Exact &amp; unchanged</em></span>')
                self.assertEqual(build.repair_source_html(rendered), rendered)
        valid = '<a href="/pwa-website/wrestlers/ox-hemlock/">Ox</a>'
        self.assertEqual(build.repair_source_html(valid), valid)
        # Explicit path mappings do not grant a generic underscore resolver.
        self.assertEqual(build.repair_source_html('<img src="/pwa-website/img/Wrestler/Unknown_Name.png">'),
                         '<img src="/pwa-website/img/Wrestler/Unknown_Name.png">')


if __name__ == '__main__':
    unittest.main()
