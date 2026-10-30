import unittest
import importlib.util

class ExtractionTests(unittest.TestCase):
    def test_multiline_rows_alias_pipes_and_numeric_source_not_stars(self):
        import match_statistics as stats
        self.assertTrue(hasattr(stats, 'event_rows'), 'Missing canonical table extractor')
        body = '## Matches\n| # | Match | Finish | Time | Rating | Rating (★) |\n|---|---|---|---|---|---|\n| 1 | [[Alpha\\|Alias]] vs. Beta | First line\nsecond line | 1:02:03 | 103 | ★★★★★ |\n| 2 | Gamma | Finish | 108:108 | 0 | DUD |'
        rows = stats.event_rows(body)
        self.assertEqual(len(rows), 2)
        self.assertEqual(rows[0]['name'], '[[Alpha|Alias]] vs. Beta')
        self.assertEqual(rows[0]['rating'], 103)
        self.assertEqual(rows[0]['seconds'], 3723)
        self.assertEqual(rows[1]['rating'], 0)
        self.assertEqual(rows[1]['duration_status'], 'invalid')

class DatasetTests(unittest.TestCase):
    def test_canonical_dedup_sort_ties_and_summary_use_full_dataset(self):
        import match_statistics as stats
        self.assertTrue(hasattr(stats, 'analyze'), 'Missing full-dataset analysis')
        def row(event, number, rating, seconds, status='valid'):
            return dict(event=event, number=number, rating=rating, seconds=seconds, duration_status=status, date='2000-01-01')
        rows = [row('b',1,90,60), row('a',2,90,120), row('a',1,0,None,'zero'), row('c',1,None,None,'missing')]
        data = stats.analyze(rows + [rows[0]], ['a','b','c','empty'])
        self.assertEqual(data['summary']['records'], 4)
        self.assertEqual(data['summary']['events'], 4)
        self.assertEqual(data['summary']['rated'], 3)
        self.assertEqual(data['summary']['timed'], 2)
        self.assertEqual(data['summary']['rating_mean'], 60)
        self.assertEqual(data['summary']['rating_median'], 90)
        self.assertEqual(data['summary']['duration_mean'], 90)
        self.assertEqual(data['summary']['duration_median'], 90)
        self.assertEqual([(r['event'],r['number']) for r in data['rankings']['top']], [('a',2),('b',1),('a',1)])
        self.assertEqual(data['rankings']['worst'][0]['rating'], 0)
        self.assertEqual(data['rankings']['shortest'][0]['event'], 'b')
        self.assertEqual(data['rankings']['longest'][0]['event'], 'a')
        self.assertEqual(stats.analyze(list(reversed(rows)), ['a','b','c','empty'])['rankings'], data['rankings'])
        with self.assertRaises(ValueError):
            stats.analyze(rows + [dict(rows[0], rating=1)], ['a','b','c'])

    def test_alias_is_not_a_second_event_and_segments_are_not_matches(self):
        import match_statistics as stats
        import build
        data = stats.collect(build.VAULT, build.REPO/'content/published-legacy.json')
        self.assertEqual(data['summary']['events'],238, 'Published population plus Landfall; audited alias must not count twice')
        self.assertEqual(data['summary']['event_urls'],239)
        self.assertEqual(data['summary']['records'],878)
        self.assertEqual(data['summary']['matches'],875)
        self.assertEqual(data['summary']['segments'],3)
        self.assertEqual(data['summary']['duplicates_removed'],3)
        self.assertEqual(data['rankings']['worst'][0]['rating'],36)
        self.assertTrue(all('Interview Segment' not in r['name'] for rows in data['rankings'].values() for r in rows))

    def test_real_archive_scope_and_independent_aggregates(self):
        import match_statistics as stats
        self.assertTrue(hasattr(stats, 'collect'), 'Missing canonical archive collection')
        import build
        import json
        import statistics
        data = stats.collect(build.VAULT, build.REPO / 'content/published-legacy.json')
        self.assertEqual(data['summary']['events'], 238)
        self.assertEqual(data['summary']['records'], 878)
        self.assertEqual(data['summary']['rated'], 866)
        self.assertEqual(data['summary']['timed'], 861)
        self.assertEqual(data['summary']['duration_status'], {'valid':861,'zero':7,'invalid':1,'missing':6})
        self.assertEqual(len({(r['event'],r['number']) for r in data['records']}), 878)
        matches = [r for r in data['records'] if r['kind']=='match']
        ratings = [r['rating'] for r in matches if r['rating'] is not None]
        seconds = [r['seconds'] for r in matches if r['seconds'] is not None]
        self.assertEqual(data['summary']['rating_mean'], sum(ratings)/len(ratings))
        self.assertEqual(data['summary']['duration_median'], statistics.median(seconds))
        for kind, field, reverse in [('top','rating',True),('worst','rating',False),('longest','seconds',True),('shortest','seconds',False)]:
            values = [r[field] for r in data['rankings'][kind]]
            self.assertEqual(len(values),25)
            self.assertEqual(values, sorted(values,reverse=reverse))
            self.assertTrue(all(x is not None for x in values))

