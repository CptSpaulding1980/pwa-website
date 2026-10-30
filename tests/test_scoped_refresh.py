"""The approved Landfall release must not publish the unrelated pipeline drift."""
import copy
import json
from pathlib import Path
import unittest
import build

class ScopedRefreshTests(unittest.TestCase):
    def test_refresh_gate_accepts_only_exact_source_derived_delta(self):
        from tools.refresh_gate import expectation
        from tools.verify_integrity import compare
        from tools.content_audit import inventory
        from tools.statistics_gate import expectation as statistics_expectation
        baseline = json.loads((build.REPO/'evidence/redesign/baseline-tracked.json').read_text())
        current = inventory(build.DOCS)
        allowed = expectation()
        stats = statistics_expectation()
        self.assertEqual(compare(baseline,current,statistics=stats,refresh=allowed),[])
        for route, field in [('events/'+allowed['slug']+'/index.html','text'),('events/index.html','links'),('index.html','text'),('championships/pwa-world-heavyweight-championship/index.html','text')]:
            altered = copy.deepcopy(current)
            altered['pages'][route][field] += ['injected'] if field=='links' else ' injected'
            self.assertTrue(compare(baseline,altered,statistics=stats,refresh=allowed),route)
        altered = copy.deepcopy(current)
        altered['data']['events.json'][0]['match_count'] += 1
        self.assertTrue(compare(baseline,altered,statistics=stats,refresh=allowed))
        altered = copy.deepcopy(current)
        altered['assets'][next(iter(altered['assets']))] = 'changed'
        self.assertTrue(compare(baseline,altered,statistics=stats,refresh=allowed))
        altered = copy.deepcopy(current)
        altered['videos'] = {'video/pwa-homepage.mp4':'tampered'}
        self.assertTrue(compare(baseline,altered,statistics=stats,refresh=allowed))
        altered = copy.deepcopy(current)
        altered['pages']['events/1982-unvalidated/index.html'] = current['pages']['index.html']
        self.assertTrue(compare(baseline,altered,statistics=stats,refresh=allowed))

    def test_published_population_plus_only_three_verified_landfall_matches(self):
        from scoped_refresh import statistics, snapshot
        before = snapshot()['statistics']
        after = statistics()
        old = {(r['event'], r['number']): r for r in before['records']}
        current = {(r['event'], r['number']): r for r in after['records']}
        self.assertEqual({k: current[k] for k in old}, old)
        added = [r for k, r in current.items() if k not in old]
        self.assertEqual([(r['rating'], r['seconds']) for r in added], [(78,1200),(81,829),(83,1220)])
        self.assertEqual(after['summary']['matches'], 875)
        self.assertEqual(after['summary']['events'], 238)
        self.assertEqual(after['summary']['event_urls'], 239)
        self.assertEqual(after['summary']['segments'], 3)
        self.assertEqual(after['event_aliases'], before['event_aliases'])

    def test_snapshot_is_exact_published_source_not_dirty_generated_output(self):
        import hashlib
        import subprocess
        from scoped_refresh import snapshot
        frozen = snapshot()
        self.assertEqual(frozen['base_sha'], 'd6ed6944fe2816f8b4ae92ccdd8f6275ac3bc27d')
        for route, source in frozen['pages'].items():
            original = subprocess.check_output(['git','show',f"{frozen['base_sha']}:docs/{route}"])
            self.assertEqual(source.encode(), original, route)
        self.assertEqual(len(frozen['data']['events.json']),238)
        self.assertEqual(len(frozen['data']['championships.json']),4)
        self.assertFalse(any(x['slug'].startswith('1982-') and '-pro-wrestling' in x['slug'] for x in frozen['data']['events.json']))

    def test_only_exact_approved_new_source_is_accepted(self):
        from scoped_refresh import validated_note
        text = validated_note()
        from unittest.mock import patch
        with patch.object(Path, 'read_text', return_value=text.replace('20:00', '19:00')):
            with self.assertRaisesRegex(ValueError, 'Landfall source changed'):
                validated_note()
