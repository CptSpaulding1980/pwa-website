---
layout: event.njk
title: PWA Power Hour 16
date: '2019-05-23'
venue: PWA Power Studio
location: Boston, Massachusetts, USA
promotion: PWA
permalink: /events/2019-05-23 - PWA Power Hour 16/
tags:
- events
matches_json: [{"number": 1, "name": "Dynamite Smith vs. Nigel Pendragon", "finish": "Dynamite Smith battled Nigel Pendragon to a  time limit draw", "rating_stars": "<span class=\"stars\">★</span>", "rating_num": 1, "time": ""}, {"number": 2, "name": "Ray Stantz vs. Julio Rivera", "finish": "Ray Stantz battled Julio Rivera to a  time limit draw", "rating_stars": "<span class=\"stars\">★★</span>", "rating_num": 2, "time": ""}, {"number": 3, "name": "Foreign Fanatics vs. Masked Maniac IV, Jack Gold & Spitfire", "finish": "Hiroto Nakamichi beat Spitfire in 18 Min 50 Sec with a School Boy", "rating_stars": "<span class=\"stars\">★★½</span>", "rating_num": 2.5, "time": "18:50"}]
---

# PWA Power Hour 16

<div class="event-header">
<div class="event-meta">
**Date:** 2019-05-23<br>
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