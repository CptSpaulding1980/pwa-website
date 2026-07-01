---
layout: event.njk
title: PWA Friday Explosion
date: '2017-06-16'
venue: ''
location: ''
promotion: PWA
permalink: /events/2017-06-16 - PWA Friday Explosion/
tags:
- events
matches_json: [{"number": 1, "name": "PWA World Tag Team Title Tournament – Semi Final #2 (Rematch): El Canek & Grizzlor vs. Ringkampf (Timothy Thatcher & WALTER)", "finish": "Ringkampf (Timothy Thatcher & WALTER) beat El Canek & Grizzlor (Rapid Powerbomb (WALTER an Grizzlor))", "rating_stars": "<span class=\"stars\">★★★★¼</span>", "rating_num": 4.25, "time": ""}, {"number": 2, "name": "Barbed Wired Deathmatch: Eddie Edwards vs. Grizzlor", "finish": "Eddie Edwards beat Grizzlor (German Suplex)", "rating_stars": "<span class=\"stars\">★★★★</span>", "rating_num": 4, "time": ""}, {"number": 3, "name": "PWA International Championship: Mark Erickson vs. Davey Boy Smith Jr. (c)", "finish": "Davey Boy Smith Jr. beat Mark Erickson (Bulldog Bomb)", "rating_stars": "<span class=\"stars\">★★★★</span>", "rating_num": 4, "time": ""}]
---

# PWA Friday Explosion

<div class="event-header">
<div class="event-meta">
**Date:** 2017-06-16<br>
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