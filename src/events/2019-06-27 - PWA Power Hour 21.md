---
layout: event.njk
title: PWA Power Hour 21
date: '2019-06-27'
venue: PWA Power Studio
location: Boston, Massachusetts, USA
promotion: PWA
permalink: /events/2019-06-27 - PWA Power Hour 21/
tags:
- events
matches_json: [{"number": 1, "name": "Julio Rivera & Salvador Sosa vs. Santana Family", "finish": "Julio Rivera & Salvador Sosa battled Santana Family to a  time limit draw", "rating_stars": "<span class=\"stars\">★★★¾</span>", "rating_num": 3.75, "time": ""}, {"number": 2, "name": "Golden Grappler vs. Saburo Aoki Jr.", "finish": "Golden Grappler battled Saburo Aoki Jr. to a  time limit draw", "rating_stars": "<span class=\"stars\">★★★½</span>", "rating_num": 3.5, "time": ""}, {"number": 3, "name": "Nigel Pendragon vs. Damon Smith", "finish": "Damon Smith beat Nigel Pendragon in 9 Min 12 Sec with a Reverse Achilles Hold", "rating_stars": "<span class=\"stars\">★★★¼</span>", "rating_num": 3.25, "time": "9:12"}, {"number": 4, "name": "Mackenzie Bergeron vs. Misterio Guerrero", "finish": "Mackenzie Bergeron beat Misterio Guerrero in 20 Min 46 Sec with a Séparateur de Jambe", "rating_stars": "<span class=\"stars\">★★★★¼</span>", "rating_num": 4.25, "time": "20:46"}, {"number": 5, "name": "Non Title Match: Los Ingobernables (Andrade El Idolo & Rush) vs. Masked Lucha Alliance", "finish": "Andrade El Idolo beat Cobra III in 23 Min 46 Sec with a Green Killer", "rating_stars": "<span class=\"stars\">★★★★½</span>", "rating_num": 4.5, "time": "23:46"}]
---

# PWA Power Hour 21

<div class="event-header">
<div class="event-meta">
**Date:** 2019-06-27<br>
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