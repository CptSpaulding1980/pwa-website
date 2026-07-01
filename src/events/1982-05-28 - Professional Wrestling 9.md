---
layout: event.njk
title: Professional Wrestling 9
date: '1982-05-28'
venue: The Vault
location: Boston, MA
promotion: PWA
permalink: /events/1982-05-28 - Professional Wrestling 9/
tags:
- events
matches_json: [{"number": 1, "name": "PNCW United National Championship: Buddy Yorke vs. Count Rorstock (c)", "finish": "Count Rorstock drew Buddy Yorke in 30 Min. 0 Sec. to retain the PNCW United National Championship", "rating_stars": "<span class=\"stars\">★★★★</span>", "rating_num": 4, "time": ""}, {"number": 2, "name": "Billy Fender vs. Golden Grappler", "finish": "Billy Fender beat Golden Grappler in 28 Min 14 Sec with a an Original German Suplex", "rating_stars": "<span class=\"stars\">★★★¾</span>", "rating_num": 3.75, "time": "28:14"}]
---

# Professional Wrestling 9

<div class="event-header">
<div class="event-meta">
**Date:** 1982-05-28<br>
**Venue:** The Vault<br>
**Location:** Boston, MA
</div>
<img src="/pwa-website/img/posters/1982-05-28 - Professional Wrestling 9.png" class="event-poster" alt="Poster">
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