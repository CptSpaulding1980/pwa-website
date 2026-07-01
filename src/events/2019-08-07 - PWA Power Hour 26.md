---
layout: event.njk
title: PWA Power Hour 26
date: '2019-08-07'
venue: PWA Power Studio
location: Boston, Massachusetts, USA
promotion: PWA
permalink: /events/2019-08-07 - PWA Power Hour 26/
tags:
- events
matches_json: [{"number": 1, "name": "Blake Twins & Mackenzie Bergeron vs. Jack Gold, Masked Maniac IV & Spitfire", "finish": "Elias Blake, Sammy Blake, & Mackenzie Bergeron battled Jack Gold,  Masked Maniac IV, & Spitfire to a  time limit draw", "rating_stars": "<span class=\"stars\">★★★½</span>", "rating_num": 3.5, "time": ""}, {"number": 2, "name": "Bran Czlimovic vs. Seth Ramsey", "finish": "Bran Czlimovic beat Seth Ramsey in 14 Min 42 Sec with a Spear", "rating_stars": "<span class=\"stars\">★★★¾</span>", "rating_num": 3.75, "time": "14:42"}, {"number": 3, "name": "PWA Junior Heavyweight Championship: Fantasio Fantastico vs. Blue Blazer Jr. (c)", "finish": "Fantasio Fantastico beat Blue Blazer Jr. in 27 Min 18 Sec with a Sniper Cross Face", "rating_stars": "<span class=\"stars\">★★★★</span>", "rating_num": 4, "time": "27:18"}]
---

# PWA Power Hour 26

<div class="event-header">
<div class="event-meta">
**Date:** 2019-08-07<br>
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