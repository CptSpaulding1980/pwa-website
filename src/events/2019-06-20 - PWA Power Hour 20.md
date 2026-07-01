---
layout: event.njk
title: PWA Power Hour 20
date: '2019-06-20'
venue: PWA Power Studio
location: Boston, Massachusetts, USA
promotion: PWA
permalink: /events/2019-06-20 - PWA Power Hour 20/
tags:
- events
matches_json: [{"number": 1, "name": "Veteran Veteran Devastators vs. Mysterious Fantasticos", "finish": "Blue Blazer Jr. beat Misterio Guerrero in 12 Min 27 Sec with a Sharpshooter", "rating_stars": "<span class=\"stars\">★★★★</span>", "rating_num": 4, "time": "12:27"}, {"number": 2, "name": "Allen Hawkins vs. Jack Gold", "finish": "Allen Hawkins beat Jack Gold in 13 Min 17 Sec with an Enzuigiri", "rating_stars": "<span class=\"stars\">★★★★¼</span>", "rating_num": 4.25, "time": "13:17"}, {"number": 3, "name": "Adamo Dragon (w/El Pulpo) vs. Poppa Thurgoode", "finish": "Adamo Dragon beat Poppa Thurgoode in 7 Min 4 Sec with a Canadian Destroyer", "rating_stars": "<span class=\"stars\">★★★★¼</span>", "rating_num": 4.25, "time": "7:04"}, {"number": 4, "name": "30 Minute Iron Man - PWA International Championship: Roadkill vs. John Hennigan (c)", "finish": "John Hennigan beat Roadkill in 30 Min 0 Sec with a Twisting Moonsault Press", "rating_stars": "<span class=\"stars\">★★★★</span>", "rating_num": 4, "time": "30:00"}]
---

# PWA Power Hour 20

<div class="event-header">
<div class="event-meta">
**Date:** 2019-06-20<br>
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