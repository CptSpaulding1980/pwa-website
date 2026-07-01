---
layout: event.njk
title: PWA Tuesday Night Action 284 - Ox running wild
date: '2019-07-15'
venue: PWA Capcom Arena
location: Boston, Massachusetts, USA
promotion: PWA
permalink: /events/2019-07-15 - PWA Tuesday Night Action 284 - Ox running wild/
tags:
- events
matches_json: [{"number": 1, "name": "Chelsea Grin vs. Saturn", "finish": "Chelsea Grin beat Saturn in 10 Min 56 Sec with a Butterfly Neck Lock", "rating_stars": "<span class=\"stars\">★★★½</span>", "rating_num": 3.5, "time": "10:56"}, {"number": 2, "name": "Invasores vs. Santana Family", "finish": "Medic 1 beat Felix Santana Jr. in 13 Min 51 Sec with a Diving Rolling Guillotine Drop", "rating_stars": "<span class=\"stars\">★★★</span>", "rating_num": 3, "time": "13:51"}, {"number": 3, "name": "Mackenzie Bergeron, Mr. Suplex & Blue Blazer Jr. vs. Los Rudos Diablos", "finish": "Mackenzie Bergeron beat The Gatekeeper in 20 Min 9 Sec with a Séparateur de Jambe", "rating_stars": "<span class=\"stars\">★★★</span>", "rating_num": 3, "time": "20:09"}, {"number": 4, "name": "Masked Maniac IV vs. Roadkill (w/Invasores)", "finish": "Roadkill beat Masked Maniac IV in 6 Min 13 Sec with a RING OUT", "rating_stars": "<span class=\"stars\">★½</span>", "rating_num": 1.5, "time": "6:13"}, {"number": 5, "name": "Tundra Wurm vs. Rick Banner", "finish": "Tundra Wurm beat Rick Banner in 5 Min 25 Sec with a Falling Lariat", "rating_stars": "<span class=\"stars\">★★</span>", "rating_num": 2, "time": "5:25"}]
---

# PWA Tuesday Night Action 284 - Ox running wild

<div class="event-header">
<div class="event-meta">
**Date:** 2019-07-15<br>
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