---
layout: event.njk
title: PWA Friday Explosion 106
date: '2018-10-05'
venue: Miami Florida
location: ''
promotion: PWA
permalink: /events/2018-10-05 - PWA Friday Explosion 106/
tags:
- events
matches_json: [{"number": 1, "name": "Cobra vs. Allen Hawkins", "finish": "Allen Hawkins beat Cobra  in 3 Min 9 Sec with a Black Mass", "rating_stars": "<span class=\"stars\">★</span>", "rating_num": 1, "time": "3:09"}, {"number": 2, "name": "Brutes vs. Casper Winkel & Rick Banner", "finish": "Brutes battled Casper Winkel & Rick Banner to a  time limit draw", "rating_stars": "<span class=\"stars\">★★★¼</span>", "rating_num": 3.25, "time": ""}, {"number": 3, "name": "Ox Hemlock vs. Dynamite Smith", "finish": "Ox Hemlock beat Dynamite Smith in 8 Min 22 Sec with a Turn Belly-to-Belly", "rating_stars": "<span class=\"stars\">★</span>", "rating_num": 1, "time": "8:22"}, {"number": 4, "name": "Felix Santana Jr. vs. Ray Stantz", "finish": "Ray Stantz beat Felix Santana Jr. in 6 Min 3 Sec with a RING OUT", "rating_stars": "<span class=\"stars\">DUD</span>", "rating_num": 0, "time": "6:03"}, {"number": 5, "name": "PWA World Heavyweight Championship: Red Dragon vs. PAC (c)", "finish": "PAC beat Red Dragon in 5 Min 33 Sec with a Nagata Lock III", "rating_stars": "<span class=\"stars\">★★★¼</span>", "rating_num": 3.25, "time": "5:33"}]
---

# PWA Friday Explosion 106

<div class="event-header">
<div class="event-meta">
**Date:** 2018-10-05<br>
**Venue:** Miami Florida<br>
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