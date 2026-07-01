---
layout: event.njk
title: PWA Tuesday Night Action 264 - Kid vs. Thatcher III - The Rubber Match
date: '2019-02-19'
venue: Keystone Centre
location: Brandon, Manitoba, Canada
promotion: PWA
permalink: /events/2019-02-19 - PWA Tuesday Night Action 264 - Kid vs. Thatcher III
  - The Rubber Match/
tags:
- events
matches_json: [{"number": 1, "name": "Veteran Veteran Devastators vs. Blake Twins", "finish": "Fabrizio Tiziano beat Sammy Blake in 11 Min 30 Sec with a Chickenwing Arm Lock", "rating_stars": "<span class=\"stars\">★★★½</span>", "rating_num": 3.5, "time": "11:30"}, {"number": 2, "name": "Victor Kurilenko (w/Brutes) vs. Cobra III (w/Masked Lucha Alliance)", "finish": "Victor Kurilenko beat Cobra III in 6 Min 45 Sec with a Choke Sleeper", "rating_stars": "<span class=\"stars\">★★★</span>", "rating_num": 3, "time": "6:45"}, {"number": 3, "name": "El Experto (w/Diablo Blanco) vs. Macho Especial (w/Blue Demon Jr.)", "finish": "El Experto battled Macho Especial to a  time limit draw", "rating_stars": "<span class=\"stars\">★★★½</span>", "rating_num": 3.5, "time": ""}, {"number": 4, "name": "Shoot Style Match (if Thatcher wins he is added to the Title Match at CoH): Timothy Thatcher vs. UK Kid", "finish": "UK Kid beat Timothy Thatcher in 2R 1 Min 8 Sec with a K.O", "rating_stars": "<span class=\"stars\">★★★½</span>", "rating_num": 3.5, "time": "1:08"}]
---

# PWA Tuesday Night Action 264 - Kid vs. Thatcher III - The Rubber Match

<div class="event-header">
<div class="event-meta">
**Date:** 2019-02-19<br>
**Venue:** Keystone Centre<br>
**Location:** Brandon, Manitoba, Canada
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