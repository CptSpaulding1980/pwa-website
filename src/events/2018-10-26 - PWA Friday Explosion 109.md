---
layout: event.njk
title: PWA Friday Explosion 109
date: '2018-10-26'
venue: Unknown
location: ''
promotion: PWA
permalink: /events/2018-10-26 - PWA Friday Explosion 109/
tags:
- events
matches_json: [{"number": 1, "name": "Saburo Aoki Jr. vs. Hiroto Nakamichi", "finish": "Saburo Aoki Jr. beat Hiroto Nakamichi in 19 Min 43 Sec with a Swift Blade", "rating_stars": "<span class=\"stars\">★★★★¾</span>", "rating_num": 4.75, "time": "19:43"}, {"number": 2, "name": "Avery Alexander vs. Winston Zedd", "finish": "Avery Alexander beat Winston Zedd in 1 Min 23 Sec with a Double Knee Stomach Crusher", "rating_stars": "<span class=\"stars\">★½</span>", "rating_num": 1.5, "time": "1:23"}, {"number": 3, "name": "Montgomery Hayes vs. Cobra ", "finish": "Montgomery Hayes beat Cobra  in 2 Min 29 Sec with a Pump Handle Slam", "rating_stars": "<span class=\"stars\">★½</span>", "rating_num": 1.5, "time": "2:29"}, {"number": 4, "name": "Yokosumo Kawashi vs. Poppa Thurgoode", "finish": "Poppa Thurgoode beat Yokosumo Kawashi in 17 Min 8 Sec with a K.O", "rating_stars": "<span class=\"stars\">★★★★</span>", "rating_num": 4, "time": "17:08"}, {"number": 5, "name": "PWA Jr. Heavyweight #1 Contender: Mark Erickson vs. Jushin Liger", "finish": "Mark Erickson battled Jushin Liger to a  time limit draw", "rating_stars": "<span class=\"stars\">★★★★¼</span>", "rating_num": 4.25, "time": ""}]
---

# PWA Friday Explosion 109

<div class="event-header">
<div class="event-meta">
**Date:** 2018-10-26<br>
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