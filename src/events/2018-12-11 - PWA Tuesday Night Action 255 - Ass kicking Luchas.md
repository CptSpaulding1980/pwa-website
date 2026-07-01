---
layout: event.njk
title: PWA Tuesday Night Action 255 - Ass kicking Luchas
date: '2018-12-11'
venue: Baltimore, Maryland
location: ''
promotion: PWA
permalink: /events/2018-12-11 - PWA Tuesday Night Action 255 - Ass kicking Luchas/
tags:
- events
matches_json: [{"number": 1, "name": "Mistico II vs. Felix Santana Jr.", "finish": "Felix Santana Jr. beat Mistico II in 19 Min 31 Sec with a RING OUT", "rating_stars": "<span class=\"stars\">★★★★½</span>", "rating_num": 4.5, "time": "19:31"}, {"number": 2, "name": "Brutes vs. Mysterious Fantasticos", "finish": "Mystery Panther beat Rampage Rage in 29 Min 39 Sec with a Top Rope Huracanrana", "rating_stars": "<span class=\"stars\">★★★½</span>", "rating_num": 3.5, "time": "29:39"}, {"number": 3, "name": "Allen Hawkins vs. Lex Rider", "finish": "Lex Rider beat Allen Hawkins in 4 Min 31 Sec with a Curb Stomps & Triangle Choke", "rating_stars": "<span class=\"stars\">★★</span>", "rating_num": 2, "time": "4:31"}, {"number": 4, "name": "Fabrizio Tiziano vs. Blue Spider", "finish": "Blue Spider beat Fabrizio Tiziano in 12 Min 0 Sec with a K.O", "rating_stars": "<span class=\"stars\">★★★¾</span>", "rating_num": 3.75, "time": "12:00"}, {"number": 5, "name": "PWA World Heavyweight Championship: Rey Fénix vs. UK Kid (c)", "finish": "UK Kid  beat Rey Fénix in 9 Min 59 Sec with a Torture Camel Clutch", "rating_stars": "<span class=\"stars\">★★★</span>", "rating_num": 3, "time": "9:59"}]
---

# PWA Tuesday Night Action 255 - Ass kicking Luchas

<div class="event-header">
<div class="event-meta">
**Date:** 2018-12-11<br>
**Venue:** Baltimore, Maryland<br>
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