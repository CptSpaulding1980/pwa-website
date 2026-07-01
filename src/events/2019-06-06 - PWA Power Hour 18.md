---
layout: event.njk
title: PWA Power Hour 18
date: '2019-06-06'
venue: PWA Power Studio
location: Boston, Massachusetts, USA
promotion: PWA
permalink: /events/2019-06-06 - PWA Power Hour 18/
tags:
- events
matches_json: [{"number": 1, "name": "Santana Family vs. Julio Rivera & Salvador Sosa", "finish": "Santana Family battled Julio Rivera & Salvador Sosa to a  time limit draw", "rating_stars": "<span class=\"stars\">DUD</span>", "rating_num": 0, "time": ""}, {"number": 2, "name": "Jonathan Gresham vs. Dynamite Smith", "finish": "Jonathan Gresham battled Dynamite Smith to a  time limit draw", "rating_stars": "<span class=\"stars\">★★★¾</span>", "rating_num": 3.75, "time": ""}, {"number": 3, "name": "Casper Winkel vs. Mark Erickson", "finish": "Mark Erickson beat Casper Winkel in 10 Min 25 Sec with a DQ", "rating_stars": "<span class=\"stars\">★★★¾</span>", "rating_num": 3.75, "time": "10:25"}, {"number": 4, "name": "Chelsea Grin vs. Jack Gold", "finish": "Jack Gold beat Chelsea Grin in 12 Min 6 Sec with a Frankensteiner", "rating_stars": "<span class=\"stars\">★★★★</span>", "rating_num": 4, "time": "12:06"}, {"number": 5, "name": "PWA International Championship: Daniel Garcia vs. Roadkill (c)", "finish": "Roadkill beat Daniel Garcia in 8 Min 56 Sec with a Side Clutch", "rating_stars": "<span class=\"stars\">★★★¼</span>", "rating_num": 3.25, "time": "8:56"}]
---

# PWA Power Hour 18

<div class="event-header">
<div class="event-meta">
**Date:** 2019-06-06<br>
**Venue:** PWA Power Studio<br>
**Location:** Boston, Massachusetts, USA
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