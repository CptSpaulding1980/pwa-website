---
layout: event.njk
title: PWA Tuesday Night Action
date: '2016-07-26'
venue: ''
location: ''
promotion: PWA
permalink: /events/2016-07-26 - PWA Tuesday Night Action/
tags:
- events
matches_json: [{"number": 1, "name": "PWA World Title #1 Contender Match: UK Kid vs. Steve Corino", "finish": "Steve Corino beat UK Kid (Figure Four Leglock)", "rating_stars": "<span class=\"stars\">★★★½</span>", "rating_num": 3.5, "time": ""}, {"number": 2, "name": "Snake King & Mike Hool & Zodiac vs. Cobra III & Mystery Panther & Shredder", "finish": "Snake King & Mike Hool & Zodiac beat Cobra III & Mystery Panther & Shredder (Fallaway Slam (Snake King an Cobra))", "rating_stars": "<span class=\"stars\">★★★½</span>", "rating_num": 3.5, "time": ""}]
---

# PWA Tuesday Night Action

<div class="event-header">
<div class="event-meta">
**Date:** 2016-07-26<br>
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