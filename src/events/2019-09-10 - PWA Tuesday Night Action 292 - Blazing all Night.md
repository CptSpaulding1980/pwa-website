---
layout: event.njk
title: PWA Tuesday Night Action 292 - Blazing all Night
date: '2019-09-10'
venue: PWA Capcom Arena
location: Boston, Massachusetts, USA
promotion: PWA
permalink: /events/2019-09-10 - PWA Tuesday Night Action 292 - Blazing all Night/
tags:
- events
matches_json: [{"number": 1, "name": "Blue Blazer Jr. vs. Julio Rivera", "finish": "Blue Blazer Jr. battled Julio Rivera to a  time limit draw", "rating_stars": "<span class=\"stars\">★★★★</span>", "rating_num": 4, "time": ""}, {"number": 2, "name": "Non Title Match: Allen Hawkins & Saburo Aoki Jr. vs. Cobra III & Macho Especial vs. ", "finish": "Cobra III & Macho Especial battled Allen Hawkins & Saburo Aoki Jr. to a  time limit draw", "rating_stars": "<span class=\"stars\">★★★¾</span>", "rating_num": 3.75, "time": ""}, {"number": 3, "name": "Avery Alexander vs. Poppa Thurgoode", "finish": "Avery Alexander beat Poppa Thurgoode in 14 Min 9 Sec with a Thunder Fire Powerbomb", "rating_stars": "<span class=\"stars\">★★★½</span>", "rating_num": 3.5, "time": "14:09"}, {"number": 4, "name": "Casper Winkel vs. Tri Clops", "finish": "Casper Winkel beat Tri Clops in 10 Min 58 Sec with a Buffalo Sleeper", "rating_stars": "<span class=\"stars\">★½</span>", "rating_num": 1.5, "time": "10:58"}]
---

# PWA Tuesday Night Action 292 - Blazing all Night

<div class="event-header">
<div class="event-meta">
**Date:** 2019-09-10<br>
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