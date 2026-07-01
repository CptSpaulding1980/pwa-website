---
layout: event.njk
title: PWA Friday Explosion
date: '2017-05-19'
venue: ''
location: ''
promotion: PWA
permalink: /events/2017-05-19 - PWA Friday Explosion/
tags:
- events
matches_json: [{"number": 1, "name": "King of the Ring – Second Round: Zack Sabre Jr. vs. Blue Blazer Jr.", "finish": "Zack Sabre Jr. beat Blue Blazer Jr. (Roll Up)", "rating_stars": "<span class=\"stars\">★★★★½</span>", "rating_num": 4.5, "time": ""}, {"number": 2, "name": "King of the Ring – Second Round: Fred Balentine vs. Tri Clops", "finish": "Fred Balentine won (Dynamite Punch Rush)", "rating_stars": "<span class=\"stars\">★★★★</span>", "rating_num": 4, "time": ""}, {"number": 3, "name": "Fatal 4 Way Match - PWA World Heavyweight Championship: Jack Swagger vs. Mark Erickson vs. Roadkill vs. Lex Rider (c)", "finish": "Jack Swagger won a Fatal Four Way Match - Eliminations: Rider by Roadkill (Small Package Hold 11:34) Erickson by Swagger (Ankle Lock 12:43) Roadkill by Swagger (Gutwrench Powerbomb 21:16)", "rating_stars": "<span class=\"stars\">★★★¾</span>", "rating_num": 3.75, "time": ""}]
---

# PWA Friday Explosion

<div class="event-header">
<div class="event-meta">
**Date:** 2017-05-19<br>
**Venue:** <br>
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