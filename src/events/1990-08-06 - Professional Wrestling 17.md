---
layout: event.njk
title: Professional Wrestling 17
date: '1990-08-06'
venue: ''
location: ''
promotion: PWA
permalink: /events/1990-08-06 - Professional Wrestling 17/
tags:
- events
matches_json: [{"number": 1, "name": "2 out of 3 Falls - Non Title Match: Blue Spider vs. Ric Flair (c)", "finish": "First Fall: Blue Spider beat Ric Flair in 17 Min 32 Sec with a School Boy, Second Fall: Blue Spider beat Ric Flair in 2 Min 37 Sec with a RING OUT", "rating_stars": "<span class=\"stars\">★★★½</span>", "rating_num": 3.5, "time": "17:32"}]
---

# Professional Wrestling 17

<div class="event-header">
<div class="event-meta">
**Date:** 1990-08-06<br>
**Venue:** <br>
**Location:** 
</div>
<img src="/pwa-website/img/posters/1990-08-06 - Professional Wrestling 17.png" class="event-poster" alt="Poster">
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