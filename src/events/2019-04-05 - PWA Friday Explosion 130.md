---
layout: event.njk
title: PWA Friday Explosion 130
date: '2019-04-05'
venue: PWA Capcom Arena
location: Boston, Massachusetts, USA
promotion: PWA
permalink: /events/2019-04-05 - PWA Friday Explosion 130/
tags:
- events
matches_json: [{"number": 1, "name": "Spitfire vs. Jack Gold", "finish": "Spitfire battled Jack Gold to a  time limit draw", "rating_stars": "<span class=\"stars\">★★★★¼</span>", "rating_num": 4.25, "time": ""}, {"number": 2, "name": "Allen Hawkins vs. Saburo Aoki Jr.", "finish": "Allen Hawkins battled Saburo Aoki Jr. to a  time limit draw", "rating_stars": "<span class=\"stars\">★★★¾</span>", "rating_num": 3.75, "time": ""}, {"number": 3, "name": "A. Alexander Heavyweight Exhibition Match: Avery Alexander vs. Blue Spider", "finish": "Avery Alexander beat Blue Spider in 13 Min 38 Sec with a Most Muscular", "rating_stars": "<span class=\"stars\">★★★★</span>", "rating_num": 4, "time": "13:38"}, {"number": 4, "name": "Fabrizio Tiziano & Montgomery Hayes vs. El Canek & Grizzlor ", "finish": "Fabrizio Tiziano beat Grizzlor  in 25 Min 24 Sec with a Just Face Lock", "rating_stars": "<span class=\"stars\">★★★★½</span>", "rating_num": 4.5, "time": "25:24"}, {"number": 5, "name": "Steel Cage Match: Diablo Blanco vs. Blue Demon Jr.", "finish": "Diablo Blanco beat Blue Demon Jr. in 17 Min 14 Sec with a Vertical Drop DDT", "rating_stars": "<span class=\"stars\">★★★★½</span>", "rating_num": 4.5, "time": "17:14"}]
---

# PWA Friday Explosion 130

<div class="event-header">
<div class="event-meta">
**Date:** 2019-04-05<br>
**Venue:** PWA Capcom Arena<br>
**Location:** Boston, Massachusetts, USA
</div>

</div>

## Matches

{% for match in matches_json %}
<div class="match-card">
<span class="match-number">#{{ match.number }}</span>
<div class="match-details">
<div class="match-name">{{ match.name | safe }}</div>
<div class="match-finish">{{ match.finish | safe }}</div>
<div class="match-meta">
<span class="match-time">{{ match.time }}</span>
<span class="match-rating">{{ match.rating_stars | safe }}</span>
</div>
</div>
</div>
{% endfor %}