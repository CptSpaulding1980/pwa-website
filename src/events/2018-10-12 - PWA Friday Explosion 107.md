---
layout: event.njk
title: PWA Friday Explosion 107
date: '2018-10-12'
venue: Philadelphia, Pennsylvania
location: ''
promotion: PWA
permalink: /events/2018-10-12 - PWA Friday Explosion 107/
tags:
- events
matches_json: [{"number": 1, "name": "Jitsu  & Ox Hemlock vs. Dynamite Smith & Ricklon Smasher", "finish": "Jitsu  beat Ricklon Smasher in 13 Min 4 Sec with a Wakigatame", "rating_stars": "<span class=\"stars\">★½</span>", "rating_num": 1.5, "time": "13:04"}, {"number": 2, "name": "Brutes vs. Casper Winkel & Rick Banner", "finish": "Brutes battled Casper Winkel & Rick Banner to a  time limit draw", "rating_stars": "<span class=\"stars\">★★★★½</span>", "rating_num": 4.5, "time": ""}, {"number": 3, "name": "Diablo Blanco vs. Fantasio Fantastico", "finish": "Diablo Blanco beat Fantasio Fantastico in 0 Min 47 Sec with a K.O", "rating_stars": "<span class=\"stars\">DUD</span>", "rating_num": 0, "time": "0:47"}, {"number": 4, "name": "PWA World Heavyweight Title #1 Contender: Fabrizio Tiziano vs. UK Kid", "finish": "Fabrizio Tiziano beat UK Kid  in 9 Min 55 Sec with a Manovra Vittoria", "rating_stars": "<span class=\"stars\">★½</span>", "rating_num": 1.5, "time": "9:55"}]
---

# PWA Friday Explosion 107

<div class="event-header">
<div class="event-meta">
**Date:** 2018-10-12<br>
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