---
layout: event.njk
title: PWA Tuesday Night Action 275 - A Ceremony of Violence
date: '2019-05-07'
venue: PWA Capcom Arena
location: Boston, Massachusetts, USA
promotion: PWA
permalink: /events/2019-05-07 - PWA Tuesday Night Action 275 - A Ceremony of Violence/
tags:
- events
matches_json: [{"number": 1, "name": "Chelsea Grin & Red Dragon vs. Santana Family", "finish": "Felix Santana III beat Chelsea Grin in 25 Min 33 Sec with a Diving Lariat", "rating_stars": "<span class=\"stars\">★★½</span>", "rating_num": 2.5, "time": "25:33"}, {"number": 2, "name": "Shoot Style Match: Victor Kurilenko vs. Theobold Lovecraft", "finish": "Victor Kurilenko beat Theobold Lovecraft in 1R 2 Min 34 Sec with a K.O", "rating_stars": "<span class=\"stars\">★★★</span>", "rating_num": 3, "time": "2:34"}, {"number": 3, "name": "Mr. Suplex vs. Keith Rowans", "finish": "Mr. Suplex beat Keith Rowans in 6 Min 11 Sec with a Genki Raiga-plex", "rating_stars": "<span class=\"stars\">★</span>", "rating_num": 1, "time": "6:11"}, {"number": 4, "name": "Ox Hemlock, WALTER & Alexander Wolfe vs. Lex Rider, Fred Balentine & Chris Hero", "finish": "Ox Hemlock beat Fred Balentine in 16 Min 3 Sec with a K.O", "rating_stars": "<span class=\"stars\">★★★¼</span>", "rating_num": 3.25, "time": "16:03"}]
---

# PWA Tuesday Night Action 275 - A Ceremony of Violence

<div class="event-header">
<div class="event-meta">
**Date:** 2019-05-07<br>
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