---
layout: event.njk
title: PWA Friday Explosion 131
date: '2019-04-11'
venue: PWA Capcom Arena
location: Boston, Massachusetts, USA
promotion: PWA
permalink: /events/2019-04-11 - PWA Friday Explosion 131/
tags:
- events
matches_json: [{"number": 1, "name": "Casper Winkel vs. Nigel Pendragon", "finish": "Casper Winkel beat Nigel Pendragon in 16 Min 0 Sec with a Rocky Mountain Driver", "rating_stars": "<span class=\"stars\">★★½</span>", "rating_num": 2.5, "time": "16:00"}, {"number": 2, "name": "Chelsea Grin vs. Spitfire vs. Villano III Jr. vs. Misterio Guerrero vs. Felix Santana III vs. Theobold Lovecraft", "finish": "Chelsea Grin won a six-pack scramble match against Spitfire, Villano III Jr., Misterio Guerrero, Felix Santana III, &Theobold Lovecraft in  30:17", "rating_stars": "<span class=\"stars\">★★★★½</span>", "rating_num": 4.5, "time": ""}, {"number": 3, "name": "Fabrizio Tiziano (w/Blue Blazer Jr.) vs. Keith Rowans", "finish": "Keith Rowans beat Fabrizio Tiziano in 17 Min 49 Sec with a Rapid Double Arm Suplex", "rating_stars": "<span class=\"stars\">★★★¾</span>", "rating_num": 3.75, "time": "17:49"}, {"number": 4, "name": "Imperium vs. Ilja Dragunov, Lex Rider & Fred Balentine", "finish": "Marcel Barthel beat Fred Balentine in 22 Min 23 Sec with a Landungsbrücken", "rating_stars": "<span class=\"stars\">★★★★</span>", "rating_num": 4, "time": "22:23"}]
---

# PWA Friday Explosion 131

<div class="event-header">
<div class="event-meta">
**Date:** 2019-04-11<br>
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