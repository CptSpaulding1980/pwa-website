---
layout: event.njk
title: PWA Power Hour 23
date: '2019-07-18'
venue: PWA Power Studio
location: Boston, Massachusetts, USA
promotion: PWA
permalink: /events/2019-07-18 - PWA Power Hour 23/
tags:
- events
matches_json: [{"number": 1, "name": "Golden Grappler vs. Saburo Aoki Jr.", "finish": "Golden Grappler beat Saburo Aoki Jr. in 11 Min 39 Sec with a Shotgun", "rating_stars": "<span class=\"stars\">★★★¾</span>", "rating_num": 3.75, "time": "11:39"}, {"number": 2, "name": "PWA Jr. Heavyweight #1 Contendership: Fantasio Fantastico vs. Julio Rivera vs. Keith Rowans vs. Misterio Guerrero vs. Villano III Jr. vs. Metalik vs. AR Fox vs. Lio Rush", "finish": "Lio Rush won a 8 wrestler battle royale in  08:03", "rating_stars": "<span class=\"stars\">★★★½</span>", "rating_num": 3.5, "time": ""}, {"number": 3, "name": "Allen Hawkins vs. Dynamite Smith", "finish": "Allen Hawkins beat Dynamite Smith in 8 Min 34 Sec with an Oklahoma Stampede", "rating_stars": "<span class=\"stars\">★★★</span>", "rating_num": 3, "time": "8:34"}, {"number": 4, "name": "Dream Match: Timothy Thatcher vs. Tri Clops", "finish": "Tri Clops beat Timothy Thatcher in 20 Min 21 Sec with an Uproot German Suplex", "rating_stars": "<span class=\"stars\">★★★★</span>", "rating_num": 4, "time": "20:21"}]
---

# PWA Power Hour 23

<div class="event-header">
<div class="event-meta">
**Date:** 2019-07-18<br>
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