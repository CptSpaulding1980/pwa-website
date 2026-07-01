---
layout: event.njk
title: PWA Tuesday Night Action 285 - Sweet Dreams
date: '2019-07-23'
venue: PWA Capcom Arena
location: Boston, Massachusetts, USA
promotion: PWA
permalink: /events/2019-07-23 - PWA Tuesday Night Action 285 - Sweet Dreams/
tags:
- events
matches_json: [{"number": 1, "name": "PWA Junior Heavyweight Championship: Lio Rush vs. Blue Blazer Jr. (c)", "finish": "Blue Blazer Jr. beat Lio Rush in 10 Min 41 Sec with a RING OUT", "rating_stars": "<span class=\"stars\">★★</span>", "rating_num": 2, "time": "10:41"}, {"number": 2, "name": "Roadkill (w/Invasores) vs. Snake King (w/Blue Spider)", "finish": "Roadkill beat Snake King in 13 Min 38 Sec with an Appeal Diving Elbowdrop", "rating_stars": "<span class=\"stars\">★★★</span>", "rating_num": 3, "time": "13:38"}, {"number": 3, "name": "PWA International Championship: Hiroto Nakamichi vs. John Hennigan (c)", "finish": "Hiroto Nakamichi beat John Hennigan in 12 Min 1 Sec with a Rising Sun Stretch", "rating_stars": "<span class=\"stars\">★★</span>", "rating_num": 2, "time": "12:01"}, {"number": 4, "name": "Tundra Wurm & Ox Hemlock vs. Fred Balentine & Rick Banner", "finish": "Rick Banner beat Ox Hemlock in 9 Min 53 Sec with a Tiger Suplex", "rating_stars": "<span class=\"stars\">★½</span>", "rating_num": 1.5, "time": "9:53"}]
---

# PWA Tuesday Night Action 285 - Sweet Dreams

<div class="event-header">
<div class="event-meta">
**Date:** 2019-07-23<br>
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