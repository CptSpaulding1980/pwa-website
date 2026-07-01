---
layout: event.njk
title: PWA Power Hour 15
date: '2019-05-16'
venue: PWA Power Studio
location: Boston, Massachusetts, USA
promotion: PWA
permalink: /events/2019-05-16 - PWA Power Hour 15/
tags:
- events
matches_json: [{"number": 1, "name": "Seth Ramsey vs. Mark Erickson", "finish": "Mark Erickson beat Seth Ramsey in 1 Min 38 Sec with a Northern Light Suplex", "rating_stars": "<span class=\"stars\">★</span>", "rating_num": 1, "time": "1:38"}, {"number": 2, "name": "Mackenzie Bergeron vs. Nigel Pendragon", "finish": "Nigel Pendragon beat Mackenzie Bergeron in 10 Min 58 Sec with a Spinning Choke", "rating_stars": "<span class=\"stars\">★★½</span>", "rating_num": 2.5, "time": "10:58"}, {"number": 3, "name": "KotR Qualifying - Second Chance: Allen Hawkins vs. Salvador Sosa", "finish": "Salvador Sosa beat Allen Hawkins in 8 Min 24 Sec with a Flying Rollup Pin", "rating_stars": "<span class=\"stars\">★★★¼</span>", "rating_num": 3.25, "time": "8:24"}]
---

# PWA Power Hour 15

<div class="event-header">
<div class="event-meta">
**Date:** 2019-05-16<br>
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