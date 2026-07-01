---
layout: event.njk
title: PWA Tuesday Night Action 273 - World Title Tournament
date: '2019-04-23'
venue: PWA Capcom Arena
location: Boston, Massachusetts, USA
promotion: PWA
permalink: /events/2019-04-23 - PWA Tuesday Night Action 273 - World Title Tournament/
tags:
- events
matches_json: [{"number": 1, "name": "Chelsea Grin vs. Villano III Jr.", "finish": "Chelsea Grin beat Villano III Jr. in 18 Min 34 Sec with a Modified Reverse Chickenwing", "rating_stars": "<span class=\"stars\">★★★★</span>", "rating_num": 4, "time": "18:34"}, {"number": 2, "name": "Seth Ramsey & Todd Jackson vs. Masked Lucha Alliance", "finish": "Cobra  beat Todd Jackson in 6 Min 16 Sec with a Jumping Tombstone", "rating_stars": "<span class=\"stars\">DUD</span>", "rating_num": 0, "time": "6:16"}, {"number": 3, "name": "World Title Tournament League:  Diablo Blanco [0] vs. Roadkill [0]", "finish": "Roadkill beat Diablo Blanco in 14 Min 13 Sec with a Triangle Scorpion", "rating_stars": "<span class=\"stars\">★★½</span>", "rating_num": 2.5, "time": "14:13"}, {"number": 4, "name": "World Title Tournament League: Ox Hemlock [0] vs. Rick Banner [0]", "finish": "Ox Hemlock beat Rick Banner in 7 Min 34 Sec with a Turn Belly-to-Belly", "rating_stars": "<span class=\"stars\">DUD</span>", "rating_num": 0, "time": "7:34"}, {"number": 5, "name": "World Title Tournament League: Avery Alexander [0] vs. Shingo Takagi [0]", "finish": "Avery Alexander beat Shingo Takagi in 21 Min 43 Sec with a Most Muscular", "rating_stars": "<span class=\"stars\">★★★★¼</span>", "rating_num": 4.25, "time": "21:43"}]
---

# PWA Tuesday Night Action 273 - World Title Tournament

<div class="event-header">
<div class="event-meta">
**Date:** 2019-04-23<br>
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