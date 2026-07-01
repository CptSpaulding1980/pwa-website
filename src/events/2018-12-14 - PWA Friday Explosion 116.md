---
layout: event.njk
title: PWA Friday Explosion 116
date: '2018-12-14'
venue: Albany, New York
location: ''
promotion: PWA
permalink: /events/2018-12-14 - PWA Friday Explosion 116/
tags:
- events
matches_json: [{"number": 1, "name": "Nigel Pendragon & Rick Banner vs. Masked Lucha Alliance", "finish": "Nigel Pendragon & Rick Banner battled Masked Lucha Alliance to a  time limit draw", "rating_stars": "<span class=\"stars\">★★★</span>", "rating_num": 3, "time": ""}, {"number": 2, "name": "Dynamite Smith vs. Ray Stantz", "finish": "Ray Stantz beat Dynamite Smith in 13 Min 24 Sec with a Tidal Suplex", "rating_stars": "<span class=\"stars\">★★★¼</span>", "rating_num": 3.25, "time": "13:24"}, {"number": 3, "name": "Allen Hawkins vs. Winston Zedd", "finish": "Allen Hawkins beat Winston Zedd in 1 Min 6 Sec with a Stepping Enzuigiri", "rating_stars": "<span class=\"stars\">★★</span>", "rating_num": 2, "time": "1:06"}, {"number": 4, "name": "Keith Rowans vs. Shingo Takagi", "finish": "Keith Rowans beat Shingo Takagi in 11 Min 43 Sec with a Flying Body Attack", "rating_stars": "<span class=\"stars\">★★★</span>", "rating_num": 3, "time": "11:43"}, {"number": 5, "name": "Ox Hemlock vs. Robert Dreissker", "finish": "Ox Hemlock beat Robert Dreissker in 7 Min 8 Sec with a Turn Belly-to-Belly", "rating_stars": "<span class=\"stars\">★★½</span>", "rating_num": 2.5, "time": "7:08"}, {"number": 6, "name": "Diablo Blanco vs. El Canek", "finish": "El Canek beat Diablo Blanco in 16 Min 56 Sec with a Torturerack", "rating_stars": "<span class=\"stars\">★★★★¼</span>", "rating_num": 4.25, "time": "16:56"}]
---

# PWA Friday Explosion 116

<div class="event-header">
<div class="event-meta">
**Date:** 2018-12-14<br>
**Venue:** Albany, New York<br>
**Location:** 
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