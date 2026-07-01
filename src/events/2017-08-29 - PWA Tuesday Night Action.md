---
layout: event.njk
title: PWA Tuesday Night Action
date: '2017-08-29'
venue: ''
location: ''
promotion: PWA
permalink: /events/2017-08-29 - PWA Tuesday Night Action/
tags:
- events
matches_json: [{"number": 1, "name": "PWA 5 Star League 2017 – Bracket A Match: Macho Especial [1] vs. Montgomery Hayes [1]", "finish": "Draw (Double K.O.)", "rating_stars": "<span class=\"stars\">★★★★½</span>", "rating_num": 4.5, "time": ""}, {"number": 2, "name": "PWA 5 Star League 2017 – Bracket A Match: Montgomery Hayes [1] vs. Silas Young [3]", "finish": "Silas Young beat Montgomery Hayes (Misery)", "rating_stars": "<span class=\"stars\">★★★★½</span>", "rating_num": 4.5, "time": ""}, {"number": 3, "name": "PWA 5 Star League 2017 – Bracket A Match: Austin Aries [4] vs. Pentagón Jr. [2]", "finish": "Austin Aries beat Pentagón Jr. (Last Chancery)", "rating_stars": "<span class=\"stars\">★★★★½</span>", "rating_num": 4.5, "time": ""}, {"number": 4, "name": "PWA 5 Star League 2017 – Bracket A Match: Blade [6] vs. Grizzlor [0]", "finish": "Blade beat Grizzlor (Praying Powerbomb)", "rating_stars": "<span class=\"stars\">★★★★¾</span>", "rating_num": 4.75, "time": ""}]
---

# PWA Tuesday Night Action

<div class="event-header">
<div class="event-meta">
**Date:** 2017-08-29<br>
**Venue:** <br>
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