---
layout: event.njk
title: PWA Power Hour 25
date: '2019-07-31'
venue: PWA Power Studio
location: Boston, Massachusetts, USA
promotion: PWA
permalink: /events/2019-07-31 - PWA Power Hour 25/
tags:
- events
matches_json: [{"number": 1, "name": "Masked Maniac IV & Spitfire vs. Mysterious Fantasticos", "finish": "Mystery Panther beat Spitfire in 15 Min 48 Sec with a La Magistral", "rating_stars": "<span class=\"stars\">★★★★½</span>", "rating_num": 4.5, "time": "15:48"}, {"number": 2, "name": "Seth Ramsey vs. Felix Santana III", "finish": "Felix Santana III beat Seth Ramsey in 12 Min 37 Sec with an Uproot German Suplex", "rating_stars": "<span class=\"stars\">★★★★¼</span>", "rating_num": 4.25, "time": "12:37"}, {"number": 3, "name": "Jr. Heavyweight Title #1 Contender Battle Royal", "finish": "Fantasio Fantastico won a 8 wrestler battle royale in  12:49", "rating_stars": "<span class=\"stars\">★★★</span>", "rating_num": 3, "time": ""}]
---

# PWA Power Hour 25

<div class="event-header">
<div class="event-meta">
**Date:** 2019-07-31<br>
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