---
layout: event.njk
title: PWA Friday Explosion 113
date: '2018-11-23'
venue: Unknown
location: ''
promotion: PWA
permalink: /events/2018-11-23 - PWA Friday Explosion 113/
tags:
- events
matches_json: [{"number": 1, "name": "Avery Alexander, Red Dragon & Ray Stantz vs. Dynamite Smith, Rick Banner & Ricklon Smasher", "finish": "Red Dragon beat Rick Banner in 21 Min 4 Sec with a Front Dropkick", "rating_stars": "<span class=\"stars\">★★★¼</span>", "rating_num": 3.25, "time": "21:04"}, {"number": 2, "name": "Ox Hemlock vs. Poppa Thurgoode", "finish": "Ox Hemlock beat Poppa Thurgoode in 4 Min 52 Sec with a K.O", "rating_stars": "<span class=\"stars\">★½</span>", "rating_num": 1.5, "time": "4:52"}, {"number": 3, "name": "Montgomery Hayes vs. Tri Clops", "finish": "Montgomery Hayes beat Tri Clops in 8 Min 55 Sec with a Stomping (Stomach)", "rating_stars": "<span class=\"stars\">★★½</span>", "rating_num": 2.5, "time": "8:55"}, {"number": 4, "name": "Shoot Style Match: Timothy Thatcher vs. Victor Kurilenko", "finish": "Timothy Thatcher beat Victor Kurilenko in 1R 4 Min 23 Sec with a K.O", "rating_stars": "<span class=\"stars\">★★★¼</span>", "rating_num": 3.25, "time": "4:23"}, {"number": 5, "name": "El Experto vs. Blue Spider", "finish": "Blue Spider beat El Experto in 3 Min 9 Sec with a K.O", "rating_stars": "<span class=\"stars\">★★★¼</span>", "rating_num": 3.25, "time": "3:09"}]
---

# PWA Friday Explosion 113

<div class="event-header">
<div class="event-meta">
**Date:** 2018-11-23<br>
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