---
layout: event.njk
title: PWA Friday Explosion 102 - PWA 5 Star League
date: '2018-09-07'
venue: Unknown
location: ''
promotion: PWA
permalink: /events/2018-09-07 - PWA Friday Explosion 102 - PWA 5 Star League/
tags:
- events
matches_json: [{"number": 1, "name": "Quarter Finals: Blade vs. Mystery Panther", "finish": "Blade battled Mystery Panther to a  time limit draw", "rating_stars": "<span class=\"stars\">★★★★★</span>", "rating_num": 5, "time": ""}, {"number": 2, "name": "Quarter Finals: Fantasio Fantastico vs. Red Dragon", "finish": "Red Dragon beat Fantasio Fantastico in 14 Min 36 Sec with a Super Kick", "rating_stars": "<span class=\"stars\">★★★¼</span>", "rating_num": 3.25, "time": "14:36"}, {"number": 3, "name": "Quarter Finals: Caristico vs. Super Delfin", "finish": "Super Delfin beat Caristico in 13 Min 57 Sec with a Roast Pig Clutch", "rating_stars": "<span class=\"stars\">★★★¼</span>", "rating_num": 3.25, "time": "13:57"}, {"number": 4, "name": "Quarter Finals: Blue Blazer Jr. vs. Macho Especial", "finish": "Macho Especial beat Blue Blazer Jr. in 14 Min 21 Sec with a Modified Tombstone", "rating_stars": "<span class=\"stars\">★★★★½</span>", "rating_num": 4.5, "time": "14:21"}]
---

# PWA Friday Explosion 102 - PWA 5 Star League

<div class="event-header">
<div class="event-meta">
**Date:** 2018-09-07<br>
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