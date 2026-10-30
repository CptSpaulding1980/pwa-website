"""Exact additive Landfall expectation, never a replacement archive baseline."""
from pathlib import Path
import sys
import tempfile
from unittest.mock import patch
sys.path.insert(0,str(Path(__file__).resolve().parent))
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
import build
from scoped_refresh import render, SLUG, snapshot
from content_audit import inventory


def expectation():
    with tempfile.TemporaryDirectory(prefix='pwa-refresh-') as tmp:
        root = Path(tmp)
        # Media are independently hash-protected; no arbitrary new media source.
        (root/'img').symlink_to(build.DOCS/'img',target_is_directory=True)
        (root/'video').symlink_to(build.DOCS/'video',target_is_directory=True)
        with patch.object(build,'DOCS',root):
            render(root)
        captured = inventory(root)
        routes = ['index.html','events/index.html','events/'+SLUG+'/index.html']
        return dict(slug=SLUG, data=captured['data']['events.json'],
                    videos={route:digest for route,digest in snapshot()['assets'].items() if route.startswith('video/')},
                    pages={route:captured['pages'][route] for route in routes})
