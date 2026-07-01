---
layout: event.njk
title: PWA Power Hour 6
date: '2019-03-05'
venue: PWA Capcom Arena
location: Boston, Massachusetts, USA
promotion: PWA
permalink: /events/2019-03-05 - PWA Power Hour 6/
tags:
- events
matches_json: [{"number": 1, "name": "Golden Grappler vs. Salvador Sosa", "finish": "Golden Grappler battled Salvador Sosa to a  time limit draw", "rating_stars": "<span class=\"stars\">★★★★★</span>", "rating_num": 5, "time": ""}, {"number": 2, "name": "Ricky Starks vs. Dynamite Smith", "finish": "Dynamite Smith beat Ricky Starks in 12 Min 50 Sec with a Victory Roll Pinfall", "rating_stars": "<span class=\"stars\">★★★★★</span>", "rating_num": 5, "time": "12:50"}, {"number": 3, "name": "Mike Hool (w/Brutes) vs. Cobra III (w/Masked Lucha Alliance)", "finish": "Mike Hool beat Cobra III in 7 Min 39 Sec with a King Kong Knee Drop", "rating_stars": "<span class=\"stars\">★★★¼</span>", "rating_num": 3.25, "time": "7:39"}, {"number": 4, "name": "Allen Hawkins vs. Jean Wilson", "finish": "Allen Hawkins beat Jean Wilson in 11 Min 13 Sec with a Body Choke Sleeper", "rating_stars": "<span class=\"stars\">★★★★¾</span>", "rating_num": 4.75, "time": "11:13"}]
---

# PWA Power Hour 6

<div class="event-header">
<div class="event-meta">
**Date:** 2019-03-05<br>
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