"""Capture read-only source and publication evidence before/after a statistics release."""
import hashlib
import json
import sys
import tarfile
from pathlib import Path
from content_audit import inventory

ROOT = Path(__file__).resolve().parents[1]
VAULT = Path('/Volumes/SSD_4TB/nextcloud/app/data/hendrik/files/Obsidian/PWA')

def capture(label):
    out = ROOT / 'evidence/statistics' / label
    out.mkdir(parents=True, exist_ok=True)
    data = inventory(ROOT / 'docs')
    (out / 'inventory.json').write_text(json.dumps(data, ensure_ascii=False, indent=2))
    hashes = {str(p.relative_to(VAULT)): hashlib.sha256(p.read_bytes()).hexdigest()
              for p in sorted(VAULT.rglob('*')) if p.is_file()}
    (out / 'vault.json').write_text(json.dumps(hashes, indent=2))
    if label == 'before':
        with tarfile.open(out / 'rollback.tar.gz', 'w:gz') as archive:
            for name in ['build.py', 'presentation.py', 'magazine.py', 'assets', 'content', 'docs', 'tests', 'tools']:
                archive.add(ROOT / name, arcname=name)
    print(json.dumps({'label': label, 'pages': len(data['pages']), 'media': len(data['assets']),
                      'vault_files': len(hashes), 'data': {k: len(v) for k, v in data['data'].items()}}))

if __name__ == '__main__':
    capture(sys.argv[1])
