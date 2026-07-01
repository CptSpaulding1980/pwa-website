---
layout: event.njk
title: PWA Tuesday Night Action 277
date: '2019-05-21'
venue: PWA Capcom Arena
location: Boston, Massachusetts, USA
promotion: PWA
permalink: /events/2019-05-21 - PWA Tuesday Night Action 277/
tags:
- events
matches_json: [{"number": 1, "name": "Veteran Veteran Devastators vs. Los Rudos Diablos (w/The Gatekeeper)", "finish": "Fabrizio Tiziano beat El Experto in 11 Min 13 Sec with a Manovra Vittoria", "rating_stars": "<span class=\"stars\">★½</span>", "rating_num": 1.5, "time": "11:13"}, {"number": 2, "name": "PWA Junior Heavyweight Championship: Rey Horus. vs. Blu Blazer Jr. (c)", "finish": "Rey Horus beat Blue Blazer Jr. in 5 Min 40 Sec with a Firebird Splash", "rating_stars": "<span class=\"stars\">★★½</span>", "rating_num": 2.5, "time": "5:40"}, {"number": 3, "name": "Avery Alexander & Red Dragon vs. Roadkill & Salvador Sosa", "finish": "Avery Alexander beat Salvador Sosa in 7 Min 56 Sec with a RING OUT", "rating_stars": "<span class=\"stars\">★</span>", "rating_num": 1, "time": "7:56"}, {"number": 4, "name": "World Heavyweight Title #1 Contender: Falls Count Anywhere Match: Ox Hemlock vs. Rick Banner vs. Mr. Suplex", "finish": "Ox Hemlock won a triple threat match against Rick Banner & Mr. Suplex in  20:39", "rating_stars": "<span class=\"stars\">★★★½</span>", "rating_num": 3.5, "time": ""}]
---

# PWA Tuesday Night Action 277

<div class="event-header">
<div class="event-meta">
**Date:** 2019-05-21<br>
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