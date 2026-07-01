---
layout: event.njk
title: Professional Wrestling 19
date: '1991-07-13'
venue: ''
location: ''
promotion: PWA
permalink: /events/1991-07-13 - Professional Wrestling 19/
tags:
- events
matches_json: [{"number": 1, "name": "Fred Balentine vs. Mitsuharu Misawa", "finish": "Mitsuharu Misawa beat Fred Balentine in 20 Min 32 Sec with a Rolling Camel Clutch", "rating_stars": "<span class=\"stars\">★★★★¼</span>", "rating_num": 4.25, "time": "20:32"}]
---

# Professional Wrestling 19

<div class="event-header">
<div class="event-meta">
**Date:** 1991-07-13<br>
**Venue:** <br>
**Location:** 
</div>
<img src="/pwa-website/img/posters/1991-07-13 - Professional Wrestling 19.png" class="event-poster" alt="Poster">
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