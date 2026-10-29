"""Exact statistics exception to the original archive-preservation gate.

Not a new baseline: original event/profile/title tables, matches, media and
records remain protected. Only four enumerated statistics routes and the new
statistics.json are compared to a fresh source-derived rendering.
"""
from pathlib import Path
import sys
import tempfile
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import build
from match_statistics import collect, render, ROUTES
from content_audit import inventory


def expectation():
    data = collect(build.VAULT, build.REPO / 'content/published-legacy.json')
    with tempfile.TemporaryDirectory(prefix='pwa-statistics-') as tmp:
        root = Path(tmp)
        for kind, (_, slug) in ROUTES.items():
            path = root / 'rankings' / slug / 'index.html'
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(build.html_page('Statistiken', render(data, kind, build.PREFIX)))
        pages = inventory(root)['pages']
    return {'pages': pages, 'data': data}
