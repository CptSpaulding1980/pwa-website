---
layout: event.njk
title: Professional Wrestling 16
date: '1990-03-07'
venue: ''
location: ''
promotion: PWA
permalink: /events/1990-03-07 - Professional Wrestling 16/
tags:
- events
matches_json: [{"number": 1, "name": "Blade vs. Mil Mascaras", "finish": "Mil Mascaras beat Blade with a Flying Cross Chop", "rating_stars": "<span class=\"stars\">★★★¾</span>", "rating_num": 3.75, "time": ""}, {"number": 2, "name": "Non Title Match: Blue Spider vs. Ric Flair (c)", "finish": "Blue Spider beat Ric Flair in 21 Min 23 Sec with a Japanese Leg Roll Clutch", "rating_stars": "<span class=\"stars\">★★★★¼</span>", "rating_num": 4.25, "time": "21:23"}]
---

# Professional Wrestling 16

<div class="event-header">
<div class="event-meta">
**Date:** 1990-03-07<br>
**Venue:** <br>
**Location:** 
</div>
<img src="/pwa-website/img/posters/1990-03-07 - Professional Wrestling 16.png" class="event-poster" alt="Poster">
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