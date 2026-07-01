---
layout: event.njk
title: PWA Clash of Honor V
date: '1997-04-01'
venue: ''
location: ''
promotion: PWA
permalink: /events/1997-04-01 - PWA Clash of Honor V/
tags:
- events
matches_json: [{"number": 1, "name": "Triple Threat - PWA World Heavyweight Championship: Lex Rider vs. Fred Balentine vs. Tri Clops ©", "finish": "Lex Rider beats Tri Clops with a Frog Splash", "rating_stars": "<span class=\"stars\">★★★★</span>", "rating_num": 4, "time": ""}]
---

# PWA Clash of Honor V

<div class="event-header">
<div class="event-meta">
**Date:** 1997-04-01<br>
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