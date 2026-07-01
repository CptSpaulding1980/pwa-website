---
layout: event.njk
title: PWA Thanksgiving Thunder 2016
date: '2016-11-27'
venue: ''
location: ''
promotion: PWA
permalink: /events/2016-11-27 - PWA Thanksgiving Thunder 2016/
tags:
- events
matches_json: [{"number": 1, "name": "PWA World Tag Team Championship: The Patriot & Cobra III vs. Chris Hero & Claudio Castagnoli (c)", "finish": "Chris Hero & Claudio Castagnoli beat The Patriot & Cobra III (England Stretch (Hero an Patriot))", "rating_stars": "<span class=\"stars\">★★★¼</span>", "rating_num": 3.25, "time": ""}, {"number": 2, "name": "No Disqualification Match: Seth Ramsey vs. Jean Wilson", "finish": "Jean Wilson beat Seth Ramsey (Western Lariat (CRITICAL))", "rating_stars": "<span class=\"stars\">★★★¼</span>", "rating_num": 3.25, "time": ""}, {"number": 3, "name": "PWA International Championship: Mystery Panther vs. Roadkill (c)", "finish": "Roadkill beat Mystery Panther (German Suplex)", "rating_stars": "<span class=\"stars\">★★★¼</span>", "rating_num": 3.25, "time": ""}, {"number": 4, "name": "Dr. Wagner Jr. vs. Blue Spider", "finish": "Blue Spider beat Dr. Wagner Jr. (0:1 Onryo Clutch 21:19 1:1 Flying Rolling Pin 08:05 1:2 Moonsault nach Spider Suplex 05:03)", "rating_stars": "<span class=\"stars\">★★★¼</span>", "rating_num": 3.25, "time": ""}, {"number": 5, "name": "ROH World Championship: Tri Clops vs. Davey Richards (c)", "finish": "Davey Richards beat Tri Clops (Straight Arm Bar)", "rating_stars": "<span class=\"stars\">★★★★</span>", "rating_num": 4, "time": ""}, {"number": 6, "name": "PWA World Heavyweight Championship: Blade vs. Lex Rider (c)", "finish": "Lex Rider beat Blade (Frog Splash)", "rating_stars": "<span class=\"stars\">★★★¾</span>", "rating_num": 3.75, "time": ""}]
---

# PWA Thanksgiving Thunder 2016

<div class="event-header">
<div class="event-meta">
**Date:** 2016-11-27<br>
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