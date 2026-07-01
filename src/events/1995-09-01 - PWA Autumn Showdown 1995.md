---
layout: event.njk
title: PWA Autumn Showdown 1995
date: '1995-09-01'
venue: ''
location: ''
promotion: PWA
permalink: /events/1995-09-01 - PWA Autumn Showdown 1995/
tags:
- events
matches_json: [{"number": 1, "name": "Blade vs. Fred Balentine", "finish": "Blade beat Fred Balentine in 21 Min 13 Sec with a Roll Up", "rating_stars": "<span class=\"stars\">★★★¾</span>", "rating_num": 3.75, "time": "21:13"}]
---

# PWA Autumn Showdown 1995

<div class="event-header">
<div class="event-meta">
**Date:** 1995-09-01<br>
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