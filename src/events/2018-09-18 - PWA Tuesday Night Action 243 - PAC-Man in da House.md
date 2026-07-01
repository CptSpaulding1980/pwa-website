---
layout: event.njk
title: PWA Tuesday Night Action 243 - PAC-Man in da House
date: '2018-09-18'
venue: Unknown
location: ''
promotion: PWA
permalink: /events/2018-09-18 - PWA Tuesday Night Action 243 - PAC-Man in da House/
tags:
- events
matches_json: [{"number": 1, "name": "Zodiac  vs. Poppa Thurgoode", "finish": "Zodiac  beat Poppa Thurgoode in 11 Min 39 Sec with a Canadian Face Buster", "rating_stars": "<span class=\"stars\">★★★¾</span>", "rating_num": 3.75, "time": "11:39"}, {"number": 2, "name": "Diablo Blanco & L.A. Park vs. Rey Fénix & Dragon Lee", "finish": "Diablo Blanco beat Dragon Lee in 20 Min 31 Sec with a Skull End", "rating_stars": "<span class=\"stars\">★★★★½</span>", "rating_num": 4.5, "time": "20:31"}, {"number": 3, "name": "Damon Smith vs. Ox Hemlock", "finish": "Ox Hemlock beat Damon Smith in 15 Min 13 Sec with a Turn Belly-to-Belly", "rating_stars": "<span class=\"stars\">★★★¼</span>", "rating_num": 3.25, "time": "15:13"}, {"number": 4, "name": "Veteran Veteran Devastators vs. Jean Wilson, Tri Clops & UK Kid", "finish": "Tri Clops beat Fabrizio Tiziano in 19 Min 24 Sec with an Ankle Hold", "rating_stars": "<span class=\"stars\">★★★¼</span>", "rating_num": 3.25, "time": "19:24"}, {"number": 5, "name": "Kota Ibushi, Kenny Omega & Hangman Page vs. BUSHI, Shingo Takagi & PAC", "finish": "PAC beat Hangman Page in 38 Min 48 Sec with a Nagata Lock III", "rating_stars": "<span class=\"stars\">★★★★★</span>", "rating_num": 5, "time": "38:48"}]
---

# PWA Tuesday Night Action 243 - PAC-Man in da House

<div class="event-header">
<div class="event-meta">
**Date:** 2018-09-18<br>
**Venue:** Unknown<br>
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