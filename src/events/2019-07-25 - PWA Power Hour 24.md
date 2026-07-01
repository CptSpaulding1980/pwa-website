---
layout: event.njk
title: PWA Power Hour 24
date: '2019-07-25'
venue: PWA Power Studio
location: Boston, Massachusetts, USA
promotion: PWA
permalink: /events/2019-07-25 - PWA Power Hour 24/
tags:
- events
matches_json: [{"number": 1, "name": "Nigel Pendragon vs. Winston Zedd", "finish": "Nigel Pendragon beat Winston Zedd in 18 Min 11 Sec with an AH (S) 6", "rating_stars": "<span class=\"stars\">★★</span>", "rating_num": 2, "time": "18:11"}, {"number": 2, "name": "Jack Gold & Spitfire vs. Blake Twins", "finish": "Jack Gold & Spitfire battled Blake Twins to a  time limit draw", "rating_stars": "<span class=\"stars\">★★★¼</span>", "rating_num": 3.25, "time": ""}, {"number": 3, "name": "Seth Ramsey vs. Dynamite Smith", "finish": "Dynamite Smith beat Seth Ramsey in 17 Min 3 Sec with an O'Connor Roll German Suplex", "rating_stars": "<span class=\"stars\">★★★¾</span>", "rating_num": 3.75, "time": "17:03"}, {"number": 4, "name": "Allen Hawkins & Golden Grappler vs. Saburo Aoki Jr. & Salvador Sosa", "finish": "Golden Grappler beat Saburo Aoki Jr. in 23 Min 41 Sec with a The Golden Triangle", "rating_stars": "<span class=\"stars\">★★★¾</span>", "rating_num": 3.75, "time": "23:41"}, {"number": 5, "name": "Fantasio Fantastico vs. Zack Sabre Jr.", "finish": "Zack Sabre Jr. beat Fantasio Fantastico in 10 Min 23 Sec with a Flying Octopus Hold", "rating_stars": "<span class=\"stars\">★★★¼</span>", "rating_num": 3.25, "time": "10:23"}]
---

# PWA Power Hour 24

<div class="event-header">
<div class="event-meta">
**Date:** 2019-07-25<br>
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