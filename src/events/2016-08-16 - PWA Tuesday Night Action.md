---
layout: event.njk
title: PWA Tuesday Night Action
date: '2016-08-16'
venue: ''
location: ''
promotion: PWA
permalink: /events/2016-08-16 - PWA Tuesday Night Action/
tags:
- events
matches_json: [{"number": 1, "name": "Masaaki Mochizuki & Steve Corino vs. Lex Rider & The Patriot", "finish": "Masaaki Mochizuki & Steve Corino beat Lex Rider & The Patriot (Victory Roll (Mochizuki an Patriot))", "rating_stars": "<span class=\"stars\">★★★½</span>", "rating_num": 3.5, "time": ""}]
---

# PWA Tuesday Night Action

<div class="event-header">
<div class="event-meta">
**Date:** 2016-08-16<br>
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