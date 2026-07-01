---
layout: event.njk
title: Professional Wrestling 22
date: '1993-09-10'
venue: ''
location: ''
promotion: PWA
permalink: /events/1993-09-10 - Professional Wrestling 22/
tags:
- events
matches_json: [{"number": 1, "name": "Fred Balentine vs. Lex Rider", "finish": "Lex Rider beat Fred Balentine in 16 Min 36 Sec with a Flying Forearm", "rating_stars": "<span class=\"stars\">★★★¾</span>", "rating_num": 3.75, "time": "16:36"}]
---

# Professional Wrestling 22

<div class="event-header">
<div class="event-meta">
**Date:** 1993-09-10<br>
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