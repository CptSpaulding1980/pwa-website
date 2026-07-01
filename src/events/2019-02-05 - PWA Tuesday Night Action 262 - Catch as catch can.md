---
layout: event.njk
title: PWA Tuesday Night Action 262 - Catch as catch can
date: '2019-02-05'
venue: Cobo Arena
location: Detroit, Michigan, USA
promotion: PWA
permalink: /events/2019-02-05 - PWA Tuesday Night Action 262 - Catch as catch can/
tags:
- events
matches_json: [{"number": 1, "name": "Chelsea Grin (w/Avery Alexander) vs. Felix Santana Jr. (w/Felix Santana Sr.)", "finish": "Chelsea Grin beat Felix Santana Jr. in 12 Min 11 Sec with a Butterfly Neck Lock", "rating_stars": "<span class=\"stars\">★★★¾</span>", "rating_num": 3.75, "time": "12:11"}, {"number": 2, "name": "Tag Title #1 Cont. Tournament - Second Chance: Ilja Dragunov & WALTER vs. Masked Lucha Alliance", "finish": "Cobra III beat WALTER in 18 Min 59 Sec with a Cobra Twist", "rating_stars": "<span class=\"stars\">★★★½</span>", "rating_num": 3.5, "time": "18:59"}, {"number": 3, "name": "Tag Title #1 Cont. Tournament - Quarter Finals: Laredo Kid & Myzteziz Jr. vs. Allen Hawkins & Golden Grappler", "finish": "Laredo Kid beat Allen Hawkins in 19 Min 43 Sec with a RING OUT", "rating_stars": "<span class=\"stars\">★★★¼</span>", "rating_num": 3.25, "time": "19:43"}, {"number": 4, "name": "Shoot Style Match (Non Title): Timothy Thatcher vs. UK Kid", "finish": "Timothy Thatcher beat UK Kid in 2R 0 Min 32 Sec with a K.O", "rating_stars": "<span class=\"stars\">★★★¼</span>", "rating_num": 3.25, "time": "0:32"}]
---

# PWA Tuesday Night Action 262 - Catch as catch can

<div class="event-header">
<div class="event-meta">
**Date:** 2019-02-05<br>
**Venue:** Cobo Arena<br>
**Location:** Detroit, Michigan, USA
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