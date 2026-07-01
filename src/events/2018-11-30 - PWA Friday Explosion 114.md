---
layout: event.njk
title: PWA Friday Explosion 114
date: '2018-11-30'
venue: Philadelphia, Pennsylvania
location: ''
promotion: PWA
permalink: /events/2018-11-30 - PWA Friday Explosion 114/
tags:
- events
matches_json: [{"number": 1, "name": "Allen Hawkins vs. Misterio Guerrero", "finish": "Allen Hawkins beat Misterio Guerrero in 15 Min 37 Sec with a Diving Body Press", "rating_stars": "<span class=\"stars\">★★★★</span>", "rating_num": 4, "time": "15:37"}, {"number": 2, "name": "Shoot Style Match: Ray Stantz vs. Veit Müller", "finish": "Veit Müller beat Ray Stantz in 1R 9 Min 45 Sec with a K.O", "rating_stars": "<span class=\"stars\">★★★¾</span>", "rating_num": 3.75, "time": "9:45"}, {"number": 3, "name": "Shoot Style Match: Red Dragon vs. Poppa Thurgoode", "finish": "Poppa Thurgoode beat Red Dragon in 1R 8 Min 8 Sec with a K.O", "rating_stars": "<span class=\"stars\">★★★¼</span>", "rating_num": 3.25, "time": "8:08"}, {"number": 4, "name": "Avery Alexander vs. Dynamite Smith", "finish": "Avery Alexander beat Dynamite Smith in 13 Min 40 Sec with a High Angle Drop Kick", "rating_stars": "<span class=\"stars\">★★★</span>", "rating_num": 3, "time": "13:40"}]
---

# PWA Friday Explosion 114

<div class="event-header">
<div class="event-meta">
**Date:** 2018-11-30<br>
**Venue:** Philadelphia, Pennsylvania<br>
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