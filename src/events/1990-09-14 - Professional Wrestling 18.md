---
layout: event.njk
title: Professional Wrestling 18
date: '1990-09-14'
venue: ''
location: ''
promotion: PWA
permalink: /events/1990-09-14 - Professional Wrestling 18/
tags:
- events
matches_json: [{"number": 1, "name": "NWA World Heavyweight Championship: Blue Spider vs. Ric Flair (c)", "finish": "Ric Flair beat Blue Spider in 26 Min 06 Sec with a Figure Four Leglock", "rating_stars": "<span class=\"stars\">★★★★½</span>", "rating_num": 4.5, "time": "26:06"}, {"number": 2, "name": "Jerry Lawler vs. Fred Balentine", "finish": "Jerry Lawler beat Fred Balentine in 16 Min 06 Sec with a Backslide", "rating_stars": "<span class=\"stars\">★★★★</span>", "rating_num": 4, "time": "16:06"}]
---

# Professional Wrestling 18

<div class="event-header">
<div class="event-meta">
**Date:** 1990-09-14<br>
**Venue:** <br>
**Location:** 
</div>
<img src="/pwa-website/img/posters/1990-09-14 - Professional Wrestling 18.png" class="event-poster" alt="Poster">
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