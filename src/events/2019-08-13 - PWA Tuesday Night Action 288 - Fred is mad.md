---
layout: event.njk
title: PWA Tuesday Night Action 288 - Fred is mad
date: '2019-08-13'
venue: PWA Capcom Arena
location: Boston, Massachusetts, USA
promotion: PWA
permalink: /events/2019-08-13 - PWA Tuesday Night Action 288 - Fred is mad/
tags:
- events
matches_json: [{"number": 1, "name": "Todd Jackson vs. UK Kid", "finish": "UK Kid beat Todd Jackson in 12 Min 8 Sec with a Camel Clutch", "rating_stars": "<span class=\"stars\">★★★¼</span>", "rating_num": 3.25, "time": "12:08"}, {"number": 2, "name": "Theobold Lovecraft vs. Cobra III", "finish": "Theobold Lovecraft beat Cobra III in 16 Min 37 Sec with a Torture Cobra Twist", "rating_stars": "<span class=\"stars\">★★★½</span>", "rating_num": 3.5, "time": "16:37"}, {"number": 3, "name": "Interview Segment /w PWA World Champion Fred Balentine", "finish": "Interview segment involving: Joey Farrell & Fred Balentine", "rating_stars": "<span class=\"stars\">★★★½</span>", "rating_num": 3.5, "time": ""}, {"number": 4, "name": "John Hennigan vs. Zack Sabre Jr.", "finish": "John Hennigan beat Zack Sabre Jr. in 14 Min 54 Sec with a Twisting Moonsault Press", "rating_stars": "<span class=\"stars\">★★★★½</span>", "rating_num": 4.5, "time": "14:54"}, {"number": 5, "name": "Invasores vs. Blue Spider & Snake King", "finish": "Invasores battled Blue Spider & Snake King to a  time limit draw", "rating_stars": "<span class=\"stars\">★★★★</span>", "rating_num": 4, "time": ""}, {"number": 6, "name": "PWA International Championship: Roadkill (w/El Pulpo) vs. Hiroto Nakamichi (c)", "finish": "Hiroto Nakamichi beat Roadkill in 21 Min 34 Sec with a RING OUT", "rating_stars": "<span class=\"stars\">★★★¾</span>", "rating_num": 3.75, "time": "21:34"}]
---

# PWA Tuesday Night Action 288 - Fred is mad

<div class="event-header">
<div class="event-meta">
**Date:** 2019-08-13<br>
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