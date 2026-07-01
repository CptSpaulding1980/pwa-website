---
layout: event.njk
title: PWA Tuesday Night Action
date: '2016-06-21'
venue: ''
location: ''
promotion: PWA
permalink: /events/2016-06-21 - PWA Tuesday Night Action/
tags:
- events
matches_json: [{"number": 1, "name": "ROH World Title Tournament - Semi Final #1: Tri Clops vs. Christopher Daniels", "finish": "Tri Clops beat Christopher Daniels (German Suplex)", "rating_stars": "<span class=\"stars\">★★★½</span>", "rating_num": 3.5, "time": ""}, {"number": 2, "name": "Non Title Match: Austin Aries vs. Roadkill", "finish": "Roadkill beat Austin Aries (Missile Dropkick)", "rating_stars": "<span class=\"stars\">★★★¾</span>", "rating_num": 3.75, "time": ""}, {"number": 3, "name": "Slicer vs. Masato Tanaka (w/ Fred Balentine)", "finish": "Masato Tanaka beat Slicer (Ankle Lock)", "rating_stars": "<span class=\"stars\">★★★½</span>", "rating_num": 3.5, "time": ""}]
---

# PWA Tuesday Night Action

<div class="event-header">
<div class="event-meta">
**Date:** 2016-06-21<br>
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