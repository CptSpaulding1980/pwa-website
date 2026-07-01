---
layout: event.njk
title: PWA Power Hour 10
date: '2019-04-11'
venue: PWA Power Studio
location: Boston, Massachusetts, USA
promotion: PWA
permalink: /events/2019-04-11 - PWA Power Hour 10/
tags:
- events
matches_json: [{"number": 1, "name": "Veteran Veteran Devastators vs. Jean Wilson & Ricklon Smasher", "finish": "Jean Wilson beat Mackenzie Bergeron in 15 Min 38 Sec with a RING OUT", "rating_stars": "<span class=\"stars\">★½</span>", "rating_num": 1.5, "time": "15:38"}, {"number": 2, "name": "Jack Fury vs. Julio Rivera", "finish": "Jack Fury beat Julio Rivera in 3 Min 33 Sec with a RING OUT", "rating_stars": "<span class=\"stars\">★</span>", "rating_num": 1, "time": "3:33"}, {"number": 3, "name": "No Holds Barred: Allen Hawkins vs. Saburo Aoki Jr.", "finish": "Allen Hawkins beat Saburo Aoki Jr. in 17 Min 36 Sec with a Punch", "rating_stars": "<span class=\"stars\">★★★★½</span>", "rating_num": 4.5, "time": "17:36"}]
---

# PWA Power Hour 10

<div class="event-header">
<div class="event-meta">
**Date:** 2019-04-11<br>
**Venue:** PWA Power Studio<br>
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