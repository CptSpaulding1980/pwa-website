---
layout: event.njk
title: Professional Wrestling 1 (Debut Show)
date: '1982-01-01'
venue: The Vault
location: Boston, MA
promotion: PWA
permalink: /events/1982-01-01 - Professional Wrestling 1 (Debut Show)/
tags:
- events
matches_json: [{"number": 1, "name": "Bubba Bradley  vs. Clarence Coles", "finish": "Bubba Bradley beat Clarence Coles in 8 Min 22 Sec with a Head Pickup Lariat", "rating_stars": "<span class=\"stars\">★★</span>", "rating_num": 2, "time": "8:22"}, {"number": 2, "name": "Chayton White Wolf & John Taming Buck vs. Ernesto Marquez & Jose Murillo", "finish": "Chayton White Wolf beat Ernesto Marquez in 1 Min 41 Sec with a Diving Body Press", "rating_stars": "<span class=\"stars\">★</span>", "rating_num": 1, "time": "1:41"}, {"number": 3, "name": "Big Dragon vs. Bud Hemsworth", "finish": "Big Dragon beat Bud Hemsworth in 11 Min 34 Sec with a Muscle Bomb Press", "rating_stars": "<span class=\"stars\">★★★¾</span>", "rating_num": 3.75, "time": "11:34"}, {"number": 4, "name": "Paullus the Colussus vs. Jamie Norkus", "finish": "Paullus the Colossus beat Jamie Norkus in 3 Min 41 Sec with a Colossal Bearhug", "rating_stars": "<span class=\"stars\">★★</span>", "rating_num": 2, "time": "3:41"}, {"number": 5, "name": "Rocky Wilbur vs. Piotr Krutov", "finish": "Rocky Wilbur beat Piotr Krutov in 14 Min 2 Sec with a Chickenwing Facelock B", "rating_stars": "<span class=\"stars\">★★★</span>", "rating_num": 3, "time": "14:02"}, {"number": 6, "name": "CWC Heavyweight Championship: Harley Race vs. Roddy Piper (vacant)", "finish": "Harley Race beat Roddy Piper (CWC Heavyweight Championship) in 7 Min 44 Sec with a Japanese Leg Roll Clutch", "rating_stars": "<span class=\"stars\">★★</span>", "rating_num": 2, "time": "7:44"}]
---

# Professional Wrestling 1 (Debut Show)

<div class="event-header">
<div class="event-meta">
**Date:** 1982-01-01<br>
**Venue:** The Vault<br>
**Location:** Boston, MA
</div>
<img src="/pwa-website/img/posters/1982-01-01 - Professional Wrestling 1 (Debut Show).png" class="event-poster" alt="Poster">
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