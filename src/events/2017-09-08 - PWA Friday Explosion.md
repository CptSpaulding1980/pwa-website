---
layout: event.njk
title: PWA Friday Explosion
date: '2017-09-08'
venue: ''
location: ''
promotion: PWA
permalink: /events/2017-09-08 - PWA Friday Explosion/
tags:
- events
matches_json: [{"number": 1, "name": "PWA 5 Star League 2017 – Bracket B Match: El Canek [5] vs. Lex Rider [4]", "finish": "El Canek beat Lex Rider (Flying Cross Body)", "rating_stars": "<span class=\"stars\">★★★★¼</span>", "rating_num": 4.25, "time": ""}, {"number": 2, "name": "PWA 5 Star League 2017 – Bracket B Match: UK Kid [6] vs. Mark Erickson [3]", "finish": "UK Kid beat Mark Erickson (Swan Dive Headbutt)", "rating_stars": "<span class=\"stars\">★★★★¼</span>", "rating_num": 4.25, "time": ""}, {"number": 3, "name": "PWA 5 Star League 2017 – Bracket A Match: Montgomery Hayes [1] vs. Blue Spider", "finish": "Montgomery Hayes beat Blue Spider (Chattanooga Cloetheline)", "rating_stars": "<span class=\"stars\">★★★★</span>", "rating_num": 4, "time": ""}]
---

# PWA Friday Explosion

<div class="event-header">
<div class="event-meta">
**Date:** 2017-09-08<br>
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