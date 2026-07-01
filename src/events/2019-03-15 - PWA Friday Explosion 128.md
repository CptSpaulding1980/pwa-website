---
layout: event.njk
title: PWA Friday Explosion 128
date: '2019-03-15'
venue: 1st Mariner Arena
location: Baltimore, Maryland, USA
promotion: PWA
permalink: /events/2019-03-15 - PWA Friday Explosion 128/
tags:
- events
matches_json: [{"number": 1, "name": "Rampage Rage vs. Macho Especial", "finish": "Rampage Rage beat Macho Especial in 3 Min 26 Sec with a K.O", "rating_stars": "<span class=\"stars\">★</span>", "rating_num": 1, "time": "3:26"}, {"number": 2, "name": "Avery Alexander, Chelsea Grin, Red Dragon & El Experto vs. Santana Family & Blue Demon Jr.", "finish": "El Experto beat Felix Santana Jr. in 14 Min 0 Sec with an Agarre Perfecto", "rating_stars": "<span class=\"stars\">★★★</span>", "rating_num": 3, "time": "14:00"}, {"number": 3, "name": "Jitsu vs. Rick Banner", "finish": "Rick Banner beat Jitsu  in 10 Min 22 Sec with a Backslide", "rating_stars": "<span class=\"stars\">★★★¼</span>", "rating_num": 3.25, "time": "10:22"}, {"number": 4, "name": "WALTER vs. Blue Spider", "finish": "WALTER beat Blue Spider in 17 Min 37 Sec with a Powerbomb", "rating_stars": "<span class=\"stars\">★★★★½</span>", "rating_num": 4.5, "time": "17:37"}]
---

# PWA Friday Explosion 128

<div class="event-header">
<div class="event-meta">
**Date:** 2019-03-15<br>
**Venue:** 1st Mariner Arena<br>
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