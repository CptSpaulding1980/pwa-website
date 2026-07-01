---
layout: event.njk
title: Professional Wrestling 15
date: '1989-10-21'
venue: ''
location: ''
promotion: PWA
permalink: /events/1989-10-21 - Professional Wrestling 15/
tags:
- events
matches_json: [{"number": 1, "name": "Stan Hansen vs. Fred Balentine", "finish": "Stan Hansen beat Fred Balentine in 21 Min 03 Sec with a Western Lariat", "rating_stars": "<span class=\"stars\">★★★¼</span>", "rating_num": 3.25, "time": "21:03"}]
---

# Professional Wrestling 15

<div class="event-header">
<div class="event-meta">
**Date:** 1989-10-21<br>
**Venue:** <br>
**Location:** 
</div>
<img src="/pwa-website/img/posters/1989-10-21 - Professional Wrestling 15.png" class="event-poster" alt="Poster">
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