---
layout: event.njk
title: PWA Tuesday Night Action 260 - Ban the Cam
date: '2019-01-22'
venue: Charlotte, North Carolina
location: ''
promotion: PWA
permalink: /events/2019-01-22 - PWA Tuesday Night Action 260 - Ban the Cam/
tags:
- events
matches_json: [{"number": 1, "name": "Brian Pillman Jr. & Teddy Hart vs. Mysterious Fantasticos", "finish": "Mystery Panther beat Teddy Hart in 19 Min 40 Sec with a La Magistral", "rating_stars": "<span class=\"stars\">★★★¾</span>", "rating_num": 3.75, "time": "19:40"}, {"number": 2, "name": "Chelsea Grin vs. Dynamite Smith", "finish": "Dynamite Smith beat Chelsea Grin in 16 Min 20 Sec with a School Boy", "rating_stars": "<span class=\"stars\">★★★★</span>", "rating_num": 4, "time": "16:20"}, {"number": 3, "name": "UWFI Style Match: Ray Stantz vs. Timothy Thatcher", "finish": "Timothy Thatcher beat Ray Stantz in 9 Min 19 Sec with a K.O", "rating_stars": "<span class=\"stars\">★★★½</span>", "rating_num": 3.5, "time": "9:19"}, {"number": 4, "name": "Golden Grappler & Allen Hawkins vs. Blue Demon Jr. & Macho Especial", "finish": "Golden Grappler & Allen Hawkins battled Blue Demon Jr. & Macho Especial to a  time limit draw", "rating_stars": "<span class=\"stars\">★★★¼</span>", "rating_num": 3.25, "time": ""}, {"number": 5, "name": "Grizzlor vs. Rick Banner", "finish": "Rick Banner beat Grizzlor  in 26 Min 40 Sec with a German Suplex", "rating_stars": "<span class=\"stars\">★★★★★</span>", "rating_num": 5, "time": "26:40"}]
---

# PWA Tuesday Night Action 260 - Ban the Cam

<div class="event-header">
<div class="event-meta">
**Date:** 2019-01-22<br>
**Venue:** Charlotte, North Carolina<br>
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