---
layout: event.njk
title: PWA Tuesday Night Action – Lucha Special
date: '2017-12-05'
venue: ''
location: ''
promotion: PWA
permalink: /events/2017-12-05 - PWA Tuesday Night Action – Lucha Special/
tags:
- events
matches_json: [{"number": 1, "name": "Best 2 out of 3 Falls Match: Keith Owens & Blue Blazer Jr. & UK Kid vs. Cobra & Cobra III & El Canek", "finish": "Keith Owens & Blue Blazer Jr. & UK Kid beat Cobra & Cobra III & El Canek (1:0 German Suplex (Blue Blazer Jr. an El Canek) (22:37) 2:0 Top Rope Sunset Flip (Blue Blazer Jr. an El Canek) (50:41))", "rating_stars": "<span class=\"stars\">★★★★¾</span>", "rating_num": 4.75, "time": ""}, {"number": 2, "name": "Mil Muertes vs. Grizzlor", "finish": "Mil Muertes beat Grizzlor (Giant Choke Slam)", "rating_stars": "<span class=\"stars\">★★★¾</span>", "rating_num": 3.75, "time": ""}, {"number": 3, "name": "Caristico vs. Lex Rider", "finish": "Lex Rider beat Caristico (Frog Splash)", "rating_stars": "<span class=\"stars\">★★★¾</span>", "rating_num": 3.75, "time": ""}, {"number": 4, "name": "Non Title Match - Best 2 out of 3 Falls Match: Rey Mysterio Jr. vs. Roadkill (c)", "finish": "Rey Mysterio Jr. beat Roadkill (1:0 Swinging Frankensteiner (07:13) 1:1 Flying Body Attack (12:02) 2:1 Mysterious Rana (21:45))", "rating_stars": "<span class=\"stars\">★★★★¼</span>", "rating_num": 4.25, "time": ""}, {"number": 5, "name": "Best 2 out of 3 Falls Match - PWA World Heavyweight Championship: Rey Mysterio Jr. vs. Roadkill (c)", "finish": "Roadkill beat Rey Mysterio Jr. (0:1 Reverse Figure 4 (09:13) 0:2 Road Diving Elbow Drop (22:13))", "rating_stars": "<span class=\"stars\">★★★★</span>", "rating_num": 4, "time": ""}]
---

# PWA Tuesday Night Action – Lucha Special

<div class="event-header">
<div class="event-meta">
**Date:** 2017-12-05<br>
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