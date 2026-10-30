"""One-time, reproducible source capture from the verified pre-refresh commit.

No working-tree docs are used. Published historical HTML is an explicit archival
source (as in published-legacy.json), not a claim that today's pipeline is valid.
"""
import hashlib
import json
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[1]
BASE = 'd6ed6944fe2816f8b4ae92ccdd8f6275ac3bc27d'

def capture():
    def read(path):
        return subprocess.check_output(['git', 'show', BASE + ':' + path], cwd=ROOT)
    files = subprocess.check_output(['git','ls-tree','-rz','--name-only',BASE,'docs'], cwd=ROOT).decode().split('\0')
    pages, data, assets = {}, {}, {}
    for path in filter(None, files):
        route = path.removeprefix('docs/')
        if path.endswith('.html'):
            pages[route] = read(path).decode()
        elif route in ['events.json','wrestlers.json','championships.json']:
            data[route] = json.loads(read(path))
        elif route.startswith(('img/','video/')):
            assets[route] = hashlib.sha256(read(path)).hexdigest()
    return dict(base_sha=BASE, pages=pages, data=data, assets=assets,
                statistics=json.loads(read('docs/statistics.json')),
                policy='Hendrik approved scoped Landfall release; preserve every previously published historical value. Quarantine conflicting 1982 imports upstream; do not infer aliases or opponents.')

if __name__ == '__main__':
    target = ROOT/'content/published-tna295.json'
    if target.exists():
        raise SystemExit('Refusing to replace frozen published source')
    target.write_text(json.dumps(capture(), ensure_ascii=False, indent=2) + '\n')
    print(target, target.stat().st_size)
