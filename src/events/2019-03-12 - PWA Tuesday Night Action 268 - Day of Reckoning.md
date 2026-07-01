---
layout: event.njk
title: PWA Tuesday Night Action 268 - Day of Reckoning
date: '2019-03-12'
venue: Baltimore Arena
location: Baltimore, Maryland, USA
promotion: PWA
permalink: /events/2019-03-12 - PWA Tuesday Night Action 268 - Day of Reckoning/
tags:
- events
matches_json: [{"number": 1, "name": "Saburo Aoki Jr. vs. Dynamite Smith", "finish": "Saburo Aoki Jr. beat Dynamite Smith in 10 Min 21 Sec with a School Boy", "rating_stars": "<span class=\"stars\">★★★¾</span>", "rating_num": 3.75, "time": "10:21"}, {"number": 2, "name": "Red Dragon vs. Felix Santana Sr.", "finish": "Felix Santana Sr. beat Red Dragon in 12 Min 59 Sec with a Kabel Naria", "rating_stars": "<span class=\"stars\">★★½</span>", "rating_num": 2.5, "time": "12:59"}, {"number": 3, "name": "Chelsea Grin vs. Theobold Lovecraft", "finish": "Chelsea Grin beat Theobold Lovecraft in 8 Min 37 Sec with a Butterfly Neck Lock", "rating_stars": "<span class=\"stars\">★★★½</span>", "rating_num": 3.5, "time": "8:37"}, {"number": 4, "name": "Best 2 out of 3 Falls: Diablo Blanco & Dr. Wagner Jr. vs. Blue Spider & Blue Demon Jr.", "finish": "Blue Spider beat Diablo Blanco in 9 Min 40 Sec with a Flying Body Press", "rating_stars": "<span class=\"stars\">★★★½</span>", "rating_num": 3.5, "time": "9:40"}, {"number": 5, "name": "Ox Hemlock, Jocephus & Jitsu  vs. Rick Banner, UK Kid & Michael Elgin", "finish": "Jitsu  beat Rick Banner in 15 Min 45 Sec with an Octopus Hold", "rating_stars": "<span class=\"stars\">★★★½</span>", "rating_num": 3.5, "time": "15:45"}]
---

# PWA Tuesday Night Action 268 - Day of Reckoning

<div class="event-header">
<div class="event-meta">
**Date:** 2019-03-12<br>
**Venue:** Baltimore Arena<br>
**Location:** Baltimore, Maryland, USA
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