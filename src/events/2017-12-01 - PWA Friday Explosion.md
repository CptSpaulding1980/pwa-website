---
layout: event.njk
title: PWA Friday Explosion
date: '2017-12-01'
venue: ''
location: ''
promotion: PWA
permalink: /events/2017-12-01 - PWA Friday Explosion/
tags:
- events
matches_json: [{"number": 1, "name": "No Disqualification No Count Out Best 2 out of 3 Falls Match: Kenny Omega vs. Blue Spider", "finish": "Kenny Omega beat Blue Spider (1:0 One Winged Angel (10:37) 2:0 One Winged Angel (CRITICAL)(17:44))", "rating_stars": "<span class=\"stars\">★★★★¼</span>", "rating_num": 4.25, "time": ""}]
---

# PWA Friday Explosion

<div class="event-header">
<div class="event-meta">
**Date:** 2017-12-01<br>
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