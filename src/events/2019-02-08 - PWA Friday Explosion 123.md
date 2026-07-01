---
layout: event.njk
title: PWA Friday Explosion 123
date: '2019-02-08'
venue: Boston Garden
location: Boston, Massachusetts, USA
promotion: PWA
permalink: /events/2019-02-08 - PWA Friday Explosion 123/
tags:
- events
matches_json: [{"number": 1, "name": "Masked Maniac IV vs. Saburo Aoki Jr.", "finish": "Saburo Aoki Jr. beat Masked Maniac IV in 1 Min 0 Sec with an El Es Culero", "rating_stars": "<span class=\"stars\">★½</span>", "rating_num": 1.5, "time": "1:00"}, {"number": 2, "name": "Tag Title #1 Cont. Tournament - Quarter Finals: Masked Lucha Alliance vs. The Lucha Brothers", "finish": "El Canek beat Pentagón Jr. in 30 Min 55 Sec with a Torturerack", "rating_stars": "<span class=\"stars\">★★★★½</span>", "rating_num": 4.5, "time": "30:55"}, {"number": 3, "name": "Tag Title #1 Cont. Tournament - Quarter Finals: Los Ingobernables de Japon vs. Mysterious Fantasticos", "finish": "EVIL  beat Mystery Panther in 15 Min 54 Sec with an Oosotogari Buster", "rating_stars": "<span class=\"stars\">★★★½</span>", "rating_num": 3.5, "time": "15:54"}, {"number": 4, "name": "Diablo Blanco vs. Blue Spider", "finish": "Blue Spider beat Diablo Blanco in 13 Min 2 Sec with a Flying Body Press", "rating_stars": "<span class=\"stars\">★★★★½</span>", "rating_num": 4.5, "time": "13:02"}]
---

# PWA Friday Explosion 123

<div class="event-header">
<div class="event-meta">
**Date:** 2019-02-08<br>
**Venue:** Boston Garden<br>
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