---
layout: event.njk
title: PWA Royal Brawl 2019
date: '2019-01-20'
venue: Boston, Massachusetts
location: ''
promotion: PWA
permalink: /events/2019-01-20 - PWA Royal Brawl 2019/
tags:
- events
matches_json: [{"number": 1, "name": "Avery Alexander, Chelsea Grin & Allen Hawkins vs. Santana Family", "finish": "Avery Alexander, Chelsea Grin, & Allen Hawkins battled Santana Family to a  time limit draw", "rating_stars": "<span class=\"stars\">★★★¾</span>", "rating_num": 3.75, "time": ""}, {"number": 2, "name": "PWA World Tag Team Championship: Casper Winkel & Rick Banner vs. Brutes (c)", "finish": "Mike Hool beat Rick Banner in 13 Min 57 Sec with a King Kong Knee Drop", "rating_stars": "<span class=\"stars\">★★★¼</span>", "rating_num": 3.25, "time": "13:57"}, {"number": 3, "name": "PWA World Heavyweight Championship: PAC vs. UK Kid (c)", "finish": "UK Kid beat PAC in 14 Min 41 Sec with a Leg Lift Backdrop Hold", "rating_stars": "<span class=\"stars\">★★★¼</span>", "rating_num": 3.25, "time": "14:41"}, {"number": 4, "name": "PWA World Title #1 Contender Battle Royal", "finish": "Rick Banner won a 53 wrestler Royal Rumble in 138:37", "rating_stars": "<span class=\"stars\">★★★★½</span>", "rating_num": 4.5, "time": ""}]
---

# PWA Royal Brawl 2019

<div class="event-header">
<div class="event-meta">
**Date:** 2019-01-20<br>
**Venue:** Boston, Massachusetts<br>
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