---
layout: event.njk
title: PWA Power Hour 17 - The Fusion
date: '2019-05-30'
venue: PWA Power Studio
location: Boston, Massachusetts, USA
promotion: PWA
permalink: /events/2019-05-30 - PWA Power Hour 17 - The Fusion/
tags:
- events
matches_json: [{"number": 1, "name": "Casper Winkel & Brutes (Jack Fury & Skullface Killah) vs. Jean Wilson, Ricklon Smasher & Mark Erickson", "finish": "Jack Fury beat Ricklon Smasher in 12 Min 22 Sec with a K.O", "rating_stars": "<span class=\"stars\">DUD</span>", "rating_num": 0, "time": "12:22"}, {"number": 2, "name": "European Rules: Julio Rivera vs. Ray Stantz", "finish": "Ray Stantz beat Julio Rivera in 2R 1 Min 2 Sec with a K.O", "rating_stars": "<span class=\"stars\">★★½</span>", "rating_num": 2.5, "time": "1:02"}, {"number": 3, "name": "PWA International Championship: Jonathan Gresham vs. Roadkill (c)", "finish": "Roadkill beat Jonathan Gresham in 15 Min 1 Sec with a K.O", "rating_stars": "<span class=\"stars\">★★★</span>", "rating_num": 3, "time": "15:01"}]
---

# PWA Power Hour 17 - The Fusion

<div class="event-header">
<div class="event-meta">
**Date:** 2019-05-30<br>
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