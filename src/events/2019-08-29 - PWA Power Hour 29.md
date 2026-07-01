---
layout: event.njk
title: PWA Power Hour 29
date: '2019-08-29'
venue: Prudential Center
location: Newark, New Jersey, USA
promotion: PWA
permalink: /events/2019-08-29 - PWA Power Hour 29/
tags:
- events
matches_json: [{"number": 1, "name": "Bran Czlimovic vs. Jack Gold", "finish": "Jack Gold beat Bran Czlimovic in 10 Min 44 Sec with a RING OUT", "rating_stars": "<span class=\"stars\">★★★</span>", "rating_num": 3, "time": "10:44"}, {"number": 2, "name": "Yuji Ishikawa vs. Nigel Pendragon", "finish": "Nigel Pendragon beat Yuji Ishikawa in 17 Min 21 Sec with a Cardiff Dragon Sleeper", "rating_stars": "<span class=\"stars\">★★★½</span>", "rating_num": 3.5, "time": "17:21"}, {"number": 3, "name": "Tri Clops vs. Aramís", "finish": "Tri Clops beat Aramís in 8 Min 19 Sec with a Flying Cross Armbreaker", "rating_stars": "<span class=\"stars\">★★½</span>", "rating_num": 2.5, "time": "8:19"}]
---

# PWA Power Hour 29

<div class="event-header">
<div class="event-meta">
**Date:** 2019-08-29<br>
**Venue:** Prudential Center<br>
**Location:** Newark, New Jersey, USA
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