---
layout: event.njk
title: Professional Wrestling 6
date: '1982-04-09'
venue: The Vault
location: Boston, MA
promotion: PWA
permalink: /events/1982-04-09 - Professional Wrestling 6/
tags:
- events
matches_json: [{"number": 1, "name": "Antonio Antiguo vs. Doctor Dorado", "finish": "Antonio Antiguo beat Doctor Dorado in 16 Min 10 Sec with a Victory Roll", "rating_stars": "<span class=\"stars\">★★★¼</span>", "rating_num": 3.25, "time": "16:10"}, {"number": 2, "name": "Holy Diver vs. Sam Barrett", "finish": "Holy Diver beat Sam Barrett in 17 Min 15 Sec with a Flying Rollup Pin", "rating_stars": "<span class=\"stars\">★★★★¼</span>", "rating_num": 4.25, "time": "17:15"}, {"number": 3, "name": "Dr. Angulo vs. Buddy Yorke", "finish": "Dr. Angulo beat Buddy Yorke in 11 Min 12 Sec with a Leg Cross Flying Rollup Pin", "rating_stars": "<span class=\"stars\">★★★¼</span>", "rating_num": 3.25, "time": "11:12"}]
---

# Professional Wrestling 6

<div class="event-header">
<div class="event-meta">
**Date:** 1982-04-09<br>
**Venue:** The Vault<br>
**Location:** Boston, MA
</div>
<img src="/pwa-website/img/posters/1982-04-09 - Professional Wrestling 6.png" class="event-poster" alt="Poster">
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