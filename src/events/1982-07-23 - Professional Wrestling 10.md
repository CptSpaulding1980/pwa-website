---
layout: event.njk
title: Professional Wrestling 10
date: '1982-07-23'
venue: The Vault
location: Boston, MA
promotion: PWA
permalink: /events/1982-07-23 - Professional Wrestling 10/
tags:
- events
matches_json: [{"number": 1, "name": "PNCW Pacific Heavyweight Championship: Lars Lundgren vs. Bob Harris (c)", "finish": "Bob Harris beat Rocky Wilbur in 30 Min 0 Sec with a Jumping Backbreaker", "rating_stars": "<span class=\"stars\">★★★★½</span>", "rating_num": 4.5, "time": "30:00"}]
---

# Professional Wrestling 10

<div class="event-header">
<div class="event-meta">
**Date:** 1982-07-23<br>
**Venue:** The Vault<br>
**Location:** Boston, MA
</div>
<img src="/pwa-website/img/posters/1982-07-23 - Professional Wrestling 10.png" class="event-poster" alt="Poster">
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