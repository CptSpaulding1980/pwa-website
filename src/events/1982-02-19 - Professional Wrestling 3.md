---
layout: event.njk
title: Professional Wrestling 3
date: '1982-02-19'
venue: The Vault
location: Boston, MA
promotion: PWA
permalink: /events/1982-02-19 - Professional Wrestling 3/
tags:
- events
matches_json: [{"number": 1, "name": "Big Dragon vs. Clarence Coles", "finish": "Big Dragon beat Clarence Coles in 2 Min 5 Sec with a Dragon Sleeper", "rating_stars": "<span class=\"stars\">★</span>", "rating_num": 1, "time": "2:05"}, {"number": 2, "name": "Bud Hemsworth vs. Piotr Krutov", "finish": "Bud Hemsworth beat Piotr Krutov in 13 Min 18 Sec", "rating_stars": "<span class=\"stars\">★★★¼</span>", "rating_num": 3.25, "time": "13:18"}, {"number": 3, "name": "Preston Toddsworth vs. Rocky Wilbur", "finish": "Rocky Wilbur beat Preston Toddsworth in 30 Min 0 Sec", "rating_stars": "<span class=\"stars\">★★★★¼</span>", "rating_num": 4.25, "time": "30:00"}]
---

# Professional Wrestling 3

<div class="event-header">
<div class="event-meta">
**Date:** 1982-02-19<br>
**Venue:** The Vault<br>
**Location:** Boston, MA
</div>
<img src="/pwa-website/img/posters/1982-02-19 - Professional Wrestling 3.png" class="event-poster" alt="Poster">
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