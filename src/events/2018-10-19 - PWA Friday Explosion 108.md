---
layout: event.njk
title: PWA Friday Explosion 108
date: '2018-10-19'
venue: Trenton, New Jersey
location: ''
promotion: PWA
permalink: /events/2018-10-19 - PWA Friday Explosion 108/
tags:
- events
matches_json: [{"number": 1, "name": "Ray Stantz vs. Felix Santana Jr.", "finish": "Ray Stantz beat Felix Santana Jr. in 5 Min 54 Sec with an Orange Crush", "rating_stars": "<span class=\"stars\">★</span>", "rating_num": 1, "time": "5:54"}, {"number": 2, "name": "Brutes vs. Casper Winkel & Rick Banner", "finish": "Casper Winkel beat Victor Kurilenko in 15 Min 46 Sec with a Buffalo Sleeper", "rating_stars": "<span class=\"stars\">★★</span>", "rating_num": 2, "time": "15:46"}, {"number": 3, "name": "Seth Ramsey vs. Avery Alexander", "finish": "Avery Alexander beat Seth Ramsey in 8 Min 10 Sec with a Diving Body Press", "rating_stars": "<span class=\"stars\">★★</span>", "rating_num": 2, "time": "8:10"}, {"number": 4, "name": "PWA World Heavyweight Championship: PAC vs. Fabrizio Tiziano (c)", "finish": "Fabrizio Tiziano beat PAC in 7 Min 40 Sec with a Rollup Pin", "rating_stars": "<span class=\"stars\">DUD</span>", "rating_num": 0, "time": "7:40"}]
---

# PWA Friday Explosion 108

<div class="event-header">
<div class="event-meta">
**Date:** 2018-10-19<br>
**Venue:** Trenton, New Jersey<br>
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