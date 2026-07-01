---
layout: event.njk
title: PWA Tuesday Night Action
date: '2017-03-06'
venue: ''
location: ''
promotion: PWA
permalink: /events/2017-03-06 - PWA Tuesday Night Action/
tags:
- events
matches_json: [{"number": 1, "name": "PWA Junior Heavyweight Title Qualifying: Tyler Bate vs. Zack Sabre Jr.", "finish": "Zack Sabre Jr. beat Tyler Bate (Jap. Leg Roll Clutch)", "rating_stars": "<span class=\"stars\">★★★★</span>", "rating_num": 4, "time": ""}, {"number": 2, "name": "Naomichi Marufuji vs. Zodiac", "finish": "Zodiac beat Naomichi Marufuji (Running Spear)", "rating_stars": "<span class=\"stars\">★★★¾</span>", "rating_num": 3.75, "time": ""}, {"number": 3, "name": "Steel Cage Match: Cody Rhodes vs. Blue Spider", "finish": "Cody Rhodes beat Blue Spider (Cross Rhodes)", "rating_stars": "<span class=\"stars\">★★★¾</span>", "rating_num": 3.75, "time": ""}]
---

# PWA Tuesday Night Action

<div class="event-header">
<div class="event-meta">
**Date:** 2017-03-06<br>
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