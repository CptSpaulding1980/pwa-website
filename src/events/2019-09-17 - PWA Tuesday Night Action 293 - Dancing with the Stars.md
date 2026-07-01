---
layout: event.njk
title: PWA Tuesday Night Action 293 - Dancing with the Stars
date: '2019-09-17'
venue: PWA Capcom Arena
location: Boston, Massachusetts, USA
promotion: PWA
permalink: /events/2019-09-17 - PWA Tuesday Night Action 293 - Dancing with the Stars/
tags:
- events
matches_json: [{"number": 1, "name": "Felix Santana Jr. vs. Mystery Panther", "finish": "Felix Santana Jr. beat Mystery Panther in 29 Min 50 Sec with a Romero Chin Lock", "rating_stars": "<span class=\"stars\">★★★★½</span>", "rating_num": 4.5, "time": "29:50"}, {"number": 2, "name": "Bran Czlimovic, Salvador Sosa & Seth Ramsey vs. Jack Gold, Mark Erickson & Spitfire", "finish": "Mark Erickson beat Salvador Sosa in 12 Min 56 Sec with an Omoplata Crossface", "rating_stars": "<span class=\"stars\">★★★★</span>", "rating_num": 4, "time": "12:56"}, {"number": 3, "name": "Non Title Match: Allen Hawkins & Saburo Aoki Jr. vs. Cobra III & Macho Especial", "finish": "Allen Hawkins & Saburo Aoki Jr. battled Cobra III & Macho Especial to a  time limit draw", "rating_stars": "<span class=\"stars\">★★★½</span>", "rating_num": 3.5, "time": ""}, {"number": 4, "name": "BUSHI vs. UK Kid", "finish": "UK Kid beat BUSHI in 35 Min 39 Sec with a RING OUT", "rating_stars": "<span class=\"stars\">★★★¾</span>", "rating_num": 3.75, "time": "35:39"}]
---

# PWA Tuesday Night Action 293 - Dancing with the Stars

<div class="event-header">
<div class="event-meta">
**Date:** 2019-09-17<br>
**Venue:** PWA Capcom Arena<br>
**Location:** Boston, Massachusetts, USA
</div>
<img src="/pwa-website/img/posters/2019-09-17 - PWA Tuesday Night Action 293 - Dancing with the Stars.png" class="event-poster" alt="Poster">
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