---
layout: event.njk
title: PWA Tuesday Night Action 279 - Grapple Heaven
date: '2019-06-04'
venue: PWA Capcom Arena
location: Boston, Massachusetts, USA
promotion: PWA
permalink: /events/2019-06-04 - PWA Tuesday Night Action 279 - Grapple Heaven/
tags:
- events
matches_json: [{"number": 1, "name": "Golden Grappler vs. Allen Hawkins vs. Saburo Aoki Jr.", "finish": "Golden Grappler won a triple threat match against Allen Hawkins & Saburo Aoki Jr. in  22:39", "rating_stars": "<span class=\"stars\">★★★</span>", "rating_num": 3, "time": ""}, {"number": 2, "name": "Jack Fury (w/Blade) vs. Mystery", "finish": "Tri Clops beat Jack Fury in 12 Min 45 Sec with a German Suplex", "rating_stars": "<span class=\"stars\">★★½</span>", "rating_num": 2.5, "time": "12:45"}, {"number": 3, "name": "SWA Rules: Victor Kurilenko vs. Theobold Lovecraft", "finish": "Victor Kurilenko beat Theobold Lovecraft in 4R 0 Min 10 Sec with a Choke Sleeper", "rating_stars": "<span class=\"stars\">★★★¾</span>", "rating_num": 3.75, "time": "0:10"}, {"number": 4, "name": "Winner gets Services of the Gatekeeper: Fabrizio Tiziano vs. Diablo Blanco", "finish": "Fabrizio Tiziano battled Diablo Blanco to a  time limit draw", "rating_stars": "<span class=\"stars\">★★</span>", "rating_num": 2, "time": ""}, {"number": 5, "name": "Veteran Veteran Devastators (Blue Blazer Jr. & Mackenzie Bergeron) & Mr. Suplex vs. Lex Rider, Rick Banner & Fred Balentine", "finish": "Lex Rider beat Mackenzie Bergeron in 20 Min 8 Sec with an Anaconda vice", "rating_stars": "<span class=\"stars\">★★★¼</span>", "rating_num": 3.25, "time": "20:08"}]
---

# PWA Tuesday Night Action 279 - Grapple Heaven

<div class="event-header">
<div class="event-meta">
**Date:** 2019-06-04<br>
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