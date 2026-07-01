---
layout: event.njk
title: PWA Friday Explosion 124
date: '2019-02-15'
venue: JFK Memorial Coliseum
location: Manchester, New Hampshire, USA
promotion: PWA
permalink: /events/2019-02-15 - PWA Friday Explosion 124/
tags:
- events
matches_json: [{"number": 1, "name": "Chelsea Grin vs. Felix Santana Sr. (w/Felix Santana Jr.)", "finish": "Chelsea Grin beat Felix Santana Sr. in 6 Min 26 Sec with a Modified Reverse Chickenwing", "rating_stars": "<span class=\"stars\">★★</span>", "rating_num": 2, "time": "6:26"}, {"number": 2, "name": "Mike Hool vs. Lex Rider", "finish": "Lex Rider beat Mike Hool in 8 Min 50 Sec with a Sleeper Hold", "rating_stars": "<span class=\"stars\">★★★½</span>", "rating_num": 3.5, "time": "8:50"}, {"number": 3, "name": "Brutes vs. Masked Lucha Alliance", "finish": "Skullface Killah beat El Canek in 15 Min 51 Sec with an Angle Choke Slam", "rating_stars": "<span class=\"stars\">★★★¼</span>", "rating_num": 3.25, "time": "15:51"}, {"number": 4, "name": "Golden Grappler vs. Blue Demon Jr.", "finish": "Blue Demon Jr. beat Golden Grappler in 9 Min 49 Sec with a Modified Sharpshooter", "rating_stars": "<span class=\"stars\">★★★½</span>", "rating_num": 3.5, "time": "9:49"}]
---

# PWA Friday Explosion 124

<div class="event-header">
<div class="event-meta">
**Date:** 2019-02-15<br>
**Venue:** JFK Memorial Coliseum<br>
**Location:** Manchester, New Hampshire, USA
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