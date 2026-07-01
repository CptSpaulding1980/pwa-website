---
layout: event.njk
title: PWA Thanksgiving Thunder 2018 - Night 2
date: '2018-11-26'
venue: East Rutherford, New Jersey
location: ''
promotion: PWA
permalink: /events/2018-11-26 - PWA Thanksgiving Thunder 2018 - Night 2/
tags:
- events
matches_json: [{"number": 1, "name": "Ray Stantz vs. Saburo Aoki Jr.", "finish": "Saburo Aoki Jr. beat Ray Stantz in 13 Min 36 Sec with an El Es Culero", "rating_stars": "<span class=\"stars\">★★★¾</span>", "rating_num": 3.75, "time": "13:36"}, {"number": 2, "name": "Gauntlet Match: Veteran Veteran Devastators & Mackenzie Bergeron vs. Dynamite Smith, Tri Clops, Jean Wilson & Fred Balentine", "finish": "Montgomery Hayes beat Fred Balentine in 40 Min 3 Sec with an Ankle Hold", "rating_stars": "<span class=\"stars\">★★★¼</span>", "rating_num": 3.25, "time": "40:03"}, {"number": 3, "name": "Best 2 out of 3 Falls - Submission - PWA World Heavyweight Championship: Fabrizio Tiziano vs. UK Kid (c)", "finish": "UK Kid beat Fabrizio Tiziano in 50 Min 52 Sec with a Camel Clutch", "rating_stars": "<span class=\"stars\">★★★★¾</span>", "rating_num": 4.75, "time": "50:52"}]
---

# PWA Thanksgiving Thunder 2018 - Night 2

<div class="event-header">
<div class="event-meta">
**Date:** 2018-11-26<br>
**Venue:** East Rutherford, New Jersey<br>
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