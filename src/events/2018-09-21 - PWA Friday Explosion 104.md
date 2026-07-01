---
layout: event.njk
title: PWA Friday Explosion 104
date: '2018-09-21'
venue: Unknown
location: ''
promotion: PWA
permalink: /events/2018-09-21 - PWA Friday Explosion 104/
tags:
- events
matches_json: [{"number": 1, "name": "Montgomery Hayes (w/Veteran Veteran Devastators) vs. The Patriot (W/ Tri Clops & UK Kid)", "finish": "Montgomery Hayes beat The Patriot in 7 Min 21 Sec with a Pump Handle Slam", "rating_stars": "<span class=\"stars\">★½</span>", "rating_num": 1.5, "time": "7:21"}, {"number": 2, "name": "PWA Jr. Heavyweight Title #1 Contender Elimination Match", "finish": "KUSHIDA  beat Theobold Lovecraft by", "rating_stars": "<span class=\"stars\">★★★★★</span>", "rating_num": 5, "time": ""}]
---

# PWA Friday Explosion 104

<div class="event-header">
<div class="event-meta">
**Date:** 2018-09-21<br>
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