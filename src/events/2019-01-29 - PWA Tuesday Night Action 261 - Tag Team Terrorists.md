---
layout: event.njk
title: PWA Tuesday Night Action 261 - Tag Team Terrorists
date: '2019-01-29'
venue: Richmond, Virginia
location: ''
promotion: PWA
permalink: /events/2019-01-29 - PWA Tuesday Night Action 261 - Tag Team Terrorists/
tags:
- events
matches_json: [{"number": 1, "name": "Ray Stantz vs. Spitfire", "finish": "Spitfire beat Ray Stantz in 14 Min 38 Sec with a Wakigatame", "rating_stars": "<span class=\"stars\">★★★½</span>", "rating_num": 3.5, "time": "14:38"}, {"number": 2, "name": "Tag Title #1 Contender Tournament: Laredo Kid & Myzteziz Jr. vs. Misterio Guerrero & Theobold Lovecraft", "finish": "Laredo Kid beat Misterio Guerrero in 27 Min 18 Sec with a Spanish Fly", "rating_stars": "<span class=\"stars\">★★★★¼</span>", "rating_num": 4.25, "time": "27:18"}, {"number": 3, "name": "Tag Title #1 Contender Tournament: WALTER & Ilja Dragunov vs. Masked Lucha Alliance", "finish": "WALTER & Ilja Dragunov battled Masked Lucha Alliance to a  time limit draw", "rating_stars": "<span class=\"stars\">★★★★½</span>", "rating_num": 4.5, "time": ""}, {"number": 4, "name": "Tag Title #1 Contender Tournament: Allen Hawkins & Golden Grappler vs. Blue Demon Jr. & Macho Especial", "finish": "Golden Grappler beat Macho Especial in 12 Min 17 Sec with a Shotgun", "rating_stars": "<span class=\"stars\">★★★¼</span>", "rating_num": 3.25, "time": "12:17"}, {"number": 5, "name": "Tag Title #1 Contender Tournament: The Lucha Brothers vs. Veteran Veteran Devastators", "finish": "Pentagón Jr. beat Fabrizio Tiziano in 22 Min 59 Sec with a Karma", "rating_stars": "<span class=\"stars\">★★★★¾</span>", "rating_num": 4.75, "time": "22:59"}, {"number": 6, "name": "Jack Fury vs. Fred Balentine", "finish": "Fred Balentine beat Jack Fury in 11 Min 19 Sec with a DQ", "rating_stars": "<span class=\"stars\">★★★½</span>", "rating_num": 3.5, "time": "11:19"}]
---

# PWA Tuesday Night Action 261 - Tag Team Terrorists

<div class="event-header">
<div class="event-meta">
**Date:** 2019-01-29<br>
**Venue:** Richmond, Virginia<br>
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