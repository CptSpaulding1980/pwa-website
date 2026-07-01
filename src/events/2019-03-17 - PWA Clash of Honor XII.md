---
layout: event.njk
title: PWA Clash of Honor XII
date: '2019-03-17'
venue: Boston Garden
location: Boston, Massachusetts, USA
promotion: PWA
permalink: /events/2019-03-17 - PWA Clash of Honor XII/
tags:
- events
matches_json: [{"number": 1, "name": "Blake Twins vs. Misterio Guerrero & Theobold Lovecraft", "finish": "Theobold Lovecraft beat Elias Blake in 20 Min 57 Sec with a Chickenwing Facelock", "rating_stars": "<span class=\"stars\">★★★★¼</span>", "rating_num": 4.25, "time": "20:57"}, {"number": 2, "name": "PWA Junior Heavyweight Championship: Avery Alexander vs. Felix Santana Jr. (c)", "finish": "Felix Santana Jr. beat Avery Alexander in 11 Min 54 Sec with a La Esparda", "rating_stars": "<span class=\"stars\">★★★★¼</span>", "rating_num": 4.25, "time": "11:54"}, {"number": 3, "name": "Hair vs. Mask Match: Montgomery Hayes vs. Roadkill", "finish": "Roadkill beat Montgomery Hayes in 14 Min 3 Sec with a Triangle Scorpion", "rating_stars": "<span class=\"stars\">★★★★¼</span>", "rating_num": 4.25, "time": "14:03"}, {"number": 4, "name": "PWA World Tag Team Championship: Masked Lucha Alliance vs. Brutes (c)", "finish": "Macho Especial beat Rampage Rage in 20 Min 14 Sec with an Elevated Boston Crab", "rating_stars": "<span class=\"stars\">★★★★½</span>", "rating_num": 4.5, "time": "20:14"}, {"number": 5, "name": "PWA International Championship: WALTER vs. Lex Rider (c)", "finish": "WALTER beat Lex Rider in 9 Min 57 Sec with a Powerbomb", "rating_stars": "<span class=\"stars\">★★★¼</span>", "rating_num": 3.25, "time": "9:57"}, {"number": 6, "name": "Junior Warfare Elimination Match", "finish": "Blue Blazer Jr. won a 20 wrestler Junior Warfare Match in 58:37", "rating_stars": "<span class=\"stars\">★★★★¼</span>", "rating_num": 4.25, "time": ""}, {"number": 7, "name": "Texas Death Match: Ox Hemlock vs. Michael Elgin", "finish": "Ox Hemlock beat Michael Elgin in a Texas Death Match with a Barbed Wire Baseball Bat in 34:14", "rating_stars": "<span class=\"stars\">★★★★½</span>", "rating_num": 4.5, "time": ""}, {"number": 8, "name": "Diablo Blanco vs. Blue Demon Jr.", "finish": "Diablo Blanco beat Blue Demon Jr. in 9 Min 18 Sec with a RING OUT", "rating_stars": "<span class=\"stars\">★★½</span>", "rating_num": 2.5, "time": "9:18"}, {"number": 9, "name": "PWA World Heavyweight Championship: Rick Banner vs. UK Kid (c)", "finish": "UK Kid beat Rick Banner in 28 Min 1 Sec with a Camel Clutch", "rating_stars": "<span class=\"stars\">★★★★★</span>", "rating_num": 5, "time": "28:01"}]
---

# PWA Clash of Honor XII

<div class="event-header">
<div class="event-meta">
**Date:** 2019-03-17<br>
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