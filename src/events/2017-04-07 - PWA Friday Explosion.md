---
layout: event.njk
title: PWA Friday Explosion
date: '2017-04-07'
venue: ''
location: ''
promotion: PWA
permalink: /events/2017-04-07 - PWA Friday Explosion/
tags:
- events
matches_json: [{"number": 1, "name": "Alberto El Patron & Cody Rhodes & Kenny Omega & Jitsu vs. Blue Spider & Fred Balentine & Mark Erickson & Davey Boy Smith Jr.", "finish": "Blue Spider & Fred Balentine & Mark Erickson & Davey Boy Smith Jr. beat Alberto El Patron & Cody Rhodes & Kenny Omega & Jitsu (Omnoplata Crossface von Erickson an Omega)", "rating_stars": "<span class=\"stars\">★★★★</span>", "rating_num": 4, "time": ""}]
---

# PWA Friday Explosion

<div class="event-header">
<div class="event-meta">
**Date:** 2017-04-07<br>
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