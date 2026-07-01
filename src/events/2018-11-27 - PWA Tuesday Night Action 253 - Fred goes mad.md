---
layout: event.njk
title: PWA Tuesday Night Action 253 - Fred goes mad
date: '2018-11-27'
venue: Chicago, Illinois
location: ''
promotion: PWA
permalink: /events/2018-11-27 - PWA Tuesday Night Action 253 - Fred goes mad/
tags:
- events
matches_json: [{"number": 1, "name": "Mackenzie Bergeron vs. Dynamite Smith", "finish": "Dynamite Smith beat Mackenzie Bergeron in 18 Min 48 Sec with a Diving Body Press", "rating_stars": "<span class=\"stars\">★★★★½</span>", "rating_num": 4.5, "time": "18:48"}, {"number": 2, "name": "PWA World Tag Team Championship: Ringkampf vs. Brutes (c)", "finish": "Ringkampf battled Brutes to a  time limit draw", "rating_stars": "<span class=\"stars\">★★★</span>", "rating_num": 3, "time": ""}, {"number": 3, "name": "PWA International Championship: Hiroto Nakamichi vs. Lex Rider (c)", "finish": "Lex Rider beat Hiroto Nakamichi in 11 Min 17 Sec with a Vaulting Frog Splash", "rating_stars": "<span class=\"stars\">★★★½</span>", "rating_num": 3.5, "time": "11:17"}, {"number": 4, "name": "Los Rudos Diablos vs. Blue Spider, Roadkill, Grizzlor & Macho Especial", "finish": "Roadkill beat L.A. Park in 23 Min 24 Sec with an Appeal Diving Elbowdrop", "rating_stars": "<span class=\"stars\">★★★★¼</span>", "rating_num": 4.25, "time": "23:24"}, {"number": 5, "name": "Montgomery Hayes vs. Fred Balentine", "finish": "Montgomery Hayes beat Fred Balentine in 23 Min 20 Sec with a Stomping (Back)", "rating_stars": "<span class=\"stars\">★★★★¾</span>", "rating_num": 4.75, "time": "23:20"}]
---

# PWA Tuesday Night Action 253 - Fred goes mad

<div class="event-header">
<div class="event-meta">
**Date:** 2018-11-27<br>
**Venue:** Chicago, Illinois<br>
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