---
layout: event.njk
title: PWA Friday Explosion
date: '2016-12-30'
venue: ''
location: ''
promotion: PWA
permalink: /events/2016-12-30 - PWA Friday Explosion/
tags:
- events
matches_json: [{"number": 1, "name": "PWA World Title #1 Contender Battle Royal Qualifiying: Alberto El Patron vs. Fred Balentine", "finish": "Alberto El Patron beat Fred Balentine (Bridge German Suplex)", "rating_stars": "<span class=\"stars\">★★★½</span>", "rating_num": 3.5, "time": ""}, {"number": 2, "name": "PWA World Title #1 Contender Battle Royal Qualifiying: UK Kid vs. Michael Elgin", "finish": "Michael Elgin beat UK Kid (Schwein)", "rating_stars": "<span class=\"stars\">★★★½</span>", "rating_num": 3.5, "time": ""}]
---

# PWA Friday Explosion

<div class="event-header">
<div class="event-meta">
**Date:** 2016-12-30<br>
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