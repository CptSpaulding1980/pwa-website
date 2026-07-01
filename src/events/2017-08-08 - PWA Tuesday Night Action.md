---
layout: event.njk
title: PWA Tuesday Night Action
date: '2017-08-08'
venue: ''
location: ''
promotion: PWA
permalink: /events/2017-08-08 - PWA Tuesday Night Action/
tags:
- events
matches_json: [{"number": 1, "name": "PWA International Championship: UK Kid vs. Davey Boy Smith Jr. (c)", "finish": "Draw (Double KO (Draw))", "rating_stars": "<span class=\"stars\">★★★★</span>", "rating_num": 4, "time": ""}]
---

# PWA Tuesday Night Action

<div class="event-header">
<div class="event-meta">
**Date:** 2017-08-08<br>
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