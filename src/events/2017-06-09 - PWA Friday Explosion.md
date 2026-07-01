---
layout: event.njk
title: PWA Friday Explosion
date: '2017-06-09'
venue: ''
location: ''
promotion: PWA
permalink: /events/2017-06-09 - PWA Friday Explosion/
tags:
- events
matches_json: [{"number": 1, "name": "Tyler Bate vs. Shredder", "finish": "Tyler Bate beat Tyler Bate (Tyler Driver '97)", "rating_stars": "<span class=\"stars\">★★★¾</span>", "rating_num": 3.75, "time": ""}, {"number": 2, "name": "Best 2 out of 3 Falls Match - PWA World Heavyweight Championship: Jack Swagger vs. Roadkill (c)", "finish": "Roadkill beat Jack Swagger (1:0 Gutwrench Bomb 14:56 1:1 Road Diving Elbow Drop 17:55 1:2 Diving Back Elbow Drop 18:25)", "rating_stars": "<span class=\"stars\">★★★½</span>", "rating_num": 3.5, "time": ""}]
---

# PWA Friday Explosion

<div class="event-header">
<div class="event-meta">
**Date:** 2017-06-09<br>
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