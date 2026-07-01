---
layout: event.njk
title: PWA King of the Ring 2017
date: '2017-06-03'
venue: ''
location: ''
promotion: PWA
permalink: /events/2017-06-03 - PWA King of the Ring 2017/
tags:
- events
matches_json: [{"number": 1, "name": "King of the Ring – Quarter Final #1: Zack Sabre Jr. vs. Lance Archer", "finish": "Zack Sabre Jr. beat Lance Archer (Tiger Suplex)", "rating_stars": "<span class=\"stars\">★★★¾</span>", "rating_num": 3.75, "time": ""}, {"number": 2, "name": "King of the Ring – Quarter Final #2: Matt Riddle vs. Ray Stantz", "finish": "Ray Stantz beat Matt Riddle (Neckbreaker Drop)", "rating_stars": "<span class=\"stars\">★★★½</span>", "rating_num": 3.5, "time": ""}, {"number": 3, "name": "King of the Ring – Quarter Final #3: Blade vs. Brian Cage", "finish": "Blade beat Brian Cage (Double Count Out 9:30 Chokeslam (CRITICAL) 17:43)", "rating_stars": "<span class=\"stars\">★★★½</span>", "rating_num": 3.5, "time": ""}, {"number": 4, "name": "King of the Ring – Quarter Final #4: Fred Balentine vs. Prince Puma", "finish": "Fred Balentine beat Prince Puma (The Hammer)", "rating_stars": "<span class=\"stars\">★★★¾</span>", "rating_num": 3.75, "time": ""}, {"number": 5, "name": "Tornado - No Holds Barred - Landmine Deathmatch - PWA World Tag Team Championship: Davey Richards & Eddie Edwards vs. El Canek & Grizzlor (c)", "finish": "Davey Richards & Eddie Edwards beat El Canek & Grizzlor (Key Lock (Richards an Grizzlor))", "rating_stars": "<span class=\"stars\">★★★½</span>", "rating_num": 3.5, "time": ""}, {"number": 6, "name": "King of the Ring - Semi Final #1: Zack Sabre Jr. vs. Ray Stantz", "finish": "Zack Sabre Jr. beat Ray Stantz (Flying Cross Armbreaker)", "rating_stars": "<span class=\"stars\">★★★★¼</span>", "rating_num": 4.25, "time": ""}, {"number": 7, "name": "King of the Ring - Semi Final #2: Blade vs. Fred Balentine", "finish": "Blade beat Fred Balentine (Low Blow)", "rating_stars": "<span class=\"stars\">★★★★</span>", "rating_num": 4, "time": ""}, {"number": 8, "name": "PWA World Heavyweight Championship: Roadkill vs. Jack Swagger (c)", "finish": "Roadkill beat Jack Swagger (Striking Piledriver)", "rating_stars": "<span class=\"stars\">★★★¼</span>", "rating_num": 3.25, "time": ""}, {"number": 9, "name": "King of the Ring - Final: Zack Sabre Jr. vs. Blade", "finish": "Zack Sabre Jr. beat Blade (Powerbomb into Sunset Flip Konter)", "rating_stars": "<span class=\"stars\">★★★★½</span>", "rating_num": 4.5, "time": ""}]
---

# PWA King of the Ring 2017

<div class="event-header">
<div class="event-meta">
**Date:** 2017-06-03<br>
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