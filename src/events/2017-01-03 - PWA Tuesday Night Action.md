---
layout: event.njk
title: PWA Tuesday Night Action
date: '2017-01-03'
venue: ''
location: ''
promotion: PWA
permalink: /events/2017-01-03 - PWA Tuesday Night Action/
tags:
- events
matches_json: [{"number": 1, "name": "PWA World Title #1 Contender Battle Royal Qualifiying: Mark Erickson vs. Roderick Strong", "finish": "Mark Erickson beat Roderick Strong (Falcon Arrow)", "rating_stars": "<span class=\"stars\">★★★½</span>", "rating_num": 3.5, "time": ""}, {"number": 2, "name": "PWA World Title #1 Contender Battle Royal Qualifiying: Snake King vs. Kyle O'Reilly", "finish": "Snake King beat Kyle O'Reilly (Outlaws Edge)", "rating_stars": "<span class=\"stars\">★★★½</span>", "rating_num": 3.5, "time": ""}]
---

# PWA Tuesday Night Action

<div class="event-header">
<div class="event-meta">
**Date:** 2017-01-03<br>
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