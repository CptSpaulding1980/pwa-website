---
layout: event.njk
title: PWA Tuesday Night Action
date: '2017-09-12'
venue: ''
location: ''
promotion: PWA
permalink: /events/2017-09-12 - PWA Tuesday Night Action/
tags:
- events
matches_json: [{"number": 1, "name": "PWA 5 Star League 2017 – Final Match: Blade [12] vs. Ox Hemlock [10]", "finish": "Ox Hemlock beat Blade (Belly to Belly)", "rating_stars": "<span class=\"stars\">★★★★</span>", "rating_num": 4, "time": ""}, {"number": 2, "name": "Blue Blazer Jr. & UK Kid vs. Fantasio Fantastico & Mystery Panther", "finish": "Draw (Time Limit Draw)", "rating_stars": "<span class=\"stars\">★★★★½</span>", "rating_num": 4.5, "time": ""}]
---

# PWA Tuesday Night Action

<div class="event-header">
<div class="event-meta">
**Date:** 2017-09-12<br>
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