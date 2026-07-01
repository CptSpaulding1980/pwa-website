---
layout: event.njk
title: PWA Tuesday Night Action
date: '2017-03-21'
venue: ''
location: ''
promotion: PWA
permalink: /events/2017-03-21 - PWA Tuesday Night Action/
tags:
- events
matches_json: [{"number": 1, "name": "Cody Rhodes vs. Fred Balentine", "finish": "Fred Balentine beat Cody Rhodes (Sledgehammer)", "rating_stars": "<span class=\"stars\">★★★¾</span>", "rating_num": 3.75, "time": ""}, {"number": 2, "name": "PWA International Title Tournament Quarter Final: Michael Elgin vs. Tri Clops", "finish": "Michael Elgin beat Tri Clops (Fallaway Slam)", "rating_stars": "<span class=\"stars\">★★★★¼</span>", "rating_num": 4.25, "time": ""}]
---

# PWA Tuesday Night Action

<div class="event-header">
<div class="event-meta">
**Date:** 2017-03-21<br>
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