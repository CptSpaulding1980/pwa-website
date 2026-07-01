---
layout: event.njk
title: PWA Tuesday Night Action 270 - Razorback Riot
date: '2019-04-02'
venue: PWA Capcom Arena
location: ''
promotion: PWA
permalink: /events/2019-04-02 - PWA Tuesday Night Action 270 - Razorback Riot/
tags:
- events
matches_json: [{"number": 1, "name": "Non Title Match: Blake Twins vs. Masked Lucha Alliance", "finish": "Cobra III beat Elias Blake in 26 Min 2 Sec with an Elbow Butt", "rating_stars": "<span class=\"stars\">★★★★¼</span>", "rating_num": 4.25, "time": "26:02"}, {"number": 2, "name": "El Hijo del Fantasma vs. Fantasio Fantastico", "finish": "El Hijo del Fantasma beat Fantasio Fantastico in 14 Min 21 Sec with a German Suplex", "rating_stars": "<span class=\"stars\">★★★½</span>", "rating_num": 3.5, "time": "14:21"}, {"number": 3, "name": "PWA Junior Heavyweight Championship: Blue Blazer Jr. vs. Felix Santana Jr. (c)", "finish": "Blue Blazer Jr. beat Felix Santana Jr. in 15 Min 10 Sec with a Moonsault Press", "rating_stars": "<span class=\"stars\">★★★¼</span>", "rating_num": 3.25, "time": "15:10"}, {"number": 4, "name": "Rick Banner vs. Roadkill", "finish": "Rick Banner and Roadkill battled to a double disqualification", "rating_stars": "<span class=\"stars\">★★★½</span>", "rating_num": 3.5, "time": ""}]
---

# PWA Tuesday Night Action 270 - Razorback Riot

<div class="event-header">
<div class="event-meta">
**Date:** 2019-04-02<br>
**Venue:** PWA Capcom Arena<br>
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