---
layout: event.njk
title: PWA One Way Lane 2019
date: '2019-02-10'
venue: Leon County Civic Center
location: Tallahassee, Florida, USA
promotion: PWA
permalink: /events/2019-02-10 - PWA One Way Lane 2019/
tags:
- events
matches_json: [{"number": 1, "name": "Tag Title #1 Cont. Tournament - Semi Finals: Laredo Kid & Myzteziz Jr. vs. Go Shiozaki & Katsuhiko Nakajima", "finish": "Myzteziz Jr. beat Katsuhiko Nakajima in 31 Min 15 Sec with a Cross Armbreaker", "rating_stars": "<span class=\"stars\">★★★★¼</span>", "rating_num": 4.25, "time": "31:15"}, {"number": 2, "name": "Tag Title #1 Cont. Tournament - Semi Finals: Masked Lucha Alliance vs. Los Ingobernables de Japon", "finish": "El Canek beat EVIL  in 24 Min 56 Sec with a Torturerack", "rating_stars": "<span class=\"stars\">★★★¾</span>", "rating_num": 3.75, "time": "24:56"}, {"number": 3, "name": "Brutes vs. Jean Wilson, Ricklon Smasher, Lex Rider & Fred Balentine", "finish": "Rampage Rage beat Ricklon Smasher in 32 Min 33 Sec with a Splash of Rage", "rating_stars": "<span class=\"stars\">★★★½</span>", "rating_num": 3.5, "time": "32:33"}, {"number": 4, "name": "Michael Elgin vs. Ox Hemlock", "finish": "Michael Elgin beat Ox Hemlock in 11 Min 40 Sec with a Spiral Bomb", "rating_stars": "<span class=\"stars\">★★★¼</span>", "rating_num": 3.25, "time": "11:40"}, {"number": 5, "name": "Tag Title #1 Cont. Tournament - Final: Laredo Kid & Myzteziz Jr. vs. Masked Lucha Alliance", "finish": "Cobra III beat Myzteziz Jr. in 29 Min 55 Sec with a Romero Special", "rating_stars": "<span class=\"stars\">★★★½</span>", "rating_num": 3.5, "time": "29:55"}, {"number": 6, "name": "Mark Erickson, Nigel Pendragon & Rick Banner vs. Dynamite Smith, Saburo Aoki Jr. & UK Kid", "finish": "Saburo Aoki Jr. beat Rick Banner in 20 Min 43 Sec with a Mi Amore de mi Novia", "rating_stars": "<span class=\"stars\">★★★★½</span>", "rating_num": 4.5, "time": "20:43"}, {"number": 7, "name": "Best 2 out of 3 Falls - No Holds Barred - Tornado Tag: Los Rudos Diablos vs. Blue Spider & Roadkill", "finish": "Roadkill beat Diablo Blanco in the third Fall after 11 Min 43 Sec with a Mexican Stretch (2:1 Falls)", "rating_stars": "<span class=\"stars\">★★★¼</span>", "rating_num": 3.25, "time": "11:43"}]
---

# PWA One Way Lane 2019

<div class="event-header">
<div class="event-meta">
**Date:** 2019-02-10<br>
**Venue:** Leon County Civic Center<br>
**Location:** Tallahassee, Florida, USA
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