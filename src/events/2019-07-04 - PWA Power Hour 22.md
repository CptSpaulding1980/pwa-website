---
layout: event.njk
title: PWA Power Hour 22
date: '2019-07-04'
venue: PWA Power Studio
location: Boston, Massachusetts, USA
promotion: PWA
permalink: /events/2019-07-04 - PWA Power Hour 22/
tags:
- events
matches_json: [{"number": 1, "name": "Seth Ramsey vs. Mark Erickson", "finish": "Seth Ramsey beat Mark Erickson in 20 Min 2 Sec with a Jumping DDT", "rating_stars": "<span class=\"stars\">★★★★</span>", "rating_num": 4, "time": "20:02"}, {"number": 2, "name": "Allen Hawkins vs. Salvador Sosa", "finish": "Allen Hawkins beat Salvador Sosa in 15 Min 52 Sec with a Rainmaker style V trigger", "rating_stars": "<span class=\"stars\">★★★¾</span>", "rating_num": 3.75, "time": "15:52"}, {"number": 3, "name": "Fabrizio Tiziano vs. Misterio Guerrero", "finish": "Fabrizio Tiziano beat Misterio Guerrero in 8 Min 48 Sec with a DQ", "rating_stars": "<span class=\"stars\">★★½</span>", "rating_num": 2.5, "time": "8:48"}, {"number": 4, "name": "Invasores vs. Roadkill & John Hennigan", "finish": "Invasores battled Roadkill & John Hennigan to a  double KO draw", "rating_stars": "<span class=\"stars\">★½</span>", "rating_num": 1.5, "time": ""}]
---

# PWA Power Hour 22

<div class="event-header">
<div class="event-meta">
**Date:** 2019-07-04<br>
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