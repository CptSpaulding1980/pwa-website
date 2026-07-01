---
layout: event.njk
title: Professional Wrestling - The Rematch
date: '1982-08-29'
venue: The Vault
location: Boston, MA
promotion: PWA
permalink: /events/1982-08-29 - Professional Wrestling - The Rematch/
tags:
- events
matches_json: [{"number": 1, "name": "PWA World Title Tournament: Dory Funk Jr. vs. The Destroyer", "finish": "Dory Funk Jr. beat The Destroyer in 33 Min 9 Sec with a Texas Suplex", "rating_stars": "<span class=\"stars\">★★★★¼</span>", "rating_num": 4.25, "time": "33:09"}]
---

# Professional Wrestling - The Rematch

<div class="event-header">
<div class="event-meta">
**Date:** 1982-08-29<br>
**Venue:** The Vault<br>
**Location:** Boston, MA
</div>
<img src="/pwa-website/img/posters/1982-08-29 - Professional Wrestling - The Rematch.png" class="event-poster" alt="Poster">
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