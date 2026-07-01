---
layout: event.njk
title: PWA Tuesday Night Action – The Gauntlet
date: '2018-04-24'
venue: ''
location: ''
promotion: PWA
permalink: /events/2018-04-24 - PWA Tuesday Night Action – The Gauntlet/
tags:
- events
matches_json: [{"number": 1, "name": "Hiroto Nakamichi vs. Tri Clops", "finish": "Tri Clops beat Hiroto Nakamichi (Hurricane Slam)", "rating_stars": "<span class=\"stars\">★★★★</span>", "rating_num": 4, "time": ""}, {"number": 2, "name": "Gauntlet Match: Blue Blazer Jr. (1.) & Keith Owens (2.) & Montgomery Hayes (4.) & UK Kid (3.) vs. Cobra (2.) & Cobra III (3.) & El Canek (4.) & Macho Especial (1.)", "finish": "El Canek won a Gauntlet Match -  Eliminations: 1. Blue Blazer Jr. by Macho Especial (3:4) 2. Keith Owens by Macho Especial (2:4) 3. Macho Especial by UK Kid (2:3) 4. UK Kid by Cobra (1:3) 5. Cobra by Mont. Hayes (1:2) 6. Cobra III by Mont. Hayes (Uproot Backdrop)(1:1) 7. Mont. Hayes by El Canek (Gorilla Lift Up Slam)(0:1))", "rating_stars": "<span class=\"stars\">★★★★★</span>", "rating_num": 5, "time": ""}]
---

# PWA Tuesday Night Action – The Gauntlet

<div class="event-header">
<div class="event-meta">
**Date:** 2018-04-24<br>
**Venue:** <br>
**Location:** 
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