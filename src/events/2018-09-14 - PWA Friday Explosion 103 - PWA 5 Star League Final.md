---
layout: event.njk
title: PWA Friday Explosion 103 - PWA 5 Star League Final
date: '2018-09-14'
venue: Unknown
location: ''
promotion: PWA
permalink: /events/2018-09-14 - PWA Friday Explosion 103 - PWA 5 Star League Final/
tags:
- events
matches_json: [{"number": 1, "name": "El Experto vs. Todd Jackson", "finish": "El Experto beat Todd Jackson in 6 Min 34 Sec with an Agarre Perfecto", "rating_stars": "<span class=\"stars\">★★½</span>", "rating_num": 2.5, "time": "6:34"}, {"number": 2, "name": "Michael Elgin vs. Mark Erickson", "finish": "Mark Erickson beat Michael Elgin in 14 Min 5 Sec with an Omoplata Crossface", "rating_stars": "<span class=\"stars\">★★★★½</span>", "rating_num": 4.5, "time": "14:05"}, {"number": 3, "name": "Best 2 out of 3 Falls: UK Kid vs. Fabrizio Tiziano", "finish": "Fabrizio Tiziano beat UK Kid in 24 Min 8 Sec with a K.O", "rating_stars": "<span class=\"stars\">★★★★¾</span>", "rating_num": 4.75, "time": "24:08"}, {"number": 4, "name": "Interview Segment /w Veteran Veteran Devastators & UK Kid", "finish": "Interview segment involving: Fabrizio Tiziano,  Montgomery Hayes, Keith Rowans & UK Kid", "rating_stars": "<span class=\"stars\">★½</span>", "rating_num": 1.5, "time": ""}, {"number": 5, "name": "PWA 5 Star League Final: Red Dragon vs. Macho Especial", "finish": "Red Dragon beat Macho Especial in 31 Min 9 Sec with a Super Kick", "rating_stars": "<span class=\"stars\">★★★★★</span>", "rating_num": 5, "time": "31:09"}]
---

# PWA Friday Explosion 103 - PWA 5 Star League Final

<div class="event-header">
<div class="event-meta">
**Date:** 2018-09-14<br>
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