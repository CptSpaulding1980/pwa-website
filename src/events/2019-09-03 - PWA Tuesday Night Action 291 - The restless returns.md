---
layout: event.njk
title: PWA Tuesday Night Action 291 - The restless returns
date: '2019-09-03'
venue: PWA Capcom Arena
location: Boston, Massachusetts, USA
promotion: PWA
permalink: /events/2019-09-03 - PWA Tuesday Night Action 291 - The restless returns/
tags:
- events
matches_json: [{"number": 1, "name": "Cobra III (w/Macho Especial) vs. Allen Hawkins", "finish": "Allen Hawkins beat Cobra III in 17 Min 21 Sec with a Diving Body Press", "rating_stars": "<span class=\"stars\">★★★★</span>", "rating_num": 4, "time": "17:21"}, {"number": 2, "name": "Blake Twins vs. Mysterious Fantasticos", "finish": "Misterio Guerrero beat Elias Blake in 16 Min 8 Sec with a La Magistral", "rating_stars": "<span class=\"stars\">★★★¾</span>", "rating_num": 3.75, "time": "16:08"}, {"number": 3, "name": "Invasores vs. Blue Spider, Jean Wilson & Ricklon Smasher", "finish": "Jean Wilson beat Medic 2 in 9 Min 49 Sec with an Axe Bomber", "rating_stars": "<span class=\"stars\">★★½</span>", "rating_num": 2.5, "time": "9:49"}, {"number": 4, "name": "Diablo Blanco, Ox Hemlock & Tundra Wurm vs. Ilja Dragunov, Rick Banner & Fred Balentine", "finish": "Diablo Blanco beat Fred Balentine in 13 Min 39 Sec with a Cross Armbreaker", "rating_stars": "<span class=\"stars\">★★½</span>", "rating_num": 2.5, "time": "13:39"}]
---

# PWA Tuesday Night Action 291 - The restless returns

<div class="event-header">
<div class="event-meta">
**Date:** 2019-09-03<br>
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