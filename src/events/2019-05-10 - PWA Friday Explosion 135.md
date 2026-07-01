---
layout: event.njk
title: PWA Friday Explosion 135
date: '2019-05-10'
venue: PWA Capcom Arena
location: Boston, Massachusetts, USA
promotion: PWA
permalink: /events/2019-05-10 - PWA Friday Explosion 135/
tags:
- events
matches_json: [{"number": 1, "name": "KotR Qualifying: Mr. Suplex vs. Keith Rowans", "finish": "Mr. Suplex beat Keith Rowans in 14 Min 35 Sec with a Genki Raiga-plex", "rating_stars": "<span class=\"stars\">★★★★½</span>", "rating_num": 4.5, "time": "14:35"}, {"number": 2, "name": "KotR Qualifying: Red Dragon vs. Misterio Guerrero", "finish": "Red Dragon beat Misterio Guerrero in 9 Min 24 Sec with a RING OUT", "rating_stars": "<span class=\"stars\">★★</span>", "rating_num": 2, "time": "9:24"}, {"number": 3, "name": "KotR Qualifying: Casper Winkel vs. Ricklon Smasher", "finish": "Ricklon Smasher beat Casper Winkel in 9 Min 49 Sec with a Spear", "rating_stars": "<span class=\"stars\">★</span>", "rating_num": 1, "time": "9:49"}, {"number": 4, "name": "KotR Qualifying: Allen Hawkins vs. Salvador Sosa", "finish": "Allen Hawkins battled Salvador Sosa to a  time limit draw", "rating_stars": "<span class=\"stars\">★★★★</span>", "rating_num": 4, "time": ""}, {"number": 5, "name": "Steel Cage Match - PWA World Tag Team Championship: Brutes vs. Masked Lucha Alliance (c)", "finish": "Cobra III beat Mike Hool in 13 Min 56 Sec with a Bat-Hanging Lock", "rating_stars": "<span class=\"stars\">★★½</span>", "rating_num": 2.5, "time": "13:56"}]
---

# PWA Friday Explosion 135

<div class="event-header">
<div class="event-meta">
**Date:** 2019-05-10<br>
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