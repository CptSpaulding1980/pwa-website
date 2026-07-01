---
layout: event.njk
title: PWA Clash of Honor VI
date: '1998-04-01'
venue: ''
location: ''
promotion: PWA
permalink: /events/1998-04-01 - PWA Clash of Honor VI/
tags:
- events
matches_json: [{"number": 1, "name": "Tri Clops vs. Jushin Liger", "finish": "Jushin Liger beat Tri Clops with a Sleeper Hold", "rating_stars": "<span class=\"stars\">★★★★¼</span>", "rating_num": 4.25, "time": ""}, {"number": 2, "name": "PWA World Heavyweight Championship: Blue Spider vs. Tiger Mask (c)", "finish": "Blue Spider beat Tiger Mask in 21 Min 14 Sec with a Shooting Star Press", "rating_stars": "<span class=\"stars\">★★★★¼</span>", "rating_num": 4.25, "time": "21:14"}]
---

# PWA Clash of Honor VI

<div class="event-header">
<div class="event-meta">
**Date:** 1998-04-01<br>
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