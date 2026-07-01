---
layout: event.njk
title: PWA Friday Explosion 112
date: '2018-11-16'
venue: Unknown
location: ''
promotion: PWA
permalink: /events/2018-11-16 - PWA Friday Explosion 112/
tags:
- events
matches_json: [{"number": 1, "name": "Rick Banner vs. Felix Santana Jr.", "finish": "Felix Santana Jr. beat Rick Banner in 16 Min 51 Sec with a Prueba de Grandeza", "rating_stars": "<span class=\"stars\">★★★¼</span>", "rating_num": 3.25, "time": "16:51"}, {"number": 2, "name": "Dynamite Smith vs. Avery Alexander", "finish": "Dynamite Smith beat Avery Alexander in 21 Min 8 Sec with a Side Suplex", "rating_stars": "<span class=\"stars\">★★★★¼</span>", "rating_num": 4.25, "time": "21:08"}, {"number": 3, "name": "Ricklon Smasher vs. Ox Hemlock", "finish": "Ricklon Smasher beat Ox Hemlock in 12 Min 17 Sec with a Jumping Bomb", "rating_stars": "<span class=\"stars\">★★★★</span>", "rating_num": 4, "time": "12:17"}, {"number": 4, "name": "Brutes vs. Ringkampf", "finish": "Timothy Thatcher beat Victor Kurilenko in 23 Min 43 Sec with a Thatcher Stretch", "rating_stars": "<span class=\"stars\">★★★¾</span>", "rating_num": 3.75, "time": "23:43"}]
---

# PWA Friday Explosion 112

<div class="event-header">
<div class="event-meta">
**Date:** 2018-11-16<br>
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