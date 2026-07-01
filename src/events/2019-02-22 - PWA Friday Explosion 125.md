---
layout: event.njk
title: PWA Friday Explosion 125
date: '2019-02-22'
venue: Portland Memorial Coliseum
location: Portland, Oregon, USA
promotion: PWA
permalink: /events/2019-02-22 - PWA Friday Explosion 125/
tags:
- events
matches_json: [{"number": 1, "name": "Mackenzie Bergeron (w/The Gatekeeper) vs. Salvador Sosa", "finish": "Mackenzie Bergeron beat Salvador Sosa in 14 Min 43 Sec with an Ankle Hold", "rating_stars": "<span class=\"stars\">★★★★½</span>", "rating_num": 4.5, "time": "14:43"}, {"number": 2, "name": "Yokosumo Kawashi vs. Julio Rivera", "finish": "Yokosumo Kawashi beat Julio Rivera in 5 Min 58 Sec with a Hip Drop", "rating_stars": "<span class=\"stars\">★★</span>", "rating_num": 2, "time": "5:58"}, {"number": 3, "name": "Masked Maniac IV & Spitfire vs. Misterio Guerrero & Theobold Lovecraft", "finish": "Misterio Guerrero beat Masked Maniac IV in 1 Min 33 Sec with a Mystery Splash", "rating_stars": "<span class=\"stars\">★</span>", "rating_num": 1, "time": "1:33"}, {"number": 4, "name": "Diablo Blanco, El Experto & Golden Grappler vs. Blue Demon Jr., Blue Spider & Macho Especial", "finish": "Diablo Blanco, El Experto, & Golden Grappler battled Blue Demon Jr.,  Blue Spider, & Macho Especial to a  time limit draw", "rating_stars": "<span class=\"stars\">★★★★</span>", "rating_num": 4, "time": ""}]
---

# PWA Friday Explosion 125

<div class="event-header">
<div class="event-meta">
**Date:** 2019-02-22<br>
**Venue:** Portland Memorial Coliseum<br>
**Location:** Portland, Oregon, USA
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