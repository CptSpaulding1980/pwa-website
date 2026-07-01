---
layout: event.njk
title: PWA Tuesday Night Action 286 - Look your back
date: '2019-07-30'
venue: PWA Capcom Arena
location: Boston, Massachusetts, USA
promotion: PWA
permalink: /events/2019-07-30 - PWA Tuesday Night Action 286 - Look your back/
tags:
- events
matches_json: [{"number": 1, "name": "Tundra Wurm vs. Rick Banner - If Banner wins he gets a World Title Shot", "finish": "Tundra Wurm beat Rick Banner in 16 Min 49 Sec with a Sky High Choke Slam", "rating_stars": "<span class=\"stars\">★★★★½</span>", "rating_num": 4.5, "time": "16:49"}, {"number": 2, "name": "Casper Winkel (w/Brutes) vs. Spitfire", "finish": "Casper Winkel beat Spitfire in 12 Min 54 Sec with a RING OUT", "rating_stars": "<span class=\"stars\">★★★★</span>", "rating_num": 4, "time": "12:54"}, {"number": 3, "name": "Invasores (Jupiter Solar & Neptune Tritano) vs. Blue Spider & John Hennigan", "finish": "Blue Spider beat Jupiter Solar in 19 Min 40 Sec with a RING OUT", "rating_stars": "<span class=\"stars\">★★★★¼</span>", "rating_num": 4.25, "time": "19:40"}, {"number": 4, "name": "SANADA vs. UK Kid", "finish": "UK Kid beat SANADA in 7 Min 36 Sec with a RING OUT", "rating_stars": "<span class=\"stars\">★★★¾</span>", "rating_num": 3.75, "time": "7:36"}, {"number": 5, "name": "No Disqualification - Non Title Match: Ox Hemlock vs. Fred Balentine", "finish": "Fred Balentine beat Ox Hemlock in 10 Min 37 Sec with an Avalanche Hold", "rating_stars": "<span class=\"stars\">★★★★★</span>", "rating_num": 5, "time": "10:37"}]
---

# PWA Tuesday Night Action 286 - Look your back

<div class="event-header">
<div class="event-meta">
**Date:** 2019-07-30<br>
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