---
layout: event.njk
title: PWA Tuesday Night Action 254 - Clash of Styles
date: '2018-12-04'
venue: Pittsburgh, Pennsylvania
location: ''
promotion: PWA
permalink: /events/2018-12-04 - PWA Tuesday Night Action 254 - Clash of Styles/
tags:
- events
matches_json: [{"number": 1, "name": "Fantasio Fantastico vs. Felix Santana III", "finish": "Fantasio Fantastico beat Felix Santana III in 7 Min 13 Sec with a Silent Clutch", "rating_stars": "<span class=\"stars\">★½</span>", "rating_num": 1.5, "time": "7:13"}, {"number": 2, "name": "Shoot Style Match: Skullface Killah vs. Veit Müller", "finish": "Skullface Killah beat Veit Müller in 1R 8 Min 41 Sec with a K.O", "rating_stars": "<span class=\"stars\">★★★¼</span>", "rating_num": 3.25, "time": "8:41"}, {"number": 3, "name": "PWA World Tag Team Championship: Ringkampf vs. Brutes (c)", "finish": "Mike Hool beat WALTER in 12 Min 17 Sec with a K.O", "rating_stars": "<span class=\"stars\">★½</span>", "rating_num": 1.5, "time": "12:17"}]
---

# PWA Tuesday Night Action 254 - Clash of Styles

<div class="event-header">
<div class="event-meta">
**Date:** 2018-12-04<br>
**Venue:** Pittsburgh, Pennsylvania<br>
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