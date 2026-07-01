---
layout: event.njk
title: PWA Tuesday Night Action 242 - Curse of the Dragon
date: '2018-09-11'
venue: Unknown
location: ''
promotion: PWA
permalink: /events/2018-09-11 - PWA Tuesday Night Action 242 - Curse of the Dragon/
tags:
- events
matches_json: [{"number": 1, "name": "Ray Stantz vs. Poppa Thurgoode", "finish": "Poppa Thurgoode beat Ray Stantz in 12 Min 39 Sec with a The Jive Soul Flow", "rating_stars": "<span class=\"stars\">★★★★</span>", "rating_num": 4, "time": "12:39"}, {"number": 2, "name": "5 Star League - Semi Finals: Super Delfin vs. Macho Especial", "finish": "Macho Especial beat Super Delfin in 10 Min 39 Sec with a Super Body Blow", "rating_stars": "<span class=\"stars\">★★★★¼</span>", "rating_num": 4.25, "time": "10:39"}, {"number": 3, "name": "Veteran Veteran Devastators vs. Jean Wilson & Tri Clops", "finish": "Keith Rowans beat Tri Clops in 8 Min 47 Sec with a K.O", "rating_stars": "<span class=\"stars\">★★★</span>", "rating_num": 3, "time": "8:47"}, {"number": 4, "name": "PWA World Heavyweight Title #1 Contender: Kenny Omega vs. Zack Sabre Jr.", "finish": "Kenny Omega beat Zack Sabre Jr. in 13 Min 37 Sec with a K.O", "rating_stars": "<span class=\"stars\">★★★¾</span>", "rating_num": 3.75, "time": "13:37"}]
---

# PWA Tuesday Night Action 242 - Curse of the Dragon

<div class="event-header">
<div class="event-meta">
**Date:** 2018-09-11<br>
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