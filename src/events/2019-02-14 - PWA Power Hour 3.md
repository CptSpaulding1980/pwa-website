---
layout: event.njk
title: PWA Power Hour 3
date: '2019-02-14'
venue: PWA Power Studio
location: Boston, Massachusetts, USA
promotion: PWA
permalink: /events/2019-02-14 - PWA Power Hour 3/
tags:
- events
matches_json: [{"number": 1, "name": "Masked Maniac IV vs. Allen Hawkins", "finish": "Allen Hawkins beat Mason Miller in 9 Min 1 Sec with an Enzuigiri", "rating_stars": "<span class=\"stars\">★★★★½</span>", "rating_num": 4.5, "time": "9:01"}, {"number": 2, "name": "Nigel Pendragon vs. Dynamite Smith", "finish": "Nigel Pendragon beat Dynamite Smith in 9 Min 36 Sec with a Spinning Choke", "rating_stars": "<span class=\"stars\">★★★</span>", "rating_num": 3, "time": "9:36"}, {"number": 3, "name": "PWA Jr. Heavyweight #1 Contendership: Avery Alexander vs. Felix Santana III", "finish": "Avery Alexander beat Felix Santana III in 9 Min 1 Sec with a Pinnacle Dropkick", "rating_stars": "<span class=\"stars\">★★★¼</span>", "rating_num": 3.25, "time": "9:01"}]
---

# PWA Power Hour 3

<div class="event-header">
<div class="event-meta">
**Date:** 2019-02-14<br>
**Venue:** PWA Power Studio<br>
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