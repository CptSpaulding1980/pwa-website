---
layout: event.njk
title: PWA Friday Explosion 105
date: '2018-09-28'
venue: Unknown
location: ''
promotion: PWA
permalink: /events/2018-09-28 - PWA Friday Explosion 105/
tags:
- events
matches_json: [{"number": 1, "name": "Dynamite Smith vs. Golden Grappler", "finish": "Dynamite Smith battled Golden Grappler to a  time limit draw", "rating_stars": "<span class=\"stars\">★★★★</span>", "rating_num": 4, "time": ""}, {"number": 2, "name": "Winston Zedd vs. Allen Hawkins", "finish": "Allen Hawkins beat Winston Zedd in 7 Min 34 Sec with an Oklahoma Stampede", "rating_stars": "<span class=\"stars\">★</span>", "rating_num": 1, "time": "7:34"}, {"number": 3, "name": "Misterio Guerrero vs. Hiroto Nakamichi", "finish": "Hiroto Nakamichi beat Misterio Guerrero in 13 Min 36 Sec with a Rising Sun Stretch", "rating_stars": "<span class=\"stars\">★★½</span>", "rating_num": 2.5, "time": "13:36"}, {"number": 4, "name": "The Blake Twins vs. Casper Winkel & Rick Banner", "finish": "Elias Blake beat Casper Winkel in 25 Min 7 Sec with a Piledriver", "rating_stars": "<span class=\"stars\">★★★★½</span>", "rating_num": 4.5, "time": "25:07"}, {"number": 5, "name": "wXw Showcase Match: Ilja Dragunov vs. WALTER", "finish": "WALTER beat Ilja Dragunov in 25 Min 33 Sec with a Powerbomb Whip", "rating_stars": "<span class=\"stars\">★★★★½</span>", "rating_num": 4.5, "time": "25:33"}]
---

# PWA Friday Explosion 105

<div class="event-header">
<div class="event-meta">
**Date:** 2018-09-28<br>
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