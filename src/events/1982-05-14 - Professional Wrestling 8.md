---
layout: event.njk
title: Professional Wrestling 8
date: '1982-05-14'
venue: The Vault
location: Boston, MA
promotion: PWA
permalink: /events/1982-05-14 - Professional Wrestling 8/
tags:
- events
matches_json: [{"number": 1, "name": "Joey Farrell vs. Ernesto Marquez", "finish": "Joey Farrell beat Ernesto Marquez in 9 Min 36 Sec with a Flying Rollup Pin", "rating_stars": "<span class=\"stars\">★★</span>", "rating_num": 2, "time": "9:36"}, {"number": 2, "name": "Paullus the Colossus vs. Burt Mancaster", "finish": "Paullus the Colossus beat Burt Mancaster in 13 Min 16 Sec with a Dangerous Knee Drop", "rating_stars": "<span class=\"stars\">★★★½</span>", "rating_num": 3.5, "time": "13:16"}, {"number": 3, "name": "Best 2 out of 3 Falls: Billy Fender & Bud Hemsworth vs. Antonio Antiguo & Dr. Angulo", "finish": "Antonio Antiguo beat Billy Fender in 49 Min 38 Sec", "rating_stars": "<span class=\"stars\">★★★★¾</span>", "rating_num": 4.75, "time": "49:38"}]
---

# Professional Wrestling 8

<div class="event-header">
<div class="event-meta">
**Date:** 1982-05-14<br>
**Venue:** The Vault<br>
**Location:** Boston, MA
</div>
<img src="/pwa-website/img/posters/1982-05-14 - Professional Wrestling 8.png" class="event-poster" alt="Poster">
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