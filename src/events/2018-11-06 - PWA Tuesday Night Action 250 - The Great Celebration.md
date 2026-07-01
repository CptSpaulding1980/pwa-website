---
layout: event.njk
title: PWA Tuesday Night Action 250 - The Great Celebration
date: '2018-11-06'
venue: New York City, New York
location: ''
promotion: PWA
permalink: /events/2018-11-06 - PWA Tuesday Night Action 250 - The Great Celebration/
tags:
- events
matches_json: [{"number": 1, "name": "PWA Junior Heavyweight Championship: Jushin Liger vs. KUSHIDA (c)", "finish": "Jushin Liger beat KUSHIDA  in 14 Min 33 Sec with a Shooting Star Press", "rating_stars": "<span class=\"stars\">★★★¾</span>", "rating_num": 3.75, "time": "14:33"}, {"number": 2, "name": "Allen Hawkins, Golden Grappler, Ox Hemlock & Zodiac vs. Felix Santana Jr., Felix Santana III, Lex Rider & Mark Erickson", "finish": "Allen Hawkins, Golden Grappler, Ox Hemlock, & Zodiac  battled Felix Santana Jr.,  Felix Santana III, Lex Rider, & Mark Erickson to a  Double Count Out", "rating_stars": "<span class=\"stars\">★★★¾</span>", "rating_num": 3.75, "time": ""}, {"number": 3, "name": "Avery Alexander vs. Dynamite Smith", "finish": "Avery Alexander beat Dynamite Smith in 11 Min 17 Sec with a High Angle Drop Kick", "rating_stars": "<span class=\"stars\">★★★</span>", "rating_num": 3, "time": "11:17"}, {"number": 4, "name": "PWA World Tag Team Championship: Brutes vs. Ringkampf (c)", "finish": "WALTER beat Jack Fury in 9 Min 6 Sec with a K.O", "rating_stars": "<span class=\"stars\">★★½</span>", "rating_num": 2.5, "time": "9:06"}, {"number": 5, "name": "Keith Rowans (w/Montgomery Hayes) vs. Fred Balentine", "finish": "Fred Balentine beat Keith Rowans in 19 Min 2 Sec with a Spear", "rating_stars": "<span class=\"stars\">★★★½</span>", "rating_num": 3.5, "time": "19:02"}, {"number": 6, "name": "Los Rudos Diablos vs. Blue Spider & Roadkill", "finish": "Blue Spider & Roadkill beat Los Rudos Diablos in 12 Min 29 Sec via Disqualification", "rating_stars": "<span class=\"stars\">★★★</span>", "rating_num": 3, "time": "12:29"}, {"number": 7, "name": "Steel Cage Match - PWA World Heavyweight Championship: UK Kid vs. Fabrizio Tiziano (c)", "finish": "UK Kid beat Fabrizio Tiziano in 13 Min 50 Sec with a British Fall", "rating_stars": "<span class=\"stars\">★★★★¼</span>", "rating_num": 4.25, "time": "13:50"}]
---

# PWA Tuesday Night Action 250 - The Great Celebration

<div class="event-header">
<div class="event-meta">
**Date:** 2018-11-06<br>
**Venue:** New York City, New York<br>
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