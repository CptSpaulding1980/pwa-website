---
layout: event.njk
title: PWA Tuesday Night Action
date: '2018-01-16'
venue: ''
location: ''
promotion: PWA
permalink: /events/2018-01-16 - PWA Tuesday Night Action/
tags:
- events
matches_json: [{"number": 1, "name": "Pete Dunne vs. Timothy Thatcher", "finish": "Pete Dunne beat Timothy Thatcher (Bridge German Suplex)", "rating_stars": "<span class=\"stars\">★★★★¾</span>", "rating_num": 4.75, "time": ""}, {"number": 2, "name": "Diablo Blanco vs. Tri Clops", "finish": "Diablo Blanco beat Tri Clops (La Magistral)", "rating_stars": "<span class=\"stars\">★★★★¼</span>", "rating_num": 4.25, "time": ""}, {"number": 3, "name": "Golden Lovers (Kenny Omega & Kota Ibushi) vs. Blue Spider & Lex Rider", "finish": "Golden Lovers (Kenny Omega & Kota Ibushi) beat Blue Spider & Lex Rider (Phoenix Splash (Ibushi an Blue Spider))", "rating_stars": "<span class=\"stars\">★★★★¼</span>", "rating_num": 4.25, "time": ""}]
---

# PWA Tuesday Night Action

<div class="event-header">
<div class="event-meta">
**Date:** 2018-01-16<br>
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