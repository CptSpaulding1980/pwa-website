---
layout: event.njk
title: PWA Power Hour 7
date: '2019-03-14'
venue: Qwest Arena
location: Boise, Idaho, USA
promotion: PWA
permalink: /events/2019-03-14 - PWA Power Hour 7/
tags:
- events
matches_json: [{"number": 1, "name": "Rampage Rage (w/Brutes) vs. Macho Especial (w/Masked Lucha Alliance)", "finish": "Rampage Rage battled Macho Especial to a 15 minute time limit draw", "rating_stars": "<span class=\"stars\">★★★★½</span>", "rating_num": 4.5, "time": ""}, {"number": 2, "name": "Blake Twins vs. Misterio Guerrero & Theobold Lovecraft", "finish": "Blake Twins battled Misterio Guerrero & Theobold Lovecraft to a 20 minute time limit draw", "rating_stars": "<span class=\"stars\">★★★★¾</span>", "rating_num": 4.75, "time": ""}, {"number": 3, "name": "Veteran Veteran Devastators vs. Julio Rivera, Masked Maniac IV, Shredder & Spitfire", "finish": "Fabrizio Tiziano beat Shredder in 6 Min 14 Sec with a Just Face Lock", "rating_stars": "<span class=\"stars\">★★½</span>", "rating_num": 2.5, "time": "6:14"}, {"number": 4, "name": "Ray Stantz vs. Poppa Thurgoode", "finish": "Poppa Thurgoode beat Ray Stantz in 3 Min 46 Sec with a Back Press", "rating_stars": "<span class=\"stars\">★★½</span>", "rating_num": 2.5, "time": "3:46"}]
---

# PWA Power Hour 7

<div class="event-header">
<div class="event-meta">
**Date:** 2019-03-14<br>
**Venue:** Qwest Arena<br>
**Location:** Boise, Idaho, USA
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