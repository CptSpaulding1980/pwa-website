---
layout: event.njk
title: PWA Tuesday Night Action 287 - Maximum Effort
date: '2019-08-06'
venue: PWA Capcom Arena
location: Boston, Massachusetts, USA
promotion: PWA
permalink: /events/2019-08-06 - PWA Tuesday Night Action 287 - Maximum Effort/
tags:
- events
matches_json: [{"number": 1, "name": "Brutes vs. Masked Maniac IV, Spitfire & Julio Rivera", "finish": "Mike Hool beat Spitfire in 19 Min 28 Sec with an Original Backdrop", "rating_stars": "<span class=\"stars\">★★★¾</span>", "rating_num": 3.75, "time": "19:28"}, {"number": 2, "name": "Adamo Dragon (w/El Pulpo) vs. Snake King", "finish": "Snake King beat Adamo Dragon in 11 Min 57 Sec with a Crucifix Powerbomb", "rating_stars": "<span class=\"stars\">★★★¾</span>", "rating_num": 3.75, "time": "11:57"}, {"number": 3, "name": "Avery Alexander vs. John Hennigan vs. Zack Sabre Jr. vs. Roadkill", "finish": "Roadkill won a four-corners match against Avery Alexander, John Hennigan, &Zack Sabre Jr. in  27:52", "rating_stars": "<span class=\"stars\">★★★★¾</span>", "rating_num": 4.75, "time": ""}, {"number": 4, "name": "No Count Out: SANADA vs. UK Kid", "finish": "UK Kid beat SANADA in 10 Min 23 Sec with a K.O", "rating_stars": "<span class=\"stars\">★★★★¼</span>", "rating_num": 4.25, "time": "10:23"}, {"number": 5, "name": "Texas Death Match - PWA World Heavyweight Championship: Fred Balentine vs. Ox Hemlock (c)", "finish": "Fred Balentine battled Ox Hemlock to a  draw", "rating_stars": "<span class=\"stars\">★★★★★</span>", "rating_num": 5, "time": ""}]
---

# PWA Tuesday Night Action 287 - Maximum Effort

<div class="event-header">
<div class="event-meta">
**Date:** 2019-08-06<br>
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