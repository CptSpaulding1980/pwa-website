---
layout: event.njk
title: PWA Friday Explosion 126
date: '2019-03-01'
venue: 1st Mariner Arena
location: Baltimore, Maryland, USA
promotion: PWA
permalink: /events/2019-03-01 - PWA Friday Explosion 126/
tags:
- events
matches_json: [{"number": 1, "name": "No Disqualification Match: El Experto vs. Macho Especial", "finish": "Macho Especial beat El Experto in 17 Min 10 Sec with a Cross Arm Fire Powerbomb", "rating_stars": "<span class=\"stars\">★★★★¼</span>", "rating_num": 4.25, "time": "17:10"}, {"number": 2, "name": "Foreign Fanatics vs. Julio Rivera, Shredder & Winston Zedd", "finish": "Jitsu  beat Julio Rivera in 4 Min 17 Sec with a K.O", "rating_stars": "<span class=\"stars\">★</span>", "rating_num": 1, "time": "4:17"}, {"number": 3, "name": "Interview Segment /w Montgomery Hayes", "finish": "Montgomery Hayes helds a promo in which he calls himself the savior of wrestling and speaks out an open challenge for clash of Honor 2019", "rating_stars": "<span class=\"stars\">★★★¾</span>", "rating_num": 3.75, "time": ""}, {"number": 4, "name": "Blue Blazer Jr. (w/The Gatekeeper) vs. Nigel Pendragon", "finish": "Blue Blazer Jr. beat Nigel Pendragon in 9 Min 58 Sec with a Moonsault Press", "rating_stars": "<span class=\"stars\">★★★½</span>", "rating_num": 3.5, "time": "9:58"}, {"number": 5, "name": "PWA International Championship: Jack Fury vs. Lex Rider (c)", "finish": "Jack Fury & WALTER battled Lex Rider to a  double KO draw", "rating_stars": "<span class=\"stars\">★★★½</span>", "rating_num": 3.5, "time": ""}]
---

# PWA Friday Explosion 126

<div class="event-header">
<div class="event-meta">
**Date:** 2019-03-01<br>
**Venue:** 1st Mariner Arena<br>
**Location:** Baltimore, Maryland, USA
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