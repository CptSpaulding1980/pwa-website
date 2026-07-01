---
layout: event.njk
title: PWA Tuesday Night Action 256 - Holy Christmas Eve
date: '2018-12-24'
venue: Albany, New York
location: ''
promotion: PWA
permalink: /events/2018-12-24 - PWA Tuesday Night Action 256 - Holy Christmas Eve/
tags:
- events
matches_json: [{"number": 1, "name": "PWA Junior Heavyweight Championship: Felix Santana Jr. vs. Avery Alexander (c)", "finish": "Felix Santana Jr. beat Avery Alexander in 16 Min 3 Sec with a Mayan Suplex", "rating_stars": "<span class=\"stars\">★★★½</span>", "rating_num": 3.5, "time": "16:03"}, {"number": 2, "name": "El Canek vs. Mackenzie Bergeron (w/The Gatekeeper)", "finish": "El Canek battled Mackenzie Bergeron to a  double KO draw", "rating_stars": "<span class=\"stars\">★★★¾</span>", "rating_num": 3.75, "time": ""}, {"number": 3, "name": "PWA World Tag Team Championship: Mysterious Fantasticos vs. Brutes (c)", "finish": "Rampage Rage beat Mystery Panther in 13 Min 5 Sec with a Diving Shoulder Attack", "rating_stars": "<span class=\"stars\">★★★</span>", "rating_num": 3, "time": "13:05"}, {"number": 4, "name": "Allen Hawkins vs. Lex Rider", "finish": "Lex Rider beat Allen Hawkins in 0 Min 35 Sec with a Curb Stomps & Triangle Choke", "rating_stars": "<span class=\"stars\">★½</span>", "rating_num": 1.5, "time": "0:35"}, {"number": 5, "name": "Veteran Veteran Devastators vs. Blue Spider & Roadkill", "finish": "Veteran Devastators battled Blue Spider & Roadkill to a  double KO draw", "rating_stars": "<span class=\"stars\">★★★¼</span>", "rating_num": 3.25, "time": ""}, {"number": 6, "name": "PWA World Heavyweight Championship: PAC vs. UK Kid (c)", "finish": "UK Kid beat PAC in 9 Min 6 Sec with a Vertical Brainbuster", "rating_stars": "<span class=\"stars\">★★½</span>", "rating_num": 2.5, "time": "9:06"}]
---

# PWA Tuesday Night Action 256 - Holy Christmas Eve

<div class="event-header">
<div class="event-meta">
**Date:** 2018-12-24<br>
**Venue:** Albany, New York<br>
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