---
layout: event.njk
title: PWA Tuesday Night Action 282 - Night of the Necro Dancer
date: '2019-06-25'
venue: PWA Capcom Arena
location: Boston, Massachusetts, USA
promotion: PWA
permalink: /events/2019-06-25 - PWA Tuesday Night Action 282 - Night of the Necro
  Dancer/
tags:
- events
matches_json: [{"number": 1, "name": "Avery Alexander vs. Mark Erickson", "finish": "Avery Alexander beat Mark Erickson in 9 Min 29 Sec with a RING OUT", "rating_stars": "<span class=\"stars\">★★★½</span>", "rating_num": 3.5, "time": "9:29"}, {"number": 2, "name": "6 Men Tornado: Brutes vs. Jean Wilson, Ricklon Smasher & Tri Clops", "finish": "Jack Fury beat Tri Clops in 7 Min 57 Sec with a Scissors Texas Clover Clutch", "rating_stars": "<span class=\"stars\">★★</span>", "rating_num": 2, "time": "7:57"}, {"number": 3, "name": "No Holds Barred: Ox Hemlock vs. Fred Balentine (w/Lex Rider)", "finish": "Ox Hemlock beat Fred Balentine in 8 Min 16 Sec with a Turn Belly-to-Belly", "rating_stars": "<span class=\"stars\">★★½</span>", "rating_num": 2.5, "time": "8:16"}]
---

# PWA Tuesday Night Action 282 - Night of the Necro Dancer

<div class="event-header">
<div class="event-meta">
**Date:** 2019-06-25<br>
**Venue:** PWA Capcom Arena<br>
**Location:** Boston, Massachusetts, USA
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