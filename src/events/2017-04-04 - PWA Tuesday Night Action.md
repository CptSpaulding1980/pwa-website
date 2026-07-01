---
layout: event.njk
title: PWA Tuesday Night Action
date: '2017-04-04'
venue: ''
location: ''
promotion: PWA
permalink: /events/2017-04-04 - PWA Tuesday Night Action/
tags:
- events
matches_json: [{"number": 1, "name": "Best 2 out of 3 Falls Match - PWA World Tag Team Championship: El Canek & Grizzlor vs. Davey Richards & Eddie Edwards (c)", "finish": "El Canek & Grizzlor beat Davey Richards & Eddie Edwards (1:0 Figure Four Leg Lock (Canek an Richards) 31:59 2:0 Choke Slam (Grizzlor an Edwards) 27:19)", "rating_stars": "<span class=\"stars\">★★★★¾</span>", "rating_num": 4.75, "time": ""}]
---

# PWA Tuesday Night Action

<div class="event-header">
<div class="event-meta">
**Date:** 2017-04-04<br>
**Venue:** <br>
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