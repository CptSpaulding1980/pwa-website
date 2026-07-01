---
layout: event.njk
title: PWA Clash of Honor
date: '1993-04-01'
venue: ''
location: ''
promotion: PWA
permalink: /events/1993-04-01 - PWA Clash of Honor/
tags:
- events
matches_json: [{"number": 1, "name": "PWA World Heavyweight Championship: Kenta Kobashi vs. Big Dragon (c)", "finish": "Big Dragon beat Kenta Kobashi in 19 Min 30 Sec with a Fire Powerbomb", "rating_stars": "<span class=\"stars\">★★★¼</span>", "rating_num": 3.25, "time": "19:30"}]
---

# PWA Clash of Honor

<div class="event-header">
<div class="event-meta">
**Date:** 1993-04-01<br>
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