---
layout: event.njk
title: PWA Tuesday Night Action 247 - Ace that runs the Place
date: '2018-10-16'
venue: Unknown
location: ''
promotion: PWA
permalink: /events/2018-10-16 - PWA Tuesday Night Action 247 - Ace that runs the Place/
tags:
- events
matches_json: [{"number": 1, "name": "Allen Hawkins vs. Felix Santana III", "finish": "Felix Santana III beat Allen Hawkins in 7 Min 57 Sec with a Fireman Carry Buster", "rating_stars": "<span class=\"stars\">★½</span>", "rating_num": 1.5, "time": "7:57"}, {"number": 2, "name": "Jitsu, Jocephus & Ox Hemlock vs. Masked Lucha Alliance", "finish": "Jitsu  beat Cobra  in 1 Min 9 Sec with an Octopus Hold", "rating_stars": "<span class=\"stars\">DUD</span>", "rating_num": 0, "time": "1:09"}, {"number": 3, "name": "Golden Grappler vs. Poppa Thurgoode", "finish": "Poppa Thurgoode beat Golden Grappler in 26 Min 27 Sec with a The Jive Soul Flow", "rating_stars": "<span class=\"stars\">★★★★¾</span>", "rating_num": 4.75, "time": "26:27"}, {"number": 4, "name": "Diablo Blanco vs. Mystery Panther", "finish": "Diablo Blanco beat Mystery Panther in 5 Min 53 Sec with a K.O", "rating_stars": "<span class=\"stars\">★</span>", "rating_num": 1, "time": "5:53"}, {"number": 5, "name": "PWA World Heavyweight Championship: Fabrizio Tiziano vs. PAC (c)", "finish": "Fabrizio Tiziano beat PAC in 9 Min 33 Sec with a Leg-Stomp Arm Hold", "rating_stars": "<span class=\"stars\">★½</span>", "rating_num": 1.5, "time": "9:33"}]
---

# PWA Tuesday Night Action 247 - Ace that runs the Place

<div class="event-header">
<div class="event-meta">
**Date:** 2018-10-16<br>
**Venue:** Unknown<br>
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