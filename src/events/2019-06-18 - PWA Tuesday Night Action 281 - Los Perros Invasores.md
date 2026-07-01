---
layout: event.njk
title: PWA Tuesday Night Action 281 - Los Perros Invasores
date: '2019-06-18'
venue: PWA Capcom Arena
location: Boston, Massachusetts, USA
promotion: PWA
permalink: /events/2019-06-18 - PWA Tuesday Night Action 281 - Los Perros Invasores/
tags:
- events
matches_json: [{"number": 1, "name": "Invasores (Medic 1 & Medic 2 /w El Pulpo) vs. Santana Family", "finish": "Medic 1 beat Felix Santana Jr. in 14 Min 11 Sec with a Diving Rolling Guillotine Drop", "rating_stars": "<span class=\"stars\">★★★★¼</span>", "rating_num": 4.25, "time": "14:11"}, {"number": 2, "name": "Winston Zedd vs. Shingo Takagi", "finish": "Shingo Takagi beat Winston Zedd in 7 Min 45 Sec with a Noshigami", "rating_stars": "<span class=\"stars\">★★★★</span>", "rating_num": 4, "time": "7:45"}, {"number": 3, "name": "PWA Jr. Heavyweight #1 Contendership Elimination Match", "finish": "Misterio Guerrero won a 8 wrestler battle royale in  33:40", "rating_stars": "<span class=\"stars\">★★★¾</span>", "rating_num": 3.75, "time": ""}, {"number": 4, "name": "Invasores (Jupiter Solar & Neptune Tritano /w El Pulpo) vs. Julio Rivera & Salvador Sosa", "finish": "Jupiter Solar beat Julio Rivera in 9 Min 47 Sec with a Moonsault Press", "rating_stars": "<span class=\"stars\">★★★★¾</span>", "rating_num": 4.75, "time": "9:47"}, {"number": 5, "name": "Brutes vs. Jean Wilson, Ricklon Smasher & Tri Clops", "finish": "Ricklon Smasher beat Skullface Killah in 2 Min 59 Sec with a Tope Atomico", "rating_stars": "<span class=\"stars\">★</span>", "rating_num": 1, "time": "2:59"}]
---

# PWA Tuesday Night Action 281 - Los Perros Invasores

<div class="event-header">
<div class="event-meta">
**Date:** 2019-06-18<br>
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