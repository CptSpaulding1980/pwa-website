---
layout: event.njk
title: PWA Power Hour 4
date: '2019-02-21'
venue: PWA Power Studio
location: Boston, Massachusetts, USA
promotion: PWA
permalink: /events/2019-02-21 - PWA Power Hour 4/
tags:
- events
matches_json: [{"number": 1, "name": "Ray Stantz vs. Spitfire", "finish": "Spitfire beat Ray Stantz in 9 Min 55 Sec with a Flying Cross Armbreaker", "rating_stars": "<span class=\"stars\">★★★¼</span>", "rating_num": 3.25, "time": "9:55"}, {"number": 2, "name": "Jitsu vs. Mystery Panther", "finish": "Jitsu  beat Mystery Panther in 7 Min 26 Sec with a Brainbuster", "rating_stars": "<span class=\"stars\">★★★½</span>", "rating_num": 3.5, "time": "7:26"}, {"number": 3, "name": "Chelsea Grin vs. Felix Santana III", "finish": "Felix Santana III beat Chelsea Grin in 10 Min 52 Sec with a La Esparda", "rating_stars": "<span class=\"stars\">★★★★½</span>", "rating_num": 4.5, "time": "10:52"}]
---

# PWA Power Hour 4

<div class="event-header">
<div class="event-meta">
**Date:** 2019-02-21<br>
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