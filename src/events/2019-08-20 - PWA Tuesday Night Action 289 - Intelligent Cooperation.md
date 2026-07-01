---
layout: event.njk
title: PWA Tuesday Night Action 289 - Intelligent Cooperation
date: '2019-08-20'
venue: PWA Capcom Arena
location: Boston, Massachusetts, USA
promotion: PWA
permalink: /events/2019-08-20 - PWA Tuesday Night Action 289 - Intelligent Cooperation/
tags:
- events
matches_json: [{"number": 1, "name": "Jun Akiyama vs. UK Kid", "finish": "UK Kid beat Jun Akiyama in 20 Min 19 Sec with a Super Diving Headbutt", "rating_stars": "<span class=\"stars\">★★★½</span>", "rating_num": 3.5, "time": "20:19"}, {"number": 2, "name": "Tri Clops, Keith Rowans, Jean Wilson & Ricklon Smasher vs. Brutes", "finish": "Jean Wilson beat Casper Winkel in 25 Min 13 Sec with a DQ", "rating_stars": "<span class=\"stars\">★★★</span>", "rating_num": 3, "time": "25:13"}, {"number": 3, "name": "Theobold Lovecraft vs. Mr. Suplex", "finish": "Mr. Suplex beat Theobold Lovecraft in 10 Min 41 Sec with a Genki Raiga-plex", "rating_stars": "<span class=\"stars\">★★½</span>", "rating_num": 2.5, "time": "10:41"}, {"number": 4, "name": "Rick Banner (w/Fred Balentine) vs. Ox Hemlock (w/Tundra Wurm)", "finish": "Ox Hemlock beat Rick Banner in 25 Min 41 Sec with a Reverse Viper Hold", "rating_stars": "<span class=\"stars\">★★★★½</span>", "rating_num": 4.5, "time": "25:41"}]
---

# PWA Tuesday Night Action 289 - Intelligent Cooperation

<div class="event-header">
<div class="event-meta">
**Date:** 2019-08-20<br>
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