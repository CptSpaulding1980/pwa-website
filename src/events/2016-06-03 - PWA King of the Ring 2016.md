---
layout: event.njk
title: PWA King of the Ring 2016
date: '2016-06-03'
venue: ''
location: ''
promotion: PWA
permalink: /events/2016-06-03 - PWA King of the Ring 2016/
tags:
- events
matches_json: [{"number": 1, "name": "King of the Ring - Semi Final #1: Mark Erickson vs. Jean Wilson", "finish": "Jean Wilson beat Mark Erickson (Western Lariat)", "rating_stars": "<span class=\"stars\">★★★¼</span>", "rating_num": 3.25, "time": ""}, {"number": 2, "name": "King of the Ring - Semi Final #2: Go Shiozaki vs. Great Sasuke", "finish": "Go Shiozaki beat Great Sasuke (Striking Lariat)", "rating_stars": "<span class=\"stars\">★★★½</span>", "rating_num": 3.5, "time": ""}, {"number": 3, "name": "Best 2 out of 3 Falls Match - PWA International Championship: Blue Spider vs. Roadkill (c)", "finish": "Roadkill beat Blue Spider in 38 Min 11 Sec with 2:0 Falls (First Fall: Crossface 17:11; Second Fall: Half Boston Crab 21:00)", "rating_stars": "<span class=\"stars\">★★★★½</span>", "rating_num": 4.5, "time": "38:11"}, {"number": 4, "name": "Prince Devitt & Ryusuke Taguchi vs. Shredder & Delirious", "finish": "Prince Devitt & Ryusuke Taguchi beat Shredder & Delirious (Stomach Crusher (Devitt an Delirious))", "rating_stars": "<span class=\"stars\">★★★¾</span>", "rating_num": 3.75, "time": ""}, {"number": 5, "name": "Unsanctioned Street Fight - Loser Leaves Town: Blade vs. Fred Balentine", "finish": "Fred Balentine beat Blade (Shotgun)", "rating_stars": "<span class=\"stars\">★★★¼</span>", "rating_num": 3.25, "time": ""}, {"number": 6, "name": "King of the Ring - Final: Jean Wilson vs. Go Shiozaki", "finish": "Jean Wilson beat Go Shiozaki (Spinebuster)", "rating_stars": "<span class=\"stars\">★★★¼</span>", "rating_num": 3.25, "time": ""}, {"number": 7, "name": "PWA World Heavyweight Championship: UK Kid vs. Lex Rider (c)", "finish": "UK Kid beat Lex Rider in 25 Min 31 Sec with a RING OUT (nach Tombstone von Kid)", "rating_stars": "<span class=\"stars\">★★★★</span>", "rating_num": 4, "time": "25:31"}]
---

# PWA King of the Ring 2016

<div class="event-header">
<div class="event-meta">
**Date:** 2016-06-03<br>
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