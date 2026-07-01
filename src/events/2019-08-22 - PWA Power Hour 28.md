---
layout: event.njk
title: PWA Power Hour 28
date: '2019-08-22'
venue: PWA Power Studio
location: Boston, Massachusetts, USA
promotion: PWA
permalink: /events/2019-08-22 - PWA Power Hour 28/
tags:
- events
matches_json: [{"number": 1, "name": "Bran Czlimovic vs. Jack Gold", "finish": "Bran Czlimovic battled Jack Gold to a  time limit draw", "rating_stars": "<span class=\"stars\">★★★</span>", "rating_num": 3, "time": ""}, {"number": 2, "name": "Best 2 out of 3 Falls Submission - PWA Junior Heavyweight Championship: Fantasio Fantastico vs. Zack Sabre Jr. (c)", "finish": "Zack Sabre Jr. beat Fantasio Fantastico in 11 Min 11 Sec with an Omoplata Arm Lock C", "rating_stars": "<span class=\"stars\">★★★¼</span>", "rating_num": 3.25, "time": "11:11"}]
---

# PWA Power Hour 28

<div class="event-header">
<div class="event-meta">
**Date:** 2019-08-22<br>
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