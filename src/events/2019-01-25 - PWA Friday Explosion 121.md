---
layout: event.njk
title: PWA Friday Explosion 121
date: '2019-01-25'
venue: Charlotte, North Carolina
location: ''
promotion: PWA
permalink: /events/2019-01-25 - PWA Friday Explosion 121/
tags:
- events
matches_json: [{"number": 1, "name": "Salvador Sosa vs. Dynamite Smith", "finish": "Salvador Sosa beat Dynamite Smith in 14 Min 43 Sec with a Senton Atomico", "rating_stars": "<span class=\"stars\">★★★½</span>", "rating_num": 3.5, "time": "14:43"}, {"number": 2, "name": "Allen Hawkins & Golden Grappler vs. Jean Wilson & Ricklon Smasher", "finish": "Golden Grappler beat Ricklon Smasher in 16 Min 48 Sec with a The Golden Triangle", "rating_stars": "<span class=\"stars\">★★★¼</span>", "rating_num": 3.25, "time": "16:48"}, {"number": 3, "name": "Hiroto Nakamichi vs. Veit Müller", "finish": "Hiroto Nakamichi beat Veit Müller in 17 Min 33 Sec with a Rising Sun Stretch", "rating_stars": "<span class=\"stars\">★★★★</span>", "rating_num": 4, "time": "17:33"}, {"number": 4, "name": "Avery Alexander vs. Felix Santana Sr.", "finish": "Avery Alexander beat Felix Santana Sr. in 17 Min 14 Sec with a Powerslam", "rating_stars": "<span class=\"stars\">★★★★¼</span>", "rating_num": 4.25, "time": "17:14"}, {"number": 5, "name": "Brutes vs. Lex Rider, Mark Erickson, Nigel Pendragon & Fred Balentine", "finish": "Jack Fury beat Mark Erickson in 9 Min 55 Sec with a RING OUT", "rating_stars": "<span class=\"stars\">★★</span>", "rating_num": 2, "time": "9:55"}]
---

# PWA Friday Explosion 121

<div class="event-header">
<div class="event-meta">
**Date:** 2019-01-25<br>
**Venue:** Charlotte, North Carolina<br>
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