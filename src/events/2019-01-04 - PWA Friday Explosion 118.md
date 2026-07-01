---
layout: event.njk
title: PWA Friday Explosion 118
date: '2019-01-04'
venue: Greenwich, Connecticut
location: ''
promotion: PWA
permalink: /events/2019-01-04 - PWA Friday Explosion 118/
tags:
- events
matches_json: [{"number": 1, "name": "Mark Erickson vs. Saburo Aoki Jr.", "finish": "Mark Erickson beat Saburo Aoki Jr. in 14 Min 32 Sec with a Sniper Cross Face", "rating_stars": "<span class=\"stars\">★★★¾</span>", "rating_num": 3.75, "time": "14:32"}, {"number": 2, "name": "Royal Brawl Qualiifers: Timothy Thatcher vs. Jack Fury", "finish": "Jack Fury beat Timothy Thatcher in 12 Min 17 Sec with a Striking Lariat", "rating_stars": "<span class=\"stars\">★★★¾</span>", "rating_num": 3.75, "time": "12:17"}, {"number": 3, "name": "Foreign Fanatics vs. Mysterious Fantasticos", "finish": "Foreign Fanatics battled Mysterious Fantasticos to a  time limit draw", "rating_stars": "<span class=\"stars\">★★★★★</span>", "rating_num": 5, "time": ""}, {"number": 4, "name": "Royal Brawl Qualifiers: Red Dragon vs. Dynamite Smith", "finish": "Dynamite Smith beat Red Dragon in 16 Min 44 Sec with an O'Connor Roll German Suplex", "rating_stars": "<span class=\"stars\">★★★★½</span>", "rating_num": 4.5, "time": "16:44"}, {"number": 5, "name": "Royal Brawl Qualifiers: Diablo Blanco vs. El Canek", "finish": "Diablo Blanco beat El Canek in 20 Min 3 Sec with a Vertical Drop DDT", "rating_stars": "<span class=\"stars\">★★★★½</span>", "rating_num": 4.5, "time": "20:03"}]
---

# PWA Friday Explosion 118

<div class="event-header">
<div class="event-meta">
**Date:** 2019-01-04<br>
**Venue:** Greenwich, Connecticut<br>
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