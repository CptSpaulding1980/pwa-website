---
layout: event.njk
title: PWA Friday Explosion 115
date: '2018-12-07'
venue: Pittsburgh, Pennsylvania
location: ''
promotion: PWA
permalink: /events/2018-12-07 - PWA Friday Explosion 115/
tags:
- events
matches_json: [{"number": 1, "name": "Saburo Aoki Jr. vs. Theobold Lovecraft", "finish": "Theobold Lovecraft beat Saburo Aoki Jr. in 11 Min 10 Sec with an Elbow Drop", "rating_stars": "<span class=\"stars\">★★★¾</span>", "rating_num": 3.75, "time": "11:10"}, {"number": 2, "name": "Veteran Veteran Devastators vs. Jean Wilson & Tri Clops", "finish": "Jean Wilson beat Blue Blazer Jr. in 19 Min 3 Sec with a Heavyweight Diving Body Press", "rating_stars": "<span class=\"stars\">★★★¾</span>", "rating_num": 3.75, "time": "19:03"}, {"number": 3, "name": "Mackenzie Bergeron vs. Cobra ", "finish": "Mackenzie Bergeron beat Cobra  in 2 Min 47 Sec with a Flying Cross Legbreaker", "rating_stars": "<span class=\"stars\">★½</span>", "rating_num": 1.5, "time": "2:47"}, {"number": 4, "name": "Non Title Match: Rey Fénix vs. UK Kid", "finish": "Rey Fénix beat UK Kid  in 11 Min 21 Sec with a Super Kick", "rating_stars": "<span class=\"stars\">★★★¾</span>", "rating_num": 3.75, "time": "11:21"}]
---

# PWA Friday Explosion 115

<div class="event-header">
<div class="event-meta">
**Date:** 2018-12-07<br>
**Venue:** Pittsburgh, Pennsylvania<br>
**Location:** 
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