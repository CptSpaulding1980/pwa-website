import unittest
import build
from bs4 import BeautifulSoup

class SharedLayoutTests(unittest.TestCase):
    def test_shared_brand_header_and_accessible_scroll_region(self):
        soup = BeautifulSoup(build.html_page('Example', '<h1>Example</h1><table><tr><td>Value</td></tr></table>'), 'html.parser')
        self.assertEqual(len(soup.select('header.site-header')), 1)
        self.assertEqual(soup.select_one('.brand-logo')['src'], '/pwa-website/img/PWA_2019-ff.png')
        self.assertEqual(soup.select_one('.skip-link')['href'], '#main-content')
        region = soup.select_one('.table-scroll')
        self.assertIsNotNone(region)
        self.assertEqual(region['tabindex'], '0')
        self.assertEqual(region['role'], 'region')
        self.assertTrue(region.get('aria-label'))

class MarkdownTests(unittest.TestCase):
    def test_semantic_table_header_without_visible_markdown_separator(self):
        rendered = build.markdown_to_html('| Name | Wins |\n| :--- | ---: |\n| **Ox** | 12 |')
        soup = BeautifulSoup(rendered, 'html.parser')
        self.assertEqual([x.text for x in soup.select('thead th')], ['Name', 'Wins'])
        self.assertEqual([x.text for x in soup.select('tbody td')], ['Ox', '12'])
        self.assertNotIn('---', soup.text)

    def test_raw_block_html_not_wrapped_in_paragraphs(self):
        rendered = build.markdown_to_html('<div class="profile">\n<img src="x.png">\n<p>Height: 201cm</p>\n</div>')
        self.assertNotIn('<p><div', rendered)
        self.assertNotIn('<p><p>', rendered)
        self.assertIn('<p>Height: 201cm</p>', rendered)

class AssetTests(unittest.TestCase):
    def test_missing_vault_asset_resolves_to_existing_published_path(self):
        self.assertEqual(build.resolve_image_path('/z_Images/brian-cage_donut.png'), '/pwa-website/img/charts/brian-cage_donut.png')
        self.assertEqual(build.resolve_image_path('/z_Images/Championships/PWA World Heavyweight Championship.png'), '/pwa-website/img/championships/PWA World Heavyweight Championship.png')

class PublishedArchiveTests(unittest.TestCase):
    def test_vault_missing_records_remain_in_indexes(self):
        import json
        from pathlib import Path
        from unittest.mock import patch
        import tempfile
        legacy = json.loads((build.REPO / 'content/published-legacy.json').read_text())
        with tempfile.TemporaryDirectory(dir=build.REPO) as temp, patch.object(build, 'DOCS', Path(temp)):
            events, wrestlers = build.preserve_published_archive([], [])
            self.assertEqual(len(events), 2)
            self.assertEqual(len(wrestlers), 2)
            for item in legacy:
                target = Path(temp) / item['kind'] / item['record']['slug'] / 'index.html'
                self.assertIn('class="site-header"', target.read_text())
            events2, wrestlers2 = build.preserve_published_archive(events, wrestlers)
            self.assertEqual(events, events2)
            self.assertEqual(wrestlers, wrestlers2)

class HomepageTests(unittest.TestCase):
    def test_magazine_uses_real_events_current_champions_and_ranking(self):
        import json
        from pathlib import Path
        from unittest.mock import patch
        import tempfile
        events = json.loads((build.DOCS / 'events.json').read_text())
        wrestlers = json.loads((build.DOCS / 'wrestlers.json').read_text())
        champs = json.loads((build.DOCS / 'championships.json').read_text())
        # Reuse the real detail pages; homepage extraction must not invent canon.
        with tempfile.TemporaryDirectory(dir=build.REPO) as temp:
            output = Path(temp)
            import shutil
            shutil.copytree(build.DOCS / 'championships', output / 'championships')
            shutil.copytree(build.DOCS / 'rankings', output / 'rankings')
            shutil.copytree(build.DOCS / 'img', output / 'img')
            with patch.object(build, 'DOCS', output):
                build.generate_homepage(events, wrestlers, champs)
            soup = BeautifulSoup((output / 'index.html').read_text(), 'html.parser')
        self.assertEqual(len(soup.select('.stat-item')), 3)
        self.assertEqual(len(soup.select('.champion-card')), len(champs))
        self.assertIn(events[0]['title'], soup.get_text())
        self.assertIn('Ox Hemlock', soup.select_one('.champions-panel').get_text())
        self.assertTrue(soup.select('.ranking-preview tr'))
        self.assertFalse(soup.select('a a'))
        self.assertEqual(soup.select_one('.nav-links a[aria-current]')['href'], '/pwa-website/')

if __name__ == '__main__':
    unittest.main()
