---
layout: event.njk
title: PWA Tuesday Night Action
date: '2016-03-29'
venue: ''
location: ''
promotion: PWA
permalink: /events/2016-03-29 - PWA Tuesday Night Action/
tags:
- events
matches_json: [{"number": 1, "name": "Non Title Match: Blue Spider vs. UK Kid (c)", "finish": "Blue Spider beat UK Kid (Roll Up)", "rating_stars": "<span class=\"stars\">★★★¾</span>", "rating_num": 3.75, "time": ""}]
---

# PWA Tuesday Night Action

<div class="event-header">
<div class="event-meta">
**Date:** 2016-03-29<br>
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