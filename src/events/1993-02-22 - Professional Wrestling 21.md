---
layout: event.njk
title: Professional Wrestling 21
date: '1993-02-22'
venue: ''
location: ''
promotion: PWA
permalink: /events/1993-02-22 - Professional Wrestling 21/
tags:
- events
matches_json: [{"number": 1, "name": "PWA World Heavyweight Championship: Kenta Kobashi vs. Big Dragon (c)", "finish": "Time Limit Draw", "rating_stars": "<span class=\"stars\">★★★★</span>", "rating_num": 4, "time": ""}]
---

# Professional Wrestling 21

<div class="event-header">
<div class="event-meta">
**Date:** 1993-02-22<br>
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