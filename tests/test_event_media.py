"""Regression tests for exact vault video mapping and real generated players."""
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from bs4 import BeautifulSoup
from event_media import discover, ensure_note_embed, homepage_player

ROOT = Path(__file__).resolve().parents[1]
VAULT = Path('/Volumes/SSD_4TB/nextcloud/app/data/hendrik/files/Obsidian/PWA')
EVENT = '2019-03-17-pwa-clash-of-honor-xii'


class VideoTests(unittest.TestCase):
    def test_exact_card_only_and_ambiguous_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            vault = Path(directory)
            (vault / 'PWA Clash of Honor XII - Rick Banner vs. UK Kid.mp4').write_bytes(b'mp4')
            (vault / 'CSW Clash of Honor XII - Rick Banner vs. UK Kid.mp4').write_bytes(b'mp4')
            (vault / 'PWA Clash of Honor XII - Rick Banner vs. Someone Else.mp4').write_bytes(b'mp4')
            rows = [('2019-03-17', 'PWA Clash of Honor XII',
                     [{'name': 'PWA World Heavyweight Championship: Rick Banner vs. UK Kid (c)'}])]
            self.assertEqual([p.name for p in discover(vault, rows)['2019-03-17']],
                             ['PWA Clash of Honor XII - Rick Banner vs. UK Kid.mp4'])
            with self.assertRaisesRegex(ValueError, 'Ambiguous'):
                discover(vault, rows + [('1993-04-01', rows[0][1], rows[0][2])])

    def test_note_annotation_survives_regeneration(self):
        with tempfile.TemporaryDirectory() as directory:
            note = Path(directory) / 'event.md'
            video = Path('PWA Clash of Honor XII - Rick Banner vs. UK Kid.mp4')
            note.write_text('---\ntitle: Event\n---\n## Anmerkungen\nCanonical matches\n')
            with patch('event_media.subprocess.run') as scan:
                self.assertTrue(ensure_note_embed(note, video))
                self.assertFalse(ensure_note_embed(note, video))
                scan.assert_called_once()
            self.assertIn('![[PWA Clash of Honor XII - Rick Banner vs. UK Kid.mp4]]', note.read_text())
            self.assertIn('Canonical matches', note.read_text())

    def test_homepage_is_quiet_loop_not_event_player(self):
        html = homepage_player(ROOT / 'docs/video/pwa-homepage.mp4', ROOT / 'docs', '/pwa-website')
        soup = BeautifulSoup(html, 'html.parser')
        video = soup.select_one('video')
        for attribute in ['autoplay', 'loop', 'muted', 'playsinline']:
            self.assertTrue(video.has_attr(attribute), attribute)
        self.assertFalse(video.has_attr('controls'))
        self.assertFalse(soup.select('h2, a'))
        self.assertEqual(soup.select_one('button')['aria-controls'], video['id'])
        self.assertIn('prefers-reduced-motion: reduce', html)

    def test_generated_players_and_sources(self):
        note = (VAULT / 'Events' / '2019-03-17 - PWA Clash of Honor XII.md').read_text()
        self.assertIn('![[PWA Clash of Honor XII - Rick Banner vs. UK Kid.mp4]]', note)
        for page, expected in [(ROOT / 'docs/index.html', 'pwa-homepage.mp4'),
                               (ROOT / 'docs/events' / EVENT / 'index.html',
                                '2019-03-17-pwa-clash-of-honor-xii-rick-banner-vs-uk-kid.mp4')]:
            soup = BeautifulSoup(page.read_text(), 'html.parser')
            players = soup.select('video[aria-label]')
            self.assertEqual(len(players), 1, page)
            if page == ROOT / 'docs/index.html':
                for attribute in ['autoplay', 'loop', 'muted', 'playsinline']:
                    self.assertTrue(players[0].has_attr(attribute), attribute)
                self.assertFalse(players[0].has_attr('controls'))
                self.assertFalse(soup.select('.home-video, .home-promo h2, .home-promo a'))
            else:
                self.assertTrue(players[0].has_attr('controls'))
                self.assertEqual(players[0]['preload'], 'metadata')
                self.assertFalse(players[0].has_attr('autoplay'))
                self.assertFalse(players[0].has_attr('loop'))
            self.assertIsNone(players[0].get('poster'))
            source = players[0].select_one('source[type="video/mp4"]')
            self.assertEqual(source['src'], '/pwa-website/video/' + expected)
            media = ROOT / 'docs/video' / expected
            self.assertTrue(media.is_file())
            self.assertLess(media.stat().st_size, 100_000_000)
            self.assertGreater(media.stat().st_size, 1_000_000)


if __name__ == '__main__':
    unittest.main()
