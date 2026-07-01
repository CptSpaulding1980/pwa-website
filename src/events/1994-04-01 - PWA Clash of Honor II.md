---
layout: event.njk
title: PWA Clash of Honor II
date: '1994-04-01'
venue: ''
location: ''
promotion: PWA
permalink: /events/1994-04-01 - PWA Clash of Honor II/
tags:
- events
matches_json: [{"number": 1, "name": "PWA World Heavyweight Championship: Fred Balentine vs. Big Dragon (c)", "finish": "Fred Balentine beat Big Dragon in 21 Min 07 Sec with a Running DDT", "rating_stars": "<span class=\"stars\">★★★¾</span>", "rating_num": 3.75, "time": "21:07"}]
---

# PWA Clash of Honor II

<div class="event-header">
<div class="event-meta">
**Date:** 1994-04-01<br>
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