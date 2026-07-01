---
layout: event.njk
title: PWA Friday Explosion
date: '2018-01-05'
venue: ''
location: ''
promotion: PWA
permalink: /events/2018-01-05 - PWA Friday Explosion/
tags:
- events
matches_json: [{"number": 1, "name": "Royal Brawl Qualifying: Pete Dunne vs. UK Kid", "finish": "Draw (Time Limit Draw)", "rating_stars": "<span class=\"stars\">★★★★¾</span>", "rating_num": 4.75, "time": ""}]
---

# PWA Friday Explosion

<div class="event-header">
<div class="event-meta">
**Date:** 2018-01-05<br>
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