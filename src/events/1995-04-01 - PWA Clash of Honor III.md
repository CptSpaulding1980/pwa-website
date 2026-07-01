---
layout: event.njk
title: PWA Clash of Honor III
date: '1995-04-01'
venue: ''
location: ''
promotion: PWA
permalink: /events/1995-04-01 - PWA Clash of Honor III/
tags:
- events
matches_json: [{"number": 1, "name": "PWA World Heavyweight Championship: Snake King vs. Fred Balentine (c)", "finish": "Fred Balentine beat Snake King in 19 Min 48 Sec with a Sledgehammer", "rating_stars": "<span class=\"stars\">★★★½</span>", "rating_num": 3.5, "time": "19:48"}]
---

# PWA Clash of Honor III

<div class="event-header">
<div class="event-meta">
**Date:** 1995-04-01<br>
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