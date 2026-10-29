"""Independent numerical cross-check: regex source tails, not generator helpers."""
import json
import re
from collections import Counter
from pathlib import Path
from statistics import median
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[1]
VAULT = Path('/Volumes/SSD_4TB/nextcloud/app/data/hendrik/files/Obsidian/PWA')
ALIAS = '2019-09-24 - Tuesday Night Action 294 - The Ox Celebration.md'


def main():
    published = json.loads((ROOT/'docs/statistics.json').read_text())
    source = {}
    for path in sorted((VAULT/'Events').glob('*.md')):
        text = path.read_text().split('## Matches',1)[1].split('\n## ',1)[0]
        for row in re.split(r'(?m)(?=^\|\s*\d+\s*\|)',text)[1:]:
            number = int(re.match(r'^\|\s*(\d+)',row)[1])
            tail = re.search(r'\|\s*(\d+:\d+(?::\d+)?)\s*\|\s*(\d+(?:\.\d+)?)\s*\|\s*([^|\n]*)\|\s*$',row,re.M)
            assert tail, (path.name,number)
            parts = list(map(int,tail[1].split(':')))
            invalid = parts[-1] > 59 or (len(parts)==3 and parts[1]>59)
            seconds = sum(n * 60**i for i,n in enumerate(reversed(parts)))
            status = 'invalid' if invalid else 'zero' if seconds==0 else 'valid'
            source[('Events/'+path.name,number)] = (float(tail[2]),seconds if status=='valid' else None,status)
    assert len(source)==869
    checked = 0
    for row in published['records'] + published['excluded_alias_records']:
        key=(row['source'],row['number'])
        if key in source:
            assert (row['rating'],row['seconds'],row['duration_status'])==source[key],key
            checked+=1
    assert checked==869
    rows = [r for r in published['records'] if r['kind']=='match']
    rates = sorted(r['rating'] for r in rows if r['rating'] is not None)
    durations = sorted(r['seconds'] for r in rows if r['seconds'] is not None)
    s = published['summary']
    assert len(rows)==s['matches']==872
    assert len(rates)==s['rated']==863
    assert len(durations)==s['timed']==858
    assert sum(rates)/len(rates)==s['rating_mean']
    assert median(rates)==s['rating_median']
    assert sum(durations)/len(durations)==s['duration_mean']
    assert median(durations)==s['duration_median']
    comparisons = []
    for kind,field,direction in [('top','rating',-1),('worst','rating',1),('longest','seconds',-1),('shortest','seconds',1)]:
        expected=sorted([r for r in rows if r[field] is not None],key=lambda r:(direction*r[field],r['date'],r['event'],r['number']))[:25]
        assert expected==published['rankings'][kind]
        path=ROOT/'docs/rankings'/f'{kind}-25-matches/index.html'
        soup=BeautifulSoup(path.read_text(),'html.parser')
        actual=[(r['data-event'],int(r['data-match'])) for r in soup.select('tbody tr')]
        assert actual==[(r['event'],r['number']) for r in expected]
        assert len(soup.select('thead th'))==7
        assert all(len(tr.select('td'))==7 for tr in soup.select('tbody tr'))
        comparisons.append({'kind':kind,'rows':len(actual),'first':expected[0],'last':expected[-1]})
    before=json.loads((ROOT/'evidence/statistics/before/inventory.json').read_text())
    after=json.loads((ROOT/'evidence/statistics/after/inventory.json').read_text())
    assert before['assets']==after['assets']
    for key,value in before['data'].items():
        assert after['data'][key]==value
    unchanged=0
    for route,page in before['pages'].items():
        if route in ['index.html','rankings/top-25-matches/index.html','rankings/worst-25-matches/index.html']:
            continue
        assert page==after['pages'][route],route
        unchanged+=1
    vault_before=json.loads((ROOT/'evidence/statistics/before/vault.json').read_text())
    vault_after=json.loads((ROOT/'evidence/statistics/after/vault.json').read_text())
    assert vault_before==vault_after
    result={'numeric_and_time_source_rows_verified':checked,'summary':s,'rating_sum':sum(rates),'duration_sum_seconds':sum(durations),
            'ranking_checks':comparisons,'unchanged_main_page_inventories':unchanged,'unchanged_assets':len(before['assets']),
            'unchanged_vault_files':len(vault_before),'all_original_urls_preserved':set(before['pages']).issubset(after['pages']),
            'new_urls':sorted(set(after['pages'])-set(before['pages'])),'errors':[]}
    out=ROOT/'evidence/statistics/independent-audit.json'
    out.write_text(json.dumps(result,ensure_ascii=False,indent=2))
    print(json.dumps({k:v for k,v in result.items() if k!='ranking_checks'},ensure_ascii=False,indent=2))

if __name__=='__main__':
    main()
