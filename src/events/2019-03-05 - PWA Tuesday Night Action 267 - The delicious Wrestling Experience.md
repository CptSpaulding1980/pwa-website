---
layout: event.njk
title: PWA Tuesday Night Action 267 - The delicious Wrestling Experience
date: '2019-03-05'
venue: Boston Garden
location: Boston, Massachusetts, USA
promotion: PWA
permalink: /events/2019-03-05 - PWA Tuesday Night Action 267 - The delicious Wrestling
  Experience/
tags:
- events
matches_json: [{"number": 1, "name": "Seth Ramsey & Todd Jackson vs. Jean Wilson & Ricklon Smasher", "finish": "Jean Wilson beat Todd Jackson in 2 Min 53 Sec with an Axe Bomber", "rating_stars": "<span class=\"stars\">★</span>", "rating_num": 1, "time": "2:53"}, {"number": 2, "name": "Mackenzie Bergeron /w/Veteran Veteran Devastators) vs. Fred Balentine", "finish": "Fred Balentine beat Mackenzie Bergeron in 8 Min 49 Sec with a Full Nelson Buster", "rating_stars": "<span class=\"stars\">★★★½</span>", "rating_num": 3.5, "time": "8:49"}, {"number": 3, "name": "Diablo Blanco vs. Blue Spider", "finish": "Blue Spider beat Diablo Blanco in 9 Min 23 Sec with a Blizzard Suplex", "rating_stars": "<span class=\"stars\">★★★¾</span>", "rating_num": 3.75, "time": "9:23"}, {"number": 4, "name": "Imperium vs. Lex Rider & Mark Erickson", "finish": "Lex Rider beat Marcel Barthel in 9 Min 6 Sec with a Vaulting Frog Splash", "rating_stars": "<span class=\"stars\">★★★¼</span>", "rating_num": 3.25, "time": "9:06"}, {"number": 5, "name": "Ox Hemlock, Jocephus & Jitsu  vs. Rick Banner, UK Kid & Michael Elgin", "finish": "Ox Hemlock, Jocephus , & Jitsu  battled Rick Banner,  UK Kid & Michael Elgin to a  double KO draw", "rating_stars": "<span class=\"stars\">★★★¼</span>", "rating_num": 3.25, "time": ""}]
---

# PWA Tuesday Night Action 267 - The delicious Wrestling Experience

<div class="event-header">
<div class="event-meta">
**Date:** 2019-03-05<br>
**Venue:** Boston Garden<br>
**Location:** Boston, Massachusetts, USA
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