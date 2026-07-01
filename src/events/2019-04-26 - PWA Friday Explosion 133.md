---
layout: event.njk
title: PWA Friday Explosion 133
date: '2019-04-26'
venue: PWA Capcom Arena
location: Boston, Massachusetts, USA
promotion: PWA
permalink: /events/2019-04-26 - PWA Friday Explosion 133/
tags:
- events
matches_json: [{"number": 1, "name": "Casper Winkel vs. Masked Maniac IV", "finish": "Casper Winkel beat Masked Maniac IV in 11 Min 15 Sec with a Buffalo Sleeper", "rating_stars": "<span class=\"stars\">★½</span>", "rating_num": 1.5, "time": "11:15"}, {"number": 2, "name": "Allen Hawkins & Golden Grappler vs. Saburo Aoki Jr. & Salvador Sosa", "finish": "Allen Hawkins & Golden Grappler battled Saburo Aoki Jr. & Salvador Sosa to a  time limit draw", "rating_stars": "<span class=\"stars\">★★½</span>", "rating_num": 2.5, "time": ""}, {"number": 3, "name": "Alexander Wolfe (w/Imperium) vs. Ilja Dragunov", "finish": "Alexander Wolfe beat Ilja Dragunov in 10 Min 29 Sec with a Sitout Powerbomb", "rating_stars": "<span class=\"stars\">★★½</span>", "rating_num": 2.5, "time": "10:29"}, {"number": 4, "name": "World Title Tournament League: Lex Rider [0] vs. WALTER [0]", "finish": "Lex Rider beat WALTER in 22 Min 14 Sec with an Anaconda vice", "rating_stars": "<span class=\"stars\">★★★¾</span>", "rating_num": 3.75, "time": "22:14"}]
---

# PWA Friday Explosion 133

<div class="event-header">
<div class="event-meta">
**Date:** 2019-04-26<br>
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