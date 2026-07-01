---
layout: event.njk
title: PWA Power Hour 13
date: '2019-05-02'
venue: PWA Power Studio
location: Boston, Massachusetts, USA
promotion: PWA
permalink: /events/2019-05-02 - PWA Power Hour 13/
tags:
- events
matches_json: [{"number": 1, "name": "El Experto vs. Theobold Lovecraft", "finish": "El Experto beat Theobold Lovecraft in 14 Min 29 Sec with a La Magistral", "rating_stars": "<span class=\"stars\">★★★¾</span>", "rating_num": 3.75, "time": "14:29"}, {"number": 2, "name": "Rampage Rage (w/Jack Fury) vs. Poppa Thurgoode", "finish": "Rampage Rage beat Poppa Thurgoode in 10 Min 41 Sec with a Pop-up Power Bomb", "rating_stars": "<span class=\"stars\">★★★★¼</span>", "rating_num": 4.25, "time": "10:41"}, {"number": 3, "name": "Mr. Suplex vs. Fantasio Fantastico", "finish": "Mr. Suplex beat Fantasio Fantastico in 7 Min 16 Sec with a Genki Raiga-plex", "rating_stars": "<span class=\"stars\">★★½</span>", "rating_num": 2.5, "time": "7:16"}]
---

# PWA Power Hour 13

<div class="event-header">
<div class="event-meta">
**Date:** 2019-05-02<br>
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