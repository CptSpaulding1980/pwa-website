---
layout: event.njk
title: PWA Tuesday Night Action
date: '2017-06-06'
venue: ''
location: ''
promotion: PWA
permalink: /events/2017-06-06 - PWA Tuesday Night Action/
tags:
- events
matches_json: [{"number": 1, "name": "Steel Cage Match: Brian Cage & Davey Richards & Eddie Edwards vs. Big Dragon & El Canek & Grizzlor", "finish": "Big Dragon & El Canek & Grizzlor beat Brian Cage & Davey Richards & Eddie Edwards (Choke Slam (Grizzlor an Richards))", "rating_stars": "<span class=\"stars\">★★★¾</span>", "rating_num": 3.75, "time": ""}, {"number": 2, "name": "British Strong Style (Pete Dunne & Trent Seven & Tyler Bate) vs. Blue Blazer Jr. & Cobra III & Shredder", "finish": "Blue Blazer Jr. & Cobra III & Shredder beat British Strong Style (Pete Dunne & Trent Seven & Tyler Bate) (Small Package (Shredder an Tyler Bate))", "rating_stars": "<span class=\"stars\">★★★★¼</span>", "rating_num": 4.25, "time": ""}]
---

# PWA Tuesday Night Action

<div class="event-header">
<div class="event-meta">
**Date:** 2017-06-06<br>
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