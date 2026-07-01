---
layout: event.njk
title: PWA Power Hour 5
date: '2019-02-28'
venue: PWA Power Studio
location: Boston, Massachusetts, USA
promotion: PWA
permalink: /events/2019-02-28 - PWA Power Hour 5/
tags:
- events
matches_json: [{"number": 1, "name": "Skullface Killah (w/Brutes) vs. El Canek (w/Cobra III)", "finish": "Skullface Killah beat El Canek in 6 Min 29 Sec with a Kill You Dead", "rating_stars": "<span class=\"stars\">★★★¼</span>", "rating_num": 3.25, "time": "6:29"}, {"number": 2, "name": "Hiroto Nakamichi vs. Fantasio Fantastico", "finish": "Fantasio Fantastico beat Hiroto Nakamichi in 5 Min 34 Sec with a Fantasía Delirante", "rating_stars": "<span class=\"stars\">★★½</span>", "rating_num": 2.5, "time": "5:34"}, {"number": 3, "name": "Ox Hemlock vs. Ricklon Smasher", "finish": "Ox Hemlock beat Ricklon Smasher in 6 Min 30 Sec with a Choke Sleeper", "rating_stars": "<span class=\"stars\">★★★</span>", "rating_num": 3, "time": "6:30"}]
---

# PWA Power Hour 5

<div class="event-header">
<div class="event-meta">
**Date:** 2019-02-28<br>
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