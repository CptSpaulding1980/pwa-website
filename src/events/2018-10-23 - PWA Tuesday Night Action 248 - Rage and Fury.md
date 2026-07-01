---
layout: event.njk
title: PWA Tuesday Night Action 248 - Rage and Fury
date: '2018-10-23'
venue: Unknown
location: ''
promotion: PWA
permalink: /events/2018-10-23 - PWA Tuesday Night Action 248 - Rage and Fury/
tags:
- events
matches_json: [{"number": 1, "name": "Jitsu vs. Dynamite Smith", "finish": "Jitsu  beat Dynamite Smith in 10 Min 41 Sec with an Octopus Hold", "rating_stars": "<span class=\"stars\">★★</span>", "rating_num": 2, "time": "10:41"}, {"number": 2, "name": "Jack Fury & Rampage Rage vs. Misterio Guerrero & Theobold Lovecraft", "finish": "Brutes battled Misterio Guerrero & Theobold Lovecraft to a  time limit draw", "rating_stars": "<span class=\"stars\">★★★¼</span>", "rating_num": 3.25, "time": ""}, {"number": 3, "name": "Blue Blazer Jr. vs. Tri Clops", "finish": "Tri Clops beat Blue Blazer Jr. in 19 Min 13 Sec with an Ankle Hold", "rating_stars": "<span class=\"stars\">★★★★½</span>", "rating_num": 4.5, "time": "19:13"}, {"number": 4, "name": "El Experto vs. Macho Especial", "finish": "Macho Especial beat El Experto in 28 Min 55 Sec with a RING OUT", "rating_stars": "<span class=\"stars\">★★★★½</span>", "rating_num": 4.5, "time": "28:55"}, {"number": 5, "name": "UK Kid & Zack Sabre Jr. vs. Fabrizio Tiziano & PAC", "finish": "PAC beat UK Kid in 22 Min 24 Sec with a K.O", "rating_stars": "<span class=\"stars\">★★★★</span>", "rating_num": 4, "time": "22:24"}]
---

# PWA Tuesday Night Action 248 - Rage and Fury

<div class="event-header">
<div class="event-meta">
**Date:** 2018-10-23<br>
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