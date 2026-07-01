---
layout: event.njk
title: PWA Friday Explosion 111
date: '2018-11-09'
venue: Unknown
location: ''
promotion: PWA
permalink: /events/2018-11-09 - PWA Friday Explosion 111/
tags:
- events
matches_json: [{"number": 1, "name": "Seth Ramsey & Todd Jackson vs. Avery Alexander & Red Dragon", "finish": "Avery Alexander beat Todd Jackson in 13 Min 55 Sec with a Pinnacle Dropkick", "rating_stars": "<span class=\"stars\">★★★</span>", "rating_num": 3, "time": "13:55"}, {"number": 2, "name": "Jitsu vs. Saburo Aoki Jr.", "finish": "Jitsu  beat Saburo Aoki Jr. in 7 Min 11 Sec with a Bodyslam", "rating_stars": "<span class=\"stars\">★½</span>", "rating_num": 1.5, "time": "7:11"}, {"number": 3, "name": "Hiroto Nakamichi vs. Poppa Thurgoode", "finish": "Poppa Thurgoode beat Hiroto Nakamichi in 18 Min 17 Sec with a Lariat Attack", "rating_stars": "<span class=\"stars\">★★★★½</span>", "rating_num": 4.5, "time": "18:17"}, {"number": 4, "name": "Casper Winkel, Rick Banner & Ricklon Smasher vs. Mysterious Fantasticos", "finish": "Rick Banner beat Misterio Guerrero in 21 Min 32 Sec with a K.O", "rating_stars": "<span class=\"stars\">★★★</span>", "rating_num": 3, "time": "21:32"}]
---

# PWA Friday Explosion 111

<div class="event-header">
<div class="event-meta">
**Date:** 2018-11-09<br>
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