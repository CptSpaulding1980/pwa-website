---
layout: event.njk
title: PWA Friday Explosion 137 - The Final Episode
date: '2019-05-24'
venue: PWA Capcom Arena
location: Boston, Massachusetts, USA
promotion: PWA
permalink: /events/2019-05-24 - PWA Friday Explosion 137 - The Final Episode/
tags:
- events
matches_json: [{"number": 1, "name": "PWA Junior Heavyweight Championship: Blue Blazer Jr. vs. Rey Horus (c)", "finish": "Blue Blazer Jr. beat Rey Horus in 11 Min 0 Sec with a Sharpshooter", "rating_stars": "<span class=\"stars\">★½</span>", "rating_num": 1.5, "time": "11:00"}, {"number": 2, "name": "Casper Winkel vs. Jean Wilson", "finish": "Casper Winkel beat Jean Wilson in 18 Min 42 Sec with a Buffalo Sleeper", "rating_stars": "<span class=\"stars\">★★★¼</span>", "rating_num": 3.25, "time": "18:42"}, {"number": 3, "name": "European Rules: Victor Kurilenko vs. Theobold Lovecraft (w/Tri Clops)", "finish": "Theobold Lovecraft beat Victor Kurilenko in R 3 after 0 Min 56 Sec via Disqualification", "rating_stars": "<span class=\"stars\">★★★¼</span>", "rating_num": 3.25, "time": "0:56"}, {"number": 4, "name": "MexiSquad (Bandido & Flamita) vs. Blake Twins", "finish": "Elias Blake beat Flamita   in 21 Min 21 Sec with a Canadian Backbreaker", "rating_stars": "<span class=\"stars\">★★★★</span>", "rating_num": 4, "time": "21:21"}, {"number": 5, "name": "PWA International Championship: Roadkill vs. WALTER (c)", "finish": "Roadkill beat WALTER in 18 Min 8 Sec with a Mexican Stretch", "rating_stars": "<span class=\"stars\">★★★¾</span>", "rating_num": 3.75, "time": "18:08"}]
---

# PWA Friday Explosion 137 - The Final Episode

<div class="event-header">
<div class="event-meta">
**Date:** 2019-05-24<br>
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