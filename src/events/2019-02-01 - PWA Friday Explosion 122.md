---
layout: event.njk
title: PWA Friday Explosion 122
date: '2019-02-01'
venue: Worcester Centrum
location: Worcester, Massachusetts, USA
promotion: PWA
permalink: /events/2019-02-01 - PWA Friday Explosion 122/
tags:
- events
matches_json: [{"number": 1, "name": "Tag Title #1 Contender Tournament: Foreign Fanatics vs. Masked Lucha Alliance", "finish": "Hiroto Nakamichi beat Cobra  in 15 Min 17 Sec with a Rising Sun Stretch", "rating_stars": "<span class=\"stars\">★★★½</span>", "rating_num": 3.5, "time": "15:17"}, {"number": 2, "name": "Tag Title #1 Contender Tournament: Los Ingobernables vs. Jean Wilson & Ricklon Smasher", "finish": "SANADA beat Ricklon Smasher in 12 Min 48 Sec with a Rounding Body Press", "rating_stars": "<span class=\"stars\">★★★¾</span>", "rating_num": 3.75, "time": "12:48"}, {"number": 3, "name": "Tag Title #1 Contender Tournament: Go Shiozaki & Katsuhiko Nakajima vs. Nigel Pendragon & Mark Erickson", "finish": "Katsuhiko Nakajima beat Mark Erickson in 17 Min 15 Sec with a Shining High Kick", "rating_stars": "<span class=\"stars\">★★★¾</span>", "rating_num": 3.75, "time": "17:15"}, {"number": 4, "name": "Tag Title #1 Contender Tournament: Lifeblood (Bandido & Mark Haskins) vs. Mysterious Fantasticos", "finish": "Fantasio Fantastico beat Bandido in 22 Min 20 Sec with an Omoplata Crossface", "rating_stars": "<span class=\"stars\">★★★¾</span>", "rating_num": 3.75, "time": "22:20"}]
---

# PWA Friday Explosion 122

<div class="event-header">
<div class="event-meta">
**Date:** 2019-02-01<br>
**Venue:** Worcester Centrum<br>
**Location:** Worcester, Massachusetts, USA
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