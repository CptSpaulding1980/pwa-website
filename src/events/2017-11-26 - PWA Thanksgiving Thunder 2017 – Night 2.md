---
layout: event.njk
title: PWA Thanksgiving Thunder 2017 – Night 2
date: '2017-11-26'
venue: ''
location: ''
promotion: PWA
permalink: /events/2017-11-26 - PWA Thanksgiving Thunder 2017 – Night 2/
tags:
- events
matches_json: [{"number": 1, "name": "Keith Owens vs. Fantasio Fantastico", "finish": "Fantasio Fantastico beat Keith Owens (Silent Clutch)", "rating_stars": "<span class=\"stars\">★★★★¼</span>", "rating_num": 4.25, "time": ""}, {"number": 2, "name": "Yokosumo Kawashi vs. Mark Erickson", "finish": "Mark Erickson beat Yokosumo Kawashi (Zero Fighter Kick Rush)", "rating_stars": "<span class=\"stars\">★★★</span>", "rating_num": 3, "time": ""}, {"number": 3, "name": "Marty Scurll & Matt Jackson & Nick Jackson & Hangman Page vs. Cobra & El Canek & The Patriot & Tri Clops", "finish": "Cobra & El Canek & The Patriot & Tri Clops beat Marty Scurll & Matt Jackson & Nick Jackson & Hangman Page (Flying Body Attack (El Canek an Matt Jackson))", "rating_stars": "<span class=\"stars\">★★★★</span>", "rating_num": 4, "time": ""}, {"number": 4, "name": "Kenny Omega vs. Blue Spider", "finish": "Blue Spider won (Shooting Star Press)", "rating_stars": "<span class=\"stars\">★★★★¾</span>", "rating_num": 4.75, "time": ""}, {"number": 5, "name": "PWA World Heavyweight Championship: Minoru Suzuki vs. Roadkill (c)", "finish": "Roadkill beat Minoru Suzuki (Road Diving Elbow Drop)", "rating_stars": "<span class=\"stars\">★★★★</span>", "rating_num": 4, "time": ""}]
---

# PWA Thanksgiving Thunder 2017 – Night 2

<div class="event-header">
<div class="event-meta">
**Date:** 2017-11-26<br>
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