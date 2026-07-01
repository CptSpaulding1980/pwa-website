---
layout: event.njk
title: PWA Tuesday Night Action
date: '2016-05-17'
venue: ''
location: ''
promotion: PWA
permalink: /events/2016-05-17 - PWA Tuesday Night Action/
tags:
- events
matches_json: [{"number": 1, "name": "King of the Ring - First Round Match: Tri Clops vs. Christopher Daniels", "finish": "Tri Clops beat Christopher Daniels (Jumping Brainbuster)", "rating_stars": "<span class=\"stars\">★★★¾</span>", "rating_num": 3.75, "time": ""}, {"number": 2, "name": "King of the Ring - Quarter Final Match: Ray Stantz vs. Mark Erickson", "finish": "Mark Erickson beat Ray Stantz (Sniper Cross Face)", "rating_stars": "<span class=\"stars\">★★★★</span>", "rating_num": 4, "time": ""}, {"number": 3, "name": "King of the Ring - Quarter Final Match: Tri Clops vs. Great Sasuke", "finish": "Great Sasuke beat Tri Clops (Vert. Fire Powerbomb)", "rating_stars": "<span class=\"stars\">★★★½</span>", "rating_num": 3.5, "time": ""}]
---

# PWA Tuesday Night Action

<div class="event-header">
<div class="event-meta">
**Date:** 2016-05-17<br>
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