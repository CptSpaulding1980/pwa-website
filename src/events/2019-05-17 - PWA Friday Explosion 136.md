---
layout: event.njk
title: PWA Friday Explosion 136
date: '2019-05-17'
venue: PWA Capcom Arena
location: Boston, Massachusetts, USA
promotion: PWA
permalink: /events/2019-05-17 - PWA Friday Explosion 136/
tags:
- events
matches_json: [{"number": 1, "name": "Hiroto Nakamichi vs. Felix Santana III", "finish": "Hiroto Nakamichi beat Felix Santana III in 7 Min 33 Sec with a Rising Sun Stretch", "rating_stars": "<span class=\"stars\">★½</span>", "rating_num": 1.5, "time": "7:33"}, {"number": 2, "name": "Fabrizio Tiziano (w/The Gatekeeper) vs. Keith Rowans", "finish": "Keith Rowans beat Fabrizio Tiziano in 12 Min 29 Sec with a Low Missile Kick", "rating_stars": "<span class=\"stars\">★★★½</span>", "rating_num": 3.5, "time": "12:29"}, {"number": 3, "name": "Mike Hool (w/Brutes) vs. Cobra III (w/Macho Especial)", "finish": "Mike Hool beat Cobra III in 8 Min 9 Sec with a King Kong Knee Drop", "rating_stars": "<span class=\"stars\">★½</span>", "rating_num": 1.5, "time": "8:09"}, {"number": 4, "name": "European Rules Match: Victor Kurilenko vs. Theobold Lovecraft (w/Tri Clops)", "finish": "Theobold Lovecraft beat Victor Kurilenko in 2R 2 Min 17 Sec with a K.O", "rating_stars": "<span class=\"stars\">★★★½</span>", "rating_num": 3.5, "time": "2:17"}]
---

# PWA Friday Explosion 136

<div class="event-header">
<div class="event-meta">
**Date:** 2019-05-17<br>
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