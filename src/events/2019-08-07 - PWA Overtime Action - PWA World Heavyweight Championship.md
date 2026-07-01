---
layout: event.njk
title: PWA Overtime Action - PWA World Heavyweight Championship
date: '2019-08-07'
venue: PWA Power Studio
location: Boston, Massachusetts, USA
promotion: PWA
permalink: /events/2019-08-07 - PWA Overtime Action - PWA World Heavyweight Championship/
tags:
- events
matches_json: [{"number": 1, "name": "Empty Arena - Falls Count Anywhere - Texas Death Match - PWA World Heavyweight Championship: Fred Balentine vs. Ox Hemlock (c)", "finish": "Fred Balentine beat Ox Hemlock in a Falls Count Anywhere Texas Death Match in 41 Min 16 Sec with a 10 Count by the Referee", "rating_stars": "<span class=\"stars\">★★★★¾</span>", "rating_num": 4.75, "time": "41:16"}]
---

# PWA Overtime Action - PWA World Heavyweight Championship

<div class="event-header">
<div class="event-meta">
**Date:** 2019-08-07<br>
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