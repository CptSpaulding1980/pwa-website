"""Independent scoped-release audit: Git baseline + raw numeric note tails.

Do NOT compare this limited release to contaminated regenerated historical notes.
The previously published numerical population is frozen, and all three approved
incremental rows are checked independently of the build extractor.
"""
import hashlib
import json
import re
import subprocess
from collections import Counter
from pathlib import Path
from statistics import median
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[1]
VAULT = Path('/Volumes/SSD_4TB/nextcloud/app/data/hendrik/files/Obsidian/PWA')
BASE = 'd6ed6944fe2816f8b4ae92ccdd8f6275ac3bc27d'
SLUG = '2019-10-08-pwa-tuesday-night-action-296-landfall'
NOTE = '2019-10-08 - PWA Tuesday Night Action 296 - Landfall.md'

def main():
    def original(path):
        return subprocess.check_output(['git','show',BASE+':docs/'+path],cwd=ROOT)
    published = json.loads((ROOT/'docs/statistics.json').read_text())
    before = json.loads(original('statistics.json'))
    old = {(r['event'],r['number']):r for r in before['records']}
    new = {(r['event'],r['number']):r for r in published['records']}
    assert len(new)==len(published['records'])==878
    assert {k:new[k] for k in old} == old
    additions = [r for k,r in new.items() if k not in old]
    assert len(additions)==3 and {r['event'] for r in additions}=={SLUG}
    text = (VAULT/'Events'/NOTE).read_text().split('## Matches',1)[1]
    tails = re.findall(r'^\|\s*(\d+)\s*\|.*?\|\s*(\d+):(\d{2})\s*\|\s*(\d+)\s*\|\s*([^|\n]*)\|\s*$',text,re.M)
    source = {int(n):(int(rating),int(minutes)*60+int(seconds),stars.strip()) for n,minutes,seconds,rating,stars in tails}
    assert source=={1:(78,1200,'★★★½'),2:(81,829,'★★★¾'),3:(83,1220,'★★★¾')}
    for row in additions:
        assert (row['rating'],row['seconds'],row['stars'])==source[row['number']]
    assert published['event_aliases']==before['event_aliases']
    assert published['excluded_alias_records']==before['excluded_alias_records']
    rows = [r for r in published['records'] if r['kind']=='match']
    rates = sorted(r['rating'] for r in rows if r['rating'] is not None)
    durations = sorted(r['seconds'] for r in rows if r['seconds'] is not None)
    s = published['summary']
    assert len(rows)==s['matches']==875
    assert len(rates)==s['rated']==866
    assert len(durations)==s['timed']==861
    assert sum(rates)/len(rates)==s['rating_mean']
    assert median(rates)==s['rating_median']
    assert sum(durations)/len(durations)==s['duration_mean']
    assert median(durations)==s['duration_median']
    assert dict(Counter(r['duration_status'] for r in rows))==s['duration_status']
    comparisons = []
    for kind,field,direction in [('top','rating',-1),('worst','rating',1),('longest','seconds',-1),('shortest','seconds',1)]:
        expected=sorted([r for r in rows if r[field] is not None],key=lambda r:(direction*r[field],r['date'],r['event'],r['number']))[:25]
        assert expected==published['rankings'][kind]
        soup=BeautifulSoup((ROOT/'docs/rankings'/f'{kind}-25-matches/index.html').read_text(),'html.parser')
        actual=[(r['data-event'],int(r['data-match'])) for r in soup.select('tbody tr')]
        assert actual==[(r['event'],r['number']) for r in expected]
        assert len(soup.select('thead th'))==7
        assert all(len(tr.select('td'))==7 for tr in soup.select('tbody tr'))
        comparisons.append({'kind':kind,'rows':len(actual)})
    events=json.loads((ROOT/'docs/events.json').read_text())
    baseline_events=json.loads(original('events.json'))
    assert [e for e in events if e['slug']!=SLUG]==baseline_events
    assert len(events)==239 and events[0]['slug']==SLUG
    # All old detail pages and PWI/title/profile values remain byte-identical.
    protected = subprocess.check_output(['git','ls-tree','-r','--name-only',BASE,'docs/events','docs/wrestlers','docs/championships','docs/rankings/pwi-500'],cwd=ROOT,text=True).splitlines()
    checked=[]
    for path in protected:
        if not path.endswith('.html') or path in ['docs/events/index.html','docs/wrestlers/index.html','docs/championships/index.html']:
            continue
        assert (ROOT/path).read_bytes()==original(path.removeprefix('docs/')),path
        checked.append(path)
    result={'base_sha':BASE,'historical_records_identical':len(old),'new_matches_verified':len(additions),
            'summary':s,'rating_sum':sum(rates),'duration_sum_seconds':sum(durations),
            'ranking_checks':comparisons,'byte_identical_historical_pages':len(checked),
            'events_preserved':len(baseline_events),'event_urls':len(events),'errors':[]}
    out=ROOT/'evidence/tna296/independent-statistics.json'
    out.write_text(json.dumps(result,ensure_ascii=False,indent=2))
    print(json.dumps(result,ensure_ascii=False,indent=2))

if __name__=='__main__':
    main()
