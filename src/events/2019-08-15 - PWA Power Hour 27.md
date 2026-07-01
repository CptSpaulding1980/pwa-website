---
layout: event.njk
title: PWA Power Hour 27
date: '2019-08-15'
venue: PWA Power Studio
location: Boston, Massachusetts, USA
promotion: PWA
permalink: /events/2019-08-15 - PWA Power Hour 27/
tags:
- events
matches_json: [{"number": 1, "name": "Best 2 out of 3 Falls - Blake Twins & Mackenzie Bergeron vs. Jack Gold, Masked Maniac IV & Spitfire", "finish": "Masked Maniac IV beat Elias Blake in 10 Min 39 Sec with a Small Package Hold", "rating_stars": "<span class=\"stars\">★★★¼</span>", "rating_num": 3.25, "time": "10:39"}, {"number": 2, "name": "Bran Czlimovic vs. Mark Erickson", "finish": "Mark Erickson beat Bran Czlimovic in 14 Min 26 Sec with a Sniper Cross Face", "rating_stars": "<span class=\"stars\">★★★★¼</span>", "rating_num": 4.25, "time": "14:26"}, {"number": 3, "name": "PWA Junior Heavyweight Championship: Zack Sabre Jr. vs. Fantasio Fantastico (c)", "finish": "Zack Sabre Jr. beat Fantasio Fantastico in 13 Min 36 Sec with an European Clutch", "rating_stars": "<span class=\"stars\">★★★¾</span>", "rating_num": 3.75, "time": "13:36"}]
---

# PWA Power Hour 27

<div class="event-header">
<div class="event-meta">
**Date:** 2019-08-15<br>
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