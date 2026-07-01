---
layout: event.njk
title: PWA Power Hour 2
date: '2019-02-07'
venue: PWA Power Studios
location: Boston, Massachusetts, USA
promotion: PWA
permalink: /events/2019-02-07 - PWA Power Hour 2/
tags:
- events
matches_json: [{"number": 1, "name": "Trevor Murdoch vs. Dynamite Smith", "finish": "Trevor Murdoch beat Dynamite Smith in 7 Min 30 Sec with a K.O", "rating_stars": "<span class=\"stars\">★★★</span>", "rating_num": 3, "time": "7:30"}, {"number": 2, "name": "Shredder vs. Nigel Pendragon", "finish": "Nigel Pendragon beat Shredder in 2 Min 24 Sec with an Original German Suplex", "rating_stars": "<span class=\"stars\">★½</span>", "rating_num": 1.5, "time": "2:24"}, {"number": 3, "name": "Tag Title #1 Cont. Tournament - Quarter Finals: Go Shiozaki & Katsuhiko Nakajima vs. Foreign Fanatics", "finish": "Go Shiozaki beat Hiroto Nakamichi in 12 Min 30 Sec with a Short-Range Lariat", "rating_stars": "<span class=\"stars\">★★★★</span>", "rating_num": 4, "time": "12:30"}]
---

# PWA Power Hour 2

<div class="event-header">
<div class="event-meta">
**Date:** 2019-02-07<br>
**Venue:** PWA Power Studios<br>
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