"""Read-only content inventory for the PWA redesign (test dependency: bs4)."""
import hashlib
import json
import re
import sys
from pathlib import Path
from bs4 import BeautifulSoup


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def inventory(root):
    pages = {}
    for path in sorted(root.rglob('*.html')):
        soup = BeautifulSoup(path.read_text(), 'html.parser')
        main = soup.find('main') or soup
        pages[str(path.relative_to(root))] = {
            'title': soup.title.get_text() if soup.title else '',
            'text': main.get_text(' ', strip=True),
            'tables': [[[' '.join(c.get_text(' ', strip=True).split()) for c in row.find_all(['th', 'td'])] for row in t.find_all('tr')] for t in main.find_all('table')],
            'matches': [x.get_text(' ', strip=True) for x in main.select('.match-card')],
            'links': sorted(a.get('href', '') for a in main.find_all('a')),
            'media': sorted(x.get('src', '') for x in main.find_all(['img', 'video', 'source', 'iframe'])),
        }
    return {'pages': pages, 'assets': {str(p.relative_to(root)): digest(p) for p in sorted((root / 'img').rglob('*')) if p.is_file()},
            'data': {p.name: json.loads(p.read_text()) for p in sorted(root.glob('*.json'))}}


if __name__ == '__main__':
    result = inventory(Path(sys.argv[1]))
    Path(sys.argv[2]).write_text(json.dumps(result, ensure_ascii=False, indent=2))
    print(json.dumps({'pages': len(result['pages']), 'assets': len(result['assets']), 'data': {k: len(v) for k, v in result['data'].items()}}))
