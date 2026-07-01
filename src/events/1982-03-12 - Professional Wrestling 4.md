---
layout: event.njk
title: Professional Wrestling 4
date: '1982-03-12'
venue: The Vault
location: Boston, MA
promotion: PWA
permalink: /events/1982-03-12 - Professional Wrestling 4/
tags:
- events
matches_json: [{"number": 1, "name": "John Taming Buck & Chayton White Wolf vs. Slavakov Nemchinov & Piotr Krutov", "finish": "John Taming Buck beat Slavakov Nemchinov in 7 Min 49 Sec", "rating_stars": "<span class=\"stars\">★½</span>", "rating_num": 1.5, "time": "7:49"}, {"number": 2, "name": "Antonio Antiguo vs. Diego Guerrero", "finish": "Diego Guerrero drew Antonio Antiguo in 15 Min. 0 Sec", "rating_stars": "<span class=\"stars\">★★★¾</span>", "rating_num": 3.75, "time": ""}, {"number": 3, "name": "Bernardo Barros vs. Joey Farrell", "finish": "Bernardo Barros beat Joey Farrell in 10 Min 25 Sec with a Hold Neck Lock", "rating_stars": "<span class=\"stars\">★½</span>", "rating_num": 1.5, "time": "10:25"}, {"number": 4, "name": "Best 2 out of 3 Falls: Preston Toddsworth vs. Rocky Wilbur", "finish": "Rocky Wilbur drew Preston Toddsworth 1 falls to 1 in 72 Min. 41 Sec", "rating_stars": "<span class=\"stars\">★★★★</span>", "rating_num": 4, "time": ""}]
---

# Professional Wrestling 4

<div class="event-header">
<div class="event-meta">
**Date:** 1982-03-12<br>
**Venue:** The Vault<br>
**Location:** Boston, MA
</div>
<img src="/pwa-website/img/posters/1982-03-12 - Professional Wrestling 4.png" class="event-poster" alt="Poster">
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