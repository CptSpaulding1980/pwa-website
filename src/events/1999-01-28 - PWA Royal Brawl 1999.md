---
layout: event.njk
title: PWA Royal Brawl 1999
date: '1999-01-28'
venue: ''
location: ''
promotion: PWA
permalink: /events/1999-01-28 - PWA Royal Brawl 1999/
tags:
- events
matches_json: [{"number": 1, "name": "PWA World Title #1 Contender Battle Royal", "finish": "Fred Balentine beat 19 other Wrestlers", "rating_stars": "<span class=\"stars\">★★★★</span>", "rating_num": 4, "time": ""}]
---

# PWA Royal Brawl 1999

<div class="event-header">
<div class="event-meta">
**Date:** 1999-01-28<br>
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