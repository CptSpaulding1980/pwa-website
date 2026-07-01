---
layout: event.njk
title: PWA Friday Explosion 127
date: '2019-03-08'
venue: 1st Mariner Arena
location: Baltimore, Maryland, USA
promotion: PWA
permalink: /events/2019-03-08 - PWA Friday Explosion 127/
tags:
- events
matches_json: [{"number": 1, "name": "Veteran Veteran Devastators vs. Mysterious Fantasticos", "finish": "Mystery Panther beat Fabrizio Tiziano in 19 Min 27 Sec with a Mysterious Rana", "rating_stars": "<span class=\"stars\">★★★★¼</span>", "rating_num": 4.25, "time": "19:27"}, {"number": 2, "name": "Mark Erickson vs. WALTER", "finish": "WALTER beat Mark Erickson in 5 Min 25 Sec with a Head Pickup Lariat", "rating_stars": "<span class=\"stars\">★★★</span>", "rating_num": 3, "time": "5:25"}, {"number": 3, "name": "Avery Alexander, Chelsea Grin & Red Dragon vs. Santana Family", "finish": "Red Dragon beat Julio Rivera in 14 Min 11 Sec with a Cobra Twist", "rating_stars": "<span class=\"stars\">★★★¼</span>", "rating_num": 3.25, "time": "14:11"}, {"number": 4, "name": "6 Way Match: Jack Fury vs. Skullface Killah vs. Fabian Aichner vs. Marcel Barthel vs. Fred Balentine vs. Lex Rider", "finish": "Lex Rider won a six-pack scramble match against Jack Fury, Skullface Killah, Fabian Aichner, Marcel Barthel, &Fred Balentine in  09:26", "rating_stars": "<span class=\"stars\">★★★¼</span>", "rating_num": 3.25, "time": ""}]
---

# PWA Friday Explosion 127

<div class="event-header">
<div class="event-meta">
**Date:** 2019-03-08<br>
**Venue:** 1st Mariner Arena<br>
**Location:** Baltimore, Maryland, USA
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