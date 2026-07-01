---
layout: event.njk
title: PWA Tuesday Night Action
date: '2017-08-15'
venue: ''
location: ''
promotion: PWA
permalink: /events/2017-08-15 - PWA Tuesday Night Action/
tags:
- events
matches_json: [{"number": 1, "name": "Triple Threat Elimination Match - PWA International Championship: UK Kid vs. Zack Sabre Jr. vs. Davey Boy Smith Jr. (c)", "finish": "Davey Boy Smith Jr. won a Triple Threat Match - Eliminations: UK Kid eliminated by Zack Sabre Jr. (Standing Cross Armbreaker 25:44) Zack Sabre eliminated by Davey Boy Smith Jr. (Runing Powerslam 26:42)", "rating_stars": "<span class=\"stars\">★★★★</span>", "rating_num": 4, "time": ""}, {"number": 2, "name": "PWA 5 Star League 2017 – Bracket A Match: Pentagón Jr. [0] vs. Blue Spider [2]", "finish": "Blue Spider beat Pentagón Jr. (Shooting Star Press)", "rating_stars": "<span class=\"stars\">★★★★</span>", "rating_num": 4, "time": ""}, {"number": 3, "name": "PWA 5 Star League 2017 – Bracket A Match: Austin Aries [2] vs. Grizzlor [0]", "finish": "Austin Aries beat Grizzlor (Last Chancery)", "rating_stars": "<span class=\"stars\">★★★★</span>", "rating_num": 4, "time": ""}, {"number": 4, "name": "PWA 5 Star League 2017 – Bracket A Match: Blade [2] vs. Silas Young [0]", "finish": "Blade beat Silas Young (Top Rope Tombstone Piledriver)", "rating_stars": "<span class=\"stars\">★★★★¼</span>", "rating_num": 4.25, "time": ""}]
---

# PWA Tuesday Night Action

<div class="event-header">
<div class="event-meta">
**Date:** 2017-08-15<br>
**Venue:** <br>
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