---
layout: event.njk
title: PWA Tuesday Night Action 290 - War Dogs ignite
date: '2019-08-27'
venue: PWA Capcom Arena
location: Boston, Massachusetts, USA
promotion: PWA
permalink: /events/2019-08-27 - PWA Tuesday Night Action 290 - War Dogs ignite/
tags:
- events
matches_json: [{"number": 1, "name": "Falls Count Anywhere - PWA International Championship: Roadkill vs. Hiroto Nakamichi (c)", "finish": "Hiroto Nakamichi beat Roadkill in 25 Min 56 Sec with a Rising Sun Stretch", "rating_stars": "<span class=\"stars\">★★★★</span>", "rating_num": 4, "time": "25:56"}, {"number": 2, "name": "Avery Alexander vs. Poppa Thurgoode", "finish": "Avery Alexander battled Poppa Thurgoode to a  double KO draw", "rating_stars": "<span class=\"stars\">★½</span>", "rating_num": 1.5, "time": ""}, {"number": 3, "name": "Diablo Blanco (w/The Gatekeeper) vs. Misterio Guerrero", "finish": "Diablo Blanco beat Misterio Guerrero in 16 Min 34 Sec with a Skull End", "rating_stars": "<span class=\"stars\">★★★</span>", "rating_num": 3, "time": "16:34"}, {"number": 4, "name": "Invasores vs. Blue Spider, Jean Wilson & Ricklon Smasher", "finish": "Invasores battled Blue Spider,  Jean Wilson, & Ricklon Smasher to a  time limit draw", "rating_stars": "<span class=\"stars\">★★★½</span>", "rating_num": 3.5, "time": ""}]
---

# PWA Tuesday Night Action 290 - War Dogs ignite

<div class="event-header">
<div class="event-meta">
**Date:** 2019-08-27<br>
**Venue:** PWA Capcom Arena<br>
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