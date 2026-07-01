---
layout: event.njk
title: PWA Tuesday Night Action 278 - Unorthodox Alliance
date: '2019-05-28'
venue: PWA Capcom Arena
location: Boston, Massachusetts, USA
promotion: PWA
permalink: /events/2019-05-28 - PWA Tuesday Night Action 278 - Unorthodox Alliance/
tags:
- events
matches_json: [{"number": 1, "name": "Dynamite Smith vs. Nigel Pendragon", "finish": "Dynamite Smith beat Nigel Pendragon in 18 Min 26 Sec with a School Boy", "rating_stars": "<span class=\"stars\">★★★¾</span>", "rating_num": 3.75, "time": "18:26"}, {"number": 2, "name": "Golden Grappler vs. Saburo Aoki Jr.", "finish": "Golden Grappler & Allen Hawkins battled Saburo Aoki Jr. to a  time limit draw", "rating_stars": "<span class=\"stars\">★½</span>", "rating_num": 1.5, "time": ""}, {"number": 3, "name": "Veteran Veteran Devastators vs. Keith Rowans, Rey Horus & Felix Santana Jr.", "finish": "Keith Rowans beat Fabrizio Tiziano in 21 Min 10 Sec with a Diving Body Press", "rating_stars": "<span class=\"stars\">★★</span>", "rating_num": 2, "time": "21:10"}, {"number": 4, "name": "Mr. Suplex & Ox Hemlock vs. Rick Banner & Lex Rider", "finish": "Lex Rider beat Mr. Suplex in 18 Min 20 Sec with a Frog Splash", "rating_stars": "<span class=\"stars\">★★★½</span>", "rating_num": 3.5, "time": "18:20"}]
---

# PWA Tuesday Night Action 278 - Unorthodox Alliance

<div class="event-header">
<div class="event-meta">
**Date:** 2019-05-28<br>
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