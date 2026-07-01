---
layout: event.njk
title: Professional Wrestling 2
date: '1982-01-29'
venue: The Vault
location: Boston, MA
promotion: PWA
permalink: /events/1982-01-29 - Professional Wrestling 2/
tags:
- events
matches_json: [{"number": 1, "name": "Preston Toddsworth vs. Rocky Wilbur", "finish": "Preston Toddsworth beat Rocky Wilbur in 20 Min 17 Sec with a Diving Body Press", "rating_stars": "<span class=\"stars\">★★★★¼</span>", "rating_num": 4.25, "time": "20:17"}, {"number": 2, "name": "Paullus the Colossus vs. Ernesto Marquez", "finish": "Paullus the Colossus beat Ernesto Marquez in 1 Min 31 Sec with a Colossal Bearhug", "rating_stars": "<span class=\"stars\">★½</span>", "rating_num": 1.5, "time": "1:31"}, {"number": 3, "name": "Joey Farrell vs. Jamie Norkus", "finish": "Joey Farrell beat Jamie Norkus in 2 Min 44 Sec", "rating_stars": "<span class=\"stars\">DUD</span>", "rating_num": 0, "time": "2:44"}, {"number": 4, "name": "Piotr Krutov, Slavakow Nemchinov & Vasily Asimov vs. Bud Hemsworth, Chayton White Wolf & John Taming Buck", "finish": "Piotr Krutov beat Bud Hemsworth in 12 Min 35 Sec with a (74%)", "rating_stars": "<span class=\"stars\">★★★¼</span>", "rating_num": 3.25, "time": "12:35"}]
---

# Professional Wrestling 2

<div class="event-header">
<div class="event-meta">
**Date:** 1982-01-29<br>
**Venue:** The Vault<br>
**Location:** Boston, MA
</div>
<img src="/pwa-website/img/posters/1982-01-29 - Professional Wrestling 2.png" class="event-poster" alt="Poster">
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