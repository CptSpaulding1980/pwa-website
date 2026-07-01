---
layout: event.njk
title: PWA Tuesday Night Action 245 - Fall Brawl
date: '2018-10-02'
venue: Unknown
location: ''
promotion: PWA
permalink: /events/2018-10-02 - PWA Tuesday Night Action 245 - Fall Brawl/
tags:
- events
matches_json: [{"number": 1, "name": "Dynamite Smith & Ricklon Smasher vs. Golden Grappler & Ox Hemlock", "finish": "Dynamite Smith & Ricklon Smasher battled Golden Grappler & Ox Hemlock to a  time limit draw", "rating_stars": "<span class=\"stars\">★★★★</span>", "rating_num": 4, "time": ""}, {"number": 2, "name": "Seth Ramsey vs. Red Dragon", "finish": "Red Dragon beat Seth Ramsey in 2 Min 1 Sec with a Vaulting Frog Splash", "rating_stars": "<span class=\"stars\">★</span>", "rating_num": 1, "time": "2:01"}, {"number": 3, "name": "El Experto & L.A. Park vs. Mysterious Fantasticos", "finish": "El Experto beat Fantasio Fantastico in 29 Min 45 Sec with a Schoolboy Suplex", "rating_stars": "<span class=\"stars\">★★★★½</span>", "rating_num": 4.5, "time": "29:45"}, {"number": 4, "name": "Dragon Lee & Mistico vs. Ringkampf", "finish": "WALTER beat Dragon Lee in 35 Min 51 Sec with a Powerbomb Whip", "rating_stars": "<span class=\"stars\">★★★★¾</span>", "rating_num": 4.75, "time": "35:51"}, {"number": 5, "name": "Veteran Veteran Devastators vs. Lex Rider, Roadkill & UK Kid", "finish": "Montgomery Hayes beat Lex Rider in 17 Min 40 Sec with a Pump Handle Slam", "rating_stars": "<span class=\"stars\">★★★★½</span>", "rating_num": 4.5, "time": "17:40"}]
---

# PWA Tuesday Night Action 245 - Fall Brawl

<div class="event-header">
<div class="event-meta">
**Date:** 2018-10-02<br>
**Venue:** Unknown<br>
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