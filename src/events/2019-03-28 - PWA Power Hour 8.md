---
layout: event.njk
title: PWA Power Hour 8
date: '2019-03-28'
venue: PWA Capcom Arena
location: Boston, Massachusetts, USA
promotion: PWA
permalink: /events/2019-03-28 - PWA Power Hour 8/
tags:
- events
matches_json: [{"number": 1, "name": "Victor Kurilenko vs. Nigel Pendragon", "finish": "Victor Kurilenko beat Nigel Pendragon in 12 Min 20 Sec with a Body Choke Sleeper", "rating_stars": "<span class=\"stars\">★★★¼</span>", "rating_num": 3.25, "time": "12:20"}, {"number": 2, "name": "Julio Rivera vs. Mr. Suplex", "finish": "Julio Rivera battled Mr. Suplex to a  double countout", "rating_stars": "<span class=\"stars\">★★½</span>", "rating_num": 2.5, "time": ""}, {"number": 3, "name": "Blake Twins vs. Jean Wilson & Ricklon Smasher", "finish": "Jean Wilson beat Elias Blake in 17 Min 58 Sec with an Axe Bomber", "rating_stars": "<span class=\"stars\">★★★★¼</span>", "rating_num": 4.25, "time": "17:58"}]
---

# PWA Power Hour 8

<div class="event-header">
<div class="event-meta">
**Date:** 2019-03-28<br>
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