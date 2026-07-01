---
layout: event.njk
title: PWA Tuesday Night Action 283 - Summer in the Tundra
date: '2019-07-02'
venue: PWA Capcom Arena
location: Boston, Massachusetts, USA
promotion: PWA
permalink: /events/2019-07-02 - PWA Tuesday Night Action 283 - Summer in the Tundra/
tags:
- events
matches_json: [{"number": 1, "name": "Veteran Veteran Devastators vs. Mysterious Fantasticos", "finish": "Mackenzie Bergeron, Elias Blake, & Sammy Blake battled Mysterious Fantasticos to a  time limit draw", "rating_stars": "<span class=\"stars\">★★½</span>", "rating_num": 2.5, "time": ""}, {"number": 2, "name": "Foreign Fanatics vs. Los Tortugas Ninja", "finish": "Hiroto Nakamichi beat Donatello in 0 Min 36 Sec with a Rising Sun Stretch", "rating_stars": "<span class=\"stars\">DUD</span>", "rating_num": 0, "time": "0:36"}, {"number": 3, "name": "Jack Fury vs. Tri Clops", "finish": "Tri Clops beat Jack Fury in 28 Min 58 Sec with a German Suplex", "rating_stars": "<span class=\"stars\">★★★★</span>", "rating_num": 4, "time": "28:58"}, {"number": 4, "name": "Invasores vs. Jack Gold, Masked Maniac IV & Spitfire", "finish": "Neptune Tritano beat Jack Gold in 22 Min 38 Sec with a Fish Stretch Sleeper", "rating_stars": "<span class=\"stars\">★★★¾</span>", "rating_num": 3.75, "time": "22:38"}, {"number": 5, "name": "Tundra Wurm vs. Lex Rider", "finish": "Tundra Wurm beat Lex Rider in 15 Min 49 Sec with a Tundra's End", "rating_stars": "<span class=\"stars\">★★★¼</span>", "rating_num": 3.25, "time": "15:49"}]
---

# PWA Tuesday Night Action 283 - Summer in the Tundra

<div class="event-header">
<div class="event-meta">
**Date:** 2019-07-02<br>
**Venue:** PWA Capcom Arena<br>
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