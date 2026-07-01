---
layout: event.njk
title: PWA Friday Explosion
date: '2016-05-13'
venue: ''
location: ''
promotion: PWA
permalink: /events/2016-05-13 - PWA Friday Explosion/
tags:
- events
matches_json: [{"number": 1, "name": "6 Men Tornado Tag Team - Steel Cage  Match: Blade & Jitsu & Takeshi Morishima vs. Fred Balentine & Naomichi Marufuji & Go Shiozaki", "finish": "Blade & Jitsu & Takeshi Morishima beat Fred Balentine & Naomichi Marufuji & Go Shiozaki (Bridge German Suplex (Jitsu an Balentine))", "rating_stars": "<span class=\"stars\">★★★½</span>", "rating_num": 3.5, "time": ""}]
---

# PWA Friday Explosion

<div class="event-header">
<div class="event-meta">
**Date:** 2016-05-13<br>
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