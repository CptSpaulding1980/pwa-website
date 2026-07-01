---
layout: event.njk
title: PWA Tuesday Night Action 244 - New Star at the Horizon
date: '2018-09-25'
venue: Unknown
location: ''
promotion: PWA
permalink: /events/2018-09-25 - PWA Tuesday Night Action 244 - New Star at the Horizon/
tags:
- events
matches_json: [{"number": 1, "name": "Steel Cage Match: Veteran Veteran Devastators vs. Jean Wilson, Tri Clops, Roadkill & The Patriot", "finish": "The Patriot beat Blue Blazer Jr. in 23 Min 19 Sec with an Escape", "rating_stars": "<span class=\"stars\">★★★¾</span>", "rating_num": 3.75, "time": "23:19"}, {"number": 2, "name": "Ox Hemlock vs. Ricklon Smasher", "finish": "Ricklon Smasher beat Ox Hemlock in 18 Min 6 Sec with a RING OUT", "rating_stars": "<span class=\"stars\">★★★★¾</span>", "rating_num": 4.75, "time": "18:06"}, {"number": 3, "name": "Dynamite Smith vs. Ray Stantz", "finish": "Dynamite Smith beat Ray Stantz in 11 Min 43 Sec with a Flying Body Attack", "rating_stars": "<span class=\"stars\">★★★¾</span>", "rating_num": 3.75, "time": "11:43"}, {"number": 4, "name": "El Experto (w/Diablo Blanco) vs. Mystery Panther (w/Fantasio Fantastico)", "finish": "El Experto beat Mystery Panther in 10 Min 30 Sec with an Agarre Perfecto", "rating_stars": "<span class=\"stars\">★★★¼</span>", "rating_num": 3.25, "time": "10:30"}, {"number": 5, "name": "Seth Ramsey vs. Allen Hawkins", "finish": "Allen Hawkins beat Seth Ramsey in 3 Min 4 Sec with a Guillotine Drop", "rating_stars": "<span class=\"stars\">★</span>", "rating_num": 1, "time": "3:04"}, {"number": 6, "name": "No Holds Barred Match: Fabrizio Tiziano vs. UK Kid", "finish": "UK Kid beat Fabrizio Tiziano in 17 Min 22 Sec with a Camel Clutch", "rating_stars": "<span class=\"stars\">★★★★¼</span>", "rating_num": 4.25, "time": "17:22"}]
---

# PWA Tuesday Night Action 244 - New Star at the Horizon

<div class="event-header">
<div class="event-meta">
**Date:** 2018-09-25<br>
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