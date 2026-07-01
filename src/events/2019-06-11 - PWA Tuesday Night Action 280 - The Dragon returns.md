---
layout: event.njk
title: PWA Tuesday Night Action 280 - The Dragon returns
date: '2019-06-11'
venue: PWA Capcom Arena
location: Boston, Massachusetts, USA
promotion: PWA
permalink: /events/2019-06-11 - PWA Tuesday Night Action 280 - The Dragon returns/
tags:
- events
matches_json: [{"number": 1, "name": "Nigel Pendragon vs. Zack Sabre Jr.", "finish": "Zack Sabre Jr. beat Nigel Pendragon in 18 Min 3 Sec with a Japanese Leg Roll Clutch", "rating_stars": "<span class=\"stars\">★★★¾</span>", "rating_num": 3.75, "time": "18:03"}, {"number": 2, "name": "Adamo Dragon, Jupiter Solar, El Pulpo & Neptune Tritano vs. Fantasio Fantastico, Misterio Guerrero, Mystery Panther, & Theobold Lovecraft", "finish": "El Pulpo beat Theobold Lovecraft in 13 Min 26 Sec with a Modified Kabel Naria", "rating_stars": "<span class=\"stars\">★★★¼</span>", "rating_num": 3.25, "time": "13:26"}, {"number": 3, "name": "Mike Hool vs. Tri Clops", "finish": "Tri Clops beat Mike Hool in 20 Min 30 Sec with a Wakigatame", "rating_stars": "<span class=\"stars\">★★★¾</span>", "rating_num": 3.75, "time": "20:30"}, {"number": 4, "name": "Winner gets managing services of The Gatekeeper: Fabrizio Tiziano vs. Diablo Blanco", "finish": "Diablo Blanco beat Fabrizio Tiziano in 20 Min 34 Sec with a RING OUT", "rating_stars": "<span class=\"stars\">★★★¼</span>", "rating_num": 3.25, "time": "20:34"}, {"number": 5, "name": "Shingo Takagi vs. Rick Banner", "finish": "Shingo Takagi beat Rick Banner in 29 Min 32 Sec with a Last of the Dragon", "rating_stars": "<span class=\"stars\">★★★¾</span>", "rating_num": 3.75, "time": "29:32"}]
---

# PWA Tuesday Night Action 280 - The Dragon returns

<div class="event-header">
<div class="event-meta">
**Date:** 2019-06-11<br>
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