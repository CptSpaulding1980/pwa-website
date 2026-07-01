---
layout: event.njk
title: PWA Tuesday Night Action
date: '2016-05-03'
venue: ''
location: ''
promotion: PWA
permalink: /events/2016-05-03 - PWA Tuesday Night Action/
tags:
- events
matches_json: [{"number": 1, "name": "UK Kid vs. KENTA", "finish": "Draw (Time Limit Draw)", "rating_stars": "<span class=\"stars\">★★★¾</span>", "rating_num": 3.75, "time": ""}, {"number": 2, "name": "Non Title – Best 2 out of 3 Falls Match: Blue Spider vs. Roadkill", "finish": "Blue Spider beat Roadkill (1:0 Oklahoma Stampede 17:52 2:0 Falcon Arrow Crush 5:35)", "rating_stars": "<span class=\"stars\">★★★★¼</span>", "rating_num": 4.25, "time": ""}]
---

# PWA Tuesday Night Action

<div class="event-header">
<div class="event-meta">
**Date:** 2016-05-03<br>
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