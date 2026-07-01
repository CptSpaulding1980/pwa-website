---
layout: event.njk
title: PWA Friday Explosion 129
date: '2019-03-29'
venue: Winnipeg Arena
location: Winnipeg, Manitoba, Canada
promotion: PWA
permalink: /events/2019-03-29 - PWA Friday Explosion 129/
tags:
- events
matches_json: [{"number": 1, "name": "Julio Rivera vs. Mr. Suplex", "finish": "Mr. Suplex beat Julio Rivera in 9 Min 30 Sec with a Genki Raiga-plex", "rating_stars": "<span class=\"stars\">★★★¾</span>", "rating_num": 3.75, "time": "9:30"}, {"number": 2, "name": "Veteran Veteran Devastators vs. Misterio Guerrero & Theobold Lovecraft", "finish": "Keith Rowans beat  by DRAW", "rating_stars": "<span class=\"stars\">★★★½</span>", "rating_num": 3.5, "time": ""}, {"number": 3, "name": "Nigel Pendragon vs. Saburo Aoki Jr.", "finish": "Saburo Aoki Jr. beat Nigel Pendragon in 12 Min 13 Sec with a Swift Blade", "rating_stars": "<span class=\"stars\">★★★¼</span>", "rating_num": 3.25, "time": "12:13"}, {"number": 4, "name": "Diablo Blanco, El Experto & Dr. Wagner Jr. vs. Blue Spider, Blue Demon Jr. & El Canek", "finish": "Diablo Blanco beat Blue Demon Jr. in 24 Min 41 Sec with a Skull End", "rating_stars": "<span class=\"stars\">★★★¼</span>", "rating_num": 3.25, "time": "24:41"}]
---

# PWA Friday Explosion 129

<div class="event-header">
<div class="event-meta">
**Date:** 2019-03-29<br>
**Venue:** Winnipeg Arena<br>
**Location:** Winnipeg, Manitoba, Canada
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