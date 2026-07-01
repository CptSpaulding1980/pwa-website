---
layout: event.njk
title: PWA Power Hour 9
date: '2019-04-04'
venue: PWA Power Studio
location: Boston, Massachusetts, USA
promotion: PWA
permalink: /events/2019-04-04 - PWA Power Hour 9/
tags:
- events
matches_json: [{"number": 1, "name": "Salvador Sosa vs. Misterio Guerrero", "finish": "Salvador Sosa beat Misterio Guerrero in 14 Min 54 Sec with an Emerald Flowsion", "rating_stars": "<span class=\"stars\">★★★½</span>", "rating_num": 3.5, "time": "14:54"}, {"number": 2, "name": "Victor Kurilenko vs. Masked Maniac IV", "finish": "Victor Kurilenko beat Masked Maniac IV in 9 Min 4 Sec with a Choke Sleeper", "rating_stars": "<span class=\"stars\">★</span>", "rating_num": 1, "time": "9:04"}, {"number": 3, "name": "Casper Winkel vs. Dynamite Smith", "finish": "Casper Winkel beat Dynamite Smith in 16 Min 33 Sec with a Buffalo Sleeper", "rating_stars": "<span class=\"stars\">★★★½</span>", "rating_num": 3.5, "time": "16:33"}, {"number": 4, "name": "Foreign Fanatics vs. Mysterious Fantasticos", "finish": "Hiroto Nakamichi & Jitsu  battled Fantasio Fantastico & Mystery Panther to a  time limit draw", "rating_stars": "<span class=\"stars\">★★★★</span>", "rating_num": 4, "time": ""}]
---

# PWA Power Hour 9

<div class="event-header">
<div class="event-meta">
**Date:** 2019-04-04<br>
**Venue:** PWA Power Studio<br>
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