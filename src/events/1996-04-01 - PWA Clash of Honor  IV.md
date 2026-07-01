---
layout: event.njk
title: PWA Clash of Honor  IV
date: '1996-04-01'
venue: ''
location: ''
promotion: PWA
permalink: /events/1996-04-01 - PWA Clash of Honor  IV/
tags:
- events
matches_json: [{"number": 1, "name": "Blue Spider vs. Tri Clops", "finish": "Tri Clops beat Blue Spider in 18 Min 39 Sec with Tights Pulling School Boy", "rating_stars": "<span class=\"stars\">★★★★</span>", "rating_num": 4, "time": "18:39"}, {"number": 2, "name": "Ladder - PWA International Championship: Jitsu vs. Lex Rider (c)", "finish": "Lex Rider beat Jitsu in 21 Min 04 Sec by retrieving the Belt", "rating_stars": "<span class=\"stars\">★★★★¼</span>", "rating_num": 4.25, "time": "21:04"}, {"number": 3, "name": "PWA World Heavyweight Championship: Blade vs. Yokosumo Kawashi (c)", "finish": "Yokosumo Kawashi beat Blade in 17 Min 27 Sec with a Leg Drop", "rating_stars": "<span class=\"stars\">★★★¼</span>", "rating_num": 3.25, "time": "17:27"}]
---

# PWA Clash of Honor  IV

<div class="event-header">
<div class="event-meta">
**Date:** 1996-04-01<br>
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