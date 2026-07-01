---
layout: event.njk
title: PWA Power Hour 1
date: '2019-01-31'
venue: PWA Power Studios
location: Boston, Massachusetts, USA
promotion: PWA
permalink: /events/2019-01-31 - PWA Power Hour 1/
tags:
- events
matches_json: [{"number": 1, "name": "Mackenzie Bergeron vs. Nigel Pendragon", "finish": "Mackenzie Bergeron battled Nigel Pendragon to a  time limit draw", "rating_stars": "<span class=\"stars\">★★★½</span>", "rating_num": 3.5, "time": ""}, {"number": 2, "name": "Masked Maniac IV & Todd Jackson vs. Jean Wilson & Ricklon Smasher", "finish": "Ricklon Smasher beat Todd Jackson in 6 Min 48 Sec with a Spear", "rating_stars": "<span class=\"stars\">★★½</span>", "rating_num": 2.5, "time": "6:48"}, {"number": 3, "name": "Ray Stantz vs. Timothy Thatcher", "finish": "Timothy Thatcher beat Ray Stantz in 1R 4 Min 40 Sec with a K.O", "rating_stars": "<span class=\"stars\">★★★½</span>", "rating_num": 3.5, "time": "4:40"}]
---

# PWA Power Hour 1

<div class="event-header">
<div class="event-meta">
**Date:** 2019-01-31<br>
**Venue:** PWA Power Studios<br>
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