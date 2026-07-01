---
layout: event.njk
title: PWA Friday Explosion 120
date: '2019-01-18'
venue: Springfield, Massachusetts
location: ''
promotion: PWA
permalink: /events/2019-01-18 - PWA Friday Explosion 120/
tags:
- events
matches_json: [{"number": 1, "name": "Royal Brawl Qualifiers: Chelsea Grin vs. Rick Banner", "finish": "Rick Banner beat Chelsea Grin in 17 Min 41 Sec with a La Magistral", "rating_stars": "<span class=\"stars\">★★★★¼</span>", "rating_num": 4.25, "time": "17:41"}, {"number": 2, "name": "Royal Brawl Qualifiers: Mackenzie Bergeron vs. Mark Erickson", "finish": "Mark Erickson beat Mackenzie Bergeron in 16 Min 25 Sec with a Double Knee Chin Crusher", "rating_stars": "<span class=\"stars\">★★★★¾</span>", "rating_num": 4.75, "time": "16:25"}, {"number": 3, "name": "Royal Brawl Qualifiers: Golden Grappler vs. Masked Maniac IV", "finish": "Golden Grappler beat Masked Maniac IV in 12 Min 14 Sec with a Piledriver", "rating_stars": "<span class=\"stars\">★★★½</span>", "rating_num": 3.5, "time": "12:14"}, {"number": 4, "name": "Royal Brawl Qualifiers: Blue Blazer Jr. vs. Roadkill", "finish": "Roadkill beat Blue Blazer Jr. in 12 Min 46 Sec with a Mexican Stretch", "rating_stars": "<span class=\"stars\">★★★★¼</span>", "rating_num": 4.25, "time": "12:46"}, {"number": 5, "name": "PAC & Zack Sabre Jr. vs. Tri Clops & UK Kid", "finish": "PAC beat UK Kid in 13 Min 5 Sec with a Shooting Star Press", "rating_stars": "<span class=\"stars\">★★★★</span>", "rating_num": 4, "time": "13:05"}]
---

# PWA Friday Explosion 120

<div class="event-header">
<div class="event-meta">
**Date:** 2019-01-18<br>
**Venue:** Springfield, Massachusetts<br>
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