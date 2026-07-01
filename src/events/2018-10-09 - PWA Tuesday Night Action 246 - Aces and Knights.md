---
layout: event.njk
title: PWA Tuesday Night Action 246 - Aces and Knights
date: '2018-10-09'
venue: Las Vegas, NV
location: ''
promotion: PWA
permalink: /events/2018-10-09 - PWA Tuesday Night Action 246 - Aces and Knights/
tags:
- events
matches_json: [{"number": 1, "name": "Shredder vs. El Experto", "finish": "El Experto beat Shredder in 3 Min 6 Sec with an Agarre Perfecto", "rating_stars": "<span class=\"stars\">DUD</span>", "rating_num": 0, "time": "3:06"}, {"number": 2, "name": "Masked Lucha Alliance vs. Jack Fury & Rampage Rage", "finish": "Rampage Rage beat Cobra III in 2 Min 58 Sec with a Splash of Rage", "rating_stars": "<span class=\"stars\">DUD</span>", "rating_num": 0, "time": "2:58"}, {"number": 3, "name": "Veteran Veteran Devastators vs. Tri Clops & Roadkill", "finish": "Roadkill beat Blue Blazer Jr. in 15 Min 45 Sec with a Reverse Figure 4", "rating_stars": "<span class=\"stars\">★★★★¼</span>", "rating_num": 4.25, "time": "15:45"}, {"number": 4, "name": "Ray Stantz & Hiroto Nakamichi vs. Santana Family", "finish": "Ray Stantz beat Felix Santana III in 12 Min 9 Sec with an Orange Crush", "rating_stars": "<span class=\"stars\">★★★½</span>", "rating_num": 3.5, "time": "12:09"}, {"number": 5, "name": "PWA International Championship: Montgomery Hayes vs. Lex Rider (c)", "finish": "Lex Rider beat Montgomery Hayes in 10 Min 4 Sec with a Vaulting Frog Splash", "rating_stars": "<span class=\"stars\">★★★</span>", "rating_num": 3, "time": "10:04"}]
---

# PWA Tuesday Night Action 246 - Aces and Knights

<div class="event-header">
<div class="event-meta">
**Date:** 2018-10-09<br>
**Venue:** Las Vegas, NV<br>
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