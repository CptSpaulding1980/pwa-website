---
layout: event.njk
title: PWA Royal Brawl 1996
date: '1996-01-22'
venue: ''
location: ''
promotion: PWA
permalink: /events/1996-01-22 - PWA Royal Brawl 1996/
tags:
- events
matches_json: [{"number": 1, "name": "PWA World Title #1 Contender Battle Royal", "finish": "Blade eliminates 19 other Wrestlers in 57 Min 09 Sec", "rating_stars": "<span class=\"stars\">★★★¾</span>", "rating_num": 3.75, "time": "57:09"}, {"number": 2, "name": "Inaugural Tournament Finals - PWA International Championship: Lex Rider vs. Roadkill (vacant)", "finish": "Lex Rider beat Roadkill in 22 Min 45 Sec with a Top Rope Reverse Flying Forearm", "rating_stars": "<span class=\"stars\">★★★★¼</span>", "rating_num": 4.25, "time": "22:45"}]
---

# PWA Royal Brawl 1996

<div class="event-header">
<div class="event-meta">
**Date:** 1996-01-22<br>
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