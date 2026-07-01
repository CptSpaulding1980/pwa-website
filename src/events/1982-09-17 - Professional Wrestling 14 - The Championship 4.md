---
layout: event.njk
title: Professional Wrestling 14 - The Championship 4
date: '1982-09-17'
venue: Korakuen Hall
location: Tokyo, Japan
promotion: PWA
permalink: /events/1982-09-17 - Professional Wrestling 14 - The Championship 4/
tags:
- events
matches_json: [{"number": 1, "name": "Dr. Angulo vs. Billy Fender", "finish": "Dr. Angulo beat Billy Fender with a Leg Cross Flying Rollup Pin in 13 Min 41 Sec", "rating_stars": "<span class=\"stars\">★★★¼</span>", "rating_num": 3.25, "time": "13:41"}, {"number": 2, "name": "PWA World Title Tournament Final - PWA World Heavyweight Championship: Dory Funk Jr. vs. Rocky Wilbur (vacant)", "finish": "Dory Funk Jr. beat Rocky Wilbur with a Spinning Toe Hold in 24 Min 19 Sec", "rating_stars": "<span class=\"stars\">★★★★</span>", "rating_num": 4, "time": "24:19"}]
---

# Professional Wrestling 14 - The Championship 4

<div class="event-header">
<div class="event-meta">
**Date:** 1982-09-17<br>
**Venue:** Korakuen Hall<br>
**Location:** Tokyo, Japan
</div>
<img src="/pwa-website/img/posters/1982-09-17 - Professional Wrestling 14 - The Championship 4.png" class="event-poster" alt="Poster">
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