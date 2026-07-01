---
layout: event.njk
title: Professional Wrestling 7
date: '1982-04-23'
venue: The Vault
location: Boston, MA
promotion: PWA
permalink: /events/1982-04-23 - Professional Wrestling 7/
tags:
- events
matches_json: [{"number": 1, "name": "Billy Fender, Bud Hemsworth & Joey Farrell vs. Antonio Antiguo, Diego Guerrero & Dr. Angulo", "finish": "Billy Fender beat Antonio Antiguo in 17 Min 39 Sec", "rating_stars": "<span class=\"stars\">★★★¾</span>", "rating_num": 3.75, "time": "17:39"}, {"number": 2, "name": "Preston Toddsworth vs. Unknown X", "finish": "Preston Toddsworth beat Unknown X in 30 Min 36 Sec with a School Boy", "rating_stars": "<span class=\"stars\">★★★★¼</span>", "rating_num": 4.25, "time": "30:36"}]
---

# Professional Wrestling 7

<div class="event-header">
<div class="event-meta">
**Date:** 1982-04-23<br>
**Venue:** The Vault<br>
**Location:** Boston, MA
</div>
<img src="/pwa-website/img/posters/1982-04-23 - Professional Wrestling 7.png" class="event-poster" alt="Poster">
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