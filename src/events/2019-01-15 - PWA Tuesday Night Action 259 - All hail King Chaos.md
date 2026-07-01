---
layout: event.njk
title: PWA Tuesday Night Action 259 - All hail King Chaos
date: '2019-01-15'
venue: Springfield, Massachusetts
location: ''
promotion: PWA
permalink: /events/2019-01-15 - PWA Tuesday Night Action 259 - All hail King Chaos/
tags:
- events
matches_json: [{"number": 1, "name": "Royal Brawl Qualifiers (Last Chance): Red Dragon vs. Nigel Pendragon", "finish": "Nigel Pendragon beat Red Dragon in 7 Min 3 Sec with a Cardiff Dragon Sleeper", "rating_stars": "<span class=\"stars\">★½</span>", "rating_num": 1.5, "time": "7:03"}, {"number": 2, "name": "Jean Wilson & Ricklon Smasher vs. Allen Hawkins & Golden Grappler", "finish": "Jean Wilson & Ricklon Smasher battled Allen Hawkins & Golden Grappler to a  double KO draw", "rating_stars": "<span class=\"stars\">★★½</span>", "rating_num": 2.5, "time": ""}, {"number": 3, "name": "Jocephus  vs. Michael Elgin", "finish": "Michael Elgin beat Jocephus  in 12 Min 22 Sec with an Elgin bomb", "rating_stars": "<span class=\"stars\">★★★¾</span>", "rating_num": 3.75, "time": "12:22"}, {"number": 4, "name": "Foreign Fanatics vs. Mysterious Fantasticos", "finish": "Foreign Fanatics battled Mysterious Fantasticos to a  time limit draw", "rating_stars": "<span class=\"stars\">★★★¾</span>", "rating_num": 3.75, "time": ""}, {"number": 5, "name": "Royal Brawl Qualifiers: Fabrizio Tiziano vs. Theobold Lovecraft", "finish": "Theobold Lovecraft beat Fabrizio Tiziano in 14 Min 12 Sec with a Chickenwing Facelock", "rating_stars": "<span class=\"stars\">★★★¼</span>", "rating_num": 3.25, "time": "14:12"}]
---

# PWA Tuesday Night Action 259 - All hail King Chaos

<div class="event-header">
<div class="event-meta">
**Date:** 2019-01-15<br>
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