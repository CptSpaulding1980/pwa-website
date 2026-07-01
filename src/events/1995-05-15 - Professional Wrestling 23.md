---
layout: event.njk
title: Professional Wrestling 23
date: '1995-05-15'
venue: ''
location: ''
promotion: PWA
permalink: /events/1995-05-15 - Professional Wrestling 23/
tags:
- events
matches_json: [{"number": 1, "name": "PWA World Heavyweight Championship: Grizzlor vs. Fred Balentine (c)", "finish": "Grizzlor beat Fred Balentine in 22 Min 09 Sec after Interference by Blade with a Pinfall  ", "rating_stars": "<span class=\"stars\">★★★½</span>", "rating_num": 3.5, "time": "22:09"}]
---

# Professional Wrestling 23

<div class="event-header">
<div class="event-meta">
**Date:** 1995-05-15<br>
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