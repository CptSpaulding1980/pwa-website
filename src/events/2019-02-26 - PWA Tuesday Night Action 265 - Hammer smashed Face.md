---
layout: event.njk
title: PWA Tuesday Night Action 265 - Hammer smashed Face
date: '2019-02-26'
venue: Erie Civic Center
location: Erie, Pennsylvania, USA
promotion: PWA
permalink: /events/2019-02-26 - PWA Tuesday Night Action 265 - Hammer smashed Face/
tags:
- events
matches_json: [{"number": 1, "name": "Masked Maniac IV & Spitfire vs. Jean Wilson & Ricklon Smasher", "finish": "Jean Wilson beat Masked Maniac IV in 7 Min 36 Sec with a Spear", "rating_stars": "<span class=\"stars\">★★½</span>", "rating_num": 2.5, "time": "7:36"}, {"number": 2, "name": "Damon Smith vs. Saburo Aoki Jr.", "finish": "Damon Smith beat Saburo Aoki Jr. in 2 Min 56 Sec with a K.O", "rating_stars": "<span class=\"stars\">★</span>", "rating_num": 1, "time": "2:56"}, {"number": 3, "name": "Ray Stantz vs. Rick Banner", "finish": "Rick Banner beat Ray Stantz in 5 Min 26 Sec with a German Suplex", "rating_stars": "<span class=\"stars\">★</span>", "rating_num": 1, "time": "5:26"}, {"number": 4, "name": "Rampage Rage (w/Brutes) vs. Fred Balentine", "finish": "Fred Balentine beat Rampage Rage in 6 Min 23 Sec with a Flying Bodyscissors Attack", "rating_stars": "<span class=\"stars\">★</span>", "rating_num": 1, "time": "6:23"}, {"number": 5, "name": "Best 2 out of 3 Falls: El Experto, Golden Grappler & Diablo Blanco vs. Blue Demon Jr., Blue Spider & Macho Especial", "finish": "Blue Spider beat Diablo Blanco in the second Fall after 15 Min 12 Sec with a La Magistral (2:0 Falls)", "rating_stars": "<span class=\"stars\">★★★</span>", "rating_num": 3, "time": "15:12"}]
---

# PWA Tuesday Night Action 265 - Hammer smashed Face

<div class="event-header">
<div class="event-meta">
**Date:** 2019-02-26<br>
**Venue:** Erie Civic Center<br>
**Location:** Erie, Pennsylvania, USA
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