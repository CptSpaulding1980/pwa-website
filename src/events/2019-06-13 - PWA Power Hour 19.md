---
layout: event.njk
title: PWA Power Hour 19
date: '2019-06-13'
venue: PWA Power Studio
location: Boston, Massachusetts, USA
promotion: PWA
permalink: /events/2019-06-13 - PWA Power Hour 19/
tags:
- events
matches_json: [{"number": 1, "name": "Rampage Rage vs. Macho Especial", "finish": "Macho Especial beat Rampage Rage in 14 Min 25 Sec with a La Magistral", "rating_stars": "<span class=\"stars\">★★★★¼</span>", "rating_num": 4.25, "time": "14:25"}, {"number": 2, "name": "Blue Blazer Jr. vs. Bandido", "finish": "Blue Blazer Jr. beat Bandido in 24 Min 14 Sec with a Sharpshooter", "rating_stars": "<span class=\"stars\">★★★¾</span>", "rating_num": 3.75, "time": "24:14"}, {"number": 3, "name": "Casper Winkel vs. Ricklon Smasher", "finish": "Casper Winkel beat Ricklon Smasher in 7 Min 34 Sec with a K.O", "rating_stars": "<span class=\"stars\">★★</span>", "rating_num": 2, "time": "7:34"}, {"number": 4, "name": "Best 2 out of 3 Falls: Jonathan Gresham vs. Dynamite Smith", "finish": "Jonathan Gresham beat Dynamite Smith in 17 Min 13 Sec with a Japanese Leg Roll Clutch", "rating_stars": "<span class=\"stars\">★★★½</span>", "rating_num": 3.5, "time": "17:13"}, {"number": 5, "name": "PWA International Championship: Johnny Power (John Hennigan) vs. Roadkill (c)", "finish": "John Hennigan beat Roadkill in 10 Min 21 Sec with a Twisting Moonsault Press", "rating_stars": "<span class=\"stars\">★★★¼</span>", "rating_num": 3.25, "time": "10:21"}]
---

# PWA Power Hour 19

<div class="event-header">
<div class="event-meta">
**Date:** 2019-06-13<br>
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