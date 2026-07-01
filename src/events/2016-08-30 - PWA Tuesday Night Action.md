---
layout: event.njk
title: PWA Tuesday Night Action
date: '2016-08-30'
venue: ''
location: ''
promotion: PWA
permalink: /events/2016-08-30 - PWA Tuesday Night Action/
tags:
- events
matches_json: [{"number": 1, "name": "Best 2 out of 3 Falls Match: Masaaki Mochizuki & Steve Corino & UK Kid & Dr. Wagner Jr. vs. Lex Rider & The Patriot & Davey Richards & Blue Spider", "finish": "Lex Rider & The Patriot & Davey Richards & Blue Spider beat Masaaki Mochizuki & Steve Corino & UK Kid & Dr. Wagner Jr. (0:1 Straight Arm Bar (Richards an Corino) 28:07 0:2 Cross Style STF (Richards an Wagner) 15:29)", "rating_stars": "<span class=\"stars\">★★★★</span>", "rating_num": 4, "time": ""}]
---

# PWA Tuesday Night Action

<div class="event-header">
<div class="event-meta">
**Date:** 2016-08-30<br>
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