---
layout: event.njk
title: PWA Power Hour 30
date: '2019-09-05'
venue: PWA Capcom Arena
location: Boston, Massachusetts, USA
promotion: PWA
permalink: /events/2019-09-05 - PWA Power Hour 30/
tags:
- events
matches_json: [{"number": 1, "name": "Yuji Ishikawa vs. Neptune Tritano", "finish": "Neptune Tritano beat Yuji Ishikawa in 18 Min 4 Sec with a Diving Body Press", "rating_stars": "<span class=\"stars\">★★★¾</span>", "rating_num": 3.75, "time": "18:04"}, {"number": 2, "name": "Mackenzie Bergeron vs. Dynamite Smith", "finish": "Mackenzie Bergeron beat Dynamite Smith in 6 Min 0 Sec with a Heel Hold", "rating_stars": "<span class=\"stars\">★★★</span>", "rating_num": 3, "time": "6:00"}, {"number": 3, "name": "Trevor Lee vs. Tri Clops", "finish": "Tri Clops beat Trevor Lee in 7 Min 43 Sec with a Neck Throw Pin", "rating_stars": "<span class=\"stars\">★½</span>", "rating_num": 1.5, "time": "7:43"}]
---

# PWA Power Hour 30

<div class="event-header">
<div class="event-meta">
**Date:** 2019-09-05<br>
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