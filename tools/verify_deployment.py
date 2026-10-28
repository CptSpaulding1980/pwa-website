"""Verify exact-SHA Pages deployment and read back real public output.

Uses the existing Git credential helper for GitHub API calls only. Never prints
or stores credentials, and never forwards them to the public Pages host.
"""
import concurrent.futures
import hashlib
import json
from pathlib import Path
import subprocess
import time
from urllib.parse import quote
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
API = 'https://api.github.com/repos/CptSpaulding1980/pwa-website'
LIVE = 'https://cptspaulding1980.github.io/pwa-website/'


def main():
    sha = subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=ROOT, text=True).strip()
    raw = subprocess.run(['git','credential','fill'],input='protocol=https\nhost=github.com\n\n', text=True, capture_output=True, check=True)
    credentials = dict(line.split('=',1) for line in raw.stdout.splitlines() if '=' in line)
    headers = {'Accept':'application/vnd.github+json','User-Agent':'PWA-deployment-verification'}
    if credentials.get('password'):
        headers['Authorization'] = 'Bearer ' + credentials['password']
    def api(path):
        with urlopen(Request(API + path, headers=headers),timeout=30) as response:
            return json.load(response)
    pages = api('/pages')
    assert pages['source'] == {'branch':'main','path':'/docs'}, pages['source']
    selected = None
    for attempt in range(90):
        runs = api('/actions/runs?head_sha=' + sha + '&per_page=30')['workflow_runs']
        exact = [run for run in runs if run['head_sha'] == sha and run['name'] == 'pages-build-deployment']
        if exact:
            selected = max(exact, key=lambda run: run['id'])
            print('Pages',selected['id'],selected['status'],selected['conclusion'],flush=True)
            if selected['status'] == 'completed':
                assert selected['conclusion'] == 'success', selected['html_url']
                break
        else:
            print('Waiting for exact-SHA Pages run',sha,flush=True)
        time.sleep(10)
    else:
        raise RuntimeError('Exact-SHA Pages run not successful within 15 minutes')
    paths = set((ROOT / 'docs').glob('*.json'))
    paths.update((ROOT / 'docs').rglob('*.html'))
    paths.add(ROOT / 'docs/styles/main.css')
    paths.update(ROOT / 'docs' / name for name in [
        'img/PWA_2019-ff.png', 'img/Banner_PWA_YouTube.png',
        'img/wrestler/Ox_Hemlock.PNG', 'img/charts/ox-hemlock_donut.png',
        'img/posters/2019-09-21 - PWA Team Wars 2019.png'])
    paths.update((ROOT / 'docs/img/championships').glob('*'))
    def check(path):
        relative = path.relative_to(ROOT / 'docs').as_posix()
        expected = hashlib.sha256(path.read_bytes()).hexdigest()
        url = LIVE + quote(relative, safe='/')
        failure = ''
        for attempt in range(8):
            try:
                # Verify the canonical URL, not just a private cache-busting preview.
                with urlopen(Request(url, headers={'Cache-Control':'no-cache','User-Agent':'PWA-live-byte-audit'}),timeout=40) as response:
                    content = response.read()
                    digest = hashlib.sha256(content).hexdigest()
                    if digest == expected:
                        return {'path':relative,'url':url,'bytes':len(content),'sha256':digest,'match':True,'status':response.status}
                    failure = 'content hash mismatch'
            except Exception as error:
                failure = str(error)
            time.sleep(10)
        return {'path':relative,'url':url,'match':False,'error':failure,'expected_sha256':expected}
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as pool:
        files = list(pool.map(check, sorted(paths)))
    result = {'sha':sha,'pages_source':pages['source'], 'workflow':{key:selected[key] for key in ['id','head_sha','status','conclusion','html_url']}, 'files_verified':len(files),'errors':[row for row in files if not row['match']],'files':files}
    destination=ROOT / 'evidence/redesign/deployment.json'
    destination.write_text(json.dumps(result,ensure_ascii=False,indent=2))
    print(json.dumps({key:value for key,value in result.items() if key != 'files'}, ensure_ascii=False))
    assert not result['errors']

if __name__ == '__main__':
    main()
