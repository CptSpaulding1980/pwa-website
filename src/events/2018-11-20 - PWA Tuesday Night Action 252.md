---
layout: event.njk
title: PWA Tuesday Night Action 252
date: '2018-11-20'
venue: Unknown
location: ''
promotion: PWA
permalink: /events/2018-11-20 - PWA Tuesday Night Action 252/
tags:
- events
matches_json: [{"number": 1, "name": "Blue Blazer Jr. vs. Saburo Aoki Jr.", "finish": "Saburo Aoki Jr. beat Blue Blazer Jr. in 14 Min 21 Sec with a Swift Blade", "rating_stars": "<span class=\"stars\">★★★¼</span>", "rating_num": 3.25, "time": "14:21"}, {"number": 2, "name": "Timothy Thatcher vs. Victor Kurilenko", "finish": "Timothy Thatcher beat Victor Kurilenko in 13 Min 51 Sec with a Thatcher Stretch", "rating_stars": "<span class=\"stars\">★★★</span>", "rating_num": 3, "time": "13:51"}, {"number": 3, "name": "6-Pack Challenge for the International Title #1 Contender", "finish": "Hiroto Nakamichi beat Diablo Blanco by", "rating_stars": "<span class=\"stars\">★★★★½</span>", "rating_num": 4.5, "time": ""}, {"number": 4, "name": "Non Title Match: Keith Rowans vs. UK Kid", "finish": "UK Kid beat Keith Rowans in 12 Min 3 Sec with a British Fall", "rating_stars": "<span class=\"stars\">★★★</span>", "rating_num": 3, "time": "12:03"}]
---

# PWA Tuesday Night Action 252

<div class="event-header">
<div class="event-meta">
**Date:** 2018-11-20<br>
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