class RenderingTests(unittest.TestCase):
    def test_four_accessible_statistics_routes_with_links_and_consistent_nav(self):
        import match_statistics as stats
        self.assertTrue(hasattr(stats, 'render'), 'Missing statistics presentation')
        import build
        from bs4 import BeautifulSoup
        data = stats.collect(build.VAULT, build.REPO / 'content/published-legacy.json')
        for kind in ['top','worst','longest','shortest']:
            soup = BeautifulSoup(build.html_page('Statistiken', stats.render(data,kind,build.PREFIX)), 'html.parser')
            self.assertEqual(soup.h1.text, 'Statistiken')
            self.assertEqual(soup.title.text, 'Statistiken | PWA')
            self.assertEqual(soup.select_one('.nav-links [aria-current]')['href'], '/pwa-website/rankings/top-25-matches/')
            self.assertEqual(soup.select_one('.nav-links [aria-current]').text, 'Statistiken')
            self.assertEqual(len(soup.select('.statistics-nav a')),4)
            self.assertEqual(len(soup.select('.statistics-nav [aria-current]')),1)
            self.assertEqual(len(soup.select('tbody tr')),25)
            self.assertEqual(len(soup.select('.table-scroll[tabindex="0"][role="region"]')),1)
            self.assertFalse(soup.select('a a'))
            self.assertIn('875', soup.get_text())
            self.assertIn('gesicherte veröffentlichte Archivstand', soup.get_text())
            self.assertIn('108:108', soup.get_text())
            for anchor in soup.select('main a[href]'):
                url=anchor['href']
                if url.endswith(('/longest-25-matches/','/shortest-25-matches/')):
                    continue  # New routes, generated during the build.
                if url.startswith(build.PREFIX):
                    target=build.DOCS/url.removeprefix(build.PREFIX+'/')
                    self.assertTrue(target.is_file() or (target/'index.html').is_file(),url)

class IntegrityTests(unittest.TestCase):
    def test_gate_allows_only_exact_statistics_change_and_rejects_tampering(self):
        import sys
        import copy
        import json
        import build
        sys.path.insert(0, str(build.REPO/'tools'))
        from verify_integrity import compare
        from content_audit import inventory
        import inspect
        self.assertIn('statistics', inspect.signature(compare).parameters, 'Missing narrow statistics gate')
        from statistics_gate import expectation
        from refresh_gate import expectation as refresh_expectation
        before = json.loads((build.REPO/'evidence/redesign/baseline-tracked.json').read_text())
        current = inventory(build.DOCS)
        allowed = expectation()
        refresh = refresh_expectation()
        self.assertEqual(compare(before,current,statistics=allowed,refresh=refresh), [])
        for section, route, field in [('pages','rankings/top-25-matches/index.html','text'),('pages','events/index.html','text')]:
            altered=copy.deepcopy(current)
            altered[section][route][field]+=' injected'
            self.assertTrue(compare(before,altered,statistics=allowed,refresh=refresh))
        altered=copy.deepcopy(current)
        altered['data']['statistics.json']['summary']['records']+=1
        self.assertTrue(compare(before,altered,statistics=allowed,refresh=refresh))

class DurationTests(unittest.TestCase):
    def test_duration_normalization_and_exclusion_reasons(self):
        self.assertIsNotNone(importlib.util.find_spec('match_statistics'), 'Missing maintained statistics module')
        from match_statistics import parse_duration
        for raw, expected in [('08:22',(502,'valid')), ('138:37',(8317,'valid')), ('1:02:03',(3723,'valid')), ('8 Min 2 Sec',(482,'valid')), ('', (None,'missing')), ('—',(None,'placeholder')), ('0:00',(None,'zero')), ('108:108',(None,'invalid')), ('1:60:00',(None,'invalid')), ('-1:00',(None,'invalid'))]:
            with self.subTest(raw=raw):
                self.assertEqual(parse_duration(raw), expected)
