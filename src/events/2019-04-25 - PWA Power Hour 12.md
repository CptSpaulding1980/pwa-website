---
layout: event.njk
title: PWA Power Hour 12
date: '2019-04-25'
venue: PWA Power Studio
location: Boston, Massachusetts, USA
promotion: PWA
permalink: /events/2019-04-25 - PWA Power Hour 12/
tags:
- events
matches_json: [{"number": 1, "name": "Victor Kurilenko vs. Theobold Lovecraft", "finish": "Theobold Lovecraft beat Victor Kurilenko in 6 Min 39 Sec with a Cobra Clutch", "rating_stars": "<span class=\"stars\">★★</span>", "rating_num": 2, "time": "6:39"}, {"number": 2, "name": "Spitfire vs. Mr. Suplex", "finish": "Mr. Suplex beat Spitfire in 8 Min 39 Sec with a Genki Raiga-plex", "rating_stars": "<span class=\"stars\">★★★</span>", "rating_num": 3, "time": "8:39"}, {"number": 3, "name": "Blake Twins vs. Masked Lucha Alliance", "finish": "Macho Especial beat Sammy Blake in 12 Min 24 Sec with an Elevated Boston Crab", "rating_stars": "<span class=\"stars\">★★½</span>", "rating_num": 2.5, "time": "12:24"}]
---

# PWA Power Hour 12

<div class="event-header">
<div class="event-meta">
**Date:** 2019-04-25<br>
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