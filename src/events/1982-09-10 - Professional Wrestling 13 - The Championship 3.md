---
layout: event.njk
title: Professional Wrestling 13 - The Championship 3
date: '1982-09-10'
venue: Korakuen Hall
location: Tokyo, Japan
promotion: PWA
permalink: /events/1982-09-10 - Professional Wrestling 13 - The Championship 3/
tags:
- events
matches_json: [{"number": 1, "name": "PWA World Title Tournament - Semi Finals: Mil Mascaras vs. Rocky Wilbur", "finish": "Rocky Wilbur beat Mil Mascaras with a Neck Throw Headlock in 43 Min 49 Sec", "rating_stars": "<span class=\"stars\">★★★★★</span>", "rating_num": 5, "time": "43:49"}, {"number": 2, "name": "PWA World Title Tournament - Semi Finals: Dory Funk Jr. vs. Nick Bockwinkel", "finish": "Dory Funk Jr. beat Nick Bockwinkel with a Backdrop in 21 Min 50 Sec", "rating_stars": "<span class=\"stars\">★★★¼</span>", "rating_num": 3.25, "time": "21:50"}]
---

# Professional Wrestling 13 - The Championship 3

<div class="event-header">
<div class="event-meta">
**Date:** 1982-09-10<br>
**Venue:** Korakuen Hall<br>
**Location:** Tokyo, Japan
</div>
<img src="/pwa-website/img/posters/1982-09-10 - Professional Wrestling 13 - The Championship 3.png" class="event-poster" alt="Poster">
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