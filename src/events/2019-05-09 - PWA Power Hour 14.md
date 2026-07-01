---
layout: event.njk
title: PWA Power Hour 14
date: '2019-05-09'
venue: PWA Capcom Arena
location: Boston, Massachusetts, USA
promotion: PWA
permalink: /events/2019-05-09 - PWA Power Hour 14/
tags:
- events
matches_json: [{"number": 1, "name": "Ray Stantz vs. Nigel Pendragon", "finish": "Nigel Pendragon beat Ray Stantz in 5 Min 35 Sec with a Boston Crab", "rating_stars": "<span class=\"stars\">DUD</span>", "rating_num": 0, "time": "5:35"}, {"number": 2, "name": "El Experto vs. Spitfire", "finish": "El Experto beat Spitfire in 5 Min 45 Sec with a K.O", "rating_stars": "<span class=\"stars\">DUD</span>", "rating_num": 0, "time": "5:45"}, {"number": 3, "name": "Jitsu vs. Dynamite Smith", "finish": "Jitsu  beat Dynamite Smith in 10 Min 33 Sec with a Brainbuster", "rating_stars": "<span class=\"stars\">★★★¼</span>", "rating_num": 3.25, "time": "10:33"}]
---

# PWA Power Hour 14

<div class="event-header">
<div class="event-meta">
**Date:** 2019-05-09<br>
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